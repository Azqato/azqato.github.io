"""Build the Weekly Investing Report page from one week's saved data.

Usage, from anywhere:  python scripts/invests/weekly/build.py 2026-11-13
To try changes before they go live:  build.py 2026-11-13 --demo PATH
writes a standalone copy to PATH instead (the site's links made absolute, a
"Demo" note on top) and leaves invests/weekly/index.html alone.
Reads data/<friday>.json (written by fetch.py), renders every section, fills
template.html with them and the popups in explain.html, and writes
invests/weekly/index.html. Changes nothing else.

The page is roadmap item 23 in docs/PRD.md, launched in 2.41.0: the Invests
sidebar, Home, the Indices & ETFs page, the sitemap and search link to it
(EXTRA_PAGES in scripts/invests/site.py). Claude Code updates it when the owner asks.

The labels follow the Index & ETF Method page (invests/indices/method.html):
the VIX and AAII action levels, the three technical timing signals, the
combined AAII and VIX tiers, and the "What Strong Signals Look Like" table.
Where the method leaves a band undefined, the owner approved these fills
(2026-11-14): RSI 60 to 70 "Elevated", 52-week range 75 to 90% "Upper",
within 2% of the 200-day average "Average". Every label is one word. The
report describes; it gives no posture or advice (owner's rule), so it shows the
method's "What It Signals" text but never its "Recommended Posture".
"""
import math, os, re, datetime as dt, html, json, pathlib, sys

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
    # A value that rounds to zero shows no sign (sense check, 2026-11-20: a
    # spread change of -0.004 read "-0.0").
    if round(n, d) == 0:
        return f"{0:.{d}f}{u}"
    return ("+" if n >= 0 else "-") + f"{abs(n):.{d}f}{u}"


def cl(n):
    return "up" if n > 0 else "down" if n < 0 else ""


def ch(n, d=1, u=""):
    return f"<span class='{cl(round(n, d))}'>{sg(n, d, u)}</span>"


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


CRYPTO_SUFFIX = "-USD"  # Yahoo crypto tickers, e.g. BTC-USD
SPANS = [("w", "1W"), ("m1", "1M"), ("m6", "6M"), ("ytd", "YTD"), ("y1", "1Y"), ("y5", "5Y"), ("y10", "10Y")]


# Status on the returns tables (owner, 2026-11-15): the past month's total
# return, Rising at +2% or more (green), Falling at -2% or less (red),
# otherwise Steady. Prices, so up is green, as in the change columns.
def ret_status(v, rng=None):
    """Status, the first that applies (owner, 2026-11-20), for every asset:
    Bear, 20% or more below its 52-week closing high (red); Correction, 10% or
    more below it (red); Bull, 20% or more above its 52-week closing low (green),
    which by then means within 10% of the high. Otherwise the price against its
    200-day average (owner, 2026-11-15; for funds the same gap as the Signals
    page): Rising more than 5% above, Falling more than 5% below, otherwise
    Steady. The 5% band: a 10-year test showed the method's 2% almost never reads
    Steady for crypto and natural gas."""
    # The figure that decided it follows in brackets, in its own "%" column
    # (owner, 2026-11-20):
    # "Bear (-29.6%)" from the high, "Bull (+24.1%)" from the low, and the
    # 200-day gap for Rising, Steady and Falling.
    # The % cell is left-aligned next to the word (class pc) so the pair reads
    # as one, "Bear (-26.0%)", however wide the table is.
    def td(c, word, n):
        return f"<td class='{c} st'>{word}</td><td class='{c} pc'>({sg(n, 1, '%')})</td>"
    # Decide on the figure as shown, to one decimal, so the label always agrees
    # with the bracket: -19.96% shows as (-20.0%) and so reads Bear (owner, 2026-11-20).
    if rng:
        rng = {k: round(x, 1) for k, x in rng.items()}
    if v is not None:
        v = round(v, 1)
    if rng:
        if rng["hi"] <= -20:
            return td("down", "Bear", rng["hi"])
        if rng["hi"] <= -10:
            return td("down", "Correction", rng["hi"])
        if rng["lo"] >= 20:
            return td("up", "Bull", rng["lo"])
    if v is None:
        return "<td class='mut st'>n/a</td><td class='pc'></td>"
    return td("up", "Rising", v) if v > 5 else td("down", "Falling", v) if v < -5 else td("", "Steady", v)


def returns_table(sections, named=False):
    """One table split into sections like the bond table (owner, 2026-11-15):
    sections is [(title, rows)], each title heading its own header row. named
    labels rows by name alone, for assets whose tickers mean little (CL=F),
    and adds a Price column (owner, 2026-11-15)."""
    h = ""
    for i, (title, rows) in enumerate(sections):
        h += (f"<tr{'' if i == 0 else chr(32) + 'class=' + chr(39) + 'tsub' + chr(39)}><th>{title}</th>"
              + ("<th>Price</th>" if named else "") + "".join(f"<th>{s[1]}</th>" for s in SPANS) + "<th class='st'>Status</th><th class='pc'>%</th></tr>") + returns_rows(rows, named)
    return f"<div class='card wrap'><table class='tt'>{h}</table></div>"


def returns_rows(rows, named=False):
    h = ""
    for r in rows:
        if named:  # prices of 1,000 or more without cents, to fit the page
            price = f"{r['last']:,.0f}" if r["last"] >= 1000 else f"{r['last']:.4f}" if r["last"] < 1 else money(r["last"])
            h += f"<tr><td><b>{E(r['n'])}</b></td><td><b>{price}</b></td>"
        else:
            h += f"<tr><td><b>{E(r['t'])}</b> <span class='fn'>{E(short(r))}</span></td>"
        for k, _ in SPANS:
            v = r["ch"][k]
            h += "<td class='mut'>n/a</td>" if v is None else f"<td class='{cl(v)}'>{sg(v, 1, '%')}</td>"
        h += ret_status(r["tech"]["ma200"] if "tech" in r else r.get("ma200"), r.get("range")) + "</tr>"
    return h


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
    return f"<div class='zbar'><div class='ztrack'>{m}<div class='zseg'>{segs}</div></div><div class='zlab'>{labs}</div></div>"


def line_chart(series, ymin, ymax, guides, w=640, h=170, labels=None, tick=None, marks=(), ticks=None):
    """series: [(points [(x_label, y)], css color)]. guides: [(y, text)].
    tick formats the x labels (default: day). marks: [(index, text, below)] points on the first series,
    each drawn as a grey dashed line across the chart at its level, labeled at its right end
    (below is unused).
    ticks: the indexes to label on the x axis (default: about six, evenly spaced)."""
    pl, pr, pt, pb = 34, (70 if marks else 26), 8, 32
    n = max(len(s[0]) for s in series)
    X = lambda i: pl + (w - pl - pr) * (i / (n - 1) if n > 1 else 0.5)
    Y = lambda y: pt + (h - pt - pb) * (1 - (y - ymin) / (ymax - ymin))
    out = f"<svg viewBox='0 0 {w} {h}' role='img' aria-label='{E(labels or 'chart')}'>"
    for y, text in guides:
        out += (f"<line x1='{pl}' x2='{w - pr}' y1='{Y(y):.1f}' y2='{Y(y):.1f}' stroke='var(--line)' stroke-dasharray='4 4'/>"
                f"<text x='{pl - 4}' y='{Y(y) + 4:.1f}' text-anchor='end'>{E(text)}</text>")
    for pts, color in series:
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(i):.1f},{Y(p[1]):.1f}" for i, p in enumerate(pts))
        # Dense lines (more points than pixels) are drawn thinner so they stay smooth.
        sw = 2.2 if len(pts) <= 300 else 1.3
        out += f"<path d='{d}' fill='none' stroke='{color}' stroke-width='{sw}' stroke-linejoin='round' stroke-linecap='round'/>"
        if len(pts) <= 12:
            out += "".join(f"<circle cx='{X(i):.1f}' cy='{Y(p[1]):.1f}' r='3' fill='{color}'/>" for i, p in enumerate(pts))
    pts = series[0][0]
    for i, text, below in marks:
        y = Y(pts[i][1])
        # High and low marks are a line across the chart at that level, in their
        # subtle grey (owner, 2026-11-15).
        out += f"<line x1='{pl}' x2='{w - pr}' y1='{y:.1f}' y2='{y:.1f}' stroke='var(--muted)' stroke-width='1' stroke-dasharray='5 3' opacity='0.7'/>"
        # Labeled at the line's right end (owner, 2026-11-15).
        out += f"<text x='{w - pr + 5}' y='{y + 4:.1f}' text-anchor='start' font-weight='600'>{E(text)}</text>"
    step = max(1, (len(pts) - 1) // 5) if len(pts) > 8 else 1
    for i in (ticks if ticks is not None else range(0, len(pts), step)):
        out += f"<text x='{X(i):.1f}' y='{h - 4}' text-anchor='middle'>{E((tick or day)(pts[i][0]))}</text>"
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
    vtop, vbot = V["cur"] >= V["hi"][0], V["cur"] <= V["lo"][0]  # a past-year high or low reads as such, not "100%"
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
    top = max(idx, key=lambda r: r["sig"]["strong"])["sig"]["strong"]
    tops = [r["t"] for r in idx if r["sig"]["strong"] == top]
    cauts = [r["t"] for r in idx if r["sig"]["caution"]]
    # ===== 1b. Stock Returns (owner, 2026-11-15: renamed from Major indices
    # and sectors): one table, indices then sectors, built below once the sector
    # figures are worked out.
    idx_lead = (
        "<p class='lead'><b>Leader, growth vs value vs dividend:</b> "
        + " &nbsp;·&nbsp; ".join(f"{lab} {E(short(lead[k]))} ({lead[k]['t']} {ch(lead[k]['ch'][k], 1, '%')})" for k, lab in (("w", "1W"), ("m1", "1M"), ("ytd", "YTD")))
        + "</p>")

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
        ("Change in bearish", (ch(d1) if d1 is not None else "n/a") + " <span class='mut' style='font-size:max(12px, .7em)'>1W</span>",
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
    # AAII and market mood share one page (owner, 2026-11-15): each is a
    # sub-section; the page is assembled with the market mood section.
    aaii_part = (
        head("AAII Survey", "aaii", 3, " s3")
        + "<p class='lede'>Individual investors' six-month outlook, surveyed weekly. The method reads the bearish share as a contrarian signal.</p>"
        + "<div class='card'>"
        + f"<div class='duo'><div>{atable}</div><div>{trend}</div></div>" + abar + mxh + fwd
        + f"<p class='quote'><b>The method on {az} ({arange} bearish):</b> “{E(AAII_SAYS[az])}” {method_link('aaii-sentiment-action-levels')}</p>"
        + ana([E(p) for p in a_pts])
        + f"<div class='src webonly'>Survey week ending {day(cur['d'], True)}. Spread is bullish minus bearish, in points. The grey tick on the bar is last week. "
        + "Source: American Association of Individual Investors, Sentiment Survey (aaii.com/sentimentsurvey)"
        + (". Averages, highs and percentiles calculated from AAII's full history.</div>" if A["hist"] else ". Averages and 1-year highs as AAII publishes them.</div>")
        + "</div>")

    # ===== 3. VIX
    v3, v3w = V["v3m"]
    ratio, ratio1 = V["cur"] / v3, V["w1"] / v3w
    term = "Inverted" if ratio >= 1 else "Normal"
    gap50 = M["volatility"][2]
    vmx = [
        ("Change", ch(V["cur"] - V["w1"]) + " <span class='mut' style='font-size:max(12px, .75em)'>1W</span>", f"{ch(V['cur'] - V['m1'])} over 1M (from {V['m1']:.1f})"),
        ("Past-year percentile", *(("Highest", f"the highest close of the last {V['n']} trading days") if vtop
                                    else ("Lowest", f"the lowest close of the last {V['n']} trading days") if vbot
                                    else (f"{V['pct']:.0f}th", f"higher than {V['pct']:.0f}% of the last {V['n']} trading days"))),
        ("Past-year range", f"{V['lo'][0]:.1f} to {V['hi'][0]:.1f}", f"low {day(V['lo'][1], True)}, high {day(V['hi'][1], True)}"),
        ("Term structure", f"<span class='{'s-caution' if term == 'Inverted' else 's-neutral'}'>{term}</span>", f"VIX {V['cur']:.1f} vs 3-month VIX {v3:.1f}"),
    ]
    vmxh = "<div class='mx'>" + "".join(f"<div><div class='k'>{k}</div><div class='v'>{v}</div><div class='d'>{d}</div></div>" for k, v, d in vmx) + "</div>"
    vbar = zone_bar([(b[0], b[1], b[2]) for b in VIX_BANDS], 10, 50, [(V["cur"], f"{V['cur']:.1f}", False), (V["w1"], f"{V['w1']:.1f}", True)], None)
    days = V["days"]
    tones = FEAR_TONES

    def days_bar(days):
        n_all = sum(days)
        bar = "<div class='zseg' style='height:20px'>" + "".join(
            f"<span class='{tones[i]}' style='width:{n / n_all * 100:.2f}%' title='{VIX_BANDS[i][1]}: {n:,} days'></span>" for i, n in enumerate(days) if n) + "</div>"
        return bar + "<div class='legend'>" + "".join(f"<span><i class='sw {tones[i]}'></i>{VIX_BANDS[i][1]} {n:,}</span>" for i, n in enumerate(days)) + "<span>(trading days)</span></div>"

    dbar, dleg = days_bar(days), ""
    # All time (owner, 2026-11-15): the same zones over the full daily history.
    dall = ("<h3 class='sub2'>Days in each zone, all time</h3>" + days_bar(V["days_all"])) if V.get("days_all") else ""
    cv = [p[1] for p in V["chart"]]
    lo_i, hi_i = cv.index(min(cv)), cv.index(max(cv))
    VH = 135  # VIX chart height
    vchart = line_chart([(V["chart"], "var(--text)")], 0, max(40, max(cv) + 4), [(0, "0"), (15, "15"), (25, "25"), (35, "35")], h=VH,
                        labels="VIX daily close, past year",
                        tick=lambda s: f"{dt.date.fromisoformat(s):%b} '{dt.date.fromisoformat(s):%y}",
                        marks=[(lo_i, f"Low {cv[lo_i]:.1f}", True), (hi_i, f"High {cv[hi_i]:.1f}", False)])
    common = max(range(5), key=lambda i: days[i])
    v_pts = [f"The VIX closed the week at {V['cur']:.1f}, in the {vz} zone ({vrange}), {'down' if V['cur'] < V['w1'] else 'up'} {abs(V['cur'] - V['w1']):.1f} points from {V['w1']:.1f} a week ago"
             + (f", when it was in the {vz1} zone." if vz1 != vz else "."),
             f"A month ago it was {V['m1']:.1f}.",
             ("It is the highest close of the past year" if vtop else "It is the lowest close of the past year" if vbot
              else f"Over the past year it was lower than today on {V['pct']:.0f}% of trading days") + f", and it spent {days[common]} of {V['n']} days in the {VIX_BANDS[common][1]} zone.",
             f"It sits {abs(gap50):.0f}% {'above' if gap50 >= 0 else 'below'} its 50-day average.",
             f"The VIX is {'above' if ratio >= 1 else 'below'} the 3-month VIX ({v3:.1f}), so expected swings over the next month are {'larger' if ratio >= 1 else 'smaller'} than over the next three months"
             + (f"; a week ago the order was the other way round ({V['w1']:.1f} against {v3w:.1f})." if (ratio >= 1) != (ratio1 >= 1) else ".")]
    vall = ""
    if V.get("all"):
        VA = V["all"]
        top = max(range(len(VA)), key=lambda k: VA[k][1])
        bot = min(range(len(VA)), key=lambda k: VA[k][1])
        vall = (f"<h3 class='sub2'>Weekly close, {VA[0][0][:4]} to {VA[-1][0][:4]}</h3>"
                + line_chart([(VA, "var(--text)")], 0, VA[top][1] + 22,
                             [(v, str(v)) for v in range(0, int(VA[top][1]) + 20, 20)], h=VH, labels="VIX weekly close since 1990",
                             tick=lambda s: s[:4], marks=[(bot, f"Low {VA[bot][1]:.1f}", True), (top, f"High {VA[top][1]:.1f}", False)],
                             ticks=[k for k in range(len(VA)) if int(VA[k][0][:4]) % 5 == 0 and (k == 0 or VA[k - 1][0][:4] != VA[k][0][:4])])
)
    S["vix"] = (
        "<section class='slide'>" + head("VIX", "vix")
        + "<p class='lede'>The market's expectation of how much the S&amp;P 500 will swing over the next 30 days, priced from options. The method treats it as its most actionable timing signal for index funds.</p>"
        + "<div class='card'>"
        + f"<div class='big'><span class='v'>{V['cur']:.1f}</span><span class='lab {fear_class(vz, VIX_BANDS)}'>{vz}</span><span class='mut'>VIX {vrange}, week ending {day(D['friday'], True)}</span></div>"
        + vbar + vmxh
        + "<h3 class='sub2'>Days in each zone, past year</h3>" + dbar + dleg + dall
        + "<h3 class='sub2'>Daily close, past year</h3>" + vchart
        # All time (owner, 2026-11-15): weekly closes since 1990.
        + vall
        + f"<p class='quote'><b>The method on {vz} (VIX {vrange}):</b> “{E(VIX_SAYS[vz])}” {method_link('vix-action-levels')}</p>"
        + ana([E(p) for p in v_pts])
        + "<div class='src webonly'>The grey tick on the bar is last week. Source: Cboe VIX and VIX3M indexes, daily closes from Yahoo Finance.</div>"
        + "</div></section>")

    # ===== 4 and 6. Timing signals
    def cell(v, s, txt):
        return f"<td><span class='s-{s[1]}'>{txt} {s[0]}</span></td>" if s else "<td class='mut'>n/a</td>"

    def timing_table(sections):
        """One table split into sections like Stock Returns (owner, 2026-11-15)."""
        h = ""
        for i, (title, fs) in enumerate(sections):
            h += (f"<tr{'' if i == 0 else chr(32) + 'class=' + chr(39) + 'tsub' + chr(39)}><th>{title}</th>"
                  "<th>RSI (14)</th><th>52-week range</th><th>vs 200-day</th><th>Strong</th><th>Caution</th></tr>") + timing_rows(fs)
        return f"<div class='card wrap'><table class='tt'>{h}</table></div>"

    def timing_rows(fs):
        h = ""
        for r in fs:
            t, s = r["tech"], r["sig"]
            h += (f"<tr><td><b>{E(r['t'])}</b> <span class='fn'>{E(short(r))}</span></td>"
                  + cell(t["rsi"], s["rsi"], f"{t['rsi']:.0f}" if t["rsi"] is not None else "")
                  + cell(t["pos"], s["pos"], f"{t['pos']:.0f}%" if t["pos"] is not None else "")
                  + cell(t["ma200"], s["ma"], sg(t["ma200"], 1, "%") if t["ma200"] is not None else "")
                  + f"<td><b class='{'s-strong' if s['strong'] else 'mut'}'>{s['strong']} of 5</b></td>"
                  + f"<td><span class='{'s-caution' if s['caution'] else 'mut'}'>{s['caution']}</span></td></tr>")
        return h

    market = ("<div class='mx' style='grid-template-columns:repeat(3,1fr);margin:0 0 14px'>"
              + f"<div><div class='k'>VIX</div><div class='v'>{V['cur']:.1f} <span class='s-{vsig}'>{vz}</span></div><div class='d'>{SIG[vsig]}: strong above 35, caution below 15</div></div>"
              + f"<div><div class='k'>AAII bearish</div><div class='v'>{cur['bear']:.1f}% <span class='s-{asig}'>{az}</span></div><div class='d'>{SIG[asig]}: strong above 60%, caution below 25%</div></div>"
              + f"<div><div class='k'>Combined AAII and VIX</div><div class='v'>Tier {T} <span class='{'s-strong' if T else 's-neutral'}'>{TIERS[T][0]}</span></div><div class='d'>{E(TIERS[T][1])}</div></div>"
              + "</div>")
    key = ("<p class='key'>Labels follow the method's “What Strong Signals Look Like” table. Strong: RSI 45 or below, lower 25% of the 52-week range, more than 2% above the 200-day average. "
           "Caution: RSI above 70, top 10% of the range, more than 2% below the 200-day average. Counts include the VIX and AAII. " + method_link("section-timing", "The timing signals") + "</p>")
    dca = ("<p class='quote'><b>From the method:</b> “The VIX, RSI, and AAII sentiment framework is a tool for deploying a pool of cash you already have more opportunistically. "
           "It is not a reason to stop or delay your regular contributions.” " + method_link("dollar-cost-averaging", "Dollar-cost averaging") + "</p>")

    cap_ = lambda t: t[0].upper() + t[1:]

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
        num = lambda xs: str(len(xs)) if xs else "none"
        p.append(f"{cap_(num(high))} {'sits' if len(high) == 1 else 'sit'} in the top 10% of the 52-week range" + (f" ({lst(high)})" if high else "")
                 + f" and {num(lower)} in the lower 25%" + (f" ({lst(lower)})." if lower else "."))
        p.append(f"{cap_(num(above))} {'is' if len(above) == 1 else 'are'} more than 2% above the 200-day average and {num(below)} more than 2% below" + (f" ({lst(below)})." if below else "."))
        p.append(f"Most Strong readings: {lst(tops)} ({top} of 5)." + (" No fund can reach 5 this week, because the VIX and AAII are both Neutral." if vsig != "strong" and asig != "strong" else ""))
        return p

    t_pts = timing_points(idx, "major funds")
    t_pts.append(f"The combined AAII and VIX reading is Tier {T} ({TIERS[T][0]}): AAII bearish is {cur['bear']:.1f}% and the VIX is {V['cur']:.1f}.")
    s_pts = timing_points(sec, "sector funds")
    # Major funds and sectors on one page (owner, 2026-11-15).
    S["timing"] = (
        "<section class='slide dense'>" + head("Signals", "timing")
        + "<p class='lede'>The method's five timing signals for index funds: two market-wide (VIX and AAII) and three for each fund (RSI, 52-week range position, and price against the 200-day average). "
        "For the 11 sector funds the method says to apply the VIX and RSI signals “more aggressively” because a single industry can fall further and for longer than the whole market.</p>"
        + market + timing_table([("Indices", idx), ("Sectors", sorted(sec, key=lambda r: (-r["sig"]["strong"], r["sig"]["caution"], r["t"])))])
        + key + dca + ana([E(p) for p in t_pts] + [E(p) for p in s_pts]) + "</section>")

    # ===== 5. Sector returns
    srt = sorted(sec, key=lambda r: -r["ch"]["w"])
    sup = sum(r["ch"]["w"] > 0 for r in sec)
    ytd_best = max(sec, key=lambda r: r["ch"]["ytd"])
    S["indices"] = (
        "<section class='slide dense'>" + head("Returns", "indices")
        + "<p class='lede'>Total return over each period, price change plus dividends reinvested, for 12 major funds and the 11 sector funds that make up the S&amp;P 500.</p>"
        + returns_table([("Indices", idx), ("Sectors", srt)])
        + idx_lead
        + "<p class='key webonly'>Sectors are the 11 Select Sector SPDR funds, which together make up the S&amp;P 500, sorted by this week's change. "
        "<button class='btn explain' type='button' data-x='sectors'>Explain sectors</button></p>"
        + "<div class='src webonly'>Total return: price change plus dividends reinvested, to this Friday's close.<span> Status, the first that applies, with the figure that decided it in the % column: Bear (red) 20% or more below the 52-week closing high; Correction (red) 10% or more below it; Bull (green) 20% or more above the 52-week closing low; otherwise the price against its 200-day average: Rising (green) more than 5% above, Falling (red) more than 5% below, otherwise Steady.</span></div>"
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
    S["aaii"] = (
        "<section class='slide'><div class='sh'><h2>Sentiment</h2></div>" + aaii_part
        + head("Market Mood", "mood", 3, " s3")
        + "<p class='lede'>Four readings of how investors are positioned, each measured the same way every week. The VIX has its own page. A reading describes the market; it is not a forecast.</p>"
        + f"<div class='card wrap'><table>{mt}</table></div>"
        + f"<div class='src'>Sources: Yahoo Finance (S&amp;P 500, SPY, TLT and the S&amp;P 500 members); ICE BofA US High Yield Index option-adjusted spread from the Federal Reserve Bank of St. Louis (FRED), whose latest reading is {day(M['junk'][3], True)}.</div>"
        + "</section>")

    # ===== 8. Bond yields
    # The same periods as the returns tables (owner, 2026-11-15), as changes in basis points.
    # Rows whose latest reading is older than Friday (FRED's lag, weekly
    # mortgage rates): the note under the table gives the dates (no marks, owner 2026-11-15).

    # Inversion (owner, 2026-11-15): a Treasury or TIPS yield below that of any
    # shorter maturity is inverted and its yield shows red; otherwise green. A
    # yield curve row is inverted when its gap is below zero.
    months = lambda r: int(r["n"].split("-")[0]) * (1 if "Month" in r["n"] else 12) if r["n"][:1].isdigit() else 0
    # Same day only (sense check, 2026-11-20): Yahoo's yields are this Friday's
    # close and FRED's are a day or more older, so in a week rates moved fast a
    # Friday yield could look inverted against a Thursday one. Each yield is
    # read on the date every maturity in its group has; a Yahoo yield uses its
    # FRED series ("same") for that day. A yield with no reading that day is left out.
    def on(r, d):
        if r["d"] == d:
            return r["last"]
        s_ = r.get("same")
        return s_["last"] if s_ and s_["d"] == d else None

    inverted, over = {}, {}
    for g in ("yld", "tips"):
        rs = sorted(grp(g), key=months)
        if not rs:
            continue
        d0 = min(r["d"] for r in rs)
        top = None
        for r in rs:
            v = on(r, d0)
            inverted[r["t"]] = top is not None and v is not None and v < top[1]
            if inverted[r["t"]]:
                over[r["t"]] = (top[0], v, top[1], d0)
            if v is not None and (top is None or v > top[1]):
                top = (r, v)
    # Real Fed Funds is not a yield gap: below zero it is "Behind" (CPI
    # inflation above the Fed funds rate), not Inverted (owner, 2026-11-15).
    REAL = "FF-CPI"
    for r in grp("curve"):
        inverted[r["t"]] = r["last"] < 0 and r["t"] != REAL

    # Policy, mortgage and inflation rows (owner, 2026-11-15): Status is the
    # direction over the past month, Rising or Falling at 10 bps or more,
    # otherwise Steady. Not colored: higher rates help savers and cost borrowers.
    trend = lambda m: "Rising" if m >= 10 else "Falling" if m <= -10 else "Steady"
    # Status colors (owner, 2026-11-15): Rising red, Falling green, Steady in
    # the normal text color.
    stat = lambda w: f"<td class='{'down' if w == 'Rising' else 'up' if w == 'Falling' else ''}'>{w}</td>"

    def ylabel(n):
        """Short labels (owner, 2026-11-15): 10-Year Treasury -> 10Y, 5-Year TIPS
        -> 5Y TIPS, 30-year mortgage -> 30Y Mortgage, 60-month car loan -> 60M Car Loan."""
        n = re.sub(r"(\d+)-[Yy]ear", r"\1Y", re.sub(r"(\d+)-[Mm]onth", r"\1M", n.replace(" Treasury", "")))
        return " ".join(w[:1].upper() + w[1:] for w in n.split(" "))

    def yrow(r):
        name = ylabel(r["n"])
        level = f"{sg(r['last'], 2)}" if r["g"] == "curve" else "n/a" if r["last"] is None else f"{r['last']:.2f}%"
        # The muni row's changes are MUB's total return in bps (owner,
        # 2026-11-15): a gain means muni prices rose and yields fell, so it is
        # green, and its Status reads the yield direction from the 1M return.
        up = 1 if r.get("ret") else -1
        # Policy and mortgage rates show their reading's month, like CPI and PCE (owner, 2026-11-15).
        when = f" <span class='fn'>{dt.date.fromisoformat(r['d']):%b}</span>" if r["g"] == "rates" else ""
        # Yield curve rows (owner, 2026-11-15): changes are not colored, and
        # Status reads Steepening or Flattening at 10 bps or more over the past
        # month, uncolored; only Inverted (or Behind, for Real Fed Funds)
        # is red. Real Fed Funds keeps Rising and Falling, as it is not a gap.
        curve = r["g"] == "curve"
        cell = lambda v: "" if curve else cl(up * round(v))
        if inverted.get(r["t"]):
            status = "<td class='down'>Inverted</td>"
        elif r["t"] == REAL and r["last"] < 0:
            status = "<td class='down'>Behind</td>"
        elif curve:
            m = r["bps"]["m1"]
            word = ("Rising" if m >= 10 else "Falling" if m <= -10 else "Steady") if r["t"] == REAL else                    ("Steepening" if m >= 10 else "Flattening" if m <= -10 else "Steady")
            status = f"<td>{word}</td>"
        else:
            status = stat(trend(-r['bps']['m1'] if r.get("ret") else r['bps']['m1']))
        return (f"<tr><td><b>{E(name)}</b>{when}</td><td><b>{level}</b></td>"
                + "".join(f"<td class='{cell(r['bps'][k])}'>{sg(r['bps'][k], 0) if round(r['bps'][k]) else '+0'}</td>" for k, _ in SPANS)
                + status + "</tr>")

    # Inflation (owner, 2026-11-15): monthly, so it changes about once a month.
    # Change colors (owner, 2026-11-15): a rise in a yield, spread or rate is red
    # and a fall green, as a rising yield means a falling bond price; inflation
    # follows the same rule, and so do the yield curve gaps (owner, 2026-11-15).
    # A zero change shows as +0.
    # Headline CPI and PCE only (owner, 2026-11-15: no core rows), in the same
    # section as the policy and mortgage rates.
    INF = [r for r in D.get("inflation") or [] if r["t"] in ("CPIAUCSL", "PCEPI")]
    mon = lambda s: f"{dt.date.fromisoformat(s):%b %Y}"
    cpi = next((r for r in INF if r["t"] == "CPIAUCSL"), None)

    def irow(r):
        cells = "".join("<td>+0</td>" if r["bps"][k] is None else f"<td class='{cl(-round(r['bps'][k]))}'>{sg(r['bps'][k], 0) if round(r['bps'][k]) else '+0'}</td>" for k, _ in SPANS)
        return f"<tr><td><b>{E(r['n'])}</b> <span class='fn'>{dt.date.fromisoformat(r['month']):%b}</span></td><td><b>{r['yoy']:.2f}%</b></td>{cells}{stat(trend(r['bps']['m1']))}</tr>"

    ycols = "".join(f"<th>{s[1]}</th>" for s in SPANS)
    TP = grp("tips")
    # Each section sorted from the lowest level to the highest (owner,
    # 2026-11-15); ties keep the shorter maturity first.
    def section(g):
        rs = grp(g) + (grp("tips") + grp("muni") if g == "yld" else [])  # TIPS share the Treasury section (owner, 2026-11-15)
        # The yield curve keeps fetch.py's fixed order (owner, 2026-11-15).
        out = [((i if g == "curve" else r["last"] or 0), months(r) if g == "yld" else 0, yrow(r)) for i, r in enumerate(rs)]
        if g == "rates":
            out += [(r["yoy"], 0, irow(r)) for r in INF]
        return "".join(h for _, _, h in sorted(out, key=lambda x: x[:2]))
    yt = f"<tr><th>Treasury, TIPS and munis</th><th>Yield</th>{ycols}<th>Status</th></tr>" + section("yld")
    for g, title, col in (("rates", "Policy, mortgage and inflation rates", "Rate"), ("curve", "Yield curve", "Gap")):
        if grp(g) or (g == "rates" and INF):
            yt += f"<tr class='tsub'><th>{title}</th><th>{col}</th>{ycols}<th>Status</th></tr>" + section(g)
    # The full notes stay on the website page; the export leaves them out
    # (owner, 2026-11-15) to make room for the table.
    late = sorted({r["d"] for r in rows if r["g"] in ("yld", "tips", "curve", "rates") and r["d"] != D["friday"] and not r.get("q")})
    be = D.get("breakeven")
    yld_note = ("<div class='webonly'><p class='key'>TIPS (Treasury Inflation-Protected Securities) pay a yield on top of inflation, a “real” yield."
                + (f" The 10-year breakeven rate (10-year Treasury minus 10-year TIPS, same day) is {be[0]:.2f}% on {day(be[1], True)}: "
                   "roughly the yearly inflation the bond market expects." if be else "")
                + " Muni (MUB) is the iShares National Muni Bond ETF: its yield as of the fetch, and its total return over each period in bps (+100 bps = +1%), green when its price rose. The yield curve rows are the gap between two yields in points; below zero means inverted. Real Fed Funds is the Fed funds rate minus CPI inflation over 12 months. "
                "Changes are red when a yield or rate rose (a rising yield means a falling bond price) and green when it fell. Status is Inverted (red) when a yield is below a shorter maturity's, or a gap is below zero, and that comes first. "
                "Otherwise it is the move over the past month: Rising (red) or Falling (green) at 10 bps or more, otherwise Steady. "
                "The yield curve rows are not colored: a gap is Steepening when it widened by 10 bps or more over the past month, Flattening when it narrowed by that much, otherwise Steady; "
                "Real Fed Funds is Behind (red) below zero, when CPI inflation is above the Fed funds rate. Mortgage rates are Freddie Mac's weekly survey averages; credit card (accounts paying interest) and car loan rates are the Fed's quarterly survey of banks.</p>"
                "<div class='src'>The 3-month, 5, 10 and 30-year Treasury yields from Yahoo Finance (Cboe indexes) at this Friday's close; the rest from FRED, including CPI (Bureau of Labor Statistics) and PCE (Bureau of Economic Analysis). "
                + (f"FRED's daily figures are its latest reading ({' or '.join(day(d, True) for d in late)}), with changes measured back from that date." if late else "") + "</div></div>")
    # Inversion callout (owner, 2026-11-15): whenever any yield or gap is
    # inverted, a red callout above the table names each one. It is data, so
    # it stays in the export; the history line is for the website only.
    bad = [r for r in rows if inverted.get(r["t"])]
    alert = ""
    if bad:
        nm_ = lambda r: ylabel(r["n"])
        items = [f"on {day(over[r['t']][3])}, the {nm_(r)} yield, {over[r['t']][1]:.2f}%, was below the {nm_(over[r['t']][0])} yield, {over[r['t']][2]:.2f}%" if r["t"] in over
                 else f"{r['n']} is {sg(r['last'], 2)} points" for r in sorted(bad, key=lambda r: r["g"] != "curve")]
        alert = ("<div class='alert'><p class='alert-h'>Inverted</p><ul>" + "".join(f"<li>{E(i[0].upper() + i[1:])}.</li>" for i in items) + "</ul>"
                 "<p class='webonly alert-n'>An inverted yield curve, short-term yields above long-term ones, has often, but not always, come before a recession.</p></div>")
    S["yields"] = (
        "<section class='slide dense xdense'>" + head("Rates", "yields")
        + "<p class='lede'>Treasury, TIPS and muni yields, the rates that set borrowing costs, inflation and the yield curve. Changes over each period are in basis points (100 bps = 1 percentage point).</p>"
        + alert + f"<div class='card wrap'><table class='tt'>{yt}</table></div>" + yld_note + "</section>")

    # ===== 9. Other (owner, 2026-11-15): one Returns-style table with
    # Commodities, Currency and Crypto sections, plus price; price change, as
    # none of them pay out.
    COM = [r for r in grp("cmd") if not r["t"].endswith(CRYPTO_SUFFIX)]
    CRY = [r for r in grp("cmd") if r["t"].endswith(CRYPTO_SUFFIX)]
    S["cmd"] = (
        "<section class='slide dense'>" + head("Other Markets", "cmd")
        + "<p class='lede'>Futures for energy and metals, the dollar index and major currencies, and crypto, which trades around the clock.</p>"
        + returns_table([("Commodities", COM), ("Currency", grp("oth")), ("Crypto", CRY)], named=True)
        + "<div class='src webonly'>Price change from Yahoo Finance: commodities and currencies to this Friday's close, crypto to the latest price at fetch time. "
        "Each currency is its own index: the PHLX currency indexes for the euro, yen, pound, Canadian dollar and Swiss franc, and the yuan and won built the same way from Yahoo's exchange rates; "
        "each is the currency's value in US cents (the yen and won per 100), so a rise means that currency got stronger."
        "<span> Status, the first that applies, with the figure that decided it in the % column: Bear (red) 20% or more below the 52-week closing high; Correction (red) 10% or more below it; Bull (green) 20% or more above the 52-week closing low; otherwise the price against its 200-day average: Rising (green) more than 5% above, Falling (red) more than 5% below, otherwise Steady.</span></div>"
        + "</section>")

    # ===== 1. This week (owner, 2026-11-15): two bullets per page of the report,
    # the page's main takeaway and then added context. Facts only, no advice.
    pct = lambda n, d=1: sg(n, d, "%")
    rose = lambda n: "rose" if n >= 0 else "fell"
    lst = lambda xs: ", ".join(xs[:-1]) + " and " + xs[-1] if len(xs) > 1 else (xs[0] if xs else "")
    CAUSE = [("rsi", "RSI above 70"), ("pos", "top 10% of the 52-week range"), ("ma", "over 2% below the 200-day")]

    def cautions(fs):
        parts = []
        for k, why in CAUSE:
            ts = [r["t"] for r in fs if r["sig"][k] and r["sig"][k][1] == "caution"]
            if ts:
                parts.append(f"{lst(ts)} ({why})")
        return "Caution: " + "; ".join(parts) + "." if parts else "No Caution readings."

    def strongest(fs, what):
        top = max(r["sig"]["strong"] for r in fs)
        tops = [r["t"] for r in fs if r["sig"]["strong"] == top]
        return f"no {what} has more than {top} of 5 Strong signals" + (f" ({lst(tops)})" if len(tops) <= 3 else "")

    def pulls(fs):
        pb = [r["t"] for r in fs if r["sig"]["rsi"] and r["sig"]["rsi"][1] == "strong"]
        return f" RSI 45 or below: {lst(pb) if len(pb) <= 4 else f'{len(pb)} of {len(fs)}'}." if pb else " None has RSI at 45 or below."

    # Major indices
    dn1 = [r for r in idx if r["ch"]["m1"] < 0]
    wm1 = min(idx, key=lambda r: r["ch"]["m1"])
    lag = min(gvd, key=lambda r: r["ch"]["ytd"])
    # Sense check (owner, 2026-11-20): when nothing rose, "0 of 12 rose, VBR
    # the most (-6.0%)" read wrong; the wording follows how many rose.
    def updown(n_up, n, what, top, name):
        v = pct(top["ch"]["w"])
        if n_up == 0:
            return f"all {n} {what} fell this week, and {name} fell the least ({v})"
        if n_up == n:
            return f"all {n} {what} rose this week, {name} the most ({v})"
        return f"{n_up} of {n} {what} rose this week, {name} the most ({v})"

    def leads(r, k):  # "leads" when it gained, "held up best" when even the leader fell
        return f"leads ({pct(r['ch'][k])})" if r["ch"][k] > 0 else f"held up best ({pct(r['ch'][k])})"

    tw_idx = (updown(ups, len(idx), "major funds", best, best["t"]) + "; "
              + updown(sup, 11, "sectors", srt[0], short(srt[0]).lower()) + ".",
              (f"Over 1 month all {len(idx)} are lower, {wm1['t']} the most ({pct(wm1['ch']['m1'])})" if len(dn1) == len(idx)
               else f"Over 1 month {len(dn1)} of {len(idx)} are lower, {wm1['t']} the most ({pct(wm1['ch']['m1'])})" if dn1
               else f"All {len(idx)} are higher over the past month")
              + f"; YTD {short(lead['ytd']).lower()} ({lead['ytd']['t']} {pct(lead['ytd']['ch']['ytd'])}) "
              + (f"leads {short(lag).lower()}" if lead["ytd"]["ch"]["ytd"] > lag["ch"]["ytd"] else f"is level with {short(lag).lower()}")
              + f" ({lag['t']} {pct(lag['ch']['ytd'])}), and among sectors {short(ytd_best).lower()} {leads(ytd_best, 'ytd')}.")
    # AAII
    tw_aaii = (f"Bearish sentiment is {cur['bear']:.1f}%, in the {az} zone ({arange})"
               + (f", {'up' if d1 >= 0 else 'down'} {abs(d1):.1f} points from last week." if d1 is not None else "."),
               (f"Bearish has topped bullish for {atleast(bb_exact)}{plural(bb, 'week')} in a row"
                + (f", and this is {'the first week' if b50 == 1 else f'week {b50}'} above 50%" if b50 else "") if bb else "Bullish is at or above bearish this week")
               + f"; the bull-bear spread of {sg(spread)} is {abs(spread - avg['spread']):.1f} points {'below' if spread < avg['spread'] else 'above'} its long-run average ({sg(avg['spread'])}).")
    # VIX
    tw_vix = (f"The VIX {rose(V['cur'] - V['w1'])} {abs(V['cur'] - V['w1']):.1f} points to {V['cur']:.1f}"
              + (f", moving from the {vz1} zone to the {vz} zone." if vz1 != vz else f", staying in the {vz} zone."),
              (f"Its highest close of the past year (range {V['lo'][0]:.1f} to {V['hi'][0]:.1f}); " if vtop
               else f"Its lowest close of the past year (range {V['lo'][0]:.1f} to {V['hi'][0]:.1f}); " if vbot
               else f"Lower than today on {V['pct']:.0f}% of the past year's trading days (range {V['lo'][0]:.1f} to {V['hi'][0]:.1f}); ")
              + f"{'above' if ratio >= 1 else 'below'} the 3-month VIX ({v3:.1f}), {'the reverse of the usual order' if ratio >= 1 else 'the usual order'}.")
    # Timing signals
    tw_timing = (f"AAII and VIX combined: Tier {T} ({TIERS[T][0]}); {strongest(idx, 'major fund')}.",
                 cautions(idx) + pulls(idx))
    tw_sectiming = (f"{strongest(sec, 'sector fund')[0].upper()}{strongest(sec, 'sector fund')[1:]}.",
                    cautions(sec) + pulls(sec))
    # Market mood
    mo, br, sh, jk = M["momentum"], M["breadth"], M["safehaven"], M["junk"]
    tw_mood = (f"{br[0]:.0f}% of S&P 500 stocks are above their 200-day average ({'up' if br[0] >= br[1] else 'down'} from {br[1]:.0f}%); "
               f"the index is {abs(mo[0]):.1f}% {'above' if mo[0] >= 0 else 'below'} its 125-day average.",
               f"Over 20 days stocks {'beat' if sh[0] >= 0 else 'trailed'} Treasuries by {abs(sh[0]):.1f} points; the high-yield spread is {jk[0]:.2f}%, "
               f"{'down' if jk[0] < jk[1] else 'up' if jk[0] > jk[1] else 'unchanged'} from {jk[1]:.2f}% ({jk[2]:.2f}% 1-year average).")
    # Bond yields
    Y = grp("yld")
    c2 = next((r for r in grp("curve") if r["t"] == "T10Y2Y"), None)
    yup = [r for r in Y if r["bps"]["w"] > 0]
    ymax = max(Y, key=lambda r: abs(r["bps"]["w"]))
    n_inv = sum(1 for v in inverted.values() if v)
    tw_yld = (f"The 10-year Treasury yield ended at {tnx['last']:.2f}%, {sg(tnx['bps']['w'], 0, ' bps')} this week and {sg(tnx['bps']['ytd'], 0, ' bps')} year to date"
              + (f"; {n_inv} {'yield or gap is' if n_inv == 1 else 'yields or gaps are'} inverted." if n_inv else "; no part of the yield curve is inverted."),
              (f"All {len(Y)} maturities rose" if len(yup) == len(Y) else "All maturities fell" if not yup else f"{len(yup)} of {len(Y)} maturities rose")
              + f", and the biggest move was the {ymax['n'].replace(' Treasury', '').lower()} ({sg(ymax['bps']['w'], 0, ' bps')})"
              + (f"; the 10-year is {abs(c2['last']):.2f} points {'above' if c2['last'] >= 0 else 'below'} the 2-year" if c2 else "")
              + (f"; CPI inflation is {cpi['yoy']:.1f}% ({mon(cpi['month'])})." if cpi else "."))
    # Commodities and the dollar
    C = COM + grp("oth")
    wk = lambda r: r["ch"]["w"]
    yt = lambda r: r["ch"]["ytd"]
    cap = lambda s: s[0].upper() + s[1:]
    nm = lambda r: {"CL=F": "WTI oil", "BZ=F": "Brent oil", "DX-Y.NYB": "the US dollar"}.get(r["t"], r["n"] if r["t"].endswith(CRYPTO_SUFFIX) else r["n"].lower())
    big = max(C, key=lambda r: abs(wk(r)))
    named = [r for r in C if r["t"] in ("CL=F", "GC=F", "DX-Y.NYB") and r is not big]
    yb, yw = max(COM, key=yt), min(COM, key=yt)  # the commodities only, as the bullet says
    tw_cmd = (f"{cap(nm(big))} {rose(wk(big))} {abs(wk(big)):.1f}% this week, the biggest commodity move; " + lst([f"{nm(r)} {pct(wk(r))}" for r in named]) + ".",
              f"In commodities, year to date {nm(yb)} {leads(yb, 'ytd')} and {nm(yw)} trails ({pct(yt(yw))}).")
    # Crypto
    btc = next(r for r in CRY if r["t"] == "BTC-USD")
    eth = next((r for r in CRY if r["t"] == "ETH-USD"), None)
    cbig = max(CRY, key=lambda r: abs(wk(r)))
    cdown = sum(wk(r) < 0 for r in CRY)
    cyb, cyw = max(CRY, key=yt), min(CRY, key=yt)
    tw_crypto = ((f"All {len(CRY)} coins fell" if cdown == len(CRY) else f"All {len(CRY)} coins rose" if not cdown else f"{cdown} of {len(CRY)} coins fell")
                 + f" this week: Bitcoin {pct(wk(btc))}" + (f", Ethereum {pct(wk(eth))}" if eth else "")
                 + f", {nm(cbig)} the most ({pct(wk(cbig))}).",
                 f"In crypto, year to date {nm(cyb)} {leads(cyb, 'ytd')} and {nm(cyw)} trails ({pct(yt(cyw))}).")

    order = ["summary", "indices", "aaii", "vix", "timing", "yields", "cmd"]
    # 2 to 4 bullets per page (owner, 2026-11-15): clauses joined by "; " become
    # their own bullets, and a section with more than 4 joins its last ones.
    semis = lambda *xs: [p.rstrip(".") for x in xs for p in x.split("; ")]

    def bullets(parts):
        parts = parts[:3] + ["; ".join(parts[3:])] if len(parts) > 4 else parts
        return [p[0].upper() + p[1:] + ("" if p.endswith(".") else ".") for p in parts]

    TW = [("Returns", bullets(semis(*tw_idx))),
          ("Sentiment", bullets([tw_aaii[0], tw_aaii[1], tw_mood[0], tw_mood[1]])),
          ("VIX", bullets([tw_vix[0]] + semis(tw_vix[1]))),
          ("Signals", bullets([tw_timing[0] + " " + tw_sectiming[0], "Major funds: " + tw_timing[1], "Sectors: " + tw_sectiming[1]])),
          ("Rates", bullets(semis(*tw_yld))),
          ("Other Markets", bullets([tw_cmd[0], tw_crypto[0], tw_cmd[1], tw_crypto[1]]))]
    assert all(2 <= len(b) <= 4 for _, b in TW)
    # Executive summary (owner, 2026-11-15): four lines across the report,
    # facts only, before the page-by-page summaries.
    spy = next(r for r in idx if r["t"] == "SPY")
    s_best, s_worst = max(sec, key=lambda r: r["ch"]["w"]), min(sec, key=lambda r: r["ch"]["w"])
    EXEC = [
        f"The S&P 500 (SPY) {rose(spy['ch']['w'])} {abs(spy['ch']['w']):.1f}% this week and is {pct(spy['ch']['ytd'])} year to date; "
        + ("none of the" if not ups else "all" if ups == len(idx) else f"{ups} of the") + f" {len(idx)} major funds rose.",
        f"Among sectors, {short(s_best)} ({s_best['t']}) {'led at' if s_best['ch']['w'] > 0 else 'fell the least,'} {pct(s_best['ch']['w'])} and {short(s_worst)} ({s_worst['t']}) {'trailed at' if s_worst['ch']['w'] > 0 else 'fell the most,'} {pct(s_worst['ch']['w'])}.",
        f"The VIX is {V['cur']:.1f} ({vz}) and AAII bearish sentiment is {cur['bear']:.1f}% ({az}); combined, Tier {T} ({TIERS[T][0]}).",
        f"The 10-year Treasury yield is {tnx['last']:.2f}% ({sg(tnx['bps']['w'], 0, ' bps')} this week)"
        + (f"; {n_inv} {'yield or gap is' if n_inv == 1 else 'yields or gaps are'} inverted." if n_inv else "; no part of the yield curve is inverted."),
    ]
    # The week's written summary (owner, 2026-11-15): Claude Code writes
    # data/summary/<friday>.json, 2 to 5 parts shown as one paragraph, with each weekly
    # update. Without it the factual bullets above are used.
    sf = HERE / "data" / "summary" / f"{D['friday']}.json"
    if sf.exists():
        EXEC = json.loads(sf.read_text(encoding="utf-8"))
        assert 2 <= len(EXEC) <= 5, "the executive summary takes 2 to 5 parts"
    S["summary"] = (
        "<section class='slide'>" + head("This Week", "summary")
        + "<div class='card tw'><div class='twg exec'><p class='twh'>Executive Summary</p>" + f"<p class='para'>{E(' '.join(EXEC))}</p>" + "</div>" + "".join(
            f"<div class='twg'><p class='twh'><a class='twl' href='#p-{k}'>{E(t)} <span>page {i}</span></a></p><ul class='facts'>" + "".join(f"<li{' class=' + chr(39) + 'main' + chr(39) if j == 0 else ''}>{E(x)}</li>" for j, x in enumerate(bs)) + "</ul></div>"
            for i, ((t, bs), k) in enumerate(zip(TW, order[1:]), 2))
        + "</div></section>")
    # Each page gets an id so the This Week headings can link to it (owner,
    # 2026-11-15); the export carries the ids onto its pages.
    return "\n".join(S[k].replace("<section class='slide", f"<section id='p-{k}' class='slide", 1) for k in order)


SITE = "https://azqato.com/invests/"
DEMO_NOTE = ("<p style='margin:0 0 14px;padding:8px 12px;border:1px dashed var(--muted);border-radius:8px;font-size:0.85rem;color:var(--muted)'>"
             "<b>Demo</b>: proposed changes, not yet on azqato.com.</p>")


def main(friday, demo=None):
    D = json.loads((HERE / "data" / f"{friday}.json").read_text(encoding="utf-8"))
    if os.environ.get("WEEKLY_MOCK_INVERT"):
        # Demo only (demo.py --mock-invert): a made-up inversion to preview the
        # callout. Never used for the live page.
        assert demo, "the mock inversion is for demos only"
        for r in D["rows"]:
            if r["t"] == "^TNX":
                r["last"] = 4.60
                if r.get("same"):
                    r["same"]["last"] = 4.60
            if r["t"] == "T10Y2Y":
                r["last"] = -0.26
    d = dt.date.fromisoformat(friday)
    week = f"Week ending Friday, {d:%B} {d.day}, {d.year}"
    page = (HERE / "template.html").read_text(encoding="utf-8")
    fill = {"__SECTIONS__": build(D), "__EXPLAIN__": (HERE / "explain.html").read_text(encoding="utf-8").strip(),
            # Subtitle (owner, 2026-11-15): the same as the export header, a
            # link to the Discord and the Friday's date.
            "__SUB__": "<a class='discord' href='https://discord.com/invite/6bnZFtNd5p'>Discord</a> · " + E(f"{d:%B} {d.day}, {d.year}"), "__WEEK__": week, "__FETCHED__": D["fetched"]}
    for k, v in fill.items():
        assert page.count(k) == 1, k
        page = page.replace(k, v)
    if demo:
        for rel, url in (("../indices/method.html", SITE + "indices/method"), ("../indices/index.html", SITE + "indices/"),
                         ("../index.html", SITE)):
            page = page.replace(f'href="{rel}', f'href="{url}').replace(f"href='{rel}", f"href='{url}")
        assert 'href="../' not in page and "href='../" not in page, "a relative site link is left in the demo"
        page = page.replace('<nav class="crumbs"', DEMO_NOTE + '<nav class="crumbs"', 1)
        pathlib.Path(demo).write_text(page, encoding="utf-8", newline="\n")
        print("wrote demo", demo, "for", week)
        return
    OUT.write_text(page, encoding="utf-8", newline="\n")
    print("wrote", OUT.relative_to(ROOT), "for", week)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 3 and args[1] == "--demo":
        main(args[0], args[2])
    elif len(args) == 1:
        main(args[0])
    else:
        sys.exit(__doc__)
