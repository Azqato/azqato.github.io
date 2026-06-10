# PATCHNOTES.md — TQQQ Strategies Site

Format: each entry lists the version, date, milestone tag, and a flat list of what changed.
Versions follow `M<milestone>.<patch>` until the site goes live, then switch to semver.

---

## [M3.1] — 2026-06-10 — Docs sync and GitHub Pages launch

Documentation updated to reflect M3 completion and the live site URL. Repository published to GitHub.

### Changed
- `README.md` — status updated to "Live (M3 complete)"; live site URL and repository URL added; stale placeholder-content notice removed from Pages table; Deploying section updated with live URL
- `docs/prd.md` — version bumped to 1.4; M3 milestone marked Complete with live URL; success criteria updated with live URL; version history updated

### Notes
- Repository: https://github.com/Azqato/leveraged-strategies
- Live site: https://azqato.github.io/leveraged-strategies/ (GitHub Pages, deploy from `main` root)

---

## [M3.0] — 2026-06-10 — M3 Content Port (Major Release)

All seven HTML pages rewritten with full strategy content ported from the six `/strategies/*.md` source files. Every placeholder block replaced. Four hero badge and lead paragraph corrections applied. This is the first release where the site is substantively usable as a strategy reference.

### Added
- `index.html` — rewrote all six strategy cards with accurate summaries: correct tickers, correct rebalancing cadences, correct instrument counts, accurate one-line descriptions for each strategy
- `3sig.html` — full rewrite: five sections (Overview, Rules and Logic, Performance Notes, Risks and Caveats, Resources) ported from `strategies/3sig.md`; allocation table (80/20 IJR/SPY), signal line formula, quarterly buy/sell table, full 30 Down Rule (4 ignores, no reset for 3 Sig), BestFolio backtest (CAGR 9.0%, max DD −52.3%, Sharpe 0.31), closed vs. open system distinction, all risk paragraphs
- `6sig.html` — full rewrite: five sections ported from `strategies/6sig.md`; allocation table (60/40 MVV/bonds), 6% quarterly signal, 30 Down Rule (2 ignores, resets to 60/40), BestFolio backtest (CAGR 11.7%, max DD −78.3%, Sharpe 0.23), plan family comparison table, all risk paragraphs
- `9sig.html` — full rewrite: five sections ported from `strategies/9sig.md`; allocation table (60/40 TQQQ/bonds), 9% quarterly signal with both safeguards (90% buying power throttle + Spike Reset trigger with three-condition test), full 30 Down Rule (2 ignores, resets to 60/40), Kelly Letter official portfolio tracking ($733k Jan 2018 → $5.9m Dec 2024), BestFolio backtest (CAGR 39.4%, max DD −72.1%, Sharpe 0.82), dot-com simulation, closed-system bootstrap stress test results
- `tqqq-ftlt.html` — full rewrite: five sections ported from `strategies/tqqq-ftlt.md`; instruments table (TQQQ, UVXY, TECL, UPRO, SQQQ, TLT), signal inputs table (SPY 200D SMA, TQQQ 20D SMA, four RSI signals), full bull/bear decision trees with SQQQ vs. TLT top-RSI selection, 10-year backtest (TQQQ FTLT +298% vs. TQQQ buy-and-hold +35%), Gayed & Bilello LRS academic table (87-year backtest), all risk paragraphs
- `hfea.html` — full rewrite: five sections ported from `strategies/hfea.md`; original 40/60 and revised 55/45 allocations, risk parity volatility basis, cost-of-leverage table (UPRO and TMF ER + borrow rates), community variants table, "HFEA The Resurrection" regime-adaptive variant (four-regime table driven by SPY 200D SMA + TLT 400D SMA, Composer ID `Cjb5ysKtJsPv6Tm3Fk0R`), backtest simulation formula, lost-decade validation, live tracking table (May 2019 to April 2025), all risk paragraphs
- `holy-grail.html` — full rewrite: five sections ported from `strategies/holy-grail.md`; instruments table (TQQQ, UVXY, TECL, SOXL, SQQQ, BSV), signal inputs table, full bull (80%)/bear decision trees with SOXL oversold layer and SQQQ vs. BSV selection, comparison table vs. TQQQ FTLT, Gayed & Bilello LRS data, all risk paragraphs; Composer ID `VPVpD1SoqR5ykVu4NdWS`

### Fixed
- `3sig.html` hero badge: "Monthly Rebalancing" → "Quarterly Rebalancing"
- `6sig.html` hero badge: "Monthly Rebalancing" → "Quarterly Rebalancing"
- `tqqq-ftlt.html` hero badge: "Buy and Hold" → "Daily Algorithm"; lead paragraph rewritten to describe daily rules-based algorithm, SPY 200D SMA, 10D RSI, and 6 instruments (was incorrectly implying passive holding)
- `holy-grail.html` hero badge: "Rules-Based Allocation" → "Event-Driven Algorithm"; lead paragraph corrected to remove TMF (TMF is not used in this strategy); instruments listed as TQQQ, UVXY, TECL, SOXL, SQQQ, BSV
- All seven pages: all `<div class="placeholder">` blocks removed and replaced with real content

### Notes
- `<!-- RESEARCH SOURCES -->` blocks in `.md` files were not ported to HTML per convention
- The 9 Sig safeguards (90% throttle and Spike Reset) are not publicly documented by Jason Kelly outside The Kelly Letter; content sourced from subscriber materials referenced in community posts
- HFEA The Resurrection Composer ID (`Cjb5ysKtJsPv6Tm3Fk0R`) and Holy Grail Composer ID (`VPVpD1SoqR5ykVu4NdWS`) are included in the HTML pages as `<code>` text, not hyperlinks
- TMF is not an instrument in the Holy Grail strategy; the prior placeholder was misleading

---

## [M1.0] — 2026-06-10 — Skeleton Build

Initial project scaffold. All four pages, shared stylesheet, shared JS, and placeholder strategy sections built from scratch.

### Added
- `index.html` — home page: site intro, leveraged ETF risk callout, three strategy cards (9 Sig blue, TQQQ FTLT green, Holy Grail purple), footer disclaimer
- `9sig.html` — 9 Sig strategy page with hero badge, five placeholder sections, mandatory risk callout in Risks section
- `tqqq-ftlt.html` — TQQQ FTLT strategy page with hero badge, five placeholder sections, mandatory risk callout in Risks section
- `holy-grail.html` — Holy Grail strategy page with hero badge, five placeholder sections, mandatory risk callout in Risks section
- `css/style.css` — full shared stylesheet: all 17 color tokens, reset, layout grid, sidebar, top-bar nav, typography, hero, strategy cards, placeholder blocks, tables, callout boxes, badges, ticker tags, footer, media queries (1024px, 768px), reduced-motion
- `js/main.js` — IntersectionObserver anchor highlighting for strategy pages, mobile nav toggle
- `strategies/9sig.md` — content source skeleton with five section headings and authoring notes
- `strategies/tqqq-ftlt.md` — content source skeleton with five section headings and authoring notes
- `strategies/holy-grail.md` — content source skeleton with five section headings and authoring notes

### Notes
- All strategy pages ship with dashed-border placeholder blocks per design spec
- Each strategy page's Risks section includes the mandatory leveraged ETF risk callout in addition to the placeholder
- Content authoring belongs to M2; port to HTML belongs to M3

---

## [M1.8] — 2026-06-10 — HFEA rename and Composer variant

Corrected the strategy acronym from HEFA (typo) to HFEA throughout the project. Added the "HFEA The Resurrection" Composer symphony as an implementation example in the content file.

### Added
- `strategies/hfea.md` (renamed from `strategies/hefa.md`) — added "Regime-adaptive variant" subsection under Rules and Logic documenting the "HFEA The Resurrection" symphony by u/derecknielsen: four-regime allocation table driven by SPY 200D SMA + TLT 400D SMA, with TMV replacing TMF when TLT is below its 400-day average

### Changed
- `strategies/hefa.md` → renamed to `strategies/hfea.md`
- `hefa.html` → renamed to `hfea.html`
- All 7 HTML pages — nav link updated from `hefa.html` to `hfea.html` in both sidebar and top-bar nav
- `index.html` — strategy card class updated from `.strat-hefa` to `.strat-hfea`; card link and HFEA card anchor updated
- `hfea.html` — placeholder source paths updated from `/strategies/hefa.md` to `/strategies/hfea.md`; inline badge token updated from `--color-strat-hefa` to `--color-strat-hfea`
- `css/style.css` — CSS custom property renamed from `--color-strat-hefa` to `--color-strat-hfea`; selector renamed from `.strat-hefa::before` to `.strat-hfea::before`
- `README.md` — `hefa.html` and `hefa.md` references updated to `hfea.html` and `hfea.md`
- `docs/prd.md` — `hefa.html` reference in pages table updated to `hfea.html`
- `docs/design.md` — strategy tint table token updated from `--color-strat-hefa` to `--color-strat-hfea`

### Notes
- Historical M1.2 and M1.3 patchnotes entries retain the original `hefa` filenames as an accurate record of what was created at that time
- The Composer symphony URL added to the `<!-- RESEARCH SOURCES -->` block in a prior patch is now accompanied by the actual content section

---

## [M1.7] — 2026-06-10 — Documentation sync

Brought all four project documents up to date to reflect the completed M1 and M2 milestones.

### Changed
- `README.md` — pages table updated from 3 to 7 pages; TQQQ FTLT description corrected (not "buy-and-hold", is a rules-based daily algorithm); project structure updated to list all 6 strategy .md files with their status; status updated from "Initial build (placeholder content)" to "Content drafted (M2 complete, M3 pending)"
- `docs/prd.md` — version bumped to 1.3; Goals updated from "three strategies" to "six strategies"; F1 updated from "four HTML pages" to "seven HTML pages"; F6 updated from "three strategy pages" to "six strategy pages"; success criteria counts updated; milestones table updated with Status column and M1/M2 marked Complete, M3/M4 marked Pending with M3 port notes referencing TQQQ FTLT and Holy Grail HTML corrections
- `docs/design.md` — version bumped to 1.2; HFEA orange tint token (`#f0883e`) added to strategy tint table; version history updated
- `docs/patchnotes.md` — this entry

---

## [M1.6] — 2026-06-10 — Holy Grail full content

Wrote full content for `strategies/holy-grail.md` from the Composer symphony JSON and the TQQQ FTLT structural lineage.

### Added / Changed
- `strategies/holy-grail.md` — full content written across five sections
  - **Metadata corrected:** Tickers are TQQQ, UVXY, TECL, SOXL, SQQQ, BSV — not TQQQ + TMF as suggested by the placeholder. Rebalancing is event-driven with 5% corridor, not "periodic."
  - **⚠ Corrections for HTML port** added: (1) TMF is not used — remove it from the lead paragraph; (2) lead paragraph needs to describe RSI and SMA regime switching, not risk parity
  - Overview: TQQQ FTLT variant with five structural differences; based on Gayed/Bilello (2015) SMA-gated leverage; Composer `(Invest Copy)` indicates original creator unknown
  - Rules and Logic: full decision tree from JSON; TQQQ 200D SMA as primary regime (not SPY); 80% bull / 20% cash; bear regime adds SOXL mean reversion; BSV instead of TLT for defensive; event-driven + 5% corridor rebalancing
  - Performance Notes: no live data accessible (Composer requires auth); structural analysis of 20% cash drag; comparison table vs. TQQQ FTLT; Gayed/Bilello LRS academic data as reference
  - Risks: TQQQ's own 200D SMA causes faster/noisier regime switches vs. SPY; 20% cash drag in bull runs; SOXL counter-trend risk; UVXY extreme volatility; no verified public live performance record
  - `<!-- RESEARCH SOURCES -->` block with 5 sources

### Notes
- Composer factsheet URL (with ?tab=backtest) required authentication; performance metrics not retrieved
- The Holy Grail is structurally a variant of TQQQ FTLT with TQQQ 200D SMA, SOXL signal, and BSV substitution
- The "(Invest Copy)" suffix on the symphony name means this is someone's copy of a shared original; original creator not identified in available sources

---

## [M1.5] — 2026-06-10 — TQQQ FTLT full content

Wrote full content for `strategies/tqqq-ftlt.md` from the original strategy post (u/derecknielsen, Reddit, Oct 2022), the Composer symphony JSON, and the underlying academic paper (Gayed & Bilello, 2015).

### Added / Changed
- `strategies/tqqq-ftlt.md` — full content written across five sections
  - **Metadata corrected:** Strategy is NOT buy-and-hold. It is a daily-rebalancing rules-based algorithm with 6 instruments. Rebalancing cadence updated from "None (buy and hold)" to "Daily (rules-based algorithmic)."
  - **⚠ Note for HTML port** added: tqqq-ftlt.html hero badge ("Buy and Hold") and lead paragraph are inaccurate and need updating when content is ported
  - Overview: u/derecknielsen origin (Oct 2022), TQQQ discovered Oct 2021 before 70%+ drawdown, goal to profit in both bull and bear; based on Gayed/Bilello "Leverage for the Long Run" (2015, SSRN #2741701); 10+ community variants, 900+ Composer Discord comments
  - Rules and Logic: full decision tree from Composer JSON + original post; 6 instruments (TQQQ, UVXY, TECL, UPRO, SQQQ, TLT); 6 signal inputs (SPY 200D SMA, TQQQ 20D SMA, 10D RSI on 4 instruments); bull/bear regime tables; SQQQ vs TLT top-RSI selection logic
  - Performance Notes: 10-year backtest Oct 2012–Oct 2022 (+298% vs +35% TQQQ buy-and-hold, 8.5× faster, ~half drawdown); Gayed/Bilello LRS data (87-year backtest; 2x LRS Sharpe 0.51 vs buy-and-hold 0.30; above 200D SMA: +14.1% CAGR); live +150% from Jun–Oct 2022
  - Risks: daily whipsaw near 200D SMA, UVXY extreme volatility, all instruments use daily reset leverage, favorable backtest window, SQQQ is directional not a hedge
  - `<!-- RESEARCH SOURCES -->` block with 6 sources (SSRN was 403, noted)

### Notes
- SSRN paper (abstract_id=2741701) returned HTTP 403; academic content obtained from CXO Advisory and The7Circles secondary analyses
- Composer factsheet URL provided but app.composer.trade requires authentication; Composer JSON was pasted directly by user in source data
- The "TQQQ For The Long Term" name is intentionally ironic given the strategy actively rotates into bearish and volatility instruments

---

## [M1.4] — 2026-06-10 — 3 Sig, 6 Sig, 9 Sig full content

Wrote full content for all three Signal plan strategy files using primary sources from Jason Kelly's site, the Kelly Letter subscriber video transcript, independent backtesting, and community Reddit threads.

### Added / Changed
- `strategies/3sig.md` — full content written across five sections
  - Corrected metadata: rebalancing is quarterly (not monthly as in the placeholder), fund is IJR/SPY (not TQQQ)
  - Overview: Jason Kelly, *The 3% Signal* (2015), value averaging concept, three-plan family structure (target = 3% × leverage multiplier)
  - Rules and Logic: 80/20 starting allocation, signal line formula, quarterly buy/sell table, full 30 Down Rule (4 sell signals ignored, no reset for 3 Sig)
  - Performance Notes: BestFolio corrected backtest (CAGR 9.0%, max DD −52.3%, Sharpe 0.31), Bogleheads community backtest, open vs. closed system distinction
  - Risks: bond buffer depletion, bond fund losses in rate hikes, fixed target, buy-and-hold comparison, data snooping, tax drag
  - `<!-- RESEARCH SOURCES -->` block with all 17 sources
- `strategies/6sig.md` — full content written across five sections
  - Corrected metadata: rebalancing is quarterly, fund is MVV (not TQQQ), 60/40 base allocation
  - Rules and Logic: 60/40 starting allocation, 6% quarterly signal, 30 Down Rule (2 sells, resets to 60/40 after)
  - Performance Notes: BestFolio corrected backtest (CAGR 11.7%, max DD −78.3%, Sharpe 0.23), plan family comparison table
  - Risks: 2x leverage amplification, "moderate" label misleading given −78.3% max DD
  - `<!-- RESEARCH SOURCES -->` block with 10 sources
- `strategies/9sig.md` — full content written across five sections
  - Rules and Logic: 60/40 base, 9% quarterly signal, full signal line formula, two additional safeguards (90% throttle, Spike Reset), 30 Down Rule (2 sells, resets to 60/40)
  - Performance Notes: Kelly Letter official account ($733k Jan 2018 → $5.9m Dec 2024); 2023 tracking ($1.5m → $4.1m, 99% TQQQ all year); BestFolio real-data backtest (CAGR 39.4%, max DD −72.1%, Sharpe 0.82); dot-com simulated recovery (18–20 years without contributions); closed-system bootstrap (median −98% DD)
  - Risks: closed-system viability, 2022 bond exhaustion (historical), 3x leverage amplification, volatility decay
  - `<!-- RESEARCH SOURCES -->` block with 10 sources

### Notes
- Reddit was not directly fetchable; user provided both Reddit thread contents directly in chat
- The 30 Down Rule transcript was the primary source for per-plan parameters (ignore counts, reset behavior, fund assignments)
- 6 Sig does not have a standalone book; *The 3% Signal* covers the 3 Sig mechanics which apply across the family
- Bond fund alternatives documented in 9sig.md: SGOV, TBLL, USFR, SPAXX, BOXX, JAAA — community has moved away from AGG for this sleeve

---

## [M1.3] — 2026-06-10 — HFEA content and research sources convention

Wrote full content for `strategies/hefa.md` using primary and community sources. Established the research sources convention for documenting external URLs inside strategy `.md` files without exposing them in HTML.

### Added
- `strategies/hefa.md` — full content written across five sections: Overview, Rules and Logic, Performance Notes, Risks and Caveats, Resources
  - Risk parity theoretical basis (S&P 500 vol ~15%, LTT vol ~10%, giving 40/60 at parity)
  - Both allocation versions: original 40/60 (Thread 1, Feb 2019) and revised 55/45 (Thread 2, Aug 2019)
  - Exact backtest figures: 23.75% CAGR (Hedgefundie's model) vs ~19% (vineviz conservative estimate), 1987-2018
  - "Lost decade" validation: Jan 2000-Sept 2011, HFEA ~11% CAGR vs S&P 500 ~0%
  - Cost-of-leverage table: UPRO 0.92% ER + 2.87% borrow rate; TMF 1.09% ER + 1.83% borrow rate
  - Live tracking table: May 2019 through April 2025, including the ~65% 2022 drawdown from peak
  - PSLDX as pre-existing analogue (launched September 2007)
  - Hedgefundie's personal framing: $100k = 15% of investable assets, goal of $10M in 20-25 years
  - `<!-- RESEARCH SOURCES -->` comment block with all 5 research URLs (never ported to HTML)
- `docs/prd.md` — Research Sources Convention section added under §3; HFEA added to pages table; version updated to 1.2

### Notes
- Primary source (Bogleheads Thread 1, Feb 2019) was paywalled via WebFetch; user provided the full text directly in chat
- Bogleheads Thread 2 (Aug 2019) was also paywalled; content inferred from accessible secondary sources
- The `<!-- RESEARCH SOURCES -->` block convention applies retroactively to future strategies; existing skeleton .md files do not require it until research is actually conducted

---

## [M1.2] — 2026-06-10 — HFEA page

Added Hedgefundie's Excellent Adventure (HFEA) as a seventh strategy.

### Added
- `hefa.html` — HFEA strategy page (placeholder sections, orange tint `#f0883e`, Quarterly Rebalancing hero badge, UPRO/TMF tickers)
- `strategies/hefa.md` — content source skeleton with authoring notes including 2022 correlation breakdown, Reddit origin, and backtest caveats

### Changed
- All 6 existing pages — HFEA nav link inserted before Support in both sidebar and top-bar nav
- `index.html` — HFEA strategy card added after Holy Grail
- `css/style.css` — added `--color-strat-hefa: #f0883e` token and `.strat-hefa::before` card rule

---

## [M1.1] — 2026-06-10 — 3 Sig, 6 Sig, nav convention, footer and support link

Expanded the site from 4 to 6 strategy pages, established the /strategies convention, and aligned the footer and support link with the broader Azqato site family.

### Added
- `3sig.html` — 3 Sig strategy page (placeholder sections, light blue tint `#79c0ff`, Monthly Rebalancing hero badge)
- `6sig.html` — 6 Sig strategy page (placeholder sections, amber tint `#e3b341`, Monthly Rebalancing hero badge)
- `strategies/3sig.md` — content source skeleton
- `strategies/6sig.md` — content source skeleton
- Support link (`https://azqato.github.io/support.html`) added as last nav item across all pages (sidebar and top-bar)
- `/strategies convention` documented in prd.md and design.md: each .md file in /strategies maps to a page, nav entry, and index card

### Changed
- `index.html` — added 3 Sig and 6 Sig strategy cards to the grid; nav updated
- `9sig.html`, `tqqq-ftlt.html`, `holy-grail.html` — nav updated with 3 Sig and 6 Sig links
- All pages — footer updated from full disclaimer to "Built by Azqato." matching the Azqato site family pattern
- `css/style.css` — added `--color-strat-3sig` and `--color-strat-6sig` tokens; added `.strat-3sig::before` and `.strat-6sig::before` card rules
- `docs/design.md` — strategy tint table updated, footer section updated, nav convention documented, version history updated
- `docs/prd.md` — pages table updated, /strategies convention section added, version history updated

### Notes
- The sidebar disclaimer ("Educational use only. Not financial advice.") remains in the sidebar on all pages
- 3 Sig and 6 Sig use light blue and amber tints to stay visually distinct from 9 Sig's medium blue

---

<!--
TEMPLATE — copy this block for future entries:

## [M<n>.<patch>] — YYYY-MM-DD — <short title>

<one sentence describing the scope of this patch>

### Added
-

### Changed
-

### Fixed
-

### Removed
-

### Notes
-

-->
