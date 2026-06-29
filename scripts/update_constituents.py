#!/usr/bin/env python3
"""
Refreshes data/nasdaq100.json from the live Nasdaq-100 index.

Fetches the constituent table from Wikipedia, applies the dual-class rule (keep
only the Class A voting share when a company has multiple classes in the index),
sanity-checks the result, preserves existing curated short names, and writes the
file only if membership actually changed. Prints the add/remove diff so the
GitHub Action commit message / log shows what moved.

Run weekly in CI. Dependencies: requests, pandas, lxml.
"""

import json
import re
import sys
from io import StringIO

import pandas as pd
import requests

LIST_PATH = "data/nasdaq100.json"
WIKI_URL = "https://en.wikipedia.org/wiki/Nasdaq-100"
UA = {"User-Agent": "azqato-stocks-bot/1.0 (https://azqato.github.io/stocks)"}

# Lower/no-vote share classes to drop, but only when their Class A sibling is present.
DUAL_CLASS = {"GOOG": "GOOGL", "FOX": "FOXA", "NWS": "NWSA"}

NAME_SUFFIXES = (
    ", Inc.", " Inc.", " Inc", " Corporation", " Corp.", " Corp", " Company",
    " plc", " PLC", " N.V.", " Ltd.", " Ltd", " S.A.",
)


def clean_name(n):
    n = str(n).strip()
    for suf in NAME_SUFFIXES:
        if n.endswith(suf):
            return n[: -len(suf)].rstrip(",").strip()
    return n


def fetch_constituents():
    html = requests.get(WIKI_URL, headers=UA, timeout=30).text
    for t in pd.read_html(StringIO(html)):
        tcol = next((c for c in t.columns if "Ticker" in str(c) or "Symbol" in str(c)), None)
        ncol = next((c for c in t.columns if "Company" in str(c) or "Name" in str(c)), None)
        if tcol is None or ncol is None or len(t) <= 50:
            continue
        rows = [(str(r[tcol]).strip().upper(), str(r[ncol]).strip()) for _, r in t.iterrows()]
        present = {s for s, _ in rows}
        out = []
        for sym, name in rows:
            if sym in DUAL_CLASS and DUAL_CLASS[sym] in present:
                continue  # drop the non-voting class, keep Class A
            out.append((sym, name))
        return out
    raise RuntimeError("Could not find the Nasdaq-100 components table on Wikipedia")


def main():
    fetched = fetch_constituents()
    syms = [s for s, _ in fetched]

    # --- sanity checks: never clobber the list on a bad scrape ---
    if not (90 <= len(syms) <= 105):
        sys.exit(f"ABORT: unexpected constituent count {len(syms)} (expected ~100).")
    if len(set(syms)) != len(syms):
        sys.exit("ABORT: duplicate tickers in fetched list.")
    bad = [s for s in syms if not re.match(r"^[A-Z][A-Z.]{0,5}$", s)]
    if bad:
        sys.exit(f"ABORT: suspicious tickers {bad}.")

    try:
        old = json.load(open(LIST_PATH, encoding="utf-8"))
    except Exception:
        old = []
    old_names = {x["t"]: x["n"] for x in old}
    old_syms = [x["t"] for x in old]

    # preserve curated short names for existing tickers; clean Wikipedia name for new ones
    listing = [{"t": s, "n": old_names.get(s) or clean_name(name)} for s, name in fetched]

    added = [s for s in syms if s not in old_syms]
    removed = [s for s in old_syms if s not in syms]
    if not added and not removed:
        print(f"No constituent changes ({len(syms)} tickers).")
        return

    with open(LIST_PATH, "w", encoding="utf-8") as f:
        json.dump(listing, f, indent=2)
        f.write("\n")
    print(f"Updated {LIST_PATH}: {len(syms)} tickers. "
          f"Added: {added or 'none'}. Removed: {removed or 'none'}.")


if __name__ == "__main__":
    main()
