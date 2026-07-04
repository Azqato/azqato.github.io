# ROADMAP.md — Implementation Plans for Planned Releases

**Version:** 3.34.12
**Last Updated:** 2026-07-04

This document holds the detailed implementation plan for every item still open on the [PRD roadmap](PRD.md#roadmap). The PRD's milestone table remains the source of truth for **what** is planned and in what order; this file is the reference for **how** each item will be built. When a release ships, its plan here is trimmed to a pointer at the PRD milestone row and the PATCHNOTES entry.

Release order (updated 2026-07-04): **v4.0.0 (reprioritized to the front)** → v3.35.0 → v3.36.0 → v3.37.0 (unscoped) → v4.1.0 → v4.2.0 → v4.3.0 → v4.4.0 → v4.5.0. (v3.34.0, v3.34.5, v3.34.6, v3.34.7, and v3.34.8 shipped 2026-07-04.)

---

## v3.34.10 — Screener: Scrollbar Undiscoverable/Invisible at Narrower Widths — SUPERSEDED BY v4.0.0

Diagnosis performed 2026-07-04 (kept below for the record); the fix itself never shipped. After the owner clarified the actual requirement is "the table should reflow/adapt so scrolling is never needed, not just that the existing scrollbar becomes easier to find," this item's scope was folded entirely into a reprioritized v4.0.0 (see below), since a scrollbar-visibility patch would be moot once the table auto-hides columns to fit instead of overflowing. The diagnosis below remains useful background for *why* v4.0.0 needed to happen now instead of later.

<details>
<summary>Original diagnosis (2026-07-04, read-only, no code shipped)</summary>

The v3.34.8 fix resolved the *sizing* bug (the table-wrap escaping its container) but did not fully resolve the reported issue: the table still becomes unreachable past a certain window width, for more than one person and more than one browser. Two further reports the same day, both after v3.34.8 shipped:
1. The original friend, on **Opera**, still can't scroll the ETFs table (only 10 rows — rules out vertical-height/row-count as a factor) at their native 1280×1024 resolution, maximized.
2. The owner, on **Chrome** (Incognito), reports that narrowing the browser window from the right causes the table and toolbar to stop scaling — the table just cuts off after a point, with no visible way to reach the rest.

**Diagnosis:**
1. Confirmed the v3.34.8 fix is live on the deployed site (`min-height: 0` on `.app-table-wrap`, `minmax(0, 1fr)` on `.site-layout` both present) — rules out stale cache/deployment lag.
2. Reproduced both reports' exact widths in headless Chrome against the live site (1280×1024 for the Opera report; a sweep from 1030px to 1400px for the Chrome resize report) — the scrollbar renders correctly and the box is properly sized at every width tested. Strong evidence the box-sizing bug is genuinely fixed.
3. Headless Chromium was not reproducing what two different real users, on two different Chromium-family browsers, were both experiencing — pointing at Chrome/Opera's default `overflow: auto` scrollbar rendering as a thin overlay that only appears on hover/active scrolling (invisible in a static look, and in every headless screenshot). Confirmed via a separate check: the `.app-toolbar` row (chips, Columns/Methodology buttons) already wraps correctly onto a second line at narrow widths in headless Chrome (`flex-wrap: wrap` working as designed) — the site's existing responsive infrastructure works; it's specifically the *table's* horizontal-scroll affordance that's undiscoverable.
4. The drafted (never-shipped) fix was: a persistently-visible non-overlay scrollbar via `::-webkit-scrollbar` styling, a wheel-to-horizontal-scroll redirect, and a right-edge fade affordance. **Superseded** — see v4.0.0.

</details>

---

## v3.37.0 — ETFs Universe: Rating Methodology Review — UNSCOPED, AWAITING OWNER INPUT

Owner flagged 2026-07-04 that the ETFs universe scoring methodology (v3.33.0: Technicals 50 / Performance 30 / Income & cost 20, rank-linear points across the fixed 10-fund list) needs a review. **No specifics given yet** — the owner will prompt with exactly what to address in a follow-up message. Placeholder only: do not start design or implementation work on this until scoped. Given as the immediate concern to the owner, this is a strong candidate to move to the front of the queue once scoped, ahead of v3.35.0/v3.36.0, but its actual position depends entirely on what the review turns up.

---

## v3.34.8 — Screener: Horizontal Scroll Broken at Some Resolutions — DONE 2026-07-04

A friend of the owner's reported the screener table couldn't be scrolled left/right on their machine — the table simply cut off after the Growth/Valuation columns with no visible way to reach the rest, no scrollbar, no response to scroll gestures. Diagnosed and fixed the same day. **Kept as its own standalone bug-fix item, not folded into v4.0.0's mobile-friendliness pass** — this is a desktop-resolution CSS correctness bug (an existing feature silently breaking at certain DPI/zoom/window-size combinations), not a design question about phone-width layout; it needed to ship immediately rather than wait behind a broader redesign pass.

### Root cause (two compounding bugs, both classic CSS gotchas)

1. **Nested flexbox `min-height:auto`**: `.app` is `display:flex; flex-direction:column; height:100vh`, and `.app-table-wrap` (the `flex:1` child that owns the table's own scrolling) had no `min-height: 0`. A flex item's default `min-height` is `auto`, which for a large-content scroll container resolves to "big enough to fit all the content" rather than "shrink to the space I was actually given" — so the box overflowed its flex parent (fixed at `height: 100vh`) instead of triggering its own internal `overflow: auto` scrollbars. Since `body { overflow: hidden }` (screener.html relies on the app owning its own scroll regions), that overflow became invisible and unreachable.
2. **CSS Grid implicit `min-width:auto`**: the shared `.site-layout` (used by every page, in `style.css`) declares `grid-template-columns: var(--sidebar-width) 1fr` — a bare `1fr` track has an implicit minimum size equal to its content's intrinsic width, not 0. The screener's wide table (20+ columns) could force the whole `1fr` grid column, and therefore the page, wider than the viewport, again trapped by `overflow: hidden`.

Both are well-documented, browser-rounding-sensitive edge cases — exactly why this "worked on my machine" (the owner's) but broke on a different resolution: DPI scaling, zoom level, and window width all shift where the flex/grid sizing math lands relative to the content's intrinsic size, so the same page can render fine at one resolution and silently clip at another.

### Fix

- `screener.html`: added `min-height: 0;` to `.app-table-wrap`.
- `style.css`: changed `.site-layout`'s grid-template-columns from `var(--sidebar-width) 1fr` to `var(--sidebar-width) minmax(0, 1fr)`. This is a site-wide shared rule but the change is a no-op for every other page (none of them have content wide enough to hit the implicit-minimum edge case) — only the screener's table exercises the difference.

### Verified

Headless Chrome screenshots at a constrained 1366×700 viewport (simulating reduced usable height from browser chrome/taskbar), before and after:
- **Before** (bug reproduced by temporarily reverting both fixes): table clipped after the Valuation column group, chip filter counts cut off mid-row, no horizontal scrollbar visible anywhere, Columns/Methodology buttons not reachable.
- **After** (fix applied): full horizontal scrollbar visible at the bottom of the table (classic Windows-style, with arrow buttons and a draggable thumb), entire table and toolbar reachable.

---

## v3.34.5 — GitHub Actions Workflow Timing Review — DONE 2026-07-04

Owner requested review of when every GitHub Actions workflow runs and how much time sits between them. Reviewed and re-scheduled the same day; two owner decisions and the resulting schedule are below.

### Owner decisions

1. **DST**: keep a fixed (non-DST-aware) cron schedule — do not swap cron lines twice a year. But instead of anchoring to a fixed Eastern-clock offset (the old approach, which silently shifted the buffer-after-close by an hour each season), **anchor 30 minutes after the *latest possible* US market close in UTC terms**. Market close is always 4:00pm US Eastern: 21:00 UTC in winter (EST, UTC-5), only 20:00 UTC in summer (EDT, UTC-4) — winter is later in UTC. Anchoring the first job at 21:30 UTC (30 min after the winter close) guarantees at least a 30-minute buffer after close in every season, growing to 90 minutes in summer.
2. **Gap spacing**: widen every gap in the chain to a uniform 30 minutes (up from the original 15/15/30/15 mix).

### Old vs. new schedule (all times UTC)

| Workflow | Old cron | New cron | Old gap | New gap |
|----------|----------|----------|---------|---------|
| Nasdaq 100 (`screener-data.yml`) | 23:00, Mon-Fri | **21:30, Mon-Fri** | — | — |
| ETFs (`screener-data-etfs.yml`) | 23:15, Mon-Fri | **22:00, Mon-Fri** | 15 min | 30 min |
| S&P 500 (`screener-data-sp500.yml`) | 23:30, Mon-Fri | **22:30, Mon-Fri** | 15 min | 30 min |
| Growth/Value/Dividend (`screener-data-gvd.yml`) | 00:00, Tue-Sat (next day) | **23:00, Mon-Fri (same day)** | 30 min | 30 min |
| International (`screener-data-intl.yml`) | 00:15, Tue-Sat (next day) | **23:30, Mon-Fri (same day)** | 15 min | 30 min |
| Constituent sync (`constituents.yml`) | 23:00, Saturday | 23:00, Saturday (unchanged) | weekly | weekly |

A side benefit of the new anchor: since the whole chain now fits between 21:30 and 23:30 UTC, every daily job lands on the **same calendar day** — the Tue-Sat day-rollover cron pattern the GVD/International jobs needed under the old schedule is gone, and their crons simplified back to a plain `1-5` (Mon-Fri) like the others.

All six still share the `screener-data` concurrency group with `cancel-in-progress: false` (unchanged): if one run is still going when the next is scheduled to start, GitHub queues the next one rather than racing or canceling.

### Shipped

All five daily workflow files updated (`screener-data.yml`, `screener-data-etfs.yml`, `screener-data-sp500.yml`, `screener-data-gvd.yml`, `screener-data-intl.yml`), plus the `constituents.yml` comment noting the new same-day window. Docs (README, PRD pipeline section + architecture diagram + folder structure + FAQ) updated to match.

---

## v3.34.6 — International Feed: Same-Company Duplicate Holdings — DONE 2026-07-04

Owner-flagged bug fixed the same day: `005930.KS` (Samsung Electronics common) and `005935.KS` (Samsung Electronics preferred) were both in the top-100 list under different ISINs, so the v3.34.0 dedup (built only for literal duplicate-ISIN rows like BHP/Barrick) never caught it.

### Full scope found

Scanned the full ~500-row raw Vanguard response by name-normalization (stripping legal suffixes, class markers, preference-share wording) and hand-verified every candidate — this confirmed the plan's caution against automatic name-matching was warranted: the same heuristic that correctly flagged Samsung also flagged **SoftBank Group Corp vs. SoftBank Corp**, which are genuinely different, separately-traded companies (parent holding company vs. its separately-listed telecom subsidiary) — a real false positive that would have wrongly merged two distinct securities if the matching had been automatic rather than hand-checked. Three real categories of same-company duplication were found:

1. **A duplicate custody record for the identical security** (not a different share class at all): Air Liquide, L'Oreal, and Engie each had one normal-ticker line and one **blank-ticker** line (Vanguard's shortName for the blank one ends "-PRIM" for Air Liquide) — almost certainly a French registered/bearer-share settlement split reported as two rows by Vanguard's custodian. Fix: sum the weight into the ticker-bearing line, drop the blank one.
2. **A real dual share class**: Samsung Electronics common/preferred, Investor AB Class A/B, Atlas Copco Class A/B. Fix: keep the higher-weighted (more liquid) class, matching the domestic `DUAL_CLASS` convention.
3. **A dual listing of the same underlying group across exchanges**: Rio Tinto's London (plc)/Australia (Ltd) listings, CATL's Hong Kong/Shenzhen listings (tie-broken by raw market value, not the rounded percentWeight, since both showed 0.04%). Fix: keep the higher-weighted listing.

### Implementation

Added `VXUS_SAME_ISSUER_MERGE` to `update_etf_constituents.py` — a hand-verified `{kept_isin: [dropped_isin, ...]}` map (8 entries, all three categories above), applied in `fetch_vxus_raw()` immediately after the existing exact-ISIN dedup and before the top-100 cut: each dropped ISIN's weight is summed into its kept ISIN, then removed entirely. No automatic name-matching ships in production code — exactly per the plan's caution, validated by the SoftBank false positive.

### Result

Rebuilding `data/vxus.json` against the live Vanguard API: Samsung preferred (`005935.KS`) dropped as expected, and correctly-combined weights promoted **L'Oreal** (`OR.PA`, 0.07%+0.14%=0.21%) and **Investor AB** (`INVE-B.ST`, 0.16%+0.04%=0.20%) into the true top 100, bumping out two lower-weighted names that had been ranked ahead of them under the old split-weight accounting (only Rio Tinto's Australian listing and CATL's Shenzhen listing were already below the cutoff on either side, so those two merges didn't change today's membership, just future-proof it). `data/vxus_map.json`'s now-unreachable manual override for Air Liquide's dropped ISIN was removed. `screener.js`'s `CURRENCY_SYMBOLS` gained `SEK` (Investor AB introduced Swedish krona to the feed).

### Verified

- `data/vxus.json`: 100 entries, 100 unique symbols, exactly one Samsung Electronics entry (Samsung Electro-Mechanics correctly remains separate — it's a genuinely different company).
- Headless Chrome: 100/100 rows rendered, no duplicate company names, tiers sum to 100.
- `sync_vxus()` re-run against the live Vanguard API twice (once before, once after removing the dead manual override) both reproduced the corrected list with zero further changes — full idempotency confirmed.

---

## v3.34.7 — International Universe: Lead with Company Name, Not Ticker — DONE 2026-07-04

Owner-requested display change shipped the same day, following the plan below exactly.

### Implementation

- **`UNIVERSES.intl`** gained `nameFirst: true` (absent/falsy on all five domestic universes, so nothing about them changes — verified below).
- **`screenCells(r)`** now checks `isNameFirst()` and, when true, swaps both the DOM order (name span first, for screen readers) and adds a `name-first` class to the `<td class="col-ticker">` cell.
- **CSS** (`screener.html`): new `.col-ticker.name-first .tkr-name` / `.tkr` rules swap which span gets the prominent styling (name: bold, proportional font, primary text color; ticker: small, muted, keeps the inherited monospace from `tbody td`). The 720px mobile breakpoint rule was generalized from unconditionally hiding `.tkr-name` to hiding whichever span is secondary in the active mode (`.col-ticker:not(.name-first) .tkr-name` vs. `.col-ticker.name-first .tkr`).
- **Header label**: new `updateTickerColumnLabel()` in `screener.js`, called on every `activate()`, sets the `data-sort="ticker"` header cell to "Company" when `isNameFirst()` and "Ticker" otherwise — skipped entirely in ETF mode, whose own "Fund" label comes from its separate `HEADS.etf` entry via the existing kind-change `renderHead()` path. A tiny DOM patch rather than growing `HEADS` into a third dimension, exactly as planned.
- **Sorting**: the `ticker` sort key now compares `a.name.localeCompare(b.name)` when `isNameFirst()`, matching what a user visually scanning company names would expect; every other universe is unchanged (still sorts by ticker string).
- **Per-stock popup**: `openStock()` now sets the modal title to the company name and the subtitle to the ticker when `isNameFirst()`, mirroring the table row's lead/secondary swap; unchanged for every other universe.

### Verified

- Headless Chrome, International universe: header reads "Company", first row's `col-ticker` cell is `<span class="tkr-name">Samsung Electronics Co.</span><span class="tkr">005930.KS</span>` with the `name-first` class present, 100/100 rows, no console errors.
- Headless Chrome, Nasdaq 100 (regression): header still reads "Ticker", cell is the original `<span class="tkr">MU</span><span class="tkr-name">Micron Technology</span>` with no `name-first` class, tiers exactly match the v3.31.0 baseline (2 S+ / 10 S / 8 A / 32 B / 24 C / 24 F, MU at top) — the `nameFirst` flag is a confirmed no-op everywhere it's absent.

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

## v3.36.0 — "FANG+" Filter

### Goal

Owner-requested filter for the NYSE FANG+-style stock list. **Blocked on the owner supplying the actual ticker list** ("which i will provide to you later") — no composition should be guessed or hardcoded ahead of that, since FANG+-style lists vary in membership and the real NYSE FANG+ index itself changes constituents periodically.

### Design direction

This was requested as **a filter**, not a new universe — the simplest reading is: within whichever stock universe is currently loaded (most FANG+-style names live in the Nasdaq 100, but the mechanism should work against any loaded universe), add a way to narrow the visible rows to just the names on the curated list. This is far lighter than building an eighth universe/feed:

1. **No new feed or scoring path needed.** The filter operates purely client-side against whichever universe's data is already loaded and already scored — a stock's score, tier, and every column stay exactly as computed for its actual universe; the filter only changes which rows are visible.
2. **This is an orthogonal filter axis, not another tier chip.** The existing `.chip-group` (`data-filter="all"/"sp"/"s"/"a"/"b"/"c"/"f"`) is single-select and mutually exclusive by design (a stock has exactly one tier). A curated-list filter needs to **AND** with the tier filter and the search box, not replace them (a user should be able to see "FANG+ stocks that are also tier S", for example) — implement as a separate toggle button/chip near the tier group, not inserted into it.
3. **Store the list in a small JSON file** (e.g. `data/fangplus.json`, a flat ticker array) once the owner provides it, structured to be reusable if other curated watchlists get requested later (a `{"name": "FANG+", "tickers": [...]}` shape rather than a single hardcoded array costs nothing extra and avoids a rewrite for the next one).
4. **Membership check**: filter predicate becomes `tickers.includes(r.ticker)` alongside the existing tier/search predicates in `render()`'s `view = rs.filter(...)` step.

### Plan

1. **Wait for the owner's ticker list** — do not start implementation before it arrives, since the filter's only real content is that list.
2. Add `data/fangplus.json` with the provided tickers (flat list, `{"name", "tickers"}` shape per above).
3. Add a toggle control near the tier chip group (e.g. a single button/checkbox, "FANG+ only"), wired into `render()`'s filter predicate alongside `filter` (tier) and `query` (search).
4. Decide behavior when the active universe contains none of the list's tickers (e.g. viewing Growth/Value/Dividend if FANG+ names aren't in that particular top-100 cut) — likely just show zero rows with the existing "no matches" empty state, no special-casing needed.
5. Confirm interaction with universe switching: since this is a client-side filter over whatever's loaded, switching universes while the toggle is on should just re-filter the new universe's rows, no extra plumbing.

### Verification

- With the real list in place: toggle on, confirm only list members show; toggle off, confirm the full universe returns; combine with a tier chip and the search box to confirm all three filters AND correctly.
- Switch universes with the toggle active; confirm the filter re-applies to the newly loaded universe without a stale row set.

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

## v4.1.0 — Screener Score History Sparklines

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
4. Whether Trend ships as a **major** version: yes as planned (v4.1.0), it introduces the first derived-data artifact and a new default column across every universe.

### Verification and acceptance

- Parity gate passes (Python scorer == headless JS scores, all universes, exact).
- History workflow green end-to-end in Actions; `history.json` size within budget.
- Headless check: sparkline SVG present per row, popup chart renders, history-fetch-failure path degrades gracefully (test by pointing the copy at a 404 path).
- Stock scoring regression baseline still holds (no scoring code changes in JS; the frontend change is render-only).

### Risks

- Scoring-port drift over time: any future scoring change must be made in **both** screener.js and the Python scorer. Mitigation: the parity test runs in the history workflow itself, so a drift fails CI loudly instead of silently mining wrong history.
- Early-history noise: feeds before v3.28 covered fewer universes and different fields. The 90-day window and hard-zero rule handle this without special cases.

---

## v4.2.0 — Deeper Index Fund Coverage

### Goal

Expand `indices.html` beyond the current core-index methodology with three new teaching sections: sector ETFs, international allocation, and the bond tent strategy. Content release: no screener, pipeline, or scoring changes.

### Plan

1. **Sector ETFs** — what sector funds are (XLK/XLV/XLE-class examples used descriptively, not as picks), how they concentrate risk relative to broad indices, how the methodology's timing signals (RSI, 52-week range, price vs 200DMA — now live in the ETFs screener universe) apply to them, and why they sit outside the core allocation.
2. **International allocation** — the case for and against ex-US exposure, VXUS as the broad instrument (cross-link to the v3.34.0 International screener universe once live), currency risk in plain English, and how the reader's home-country bias shows up in practice.
3. **Bond tent strategy** — what it is (rising bond allocation approaching a goal date, descending after), why it exists (sequence-of-returns risk, defined at first use per content rules), and how it interacts with the income-contribution investing model the site teaches.
4. Sequencing note: ship **after** v3.34.0 so the international section can link to the live International universe; the sector-ETF section already has the ETFs universe to point at.

### Mechanics (applies to all four content releases, v4.2.0-v4.5.0)

- Written for the primary persona (first-position investor): teach before asserting, define terms at first use, anchor to decisions the reader has faced.
- Content rules: no em dashes, no advice language (educational framing only, no buy/sell verbs aimed at the reader), examples are descriptive not prescriptive.
- Each new section gets: sidebar nav entry (IntersectionObserver hookup is automatic from the section markup pattern), FAQ page additions where a natural Q&A falls out, `sitemap.xml` lastmod bump, meta description review on the touched page.
- Docs per release: PATCHNOTES entry, PRD milestone flip, README page-count touch-ups if section counts are cited.
- Verification: headless render of the touched page, accordion/sidebar behavior intact, no console errors.

---

## v4.3.0 — Additional Illustrative Examples (Historical Market Events)

### Goal

Add worked historical examples across existing pages, showing the methodology applied to real, dated market episodes.

### Plan

1. Candidate episodes (owner to pick 3-5 at kickoff): the 2020 COVID crash and recovery (timing signals at the extreme), the 2021-2022 growth drawdown (what PEG/valuation flagged before it), the 2022-2023 rate cycle (cash-vs-debt pillar behavior), dot-com era NVDA/CSCO contrast (surviving a winner's drawdown), and a dividend-cut case study (what the balance sheet showed first).
2. Placement: each example embeds in the page whose concept it illustrates (metrics examples on `metrics.html`, timing examples on `indices.html`, temperament examples on `philosophy.html`) rather than a standalone examples page, so concepts and cases stay adjacent.
3. Format per example: dated setup (what was knowable then, hindsight explicitly flagged), the metric readings at the time, what the methodology's rules said, what happened, and the teaching point. Historical figures verified against at least one primary-ish source before publishing; approximate figures rounded and labeled approximate.
4. Constraint: examples must not read as track-record claims (no "this is what I bought"); they are illustrations of the rules, per the no-advice rule.
5. Mechanics per the shared checklist in v4.2.0.

---

## v4.4.0 — Additional Philosophy Sections

### Goal

Extend `philosophy.html` (currently 9 sections) with new conceptual material.

### Plan

1. Candidate sections (owner to pick at kickoff; these came out of prior roadmap discussion and PRD content-goals): when to sell (the hardest omission in most methodologies), position sizing and concentration for the income-contribution investor, drawdown temperament (what a 30% paper loss actually feels like and pre-committing behavior), the difference between conviction and stubbornness, and information diet (what to read daily vs quarterly vs never).
2. Each section follows the existing philosophy-page pattern: concept, first-person grounding, the practical rule that falls out of it, cross-links to the metric/page that operationalizes it.
3. FAQ additions for each new section (the FAQ page mirrors philosophy questions today).
4. Mechanics per the shared checklist in v4.2.0.

---

## v4.5.0 — Conference Call Research Guide

### Goal

A new setup-guide page (peer to `finviz.html` and `seekingalpha.html`) teaching how to research earnings conference calls: how to listen, what to note, how to log insights.

### Plan

1. **New page `conferencecalls.html`** following the existing guide-page pattern (step sections, sidebar nav, callout boxes): where calls live (IR pages, transcript sources incl. Seeking Alpha, cross-linking the existing guide), the anatomy of a call (prepared remarks vs Q&A and why Q&A matters more), what to listen for mapped to the site's six scored metrics (guidance vs the forward estimates the screener scores, margin commentary, balance-sheet language), red-flag phrasing patterns, and a simple insight log template (date, company, claim, metric affected, follow-up date).
2. Navigation: header/footer nav additions across all pages (the one release in this set that touches every HTML file), sitemap entry, og/meta for the new page.
3. Ties into the site loop: the guide should close the loop from screener score → "why is the forward estimate what it is" → hearing management's own version on the call.
4. Mechanics per the shared checklist in v4.2.0, plus: full-site headless spot check since nav on every page changes.

---

## v4.0.0 — Screener Responsive Redesign & Site-Wide Mobile-Friendliness Pass — REPRIORITIZED TO THE FRONT (2026-07-04)

### Why this moved to the front of the queue

Originally the last item in the roadmap (a backlog hardening pass). Reprioritized the same day two real users hit the screener's horizontal-scroll problem (v3.34.8, v3.34.10): the owner clarified the actual requirement is **the screener should reflow so scrolling is never needed at all**, not just that the existing scroll mechanism become easier to find. That is fundamentally the same design question this pass was already scoped to answer ("should the table pin columns and reflow, or just scroll, at narrow widths?") — solving it once now, across the full width range (desktop-narrow through phone), avoids redoing the same design work twice and avoids shipping two different narrow-width behaviors a few weeks apart. v3.34.10's scrollbar-visibility fix is superseded and folded in here (see that entry for the diagnosis that led to this decision).

### Goal

A dedicated redesign so the screener remains fully usable — no horizontal scrolling required — across the entire range from full desktop down to phone width, plus the original mobile-hardening scope for the other 8 content pages (which, per audit below, don't have this problem — they're normal flowing content with no fixed-width elements).

### Owner decision (2026-07-04)

**Auto-hide column groups at narrower widths**, extending the existing Columns menu rather than building a new component: below defined width breakpoints, lower-priority column groups progressively hide automatically (Ticker/Tier/Score/Factors and Snapshot always visible; Growth/Performance, then Valuation/Income, then Balance Sheet/Technicals drop off as the window narrows), with the existing Columns menu still available to manually override which groups show at any width. Rejected alternatives: a card-per-stock layout (real UI rebuild, loses at-a-glance column scanning) and pure fluid/shrink-to-fit sizing (hard legibility floor with 15-20 financial columns; wouldn't actually eliminate scrolling on its own).

### Scope confirmed narrow (2026-07-04, read-only audit)

Checked all 9 pages for fixed-width elements that could force horizontal overflow: **only `screener.html` has one** (the data table). The other 8 pages (`philosophy.html`, `metrics.html`, `indices.html`, `finviz.html`, `seekingalpha.html`, `faq.html`, `index.html`, plus the shared sidebar) are normal flowing prose/content with no wide fixed-width elements, and already reflow correctly — the `max-width: 767px` breakpoint (shrinks headings, collapses the metric grid) has not been checked against real device widths but is not expected to need structural changes, just verification. The `.app-toolbar` row (chips, Columns/Methodology buttons) already wraps correctly via `flex-wrap: wrap` at narrow widths (confirmed in headless Chrome at 1150px — Methodology button wraps to its own second line rather than being clipped) — no fix needed there, just inclusion in the width-sweep verification pass.

### Known starting points (carried over from the original scope, still relevant)

1. **The universe switcher has 7 buttons** (Nasdaq 100, S&P 500, Growth, Value, Dividend, ETFs, International) in a `flex-wrap` row — functional, but never checked for how many rows it wraps to on a 375px phone or whether it pushes other controls down awkwardly. May also need auto-collapse-to-dropdown treatment at some width, consistent with the column-hiding approach.
2. **The methodology modal's tables** share the same `.table-wrap` component flagged in v3.35.0; sequence that fix in alongside this pass (or before it) since both touch table rendering.
3. **Touch target sizing** has not been audited: chip filters, column-visibility checkboxes, and the sort-arrow click targets in table headers were sized for mouse pointers first.

### Plan

1. **Define the column-group breakpoint tiers** for the stock table (Snapshot/Growth/Valuation/Balance Sheet groups) and the ETF table (Snapshot/Performance/Income/Technicals groups) separately, since they have different column counts and priorities. Ticker/Tier/Score/Factors always visible at every width (this is the information needed to answer "is this a good stock/fund," the core of the site's value).
2. **Implement auto-hide via the existing Columns-menu infrastructure**: the checkboxes that already drive `applyColumnVisibility()` get their checked state driven by a width-based default in addition to manual user toggling, so a user's manual choice is still respected but the automatic default adapts to window width.
3. **Universe-switcher and toolbar row**: decide whether the 7-button row needs its own narrow-width treatment (e.g. collapsing to a dropdown) or whether `flex-wrap` (already confirmed working) is sufficient — likely sufficient given confirmed correct wrapping behavior, revisit only if the width audit below finds it awkward.
4. **Device/window-width audit**: headless Chrome sweep from ~375px (phone) up through ~1024-1280px (narrow desktop, matching both real reports) to ~1920px (full desktop) across the screener (both stock and ETF/International column sets) and spot-check the other 8 pages, cataloging concrete issues.
5. **Fix and re-verify**: apply fixes, re-run the same width sweep to confirm no desktop regression (every page already works at full width; this must not be a rewrite of what's already correct).

### Verification

- Headless Chrome screenshots/DOM checks across the full width range (375px through ~1920px) for the screener in both stock-kind and ETF-kind modes, confirming Ticker/Tier/Score/Factors are always visible and no column group is ever clipped without also being hidden (i.e., never scroll-required, per the owner's requirement) — a real, provable check unlike the scrollbar-visibility dead end in v3.34.10.
- Spot-check the other 8 pages at 375px/414px/768px, before/after, kept as a record in the PATCHNOTES entry.
- Full click-through of the screener (universe switch, sort, filter, popup, methodology modal, Columns-menu manual override) at several widths after the pass, confirming manual overrides still work on top of the automatic width-based defaults.

---

## Unversioned backlog (no plans yet by design)

- Growth/Value/Dividend standalone framework pages — remains backlog until the owner promotes it to a version.
- Explicitly not planned (owner decisions 2026-07-03): email/RSS changelog subscription, historical scoring backtests, options/crypto/forex coverage.
