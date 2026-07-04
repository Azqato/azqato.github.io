# ROADMAP.md — Implementation Plans for Planned Releases

**Version:** 3.33.1
**Last Updated:** 2026-07-03

This document holds the detailed implementation plan for every item still open on the [PRD roadmap](PRD.md#roadmap). The PRD's milestone table remains the source of truth for **what** is planned and in what order; this file is the reference for **how** each item will be built. When a release ships, its plan here is trimmed to a pointer at the PRD milestone row and the PATCHNOTES entry.

Release order (committed 2026-07-03): v3.34.0 → v4.0.0 → v4.1.0 → v4.2.0 → v4.3.0 → v4.4.0.

---

## v3.34.0 — Screener: International Universe (VXUS Top 100)

### Goal

A seventh screener universe: the top 100 holdings of VXUS (Vanguard Total International Stock ETF), scored with the **same six-metric stock model** as the other stock universes (Growth 60 / Valuation 20 / Balance sheet 20, hard-zero missing data, S+/S/A/B/C/F tiers). This is a stock universe, not an ETF universe: it reuses the stock table, columns, and scoring path with zero changes to the scoring math.

### Why this is its own release

Three problems the domestic universes never had, each needing its own solution:

1. **Symbol mapping.** Vanguard reports VXUS holdings with local-exchange tickers and no exchange suffix (`2330` for TSMC, `NESN` for Nestlé). Yahoo needs suffixed symbols (`2330.TW`, `NESN.SW`). A mapping layer is required.
2. **Currency display.** yfinance returns prices in each listing's local currency (TWD, CHF, JPY, EUR…). The screener's Price and Cash/Debt columns are currently formatted as dollars.
3. **Sparse analyst estimates.** Forward revenue/EPS estimates and PEG are thinner for foreign listings. Under the hard-zero rule, poor coverage could zero out 50 of 100 points for a large share of the list.

### Phase 0 — Probe (build nothing until this is done)

Mirror the approach that de-risked v3.33.0: verify empirically before writing production code.

1. **Probe the Vanguard holdings API for VXUS** (`.../profile/api/VXUS/portfolio-holding/stock`, same endpoint `update_etf_constituents.py` uses). Record: raw holdings count (VXUS holds ~8,500 stocks, so the size-band guard needs a much wider window than the 110-500 used for VUG/VTV/VIG), and exactly which identity fields each entity carries (`ticker`, `longName`, and critically whether an **ISIN** or SEDOL field is present).
2. **Probe symbol resolution** for the actual top 100 by weight. Strategy ladder, stopping at the first rung that works:
   - If Vanguard provides ISINs: resolve ISIN → Yahoo symbol via Yahoo's search endpoint (`query2.finance.yahoo.com/v1/finance/search?q=<ISIN>`), which yfinance itself uses for ISIN lookups.
   - If not: resolve by company name search against the same endpoint, then validate the hit by comparing market cap / country.
   - Either way, expect a residue of ambiguous names (dual listings, ADR vs ordinary); these get manual overrides.
3. **Probe field coverage** on the resolved top 100 with yfinance: for each of the six scored inputs (Rev TTM/FWD, EPS TTM/FWD, PEG FWD, cash & debt) plus price/market cap, count how many of the 100 names return data. This number decides the sparse-estimates question (Phase 3).

Deliverable: a coverage report presented to the owner before any production code.

### Phase 1 — Constituents and mapping

1. **`data/vxus.json`** — same `[{"t","n"}]` shape as the other lists, but `t` holds the **Yahoo symbol** (suffixed), so the data fetcher needs no special casing.
2. **`data/vxus_map.json`** (new, committed) — the resolution cache: Vanguard identity (ISIN or ticker+name) → Yahoo symbol, plus a `manual` override block that the sync script always honors. This makes weekly syncs cheap (only newly added holdings need resolution) and makes bad auto-resolutions correctable by hand-editing one file.
3. **Extend `update_etf_constituents.py`** with a `vxus` entry: fetch holdings, take top 100 by weight, resolve each through the cache (hitting Yahoo search only for cache misses), apply the same never-clobber sanity checks (count, duplicates, plus a new check: every symbol must have resolved; abort rather than write a partial list). The existing ticker regex `^[A-Z][A-Z.]{0,5}$` must be relaxed for this fund only (digits and exchange suffixes: `2330.TW`, `RELIANCE.NS`).
4. Weekly sync joins the existing Saturday 23:00 UTC `constituents.yml` job.

### Phase 2 — Feed

1. Reuse **`scripts/fetch_screener_data.py`** unchanged if possible (`--list data/vxus.json --out data/screener_intl.json`); it already takes list/out arguments. Additions if needed: capture `info["currency"]` per ticker into a new feed field `cur`, and market cap left in native currency.
2. New workflow **`screener-data-intl.yml`**: Tue-Sat 00:15 UTC (15 minutes after the GVD job, keeping the stagger), same `screener-data` concurrency group, same pinned `yfinance==1.4.1`, `[skip ci]` commit.
3. Seed the feed with a local run before shipping, as with every prior universe.

### Phase 3 — Owner decisions (gate between probe and build)

To be put to the owner with the Phase 0 coverage report:

1. **Currency display.** Recommendation: keep numbers in native currency and label them (e.g. `2,485 TWD` or a `cur` suffix on the Price cell; Cash/Debt column already renders a ratio-like pair so the label matters less). Converting to USD adds an FX feed dependency for purely cosmetic benefit; scoring is unaffected either way because all six scored metrics are growth rates and ratios, which are currency-agnostic.
2. **Sparse estimates.** If probe coverage is decent (roughly 80%+ of names have forward estimates), recommendation: keep the hard-zero rule untouched, accept a larger F cohort, and say so in the methodology popup. If coverage is poor, the fallback options to present: score those names on the metrics they have with a shrunk denominator (breaks the fixed /100 rule), or drop chronically uncovered names below the top-100 cut. Do not decide this before seeing the data.
3. **ADR preference.** Where a top holding has a liquid US ADR (TSM, NVO, ASML…), using the ADR would give USD pricing and better estimate coverage, but changes what is actually being ranked (ADR vs local line). Recommendation: rank the local listing that Vanguard actually holds, use the ADR only as a manual-override fallback when the local line has no Yahoo data.

### Phase 4 — Frontend

Small by design, because v3.33.0 pre-paid for it:

1. Add `intl` to `UNIVERSES` in `screener.js` with `kind` omitted (stock kind), paths to `screener_intl.json`, its own cache key. Seventh button in `screener.html` plus meta/disclaimer updates.
2. If the currency decision lands on labeling: thread the `cur` field through `rows()` and the Price cell formatter for stock mode (no-op for feeds without `cur`, so the five domestic universes render exactly as before).
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

## Unversioned backlog (no plans yet by design)

- Growth/Value/Dividend standalone framework pages — remains backlog until the owner promotes it to a version.
- Explicitly not planned (owner decisions 2026-07-03): email/RSS changelog subscription, historical scoring backtests, options/crypto/forex coverage.
