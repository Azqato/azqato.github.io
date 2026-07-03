#!/usr/bin/env python3
"""
Refreshes the ETF-defined constituent lists the screener's Growth, Value, and
Dividend universes rank against:
  data/vug.json  -- top 100 holdings of VUG (Vanguard Growth ETF)
  data/vtv.json  -- top 100 holdings of VTV (Vanguard Value ETF)
  data/vig.json  -- top 100 holdings of VIG (Vanguard Dividend Appreciation ETF)

For each fund it fetches the full stock holdings from Vanguard's own profile
API (weight-sorted, refreshed monthly by Vanguard), applies the dual-class rule
(keep only the Class A voting share when a fund holds multiple classes), takes
the top 100 by weight, sanity-checks the result, preserves existing curated
short names, and writes the file only if membership actually changed. Prints
the add/remove diff so the GitHub Action commit message / log shows what moved.

Tickers are stored in display form (e.g. "BRK.B"); the data fetcher converts
the dot to a dash ("BRK-B") for Yahoo lookups.

Run weekly in CI alongside update_constituents.py. Dependencies: requests.
"""

import json
import re
import sys

import requests

UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Accept": "application/json",
}

API = "https://investor.vanguard.com/investment-products/etfs/profile/api/{fund}/portfolio-holding/stock"

# Duplicate share classes to drop, but only when the kept sibling is present.
# Convention matches the index lists: keep the Class A voting share, except
# Berkshire where the accessible B share is the one every list carries.
DUAL_CLASS = {"GOOG": "GOOGL", "FOX": "FOXA", "NWS": "NWSA", "BF.B": "BF.A",
              "HEI.A": "HEI", "BRK.A": "BRK.B", "LEN.B": "LEN"}

NAME_SUFFIXES = (
    ", Inc.", " Inc.", " Inc", " Corporation", " Corp.", " Corp", " Company",
    " plc", " PLC", " N.V.", " NV", " Ltd.", " Ltd", " S.A.", " & Co.",
)

TOP_N = 100

# Per-fund config: which fund to fetch, where to write, and the expected size
# band of the RAW holdings list (a guard so a bad response never clobbers a
# good list -- both funds hold comfortably more than 100 stocks).
FUNDS = {
    "vug": {"fund": "VUG", "path": "data/vug.json", "raw_lo": 110, "raw_hi": 500},
    "vtv": {"fund": "VTV", "path": "data/vtv.json", "raw_lo": 110, "raw_hi": 500},
    "vig": {"fund": "VIG", "path": "data/vig.json", "raw_lo": 110, "raw_hi": 500},
}


def clean_name(n):
    n = str(n).strip()
    for suf in NAME_SUFFIXES:
        if n.endswith(suf):
            return n[: -len(suf)].rstrip(",").strip()
    return n


def fetch_holdings(fund, raw_lo, raw_hi):
    """Return [(symbol, name), ...] weight-sorted from Vanguard's profile API."""
    r = requests.get(API.format(fund=fund), headers=UA, timeout=60)
    r.raise_for_status()
    entities = r.json()["fund"]["entity"]
    if not (raw_lo <= len(entities) <= raw_hi):
        sys.exit(f"ABORT [{fund}]: unexpected raw holdings count {len(entities)} "
                 f"(expected {raw_lo}-{raw_hi}).")
    rows = []
    for e in entities:
        sym = str(e.get("ticker") or "").strip().upper().replace(" ", "")
        name = str(e.get("longName") or e.get("shortName") or "").strip()
        wt = float(e.get("percentWeight") or 0)
        if sym and name:
            rows.append((wt, sym, name))
    rows.sort(key=lambda x: -x[0])  # the API is weight-sorted; make it explicit
    present = {s for _, s, _ in rows}
    out = []
    for _, sym, name in rows:
        if sym in DUAL_CLASS and DUAL_CLASS[sym] in present:
            continue  # drop the non-voting class, keep Class A
        out.append((sym, name))
    return out[:TOP_N]


def sync(name, cfg):
    raw = fetch_holdings(cfg["fund"], cfg["raw_lo"], cfg["raw_hi"])
    syms = [s for s, _ in raw]

    # --- sanity checks: never clobber the list on a bad fetch ---
    if len(syms) != TOP_N:
        sys.exit(f"ABORT [{name}]: expected {TOP_N} holdings after dedupe, got {len(syms)}.")
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

    # preserve curated short names for existing tickers; clean Vanguard name for new ones
    listing = [{"t": s, "n": old_names.get(s) or clean_name(nm)} for s, nm in raw]

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
    for name, cfg in FUNDS.items():
        if sync(name, cfg):
            changed = True
    # Exit 0 either way; the workflow inspects the git diff to decide what to do.
    if not changed:
        print("No constituent changes for any fund.")


if __name__ == "__main__":
    main()
