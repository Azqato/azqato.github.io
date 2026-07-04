#!/usr/bin/env python3
"""
Refreshes the ETF-defined constituent lists the screener's Growth, Value,
Dividend, and International universes rank against:
  data/vug.json   -- top 100 holdings of VUG (Vanguard Growth ETF)
  data/vtv.json   -- top 100 holdings of VTV (Vanguard Value ETF)
  data/vig.json   -- top 100 holdings of VIG (Vanguard Dividend Appreciation ETF)
  data/vxus.json  -- top 100 holdings of VXUS (Vanguard Total International Stock ETF)

For VUG/VTV/VIG it fetches the full stock holdings from Vanguard's own profile
API (weight-sorted, refreshed monthly by Vanguard), applies the dual-class rule
(keep only the Class A voting share when a fund holds multiple classes), takes
the top 100 by weight, sanity-checks the result, preserves existing curated
short names, and writes the file only if membership actually changed. Prints
the add/remove diff so the GitHub Action commit message / log shows what moved.

Tickers are stored in display form (e.g. "BRK.B"); the data fetcher converts
the dot to a dash ("BRK-B") for Yahoo lookups.

VXUS is handled separately (see sync_vxus): its holdings report local-exchange
tickers with no exchange suffix and no US convention, so each holding is
identified by ISIN (which Vanguard's API returns directly) and resolved to a
suffixed Yahoo symbol via Yahoo's search endpoint. The resolution is cached in
data/vxus_map.json (ISIN -> Yahoo symbol) so a weekly sync only needs to
resolve newly-added holdings; a `manual` block in that file always overrides
the automatic resolution and is how a bad auto-resolution gets corrected.
Vanguard's raw holdings occasionally report the same ISIN as two separate
rows (observed for BHP Group and Barrick Gold); these are merged by summing
weight before ranking, so "top 100 by weight" means 100 distinct issuers.

Run weekly in CI alongside update_constituents.py. Dependencies: requests.
"""

import json
import re
import sys
import time

import requests

UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Accept": "application/json",
}

API = "https://investor.vanguard.com/investment-products/etfs/profile/api/{fund}/portfolio-holding/stock"
YAHOO_SEARCH = "https://query2.finance.yahoo.com/v1/finance/search"

# Duplicate share classes to drop, but only when the kept sibling is present.
# Convention matches the index lists: keep the Class A voting share, except
# Berkshire where the accessible B share is the one every list carries.
DUAL_CLASS = {"GOOG": "GOOGL", "FOX": "FOXA", "NWS": "NWSA", "BF.B": "BF.A",
              "HEI.A": "HEI", "BRK.A": "BRK.B", "LEN.B": "LEN"}

NAME_SUFFIXES = (
    ", Inc.", " Inc.", " Inc", " Corporation", " Corp.", " Corp", " Company",
    " plc", " PLC", " N.V.", " NV", " Ltd.", " Ltd", " S.A.", " SA", " & Co.",
    " AG", " SE", " ASA", " A/S", " KGaA", " SpA", " S.p.A.", " AB", " OYJ", " Oy", " GmbH",
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

# VXUS config: Vanguard's holdings API caps at exactly 500 entities for this
# fund (confirmed empirically 2026-07-03, not the ~8,500 VXUS actually holds),
# so the guard band is tight rather than the wide 110-500 used above.
VXUS_FUND = "VXUS"
VXUS_LIST_PATH = "data/vxus.json"
VXUS_MAP_PATH = "data/vxus_map.json"
VXUS_RAW_LO = 480
VXUS_RAW_HI = 520
# A Yahoo symbol looks like TICKER or TICKER.SUFFIX, where TICKER may contain
# digits (Asian local tickers) and letters (Western ones), and SUFFIX is a
# short exchange code -- much looser than the domestic BRK.B-style regex.
VXUS_SYMBOL_RE = re.compile(r"^[A-Z0-9-]{1,10}(\.[A-Z]{1,3})?$")


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


def fetch_vxus_raw():
    """Return VXUS holdings deduped by ISIN (weight summed), weight-sorted.

    Vanguard's raw response occasionally reports the same ISIN as two
    separate rows (observed for BHP Group and Barrick Gold) -- merge those
    before ranking so "top 100 by weight" means 100 distinct issuers, not
    a split holding occupying two slots.
    """
    r = requests.get(API.format(fund=VXUS_FUND), headers=UA, timeout=60)
    r.raise_for_status()
    entities = r.json()["fund"]["entity"]
    if not (VXUS_RAW_LO <= len(entities) <= VXUS_RAW_HI):
        sys.exit(f"ABORT [vxus]: unexpected raw holdings count {len(entities)} "
                 f"(expected {VXUS_RAW_LO}-{VXUS_RAW_HI}).")
    by_isin = {}
    for e in entities:
        isin = str(e.get("isin") or "").strip()
        if not isin:
            continue
        wt = float(e.get("percentWeight") or 0)
        if isin in by_isin:
            by_isin[isin]["weight"] += wt
        else:
            by_isin[isin] = {
                "isin": isin,
                "ticker": str(e.get("ticker") or "").strip(),
                "name": str(e.get("longName") or e.get("shortName") or "").strip(),
                "weight": wt,
            }
    rows = sorted(by_isin.values(), key=lambda x: -x["weight"])
    return rows[:TOP_N]


def yahoo_search(query):
    """Query Yahoo's search endpoint; return the EQUITY-type hits."""
    try:
        r = requests.get(YAHOO_SEARCH, params={"q": query}, headers=UA, timeout=20)
        r.raise_for_status()
        quotes = r.json().get("quotes", [])
    except Exception:
        return []
    return [q for q in quotes if q.get("quoteType") == "EQUITY" and q.get("symbol")]


def resolve_vxus_symbol(isin, name, manual, cache):
    """ISIN -> Yahoo symbol, via manual override, then cache, then live lookup.

    Live lookup tries ISIN search first (works for ~99% of holdings); falls
    back to a name search for the rare holding with no ticker in Vanguard's
    data (observed for Air Liquide). Returns None if nothing resolves --
    the caller aborts rather than writing a partial list.
    """
    if isin in manual:
        return manual[isin]
    if isin in cache:
        return cache[isin]
    hits = yahoo_search(isin)
    if not hits:
        hits = yahoo_search(name)
    time.sleep(0.3)
    return hits[0]["symbol"] if hits else None


def sync_vxus():
    raw = fetch_vxus_raw()

    try:
        vmap = json.load(open(VXUS_MAP_PATH, encoding="utf-8"))
    except Exception:
        vmap = {"manual": {}, "resolved": {}}
    manual = vmap.get("manual", {})
    cache = dict(vmap.get("resolved", {}))

    resolved = {}
    for item in raw:
        sym = resolve_vxus_symbol(item["isin"], item["name"], manual, cache)
        if not sym or not VXUS_SYMBOL_RE.match(sym):
            sys.exit(f"ABORT [vxus]: could not resolve a Yahoo symbol for "
                      f"{item['ticker']!r} / {item['isin']} ({item['name']}).")
        resolved[item["isin"]] = sym

    syms = list(resolved.values())
    if len(syms) != TOP_N:
        sys.exit(f"ABORT [vxus]: expected {TOP_N} holdings, got {len(syms)}.")
    if len(set(syms)) != len(syms):
        dupes = [s for s in syms if syms.count(s) > 1]
        sys.exit(f"ABORT [vxus]: duplicate resolved symbols {dupes} -- add a manual override.")

    try:
        old = json.load(open(VXUS_LIST_PATH, encoding="utf-8"))
    except Exception:
        old = []
    old_names = {x["t"]: x["n"] for x in old}
    old_syms = [x["t"] for x in old]

    listing = [{"t": resolved[item["isin"]], "n": old_names.get(resolved[item["isin"]]) or clean_name(item["name"])}
               for item in raw]

    # Cache write happens regardless of whether membership changed, so newly
    # resolved holdings are never re-resolved on the next run.
    with open(VXUS_MAP_PATH, "w", encoding="utf-8") as f:
        json.dump({"manual": manual, "resolved": resolved}, f, indent=2)
        f.write("\n")

    added = [s for s in syms if s not in old_syms]
    removed = [s for s in old_syms if s not in syms]
    if not added and not removed:
        print(f"[vxus] No constituent changes ({len(syms)} tickers).")
        return False

    with open(VXUS_LIST_PATH, "w", encoding="utf-8") as f:
        json.dump(listing, f, indent=2)
        f.write("\n")
    print(f"[vxus] Updated {VXUS_LIST_PATH}: {len(syms)} tickers. "
          f"Added: {added or 'none'}. Removed: {removed or 'none'}.")
    return True


def main():
    changed = False
    for name, cfg in FUNDS.items():
        if sync(name, cfg):
            changed = True
    if sync_vxus():
        changed = True
    # Exit 0 either way; the workflow inspects the git diff to decide what to do.
    if not changed:
        print("No constituent changes for any fund.")


if __name__ == "__main__":
    main()
