#!/usr/bin/env python3
"""
Builds data/screener.json for the Nasdaq 100 screener (screener.html).

Runs in GitHub Actions on a daily cron. Uses yfinance (public Yahoo Finance
data) so there is no API key and no per-symbol subscription restriction -- the
whole Nasdaq 100 is refreshed every run.

Forward metrics use the CURRENT fiscal-year ("0y") analyst consensus to match
Seeking Alpha's "FWD" convention (not yfinance's forwardPE / "+1y" rows, which
look a year further out). P/E FWD uses Yahoo's priceEpsCurrentYear and PEG FWD
uses Yahoo's pegRatio, both of which track Seeking Alpha. EPS Growth FWD is
GAAP-basis and will differ from SA's Non-GAAP figure.

Output schema matches what screener.html reads:
  { "updated": ISO, "source": "yahoo", "stocks": { TICKER: {...}, ... } }

Env:
  PAUSE   seconds to wait between symbols (default 0.8) -- be polite to Yahoo
"""

import datetime
import json
import os
import sys
import time

import yfinance as yf

LIST_PATH = "data/nasdaq100.json"
OUT_PATH = "data/screener.json"
PAUSE = float(os.environ.get("PAUSE", "0.8"))


def num(x):
    """Coerce to a finite float, else None."""
    try:
        f = float(x)
    except (TypeError, ValueError):
        return None
    if f != f or f in (float("inf"), float("-inf")):
        return None
    return f


def estimate_growth(df, period):
    """Pull the analyst 'growth' value (a decimal) for a period row, e.g. '0y'."""
    try:
        return num(df.loc[period, "growth"])
    except Exception:
        return None


def estimate_avg(df, period):
    """Pull the analyst average estimate (e.g. EPS or revenue) for a period row."""
    try:
        return num(df.loc[period, "avg"])
    except Exception:
        return None


def fetch(symbol):
    t = yf.Ticker(symbol)
    info = t.info or {}

    rec = {}
    rec["price"] = num(info.get("currentPrice")) or num(info.get("regularMarketPrice"))
    rec["marketCap"] = num(info.get("marketCap"))
    rec["cash"] = num(info.get("totalCash"))
    rec["debt"] = num(info.get("totalDebt"))

    rg = num(info.get("revenueGrowth"))
    rec["revTTM"] = rg * 100 if rg is not None else None
    eg = num(info.get("earningsGrowth"))
    rec["epsTTM"] = eg * 100 if eg is not None else None

    # Forward figures use the CURRENT fiscal-year ("0y") consensus estimate to
    # match Seeking Alpha's "FWD" convention. yfinance's forwardPE / "+1y" rows
    # are one fiscal year further out, which reads systematically too low.
    earn = None
    rev = None
    try:
        earn = t.earnings_estimate
    except Exception:
        pass
    try:
        rev = t.revenue_estimate
    except Exception:
        pass

    # P/E FWD: Yahoo's priceEpsCurrentYear (price / current-FY EPS) matches
    # Seeking Alpha's "P/E FWD" to the cent. Fall back to price / 0y estimate,
    # then to forwardPE.
    price = rec["price"]
    pe = num(info.get("priceEpsCurrentYear"))
    if pe is None:
        eps_cur = estimate_avg(earn, "0y")
        if price is not None and eps_cur is not None and eps_cur > 0:
            pe = price / eps_cur
        else:
            pe = num(info.get("forwardPE"))
    rec["peFwd"] = pe

    # Revenue / EPS Growth FWD = current-FY ("0y") consensus growth.
    # NOTE: EPS Growth FWD is GAAP-basis and will differ from Seeking Alpha,
    # which uses Non-GAAP consensus (not exposed by yfinance).
    eg_fwd = estimate_growth(earn, "0y")
    rec["epsFwd"] = eg_fwd * 100 if eg_fwd is not None else None
    rg_fwd = estimate_growth(rev, "0y")
    rec["revFwd"] = rg_fwd * 100 if rg_fwd is not None else None

    # PEG FWD: Yahoo's pegRatio incorporates a longer-term growth rate and
    # tracks Seeking Alpha's PEG (FWD) closely (SA's exact 3-5yr long-term
    # growth input is not exposed by yfinance). Fall back to trailingPegRatio,
    # then to the 1-yr forward PEG (P/E / EPS growth).
    peg = num(info.get("pegRatio"))
    if peg is None or peg == 0:
        peg = num(info.get("trailingPegRatio"))
    if (peg is None or peg == 0) and rec["peFwd"] is not None and rec["epsFwd"] not in (None, 0) and rec["epsFwd"] > 0:
        peg = rec["peFwd"] / rec["epsFwd"]
    rec["pegFwd"] = peg

    return rec


def main():
    with open(LIST_PATH, encoding="utf-8") as f:
        listing = json.load(f)

    now = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
    stocks = {}
    ok = 0

    for item in listing:
        sym = item["t"]
        rec = {"t": sym, "name": item["n"]}
        for attempt in range(3):
            try:
                rec.update(fetch(sym))
                rec["priceUpdated"] = now
                rec["fundamentalsUpdated"] = now
                if rec.get("price") is not None:
                    ok += 1
                break
            except Exception as e:  # noqa: BLE001 - keep going on any single-symbol failure
                if attempt == 2:
                    print(f"{sym}: failed after retries: {e!r}", file=sys.stderr)
                else:
                    time.sleep(2)
        stocks[sym] = rec
        time.sleep(PAUSE)

    out = {"updated": now, "source": "yahoo", "stocks": stocks}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
        f.write("\n")

    print(f"Wrote {OUT_PATH}: {ok}/{len(listing)} symbols with price data.")


if __name__ == "__main__":
    main()
