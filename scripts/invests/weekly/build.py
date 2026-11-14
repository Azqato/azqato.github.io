"""Build the Weekly Investing Report page from one week's saved data.

Usage, from anywhere:  python scripts/invests/weekly/build.py 2026-11-13
Reads data/<friday>.json (written by fetch.py), renders every section, fills
template.html with them and the popups in explain.html, and writes
invests/weekly/index.html. Changes nothing else.

The page is roadmap item 23 in docs/PRD.md: an unlisted preview (noindex, no
links to it, not in the sitemaps) that Claude Code updates when the owner asks.

The labels follow the Index & ETF Method page (invests/indices/method.html):
the VIX and AAII action levels, the three technical timing signals, the
combined AAII and VIX tiers, and the "What Strong Signals Look Like" table.
Where the method leaves a band undefined, the owner approved these fills
(2026-11-14): RSI 60 to 70 "Elevated", 52-week range 75 to 90% "Upper",
within 2% of the 200-day average "Average". Every label is one word. The
report describes; it gives no posture or advice (owner's rule), so it shows the
method's "What It Signals" text but never its "Recommended Posture".
"""
import datetime as dt, html, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
OUT = ROOT / "invests" / "weekly" / "index.html"
METHOD = "../indices/method.html"

# ---------------------------------------------------------------- the method's rules
# Each band: (upper bound, label, signal, range text). Signal is the method's
# "What Strong Signals Look Like" column: strong, neutral or caution.
VIX_BANDS = [(15, "Complacent", "caution", "below 15"), (25, "Moderate", "neutral", "15 to 25"),
             (35, "Elevated", "neutral", "25 to 35"), (45, "High", "strong", "35 to 45"),
             (999, "Crisis", "strong", "above 45")]
VIX_SAYS = {  # the method's "What It Signals" column, word for word
    "Complacent": "Investors are not pricing in risk. Protective positioning is minimal. Assets are likely priced near cyclical highs.",
    "Moderate": "Normal to moderately elevated uncertainty. Some hedging activity. This is the typical backdrop for equity markets over most of any given year.",
    "Elevated": "Meaningful uncertainty or a developing correction. Quality assets are being sold alongside weaker ones. Forced selling may be beginning.",
    "High": "Widespread panic. Markets are pricing in scenarios that often do not fully materialize. Most near-term bad news is already reflected in prices. Historically one of the most reliable entry windows.",
    "Crisis": "Acute market stress. Liquidity events, forced de-leveraging, or systemic fear. These moments are rare (roughly once per decade) and historically represent the highest-conviction long entry in the market cycle.",
}
AAII_BANDS = [(25, "Optimism", "caution", "below 25%"), (35, "Average", "neutral", "25 to 35%"),
              (50, "Concern", "neutral", "35 to 50%"), (60, "Fear", "neutral", "50 to 60%"),
              (999, "Extreme", "strong", "above 60%")]
AAII_SAYS = {
    "Optimism": "Retail investors are overwhelmingly bullish. Most equity exposure has already been deployed. Few buyers remain to push prices meaningfully higher. March 2000 is the clearest historical example at ~17% bearish.",
    "Average": "Near the long-run baseline of approximately 31% bearish. No significant contrarian signal in either direction. Conditions are within the normal range of investor sentiment.",
    "Concern": "Sentiment is drifting above the historical average. Investors are becoming cautious. Prices and sentiment are beginning to diverge from the bullish zone.",
    "Fear": "More investors expect a market decline than at any point in the historical average range. This level has historically preceded meaningful recoveries across multiple cycles, including December 2018 and February 2003.",
    "Extreme": "Readings above 60% are historically rare and have clustered at or near major market bottoms: 2009 (~70%), 2022 (~61%), 2025 (~61%). Retail investors are at or near maximum pessimism. The selling is largely exhausted.",
}
# RSI: the method's table marks 30 to 45 as the strong range; below 30 it calls
# "deep oversold, high conviction", so both count as strong here.
RSI_BANDS = [(30, "Oversold", "strong"), (45.0001, "Pullback", "strong"), (60, "Neutral", "neutral"),
             (70.0001, "Elevated", "neutral"), (999, "Overbought", "caution")]
POS_BANDS = [(25, "Lower", "strong"), (75.0001, "Middle", "neutral"), (90, "Upper", "neutral"), (999, "High", "caution")]
MA_BANDS = [(-2, "Below", "caution"), (2.0001, "Average", "neutral"), (999, "Above", "strong")]
TIERS = {0: ("None", "Neither VIX above 25 nor AAII bearishness above 50%."),
         1: ("Moderate", "Either VIX above 25, or AAII bearishness above 50%."),
         2: ("Strong", "VIX above 35 and AAII bearishness above 55%."),
         3: ("Maximum", "VIX above 45 and AAII bearishness above 60%.")}
SIG = {"strong": "Strong", "neutral": "Neutral", "caution": "Caution"}


def band(v, bands):
    for b in bands:
        if v < b[0]:
            return b
    return bands[-1]


def vix_band(v):
    b = band(v, VIX_BANDS)
    sig = "strong" if v > 35 else "caution" if v < 15 else "neutral"
    return b[1], sig, b[3]


def aaii_band(bear):
    b = band(bear, AAII_BANDS)
    sig = "strong" if bear > 60 else "caution" if bear < 25 else "neutral"
    return b[1], sig, b[3]


def tier(vix, bear):
    if vix > 45 and bear > 60:
        return 3
    if vix > 35 and bear > 55:
        return 2
    if vix > 25 or bear > 50:
        return 1
    return 0


def fund_signals(r, vsig, asig):
    t = r["tech"]
    # Labels use the numbers as the page shows them (RSI and range to whole
    # numbers, the 200-day gap to one decimal), so a shown 75% is never "Middle".
    out = {"rsi": band(round(t["rsi"]), RSI_BANDS)[1:] if t["rsi"] is not None else None,
           "pos": band(round(t["pos"]), POS_BANDS)[1:] if t["pos"] is not None else None,
           "ma": band(round(t["ma200"], 1), MA_BANDS)[1:] if t["ma200"] is not None else None}
    sigs = [vsig, asig] + [v[1] for v in out.values() if v]
    out["strong"] = sum(s == "strong" for s in sigs)
    out["caution"] = sum(s == "caution" for s in sigs)
    return out


# ---------------------------------------------------------------- formatting
E = html.escape


def sg(n, d=1, u=""):
    return ("+" if n >= 0 else "−") + f"{abs(n):.{d}f}{u}"


def cl(n):
    return "up" if n > 0 else "down" if n < 0 else ""


def ch(n, d=1, u=""):
    return f"<span class='{cl(n)}'>{sg(n, d, u)}</span>"


def day(s, year=False):
    d = dt.date.fromisoformat(s)
    return f"{d:%b} {d.day}" + (f", {d.year}" if year else "")


def money(n):
    return f"{n:,.2f}"


def head(title, key, level=2, extra=""):
    return (f"<div class='sh{extra}'><h{level}>{title}</h{level}><button class='btn explain' type='button' "
            f"data-x='{key}'>Explain</button></div>")


def ana(points):
    return "<div class='ana'><b>What the numbers show</b>" + " ".join(points) + "</div>"


def method_link(anchor, text="Read the method"):
    return f"<a href='{METHOD}#{anchor}'>{text}</a>"


def plural(n, word):
    return f"{n} {word}" + ("" if n == 1 else "s")


def short(r):
    return r["n"].rsplit(" (", 1)[0]


SPANS = [("w", "1W"), ("m1", "1M"), ("m6", "6M"), ("ytd", "YTD"), ("y1", "1Y"), ("y5", "5Y"), ("y10", "10Y")]


def returns_table(rows):
    h = "<tr><th>Ticker</th>" + "".join(f"<th>{s[1]}</th>" for s in SPANS) + "</tr>"
    for r in rows:
        h += f"<tr><td><b>{E(r['t'])}</b> <span class='fn'>{E(short(r))}</span></td>"
        for k, _ in SPANS:
            v = r["ch"][k]
            h += "<td class='mut'>n/a</td>" if v is None else f"<td class='{cl(v)}'>{sg(v, 1, '%')}</td>"
        h += "</tr>"
    return f"<div class='card wrap'><table class='tt'>{h}</table></div>"


# Fear-scale colors for the VIX and AAII bands (owner, 2026-11-14): calm is
# green, the middle grey, rising fear red. Deliberately not the method's
# Strong/Caution colors, which would paint high fear green and read as "buy";
# those stay on the Timing signals tables, where the word is shown with them.
FEAR_TONES = ["zs", "zn", "zc", "zc2", "zc3"]
FEAR_TEXT = ["up", "mut", "down", "down", "down"]


def fear_class(label, bands):
    return FEAR_TEXT[[b[1] for b in bands].index(label)]


def zone_bar(bands, lo, hi, marks, fmt):
    """A horizontal scale split into the method's bands, with markers, colored
    as a fear scale. bands: [(upper, label, signal)], marks: [(value, text, is_previous)]."""
    segs, labs, start = "", "", lo
    for i, b in enumerate(bands):
        end = min(b[0], hi)
        if end <= start:
            continue
        w = (end - start) / (hi - lo) * 100
        cls = FEAR_TONES[i]
        segs += f"<span class='{cls}' style='width:{w:.2f}%'></span>"
        labs += f"<span style='width:{w:.2f}%'>{E(b[1])}</span>"
        start = end
    m = ""
    for v, text, prev in sorted(marks, key=lambda x: not x[2]):
        x = max(0, min(100, (v - lo) / (hi - lo) * 100))
        m += f"<div class='zm{' prev' if prev else ''}' style='left:{x:.2f}%'>{'' if prev else E(text)}</div>"
    return f"<div class='zbar'>{m}<div class='zseg'>{segs}</div><div class='zlab'>{labs}</div></div>"


def line_chart(series, ymin, ymax, guides, w=640, h=170, labels=None):
    """series: [(points [(x_label, y)], css color)]. guides: [(y, text)]."""
    pl, pr, pt, pb = 34, 26, 8, 20
    n = max(len(s[0]) for s in series)
    X = lambda i: pl + (w - pl - pr) * (i / (n - 1) if n > 1 else 0.5)
    Y = lambda y: pt + (h - pt - pb) * (1 - (y - ymin) / (ymax - ymin))
    out = f"<svg viewBox='0 0 {w} {h}' role='img' aria-label='{E(labels or 'chart')}'>"
    for y, text in guides:
        out += (f"<line x1='{pl}' x2='{w - pr}' y1='{Y(y):.1f}' y2='{Y(y):.1f}' stroke='var(--line)' stroke-dasharray='4 4'/>"
                f"<text x='{pl - 4}' y='{Y(y) + 4:.1f}' text-anchor='end'>{E(text)}</text>")
    for pts, color in series:
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(p[1]):.1f}" for i, p in enumerate(pts))
        out += f"<path d='{d}' fill='none' stroke='{color}' stroke-width='2.2' stroke-linejoin='round'/>"
        if len(pts) <= 12:
            out += "".join(f"<circle cx='{X(i):.1f}' cy='{Y(p[1]):.1f}' r='3' fill='{color}'/>" for i, p in enumerate(pts))
    pts = series[0][0]
    step = max(1, (len(pts) - 1) // 5) if len(pts) > 8 else 1
    for i in range(0, len(pts), step):
        out += f"<text x='{X(i):.1f}' y='{h - 4}' text-anchor='middle'>{E(day(pts[i][0]))}</text>"
    return f"<div class='chart'>{out}</svg></div>"


# ---------------------------------------------------------------- the sections
def build(D):
    rows = D["rows"]
    grp = lambda g: [r for r in rows if r["g"] == g]
    idx, sec = grp("idx"), grp("sec")
    V, A, M = D["vix"], D["aaii"], D["mood"]
    cur = A["weeks"][-1]
    vz, vsig, vrange = vix_band(V["cur"])
    vz1 = vix_band(V["w1"])[0]
    az, asig, arange = aaii_band(cur["bear"])
    T = tier(V["cur"], cur["bear"])
    for r in idx + sec:
        r["sig"] = fund_signals(r, vsig, asig)
    S = {}

    # --- AAII facts used on several pages
    d1 = cur["bear"] - A["w1"]["bear"] if A["w1"] else None
    dk = cur["bear"] - A["back"]["bear"] if A["back"] else None
    spread = cur["bull"] - cur["bear"]
    bb, bb_exact = A["streak"]["bearBull"]
    b50, b50_exact = A["streak"]["bear50"]
    atleast = lambda exact: "" if exact else "at least "

    # ===== 1. This week + Major indices
    best = max(idx, key=lambda r: r["ch"]["w"])
    worst = min(idx, key=lambda r: r["ch"]["w"])
    ups = sum(r["ch"]["w"] > 0 for r in idx)
    gvd = [r for r in idx if r["t"] in ("VUG", "VTV", "VIG")]
    lead = {k: max(gvd, key=lambda r: r["ch"][k]) for k in ("w", "m1", "ytd")}
    sbest = max(sec, key=lambda r: r["ch"]["w"])
    sworst = min(sec, key=lambda r: r["ch"]["w"])
    tnx = next(r for r in rows if r["t"] == "^TNX")
    tbp = (tnx["last"] - tnx["wk"]) * 100
    top = max(idx, key=lambda r: r["sig"]["strong"])["sig"]["strong"]
    tops = [r["t"] for r in idx if r["sig"]["strong"] == top]
    cauts = [r["t"] for r in idx if r["sig"]["caution"]]
    facts = [
        f"{ups} of {len(idx)} major funds rose this week. {best['t']} did best ({sg(best['ch']['w'], 1, '%')}) and {worst['t']} trailed ({sg(worst['ch']['w'], 1, '%')}).",
        f"The VIX {'fell' if V['cur'] < V['w1'] else 'rose'} from {V['w1']:.1f} to {V['cur']:.1f}"
        + (f", moving from the {vz1} zone to the {vz} zone." if vz1 != vz else f", staying in the {vz} zone."),
        f"AAII bearish sentiment is {cur['bear']:.1f}% ({az})" + (f", {'up' if d1 >= 0 else 'down'} {abs(d1):.1f} points from last week" if d1 is not None else "")
        + (f". Bearish has outnumbered bullish for {atleast(bb_exact)}{plural(bb, 'week')} in a row." if bb else "."),
        f"Combined AAII and VIX signal: Tier {T} ({TIERS[T][0]}).",
        f"Timing signals: the most Strong readings any major fund shows is {top} of 5"
        + (f" ({', '.join(tops)})." if len(tops) <= 3 else f" ({len(tops)} of {len(idx)} funds).")
        + (f" {', '.join(cauts)} {'has' if len(cauts) == 1 else 'have'} a Caution reading." if cauts else " None has a Caution reading."),
        f"Sectors: {short(sbest)} led ({sg(sbest['ch']['w'], 1, '%')}) and {short(sworst).lower()} trailed ({sg(sworst['ch']['w'], 1, '%')}).",
        f"The 10-year Treasury yield ended at {tnx['last']:.2f}%, {sg(tbp, 0, ' bps')} on the week.",
    ]
    S["summary"] = (
        "<section class='slide'>" + head("This week", "summary")
        + "<p class='lede'>The week in a few facts, each taken from a page of this report. They describe what happened; they are not advice.</p>"
        + "<div class='card'><ul class='facts'>" + "".join(f"<li>{E(f)}</li>" for f in facts) + "</ul></div>"
        + head("Major indices", "indices", 3, " s3")
        + "<p class='lede'>Total return (price change plus dividends reinvested) over each period, ending at this Friday's close. The last six are Vanguard funds that split the market by style, dividends and region.</p>"
        + returns_table(idx)
        + "<p class='lead'><b>Leader, growth vs value vs dividend:</b> "
        + " &nbsp;·&nbsp; ".join(f"{lab} {E(short(lead[k]))} ({lead[k]['t']} {ch(lead[k]['ch'][k], 1, '%')})" for k, lab in (("w", "1W"), ("m1", "1M"), ("ytd", "YTD")))
        + "</p></section>")

    # ===== 2. AAII
    avg, hi, W = A["avg"], A["hi1y"], A["weeks"]
    kk = f"{A['span']}W" if A["span"] else ""
    # This week against last week, a few weeks back and the long-run average.
    rows_a = [("Bullish", "bull", "bull"), ("Neutral", "neut", "neut"), ("Bearish", "bear", "bear"), ("Spread", None, "")]
    val = lambda w, k: (w["bull"] - w["bear"]) if k is None else w[k]
    at_ = "<tr><th></th><th>This week</th><th>1W</th>" + (f"<th>{kk}</th>" if kk else "") + "<th>Average</th></tr>"
    for lab, k, c in rows_a:
        v = val(cur, k)
        shown = sg(v) if k is None else f"{v:.1f}%"
        base = sg(avg["spread"]) if k is None else f"{avg[k]:.1f}%"
        at_ += (f"<tr><td class='{c}'>{lab}</td><td class='{c}'><b>{shown}</b></td>"
                + (f"<td>{ch(v - val(A['w1'], k))}</td>" if A["w1"] else "<td class='mut'>n/a</td>")
                + (f"<td>{ch(v - val(A['back'], k))}</td>" if kk else "")
                + f"<td class='mut'>{base}</td></tr>")
    atable = f"<div class='wrap'><table class='tt'>{at_}</table></div>"
    mx = [
        ("Change in bearish", (ch(d1) if d1 is not None else "n/a") + " <span class='mut' style='font-size:.7em'>1W</span>",
         (f"{ch(dk)} over {A['span']} weeks" if dk is not None else "")),
        ("In a row", f"{atleast(bb_exact)}{plural(bb, 'week')}", f"bearish above bullish; {plural(b50, 'week')} above 50%"),
    ]
    if A["pct"] is not None:
        mx.append(("Percentile", f"{A['pct']:.0f}th", f"bearish higher than {A['pct']:.0f}% of weeks since {A['first'][:4]}"))
    if len(W) >= 8:
        mx.append(("8-week average", f"{sum(w['bear'] for w in W) / len(W):.1f}%", f"bearish; bullish {sum(w['bull'] for w in W) / len(W):.1f}%"))
    mx.append(("1-year bearish high", f"<span class='bear'>{hi['bear'][0]:.1f}%</span>", f"{day(hi['bear'][1], True)}; bullish high {hi['bull'][0]:.1f}%"))
    if len(mx) < 4:
        mx.insert(0, ("Zone", f"<span class='{fear_class(az, AAII_BANDS)}'>{az}</span>", f"bearish {arange}"))
    mx = mx[:4]
    mxh = "<div class='mx'>" + "".join(f"<div><div class='k'>{k}</div><div class='v'>{v}</div><div class='d'>{d}</div></div>" for k, v, d in mx) + "</div>"
    abar = zone_bar([(b[0], b[1], b[2]) for b in AAII_BANDS], 10, 70,
                    [(cur["bear"], f"{cur['bear']:.1f}% {az}", False)] + ([(A["w1"]["bear"], f"{A['w1']['bear']:.1f}%", True)] if A["w1"] else []), None)
    trend = ""
    if len(W) >= 2:
        trend = (line_chart([([(w["d"], w["bull"]) for w in W], "var(--up)"), ([(w["d"], w["bear"]) for w in W], "var(--down)"),
                             ([(w["d"], w["neut"]) for w in W], "var(--muted)")], 10, 60, [(20, "20%"), (40, "40%"), (50, "50%")], w=420, h=165,
                            labels="AAII bullish, bearish and neutral by week")
                 + "<div class='legend'><span>Last " + plural(len(W), "week") + ":</span><span><i class='sw' style='background:var(--up)'></i>Bullish</span>"
                 + "<span><i class='sw' style='background:var(--down)'></i>Bearish</span><span><i class='sw' style='background:var(--muted)'></i>Neutral</span></div>")
    fwd = ""
    if A.get("fwd") and A["fwd"].get("bear50"):
        f50, fa = A["fwd"]["bear50"], A["fwd"]["all"]
        fwd = ("<div class='wrap' style='margin-top:12px'><table class='tt'><tr><th>Past S&amp;P 500 price change after survey weeks</th><th>Weeks</th>"
               "<th>6 months later</th><th>12 months later</th><th>Higher after 12M</th></tr>"
               + "".join(f"<tr><td>{lab}</td><td>{s['n']:,}</td><td class='{cl(s['m6'])}'>{sg(s['m6'], 1, '%')}</td><td class='{cl(s['m12'])}'>{sg(s['m12'], 1, '%')}</td><td>{s['pos12']:.0f}%</td></tr>"
                         for lab, s in (("Weeks with bearish above 50%", f50), ("All weeks", fa)))
               + "</table></div><p class='key'>Past results, not a forecast. Averages over every survey week since "
               + A["first"][:4] + "; neighbouring weeks overlap.</p>")
    a_pts = [f"Bearish sentiment is {cur['bear']:.1f}%, in the {az} zone ({arange})."]
    if d1 is not None:
        a_pts.append(f"It {'rose' if d1 >= 0 else 'fell'} {abs(d1):.1f} points from last week"
                     + (f" and {'rose' if dk >= 0 else 'fell'} {abs(dk):.1f} over {A['span']} weeks." if dk is not None else "."))
    a_pts.append(f"The bull-bear spread of {sg(spread)} is {abs(spread - avg['spread']):.1f} points {'below' if spread < avg['spread'] else 'above'} its long-run average of {sg(avg['spread'])}.")
    a_pts.append(f"Bearish readings have topped bullish ones for {atleast(bb_exact)}{plural(bb, 'week')} in a row"
                 + (f", and this is {'the first week' if b50 == 1 else f'week {b50}'} above 50%." if b50 else "."))
    if cur["bear"] > hi["bear"][0]:
        a_pts.append(f"That is above the 1-year bearish high of {hi['bear'][0]:.1f}% ({day(hi['bear'][1], True)}).")
    if A["pct"] is not None:
        a_pts.append(f"It is higher than {A['pct']:.0f}% of all weekly readings since {A['first'][:4]}.")
    a_pts.append("The method gives more weight to several weeks in a row at an extreme than to a single week.")
    S["aaii"] = (
        "<section class='slide'>" + head("AAII Investor Sentiment", "aaii")
        + "<p class='lede'>Individual investors' six-month outlook, surveyed weekly. The method reads the bearish share as a contrarian signal.</p>"
        + "<div class='card'>"
        + f"<div class='duo'><div>{atable}</div><div>{trend}</div></div>" + abar + mxh + fwd
        + f"<p class='quote'><b>The method on {az} ({arange} bearish):</b> “{E(AAII_SAYS[az])}” {method_link('aaii-sentiment-action-levels')}</p>"
        + ana([E(p) for p in a_pts])
        + f"<div class='src'>Survey week ending {day(cur['d'], True)}. Spread is bullish minus bearish, in points. The grey tick on the bar is last week. "
        + "Source: American Association of Individual Investors, Sentiment Survey (aaii.com/sentimentsurvey)"
        + (". Averages, highs and percentiles calculated from AAII's full history.</div>" if A["hist"] else ". Averages and 1-year highs as AAII publishes them.</div>")
        + "</div></section>")

    # ===== 3. VIX
    v3, v3w = V["v3m"]
    ratio, ratio1 = V["cur"] / v3, V["w1"] / v3w
    term = "Inverted" if ratio >= 1 else "Normal"
    gap50 = M["volatility"][2]
    vmx = [
        ("Change", ch(V["cur"] - V["w1"]) + " <span class='mut' style='font-size:.75em'>1W</span>", f"{ch(V['cur'] - V['m1'])} over 1M (from {V['m1']:.1f})"),
        ("Past-year percentile", f"{V['pct']:.0f}th", f"higher than {V['pct']:.0f}% of the last {V['n']} trading days"),
        ("52-week range", f"{V['lo'][0]:.1f} to {V['hi'][0]:.1f}", f"low {day(V['lo'][1], True)}, high {day(V['hi'][1], True)}"),
        ("Term structure", f"<span class='{'s-caution' if term == 'Inverted' else 's-neutral'}'>{term}</span>", f"VIX {V['cur']:.1f} vs 3-month VIX {v3:.1f}"),
    ]
    vmxh = "<div class='mx'>" + "".join(f"<div><div class='k'>{k}</div><div class='v'>{v}</div><div class='d'>{d}</div></div>" for k, v, d in vmx) + "</div>"
    vbar = zone_bar([(b[0], b[1], b[2]) for b in VIX_BANDS], 10, 50, [(V["cur"], f"{V['cur']:.1f}", False), (V["w1"], f"{V['w1']:.1f}", True)], None)
    days = V["days"]
    tones = FEAR_TONES
    dbar = "<div class='zseg' style='height:20px'>" + "".join(
        f"<span class='{tones[i]}' style='width:{n / V['n'] * 100:.2f}%' title='{VIX_BANDS[i][1]}: {n} days'></span>" for i, n in enumerate(days) if n) + "</div>"
    dleg = "<div class='legend'>" + "".join(f"<span><i class='sw {tones[i]}'></i>{VIX_BANDS[i][1]} {n}</span>" for i, n in enumerate(days)) + "<span>(trading days)</span></div>"
    vchart = line_chart([(V["chart"], "var(--text)")], 10, max(40, max(p[1] for p in V["chart"]) + 2), [(15, "15"), (25, "25"), (35, "35")], h=125,
                        labels="VIX daily close, last three months")
    common = max(range(5), key=lambda i: days[i])
    v_pts = [f"The VIX closed the week at {V['cur']:.1f}, in the {vz} zone ({vrange}), {'down' if V['cur'] < V['w1'] else 'up'} {abs(V['cur'] - V['w1']):.1f} points from {V['w1']:.1f} a week ago"
             + (f", when it was in the {vz1} zone." if vz1 != vz else "."),
             f"A month ago it was {V['m1']:.1f}.",
             f"Over the past year it was lower than today on {V['pct']:.0f}% of trading days, and it spent {days[common]} of {V['n']} days in the {VIX_BANDS[common][1]} zone.",
             f"It sits {abs(gap50):.0f}% {'above' if gap50 >= 0 else 'below'} its 50-day average.",
             f"The VIX is {'above' if ratio >= 1 else 'below'} the 3-month VIX ({v3:.1f}), so expected swings over the next month are {'larger' if ratio >= 1 else 'smaller'} than over the next three months"
             + (f"; a week ago the order was the other way round ({V['w1']:.1f} against {v3w:.1f})." if (ratio >= 1) != (ratio1 >= 1) else ".")]
    S["vix"] = (
        "<section class='slide'>" + head("VIX: the fear gauge", "vix")
        + "<p class='lede'>The market's expectation of how much the S&amp;P 500 will swing over the next 30 days, priced from options. The method treats it as its most actionable timing signal for index funds.</p>"
        + "<div class='card'>"
        + f"<div class='big'><span class='v'>{V['cur']:.1f}</span><span class='lab {fear_class(vz, VIX_BANDS)}'>{vz}</span><span class='mut'>VIX {vrange}, week ending {day(D['friday'], True)}</span></div>"
        + vbar + vmxh
        + "<h3 class='sub2'>Days in each zone, past year</h3>" + dbar + dleg
        + "<h3 class='sub2'>Last three months</h3>" + vchart
        + f"<p class='quote'><b>The method on {vz} (VIX {vrange}):</b> “{E(VIX_SAYS[vz])}” {method_link('vix-action-levels')}</p>"
        + ana([E(p) for p in v_pts])
        + "<div class='src'>The grey tick on the bar is last week. Source: Cboe VIX and VIX3M indexes, daily closes from Yahoo Finance.</div>"
        + "</div></section>")

    # ===== 4 and 6. Timing signals
    def cell(v, s, txt):
        return f"<td><span class='s-{s[1]}'>{txt} {s[0]}</span></td>" if s else "<td class='mut'>n/a</td>"

    def timing_table(fs):
        h = "<tr><th>Ticker</th><th>RSI (14)</th><th>52-week range</th><th>vs 200-day</th><th>Strong</th><th>Caution</th></tr>"
        for r in fs:
            t, s = r["tech"], r["sig"]
            h += (f"<tr><td><b>{E(r['t'])}</b> <span class='fn'>{E(short(r))}</span></td>"
                  + cell(t["rsi"], s["rsi"], f"{t['rsi']:.0f}" if t["rsi"] is not None else "")
                  + cell(t["pos"], s["pos"], f"{t['pos']:.0f}%" if t["pos"] is not None else "")
                  + cell(t["ma200"], s["ma"], sg(t["ma200"], 1, "%") if t["ma200"] is not None else "")
                  + f"<td><b class='{'s-strong' if s['strong'] else 'mut'}'>{s['strong']} of 5</b></td>"
                  + f"<td><span class='{'s-caution' if s['caution'] else 'mut'}'>{s['caution']}</span></td></tr>")
        return f"<div class='card wrap'><table class='tt'>{h}</table></div>"

    market = ("<div class='mx' style='grid-template-columns:repeat(3,1fr);margin:0 0 14px'>"
              + f"<div><div class='k'>VIX</div><div class='v'>{V['cur']:.1f} <span class='s-{vsig}'>{vz}</span></div><div class='d'>{SIG[vsig]}: strong above 35, caution below 15</div></div>"
              + f"<div><div class='k'>AAII bearish</div><div class='v'>{cur['bear']:.1f}% <span class='s-{asig}'>{az}</span></div><div class='d'>{SIG[asig]}: strong above 60%, caution below 25%</div></div>"
              + f"<div><div class='k'>Combined AAII and VIX</div><div class='v'>Tier {T} <span class='{'s-strong' if T else 's-neutral'}'>{TIERS[T][0]}</span></div><div class='d'>{E(TIERS[T][1])}</div></div>"
              + "</div>")
    key = ("<p class='key'>Labels follow the method's “What Strong Signals Look Like” table. Strong: RSI 45 or below, lower 25% of the 52-week range, more than 2% above the 200-day average. "
           "Caution: RSI above 70, top 10% of the range, more than 2% below the 200-day average. Counts include the VIX and AAII. " + method_link("section-timing", "The timing signals") + "</p>")
    dca = ("<p class='quote'><b>From the method:</b> “The VIX, RSI, and AAII sentiment framework is a tool for deploying a pool of cash you already have more opportunistically. "
           "It is not a reason to stop or delay your regular contributions.” " + method_link("dollar-cost-averaging", "Dollar-cost averaging") + "</p>")

    def timing_points(fs, what):
        n = len(fs)
        cnt = lambda k, lab: [r["t"] for r in fs if r["sig"][k] and r["sig"][k][0] == lab]
        pull, over, ob = cnt("rsi", "Pullback") + cnt("rsi", "Oversold"), cnt("rsi", "Overbought"), cnt("rsi", "Elevated")
        lower, high = cnt("pos", "Lower"), cnt("pos", "High")
        above, below = cnt("ma", "Above"), cnt("ma", "Below")
        top = max(r["sig"]["strong"] for r in fs)
        tops = [r["t"] for r in fs if r["sig"]["strong"] == top]
        lst = lambda xs: ", ".join(xs) if xs else "none"
        p = [f"RSI is at 45 or below for {len(pull)} of {n} {what} ({lst(pull)})" + (f"; {len(over)} {'is' if len(over) == 1 else 'are'} above 70 ({lst(over)})." if over else "; none is above 70.")]
        p.append(f"{len(high)} {'sits' if len(high) == 1 else 'sit'} in the top 10% of the 52-week range ({lst(high)}) and {len(lower)} in the lower 25%" + (f" ({lst(lower)})." if lower else "."))
        p.append(f"{len(above)} {'is' if len(above) == 1 else 'are'} more than 2% above the 200-day average and {len(below)} more than 2% below" + (f" ({lst(below)})." if below else "."))
        p.append(f"Most Strong readings: {lst(tops)} ({top} of 5)." + (" No fund can reach 5 this week, because the VIX and AAII are both Neutral." if vsig != "strong" and asig != "strong" else ""))
        return p

    t_pts = timing_points(idx, "major funds")
    t_pts.append(f"The combined AAII and VIX reading is Tier {T} ({TIERS[T][0]}): AAII bearish is {cur['bear']:.1f}% and the VIX is {V['cur']:.1f}.")
    S["timing"] = (
        "<section class='slide'>" + head("Timing signals: major funds", "timing")
        + "<p class='lede'>The method's five timing signals for index funds: two market-wide (VIX and AAII) and three for each fund (RSI, 52-week range position, and price against the 200-day average).</p>"
        + market + timing_table(idx) + key + dca + ana([E(p) for p in t_pts]) + "</section>")
    s_pts = timing_points(sec, "sector funds")
    S["sectiming"] = (
        "<section class='slide'>" + head("Timing signals: sectors", "timing")
        + "<p class='lede'>The same three fund signals for the 11 sector funds. The method says to apply the VIX and RSI timing signals “more aggressively for sector funds” because a single industry can fall further and for longer than the whole market.</p>"
        + market + timing_table(sorted(sec, key=lambda r: (-r["sig"]["strong"], r["sig"]["caution"], r["t"]))) + key + ana([E(p) for p in s_pts]) + "</section>")

    # ===== 5. Sector returns
    srt = sorted(sec, key=lambda r: -r["ch"]["w"])
    sup = sum(r["ch"]["w"] > 0 for r in sec)
    ytd_best = max(sec, key=lambda r: r["ch"]["ytd"])
    S["sectors"] = (
        "<section class='slide'>" + head("Sectors", "sectors")
        + "<p class='lede'>The 11 Select Sector SPDR funds, which together hold the S&amp;P 500 split by industry. Total return over each period, sorted by this week's change.</p>"
        + returns_table(srt)
        + ana([E(f"{sup} of 11 sectors rose this week. {short(srt[0])} led ({sg(srt[0]['ch']['w'], 1, '%')}) and {short(srt[-1]).lower()} trailed ({sg(srt[-1]['ch']['w'], 1, '%')})."),
               E(f"Year to date, {short(ytd_best).lower()} leads ({sg(ytd_best['ch']['ytd'], 1, '%')}).")])
        + "</section>")

    # ===== 7. Market mood
    ab = lambda n, d=1, u="%": f"{abs(n):.{d}f}{u}" + (" above" if n >= 0 else " below")
    cs = lambda n, txt: f"<span class='{cl(n)}'>{txt}</span>"
    MOOD = [
        ("Momentum", "S&amp;P 500 against its 125-day average", cs(M["momentum"][0], ab(M["momentum"][0])), cs(M["momentum"][1], ab(M["momentum"][1])), M["momentum"][0] - M["momentum"][1], 1, " pts"),
        ("Breadth", "S&amp;P 500 stocks above their 200-day average", f"{M['breadth'][0]:.1f}%", f"{M['breadth'][1]:.1f}%", M["breadth"][0] - M["breadth"][1], 1, " pts"),
        ("Safe-haven demand", "Stocks (SPY) minus Treasuries (TLT), 20-day return", cs(M["safehaven"][0], sg(M["safehaven"][0], 1, " pts")), cs(M["safehaven"][1], sg(M["safehaven"][1], 1, " pts")), M["safehaven"][0] - M["safehaven"][1], 1, " pts"),
        ("Junk bond demand", f"High-yield bond spread over Treasuries (1-year average {M['junk'][2]:.2f}%)", f"{M['junk'][0]:.2f}%", f"{M['junk'][1]:.2f}%", (M["junk"][0] - M["junk"][1]) * 100, 0, " bps"),
    ]
    mt = "<tr><th>Indicator</th><th style='text-align:left'>What it measures</th><th>This week</th><th>Last week</th><th>Change</th></tr>" + "".join(
        f"<tr><td><b>{a}</b></td><td style='text-align:left;white-space:normal;color:var(--muted)'>{b}</td><td>{c}</td><td>{d}</td><td class='{cl(e)}'>{sg(e, f, g)}</td></tr>"
        for a, b, c, d, e, f, g in MOOD)
    S["mood"] = (
        "<section class='slide'>" + head("Market mood", "mood")
        + "<p class='lede'>Four readings of how investors are positioned, each measured the same way every week. The VIX has its own page. A reading describes the market; it is not a forecast.</p>"
        + f"<div class='card wrap'><table>{mt}</table></div>"
        + f"<div class='src'>Sources: Yahoo Finance (S&amp;P 500, SPY, TLT and the S&amp;P 500 members); ICE BofA US High Yield Index option-adjusted spread from the Federal Reserve Bank of St. Louis (FRED), whose latest reading is {day(M['junk'][3], True)}.</div>"
        + "</section>")

    # ===== 8. Bond yields
    yt = "<tr><th>Maturity</th><th>Yield</th><th>This week</th><th>Year to date</th></tr>" + "".join(
        f"<tr><td>{E(r['n'])}</td><td>{r['last']:.2f}%</td><td class='{cl(r['last'] - r['wk'])}'>{sg((r['last'] - r['wk']) * 100, 0, ' bps')}</td><td class='{cl(r['last'] - r['ye'])}'>{sg((r['last'] - r['ye']) * 100, 0, ' bps')}</td></tr>"
        for r in grp("yld"))
    S["yields"] = (
        "<section class='slide'>" + head("Bond yields", "yields")
        + "<p class='lede'>US Treasury yields. Changes are in basis points (100 bps = 1 percentage point).</p>"
        + f"<div class='card wrap'><table>{yt}</table></div></section>")

    # ===== 9. Oil, gold, crypto and the dollar
    def tiles(g):
        out = ""
        for r in grp(g):
            w, y = (r["last"] / r["wk"] - 1) * 100, (r["last"] / r["ye"] - 1) * 100
            out += (f"<div class='tile'><div class='k'>{E(r['n'])}</div><div class='v'>{money(r['last'])}</div>"
                    f"<div class='d'>Week {ch(w, 2, '%')} · YTD {ch(y, 2, '%')}</div></div>")
        return out

    S["cmd"] = (
        "<section class='slide'>" + head("Oil, gold, crypto and the dollar", "cmd")
        + "<p class='lede'>Futures for oil and gold. Crypto trades around the clock, so its price is the latest at fetch time.</p>"
        + f"<div class='tiles'>{tiles('cmd')}</div><h3 class='sub2'>The dollar</h3><div class='tiles'>{tiles('oth')}</div></section>")

    order = ["summary", "aaii", "vix", "timing", "sectors", "sectiming", "mood", "yields", "cmd"]
    return "\n".join(S[k] for k in order)


def main(friday):
    D = json.loads((HERE / "data" / f"{friday}.json").read_text(encoding="utf-8"))
    d = dt.date.fromisoformat(friday)
    week = f"Week ending Friday, {d:%B} {d.day}, {d.year}"
    page = (HERE / "template.html").read_text(encoding="utf-8")
    fill = {"__SECTIONS__": build(D), "__EXPLAIN__": (HERE / "explain.html").read_text(encoding="utf-8").strip(),
            "__SUB__": E(f"{week}. Prices fetched {D['fetched']} (local time)."), "__WEEK__": week, "__FETCHED__": D["fetched"]}
    for k, v in fill.items():
        assert page.count(k) == 1, k
        page = page.replace(k, v)
    OUT.write_text(page, encoding="utf-8", newline="\n")
    print("wrote", OUT.relative_to(ROOT), "for", week)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
