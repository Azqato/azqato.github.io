"""Fetch one week's numbers for the Weekly Investing Report.

Usage, from anywhere:  python scripts/invests/weekly/fetch.py [FRIDAY]
FRIDAY is the week's last trading day as YYYY-MM-DD; it defaults to the most
recent Friday. Writes data/<friday>.json; build.py turns that into the page.

Every number comes from a source Claude Code can fetch (roadmap item 23):
  - prices, yields, the VIX and VIX3M: Yahoo Finance via yfinance. Bitcoin and
    Ethereum trade every day, so they use the latest price at fetch time;
  - market mood: calculated from Yahoo Finance closes, plus the ICE BofA US High
    Yield spread from FRED's free CSV. Breadth uses the S&P 500 member list in
    the sibling Stocks repository (../Stocks/data/sp500.json), read only;
  - AAII: data/aaii.json holds the readings published at aaii.com/sentimentsurvey
    (Claude Code adds each Thursday's reading by hand). If the owner's one-time
    AAII history download has been imported (aaii_import.py), it is merged in
    from private/aaii-history.csv, which is git-ignored: only the statistics
    calculated from it reach the page, never the raw history.
Fund returns are total returns (dividends reinvested, Yahoo's adjusted closes),
the same basis as the ETF screener. RSI, the 52-week range and the 200-day
average use unadjusted prices, also as the screener does (Stocks repository,
scripts/fetch_etf_data.py): 14-day Wilder RSI over one year of closes, and an
intraday 52-week high and low.
The 2-year Treasury (2YY=F) is left out because Yahoo returned stale values.
Needs: pip install yfinance pandas
"""
import csv, datetime as dt, io, json, pathlib, sys, urllib.request
import pandas as pd
import yfinance as yf

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
SP500 = ROOT.parent / "Stocks" / "data" / "sp500.json"
AAII_PUBLIC = HERE / "data" / "aaii.json"
AAII_PRIVATE = HERE / "private" / "aaii-history.csv"
FRED_HY = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2"

# (ticker, label, group). idx = Major indices, sec = sector funds, yld = Bond
# yields, cmd = oil, gold and crypto tiles, oth = the dollar tile.
TICKERS = [
    ("SPY", "S&P 500 (SPY)", "idx"), ("QQQ", "Nasdaq 100 (QQQ)", "idx"),
    ("IWM", "Russell 2000 (IWM)", "idx"), ("DIA", "Dow Jones 30 (DIA)", "idx"),
    ("VUG", "Growth (VUG)", "idx"), ("VTV", "Value (VTV)", "idx"),
    ("VIG", "Dividend (VIG)", "idx"), ("VT", "World (VT)", "idx"),
    ("VTI", "Domestic (VTI)", "idx"), ("VXUS", "International (VXUS)", "idx"),
    ("XLK", "Technology (XLK)", "sec"), ("XLC", "Communication (XLC)", "sec"),
    ("XLY", "Consumer discretionary (XLY)", "sec"), ("XLP", "Consumer staples (XLP)", "sec"),
    ("XLF", "Financials (XLF)", "sec"), ("XLV", "Health care (XLV)", "sec"),
    ("XLI", "Industrials (XLI)", "sec"), ("XLE", "Energy (XLE)", "sec"),
    ("XLB", "Materials (XLB)", "sec"), ("XLU", "Utilities (XLU)", "sec"),
    ("XLRE", "Real estate (XLRE)", "sec"),
    ("^IRX", "3-Month Treasury", "yld"), ("^FVX", "5-Year Treasury", "yld"),
    ("^TNX", "10-Year Treasury", "yld"), ("^TYX", "30-Year Treasury", "yld"),
    ("CL=F", "Crude oil (WTI)", "cmd"), ("BZ=F", "Crude oil (Brent)", "cmd"),
    ("GC=F", "Gold", "cmd"), ("BTC-USD", "Bitcoin", "cmd"), ("ETH-USD", "Ethereum", "cmd"),
    ("DX-Y.NYB", "US Dollar Index", "oth"),
]
FUNDS = {"idx", "sec"}
CRYPTO = {"BTC-USD", "ETH-USD"}
EOD = pd.Timedelta(hours=23, minutes=59)


def upto(s, day):
    """The series up to and including the given day."""
    return s[s.index <= day + EOD]


def at(s, day):
    return float(upto(s, day).iloc[-1])


def hist(t, period, adjust):
    h = yf.Ticker(t).history(period=period, auto_adjust=adjust)
    h.index = h.index.tz_localize(None)
    return h


def closes(t, period, adjust):
    return hist(t, period, adjust)["Close"].dropna()


def rsi14(c):
    """14-day Wilder RSI, the screener's formula."""
    if len(c) < 15:
        return None
    d = [c[i] - c[i - 1] for i in range(1, len(c))]
    up = sum(x for x in d[:14] if x > 0) / 14
    dn = -sum(x for x in d[:14] if x < 0) / 14
    for x in d[14:]:
        up = (up * 13 + max(x, 0)) / 14
        dn = (dn * 13 + max(-x, 0)) / 14
    return 100.0 if dn == 0 else 100 - 100 / (1 + up / dn)


def technicals(t, fri):
    """RSI, 52-week range position and the gap to the 200-day average at FRIDAY."""
    h = upto(hist(t, "2y", False), fri)
    year = h[h.index > fri - pd.Timedelta(days=365)]
    c = [float(x) for x in year["Close"].dropna()]
    last = c[-1]
    lo, hi = float(year["Low"].min()), float(year["High"].max())
    all_c = [float(x) for x in h["Close"].dropna()]
    ma = sum(all_c[-200:]) / 200 if len(all_c) >= 200 else None
    return {"rsi": rsi14(c), "lo": lo, "hi": hi,
            "pos": (last - lo) / (hi - lo) * 100 if hi > lo else None,
            "ma200": (last / ma - 1) * 100 if ma else None}


def prices(fri):
    prev, ye = fri - pd.Timedelta(days=7), pd.Timestamp(fri.year - 1, 12, 31)
    spans = {"w": prev, "m1": fri - pd.DateOffset(months=1), "m6": fri - pd.DateOffset(months=6),
             "ytd": ye, "y1": fri - pd.DateOffset(years=1), "y5": fri - pd.DateOffset(years=5),
             "y10": fri - pd.DateOffset(years=10)}
    rows = []
    for t, n, g in TICKERS:
        fund = g in FUNDS
        h = closes(t, "11y" if fund else "2y", adjust=fund)
        cur = h if t in CRYPTO else upto(h, fri)
        last = float(cur.iloc[-1])
        r = dict(t=t, n=n, g=g, last=last, wk=at(h, prev), ye=at(h, ye), d=str(cur.index[-1].date()))
        if fund:  # total return over each span; None when the fund is too young
            r["ch"] = {}
            for k, day in spans.items():
                s = upto(h, day)
                young = s.empty or (h.index[0] - day).days > 21
                r["ch"][k] = None if young else round((last / float(s.iloc[-1]) - 1) * 100, 4)
            r["tech"] = technicals(t, fri)
        rows.append(r)
        print(t, r["d"], round(last, 3))
    return rows


def vix_block(fri):
    v = upto(closes("^VIX", "2y", False), fri)
    year = v.iloc[-252:]
    zones = [0, 0, 0, 0, 0]  # below 15, 15-25, 25-35, 35-45, above 45
    for x in year:
        zones[0 if x < 15 else 1 if x < 25 else 2 if x < 35 else 3 if x <= 45 else 4] += 1
    cur = float(v.iloc[-1])
    v3 = upto(closes("^VIX3M", "1y", False), fri)
    return {"cur": cur, "w1": at(v, fri - pd.Timedelta(days=7)), "m1": at(v, fri - pd.DateOffset(months=1)),
            "lo": [float(year.min()), str(year.idxmin().date())], "hi": [float(year.max()), str(year.idxmax().date())],
            "pct": float((year < cur).mean() * 100), "days": zones, "n": len(year),
            "v3m": [float(v3.iloc[-1]), at(v3, fri - pd.Timedelta(days=7))],
            "chart": [[str(d.date()), round(float(x), 2)] for d, x in v.iloc[-63:].items()]}


def mood(fri):
    prev, M = fri - pd.Timedelta(days=7), {}
    # Momentum: S&P 500 against its 125-day average.
    spx = closes("^GSPC", "2y", True)
    gap = (spx / spx.rolling(125).mean() - 1) * 100
    M["momentum"] = [at(gap, fri), at(gap, prev)]
    # Volatility: the VIX and its gap to its 50-day average (shown on the VIX page).
    vix = closes("^VIX", "2y", True)
    vgap = (vix / vix.rolling(50).mean() - 1) * 100
    M["volatility"] = [at(vix, fri), at(vix, prev), at(vgap, fri), at(vgap, prev)]
    # Safe-haven demand: SPY 20-day return minus TLT 20-day return.
    spy, tlt = closes("SPY", "2y", True), closes("TLT", "2y", True)
    diff = (spy.pct_change(20) - tlt.pct_change(20)).dropna() * 100
    M["safehaven"] = [at(diff, fri), at(diff, prev)]
    # Breadth: share of S&P 500 members above their 200-day average.
    tick = [m["t"].replace(".", "-") for m in json.loads(SP500.read_text(encoding="utf-8"))]
    px = yf.download(tick, period="2y", auto_adjust=True, progress=False, threads=True)["Close"]
    px.index = px.index.tz_localize(None)
    ma = px.rolling(200).mean()

    def breadth(day):
        i = px.index[px.index <= day + EOD][-1]
        ok = px.loc[i].notna() & ma.loc[i].notna()
        return float((px.loc[i][ok] > ma.loc[i][ok]).mean() * 100), int(ok.sum())

    b1, n1 = breadth(fri)
    b0, _ = breadth(prev)
    M["breadth"] = [b1, b0, n1]
    # Junk bond demand: ICE BofA US High Yield option-adjusted spread, with its 1-year average.
    raw = urllib.request.urlopen(FRED_HY, timeout=30).read().decode()
    rows = list(csv.reader(io.StringIO(raw)))[1:]
    hy = pd.Series({pd.Timestamp(d): float(v) for d, v in rows if v not in ("", ".")}).sort_index()
    avg = float(hy[hy.index > hy.index[-1] - pd.Timedelta(days=365)].mean())
    M["junk"] = [at(hy, fri), at(hy, prev), avg, str(upto(hy, fri).index[-1].date())]
    return M


def aaii_block(fri):
    pub = json.loads(AAII_PUBLIC.read_text(encoding="utf-8"))
    weeks = {}
    if AAII_PRIVATE.exists():
        with AAII_PRIVATE.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                weeks[r["date"]] = {"d": r["date"], "bull": float(r["bull"]), "neut": float(r["neut"]), "bear": float(r["bear"])}
    hist_n = len(weeks)
    for w in pub["weeks"]:  # the published readings win over the download
        weeks[w["d"]] = w
    W = [w for _, w in sorted(weeks.items()) if pd.Timestamp(w["d"]) <= fri]
    full = hist_n >= 520  # ten years or more: enough to compute averages and percentiles ourselves
    cur = W[-1]
    cd = pd.Timestamp(cur["d"])
    by = {w["d"]: w for w in W}

    def back(days):
        return by.get(str((cd - pd.Timedelta(days=days)).date()))

    # The longest look-back available up to four weeks, so the page can say "3W" until a fifth week exists.
    span = next((k for k in (4, 3, 2) if back(7 * k)), None)
    out = {"weeks": W[-8:], "w1": back(7), "span": span, "back": back(7 * span) if span else None,
           "hist": full, "n": len(W), "first": W[0]["d"]}

    def streak(test):
        n = 0
        for w in reversed(W):
            if not test(w):
                break
            n += 1
        return [n, n < len(W)]  # [weeks, exact]; not exact when it runs back to the first week on file

    out["streak"] = {"bearBull": streak(lambda w: w["bear"] > w["bull"]), "bear50": streak(lambda w: w["bear"] > 50)}
    if full:
        n = len(W)
        out["avg"] = {k: sum(w[k] for w in W) / n for k in ("bull", "neut", "bear")}
        year = [w for w in W if pd.Timestamp(w["d"]) > cd - pd.Timedelta(days=365)]
        out["hi1y"] = {k: (lambda m: [m[k], m["d"]])(max(year, key=lambda w: w[k])) for k in ("bull", "neut", "bear")}
        out["pct"] = sum(w["bear"] < cur["bear"] for w in W) / n * 100
        out["fwd"] = forward(W, fri)
    else:
        out["avg"] = pub["published"]["avg"]
        out["hi1y"] = pub["published"]["hi1y"]
        out["pct"] = out["fwd"] = None
    out["avg"]["spread"] = out["avg"]["bull"] - out["avg"]["bear"]
    return out


def forward(W, fri):
    """S&P 500 price change 6 and 12 months after each survey week: weeks with
    bearish above 50% against all weeks. History only, used on the page as
    'past results, not a forecast'."""
    spx = closes("^GSPC", "max", False)

    def after(d, days):
        end = d + pd.Timedelta(days=days)
        if end > fri:
            return None
        return (at(spx, end) / at(spx, d) - 1) * 100

    rows = []
    for w in W:
        d = pd.Timestamp(w["d"])
        if d < spx.index[0]:
            continue
        rows.append((w["bear"] > 50, after(d, 182), after(d, 365)))

    def summary(sel):
        s6 = [r[1] for r in sel if r[1] is not None]
        s12 = [r[2] for r in sel if r[2] is not None]
        if not s12:
            return None
        return {"n": len(s12), "m6": sum(s6) / len(s6), "m12": sum(s12) / len(s12),
                "pos12": sum(x > 0 for x in s12) / len(s12) * 100}

    return {"bear50": summary([r for r in rows if r[0]]), "all": summary(rows)}


def main(friday):
    fri = pd.Timestamp(friday)
    d = {"rows": prices(fri), "fetched": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
         "mood": mood(fri), "vix": vix_block(fri), "aaii": aaii_block(fri), "friday": friday}
    out = HERE / "data" / f"{friday}.json"
    out.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.exit(__doc__)
    if len(sys.argv) == 2:
        day = sys.argv[1]
    else:
        today = dt.date.today()
        day = str(today - dt.timedelta(days=(today.weekday() - 4) % 7))
    main(day)
