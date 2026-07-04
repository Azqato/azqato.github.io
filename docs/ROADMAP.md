# ROADMAP.md — Implementation Plans for Planned Releases

**Version:** 3.34.2
**Last Updated:** 2026-07-04

This document holds the detailed implementation plan for every item still open on the [PRD roadmap](PRD.md#roadmap). The PRD's milestone table remains the source of truth for **what** is planned and in what order; this file is the reference for **how** each item will be built. When a release ships, its plan here is trimmed to a pointer at the PRD milestone row and the PATCHNOTES entry.

Release order (updated 2026-07-04): v3.34.5 → v3.35.0 → v4.0.0 → v4.1.0 → v4.2.0 → v4.3.0 → v4.4.0 → v4.5.0. (v3.34.0 shipped 2026-07-04.)

---

## v3.34.5 — GitHub Actions Workflow Timing Review

### Goal

Owner requested review of when every GitHub Actions workflow runs and how much time sits between them, ahead of the next round of feature work — inserted as the immediate next step (before v3.35.0).

### Current schedule (compiled 2026-07-04, all times UTC)

| Order | Workflow | Cron | Days | Gap from previous |
|-------|----------|------|------|--------------------|
| 1 | Nasdaq 100 (`screener-data.yml`) | `0 23 * * 1-5` | Mon-Fri | — (first) |
| 2 | ETFs (`screener-data-etfs.yml`) | `15 23 * * 1-5` | Mon-Fri | 15 min |
| 3 | S&P 500 (`screener-data-sp500.yml`) | `30 23 * * 1-5` | Mon-Fri | 15 min |
| 4 | Growth/Value/Dividend (`screener-data-gvd.yml`) | `0 0 * * 2-6` | Tue-Sat (= Mon-Fri trading days, next calendar day) | 30 min |
| 5 | International (`screener-data-intl.yml`) | `15 0 * * 2-6` | Tue-Sat (= Mon-Fri trading days, next calendar day) | 15 min |
| 6 | Constituent sync (`constituents.yml`) | `0 23 * * 6` | Saturday only | ~23h (weekly, not daily) |

All six share the `screener-data` concurrency group with `cancel-in-progress: false`, so if one run is still going when the next is scheduled to start, GitHub queues the next one rather than running them in parallel or canceling either — a slow run delays the next job's actual start but never corrupts data or causes a race on the commit.

### Things worth the owner's attention (found while compiling the table above, not yet acted on)

1. **GitHub's cron scheduler is UTC-only and does not observe US daylight saving time** (this is already called out as a code comment in `screener-data.yml` but is easy to miss). `23:00 UTC` is **6:00pm US Eastern in winter (EST)** but **7:00pm Eastern in summer (EDT)** — the whole staggered chain silently shifts an hour twice a year relative to US market close (4:00pm Eastern), rather than staying pinned to "2-3 hours after close." If the owner wants the refresh to consistently land a fixed number of hours after the US close, the cron times need a DST-aware adjustment twice a year (there's no native DST cron support on GitHub Actions, so this would mean either two sets of cron lines swapped manually each March/November, or accepting the seasonal drift as-is, which is what today's setup does).
2. **The 15-minute gaps (steps 2→3 and 4→5) are tighter than the 30-minute gap (steps 3→4).** The ETFs job (10 symbols) and the International job (100 symbols, foreign listings, possibly slower per-symbol due to network latency to non-US exchanges' underlying data) are the two after each 15-minute gap — worth confirming neither one has historically run long enough to bump into the next job's start (GitHub Actions run logs would show actual durations; not checked as part of this review, since it wasn't asked for a data-driven audit, just the schedule layout).
3. **The Saturday constituent sync (23:00 UTC) lands at the same time-of-day as the Mon-Fri Nasdaq 100 job**, but on a day none of the daily jobs run, so there's no actual conflict — flagged only because it's easy to misread the table above as a same-day collision.

### Plan

1. Present the table and the three notes above to the owner for review.
2. If the owner wants changes (e.g., DST-aware scheduling, wider gaps, a different stagger order), make the corresponding cron edits and re-verify via `workflow_dispatch` manual runs before the next scheduled trigger.
3. If the owner confirms the current schedule is fine as-is, close this out with no code changes — the value was in having the compiled table for review, not necessarily in changing anything.

---

## v3.35.0 — Screener Methodology Audit & Table Display Fixes

### Goal

Two owner-flagged problems with the screener's Methodology popup: (1) the content needs a pass to confirm it's fully current against the shipped model (the popup has been edited five times in one day across v3.30.0-v3.34.0 — scoring model v2, S+ tier, margins removal, the ETF section, and the International row just added — so it needs a fresh read-through, not just trust that each edit was locally correct), and (2) real display problems: tables in the popup visually break with clipped content and text that doesn't wrap properly.

### Root cause found (code inspection, 2026-07-04)

`style.css`'s `.table-wrap` rule is self-contradictory:

```css
.table-wrap {
  overflow-x: auto;   /* intended: horizontal scrollbar for wide tables */
  margin-bottom: 6px;
  border: 1px solid var(--color-border);
  border-radius: 8px;
  overflow: hidden;    /* BUG: shorthand resets BOTH axes, silently cancels the line above */
}
```
`overflow` is shorthand for `overflow-x` + `overflow-y`; the later `overflow: hidden` wins in the cascade and overrides the `overflow-x: auto` three lines above for both axes. The practical effect: a methodology table wider than the modal (the pillar tables have 4 columns including a long "Better means"/description column, and the International row added in v3.34.0 has a long single-paragraph cell) doesn't get a horizontal scrollbar — its overflow is just **clipped and invisible**, with no visual indication anything is cut off. Compounding it, `thead th { white-space: nowrap; }` (style.css) keeps header cells from wrapping at all, so a narrow modal width (or a narrow viewport under the 1023px breakpoint) can force the clipping even on shorter tables. This one CSS bug is likely the whole "display issues with the tables" report; the plan below still includes a review pass in case there's more (e.g. long `<td>` copy that should wrap rather than scroll, which is a design choice, not just a bug fix).

### Plan

1. **Fix the CSS bug**: remove the trailing `overflow: hidden` from `.table-wrap` (or reorder so `overflow-x: auto` is declared last and `overflow-y` is set explicitly if hiding vertical overflow was actually intended — check whether any table relies on vertical clipping before just deleting the line). This one change affects every `.table-wrap` site-wide (metrics.html, indices.html, guide pages, not just the screener), so verify none of those depended on the accidental `hidden` behavior.
2. **Decide scroll vs. wrap per table**: the methodology's data tables (pillar weights, scoring curve, universe-source table) are naturally tabular and reasonable to let scroll horizontally on narrow viewports once the bug is fixed. But cells with long prose (the universe-source table's description column, e.g. the new International row) read better wrapping within a wider column than forcing the whole table into a horizontal scroll for one long sentence. Recommendation: keep scroll for the numeric/short-label tables, and either widen the description column or explicitly wrap long-text columns (`white-space: normal` already applies to plain `td`, so once the overflow bug is fixed this may resolve on its own — verify before adding overrides).
3. **Audit methodology content for currency against the shipped model**: read `#methodStock` and `#methodEtf` end-to-end against the current `METRICS`/`ETF_METRICS` arrays and scoring code in `screener.js`, checking in particular: the pillar weight tables still say Growth 60/Valuation 20/Balance 20 and Technicals 50/Performance 30/Income&Cost 20 (correct as of v3.31.0/v3.33.0 — verify no later edit drifted); the "S+" and tier-band language matches `computeTierMap`; the International row reads correctly next to the other four universe-source rows without breaking the table's tone; the worked PEG example's numbers are still representative of live data, not stale from whenever it was written.
4. **Visual polish pass beyond the bug fix**: with real content now spanning stock model + ETF model + six universe-source rows, re-check spacing, heading hierarchy, and mobile (under 1023px) rendering of the modal generally, since the modal's content volume has grown substantially since v3.29.0 without a matching visual review.

### Verification

- Headless Chrome screenshot or DOM check of the methodology modal in both stock and ETF mode, at a standard desktop width and at a narrow (~375px) mobile width, confirming no clipped table content and no unexpected horizontal scrollbars on tables that should wrap.
- Spot-check `metrics.html`/`indices.html`/guide pages (which also use `.table-wrap`) after the CSS fix to confirm no regression from removing the `overflow: hidden` line.

---

## v3.34.0 — Screener: International Universe (VXUS Top 100) — SHIPPED 2026-07-04

Fully built and verified; see [PRD.md](PRD.md#roadmap) (milestone table + Data Pipeline + Data Model sections) and [PATCHNOTES.md](PATCHNOTES.md) for the as-built record, including two data quirks the probe below didn't anticipate (a Vanguard split-ISIN duplicate and Yahoo's pence-not-pounds London quoting). The plan below is kept for historical reference.

<details>
<summary>Original plan (superseded by the as-built record above)</summary>

### Goal

A seventh screener universe: the top 100 holdings of VXUS (Vanguard Total International Stock ETF), scored with the **same six-metric stock model** as the other stock universes (Growth 60 / Valuation 20 / Balance sheet 20, hard-zero missing data, S+/S/A/B/C/F tiers). This is a stock universe, not an ETF universe: it reuses the stock table, columns, and scoring path with zero changes to the scoring math.

### Why this is its own release

Three problems the domestic universes never had, each needing its own solution:

1. **Symbol mapping.** Vanguard reports VXUS holdings with local-exchange tickers and no exchange suffix (`2330` for TSMC, `NESN` for Nestlé). Yahoo needs suffixed symbols (`2330.TW`, `NESN.SW`). A mapping layer is required.
2. **Currency display.** yfinance returns prices in each listing's local currency (TWD, CHF, JPY, EUR…). The screener's Price and Cash/Debt columns are currently formatted as dollars.
3. **Sparse analyst estimates.** Forward revenue/EPS estimates and PEG are thinner for foreign listings. Under the hard-zero rule, poor coverage could zero out 50 of 100 points for a large share of the list.

### Phase 0 — Probe (complete 2026-07-03)

Mirrored the approach that de-risked v3.33.0: verified empirically before writing production code. Findings:

1. **Vanguard holdings API shape.** The endpoint (`.../profile/api/VXUS/portfolio-holding/stock`) does **not** return all ~8,500 VXUS holdings — it caps at exactly **500** entities, weight-sorted. That's actually convenient (no pagination to build), but it changes the Phase 1 sanity-check band: the guard should assert **exactly 500** returned (or a tight band around it, e.g. 480-520), not the wide 110-500 band used for VUG/VTV/VIG. Every entity carries an **ISIN** directly (`"isin": "TW0002330008"`), plus a `sedol` field — no separate lookup call needed to get an identity key. Top-100-by-weight coverage sums to 37.4 of the fund's 65.5% visible weight in the 500-row response, consistent with a long, thin international tail below that.
2. **Symbol resolution ladder, tested on the real top 100 holdings:**
   - **Rung 1 — ISIN → Yahoo search** (`query2.finance.yahoo.com/v1/finance/search?q=<ISIN>`): resolved **99/100** with exactly one EQUITY hit each (2330 → `2330.TW`, NESN → `NESN.SW`, 8306 → `8306.T`, etc.). Three names returned more than one EQUITY match (dual-listing cases: Alibaba HK/Singapore, Siemens DE/Frankfurt-classic, Siemens Energy DE/Stuttgart) — first hit (primary listing) was correct in all three on inspection.
   - **Rung 2 — name search fallback**: the one ISIN miss (Air Liquide, `FR0000053951` — Vanguard's raw entity had a blank `ticker` field) resolved cleanly by name search to `AI.PA`, its primary Paris listing.
   - **Net result: 100/100 resolvable** with the two-rung ladder as planned. No case needed the market-cap/country validation step; it stays in as a guard for future weeks' new entrants, not because today's data needed it.
3. **Field coverage on the resolved top 100**, using the exact yfinance fields `fetch_screener_data.py` reads (not approximations): `revenueGrowth` (revTTM) 94/100, `earningsGrowth` (epsTTM) 88/100, current-FY `revenue_estimate` growth (revFwd) 100/100, current-FY `earnings_estimate` growth (epsFwd) 98/100, `pegRatio`/`trailingPegRatio` (pegFwd) 100/100, `totalCash`/`totalDebt` 100/100. **This resolves the sparse-estimates worry**: coverage is 88-100% across all six scored inputs, and because the hard-zero rule already applies **per metric, not per stock** (screener.js `activeMetrics()`/`ETF_METRICS` pattern: a missing input zeros only its own weight, the /100 denominator never shrinks), the worst case is roughly a dozen names losing 10 of 100 points on `epsTTM` alone — a minor haircut, not the "zero out 50 of 100 points" scenario the original concern envisioned.
4. **Currency diversity confirmed material**: even the top 15 holdings alone span TWD, KRW, EUR, GBP, JPY, CHF, HKD, CAD. This settles the currency-display decision in favor of the native-currency-with-label recommendation below — a single reporting currency was never realistic for this universe.

Deliverable (this section) presented to the owner 2026-07-03; Phase 3 decisions below are now data-backed rather than speculative.

### Phase 1 — Constituents and mapping

1. **`data/vxus.json`** — same `[{"t","n"}]` shape as the other lists, but `t` holds the **Yahoo symbol** (suffixed), so the data fetcher needs no special casing.
2. **`data/vxus_map.json`** (new, committed) — the resolution cache: Vanguard identity (ISIN, keyed off the `isin` field Vanguard already returns) → Yahoo symbol, plus a `manual` override block that the sync script always honors (seed it with the Air Liquide case and the three confirmed dual-listing picks found in the probe). This makes weekly syncs cheap (only newly added holdings need resolution) and makes bad auto-resolutions correctable by hand-editing one file.
3. **Extend `update_etf_constituents.py`** with a `vxus` entry: fetch holdings, take top 100 by weight, resolve each through the cache (hitting Yahoo search only for cache misses: ISIN first, name-search fallback second, per the tested ladder), apply the same never-clobber sanity checks (raw count in the 480-520 band per the probe finding above, no duplicates, plus a new check: every symbol must have resolved; abort rather than write a partial list). The existing ticker regex `^[A-Z][A-Z.]{0,5}$` must be relaxed for this fund only (digits and exchange suffixes: `2330.TW`, `005930.KS`, `AI.PA`).
4. Weekly sync joins the existing Saturday 23:00 UTC `constituents.yml` job.

### Phase 2 — Feed

1. Reuse **`scripts/fetch_screener_data.py`** unchanged if possible (`--list data/vxus.json --out data/screener_intl.json`); it already takes list/out arguments. Additions if needed: capture `info["currency"]` per ticker into a new feed field `cur`, and market cap left in native currency.
2. New workflow **`screener-data-intl.yml`**: Tue-Sat 00:15 UTC (15 minutes after the GVD job, keeping the stagger), same `screener-data` concurrency group, same pinned `yfinance==1.4.1`, `[skip ci]` commit.
3. Seed the feed with a local run before shipping, as with every prior universe.

### Phase 3 — Owner decisions (all locked 2026-07-03)

1. **Currency display — LOCKED: native currency, labeled with the currency symbol where one exists.** Numbers render in each stock's local currency using its **symbol**, not the 3-letter code, wherever a standard symbol exists (e.g. `NT$2,445` for TWD, `₩309,500` for KRW, `€284.10` for EUR, `£` for GBP, `¥` for JPY, `HK$` for HKD, `C$` for CAD). Fall back to the 3-letter ISO code (e.g. `CHF`) only for currencies with no widely recognized symbol or where the symbol is ambiguous with `$` alone (e.g. distinguish `HK$`/`NT$`/`C$` rather than a bare `$`, since the site's existing `$` always means USD elsewhere). No FX-rate feed dependency; scoring is unaffected either way — all six scored metrics are growth rates and ratios, currency-agnostic by construction.
2. **Sparse estimates — resolved by the probe, no owner decision needed.** Coverage on all six scored inputs is 88-100% (worst case `earningsGrowth`/epsTTM at 88/100). Keep the hard-zero rule exactly as-is: no shrunk denominator, no dropped names. The methodology popup gets one added sentence noting that a small number of international names may show a lower Factors count where Yahoo's analyst coverage is thin, same framing as the existing hard-zero note for domestic stocks.
3. **ADR preference — LOCKED: rank the local listing.** Rank the local listing that Vanguard actually holds (that's what the fund owns and what should be scored); use a liquid US ADR only as a manual-override fallback in `vxus_map.json` for the rare case where the local line has no Yahoo data at all — none of the top 100 needed this in the probe, so the fallback path may simply go unused at launch.

**All three Phase 3 gates are now clear. Phase 1 (constituents and mapping) can begin.**

### Phase 4 — Frontend

Small by design, because v3.33.0 pre-paid for it:

1. Add `intl` to `UNIVERSES` in `screener.js` with `kind` omitted (stock kind), paths to `screener_intl.json`, its own cache key. Seventh button in `screener.html` plus meta/disclaimer updates.
2. Thread the `cur` field (ISO code from `info["currency"]`) through `rows()` and the Price/Cash/Debt cell formatters for stock mode (no-op for feeds without `cur`, so the five domestic universes render exactly as before). Add a small `CURRENCY_SYMBOLS` lookup (ISO code → symbol: `TWD → "NT$"`, `KRW → "₩"`, `EUR → "€"`, `GBP → "£"`, `JPY → "¥"`, `HKD → "HK$"`, `CAD → "C$"`, `CHF` has no fallback so it prints the code, plus entries for any other currency the resolved top 100 turns up) so formatting is a plain object lookup, not per-currency branching logic. Unknown/unmapped codes fall back to printing the ISO code itself.
3. Methodology popup: one paragraph in the stock section's universe-source table (VXUS top 100, Vanguard holdings API, local listings, currency note, estimates-coverage note).

### Verification and acceptance

- Headless-Chrome check on the ETF universe pattern: all rows render, tier counts sum to 100, popup opens on a suffixed symbol (`.TW`, `.SW` in element IDs/selectors must not break — probe for selector-safety, dots in tickers already exist as `BRK.B` so `data-ticker` handling is likely fine but must be confirmed).
- **Stock regression is mandatory**: Nasdaq 100 headless run must still match the v3.31.0 baseline (2 S+ / 10 S / 8 A / 32 B / 24 C / 24 F, MU and NVDA at 100, subject to that day's data).
- Feed run completes 100/100 tickers with retries; nulls only where Yahoo genuinely has no data.
- All four docs updated; PATCHNOTES entry; PRD milestone flipped to Complete.

### Risks

- Vanguard may paginate or shape the VXUS response differently at ~8,500 holdings (the sibling funds return a few hundred). The probe settles this.
- Yahoo search rate limits during first-time resolution of 100 names: resolve with a pause and cache aggressively; this cost is paid once.
- yfinance field names for foreign listings can differ in reliability (the v3.33.0 lesson: verify `dividendYield`-class traps per field, per market, before trusting them).

</details>

---

## v4.0.0 — Screener Score History Sparklines

### Goal

A per-ticker score trend visual in the screener: a small inline sparkline column in the table and a larger score-history chart in the per-stock popup, mined from the git history of the committed data feeds. This is why the feeds live in git (PRD: reclassified as intentional design in v3.32.0).

### The central design fact

**The feeds store raw metrics, not scores.** Scores are computed client-side at render time. So "score history" cannot be read out of old files directly; it must be **recomputed** by replaying each historical feed snapshot through the scoring model. Two consequences:

1. The scoring model must be **ported to Python** (a second implementation). Parity risk is real and must be tested, not assumed.
2. A decision is forced about **which** model to replay (see decisions below), because the model itself changed over time (v3.21 percentile scoring → v3.30 model v2 → v3.31 six-metric weights).

### Phase 1 — History builder (`scripts/build_score_history.py`)

1. For each feed file (`screener.json`, `screener_sp500.json`, `screener_gvd.json`, `screener_etfs.json`):
   - `git log --reverse --format="%H %cI" -- data/<feed>` to enumerate snapshots; take at most one per calendar day (feeds commit once per trading day already).
   - `git show <sha>:data/<feed>` to read each snapshot without checkouts.
2. **Python port of the scoring model** (current model only): stock mode = percentile rank per metric across the loaded universe, 22% clamp, weights 10/20/10/20/20/20, hard-zero missing, sum /100; ETF mode = rank-linear points. GVD needs the same per-universe splitting the frontend does (score within Growth, Value, Dividend separately).
   - **Parity gate:** the port must reproduce today's live scores exactly. Test = run the Python scorer on the current feeds and diff against the headless-Chrome-rendered scores for all universes (the same harness used for the v3.33.0 regression). Any mismatch is a bug in the port; fix before mining history.
   - Old snapshots predate some fields (margins came and went; earlier feeds may lack fields entirely). The miner scores whatever fields exist under the current model's rules: a missing metric is a hard zero, same as live. Snapshots older than the six current fields will therefore show depressed scores; the window cap below makes this mostly moot.
3. **Output format** — `data/history.json` (or one file per universe if size demands): `{"updated": ..., "window": 90, "series": {"NVDA": [[<date>, <score>], ...]}}`, capped at the **last 90 trading days** per ticker. Budget check before committing to the format: ~750 unique tickers × 90 points ≈ small single-digit MB pretty-printed; minify (no indent) and it comfortably fits GitHub Pages. If it grows past ~2 MB, split per universe so the screener only fetches the active universe's history.
4. **Workflow**: extend each existing feed workflow with a final step that rebuilds history after committing the feed, or (cleaner, recommended) one new nightly workflow at 00:30 UTC Tue-Sat that runs once after all four feeds have landed, needs `fetch-depth: 0` (full clone; the feed workflows can stay shallow), and commits `data/history.json` with `[skip ci]`. Same concurrency group.

### Phase 2 — Frontend

1. **Trend column**: new narrow column (in the Snapshot group, next to Score) rendering an inline SVG polyline of the ticker's score series. Pure vanilla: one `<svg>` per row, points normalized to a fixed 0-100 y-scale so sparklines are comparable across rows; stroke colored by net direction (up = green token, down = red token, flat = muted). No axes, no libraries.
2. **Popup chart**: larger version in the per-stock popup with first/last score labels and the window ("last 90 trading days"). Same SVG approach.
3. **Loading**: history fetched lazily (after the main feed renders, non-blocking) with its own cache key; if the fetch fails the Trend column renders the missing glyph and everything else works. The Columns menu gets Trend as a toggleable column.
4. Methodology popup: a sentence on what the sparkline shows and the recompute-under-current-model caveat.

### Owner decisions to confirm before build

1. **Replay model**: recommend recomputing all history under the **current** model (consistent, comparable series). The alternative (as-shipped scores per era) is not reconstructible anyway; the historical rendered scores were never stored.
2. **Window**: recommend 90 trading days shown; the miner can be re-run with a bigger window later since git history keeps everything.
3. **Universes covered**: recommend all six including ETFs (rank-linear replays identically).
4. Whether Trend ships as a **major** version: yes as planned (v4.0.0), it introduces the first derived-data artifact and a new default column across every universe.

### Verification and acceptance

- Parity gate passes (Python scorer == headless JS scores, all universes, exact).
- History workflow green end-to-end in Actions; `history.json` size within budget.
- Headless check: sparkline SVG present per row, popup chart renders, history-fetch-failure path degrades gracefully (test by pointing the copy at a 404 path).
- Stock scoring regression baseline still holds (no scoring code changes in JS; the frontend change is render-only).

### Risks

- Scoring-port drift over time: any future scoring change must be made in **both** screener.js and the Python scorer. Mitigation: the parity test runs in the history workflow itself, so a drift fails CI loudly instead of silently mining wrong history.
- Early-history noise: feeds before v3.28 covered fewer universes and different fields. The 90-day window and hard-zero rule handle this without special cases.

---

## v4.1.0 — Deeper Index Fund Coverage

### Goal

Expand `indices.html` beyond the current core-index methodology with three new teaching sections: sector ETFs, international allocation, and the bond tent strategy. Content release: no screener, pipeline, or scoring changes.

### Plan

1. **Sector ETFs** — what sector funds are (XLK/XLV/XLE-class examples used descriptively, not as picks), how they concentrate risk relative to broad indices, how the methodology's timing signals (RSI, 52-week range, price vs 200DMA — now live in the ETFs screener universe) apply to them, and why they sit outside the core allocation.
2. **International allocation** — the case for and against ex-US exposure, VXUS as the broad instrument (cross-link to the v3.34.0 International screener universe once live), currency risk in plain English, and how the reader's home-country bias shows up in practice.
3. **Bond tent strategy** — what it is (rising bond allocation approaching a goal date, descending after), why it exists (sequence-of-returns risk, defined at first use per content rules), and how it interacts with the income-contribution investing model the site teaches.
4. Sequencing note: ship **after** v3.34.0 so the international section can link to the live International universe; the sector-ETF section already has the ETFs universe to point at.

### Mechanics (applies to all four content releases, v4.1.0-v4.4.0)

- Written for the primary persona (first-position investor): teach before asserting, define terms at first use, anchor to decisions the reader has faced.
- Content rules: no em dashes, no advice language (educational framing only, no buy/sell verbs aimed at the reader), examples are descriptive not prescriptive.
- Each new section gets: sidebar nav entry (IntersectionObserver hookup is automatic from the section markup pattern), FAQ page additions where a natural Q&A falls out, `sitemap.xml` lastmod bump, meta description review on the touched page.
- Docs per release: PATCHNOTES entry, PRD milestone flip, README page-count touch-ups if section counts are cited.
- Verification: headless render of the touched page, accordion/sidebar behavior intact, no console errors.

---

## v4.2.0 — Additional Illustrative Examples (Historical Market Events)

### Goal

Add worked historical examples across existing pages, showing the methodology applied to real, dated market episodes.

### Plan

1. Candidate episodes (owner to pick 3-5 at kickoff): the 2020 COVID crash and recovery (timing signals at the extreme), the 2021-2022 growth drawdown (what PEG/valuation flagged before it), the 2022-2023 rate cycle (cash-vs-debt pillar behavior), dot-com era NVDA/CSCO contrast (surviving a winner's drawdown), and a dividend-cut case study (what the balance sheet showed first).
2. Placement: each example embeds in the page whose concept it illustrates (metrics examples on `metrics.html`, timing examples on `indices.html`, temperament examples on `philosophy.html`) rather than a standalone examples page, so concepts and cases stay adjacent.
3. Format per example: dated setup (what was knowable then, hindsight explicitly flagged), the metric readings at the time, what the methodology's rules said, what happened, and the teaching point. Historical figures verified against at least one primary-ish source before publishing; approximate figures rounded and labeled approximate.
4. Constraint: examples must not read as track-record claims (no "this is what I bought"); they are illustrations of the rules, per the no-advice rule.
5. Mechanics per the shared checklist in v4.1.0.

---

## v4.3.0 — Additional Philosophy Sections

### Goal

Extend `philosophy.html` (currently 9 sections) with new conceptual material.

### Plan

1. Candidate sections (owner to pick at kickoff; these came out of prior roadmap discussion and PRD content-goals): when to sell (the hardest omission in most methodologies), position sizing and concentration for the income-contribution investor, drawdown temperament (what a 30% paper loss actually feels like and pre-committing behavior), the difference between conviction and stubbornness, and information diet (what to read daily vs quarterly vs never).
2. Each section follows the existing philosophy-page pattern: concept, first-person grounding, the practical rule that falls out of it, cross-links to the metric/page that operationalizes it.
3. FAQ additions for each new section (the FAQ page mirrors philosophy questions today).
4. Mechanics per the shared checklist in v4.1.0.

---

## v4.4.0 — Conference Call Research Guide

### Goal

A new setup-guide page (peer to `finviz.html` and `seekingalpha.html`) teaching how to research earnings conference calls: how to listen, what to note, how to log insights.

### Plan

1. **New page `conferencecalls.html`** following the existing guide-page pattern (step sections, sidebar nav, callout boxes): where calls live (IR pages, transcript sources incl. Seeking Alpha, cross-linking the existing guide), the anatomy of a call (prepared remarks vs Q&A and why Q&A matters more), what to listen for mapped to the site's six scored metrics (guidance vs the forward estimates the screener scores, margin commentary, balance-sheet language), red-flag phrasing patterns, and a simple insight log template (date, company, claim, metric affected, follow-up date).
2. Navigation: header/footer nav additions across all pages (the one release in this set that touches every HTML file), sitemap entry, og/meta for the new page.
3. Ties into the site loop: the guide should close the loop from screener score → "why is the forward estimate what it is" → hearing management's own version on the call.
4. Mechanics per the shared checklist in v4.1.0, plus: full-site headless spot check since nav on every page changes.

---

## v4.5.0 — Site-Wide Mobile-Friendliness Pass

### Goal

A dedicated review-and-fix pass for phone-width usage across every page, not just a spot fix. The site already has real responsive infrastructure (`<meta name="viewport">` present site-wide; sidebar nav collapses to a hamburger under 1024px in `style.css`; the screener's methodology modal drops to full width under 900px; the universe-switcher buttons already wrap via `flex-wrap`), so this is a **hardening and audit pass**, not a from-scratch mobile build.

### Known starting points (found by code inspection, 2026-07-04)

1. **The screener's main data table** (`.app-table-wrap`, `min-width: 900px` on the inner table) is deliberately horizontal-scroll on phones, which is a defensible choice for a dense data grid, but has never been reviewed for whether it's the *right* choice — e.g. whether the Ticker/Tier/Score columns should stick to the left edge while the rest scrolls, so a phone user always has orientation context. Worth a deliberate decision, not just inherited behavior.
2. **The universe switcher now has 7 buttons** (Nasdaq 100, S&P 500, Growth, Value, Dividend, ETFs, International, after v3.34.0) in a `flex-wrap` row — functional, but never checked for how many rows it wraps to on a 375px-wide phone or whether it pushes the summary/search controls down awkwardly.
3. **The methodology modal's tables** share the same `.table-wrap` component flagged in v3.35.0; that fix should land first since the mobile pass would otherwise be reviewing tables that are known-broken for an unrelated reason.
4. **Touch target sizing** has not been audited: chip filters, column-visibility checkboxes, and the sort-arrow click targets in table headers were sized for mouse pointers first.
5. **Content pages** (`philosophy.html`, `metrics.html`, `indices.html`, `finviz.html`, `seekingalpha.html`, `faq.html`) have a `max-width: 767px` breakpoint that shrinks headings and collapses the metric grid to one column, but has not been checked against real device widths (iPhone SE-class 375px vs. a larger phone) for anything beyond that one breakpoint.

### Plan

1. **Sequence after v3.35.0** (the table CSS bug fix), since fixing `.table-wrap` changes what "currently broken" looks like for both the methodology tables and any content-page tables this pass would otherwise flag as a mobile-specific issue.
2. **Device-width audit**: headless Chrome (or manual DevTools) pass at 375px, 414px, and 768px widths across all 9 pages (8 content + screener), cataloging concrete issues (not just "looks cramped") — overflow, overlapping elements, unreachable controls, text truncation that hides information.
3. **Screener-specific decisions**: whether to pin the Ticker/Tier/Score columns while scrolling the rest of the table; whether the universe-switcher should become a dropdown below some width instead of an ever-taller wrapped button grid; whether the Columns menu and search box need resizing on narrow widths.
4. **Fix and re-verify**: apply fixes page by page, re-running the same headless width audit to confirm each fix didn't regress desktop rendering (every page already works on desktop; this pass must not be a rewrite).

### Verification

- Headless Chrome screenshots or DOM checks at 375px/414px/768px for all 9 pages, before and after, kept as a before/after record in the PATCHNOTES entry.
- Confirm no desktop regression: full click-through of the screener (universe switch, sort, filter, popup, methodology modal) at the existing desktop width after the pass.

---

## Unversioned backlog (no plans yet by design)

- Growth/Value/Dividend standalone framework pages — remains backlog until the owner promotes it to a version.
- Explicitly not planned (owner decisions 2026-07-03): email/RSS changelog subscription, historical scoring backtests, options/crypto/forex coverage.
