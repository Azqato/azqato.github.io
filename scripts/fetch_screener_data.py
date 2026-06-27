#!/usr/bin/env python3
"""
Builds data/screener.json for the Nasdaq 100 screener (screener.html).

Runs in GitHub Actions on a daily cron. Uses yfinance (public Yahoo Finance
data) so there is no API key and no per-symbol subscription restriction -- the
whole Nasdaq 100 is refreshed every run.

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
    """Pull the analyst 'growth' value (a decimal) for a period row, e.g. '+1y'."""
    try:
        return num(df.loc[period, "growth"])
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

    rec["peFwd"] = num(info.get("forwardPE"))

    eps_fwd = None
    try:
        g = estimate_growth(t.earnings_estimate, "+1y")
        eps_fwd = g * 100 if g is not None else None
    except Exception:
        pass
    rec["epsFwd"] = eps_fwd

    rev_fwd = None
    try:
        g = estimate_growth(t.revenue_estimate, "+1y")
        rev_fwd = g * 100 if g is not None else None
    except Exception:
        pass
    rec["revFwd"] = rev_fwd

    if rec["peFwd"] is not None and eps_fwd is not None and eps_fwd > 0:
        rec["pegFwd"] = rec["peFwd"] / eps_fwd
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
