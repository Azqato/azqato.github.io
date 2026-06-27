#!/usr/bin/env python3
"""
Builds data/screener.json for the Nasdaq 100 screener (screener.html).

Runs in GitHub Actions on a daily cron. Uses yfinance (public Yahoo Finance
data) so there is no API key and no per-symbol subscription restriction -- the
whole Nasdaq 100 is refreshed every run.

Forward metrics (P/E FWD, Revenue/EPS Growth FWD) use the CURRENT fiscal-year
("0y") analyst consensus to match Seeking Alpha's "FWD" convention, rather than
yfinance's forwardPE / "+1y" rows which look one fiscal year further out.

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

    # P/E FWD = price / current-FY EPS estimate (falls back to forwardPE).
    price = rec["price"]
    eps_cur = estimate_avg(earn, "0y")
    if price is not None and eps_cur is not None and eps_cur > 0:
        rec["peFwd"] = price / eps_cur
    else:
        rec["peFwd"] = num(info.get("forwardPE"))

    # EPS / Revenue Growth FWD = current-FY ("0y") consensus growth.
    eg_fwd = estimate_growth(earn, "0y")
    rec["epsFwd"] = eg_fwd * 100 if eg_fwd is not None else None
    rg_fwd = estimate_growth(rev, "0y")
    rec["revFwd"] = rg_fwd * 100 if rg_fwd is not None else None

    # PEG (1-yr forward) = forward P/E / forward EPS growth %. NOTE: Seeking
    # Alpha's PEG divides by a 3-5yr long-term growth rate, which yfinance does
    # not expose; this is the 1-year forward approximation.
    if rec["peFwd"] is not None and rec["epsFwd"] is not None and rec["epsFwd"] > 0:
        rec["pegFwd"] = rec["peFwd"] / rec["epsFwd"]
    else:
        rec["pegFwd"] = None

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
