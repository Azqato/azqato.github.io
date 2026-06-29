#!/usr/bin/env python3
"""
Refreshes the constituent lists the screener ranks against:
  data/nasdaq100.json  -- the live Nasdaq-100 index
  data/sp500.json      -- the live S&P 500 index

For each index it fetches the constituent table from Wikipedia, applies the
dual-class rule (keep only the Class A voting share when a company has multiple
classes in the index), sanity-checks the result, preserves existing curated
short names, and writes the file only if membership actually changed. Prints the
add/remove diff so the GitHub Action commit message / log shows what moved.

Tickers are stored in display form (e.g. "BRK.B"); the data fetcher converts the
dot to a dash ("BRK-B") for Yahoo lookups.

Run weekly in CI. Dependencies: requests, pandas, lxml.
"""

import json
import re
import sys
from io import StringIO

import pandas as pd
import requests

UA = {"User-Agent": "azqato-stocks-bot/1.0 (https://azqato.github.io/stocks)"}

# Lower/no-vote share classes to drop, but only when their Class A sibling is present.
DUAL_CLASS = {"GOOG": "GOOGL", "FOX": "FOXA", "NWS": "NWSA"}

NAME_SUFFIXES = (
    ", Inc.", " Inc.", " Inc", " Corporation", " Corp.", " Corp", " Company",
    " plc", " PLC", " N.V.", " Ltd.", " Ltd", " S.A.",
)

# Per-index config: where to scrape, where to write, and the expected size band
# (a guard so a bad scrape never clobbers a good list).
INDICES = {
    "nasdaq100": {
        "url": "https://en.wikipedia.org/wiki/Nasdaq-100",
        "path": "data/nasdaq100.json",
        "min_rows": 50,   # ignore small unrelated tables on the page
        "count_lo": 90,
        "count_hi": 105,
    },
    "sp500": {
        "url": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
        "path": "data/sp500.json",
        "min_rows": 400,
        "count_lo": 480,
        "count_hi": 515,
    },
}


def clean_name(n):
    n = str(n).strip()
    for suf in NAME_SUFFIXES:
        if n.endswith(suf):
            return n[: -len(suf)].rstrip(",").strip()
    return n


def fetch_constituents(url, min_rows):
    """Return [(symbol, name), ...] from the first plausible constituents table."""
    html = requests.get(url, headers=UA, timeout=30).text
    for t in pd.read_html(StringIO(html)):
        tcol = next((c for c in t.columns if "Ticker" in str(c) or "Symbol" in str(c)), None)
        ncol = next((c for c in t.columns if "Company" in str(c) or "Security" in str(c) or "Name" in str(c)), None)
        if tcol is None or ncol is None or len(t) <= min_rows:
            continue
        # Wikipedia uses dotted classes (BRK.B); Yahoo wants a dash, but we store
        # the display form and convert at fetch time.
        rows = [(str(r[tcol]).strip().upper().replace(" ", ""), str(r[ncol]).strip())
                for _, r in t.iterrows()]
        present = {s for s, _ in rows}
        out = []
        for sym, name in rows:
            if sym in DUAL_CLASS and DUAL_CLASS[sym] in present:
                continue  # drop the non-voting class, keep Class A
            out.append((sym, name))
        return out
    raise RuntimeError(f"Could not find a constituents table at {url}")


def sync(name, cfg):
    fetched = fetch_constituents(cfg["url"], cfg["min_rows"])
    syms = [s for s, _ in fetched]

    # --- sanity checks: never clobber the list on a bad scrape ---
    if not (cfg["count_lo"] <= len(syms) <= cfg["count_hi"]):
        sys.exit(f"ABORT [{name}]: unexpected constituent count {len(syms)} "
                 f"(expected {cfg['count_lo']}-{cfg['count_hi']}).")
    if len(set(syms)) != len(syms):
        sys.exit(f"ABORT [{name}]: duplicate tickers in fetched list.")
    bad = [s for s in syms if not re.match(r"^[A-Z][A-Z.]{0,5}$", s)]
    if bad:
        sys.exit(f"ABORT [{name}]: suspicious tickers {bad}.")

    path = cfg["path"]
    try:
        old = json.load(open(path, encoding="utf-8"))
    except Exception:
        old = []
    old_names = {x["t"]: x["n"] for x in old}
    old_syms = [x["t"] for x in old]

    # preserve curated short names for existing tickers; clean Wikipedia name for new ones
    listing = [{"t": s, "n": old_names.get(s) or clean_name(nm)} for s, nm in fetched]

    added = [s for s in syms if s not in old_syms]
    removed = [s for s in old_syms if s not in syms]
    if not added and not removed:
        print(f"[{name}] No constituent changes ({len(syms)} tickers).")
        return False

    with open(path, "w", encoding="utf-8") as f:
        json.dump(listing, f, indent=2)
        f.write("\n")
    print(f"[{name}] Updated {path}: {len(syms)} tickers. "
          f"Added: {added or 'none'}. Removed: {removed or 'none'}.")
    return True


def main():
    changed = False
    for name, cfg in INDICES.items():
        if sync(name, cfg):
            changed = True
    # Exit 0 either way; the workflow inspects the git diff to decide what to do.
    if not changed:
        print("No constituent changes for any index.")


if __name__ == "__main__":
    main()
