#!/usr/bin/env python3
"""
Builds a screener data feed from a constituent list.

Runs in GitHub Actions on a daily cron. Uses yfinance (public Yahoo Finance
data) so there is no API key and no per-symbol subscription restriction -- the
whole list is refreshed every run.

Three feeds are produced by three staggered runs so the Nasdaq 100 (the
screener's default view) always refreshes first and never waits on the larger
jobs:
  --list data/nasdaq100.json --out data/screener.json          (23:00 UTC)
  --list data/sp500.json     --out data/screener_sp500.json     (23:30 UTC)
  --combined growth=data/vug.json --combined value=data/vtv.json \
      --combined dividend=data/vig.json --out data/screener_gvd.json  (00:00 UTC)
Defaults reproduce the original Nasdaq 100 behavior when run with no args.

Combined mode bundles several universes into one feed file, keyed by universe
name, with each universe holding the same {updated, source, stocks} object a
single-list feed has. Symbols appearing in more than one universe (the Growth,
Value, and Dividend lists overlap heavily) are fetched from Yahoo only once
per run.

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

import argparse
import datetime
import json
import os
import sys
import time

import yfinance as yf

DEFAULT_LIST = "data/nasdaq100.json"
DEFAULT_OUT = "data/screener.json"
PAUSE = float(os.environ.get("PAUSE", "0.8"))


def yahoo_symbol(sym):
    """Yahoo uses a dash for share classes that Wikipedia writes with a dot."""
    return sym.replace(".", "-")


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
    t = yf.Ticker(yahoo_symbol(symbol))
    info = t.info or {}

    rec = {}
    rec["price"] = num(info.get("currentPrice")) or num(info.get("regularMarketPrice"))
    rec["marketCap"] = num(info.get("marketCap"))
    rec["cash"] = num(info.get("totalCash"))
    rec["debt"] = num(info.get("totalDebt"))

    # Daily change: latest price vs the prior session's close. The pipeline runs
    # after the US close, so this is that trading day's move.
    prev = num(info.get("regularMarketPreviousClose")) or num(info.get("previousClose"))
    rec["prevClose"] = prev
    if rec["price"] is not None and prev not in (None, 0):
        rec["changePct"] = (rec["price"] / prev - 1) * 100
    else:
        rec["changePct"] = None

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


def build_stocks(listing, now, cache):
    """Fetch every symbol in a listing, reusing records already fetched this run."""
    stocks = {}
    ok = 0
    for item in listing:
        sym = item["t"]
        if sym in cache:
            rec = dict(cache[sym])
            rec["name"] = item["n"]  # each list keeps its own curated name
            stocks[sym] = rec
            if rec.get("price") is not None:
                ok += 1
            continue
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
        cache[sym] = rec
        time.sleep(PAUSE)
    return stocks, ok


def main():
    ap = argparse.ArgumentParser(description="Build a screener data feed from a constituent list.")
    ap.add_argument("--list", dest="list_path", default=DEFAULT_LIST,
                    help=f"constituent list JSON (default {DEFAULT_LIST})")
    ap.add_argument("--combined", action="append", default=[], metavar="NAME=LIST",
                    help="bundle several universes into one feed keyed by NAME "
                         "(repeatable, e.g. --combined growth=data/vug.json); overrides --list")
    ap.add_argument("--out", dest="out_path", default=DEFAULT_OUT,
                    help=f"output feed JSON (default {DEFAULT_OUT})")
    args = ap.parse_args()

    now = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
    cache = {}  # symbol -> fetched record, shared across universes in one run

    if args.combined:
        universes = {}
        totals = []
        for spec in args.combined:
            name, _, list_path = spec.partition("=")
            if not name or not list_path:
                sys.exit(f"Bad --combined spec {spec!r}; expected NAME=LIST.")
            with open(list_path, encoding="utf-8") as f:
                listing = json.load(f)
            stocks, ok = build_stocks(listing, now, cache)
            universes[name] = {"updated": now, "source": "yahoo", "stocks": stocks}
            totals.append(f"{name} {ok}/{len(listing)}")
        out = {"updated": now, "source": "yahoo", "universes": universes}
        summary = "; ".join(totals)
    else:
        with open(args.list_path, encoding="utf-8") as f:
            listing = json.load(f)
        stocks, ok = build_stocks(listing, now, cache)
        out = {"updated": now, "source": "yahoo", "stocks": stocks}
        summary = f"{ok}/{len(listing)}"

    with open(args.out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
        f.write("\n")

    print(f"Wrote {args.out_path}: {summary} symbols with price data.")


if __name__ == "__main__":
    main()
