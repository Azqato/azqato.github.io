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
# FRED series for the yields taken from Yahoo, for a same-day inversion test.
AAII_PRIVATE = HERE / "private" / "aaii-history.csv"
FRED_HY = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2"

# (ticker, label, group). idx = Major indices, sec = sector funds, yld = Bond
# yields, cmd = oil, gold and crypto tiles, oth = the dollar tile.
TICKERS = [
    ("SPY", "S&P 500 (SPY)", "idx"), ("QQQ", "Nasdaq 100 (QQQ)", "idx"),
    ("IWM", "Russell 2000 (IWM)", "idx"), ("DIA", "Dow Jones 30 (DIA)", "idx"), ("RSP", "Equal Weight (RSP)", "idx"),
    ("VUG", "Growth (VUG)", "idx"), ("VTV", "Value (VTV)", "idx"),
    ("VIG", "Dividend (VIG)", "idx"), ("VBR", "Small-Cap Value (VBR)", "idx"), ("VT", "World (VT)", "idx"),
    ("VTI", "Domestic (VTI)", "idx"), ("VXUS", "International (VXUS)", "idx"),
    ("XLK", "Technology (XLK)", "sec"), ("XLC", "Communication (XLC)", "sec"),
    ("XLY", "Consumer discretionary (XLY)", "sec"), ("XLP", "Consumer staples (XLP)", "sec"),
    ("XLF", "Financials (XLF)", "sec"), ("XLV", "Health care (XLV)", "sec"),
    ("XLI", "Industrials (XLI)", "sec"), ("XLE", "Energy (XLE)", "sec"),
    ("XLB", "Materials (XLB)", "sec"), ("XLU", "Utilities (XLU)", "sec"),
    ("XLRE", "Real estate (XLRE)", "sec"),
    ("CL=F", "Crude oil (WTI)", "cmd"), ("BZ=F", "Crude oil (Brent)", "cmd"), ("NG=F", "Natural gas", "cmd"),
    ("GC=F", "Gold", "cmd"), ("SI=F", "Silver", "cmd"), ("PL=F", "Platinum", "cmd"), ("HG=F", "Copper", "cmd"),
    ("BTC-USD", "Bitcoin", "cmd"), ("ETH-USD", "Ethereum", "cmd"), ("BNB-USD", "BNB", "cmd"), ("XRP-USD", "XRP", "cmd"),
    ("SOL-USD", "Solana", "cmd"), ("TRX-USD", "TRON", "cmd"), ("DOGE-USD", "Dogecoin", "cmd"), ("ZEC-USD", "Zcash", "cmd"),
    ("ADA-USD", "Cardano", "cmd"), ("XMR-USD", "Monero", "cmd"), ("LTC-USD", "Litecoin", "cmd"),
    ("DX-Y.NYB", "US Dollar", "oth"),
    # Currencies (owner, 2026-11-15), each as its own index pulled like the
    # Dollar Index: the PHLX currency indexes, each currency's value in US
    # cents (the yen per 100 yen), so a rise means that currency got stronger.
    # Yahoo has none for the yuan or the won, so those two are built the same
    # way from Yahoo's exchange rates (see FX_INDEX).
    ("CNY-IDX", "Chinese Yuan", "oth"), ("^XDE", "Euro", "oth"), ("^XDN", "Japanese Yen", "oth"), ("^XDB", "British Pound", "oth"),
    ("KRW-IDX", "Korean Won", "oth"), ("^XDC", "Canadian Dollar", "oth"), ("^XDS", "Swiss Franc", "oth"),
]
FUNDS = {"idx", "sec"}
CRYPTO = {t for t, _, _ in TICKERS if t.endswith("-USD")}
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


def range52(t, last_day, last=None):
    """How far the price sits from its 52-week closing high and low, in % (owner,
    2026-11-20: Bear, Correction and Bull). Prices, not total return: the last
    252 daily closes up to last_day. For crypto, last is the price at fetch time."""
    if t in FX_INDEX:
        src, k = FX_INDEX[t]
        h = k / closes(src, "2y", adjust=False)
    else:
        h = closes(t, "2y", adjust=False)
    y = upto(h, pd.Timestamp(last_day)).iloc[-252:]
    last = float(y.iloc[-1]) if last is None else last
    hi, lo = max(float(y.max()), last), min(float(y.min()), last)
    return {"hi": round((last / hi - 1) * 100, 4), "lo": round((last / lo - 1) * 100, 4)}


def spans_of(fri):
    """The start of each period the returns tables show, ending at Friday."""
    return {"w": fri - pd.Timedelta(days=7), "m1": fri - pd.DateOffset(months=1), "m6": fri - pd.DateOffset(months=6),
            "ytd": pd.Timestamp(fri.year - 1, 12, 31), "y1": fri - pd.DateOffset(years=1),
            "y5": fri - pd.DateOffset(years=5), "y10": fri - pd.DateOffset(years=10)}


def yield_changes(h, last, ref):
    """A yield's change over each period, in basis points (owner, 2026-11-15:
    the same periods as the returns tables), measured back from ref, the date
    of the yield's own latest reading."""
    return {k: round((last - at(h, day)) * 100, 2) for k, day in spans_of(ref).items()}


# Treasury and TIPS yields to this Friday (owner, 2026-11-20: update
# everything). FRED posts the Treasury's daily par yield curves a day or more
# late, but the Treasury publishes them the same afternoon. FRED keeps the
# history; any newer days come from the Treasury's own CSVs. Same figures:
# FRED's DGS and DFII series are these curves.
TREASURY_COL = {"DGS1MO": "1 Mo", "DGS3MO": "3 Mo", "DGS6MO": "6 Mo", "DGS1": "1 Yr", "DGS2": "2 Yr", "DGS5": "5 Yr",
                "DGS7": "7 Yr", "DGS10": "10 Yr", "DGS20": "20 Yr", "DGS30": "30 Yr"}
TREASURY_REAL = {"DFII5": "5 YR", "DFII7": "7 YR", "DFII10": "10 YR", "DFII20": "20 YR", "DFII30": "30 YR"}
_cache, _own = {}, {}


def treasury(kind):
    """The Treasury's daily par yield curve ("daily_treasury_yield_curve") or
    real yield curve ("daily_treasury_real_yield_curve") for this year and last,
    as {column: Series}."""
    if kind not in _cache:
        out = {}
        for year in (dt.date.today().year - 1, dt.date.today().year):
            url = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/"
                   f"{year}/all?type={kind}&field_tdr_date_value={year}&page&_format=csv")
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            rows = list(csv.DictReader(io.StringIO(urllib.request.urlopen(req, timeout=30).read().decode("utf-8-sig"))))
            for r in rows:
                day = pd.Timestamp(dt.datetime.strptime(r["Date"], "%m/%d/%Y"))
                for k, v in r.items():
                    if k != "Date" and v not in ("", None):
                        out.setdefault(k, {})[day] = float(v)
        _cache[kind] = {k: pd.Series(v).sort_index() for k, v in out.items()}
    return _cache[kind]


def fred(series):
    """A FRED series from its free CSV, as a date-indexed float Series. For a
    Treasury or TIPS yield, days the Treasury has published since FRED's last
    reading are added from the Treasury's CSV."""
    if series in _cache:
        return _cache[series]
    raw = urllib.request.urlopen(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}", timeout=30).read().decode()
    rows = list(csv.reader(io.StringIO(raw)))[1:]
    h = pd.Series({pd.Timestamp(d): float(v) for d, v in rows if v not in ("", ".")}).sort_index()
    _own[series] = h.index[-1]
    col = TREASURY_COL.get(series) or TREASURY_REAL.get(series)
    if col:
        t = treasury("daily_treasury_yield_curve" if series in TREASURY_COL else "daily_treasury_real_yield_curve")[col]
        h = pd.concat([h, t[t.index > h.index[-1]]])
    _cache[series] = h
    return h


# Yields from FRED (owner, 2026-11-15): the Treasury maturities Yahoo lacks,
# TIPS real yields, the yield curve, the Fed funds rate and mortgage rates.
# FRED posts most daily readings the next business day, so a Saturday fetch
# usually has Thursday's; mortgage rates are weekly, on Thursdays. Each row
# keeps its own date and its changes are measured back from that date.
FRED_ROWS = [
    ("DGS1MO", "1-Month Treasury", "yld"), ("DGS3MO", "3-Month Treasury", "yld"), ("DGS6MO", "6-Month Treasury", "yld"),
    ("DGS1", "1-Year Treasury", "yld"), ("DGS2", "2-Year Treasury", "yld"), ("DGS5", "5-Year Treasury", "yld"),
    ("DGS7", "7-Year Treasury", "yld"), ("DGS10", "10-Year Treasury", "yld"), ("DGS20", "20-Year Treasury", "yld"),
    ("DGS30", "30-Year Treasury", "yld"),
    ("DFII5", "5-Year TIPS", "tips"), ("DFII10", "10-Year TIPS", "tips"), ("DFII30", "30-Year TIPS", "tips"),
    # Yield curve, in this fixed order (owner, 2026-11-15), Real Fed Funds last.
    ("T10Y2Y", "10Y - 2Y", "curve"), ("DGS30-DGS10", "30Y - 10Y", "curve"), ("DGS2-DFF", "2Y - Fed Funds", "curve"),
    ("T10YFF", "10Y - Fed Funds", "curve"), ("DGS30-DFF", "30Y - Fed Funds", "curve"), ("FF-CPI", "Real Fed Funds", "curve"),
    ("DFF", "Fed Funds Rate", "rates"), ("MORTGAGE30US", "30-year mortgage", "rates"), ("MORTGAGE15US", "15-year mortgage", "rates"),
    # Credit card and car loan rates (owner, 2026-11-15): the Fed's quarterly
    # survey of banks (G.19), readings dated Feb, May, Aug and Nov.
    ("TERMCBCCINTNS", "Credit card", "rates"), ("RIFLPBCIANM60NM", "60-month car loan", "rates"),
]
# Quarterly rows measure their changes back from Friday, not from their own
# date, so a quarter's move shows only in the periods it falls inside.
QUARTERLY = {"TERMCBCCINTNS", "RIFLPBCIANM60NM"}


def ff_cpi():
    """The real Fed funds rate (owner, 2026-11-15; was Fed funds plus 1 point):
    the Fed funds rate minus CPI inflation over 12 months. Each CPI month
    counts from the start of the next month (October's from November 1), so
    it uses the same CPI month as the CPI row (owner, 2026-11-15)."""
    ff = fred("DFF")
    c = fred("CPIAUCSL")
    yoy = yoy12(c)
    yoy.index = yoy.index + pd.DateOffset(months=1)
    y = yoy.reindex(ff.index.union(yoy.index)).ffill().reindex(ff.index)
    return (ff - y).dropna().round(2)


# The 10Y - 2Y and 10Y - Fed Funds gaps are built from the daily yields like
# the others, so they reach Friday with the Treasury's figures; the ids stay.
CUSTOM = {"FF-CPI": ff_cpi, "T10Y2Y": lambda: (fred("DGS10") - fred("DGS2")).dropna().round(2),
          "T10YFF": lambda: (fred("DGS10") - fred("DFF")).dropna().round(2)}


def fred_rows(fri):
    rows = []
    for t, n, g in FRED_ROWS:
        # "A-B" is a gap FRED has no series for (owner, 2026-11-15: 30-year
        # minus 10-year), built from the two daily yields.
        if t in CUSTOM:
            h = CUSTOM[t]()
        elif "-" in t:
            a, b = t.split("-")
            h = (fred(a) - fred(b)).dropna().round(2)
        else:
            h = fred(t)
        cur = upto(h, fri)
        last, ref = float(cur.iloc[-1]), cur.index[-1]
        base = fri if t in QUARTERLY else ref
        rows.append(dict(t=t, n=n, g=g, last=last, wk=at(h, base - pd.Timedelta(days=7)), ye=at(h, pd.Timestamp(fri.year - 1, 12, 31)),
                         d=str(ref.date()), bps=yield_changes(h, last, base), q=t in QUARTERLY,
                         src="Treasury" if (t in TREASURY_COL or t in TREASURY_REAL) and ref > fred_last(t) else "FRED"))
        print(t, rows[-1]["d"], last)
    return rows


def fred_last(t):
    """FRED's own latest date for a series, before any Treasury days were added."""
    fred(t)
    return _own[t]


def muni(fri):
    """Munis (owner, 2026-11-15): no free source keeps a muni yield history, so
    the row is MUB, the iShares National Muni Bond ETF: its yield from Yahoo as
    of the fetch, and its total return over each period, in basis points
    (+1.00% = +100 bps), to this Friday's close."""
    h = closes("MUB", "11y", adjust=True)
    last = float(upto(h, fri).iloc[-1])
    y = yf.Ticker("MUB").info.get("yield")
    ret = {k: round((last / float(upto(h, day).iloc[-1]) - 1) * 10000) for k, day in spans_of(fri).items()}
    print("MUB", y, ret)
    return [dict(t="MUB", n="Muni (MUB)", g="muni", last=round(y * 100, 2) if y else None, d=str(fri.date()), bps=ret, ret=True)]


def breakeven(fri):
    """The 10-year breakeven inflation rate: the 10-year Treasury yield minus the
    10-year TIPS yield, both from the same day (FRED's T10YIE, built here from
    the two yields so it reaches Friday with the Treasury's figures)."""
    h = upto((fred("DGS10") - fred("DFII10")).dropna().round(2), fri)
    return [float(h.iloc[-1]), str(h.index[-1].date())]


# Inflation (owner, 2026-11-15): CPI from the Bureau of Labor Statistics and
# PCE from the Bureau of Economic Analysis, both monthly, through FRED.
INFLATION = [("CPIAUCSL", "CPI"), ("PCEPI", "PCE")]


def yoy12(h):
    """Inflation over 12 months: each month's index against the same calendar
    month a year earlier, never 12 rows back (2026-11-22: BLS published no
    October 2025 CPI, so counting rows compared later months with 13 months
    before). A month with no reading a year earlier has no rate."""
    return ((h / h.shift(freq=pd.DateOffset(months=12)).reindex(h.index)) - 1).dropna() * 100


def inflation(fri):
    """Each measure's 12-month rate for its latest month, and how far that rate
    moved over the bond table's periods, in basis points (1W is not measured:
    the figures are monthly). YTD is against last December's rate."""
    out = []
    for t, n in INFLATION:
        h = upto(fred(t), fri)
        yoy = yoy12(h)
        m = yoy.index[-1]  # the latest month with a 12-month rate
        last = float(yoy.iloc[-1])
        # k calendar months back, or the nearest earlier month with a rate
        back = lambda k: round((last - float(yoy[yoy.index <= m - pd.DateOffset(months=k)].iloc[-1])) * 100, 2)
        dec = float(yoy[yoy.index <= pd.Timestamp(fri.year - 1, 12, 1)].iloc[-1])
        prev = m - pd.DateOffset(months=1)
        out.append({"t": t, "n": n, "month": str(m.date()), "yoy": round(last, 3), "prev": round(float(yoy[yoy.index <= prev].iloc[-1]), 3),
                    "mom": round((float(h[m]) / float(h[prev]) - 1) * 100, 3) if prev in h.index else None,
                    "bps": {"w": None, "m1": back(1), "m6": back(6), "ytd": round((last - dec) * 100, 2),
                            "y1": back(12), "y5": back(60), "y10": back(120)}})
        print(t, out[-1])
    return out


# The economy (owner, 2026-11-22): real GDP growth from the Bureau of Economic
# Analysis (quarterly, the change from the quarter before at an annual pace,
# the headline figure) and the unemployment rate from the Bureau of Labor
# Statistics (monthly), both through FRED, in the Rates table.
ECON = [("A191RL1Q225SBEA", "GDP Growth", True), ("UNRATE", "Unemployment", False)]


def econ(fri):
    """Each measure's latest reading and how far it moved over the bond table's
    periods, in basis points, like the inflation rows: k months before the
    reading's own month, or the nearest earlier reading (for GDP, the quarter
    that covers that month). 1W is not measured. YTD is against the last
    reading for last December or before."""
    out = []
    for t, n, q in ECON:
        h = upto(fred(t), fri)
        m, last = h.index[-1], float(h.iloc[-1])
        back = lambda k: round((last - float(h[h.index <= m - pd.DateOffset(months=k)].iloc[-1])) * 100, 2)
        dec = float(h[h.index <= pd.Timestamp(fri.year - 1, 12, 1)].iloc[-1])
        # The last four readings, so a run of shrinking quarters can be called
        # out (owner, 2026-11-22: two quarters of negative GDP growth in a row).
        out.append({"t": t, "n": n, "q": q, "month": str(m.date()), "last": last,
                    "hist": [[str(d.date()), float(v)] for d, v in h.iloc[-4:].items()],
                    "bps": {"w": None, "m1": back(1), "m6": back(6), "ytd": round((last - dec) * 100, 2),
                            "y1": back(12), "y5": back(60), "y10": back(120)}})
        print(t, out[-1])
    return out


def inflation_10y(fri):
    """The Inflation page's chart (owner, 2026-11-22): 10 years of monthly CPI
    and core CPI inflation over 12 months (BLS, CPIAUCSL and CPILFESL) and the
    Fed funds rate's monthly average (FEDFUNDS), all through FRED, ending at
    CPI's latest month, plus the 30, 10 and 2-year Treasury yields' monthly
    averages. A month the Fed funds average is not out for yet is
    left out of that line."""
    cpi, core, ff = yoy12(upto(fred("CPIAUCSL"), fri)), yoy12(upto(fred("CPILFESL"), fri)), upto(fred("FEDFUNDS"), fri)
    # Every calendar month to CPI's latest, with None where a series has no
    # rate (no October 2025 CPI, so no rate for it or for October 2026), so the
    # chart shows a gap, not a join.
    months = pd.date_range(end=upto(fred("CPIAUCSL"), fri).index[-1], periods=121, freq="MS")
    pick = lambda s: [[str(m.date())[:7], round(float(s[m]), 2) if m in s.index else None] for m in months]
    # Treasury yields for the page's second chart (owner, 2026-11-22): each
    # month's average of the daily 30, 10 and 2-year yields, over the same months.
    avg = lambda t: upto(fred(t), fri).resample("MS").mean()
    out = {"cpi": pick(cpi), "core": pick(core), "ff": pick(ff), "y30": pick(avg("DGS30")), "y10": pick(avg("DGS10")), "y2": pick(avg("DGS2"))}
    print("inflation_10y", {k: (v[0], v[-1], len(v), [m for m, x in v if x is None]) for k, v in out.items()})
    return out


# Built currency indexes: (Yahoo rate in units per dollar, scale). The yuan is
# US cents per yuan; the won, like the PHLX yen index, US cents per 100 won.
FX_INDEX = {"CNY-IDX": ("CNY=X", 100), "KRW-IDX": ("KRW=X", 10000)}


def prices(fri):
    prev, ye = fri - pd.Timedelta(days=7), pd.Timestamp(fri.year - 1, 12, 31)
    spans = spans_of(fri)
    rows = []
    for t, n, g in TICKERS:
        fund = g in FUNDS
        other = g in ("cmd", "oth")  # owner, 2026-11-15: the Returns table's periods too
        if t in FX_INDEX:
            src, k = FX_INDEX[t]
            h = k / closes(src, "11y", adjust=False)
        else:
            h = closes(t, "11y" if fund or other or g == "yld" else "2y", adjust=fund)
        cur = h if t in CRYPTO else upto(h, fri)
        last = float(cur.iloc[-1])
        r = dict(t=t, n=n, g=g, last=last, wk=at(h, prev), ye=at(h, ye), d=str(cur.index[-1].date()))
        if fund or other:  # total return (funds) or price change over each span; None when too young
            r["ch"] = {}
            for k, day in spans.items():
                s = upto(h, day)
                young = s.empty or (h.index[0] - day).days > 21
                r["ch"][k] = None if young else round((last / float(s.iloc[-1]) - 1) * 100, 4)
        r["range"] = range52(t, r["d"], last if t in CRYPTO else None) if fund or other else None
        if fund:
            r["tech"] = technicals(t, fri)
        elif other:  # gap to the 200-day average, for Status (owner, 2026-11-15)
            r["ma200"] = round((last / float(cur.iloc[-200:].mean()) - 1) * 100, 4) if len(cur) >= 200 else None
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
            "chart": [[str(d.date()), round(float(x), 2)] for d, x in year.items()],
            "all": vix_all(fri), "days_all": vix_days_all(fri)}


def vix_days_all(fri):
    """Trading days in each VIX zone over Yahoo's full daily history (1990 on),
    zoned as in vix_block (owner, 2026-11-15)."""
    zones = [0, 0, 0, 0, 0]
    for x in upto(closes("^VIX", "max", False), fri):
        zones[0 if x < 15 else 1 if x < 25 else 2 if x < 35 else 3 if x <= 45 else 4] += 1
    return zones


def vix_all(fri):
    """The VIX's weekly close (each week's last daily close) from the start of
    Yahoo's history (1990) to this Friday, for the all-time chart (owner,
    2026-11-15)."""
    v = upto(closes("^VIX", "max", False), fri).resample("W-FRI").last().dropna()
    return [[str(d.date()), round(float(x), 2)] for d, x in v.items()]


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
    d = {"rows": prices(fri) + fred_rows(fri) + muni(fri), "breakeven": breakeven(fri), "inflation": inflation(fri), "inflation_10y": inflation_10y(fri), "econ": econ(fri), "fetched": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
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
