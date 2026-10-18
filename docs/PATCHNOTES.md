# Patch Notes

All notable changes to the Azqato Portfolio are documented here.
Format: `[version] - YYYY-MM-DD`

---

## [2.30.1] - 2026-10-18

### Changed
- **Market Overview**: the RSI line reads "10D RSI:" and is centered in each card.

## [2.30.0] - 2026-10-18

### Added
- **Market Overview** (`invests/indices/market/`): every card shows a 52-week range bar with a dot at today's
price and the low and high beneath, plus a 10-day RSI line, red at 79 or above (overbought) and green at 31 or
below (oversold). Treasury yields show the range but no RSI.
- Bonds gains the Fed Funds Rate, CPI and Core CPI (year over year), from FRED, each with an "As of" date: the day
for Fed Funds, the month for the monthly CPI pair.

### Changed
- The categories now lead with Indices, Broad Market, Bond Funds and Market Cap, reorganized in the Stocks data feed
(v5.10.0). The page reads the new fields from the same feed. The intro and search description were updated.
- `check.py` allows the Market Overview inline script's stocks-market inventory item to change.

## [2.29.0] - 2026-10-16

### Changed
- **URL Structure** reworked after a field run on a local-only static site of about 1,070 pages, where several
parts assumed a hosted site. It now works out how the site runs first (hosted with redirects, static hosting only,
or local only), and applies the standard by mode: local-only sites get relative links that name the file, no
redirects, canonicals, sitemap or lowercase catch-all, and old files deleted once nothing outside links in.
- Every page except the home page now lives in its own folder, even a single page. A clean-root rule moves
stylesheets, scripts, images and fonts under one assets folder, with unused files proposed for deletion only after
a scripted check and approval.
- The audit now flags hand-written menus so all navigation is generated from one source, lists exceptions to the
standard as narrow, approved patterns (such as case-sensitive video IDs), and the checks include a from-disk link
check and a navigation-matches-source check. The report adds the hosting mode, exceptions and the root cleanup.

## [2.28.0] - 2026-10-16

### Added
- **A new prompt, URL Structure** (`codes/prompts/url-structure/`): audit a site's URLs against one standard
(lowercase hyphenated paths, plural collections, one folder per area with an overview page, one canonical address
per page), then, after approval, move pages one area at a time with tested redirects, and navigation, sitemap and
canonical tags to match. Built from the author's draft with these changes: one trailing-slash form chosen by what
the host serves natively, instead of always none; redirect pages where the host cannot send a 301; an offer to add
a redirect-check script when the site has no tests, instead of stopping; routes, links and the crawl counted with a
script; unknown external links marked unknown; one hop for every redirect, including existing ones; and approval
before editing the project's instructions file. It sits after SEO Audit, so the list now holds 26 prompts.

## [2.27.1] - 2026-10-14

### Changed
- **App Performance** now ends by adding every optimization it found but did not ship to the project's roadmap
(the screen or flow, its measured cost, the likely fix and a rough size), updating existing entries instead of
duplicating them, and asking where to put them if the project has no roadmap. It replaces the closing line that
said not to commit.

## [2.27.0] - 2026-10-14

### Added
- **A new prompt, App Performance** (`codes/prompts/app-performance/`): measure where an app is really slow at
startup, opening screens, loading content and scrolling, fix the biggest gaps one at a time, and keep a fix only if
repeated before and after runs prove it. Built from the author's brief and rewritten to the section's writing rules:
it reads the project first, times everything with a script (median and spread of 3 or more runs), asks rather than
guesses when something cannot be measured, forbids passing by removing features, and ends with a per-fix table and
the checks run. It sits after Animation Performance in the list, so the list now holds 25 prompts.

## [2.26.0] - 2026-10-12

### Added
- **A `Data` column** in the screener, next to Factors, showing `n/6`: how many of the six scored metrics the
company actually publishes. Sortable, and flagged amber when anything is unreported. The score breakdown popup
spells it out when anything is missing.
- A missing metric scores zero against a denominator fixed at 100, so without this a low score cannot be read: a
company that reports everything and ranks badly looks identical to one nobody covers. Across the bottom of the
market, the share of names missing at least one metric runs 24% in C, 38% in D and 59% in F.
- `computeScoreMap` already counted this and discarded the number, so nothing new is computed and no score, rank
or tier changes. The `Azqato Screen` group header widens from 3 columns to 4 in both layouts.

### Changed
- All of it is registered in `site.py`'s `CONTENT_EDITS` and `SCRIPT_EDITS` alongside the clamp and tier work, so
a rebuild from the `_sources` snapshot cannot drop it.

## [2.25.0] - 2026-10-12

### Fixed
- **The clamp and tier work was one build away from being silently reverted.** `invests/` is rebuilt from the
read-only snapshot in `scripts/invests/_sources/`, and that snapshot still carries the single symmetric
`CLAMP_Q` of 0.22 and the original v3.29.0 five-label tier bands. Running `site.py` would have undone the whole
of 2026-10-12: the clamp split, both rounds of re-cut bands, and the D tier. All of it is now registered in
`CONTENT_EDITS['stocks/screener.html']` (11 pairs) and `SCRIPT_EDITS['screener.js']` (11 pairs), which is the
tracked home this script already provides for exactly this hazard. Each pair asserts its target is present, so a
future snapshot that rewords any of it fails the build loudly instead of dropping the correction.
- Verified by running the real `apply_edits` over the snapshot: no stale band or clamp string survives, and the
live `screener.js` is now byte-identical to what the build would produce from the snapshot, so the build is a
no-op on these regions rather than a revert.
- **A stale comment in `screener.js` contradicted the code under it.** The block above `TIER_CUTS` still read
`S = top 10%, A = next 10%, B = 20-50%, C = 50-75%, F = bottom 25%` while the block immediately below it defined
the six-band scheme.
- **A wrong figure in the same comment.** It claimed the five-label scheme it replaced scored 2.48 bits; the
measurement is 2.28. The PRD and the patch notes had it right.

## [2.24.1] - 2026-10-12

### Fixed
- **The site search index carried stale tier prose.** `invests/assets/js/search-index.js` is generated by the
build, and its copy of the screener's tier text still described the *original* v3.29.0 bands (A = next 10%,
B = 20-50%, C = 50-75%, F = bottom 25%, 100-stock counts of 10/10/30/25/25). It had therefore been wrong through
every band change of 2026-10-12, so searching the site returned a different definition from the page itself.
Refreshed in place to the live six-band scheme.
- The ETF tier heading read "Tiers on a 10-fund list" and the paragraph under it counted tiers out of 10. The
fund universe is 36. The heading is now "Tiers on a short fund list" and the counts match; the `id` is left
alone so existing anchor links still resolve.

## [2.24.0] - 2026-10-12

### Changed
- **A D tier is added, and the bands become S 10%, A 10%, B 20%, C 20%, D 20%, F 20%.** `TIER_CUTS` in
`invests/assets/js/stocks/screener.js` becomes `[s 0.10, a 0.20, b 0.40, c 0.60, d 0.80]`, with `TIER_LABEL` and
`TIER_COLOR` gaining a `d` entry.
- **The tier color ramp shifts to stay monotonic.** C moves from light red to orange (`--color-tier-c` is now
`--ti-color-orange`, `#f0883e` in `src-stocks.css`) and D inherits the light red C used to own (new
`--color-tier-d`, `#ffa198`), with a matching `.v-d` badge rule on the screener page.
- **Two stale tier tooltips are fixed.** The stock and ETF table header rows emit their own `title` text from
JavaScript, and both still described the original scheme (A = next 10%, B = 20-50%, C = 50-75%, F = bottom 25%).
Every earlier copy edit touched the static HTML and missed them, so the page showed two different band definitions
depending on where you hovered.
- The tier legend, the Tier column tooltip, the band explanation and the ETF universe copy match the new bands and
per-100 counts (about 10 S, 10 A, 20 B, 20 C, 20 D and 20 F), plus a new paragraph on what the C and D line means.

### Notes
- Domestic lands at 0.7% S+, 9.4% S, 10.6% A, 20.8% B, 18.6% C, 20.6% D and 19.4% F. No band exceeds 20.8%.
- Measured against the sizing rule, these cuts reach 91.3% of the information ceiling for six labels against
88.3% for the five-label scheme they replace.
- The C and D line is where valuation support disappears: median PEG points fall from 11.4 of 25 in C to 0.6 in D.
- No score and no ranking changes: tier cuts apply to the finished ranking and cannot feed back into it.

## [2.23.0] - 2026-10-12

### Changed
- **Tier bands settle at S 10%, A 15%, B 25%, C 25%, F 25%** (owner's distribution). `TIER_CUTS` in
`invests/assets/js/stocks/screener.js` becomes `[s 0.10, a 0.25, b 0.50, c 0.75]`.
- **This reverts 2.22.0 the same day.** That release shrank F from a quarter of the market to a tenth, on the
argument that a band holding a quarter of everything says little about anything in it. The argument was right and
the fix was wrong: it put half the market in B, failing the same test twice as badly.
- **The sizing rule is now written down** in the source and on the page: no band may grow so large that the label
stops narrowing anything down. Measured as the information content of a tier label on the Domestic universe, these
cuts give 2.28 bits against 2.23 for the original and 2.00 for 2.22.0's arrangement, with a 2.58-bit ceiling.
- The tier legend, the Tier column tooltip, the band explanation and the ETF universe copy match the new bands and
per-100 counts (about 10 S, 15 A, 25 B, 25 C and 25 F).

### Notes
- Domestic lands at 9.4% S, 15.8% A, 24.4% B, 25.1% C and 24.6% F. No band exceeds 25%.
- No score and no ranking changes: tier cuts apply to the finished ranking and cannot feed back into it.
- A D band was evaluated and rejected. It would not separate the two populations in F (genuinely shrinking
companies, and companies nobody publishes estimates for), because a D of the bottom 10-25% would itself be half
missing-data cases. That ambiguity is a data problem rather than a tier problem.
- S+ is unchanged: still any stock scoring a perfect 100, not a rank cut.

## [2.22.0] - 2026-10-12

### Changed
- **New tier bands on the stock screener** (owner's distribution). `TIER_CUTS` in
`invests/assets/js/stocks/screener.js` becomes `[s 0.10, a 0.20, b 0.70, c 0.90]`: S is still the top 10% and A the
next 10%, but B goes from 30% to 50%, C from 25% to 20%, and F from 25% to 10%. The old split made F a quarter of
the market, and a tier that holds a quarter of everything says very little about anything in it. B is now the
middle of the pack and F is reserved for the worst tenth.
- The tier legend, the Tier column tooltip, the band explanation and the ETF universe's copy are updated to match,
including the per-100 counts (about 10 S, 10 A, 50 B, 20 C and 10 F).

### Notes
- Measured on the live feeds: the Domestic universe lands at 9.4% S, 10.6% A, 49.9% B, 19.9% C and 9.6% F against
targets of 10/10/50/20/10, the drift being boundary ties rounding up.
- Nothing is demoted. Exactly two transitions happen: names move C to B and F to C, 35.3% of Domestic labels in all.
No score and no ranking changes, because tier cuts are applied to the finished ranking and cannot feed back into it.
- **S+ is unchanged**: still any stock scoring a perfect 100, not a rank cut. It stays the only tier whose size
depends on the scoring curve rather than on rank.

## [2.21.0] - 2026-10-12

Supersedes 2.20.0 the same day. That release refitted the screener's single clamp constant to 0.13; the owner
judged it too strict at the top, and revisiting it showed the symmetric form was the problem, not the value.

### Added
- **The clamp's two ends are now set independently.** `CLAMP_LO` and `CLAMP_HI` replace `CLAMP_Q` in
`invests/assets/js/stocks/screener.js`: a metric scores zero at or below the `CLAMP_LO`th percentile and full
marks at or above the (1 - `CLAMP_HI`)th. Live values are 0.13 and 0.22, so zero in the bottom 13% and full marks
in the top 22%. A single constant set both ends before, which forced a forgiving floor and a reachable ceiling to
trade off against each other.

### Changed
- **The screener page's "How a rank becomes points" section** is rewritten for the new curve: 0 points at the
13th percentile, 5 at the 29th, 11.4 at the median, 15 at the 62nd, 20 at the 78th and up. The note now explains
why the floor matters more than the ceiling, which is that a cell pinned at 0 or 20 says nothing about where a
company actually ranks.

### Notes
- Net effect against the pre-2.20.0 behavior: the Domestic median score rises from 45 to 50, the 90th percentile
from 77 to 80, and the share of metric cells flattened to 0 or 20 falls from 45.6% to 32.9%. Perfect scores are
unchanged at roughly five in the Nasdaq 100 and twelve in the S&P 500, so the top of the list reads as it did.
- Dropping the clamp entirely was measured and rejected: pure rank-linear points need no constants but no stock
would reach 100 and the top of the pack converges (Domestic 90th percentile falls to 69). The orderings are nearly
identical either way, Spearman 0.9903, so the clamp's job is separation in the displayed score rather than in the
ranking.
- The two values are counted inward from opposite ends, so a larger `CLAMP_LO` is **harsher** and a larger
`CLAMP_HI` is **more generous**. Worth remembering before anyone touches them again.

## [2.20.0] - 2026-10-12

### Changed
- **The stock screener's percentile clamp is refitted, which moves nearly every score on the site.**
`CLAMP_Q` in `invests/assets/js/stocks/screener.js` goes from 0.22 to 0.13, so a metric now scores zero at or
below the 13th percentile and full marks at the 87th and up, where it used to be the 22nd and the 78th. The median
still scores exactly half. The clamp is documented as calibrated so roughly one Nasdaq 100 and five S&P 500 stocks
reach a perfect 100; as the feeds' data changed it had drifted to 5 and 12. At 0.13 it produces 2 and 5.
- **The screener page's "How a rank becomes points" section** now matches the code: the curve table, the formula,
and the calibration sentence, which says two Nasdaq 100 stocks rather than one. The Nasdaq 100 cannot be brought
to one at any clamp value, because MU and SNDK rank in the top percentile of all six scored metrics and score 100
even at 0.10.

### Notes
- Measured impact: 2,920 of 3,465 Domestic scores moved, 91 of 100 in the Nasdaq 100, 437 of 500 in the S&P 500,
in a band of -10 to +9 points with a mean of -0.2 and 310 Domestic tier changes. Scores are percentile ranks, so
refitting cannot move the average much; it tightens the top, and the names that fall are those that had been taking
full marks from the 78th percentile upward.
- The direction is counterintuitive and worth remembering before anyone touches it again: a **larger** `CLAMP_Q`
is more generous, because full marks begin at the (1 - q)th percentile.
- The matching constant in the stocks feed repo (`scripts/analyze_etf_holdings.py`) was changed in the same pass,
and that repo's v5.4.0 notes carry the full sweep.

## [2.19.1] - 2026-10-12

### Fixed
- **`scripts/prompts/build.py --check` reported every prompt page out of date on a clean tree.** It compared pages
without the Codes shell, but missed two things `shell.py` adds (the `codes.css` link and the byline) and the blank lines
the shell leaves behind. It now ignores all three and passes when nothing has changed.
- **A prompts build could strip the Contents sidebar.** The build wrote pages without it and relied on
`scripts/codes/shell.py` being run by hand afterwards. It now reruns the shell itself whenever it writes a page.
Rebuilding a deleted page gives a byte-identical file.
- The prompts PRD and the site PRD runbook describe the new order and restore `--check` to the checks.

## [2.19.0] - 2026-10-12

### Added
- **Prompts operating notes, `codes/prompts/docs/PRD.md`.** Rewritten from the archived prompts repository's PRD for
the section as it now runs: where the sources and generated pages live, the content and writing rules every prompt
follows, title and description budgets, how Copy and Expand behave, adding, editing, hiding, renaming and removing a
prompt, public and retired addresses, the build and checks, and versioning. Its one idea from the old TODO, a Legal
Audit prompt, is kept in its Ideas section. The old repository's design notes were not carried over.
- **The prompts repository's patch notes, v1.0.0 to v1.112.0**, are merged word for word at the end of this file. Its
separate version line ends there; prompts changes are site versions from this entry on.

### Fixed
- The Add Prompt prompt described the old repository's process (`prompts-data.js`, the README list, its own patch
notes). It now points to the prompts PRD and the site's patch notes, and its description says what it does today.
- The site PRD's runbook and "Adding a prompt" gave the sources as `prompts/md/`; they are `codes/prompts/md/`. It now
links the prompts PRD for the full process. The same path is fixed in the build script's header comment.
- Both runbooks left out `scripts/codes/shell.py`, which has to run after the prompts build or the pages lose the
Contents sidebar. It is now listed. `build.py --check` is dropped from the runbook: since the shell was added it
reports every prompt page out of date even on a clean tree. The prompts PRD records this as a known issue.

## [2.18.1] - 2026-10-11

### Fixed
- **The two trailing growth metrics were named and defined wrongly on every page that mentions them.** They were called
Revenue Growth TTM and EPS Growth TTM, and the metrics page defined TTM as "the most recently completed twelve-month
period" compared with "the same period one year earlier". The stocks feed carries Yahoo's `revenueGrowth` and
`earningsGrowth`, which are the latest reported quarter against the same quarter a year earlier. Measured against
quarterly income statements for AAPL, MSFT, NVDA, KO and WMT, the feed matched latest-quarter year over year to within
0.05 percentage points on all five (AAPL 16.40 against 16.36, NVDA 105.90 against 105.85). A true twelve-month figure
cannot be computed for any company from that source, which publishes only five or six quarters where eight are needed.
- The screener's columns now read **Rev Q YoY** and **EPS Q YoY**, its score popup reads Revenue Growth (Q, YoY) and EPS
Growth (Q, YoY), and the scoring-pillar table's first pillar is **Reported** rather than TTM, spelling out that each is
the latest reported quarter against the same quarter a year earlier.
- The metrics page's two sections are retitled Revenue Growth (Quarter) and EPS Growth (Quarter), describe the quarterly
comparison and why the year-earlier quarter is the right comparison (it takes seasonality out), and each carries a note
naming the old label and the feed key it still uses. The stock method page's two cards match.
- **The deceleration guidance was actively misleading** and is rewritten. It told readers that "consistent deceleration
across four or more quarters is one of the clearest warning signals available" and to watch a +20%, +15%, +10%, +5%
sequence, on a page whose number is a single quarter and cannot show a sequence. It now says to read the company's own
reported quarterly history alongside it, and the red-flag bullet no longer treats one soft quarter as a trend.
- The feed keys `revTTM` and `epsTTM` are deliberately unchanged. They are internal names read by this site and by
Automate Fundamentals, both of which already treat them as quarterly, so renaming them costs a coordinated three-repo
deploy and gains a reader nothing. Automate Fundamentals' matching Learn pages were corrected in its v0.124.2.
- The corrections live in `CONTENT_EDITS` and `SCRIPT_EDITS` in `scripts/invests/site.py`, not in `_sources/`, which
`snapshot.py` regenerates and would silently undo. Each replacement asserts its target is present, so a future snapshot
that rewords any of this fails the build loudly instead of dropping the fix; tested by rewording a snapshot and
confirming the build stops.
- `scripts/invests/check.py` also had three inventory items failing before this change, left over from the ETFs list
growing from 10 funds to 36. Those are allowlisted alongside the ones this change rewrites, so the suite is green again.

## [2.18.0] - 2026-10-08

### Added
- **Azqato's Tools at `/codes/tools/`** (item 22): the ten browser tools and their list, moved from
github.com/Azqato/tools word for word by `scripts/tools-site/migrate.py`, with the shared nav, footer, search
and colors. Each tool has a clean address (`/tools/link-cleaner/`); the old file names redirect. The list's
VIX Strategy and Nasdaq 100 Screener now open their Invests pages. `scripts/tools-site/browser.py` tests it.
- **Azqato's Prompts at `/codes/prompts/`**: the 24 prompts, moved word for word into `prompts/md/`, where they are
written from now on. `scripts/prompts/build.py` gives each a real page (`/prompts/mobile-responsive-audit/`)
holding its description and full text, with Expand and Copy as before; Copy's pointer now names azqato.com.
The plain Markdown is published at `/prompts/md/<slug>.md`. `scripts/prompts/browser.py` tests it.
- Both sections are in the footer, the site search and the sitemap; Codes and Projects link to them here.
- **Codes laid out like Invests** (owner's request, 2026-10-08): Tools and Prompts now live under Codes, at
`/codes/tools/` and `/codes/prompts/` (never live at the shorter addresses, so no redirects). Every Codes page has a
Contents sidebar (Home, then a collapsible Prompts group and Tools group listing every page) and Previous / Next
links, written by `scripts/codes/shell.py`; on phones it folds behind a Contents button. Each page keeps its
original interface inside. The old Prompts sidebar and its logo are gone; prompt search sits above the list on the
Prompts home page, and site search stays in the second bar. Tools use 90% of the width, hero centered.

### Changed
- The build scripts folder is `scripts/` (was `tools/`), so `/tools/` can be the Tools section.

### Fixed
- Tools: tool pages ran edge to edge on phones (`.page` reset `.wrap`'s side padding); now padded.
- `build-nav.py` added a second theme.js line to pages two folders deep on every run.

Not yet done, by the owner's instruction: rollout (push), and the old repos' redirects and retirement.

---

## [2.17.3] - 2026-10-07

### Fixed
- Search Console's four 404s now redirect (301) on Cloudflare: `/home` to the home page, `/Twitter` to
https://twitter.com/azqato, `/stocks/` to `/invests/stocks/`, and `/leveraged-strategies/` straight to
`/invests/leveraged/` (it was a redirect page). Cloudflare's www-to-root and Always Use HTTPS are on (owner).

---

## [2.17.2] - 2026-10-07

### Fixed
- Search Console, "Alternate page with proper canonical tag": the 10 root pages answered at both `/about`
and `/about/` on Cloudflare. `_redirects` now sends the no-slash form to the slash form (301), as `/invests`
already did. The canonical tags were already right; this removes the duplicate address.

Still reported, and expected: `www.azqato.com` and `http://` copies (need Cloudflare redirect settings,
owner's dashboard) and the `azqato.github.io` copy (a second host by design; its canonical points here).

---

## [2.17.1] - 2026-10-05

### Fixed
- Invests' top bar is now the same as azqato.com's on every page (owner's request): 53px tall (was 44),
the same logo size, font and link spacing; the second bar was already 60px on both. On phones the bar
stays, with the same menu button, instead of hiding (its links were in the sidebar).

---

## [2.17.0] - 2026-10-05

### Changed
- Colors follow the Template Interface Color Standard 1.0 across azqato.com and Invests (owner approved
every recommendation of the gap analysis). One file, `colors.css`, holds the standard's roles
(`--ti-color-*`); `styles.css`, `theme.css`'s `--color-*`, the `--pp-*` palette and the source sections'
tokens all point at it. Light is a white page with gray-blue panels; dark is the standard's gray.
- Accent: Azqato's emerald rebuilt at the standard's grades: `#046e55` light; dark fills `#0a9f78`, dark
text `#09ba8c`. Focus ring `#1a8568` everywhere, on azqato.com too.
- Gains are the success green, not the accent (calculator); buttons are the accent, not green (VIX).
- Data and strategy colors (tiers, strategies, VIX tiers, language tags) are palette grade 60 in light and
30 in dark. In dark, all text colors sit at grade 30 so they pass on tinted badges and callouts too.

### Fixed
- Control borders (inputs, selects, buttons) now 3:1 (were 1.36:1 light, 2.02:1 dark).
- Blue text on blue callouts (was 4.44:1); text on the accent fill uses the on-accent role in dark.
- Links in running text on azqato.com are underlined.
- Calculator preview box used the solid accent as its background; now the tint.

Other companies' brand colors (Discord, Spotify, Buy Me a Coffee, YouTube) and the brand catalog page
keep their own values. Contrast checked on all 23 Invests pages and 12 azqato.com pages, both themes.

---

## [2.16.0] - 2026-10-05

### Added
- 9 Sig Calculator at `/invests/leveraged/9sig-calculator` (owner's request; plan in docs/9SIG-CALCULATOR.md).
A quarterly journal in the browser: settings (start amounts, new cash, 9/6/3% target, bond reserve, tickers),
a quarter form with a live preview of the trade, a "This quarter" card with next quarter's signal line, a
dashboard (tiles, return, drawdown, total assets and split charts, all statistics), and a table with key or
all columns. Follows the 9 Sig page's rules: signal line, 90% throttle, 30 Down, Spike Reset; your own action
overrides the suggestion. Several plans; everything kept in this browser's localStorage.
- Import (.xlsx, .csv, or a backup .json, including the community 9-SIG Google Sheet downloaded as Excel):
only the inputs are read, with a preview and a choice of a new plan or replacing the current one.
- Export to Excel (Quarters, Summary and Settings sheets), CSV, and a JSON backup. No libraries: the xlsx is
written and read in `assets/js/own/sig-xlsx.js`.
- A "Track your own plan" link under the 3, 6 and 9 Sig headings.
- `browser.py`: the engine checked against the sheet's rounds 0 to 3 (bond shares, cash, totals, round 3
signal line), plus the page's form, export, import round trip and storage.

### Changed
- `site.py` builds pages written for this site from `tools/invests/pages/` ("own" sources).

---

## [2.15.3] - 2026-10-03

### Added
- FAQ: seven topic groups, from the questions as they already run; no question moved or reworded
(SEO review S7). Each is a section with an h2, so "On this page" lists them, and the filter hides a group
with no matching questions.

### Changed
- Roadmap items 1 and 2: the live Invests site checked (21 pages, two widths, two themes: no errors;
one outside link down, Zacks, for the owner), and PRD Part 2's drafted sections brought up to date:
goals, stories and success criteria marked met, FAQ answers 3, 6, 10 and 12 corrected, D23 records
the 2026-10-03 decisions. New owner questions Q11 to Q13 in docs/OWNER-QUESTIONS.md.

---

## [2.15.2] - 2026-10-03

### Changed
- Invests home: the dead space above "Azqato Invests" is gone (the hero's 80px top padding; owner's request).

---

## [2.15.1] - 2026-10-03

### Changed
- VIX Strategy is one page again, at `invests/indices/vix/` (owner's request): the VIX method page is
folded back in, so the method, the dashboard, the custom builder and the risk notes sit together.
`invests/vix/`, `vix/method.html`, `vix/dashboard.html` and `vix/custom.html` redirect straight
there (redirect pages, plus 301s in `_redirects`).

---

## [2.15.0] - 2026-10-03

The owner's answers to docs/OWNER-QUESTIONS.md.

### Changed
- VIX Strategy moves into Indices & ETFs (owner's request); its address is unchanged.
- Individual Stocks, Indices & ETFs and VIX Strategy are landing pages with cards; their long sections
moved word for word to new Method pages (`stocks/method.html`, `indices/method.html`, `vix/method.html`).
Old links to a moved section forward to the Method page.
- Stocks: 12 metrics everywhere (Q7). The grid gains Gross Margin and Net Margin; `check.py` enforces 12.
- Holy Grail: the two "not accessible" sentences now point at the Composer Atlas figures (C1, C2).
- Resources: two dead thestreet.com links removed (C3, C4); RobinTrack marked "(historical, to 2020)" (C5).
- SEO: an h1 on every page, longer titles, descriptions within 160 characters, no skipped heading
levels, "Related" links on the leveraged, metrics and philosophy pages (S1 to S5).
- Root pages: longer titles; music description rewritten (S2, S3).
- Projects: cards written into the HTML by `tools/prerender-projects.py` (S6); dark C#/HTML tags
brightened to pass contrast (Q5).

---

## [2.14.3] - 2026-10-02

### Changed
- Second-bar names, as the owner chose: "About Azqato", "Azqato's Discord", "Azqato's Music",
"Azqato's Links", "Azqato's Projects" and "Support Azqato" (`BAR_TITLES` in `tools/build-nav.py`).

---

## [2.14.2] - 2026-10-02

### Changed
- Every page except the home page now has a second bar that matches Azqato Invests (owner's request):
the page's emoji and name (for example "💻 Azqato Codes"), "Search the site" and the theme button. The
top bar shows only "Azqato." and the links. The home page keeps its single bar.

### Added
- `search.js` and the generated `search-index.js`: a site search over every root page and every Invests
section. Opens with the button, "/" or Ctrl+K. `tools/build-nav.py` writes the index and the bar.
- `docs/OWNER-QUESTIONS.md`: every open question for the owner, in detail.

---

## [2.14.1] - 2026-10-02

### Added
- `docs/SEO-REVIEW.md` (build pass, item 13; drafts only, nothing live): an audit of all 30 pages
(titles, descriptions, headings, links in the text, length), seven small fixes, and drafts of the
landing and Method pages for Individual Stocks, Indices & ETFs and VIX, for the owner's review.
- `.gitignore`: Python's `__pycache__/`.

---

## [2.14.0] - 2026-10-02

### Changed
- Azqato Invests folded into the main structure (build pass, item 8): its generator, checks and
inventories moved from `invests/scripts/` and `invests/inventory/` to `tools/invests/`. The pages and
their addresses are unchanged.
- Invests' azqato.com strip takes its links from `tools/build-nav.py`, relative to each page.
- `docs/PRD.md`: the folder map is brought up to date (items 5, 7, 8 and 20); Part 2, P14 is marked done.

---

## [2.13.9] - 2026-10-02

### Changed
- The music page's script (2,325 lines: visualizer, player, animated favicon) moved unchanged to
`music/viz.js` (build pass, item 20). The page drops from 119.7 KB to 17.4 KB, and the script is cached
on its own. Checked in Edge: all ten modes animate, the track plays, Pause works, no errors.

---

## [2.13.8] - 2026-10-02

### Changed
- Clean addresses (build pass, item 7): the ten root pages moved into folders, so azqato.com/discord/
replaces discord.html. Each old `.html` address is a redirect page, and `_redirects` sends it to the new
address in one hop on azqato.com. Links still work when a page is opened from disk.
- `tools/build-nav.py` writes the nav and footer links relative to each page and stamps the pages in
their folders. Canonicals, og:url, sitemap.xml and Invests' top bar use the new addresses.
- `docs/PRD.md`: the Future update is marked done, with ten new compatibility entries.

---

## [2.13.7] - 2026-10-02

### Added
- Light and dark themes on every page (build pass, item 5). The site follows the visitor's system theme
until they press the ☀️/🌙 button; the choice is remembered in their browser. music.html stays dark.
- `theme.js` at the root, shared by azqato.com and Azqato Invests (replaces `invests/assets/js/theme.js`).

### Changed
- One palette for the whole site (DESIGN.md): new tokens in `styles.css`; Invests' `--pp-*` colors mapped
to it in `invests/assets/css/site.css`.
- The top bar is the slim full-width strip Invests uses, with the theme button at its end.
- `tools/build-nav.py` stamps the theme button and script; Projects, YouTube and Home colors moved to tokens.
- `docs/DESIGN.md` and `docs/PRD.md` updated (rule 6 replaced; Future update marked done).

---

## [2.13.6] - 2026-10-02

### Changed
- Azqato Invests: one VIX page (build pass, item 12). `/invests/vix/` now holds the strategy, the VIX
Dashboard (`#dashboard`) and the VIX Custom builder (`#custom`), with nothing cut. The old Dashboard and
Custom builder addresses redirect to their sections. Invests has 19 pages.
- `invests/scripts/site.py`: `COMBINE`, `COMBINE_RENAME` and `MOVED`; `check.py` verifies redirect
pages; `browser.py` tests both tools on the one page.
- `docs/PRD.md` Part 2, P16 and Invests: Deprecation and Removal.

---

## [2.13.5] - 2026-10-02

### Changed
- The old stocks, vix and leverage sites now redirect to Azqato Invests (build pass, item 9; D7): 19
pages across those three repos (stocks v5.0.0, vix v2.0.0, leverage v2.0.0), each in one hop to its
new page on azqato.com/invests/. Their data files and scheduled jobs are unchanged. The old vix
Dashboard and Custom builder go straight to their sections of the one VIX page (item 12).
- `leveraged-strategies/index.html`: the old `/leveraged-strategies/` address, a 404 since the repo
rename, now redirects to Leveraged Strategies too.
- `projects.html`: the VIX, stocks and leverage cards' demo links open the Invests pages directly.
- `docs/PRD.md` Part 2, Invests: Deprecation and Removal: the list marked done.

---

## [2.13.4] - 2026-10-02

### Fixed
- Azqato Invests VIX pages (build pass, item 10): when the main VIX feed fails and nothing is cached,
the pages now read the second source, `data/vix.json` from the vix repo via raw GitHub, instead of
waiting on the allorigins relay that browsers refuse. Sources time out after 8 seconds.
- The vix repo's job writes `data/vix.json` too (vix v1.3.0).
- `docs/PRD.md` Part 2, P12: step 2 recorded as done.

---

## [2.13.3] - 2026-10-02

### Changed
- Azqato Invests corrections (build pass, item 11). Resources: the two dead links are removed (Denver
condo listings and Dividend Stocks Online). Holy Grail: a "Backtest on Composer Atlas" box, filled live
from Composer Atlas on every page load, with the figures built in and the last reading saved for when
Atlas can't be reached.
- `invests/scripts/site.py`: `REMOVE_LINKS` and `ATLAS_FIGURES`; `check.py`: `REMOVED`; `browser.py`
prints UTF-8, so its notes no longer crash Windows' console.
- `docs/PRD.md` Part 2, P11: what was done, and the corrections list for the owner (C1 to C8).
`docs/DESIGN.md`: Composer Atlas figures.

---

## [2.13.2] - 2026-10-02

### Fixed
- `music.html` on phones (build pass, item 15e), tested at 320 to 480 px: the stage console spans the
screen, the duplicate badge is hidden, the footer drops from about seven lines to three, and the seek
bar is a 24 px tap target on touch screens. Desktop unchanged.
- `docs/DESIGN.md`: new section, Music page on phones.

---

## [2.13.1] - 2026-10-02

### Changed
- An emoji favicon for each page (build pass, item 21): 🙋 About, 💬 Discord, 💻 Codes, 🎧 Music,
🔗 Links, 🛠️ Projects, 📺 YouTube, ☕ Support, 🎮 Gaming Accounts, 🔒 Privacy; Home stays 🦁. The
Invests pages take their section's emoji (📈 📊 ⚡ 🚀 📚; 💰 for Invests Home).
- Section brands in the top bar: "🎧 Azqato Music" on the music page, "💻 Azqato Codes" on the codes page.
- `tools/build-nav.py` stamps the icons and brands (`ICONS`, `BRANDS`); `invests/scripts/site.py` has `GROUP_ICONS`.
- `docs/DESIGN.md`: new section, Page emoji and section brands.

---

## [2.13.0] - 2026-10-02

### Changed
- Footer on all 12 pages (build pass, item 6): replaced the one-line "Built by Azqato" with a panel
styled after the Azqato Invests footer: the brand, plain links to every site page and every Invests
section, and "© 2026 Azqato". `tools/build-nav.py` now stamps it from one list, like the nav;
`styles.css` holds `.site-footer`; `music.html` uses a compact variant over the stage.
- `docs/DESIGN.md` Footer, `docs/PRD.md` Never do these and Maintenance rules: the footer is generated.

---

## [2.12.6] - 2026-10-02

### Added
- `img/yt-thumb-*-160.webp`: 160 px WebP copies of the four YouTube channel thumbnails, 30 KB in
all against 2.37 MB (build pass, item 15a). The originals stay in `img/`.

### Changed
- `youtube.html`: the thumbnails load the copies, lazily, with width and height set.

---

## [2.12.5] - 2026-10-02

### Changed
- `music.html`: the render loop pauses while the tab is hidden and resumes when it comes back; a
visitor who pressed Pause stays paused (build pass, item 15c).

---

## [2.9.5] - 2026-10-02

### Changed
- `music.html`: no pulsing unless the fire is firing. The background, horizon, floor grid and panel
brightness envelopes are multiplied by `fireGate`, which eases in and out over 250 ms so the gate
itself makes no hard step. Measured in headless Edge: idle luminance spread 0.0086 to 0.0038; worst
playing step 0.0042 (reserved version, Roadmap v2.9.5).

---

## [2.12.4] - 2026-10-02

### Changed
- `.githooks/pre-commit`: a commit that stages a root page is blocked when `tools/build-nav.py
--check` finds any page's nav out of date (build pass, item 15b).
- `docs/PRD.md`: the build pass approved; the owner's answers recorded; the build pass table.

---

## [2.12.3] - 2026-10-02

### Added
- `docs/DESIGN.md`: One palette for the whole site, the owner's picks for every color role in dark
and light (Roadmap at a glance, item 4; Invests P15), with contrast figures.

### Changed
- `docs/PRD.md`: P15 and Roadmap at a glance item 4 marked decided.

---

## [2.12.2] - 2026-10-02

### Changed
- `docs/PRD.md` Part 2, the owner's review of Invests' drafted sections, all suggestions accepted:
Tenet 3 and the "nothing from azqato.com" and "nothing pushed" non-goals removed (D22); Tenet 2 is
now "push only on the owner's word"; Tenet 5 softened for the shared look; a seventh goal (one look
with azqato.com); goals, user stories and success criteria marked met or open; analytics-based
metrics postponed; the press release dated; FAQ 7 mentions Cloudflare's beacon. Earlier text kept.
- `docs/PRD.md` Roadmap at a glance: the full review moves after item 15; the Discord card check is
done; new item 21 (a brand per section, an emoji per page). `docs/TODO.md`: the brand, mascot and
analytics questions answered.

---

## [2.12.1] - 2026-10-02

### Changed
- `docs/PRD.md`: new Roadmap at a glance at the top of the Roadmap, listing every open item from both
halves of the site in one suggested order (now, one site and one look, Invests content, the main
site, later), each pointing at its detail. Part 2's Current phase now leads with what's next and
lists its updates newest first; its Future updates run P12 to P17 in order. The deferred "no
light/dark toggle" row and the "SKIP cleanup" row are marked as reversed and done. No item was
removed.

---

## [2.12.0] - 2026-10-02

### Changed
- Docs merged: Azqato Invests' README, LICENSE and six documents (`invests/docs/`) merged word for
word into the main README, LICENSE and docs, by the owner's decision, keeping the five-document set
closed. `docs/PRD.md` gained Part 2: Azqato Invests (its PRD, HOSTING.md, README and TODO.md);
`docs/DESIGN.md` gained Azqato Invests Visual System (its DESIGN.md and UI-REVIEW.md); its patch
notes are the Azqato Invests history at the end of this file; `LICENSE.md` carries its terms.
- New decision, PRD Part 2, D22: the main site's rules, docs and design win. Supersedes its D5 and
Tenet 3.
- Version numbers combined: Invests changes are main 2.x entries from now on (its own line ended at
v1.1.1).
- `docs/PRD.md`: Part 1 places that still described `invests.html` as the investing hub marked with
the current state; Documentation Versus Reality rows 37 to 39; Current phase and the Which document
table point at Part 2. `docs/DESIGN.md`: rule 6 (no light theme) and the two `invests.html` cards
marked. `README.md`: the Invests row and the investor line describe the 21-page site.
- `invests/scripts/check.py`, `browser.py`: docstrings point at the PRD's Part 2.

### Removed
- `invests/README.md`, `invests/LICENSE.md` and `invests/docs/` (PRD, DESIGN, PATCHNOTES, HOSTING,
TODO, UI-REVIEW), after a script confirmed every paragraph and table row is in the merged docs.

---

## [2.11.3] - 2026-10-02

### Changed
- Azqato Invests v1.1.0: its sections are grouped by topic (Individual Stocks, Indices & ETFs, VIX
Strategy, Leveraged Strategies, Resources) at new addresses; the old ones were live about an hour
and get no redirects (owner's decision). See invests/docs/PATCHNOTES.md.
- Roadmap (Future updates): the Invests top bar and theme button across the whole site, clean
addresses for every page (`/discord` instead of `discord.html`), and the Invests footer across the
whole site.

---

## [2.11.2] - 2026-10-02

### Changed
- Azqato Invests v1.0.1: the pager buttons fit their text, with Next at the right edge; the gap above
the pager on Home and Resources matches the other pages; the sidebar's "Educational use only. / Not
financial advice." note sits at the bottom of the sidebar on two lines.
- The working notes from the merge (HANDOVER.md, never committed) moved into invests/docs/PRD.md
and were deleted. The post-launch list (old-site redirects, the two dead Resources links, deleting
the empty Azqato/invests repository after testing) is on the invests roadmap (P13).

---

## [2.11.1] - 2026-10-02

### Changed
- `invests/` in this repository is now the single source of truth for Azqato Invests. The separate
local repository it was built in is retired and will be deleted; nothing is edited there.
- invests/docs/PRD.md: Repository Hygiene, the Runbook's Local setup, Build and Deploy, and Rollback
describe working in `invests/` here instead of copying from the separate repository.

### Deployed
- Pushed 2026-10-02 (v2.11.0 and v2.11.1); Azqato Invests is live at https://azqato.com/invests/.
Post-deploy check: all 43 served files under invests/ match the local copies byte for byte;
https://azqato.com/invests and /invests.html answer 301 to /invests/ in one hop (`_redirects` works);
https://azqato.github.io/invests.html redirects to invests/index.html. In headless Edge, light and
dark: Home, the Screener (data loaded) and the VIX Dashboard (LIVE) show no script errors.

---

## [2.11.0] - 2026-10-02

Azqato Invests moves in. The investing site built in its own repository (stocks, vix and leverage
merged with this site's invests.html, 21 pages) now lives in `invests/`, served at
https://azqato.com/invests/. It is self-contained for now: its pages, assets, generator, checks and
docs are all inside the folder, and its own docs (invests/docs/PRD.md) govern it. Folding it into
this site's structure is planned for later. Its history stays in its own repository.

### Added
- `invests/`: the 21 pages, assets, sitemap.xml, scripts and docs of Azqato Invests.
- `_redirects`: Cloudflare Pages rules sending `/invests` and `/invests.html` to `/invests/` in one hop,
so the old page and the new folder never compete for the address.
- robots.txt: a second Sitemap line for https://azqato.com/invests/sitemap.xml.

### Changed
- `invests.html` is now a one-file redirect page to `invests/` (the first compatibility entry under the
removal policy). Its content lives on in the new Home and Resources pages, word for word.
- The nav's Invests item, the Home explore card and the Links page button point at `invests/`
(tools/build-nav.py updated and rerun).
- sitemap.xml: the Invests entry is https://azqato.com/invests/.
- Links to the new site use `invests/index.html`, so they also work when a page is opened from disk
(a folder link there shows a file listing); Cloudflare Pages serves it as /invests/.
- .githooks/pre-commit skips `invests/inventory/`: word-for-word records of the source pages, not pages.
Azqato Invests' pages are checked as usual (their missing-value mark is now an en dash).
- docs/PRD.md: site structure, folder structure, public surface and compatibility entries.

### Verified
- Served from this repository's root in headless Edge: all 21 pages under /invests/ in light and dark,
no script errors, no failed requests, no links leaving the folder; the screener loads its data and the
VIX tools read LIVE; invests.html lands on /invests/. `python invests/scripts/check.py`: 0 failures.
- Not verified: the `_redirects` rules (Cloudflare only) and the live deploy; nothing is pushed.

---

## [2.10.7] - 2026-09-29

The canonical domain is a **Cloudflare Pages** deployment, not GitHub Pages behind a proxy. Every
document in this project had the hosting wrong, and the v2.9.9 audit had confidently refined it to a
different wrong answer. The owner corrected it in one sentence: "I use Cloudflare Pages instead of
GitHub."

### What is actually true
`azqato.com` and `azqato.github.io` are **two independent deployments of the same commit**, not a
proxy and an origin. Each builds from a push to `main`. Neither knows about the other. That explains
several things this project had recorded as unexplained or had explained wrongly:

- The `.html` to extensionless 307 found during the v2.10.6 deploy check is Cloudflare Pages' default
  URL handling, not a mystery rule somebody added.
- `cfOrigin;dur=0` on every request was not aggressive caching in front of an origin. There is no
  other origin to contact.
- The empty 404 on `azqato.com` against GitHub's styled 404 on `azqato.github.io` is two different
  products, not one product behaving inconsistently.

Corroborated before changing anything: Cloudflare nameservers, Cloudflare IPs on both apex and `www`,
no GitHub headers anywhere in the `azqato.com` response.

### Fixed, and one of these was a real problem
- **`privacy-policy.html` named the wrong data controller.** It said "The site is hosted on GitHub
  Pages" and told readers their server-log data sits with GitHub. For the canonical domain, where
  essentially all traffic goes, it sits with **Cloudflare**. The page now describes both hosts, says
  which serves which address, and says plainly that in practice it means Cloudflare. This shipped
  yesterday in v2.10.5, so it was wrong for one day. It is the one item here with consequences beyond
  tidiness, which is why it was fixed first.
- **The deploy-verification step was checking the wrong host, for a reason that no longer exists.**
  v2.10.3 had deliberately kept the check on `azqato.github.io`, reasoning it was "the origin" and that
  `azqato.com` was a cache that might lie. With two independent deployments, **a green GitHub Pages
  build is not evidence that Cloudflare Pages built anything at all**. The check could have passed
  while the canonical domain sat on a failed build. It now checks `azqato.com` with a cache-buster, and
  says explicitly that each host reports only on itself.
- Architecture diagram, hosting table, third-party data tables, Security Model, and the environments
  note all corrected.

### The CNAME milestone is closed as moot, not deferred
A `CNAME` file is a **GitHub Pages** mechanism. `azqato.com` does not run on GitHub Pages, so the file
would have done nothing for it. Everything the milestone worried about dissolves with the premise: the
DNS never needed confirming for this purpose, the Pages custom-domain field was never going to be
involved, and the redirect-loop risk that justified holding it back could not occur, because there is
no proxy relationship to loop through. The milestone's real goal, making `azqato.com` canonical, was
already met by what shipped on 2026-09-28.

The caution cost nothing and was reasonable given what was believed. But the entire analysis, several
hundred words across three documents, rested on an assumption about infrastructure that is described
nowhere in this repository and was never flagged as an assumption. **When a plan depends on how
something outside the repository is wired, ask before writing the plan.**

### A constraint that turned out to be false
Both the Security Model and the constraints table said no CSP was possible because GitHub Pages cannot
send custom response headers. True of `azqato.github.io`. **False of `azqato.com`**, which runs on
Cloudflare Pages and supports a `_headers` file. Nothing was added, and going without a CSP is still
defensible on a static site with no user input. The change is that it is now a decision rather than a
limitation, and the documents say so.

### Changed
- **Music page sharing copy**, at the owner's request, reframed around why the page exists rather than
  what it does. `og:title` is now "A Concert Stage Built to Showcase the Music"; the description leads
  with Azqato building the page to showcase his music. Re-ran the v2.10.4 compliance gate: 43 and 172
  characters, no site name in `og:title`.

### Decided
- **Internal links keep their `.html`.** Each internal click on `azqato.com` therefore takes a 307 to
  the extensionless form. It costs a few milliseconds. Dropping the extensions would mean changing the
  nav generator and every page body, and would stop the site working when a page is opened straight
  from disk, which is how it has always been developed. Canonical and `og:url` already point at the
  extensionless destination, so shared links and crawlers are unaffected. Not revisited unless the
  development workflow changes.

---

## [2.10.6] - 2026-09-28

Canonical and `og:url` repointed at the URLs `azqato.com` actually serves. A same-day fix to a defect
introduced by v2.10.4, found by verifying the deploy rather than assuming it.

### The defect
v2.10.4 wrote `https://azqato.com/projects.html` into every canonical and `og:url` tag. Checking the
live site afterwards showed that `azqato.com` **307-redirects `/projects.html` to `/projects`**. There
is a Cloudflare rule stripping the extension, which nobody had recorded anywhere, and the audit never
saw it because it was reading the repository rather than the responses.

So all 11 non-index pages were declaring a canonical URL that immediately redirects. That is a
self-defeating signal: the tag says "the authoritative address is X", and X replies "no, it is Y". A
crawler will usually follow it and land in the right place, but a canonical is a statement about the
preferred address, and pointing it at a redirect weakens the one thing it exists to assert. The
sitemap had the same 11 URLs and the same problem.

### Changed
- All 11 non-index pages: `rel="canonical"` and `og:url` drop the `.html`.
- `sitemap.xml`: the same 11 `<loc>` values, with a comment recording why the URLs are extensionless
  so the next person does not "fix" them back.
- `index.html` was already correct. It declared `https://azqato.com/`, which returns 200 directly.

Verified on both hosts before changing anything: the extensionless form returns 200 on `azqato.com`
and on `azqato.github.io`, because GitHub Pages serves `/projects` for `projects.html` natively. The
declared URLs are therefore correct on the origin as well, which matters while the `CNAME` is still
outstanding.

### Not changed
Internal nav and body links still use `.html`. On `azqato.com` every internal click therefore takes a
307 before landing. That is a pre-existing condition of the Cloudflare rule rather than anything this
batch introduced, and changing it means touching the nav generator and every page body, which is a
separate decision. Recorded in `docs/TODO.md`.

### Also verified, and one trap recorded
Every declared canonical URL and every `sitemap.xml` entry was resolved against both hosts after the
deploy: 12 of 12 return 200 directly, with no redirect, on `azqato.com` and on `azqato.github.io`.

The Cloudflare analytics beacon was re-checked at the same time and **nearly produced a false
correction.** A plain `curl https://azqato.com/` returns a page with no beacon in it, which looks like
proof the analytics had been switched off and the privacy policy shipped hours earlier was wrong. It
is not. Cloudflare injects the beacon only when the request carries an `Accept: text/html` header,
which every real browser sends and `curl` does not. With the header it appears deterministically, on
`azqato.com` and never on `azqato.github.io`. The privacy policy is accurate as written. The check is
recorded in the PRD Security Model so the next person does not "fix" a correct page on the strength of
a bare `curl`.

### Worth keeping
The deploy check is what caught this. Confirming that a page went live is a weaker check than asking
whether the thing shipped is actually correct against the live site, and the second one is what found
a redirect rule that exists in nobody's documentation. The gap was not in the code; it was that the
head tags were written from the repository's filenames without ever asking what the canonical host
does with them.

---

## [2.10.5] - 2026-09-28

`privacy-policy.html` rewritten to describe this site rather than a generic one. The page was the last
piece of the analytics decision: v2.10.0 fixed the copy that claimed the site had no analytics, but the
privacy policy is the page a reader actually goes to when they want to know, and it was still generated
boilerplate from 2024 describing a site with ads, accounts and cookies. 14,212 bytes down to 13,381,
which is the right direction, because the old page was longer for being generic rather than for saying
more.

### Removed
- **Consent**, which described a log-in flow that does not exist.
- **Google DoubleClick DART Cookie**, **Advertising Partners** and **Third Party Privacy Policies**,
  all of which described ad networks this site has never carried.
- **Cookies and Web Beacons**, which explained cookie handling for a site that sets none.
- **How We Use Your Information**, a list of uses for information that is never collected.

A policy that describes the wrong site is worse than a short one. It is confidently wrong about exactly
the thing the reader came to check, and every false protection in it makes the true statements next to
it harder to believe.

### Added
- **The short version**, at the top, stating plainly that there are no accounts, forms, comments,
  newsletters or ads, no cookies set by the site, and no marketing trackers, then naming the three
  things that do see a visitor: the host, the analytics on the main domain, and the embedded players.
- **Web server logs.** GitHub Pages records requests as any web server does, including IP address,
  user agent, page and referrer. That is hosting infrastructure rather than a choice made here, and
  GitHub controls that data under its own policy.
- **Analytics on azqato.com.** The real disclosure, and the reason this milestone existed. It names
  Cloudflare, says the script is injected at the edge before the page reaches the visitor, and is
  specific about what kind of analytics it is, because "analytics" covers very different things: it is
  cookieless, does not fingerprint, does not build a profile, does not follow anyone between sites and
  is not shared with advertisers. It then says any blocker stops it and nothing on the site breaks,
  which is true and is the part most policies leave out.
- **Embedded players on the Music page.** Mixcloud and YouTube are loaded directly by the browser, so
  they see the visitor's IP and may set their own cookies, and this happens on page load rather than on
  play. No other page loads anything third party, and the one locally served track involves nobody.
- **Your rights over your data.** States the GDPR and CCPA rights, then refuses the usual dodge: this
  site holds no personal data to hand over or delete because it collects none, and the data that does
  exist sits with GitHub, Cloudflare, Mixcloud and YouTube as separate controllers, so a request is
  best made to them directly.
- **Copyright**, pointing at `LICENSE.md`, closing the last place the site implied its source was free
  to reuse.
- **Changes and contact**, noting that the revision history is public so any change to this page can be
  read in the repository, and ending by saying the page has not been reviewed by a lawyer and is not
  legal advice.

### Kept
- Children's Information, Affiliate Links, Financial Disclaimer and Entertainment Purposes, which were
  the four sections that were already accurate. The affiliate section gained a sentence naming where
  the links actually appear, which is the Support page and parts of Invests.

### Changed
- Hero: "Last updated: 2024. Accessible from azqato.github.io" became "Last updated: 28 September 2026.
  Applies to azqato.com and azqato.github.io, which serve the same site."

---

## [2.10.4] - 2026-09-28

Page heads: titles, social sharing tags, meta descriptions and canonical URLs, on all 12 pages. The
item with the actual payoff in this batch. Before this, every link shared to Discord rendered as a bare
URL with no title card, on a site whose primary call to action is its Discord page, and all 12 browser
tabs truncated to the same word.

### Added
Nine tags in every head, verified by count on each page rather than by spot-check: `<title>`,
`<meta name="description">`, `<link rel="canonical">`, `og:title`, `og:description`, `og:url`,
`og:type`, `og:site_name`, `twitter:card`.

- All `og:url` and `canonical` values are absolute on `https://azqato.com/`, the canonical domain
  decided at the audit. They are correct today: that domain already serves this site through
  Cloudflare, and the `CNAME` decision that is still outstanding changes which host is formally
  authoritative, not whether the address works.
- **No `og:image`, which is the specification rather than an omission.** The documentation spec puts
  images off by default, so `twitter:card` is `summary` rather than `summary_large_image`. Cards render
  as text. Adding an image later changes both settings together and needs a real per-page image or one
  credible default, not a logo stretched to fit.

### Changed
All 12 titles, from brand-first with a pipe (`Azqato | Projects`) to page-first with a suffix:

| Page | Was | Now |
|------|-----|-----|
| `index.html` | Azqato \| Welcome | Azqato - Communities, Projects, Music |
| `about.html` | Azqato \| About | About - Azqato |
| `discord.html` | Azqato \| Discord | Discord Communities - Azqato |
| `invests.html` | Azqato \| Invests | Investing Tools and Resources - Azqato |
| `codes.html` | Azqato \| Codes | AI Prompts and Coding Tools - Azqato |
| `music.html` | Azqato \| Music | Music and DJ Mixes - Azqato |
| `links.html` | Azqato \| Links | All Links - Azqato |
| `projects.html` | Azqato \| Projects | Projects - Azqato |
| `youtube.html` | Azqato \| YouTube | YouTube Channels - Azqato |
| `support.html` | Azqato \| Support | Support the Work - Azqato |
| `accounts.html` | Azqato \| Accounts | Gaming Accounts - Azqato |
| `privacy-policy.html` | Azqato \| Privacy Policy | Privacy Policy - Azqato |

The two that identified nothing to a stranger, "Welcome" and "Codes", now say what the page is. The
longest title is 38 characters against a 60 character budget, and no two pages share their first 30
characters, which is roughly what a tab shows.

### How it was applied
By script, with a compliance gate that ran to completion before a single file was written. The gate
failed the entire run on any title over 60 characters, any `og:title` over 70, any description over
200, an `og:title` containing the site name, a non-index title missing the suffix, two pages sharing
their first 30 characters, or a placeholder title. It passed on the first complete run. The ordering is
the part worth repeating: a script that validates all of its input before touching any of 12 files
cannot leave the repository half-edited.

### Verified
- `python tools/build-nav.py --check` clean, which matters because the nav block sits in all 12 heads.
- Browser test in headless Edge against a local server on `index`, `projects`, `music` and
  `privacy-policy`. All render correctly, with the music page's stage, lasers, local track, both
  Mixcloud embeds and the visualizer mode buttons intact.
- Still outstanding, because it cannot be done before deploying: paste two or three live URLs into
  Discord and look at the cards. That is the only check that tests what this milestone is for.

---

## [2.10.3] - 2026-09-28

Canonical domain, repository side. **Partial by design: the `CNAME` file was deliberately not created.**

### Changed
- `sitemap.xml`: all 12 `<loc>` values repointed from `azqato.github.io` to `azqato.com`, with a
  comment recording that the canonical domain was decided on 2026-09-28.
- `robots.txt`: the `Sitemap:` line and the header comment repointed.
- `README.md`: the live link is now `https://azqato.com/`.
- `docs/PRD.md`: the public-surface definition, the compatibility-entry example, the deploy step, the
  Environments table, Monitoring, the north-star metric, the press release dateline and its call to
  action. The unresolved note asking whether `azqato.com` was related to this repository was marked
  resolved: it is this repository, served through Cloudflare. The absence of a `CNAME` had been read as
  evidence the domain was unrelated, which was wrong.

### Not changed, on purpose
The `CNAME` file. It is the one change on the roadmap that can take the site down, and it depends on
the DNS records and the GitHub Pages custom-domain setting, both of which live outside this repository
and neither of which could be confirmed. Everything above is a text edit one revert undoes.

This split is why the batch is coherent rather than contradictory. The owner had excluded v2.10.3 from
the batch to avoid exactly this risk, which was sound, but v2.10.4 writes `azqato.com` into 12 page
heads, and shipping that while the sitemap still said `azqato.github.io` would have left the site
declaring one canonical address in its heads and another in its sitemap. That is worse than the
ambiguity it started with: two hosts merely competing is something a crawler resolves conservatively,
whereas an active contradiction invites it to pick, and it may not pick the intended one. Splitting on
the line of what needs DNS, rather than on the milestone boundary, let the risky part wait while the
rest shipped consistently.

### Deploy verification stays on the origin
The runbook still says to confirm a deploy by opening `azqato.github.io` rather than `azqato.com`, and
that is now a documented decision rather than a leftover. Cloudflare sits in front of the canonical
domain and caches, so a stale page there says nothing about whether GitHub Pages published, and a fresh
one might be a cache hit from before the push. The origin answers the question the check is asking.

---

## [2.10.2] - 2026-09-28

`.gitattributes` added at root, pinning `* text=auto eol=lf` with explicit `binary` lines for `*.mp3`,
`*.jpg`, `*.jpeg`, `*.png`, `*.gif` and `*.ico`.

### The finding that prompted this was wrong, and the correction is the useful part
The v2.9.9 audit recorded that `music.html` was committed with CRLF while every other text file was LF,
and scheduled a "deliberately noisy" commit that would rewrite all 12 pages. That was checked properly
before running, with `git ls-files --eol`, which is the authoritative test. **Every committed blob in
this repository was already LF, `music.html` included.** The CRLF existed only in the working tree, on
`music.html` and `.vscode/settings.json`.

What had been keeping the repository clean was `core.autocrlf=true` in the local git config, which
converted silently on the way in. That is not part of the repository. A second machine, a CI runner or
a fresh clone with a different setting would have committed CRLF, and nobody would have noticed until
the diff arrived.

So this file does not repair a broken repository. It moves a guarantee that was an accident of one
machine's configuration into the repository, where every clone gets it. That is a better reason than
the one the audit gave.

`git add --renormalize .` produced **zero changes**. The predicted 12-file diff never existed. The
sequencing advice that put this milestone first cost nothing and was sound reasoning, but it was
reasoning built on a premise that was cheap to check and had not been.

The lesson worth keeping: `git status` and editor line-ending indicators describe the working tree, not
the repository. Only `git ls-files --eol` answers what is actually committed.

### Note
`tools/build-nav.py` still contains its deliberate code to preserve whatever line ending each file
already uses. That note in the audit was accurate. It is belt-and-braces now rather than a workaround,
and it was left alone.

---

## [2.10.1] - 2026-09-28

`tools/build-nav.py`: the `SKIP` set listed `nav-extraction-test.html` and `reduced-motion-test.html`,
neither of which has existed for some time. Leaving them there implied a rule the project no longer
has, and the next reader would have had to check whether those files mattered.

`SKIP` is now an empty set with a comment naming what used to be in it and why it is gone. Emptying it
rather than deleting the mechanism costs one line and is the better shape: the loop that reads it is
untouched, so the next person who genuinely needs to exclude a page adds a filename instead of
rebuilding the feature. No behavioral change, since the script only ever iterated files that exist.
`python tools/build-nav.py --check` reports the nav is up to date in every page, which is the same
answer it gave before, and that is the point.

Offered at the v2.9.9 audit and deferred with "revisit this later", then pulled back into scope the
same day when the owner scheduled the batch.

---

## [2.10.0] - 2026-09-28

Copy alignment, applied immediately after the v2.9.9 audit closed. The audit put six questions to the
owner and all six were answered the same day. Five of the six became scheduled Roadmap milestones
(v2.10.2 through v2.10.5). This entry covers the one part that was pure documentation and so was
applied rather than scheduled: the sentences that had become false the moment a licence existed and
the moment the Cloudflare beacon was found.

### Changed
- **External FAQ, the open-source answer.** It read "Yes. The site and nearly every project on it are
  open source at github.com/Azqato." Now separates the two things it had run together: the individual
  projects are mostly public repositories carrying their own licences, while this site is
  source-available rather than open source, readable on purpose but reserved, with `LICENSE.md` setting
  out what is granted and an invitation to ask for anything else.
- **Press release boilerplate.** "Everything he builds is open source, runs entirely in the browser,
  and is free to use" became "Everything he builds runs entirely in the browser and is free to use, and
  most of the projects are public on GitHub."
- **Security Model, what the site collects.** It read "None. No analytics, no cookies set by the site,
  no tracking pixels, no forms, and no accounts." That was true of the source and false of what a
  visitor to the canonical domain receives. It now states both: nothing from the site's own code, plus
  GitHub's server-level request logging and the Cloudflare Web Analytics beacon injected into every
  page served from `azqato.com`.
- **External FAQ, "Why no analytics?" became "What analytics does the site use?"** The old answer
  defended a position the site no longer holds. The honest description is now "no tracking of its own,
  plus cookieless aggregate counts from the CDN", and the entry says so rather than defending the
  earlier absolute claim, because Tenet 6 does not leave room for a claim that is technically about the
  source while being false about what a visitor gets.
- **North star metric.** The paragraph explaining the metric's weakness assumed no analytics existed at
  all. Annotated: Cloudflare Web Analytics does hold real page-level visit counts that were never taken
  into account when the metric was designed. Whether to start reading them, and whether the metric
  should be redefined around them, is left unresolved rather than answered in passing.
- `docs/TODO.md`: the six decided items moved out of Decisions Waiting On The Owner and into a Decided
  section pointing at the Roadmap milestones, leaving three genuinely open items.

### Decisions recorded
All six are written up in full, with effort estimates, sequencing and open risks, under Decided At The
v2.9.9 Audit in the PRD Roadmap. In brief: keep all rights reserved; `azqato.com` is canonical; keep
the Cloudflare beacon and fix the copy; add the full sharing-tag set to all 12 pages; fix all 12 page
titles in the same pass; add `.gitattributes` and normalize everything. The smaller cleanups in
`docs/TODO.md` were offered and deferred.

### Not changed
- Nothing outside `/docs` and `README.md` was touched **in this version**. No page head, no title,
  no `CNAME`, no `.gitattributes`, and no `privacy-policy.html`. All of those except the `CNAME`
  shipped later the same day as v2.10.1 through v2.10.5. Those are the four scheduled milestones, and the
  recommended order puts the renormalization first so its whitespace-only diff across all 12 pages
  does not contaminate the head edits.
- No version control command that changes state was run.

---

## [2.9.9] - 2026-09-28

Full documentation audit, the first since v2.8.5 on 2026-08-24, covering the 17 commits since.
Read every document in `/docs` in full plus the README, then checked them against the code in
three passes. Four files created, 13 new discrepancies recorded, six questions left open for the
owner. No page was browser-tested, because a documentation-only change is a minor update under
the cadence policy this entry adopts.

### Added
- `LICENSE.md` at the repository root. The project had no licence text anywhere, while the README
  invited people to copy the source. Adopted the all rights reserved, source-available default,
  with sections covering no licence granted, AI search and automated access, no waiver, permission,
  platform terms, third-party content, no warranty, and the not-financial-advice disclaimer. AI
  referencing and quoting are granted; substitution is not; training data is routed to a request
  on the public issue tracker.
- `robots.txt` at the root. Confirmed missing by a live 404 on both hosts, not just absent from the
  repository. Fully open to every crawler with no exclusions, carrying a comment that says the
  openness is deliberate and that `LICENSE.md` wins if the two ever look like they disagree.
- `sitemap.xml` at the root, listing all 12 pages, which is every page: none sits behind a sign-in.
  Each `lastmod` is that page's last commit date read from git, not today's date. `robots.txt`
  names it on a `Sitemap:` line.
- `docs/TODO.md`. Seeded from open items already scattered through the other documents plus what
  this audit turned up. It is a holding place, explicitly not an instruction list, and it is never
  consolidated, merged, moved, or deleted.
- PRD: six new sections. **Verification Environment** (verify locally, never against production;
  `file://` does not count for `music.html` because it disables audio routing). **Testing Cadence**
  (see Changed). **Repository Hygiene** (a policy record, reported as a table of 10 rules against
  their actual state). **Licensing**. **Social Sharing Tags**. **Page Titles**, which this project had never recorded and   fails on all 12 pages, every one of them brand-first with a pipe separator so that every tab
  truncates to the same string.
- PRD Roadmap: a **Future updates** section, opening with a proposal for a progress dashboard built
  from the prompt at `https://azqato.github.io/prompts/p/progress-dashboard.html`. Added rather than
  adopted as a rule because this project has no `CLAUDE.md` and so no existing dashboard convention.
- PRD Roadmap: a **Verification checklist** naming the seven areas whose claims were not read in code
  at this audit and are carried forward on an earlier audit's authority.
- PRD: Open Questions 9 through 14, and Documentation Versus Reality rows 21 through 33.

### Changed
- **Testing Cadence replaced the project's rule of that kind.** The old rule required a browser check
  after every edit with no project-specific reason recorded for the frequency. The replaced wording
  was, in How to Verify a Change: "There is no test suite, so verification is manual and specific. Do
  all of these:", together with the Monitoring table row "Console errors | DevTools Console on the
  changed page | After each change". The default now applies: browser tests use headless Edge with a
  unique `--user-data-dir`; an assumption check and one browser test run immediately before a major
  update ships; minor updates (wording, docs, comments, patch notes) ship without either; batched
  edits are tested once; and confirming a deploy arrived is not a test. The verification steps
  themselves are unchanged, and the section now says the cadence governs when they run, not what
  they contain.
- **Never Do These: the visualizer rule had inverted and was rewritten.** It read "Never claim in copy
  that the music visualizer reacts to the audio. It does not." It does. `music.html` builds a real
  `AnalyserNode`, calls `createMediaElementSource` on the native player, and drives the lights from
  `getByteFrequencyData` every frame. The rule now draws the real line: true for the one same-origin
  track, false for the cross-origin Mixcloud and YouTube embeds, and false on `file://` where
  `canRouteAudio` is false and the page says so. The old wording is quoted in place. Following the old
  rule would have required deleting true sentences from the README and the FAQ.
- **README** made precise about analytics instead of left inaccurate. It claimed "no analytics, and no
  tracking" without qualification. `azqato.com` and `www.azqato.com` both serve a Cloudflare Web
  Analytics beacon, injected at the edge and not present in this repository's source;
  `azqato.github.io` is clean. The README now distinguishes what the site's own code does from what
  the `azqato.com` edge adds. Whether to keep the beacon is Open Question 12.
- **README**: "The source is open. Read it, copy it, or use it as a starting point for your own site"
  became a neutral pointer to `LICENSE.md`. A bare grant with no licence text behind it is an
  ambiguity, and leaving it beside a reserved-rights licence would mislead a reader in one direction
  or the other. The new wording asserts neither posture, pending Open Question 9.
- **Documentation Process: the document set is five, not four.** The old text read "Exactly four
  documents. No fifth file is created inside `/docs`", and maintenance rule 7 read "Never create a new
  `.md` file in `/docs`. Add a section to one of the three instead." Both contradicted the newly
  required `docs/TODO.md` and were updated to name it as the last addition.
- DESIGN.md: four stale claims corrected. `styles.css` given as 2,282 bytes, actually 2,887 since the
  v2.8.7 reduced-motion block. Only `lang-js` and `lang-html` described as in use; `lang-cs` joined
  them in v2.9.8. `.track-tag` described as reading "Drives the visualizer", text removed in v2.9.4;
  it carries the track credit now. Build rule 4 said "Any new page copies the nav block verbatim from
  an existing page... There is no shared nav include yet", false since v2.8.8 and contradicting
  DESIGN.md's own navigation section; replaced with the generator workflow, because as written it
  instructed the reader to do the one thing Never Do These forbids.
- PRD: `music.html` given as "roughly 91,000 bytes" in the Build section against 114 KB in nine other
  places. It is 117,417 bytes. Shared CSS given as 2.3 KB, now 2.8 KB.
- PRD: the Current Phase claim that "nothing is waiting on a decision any more" was true after v2.8.9
  and is not now.
- PRD: `2.9.5` added to the reserved version numbers, held for the visualizer brightness gate.
- PRD: the em-dash compliance paragraph still named `.vscode/recentfedsummary.MD` as out of
  compliance; that file was deleted in v2.8.9. Replaced with this audit's sweep result, which is zero
  violations across every tracked file and the four new ones, with six exempt occurrences inside
  backtick code spans where the rule names the character it prohibits.
- PRD: the Browser Testing section said the Edge binary path "has not been verified on this machine".
  It was verified at this audit.
- PRD: the press release said fourteen tools; it is fifteen as of v2.9.7.
- PRD: Working Practice gained a step to check `docs/TODO.md` before pushing, an explicit "ask before
  pushing" step, and a note that confirming the deploy afterwards is a comparison rather than a test.
- PRD: How An Audit Is Run gained five steps covering reading TODO.md, checking that required files
  are actually served rather than merely mentioned, keeping a policy record separate from an action,
  and naming what was not verified.

### Fixed
- The PRD's open question about whether `azqato.com` is related to this repository, which reasoned
  from the absence of a `CNAME` file that it was not. It is: the domain serves this exact site through
  Cloudflare, all 12 page footers link it, and git history shows a `CNAME` created and then deleted.
  Answering it opened a larger one, because the repository now demonstrably has two live hosts and no
  recorded canonical. See Open Question 10.

### Not changed, on purpose
- **No `CLAUDE.md` and no `/dashboard` were created.** An audit does not create a `CLAUDE.md` for a
  project that has none, and with no existing progress-dashboard convention the standing rule was not
  added either; a Future Updates roadmap entry proposes one instead.
- **No `.gitattributes` was created**, though its absence is a real gap: `music.html` is committed CRLF
  while everything else is LF, and `tools/build-nav.py` deliberately preserves per-file endings. A
  blanket `eol=lf` would rewrite all 12 pages in one diff. Repository Hygiene is a policy record, not
  an action, so this is recorded as a discrepancy and as Open Question 13.
- **No page head was edited**, although all 12 pages carry zero `og:` tags, zero `twitter:` tags, no
  meta description, and no canonical tag, and all 12 titles are brand-first. Social Sharing Tags and
  Page Titles are both policy records, and the specification puts a page edit outside an audit. The
  work was decided on the same day and is scheduled as Roadmap v2.10.4.
- **`privacy-policy.html` was left as it is** at the audit. Boilerplate describing Google DART cookies
  and ad networks this site does not have, recorded as row 17 and Open Question 6 since the v2.8.5
  audit. The owner decided on 2026-09-28 to rewrite it, scheduled as Roadmap v2.10.5, and it is now
  the page that has to carry the real Cloudflare disclosure.
- **`tools/build-nav.py`'s `SKIP` set** still names two files that no longer exist. Harmless dead
  configuration in a working script, outside this audit's write scope, logged in `docs/TODO.md`.
- **No version control command that changes state was run.** Nothing was staged, committed, pushed, or
  untracked by the audit.

---

## [2.9.8] - 2026-09-28

### Added: Automate Fundamentals on the Projects grid
The v2.9.7 note said this project was left off `projects.html` because that page's card
array requires a `github` field and there is no public repository. The rule below settles
that, so the card is now on both pages.

- Added a fifteenth entry to the `PROJECTS` array, placed first to match its position in
  the Invests grid.

### Changed: the `github` field falls back to the project's own site
**Adopted as a standing rule.** When a project has no public repository, its `github` field
points at the project's own site and `demo` is set to the same URL.

- This is not a new pattern so much as a named one. Two entries already did it, No Fee
  Apartments and LV Guest List, both external commercial sites. Automate Fundamentals is
  the third and the first that is private rather than external.
- The GitHub icon button was hardcoded to `title="View on GitHub"`, which became false the
  moment the link went anywhere else, and had been false on those two cards for as long as
  they have existed. `buildCard` now tests the `github` value against
  `^https://github.com/` and labels the button "No public repository, opens the project
  site" when it does not match.
- The label is derived from the URL rather than from a flag on the entry, because a flag is
  a second thing to remember and would eventually disagree with the link it describes.
- The button also gained an `aria-label`. A `title` alone is not reliably announced, and an
  unlabelled link containing only an SVG reads as nothing useful.
- The octocat mark itself still renders on all three. It marks the repository slot rather
  than the destination, and relabeling it is what keeps that honest.

### Documentation
- `docs/PRD.md`: the project count moved from 14 to 15 in the page inventory, in F1, and in
  the array-order list.
- `docs/PRD.md`: the sentence describing the two external-site entries is replaced by a
  full statement of the fallback rule, how the card detects it, and why it is read off the
  host instead of a flag.
- `docs/PRD.md`: the `PROJECTS` schema comment for `github` now describes the fallback.
- The new entry is tagged `lang-cs`, for .NET. That class has been defined in the page's
  stylesheet since it was written but no project had used it, so this is the first card to
  render the C# green.

---

## [2.9.7] - 2026-09-28

### Added: Automate Fundamentals on the Invests page
A new site is in progress at `automatefundamentals.com`, and the Invests project grid is
where it belongs.

- Added a seventh card to the `invests.html` project grid, placed first because it is the
  newest work and the rest of the grid has no meaningful order. Icon, title, arrow and
  description follow the existing `project-card` pattern exactly, so no CSS changed.
- The description says what the site says about itself, a strategy builder for investors
  who work from earnings reports rather than charts, and states plainly that it is in free
  beta. The site is a beta with its trading and backtesting features still hypothetical,
  and a card that implied a finished product would be wrong within a week.
- This is the first project card on the site that points at a domain other than
  `azqato.github.io`. It keeps `target="_blank" rel="noopener"` like every other outbound
  link on the page, so nothing about the link handling is special.
- Not added to `projects.html`. That page's card array carries a `github` field alongside
  `demo`, and there is no public repository to put in it yet.

### Documentation
- `docs/PRD.md`: the page inventory said the Invests page carries six project cards.

---

## [2.9.6] - 2026-09-08

### Added: `.gitignore` now excludes the local brand folder
A brand and merchandise concept folder was built in the working tree: three planning
documents, 100 concept files under `brand/assets/`, and a generated reading page. It is
deliberately not part of this repository.

- Added `brand/` and `tools/build-brand-page.py` to `.gitignore`. GitHub Pages serves this
  repository publicly from the root, so a committed `brand/` would be readable at
  `azqato.com/brand/`, including supplier notes, priority scores, and an unresolved question
  about the mascot artwork's licensing provenance.
- Ignoring it is the point rather than a side effect. Leaving the folder merely unstaged
  means a single `git add .` publishes it, and this folder will sit in the working tree for
  months. The generator is ignored alongside it because it only builds that folder and would
  be a dangling reference in a fresh clone.
- The trade is that none of it is backed up by git. That is recorded in the folder's own
  review document so it is not discovered the hard way.

### Documentation
- `docs/PRD.md`: the folder tree now lists `brand/` and its contents under the existing
  untracked-and-local-only block, with the reasoning for the exclusion and a note that
  reversing it is a two-line edit.
- `docs/PRD.md`: the `.gitignore` line in the tree said "env-file patterns only", which
  stopped being true with this change.
- No page changed and nothing on the deployed site is affected. Version 2.9.5 stays reserved
  for the roadmap item that gates the visualizer's brightness modulation on the fire.

---

## [2.9.4] - 2026-08-30

### Fixed: the screens pulsed with the music
The v2.9.3 work capped the rate of discrete flashes. It did nothing for this, because this was continuous modulation rather than flashing and no rate limit touches it.

The cause was one deliberate decision applied in the wrong place. `sampleAudio()` smooths asymmetrically on purpose: it jumps 75 percent of the way to a new peak in a single frame so that a kick reads as impact. That is right for anything that moves and wrong for anything that glows, because the same step spread across a large area of the screen is seen as the whole picture pulsing rather than as a hit landing.

- Added two slow luminance envelopes, `envBroad` and `envLow`: the same signal, symmetrically smoothed with roughly a 300 ms time constant and frame-rate corrected. Brightness now reads from these; motion still reads from `favg()`. Fast things stay fast, lit things swell.
- Repointed the four brightness terms at them: panel bloom, the white wash over the main panel, the background radial gradient with its horizon glow, and the stage floor grid.
- Reduced the background's swing (0.45 to 0.30 on the inner stop, 0.20 to 0.14 on the mid stop). It is the largest lit area on the page, so it contributes most to the sensation of the room breathing.

Measured by driving the real `updateEnvelopes()` at simulated refresh rates, worst single-frame change in the panel bloom term:

| Display | Largest one-frame luminance step | `t` advance over 4 s |
|---|---|---|
| 60 Hz | 0.0073 | 239.1 |
| 120 Hz | 0.0037 | 239.6 |
| 144 Hz | 0.0031 | 239.6 |

Before the change a single attack could move that term by roughly 0.22 in one frame, so the worst case is about thirty times smaller. The envelope still reaches the same range (0.001 to 0.601 at every refresh rate), so nothing is flattened; it only gets there smoothly.

### Fixed: second instance of the frame-count defect
`t` was a plain frame counter incremented once per `requestAnimationFrame`, and fourteen call sites multiply it by a coefficient tuned on a 60 Hz panel (`t * 0.018`, `t * 0.05`, and so on). The whole idle animation therefore ran about 2.4 times too fast on a 144 Hz display. `t` now advances in 60 fps-equivalent frames, which keeps every one of those coefficients correct without touching them; the table above shows it advancing identically at all three rates. `glTime` had the same defect via a hardcoded `1 / 60` per frame and is now on the wall clock too.

This is the same class of bug as the beat refractory fixed in v2.9.3. Anything counted in frames is a rate that changes with the viewer's monitor.

### Changed
- Removed the "Drives the visualizer" text under the track. The span is now empty by default and populates only with the serve-over-http warning when the audio path is unavailable. The credit line above it is unchanged.

---

## [2.9.3] - 2026-08-30

### Fixed
- **The stage was flashing above the WCAG 2.3.1 limit on any high-refresh display, and the page's
  own documentation said otherwise.** Every rate in the light rig was a frame count, and
  `requestAnimationFrame` runs at the display's refresh rate, so the 26-frame beat refractory was
  the documented 433 ms only on a 60 Hz panel. Driving the real detector with a worst-case signal
  that clears its threshold on every frame:

  | Display | Before | After | Limit |
  |---|---|---|---|
  | 60 Hz | 2.40 /s | **1.70 /s** | 3 /s |
  | 120 Hz | **4.70 /s** | **1.70 /s** | 3 /s |
  | 144 Hz | **5.60 /s** | **1.70 /s** | 3 /s |

  Every rate is now wall-clock milliseconds, so the rig behaves identically on a phone, a TV and a
  144 Hz monitor, and the refractory is 600 ms rather than 433, which sits under the limit instead
  of on it. The per-frame decays are refresh-rate independent too, so a pulse now lasts as long on a
  gaming monitor as on a TV instead of being half as long and twice as sharp.
- **Screen-mode cycling had the same defect.** `MODE_LEN` was 1800 frames, commented as "~30 s at 60
  fps", which meant the whole centre panel swapped every 15 seconds on a 120 Hz display. Now 30
  seconds on a clock.

### Changed
- **Luminance amplitude cut across the rig, because rate is only half of photosensitivity.** The
  full-width light pump is halved (0.55 to 0.26) with its gradient stops reduced, the white wash
  over the main panel cut to roughly a third (0.30 to 0.12 on the flash term, 0.10 to 0.05 on the
  ambient term), panel bloom's beat and flash contributions roughly halved, and the laser response
  softened (0.35 to 0.22). The rare full-screen drop flash is gated to one per 8 seconds rather than
  one per 5.
- **Impact is carried by motion, not brightness.** The beat-synced panel zoom, the crowd bounce and
  the laser beam count are untouched. They read as impact and cannot flicker.
- **The screen only flashes when the pyro is firing.** Both the full-width light pump and the white
  wash over the main panel are now gated on `fireActive`, which is true while any of the four jets
  is actually burning. A flash with nothing visibly causing it reads as a glitch; the same flash
  with fire behind it reads as the blast throwing light across the room, which is what it was always
  meant to be. The flag is set in `drawFire()`, which runs after the flashes in the frame, so the
  gate uses the previous frame's state. That is 16 ms at 60 fps and is not perceivable. It also
  narrows the photosensitivity exposure further, since the flash can no longer fire during quiet
  passages when the jets are down.
- **The track credit now names the artists.** The tag under the title reads "EOB, Azqato" at all
  times. It previously read "Drives the visualizer", and was overwritten with a serve-over-http
  warning on local file loads, so the artists were never credited on the page at all. The warning
  moved to its own muted line underneath rather than being dropped.

### Notes
- **This closes an accessibility item that had been open since v2.8.7** and was listed in both
  DESIGN.md and the PRD as "the beat flash rate has never been measured". It has now been measured,
  and it failed. The pause control from v2.8.7 was the mitigation; it was never the fix.
- **The earlier documentation was confidently wrong.** DESIGN.md and the PRD both described the rate
  as "at the limit rather than under it" and treated that as the safe case. It was over the limit by
  a wide margin on hardware a large share of visitors own. Both documents are corrected rather than
  quietly updated.
- **The general lesson, which is not specific to this page: a rate expressed in frames is not a
  rate.** Anything that has to respect a per-second limit must be measured against a clock, and on
  more than one refresh rate, or the measurement only describes the machine it was taken on.
- **Verified in headless Edge** (never Chrome), before and after, by driving the page's real
  `updateBeat` at simulated 60, 120 and 144 Hz rather than by reading the constants. The credit line
  and the http note were checked in the rendered DOM in the same pass.

## [2.9.2] - 2026-08-30

### Fixed: the logarithmic band mapping collapsed at the low end
v2.9.1 claimed to give the bass its fair share of the display. It did not, and the claim was wrong rather than merely optimistic.

- Each band is about 10 percent wider than the one below it, but 10 percent of 30 Hz is 3 Hz and one bin at `fftSize` 1024 spans about 47 Hz. The first fourteen bands therefore all rounded to the same bin and moved as a single value. Instrumenting the running page showed it directly: `bandBins` read `1,1,1,1,1,1,1` and bands 0 through 5 all held an identical `0.28`.
- Each band is now forced to advance at least one bin. That makes the low end linear and the top end logarithmic, which is what a mel or bark scale does and what the v2.9.1 change was supposed to deliver. After the fix `bandBins` reads `1,2,3,4,5,6,7,8,9` and the bands hold distinct values.

### Fixed: the page failed invisibly on a local file
- Opened over `file://`, the browser treats the same-folder mp3 as cross-origin, so the page skips Web Audio and runs the synthetic idle animation. That is the correct behaviour and it has been in place since v2.8.10, but nothing on screen said so: the tag under the track still read "Drives the visualizer", and a stage running its idle loop looks exactly like a stage that is ignoring the music. The tag now reads "Serve over http to make the visualizer react" whenever the audio path is unavailable.
- This is the difference between a feature that is broken and a feature that is not connected, and the page was giving no way to tell them apart. On the deployed site, which is HTTPS, the condition never arises.

### Verification note
Instrumenting the live page found both of the above; the v2.9.1 measurement did not, because it tested the detector algorithm against decoded audio rather than the running page. Both are worth doing and neither substitutes for the other: the offline harness proves the maths, the live probe proves the wiring. The kick detector's behaviour in a real browser, with a real audio device, is still unconfirmed. Headless Edge has no audio device and its analyser returns a frozen snapshot, so it cannot answer that question, and the deployed site is now the place to check it.

---

## [2.9.1] - 2026-08-30

### Fixed: the visualizer now reads as reacting to the music
v2.8.10 wired a real analyser and the stage moved with the audio, but it did not look like it was listening: the kick did not land and a drum hit was not distinguishable from a pad. Four causes, all real, all now fixed.

- **Two low-pass filters in series.** `analyser.smoothingTimeConstant` was 0.8 and `freq()` smoothed again at `0.72 / 0.28`. A kick is a transient, and each filter rounded off its leading edge; together they removed it. The analyser now smooths at 0.35 and `freq()` smooths asymmetrically instead: it jumps to a new peak at `0.25 / 0.75` and falls back at `0.82 / 0.18`. Attack survives, decay stays smooth, and the leading edge of a hit is the part the eye reads as impact.
- **Linear band mapping.** 64 bands spread evenly across the spectrum put the entire kick region inside band 0 while sixty-odd bands displayed hiss. Bands are now spaced logarithmically from 30 Hz to 16 kHz, built once from the actual sample rate, which is how hearing divides pitch and therefore how the display has to divide it.
- **Resolution too coarse to see a kick.** `fftSize` was 256, about 190 Hz per bin, wider than the whole kick band. Now 1024. Deliberately not 2048: frequency resolution trades against time resolution, and a 2048 window spans 46 ms, longer than a frame at 60 fps, which smears the transients this change exists to preserve.
- **Averaging within a band.** Band level is now the peak of its bins rather than the mean, so one loud bin is not averaged away by quiet neighbours.

### Added: kick detection
- Added a second analyser dedicated to finding kicks: `fftSize` 2048 for about 23 Hz per bin, `smoothingTimeConstant` 0, tapping the same source but not connected to the output. It takes the opposite resolution trade from the general analyser because it needs frequency precision rather than time precision.
- Detection is by onset, not by level. On a modern master the bass sits near the ceiling almost continuously, so "is the bass loud" is true nearly always and fires on nothing. A kick is instead identified by its attack: a sharp rise in 30-150 Hz energy over the last few frames, with a threshold that adapts to the track's own recent behaviour so quiet passages still register and loud ones do not fire continuously. Ported from `feature/native-audio-player`, where the constants were tuned with `ffmpeg` against a known tempo.
- `beatPulse` now drives the screen zoom, the crowd bounce, the laser intensity, and the WebGL clock, so a hit moves several independent things at once. That is what reads as reaction; a single brightness change does not.
- Added the loud-moment gate from the same branch: a full brightness flash fires only when loudness is a genuine statistical outlier against a slowly adapting baseline, coincides with an actual kick, and has not fired in the last 5 seconds. It reads as a drop rather than as every beat.
- Replaced the old `drawBeatFlash` trigger, which was `favg(0, 5) >= 0.76`. On a loud master that test is either true continuously or never true, and both look identical to no reaction at all.

### Verified
Measured offline rather than judged by eye. The mp3 was decoded in the browser and the detector run over a 2048-point FFT at a 60 Hz hop, reproducing exactly what the page sees per frame:

| Measure | Result |
|---------|--------|
| Hits detected | 92 over 44.5 s |
| Rate | 124.0 per minute |
| Median interval | 0.480 s, implying 125.0 BPM |
| Intervals in 380-620 ms | 94 percent |
| Interval p10 / p90 | 0.430 s / 0.560 s |

124 BPM against the 124-128 BPM the branch measured independently for its own test track. The detector is locking to the real beat, not firing on noise.

### Accessibility
- **WCAG 2.3.1 measured, not assumed.** The 26-frame refractory caps beat-driven events at 2.3 per second in principle, and the measurement found a maximum of 3 in any one-second window, which is at the limit rather than under it. So the full-width light pump is scaled to 0.55 on the audio path and the impact is carried by the screen zoom, the crowd, and the lasers, which are motion rather than luminance. The one true full-screen brightness flash remains gated to at most one per 5 seconds. There is a comment in the source saying not to raise the pump; it is load-bearing.
- The reduced-motion behaviour from v2.8.7 is unchanged: the loop still starts paused when the system asks for reduced motion, and the pause control still stops everything.

### Performance
- `freq()` called `getByteFrequencyData` on every band, so the full spectrum was refetched 64 times per frame and more once `favg()` was counted. Sampling now happens once per frame in `sampleAudio()` and `freq()` only reads the result.

### Documentation
- Closed milestone v2.9.1 in `docs/PRD.md` and recorded the measured figures, so the next person tuning this has a baseline to compare against rather than an opinion.
- Updated the signal sections of `docs/PRD.md` and `docs/DESIGN.md`, and removed the DESIGN.md warning against tuning visuals to the old signal, which no longer applies.
- `music.html` is now 110 KB, still the one acknowledged exception to the 50 KB page budget.

---

## [2.8.10] - 2026-08-29

### Added: the visualizer now reacts to real audio
- Added a native track player to the top of the `music.html` stage console: one same-origin file (`audio/womanchild-azqato-remix.mp3`, 6.1 MB, 4:46), with a play/pause button, title, elapsed and total time, and a draggable scrub bar. The two Mixcloud embeds and all three platform links are untouched and sit below it.
- Wired the track through a Web Audio `AnalyserNode` (fftSize 256, smoothing 0.8). While it plays, `freq()` reads real frequency data and the lasers, fire columns, screen pulses, crowd, and animated favicon follow the music. This is the first time anything on the site has responded to audio.
- Kept the synthetic three-sine signal as the fallback, and it is a fallback rather than a failure state. It runs when the track is paused, when it has never been started, and when a Mixcloud embed is playing. A paused element reads as silence, so falling through to the analyser would flatten the stage rather than idle it. Both branches share the same `0.72 / 0.28` smoothing, so the handover at play and pause is continuous rather than a jump.

### Technical notes
- Band `i` reads analyser bin `floor((i / 64) * bins * 0.8)`. The top fifth of the spectrum is skipped because it is nearly always empty and would otherwise waste a fifth of the bands on silence.
- Raw amplitudes are raised to the power 1.6 before smoothing. Without that curve most tracks sit inside a narrow loudness band and the stage reads as uniformly bright rather than dynamic. The exponent is ported from `feature/native-audio-player`, where it was tuned against a real track.
- The `AudioContext` is created lazily inside the play button's click handler, not at load. Browsers refuse to start one outside a user gesture, and creating it up front would leave a suspended context that never resumes.
- `createMediaElementSource` is called exactly once and guarded by an `audioWired` flag, because a second call on the same element throws. If it does throw, the error is logged and `analyser` is reset to null, which degrades the page to the synthetic signal instead of breaking playback.
- `preload="metadata"` rather than `none`. With `none` the duration stayed at `0:00` until first play, so the scrub bar had no range to show.
- Removed the `analyser` and `freqData` dead declarations, which had been declared and never assigned since the visualizer was written. They are now real. The Known Technical Debt row and the deferred cleanup item that tracked them are both gone.

### Known limitation
- **The stage is driven by the audio but does not yet read as reacting to it.** Confirmed on the first real listen: the kick does not land, and you cannot tell a drum hit from a pad by watching. Scoped as milestone v2.9.1 with six hypotheses to measure before changing anything, chief among them that the analyser's 0.8 smoothing and `freq()`'s own `0.72 / 0.28` are two low-pass filters in series and a kick is a transient. The onset-based kick detector already sitting on `feature/native-audio-player` exists because a raw analyser level does not give you a kick, and is pulled forward into that milestone.

### Fixed
- Skip Web Audio entirely when the page is opened over `file://`. The browser treats a same-folder mp3 as cross-origin there, so `createMediaElementSource` succeeds, reroutes the element, and outputs silence with no error thrown. The track appeared to play with the timer running and no sound. The page now checks `location.protocol` and leaves the element unrouted on a local file, so playback is audible and the stage runs synthetic. Serve over http to get the real path.

### Documentation
- Rewrote the "The visualizer is not audio-reactive" section of `docs/DESIGN.md` and the "signal driving the visualizer" section of `docs/PRD.md`. Both were correct when written and are now false. The replacement text is explicit about which of the three playback situations gets which signal, because the interesting case is the one that has not changed: a visitor playing a Mixcloud mix still sees choreography, not reaction, and no browser will ever let that page read cross-origin iframe audio.
- Added F19 (Native Track Player) to the feature list, updated F14 and F15, and added `audio/` to the folder tree and the public surface table.
- Marked steps 2 through 4 of milestone v2.9.0 as done and restated what the milestone is now: replacing the Mixcloud embeds, which is gated on the remaining audio files rather than on code. Five features are still unmerged on `feature/native-audio-player`: the `<video>` element, the onset-based kick detector, the beat-synced screen pulse, the loud-moment flash, and the Video screen mode. The beat flash needs measuring against WCAG 2.3.1 before it can ship.
- Recorded the sizing answer the milestone was waiting on: 6.1 MB for a 4:46 track at 192 kbps, so a handful of tracks fits in the repository and GitHub Pages serves them like any other asset. No object storage needed.
- Updated the `music.html` page weight from 91 KB to 99 KB everywhere it appears in the constraints, success criteria, technical debt, tenets, and working-practice sections. It remains the one acknowledged exception to the 50 KB budget.
- Noted that the zero-external-request caveat did **not** move. The player was added beside the embeds, not in place of them, so every "except `music.html`" qualifier still stands.

---


## [2.8.9] - 2026-08-29

### Fixed: dead demo link on the Leveraged Strategies card
- Fixed the Leveraged Strategies card in `projects.html`, which pointed its demo link at `azqato.github.io/leveraged-strategies/`. That URL returns a hard 404 and has since the project was renamed. Both the `demo` and `github` fields now point at `leverage`.
- Verified against the live web rather than assumed: `/leverage/` serves the page titled "Leveraged Strategies", `/leveraged-strategies/` returns 404, and the GitHub API resolves `Azqato/leveraged-strategies` to `Azqato/leverage`. GitHub redirects renamed repositories, which is why the `github` link still worked, but GitHub Pages does not redirect Pages URLs, which is why the demo link did not. Patch note 2.6.12 moved `invests.html` to the new URL and missed `projects.html`.
- No compatibility entry was added at the old path, because no repository serves it and there is nowhere to put one.

### Removed
- Removed `wrangler.jsonc`. It described a complete Cloudflare Workers deploy target, arrived on 2026-07-09 via the only pull request in this repository's history (a Cloudflare autoconfiguration integration), and was never used for a real deploy. An untested deploy path implies a safety net nobody has checked. The site is plain files and moves to any static host with no configuration, so nothing was lost.
- Removed the wrangler-specific patterns from `.gitignore` (`.wrangler`, `.dev.vars*`) along with the config they belonged to. The defensive `.env*` exclusion stays.
- Removed `.vscode/recentfedsummary.MD`, a personal summary of a finance video that was tracked in git, unrelated to the site, and the only remaining source of em-dash violations in the repository. Setting aside the exempt lines where a rule names the character it prohibits, the project is now fully compliant with its own writing policy.

### Changed
- Milestone v2.9.0 is no longer blocked. It was waiting on somewhere to host audio; the owner is supplying standalone audio files to be played directly on the page. The milestone grew in scope as a result: it now replaces the two Mixcloud iframes rather than adding a player beside them, and it is the next substantial piece of work on the site.
- Rewrote the Current Phase section of `docs/PRD.md`, which described the project as being in maintenance with a paused branch and a half-finished milestone. None of that is true any more. It now names v2.9.0 as next and lists the six remaining defect items with their sizes.

### Documentation
- Closed open questions 1 through 5 in `docs/PRD.md`. Each keeps its original text struck through with the answer beside it, per the documentation process, rather than being deleted. Questions 6, 7, and 8 remain, and question 8 is partly closed by v2.8.7.
- Recorded a standing rule in `docs/PRD.md` (Never Do These) and `docs/DESIGN.md` (Image Assets): **nothing in `img/` is ever deleted unless the owner asks for that file by name.** Unreferenced is the normal state of that folder, which is a working asset library rather than build output. The removal policy's plain internal delete does not apply there, and future audits should stop raising it. The corresponding Known Technical Debt row and deferred item were reworded from open questions into settled decisions.
- Updated the three Documentation Versus Reality rows that these answers resolve (15, 16, and 19) with what was decided and why.
- Removed every reference to Cloudflare Workers and `wrangler.jsonc` from the tech stack, folder tree, environments table, alternative hosts table, public surface table, security section, and internal FAQ. The Environments discrepancy note is now marked resolved instead of open: there is again exactly one environment, without qualification.
- Added v2.8.9 to the milestone table and updated the v2.9.0 row from blocked to ready.

---

## [2.8.8] - 2026-08-29

### Added: `tools/build-nav.py`, the nav now has one source
- Added `tools/build-nav.py`, which holds the navigation bar once and stamps it into every page. Running it rewrites the block between the `<!-- NAV -->` marker and the closing `</nav>` tag in all 12 HTML files and sets `class="active"` from each file's own name.
- Added a `--check` mode that reports any page whose nav has drifted, writes nothing, and exits non-zero. Running the script with no nav change prints "nav is up to date in every page", which doubles as a consistency check across all 12 pages.
- No markers were added to any page. Both `<!-- NAV -->` and `</nav>` already appeared exactly once per file, which is what makes the range unambiguous without extra scaffolding.
- The script preserves each file's own line endings. `music.html` is CRLF while every other page is LF, and rewriting that would have produced a whole-file diff instead of a nav diff.
- The two pages that are not in the nav (`accounts.html`, `privacy-policy.html`) need no special case: no entry matches their filename, so they receive the nav with no active item, which is what they had before.

### Changed
- **The deployed site is byte-for-byte unchanged by this release.** The script was verified against the existing pages before anything was committed: it reproduces all 12 navs exactly, producing an empty `git diff`. It was then verified to repair drift, by deliberately removing the Music link from `accounts.html` and corrupting a link label in `music.html`, running the script, and confirming both files returned to their committed state with line endings intact.
- Milestone v2.7.0 is complete. Both outstanding items (shared nav extraction and active-state detection) are closed by this change, roughly seven weeks after the CSS half shipped.

### Documentation
- Recorded in `docs/PRD.md` that the nav extraction shipped by a third method, not either of the two the milestone originally proposed. JS injection was rejected because it removes the nav entirely without JavaScript, trading away the site's graceful degradation to fix a maintenance problem that had never once produced a broken page. A real build step was rejected because it puts a toolchain between the source and the deployed artifact. A stamp script whose output is committed has neither property: the repository still contains complete deployable HTML, nothing runs at request time, and deleting the script would cost only the convenience.
- Rewrote the Build section of the Runbook to state that there is still no build step, and to explain why the stamp script is not one.
- Updated the Tenet 3 discussion, which previously used the nav duplication as its worked example of simplicity winning on merit. It now records what changed that verdict.
- Updated Known Technical Debt: the nav markup row is closed. What remains is the roughly 20 line toggle script, still duplicated verbatim in all 12 pages, and the fact that nothing runs `--check` automatically. Wiring it into the `pre-commit` hook alongside the em-dash guard is the obvious next step and is recorded as such.
- Updated the Working Practice never-do list, the common errors table, the fragile areas table, maintenance rule 4, the verification steps, the prerequisites table (Python 3 is now needed to change the nav, standard library only), the folder tree, the public surface table, and feature F3.
- Added a note to the Navigation Bar section of `docs/DESIGN.md` that the markup is generated and must not be hand-edited.
- Added v2.7.0, v2.8.7, and v2.8.8 rows to the milestone table.

---

## [2.8.7] - 2026-08-29

### Added: reduced motion support sitewide and a pause control on `music.html`
- Added a `@media (prefers-reduced-motion: reduce)` block to `styles.css` that collapses every animation and transition to `0.01ms` and forces `transform: none` on hover. The card hover lift is suppressed; the border and background color changes that carry the same affordance are untouched, so no interactive element loses its cue.
- Added a play/pause control to the mode-button row on `music.html` (`.motion-btn`, styled in `--accent` rather than the `--purple` used by the mode pills so it reads as a control over the whole scene). Every visitor can now stop the animation, which nothing on the page allowed before.
- The `music.html` visualizer now reads `prefers-reduced-motion` in JavaScript and decides whether to start its render loop. A CSS media query cannot stop a `requestAnimationFrame` loop, so this had to be handled in the script rather than the stylesheet.
- One frame is always painted before the loop is gated, so a paused stage shows the full scene rather than an empty canvas. Verified in Microsoft Edge with `--force-prefers-reduced-motion`: the button reads "Play" and the stage holds a complete still frame.

### Changed
- Refactored the `music.html` main loop: `draw()` no longer schedules itself. A new `loop()` drives the frames and a new `setPlaying()` starts and cancels it, updating the button label, `aria-pressed`, and `aria-label` together.
- Clicking a mode button while paused now redraws a single frame, so the picked mode is visible without starting the animation.
- The `resize` handler now redraws a single frame while paused, so the still frame stays correct after `build()` recomputes the stage layout.

### Documentation
- Resolved Open Question 8 in `docs/PRD.md`. Three candidates were built into a local harness and compared: freeze on first frame, start paused with a control, and a calm mode keeping slow motion without strobes or lasers. The control won because it is the only one of the three that also satisfies WCAG 2.2.2 (Pause Stop Hide, Level A) for the majority of visitors who never set a reduced-motion preference. The question is kept with its original text struck through rather than deleted, per the documentation process.
- Added feature F18 to `docs/PRD.md` and updated F14 to mention the control.
- Checked off the reduced-motion item in the v2.7.0 milestone in `docs/PRD.md`. That milestone now has only the nav extraction and its active-state detection outstanding.
- Replaced the `prefers-reduced-motion` row in Known Technical Debt with the tab-hidden render loop, which is the part that remains unsolved and is a battery concern rather than an accessibility one.
- Added a "Reduced motion" subsection to the Animation and Motion section of `docs/DESIGN.md` documenting both layers, the on-load behavior table, and the WCAG reasoning.
- Rewrote the accessibility gaps list in `docs/DESIGN.md`: the two items this release closed were removed and marked as closed, and two gaps that had been ranked below them (unmeasured beat flash rate against WCAG 2.3.1, and browser-default focus styles) are now named explicitly.

---

## [2.8.6] - 2026-08-29

### Changed: RouteNote referral code surfaced on the badge
- Changed the RouteNote promo badge on `support.html` from "Free Distribution" to "Referral Code: 2fcd201c", so the code is visible at a glance and visitors remember to enter it at sign-up. Referral credit is only granted when the code is entered.
- Moved the free-distribution message into the card description, which now reads "Free music distribution to Spotify, Apple Music, and every major platform. Enter referral code 2fcd201c when you sign up."
- Updated the RouteNote row of the active affiliate cards table in `docs/PRD.md` to match the new badge text.

---

## [2.8.5] - 2026-08-24

### Added
- Added a full "Documentation Versus Reality" table to `docs/PRD.md` recording all 20 discrepancies found between the documentation and the source, with the source trusted and the reasoning for each.
- Added a "Risks and Open Questions" section to `docs/PRD.md` covering what was not fully understood, fragile areas of the codebase, changes that are dangerous without more context, work in progress at audit time, and 8 numbered open questions for the author to resolve.
- Added a "Working Practice" section to `docs/PRD.md`: pre-edit checks, a "which document to read first" table, a never-do list, an 8-step verification procedure, and post-change documentation sync steps.
- Added a "Conventions" section to `docs/PRD.md` derived from the code itself, covering naming, formatting, organization, comments, error handling, and commit message and branching practice, naming the dominant form wherever the codebase is inconsistent.
- Added a "Browser Testing" section to `docs/PRD.md` adopting Microsoft Edge as the browser for any automated or headless testing, with resolved binary paths, and recording `test-local-audio.bat` as a pre-existing Chrome-driving deviation.
- Added a "Deprecation and Removal" section to `docs/PRD.md` defining the deploy boundary for this project, the HTML meta-refresh redirect mechanism, a full public surface table, and a retired items log.
- Added a "Press Release" section to `docs/PRD.md`, which the previous "Press Release and FAQ" block referenced but never actually contained.
- Added Retention metrics to `docs/PRD.md`, previously the one missing metrics category, together with an explicit statement that the site cannot measure retention and the three proxies available instead.
- Added a "How an audit is run" procedure to the Documentation Process section of `docs/PRD.md`.
- Added feature F13 (Codes page), F14 (music stage visualizer), F15 (stage console), F16 (shared stylesheet), and F17 (writing-style guard) to the `docs/PRD.md` feature list.
- Added a sixth product tenet, "Say What Is Actually True", covering site copy, promo badges, and documentation equally.
- Added a full `music.html` Visual System section to `docs/DESIGN.md`: scene structure, draw order, screen layout, DJ booth, reflection, bloom, scanlines, the 10-mode table with visible and hidden state, and the animated favicon.
- Added an image asset table to `docs/DESIGN.md` listing all 15 files in `img/` with sizes and referencing pages.
- Added six "Rules for Staying Consistent" to `docs/DESIGN.md`.
- Expanded the external FAQ in `docs/PRD.md` from 8 to 20 questions.

### Changed
- Rewrote `README.md` for a general reader: name, description, live link, a 12-row table of what each page offers in plain language, who it is for, current status, and links to `/docs`. Removed the clone and serve commands, the file overview, the tech stack table, the version number, and the "Adding a Project" and "Adding a Discord Server" instructions. All of that content was preserved in the `docs/PRD.md` Operational Runbook and Data Models sections rather than deleted.
- Rewrote `docs/DESIGN.md` around the two-layer CSS model (shared `styles.css` tokens versus page-scoped `:root` overrides), with separate token tables for each layer, the inline `rgba()` brand colors, and roughly 15 documented component patterns.
- Rewrote `docs/PRD.md` in full, merging every existing section rather than replacing it. Original intent, rationale, and wording were kept wherever the code agreed with them; where the code disagreed, both readings are recorded.
- Documented `wrangler.jsonc` as a configured but unused Cloudflare Workers deploy target in the tech stack and Environments sections, alongside the existing "only one environment" statement.
- Restated the under-50 KB page weight constraint as met on 11 of 12 pages, naming `music.html` at 91 KB as a deliberate and explained exception rather than quietly restating the target.
- Reprioritized the accessibility section of `docs/DESIGN.md`, promoting the absence of a reduced-motion path on `music.html` from a minor gap to a genuine problem.

### Fixed
- Corrected the navigation bar description in `README.md` and `docs/DESIGN.md` to the 10 current items (Home, About, Discord, Invests, Codes, Music, Links, Projects, YouTube, Support). Both had described a nav with external Tools and GitHub links that was removed in v2.6.x, and both omitted Music, added in v2.8.0.
- Added `codes.html`, which was live and in the nav of all 12 pages but appeared nowhere in `README.md` or `docs/PRD.md`, to the site structure table, folder tree, public surface list, and feature list.
- Corrected the page count from 11 to 12 in every location, and dropped the "self-contained" description of the pages, which stopped being accurate when `styles.css` was extracted in v2.7.0.
- Corrected the clone URL in the runbook from `github.com/Azqato/Azqato.git` to the actual remote, `github.com/Azqato/azqato.github.io.git`.
- Narrowed the "zero external requests" claim, which was true of 11 pages but not of `music.html` (two Mixcloud iframes on every load) or `projects.html` (one cross-site favicon), everywhere it appeared in the performance, privacy, and security sections.
- Corrected the affiliate card data model in `docs/PRD.md` and `docs/DESIGN.md` to the real class names (`.affiliate-logo`, `.affiliate-promo`, `.affiliate-link-btn`, on an anchor element). Three of the four previously documented class names did not exist in `support.html`.
- Removed the `activeTag` state variable from the `docs/PRD.md` state management table. No such variable exists; filter state lives in the DOM as `.active` and `data-hidden`.
- Corrected the mobile breakpoint in `docs/DESIGN.md` from "< 600px: nav links hidden" to the actual split: the nav collapses into a toggle at 860 px and content padding tightens at 600 px. The superseded claim is kept and marked rather than erased.
- Corrected the image usage claims in `docs/DESIGN.md`: `index.html` contains no image element at all, `music.html` lists no playlists, and 10 of the 15 files in `img/` are referenced by nothing, including a 1.9 MB GIF that appeared in no documentation.
- Corrected feature F4, which claimed the landing page hero includes a profile photo. It has interest pills and two CTA buttons.
- Corrected feature F11, which claimed the lion favicon is identical across all 12 pages. `music.html` replaces it at runtime every third frame.
- Documented that the `music.html` visualizer is not audio-reactive. `analyser` and `freqData` are declared and never assigned, so every visual is procedural. This was stated nowhere before and is now recorded in `docs/DESIGN.md`, the data flow section, F14, and Known Technical Debt.
- Corrected the Known Technical Debt entry describing the nav as duplicated across "all 11 HTML files" to 12.

### Removed
- Removed nothing from the codebase. This audit was documentation only; no HTML, CSS, JavaScript, or image file was edited, renamed, or deleted.

### Writing style sweep
- Swept every text file in the repository for both prohibited em-dash forms independently (the literal character and the HTML entity), including files inside dot-directories that a plain recursive glob skips.
- Found **zero violations** in any HTML file, in `styles.css`, and in all documentation prose.
- Found 4 occurrences in `docs/PRD.md` and `docs/PATCHNOTES.md`, all inside backtick code spans where the rule names or quotes the character it prohibits. All are exempt under the existing policy and were left in place.
- Found 2 occurrences in `.githooks/pre-commit`, where the guard defines the character it blocks. Exempt and left in place.
- Found 13 lines with real violations in `.vscode/recentfedsummary.MD`, a personal note unrelated to the site that is tracked in git. Left untouched: it is outside this audit's write scope and outside the project's own documentation. Recorded as Open Question 1 in `docs/PRD.md`.

---

## [2.8.4] - 2026-08-24

### Added: RouteNote affiliate card on `support.html`
- Added a RouteNote referral card to the affiliate partners grid on `support.html`, placed after Twitch Prime. Links to `routenote.com/rn/referral/2fcd201c` (referral code `2fcd201c`) with a "Free Distribution" promo badge and an orange-tinted logo tile.
- Updated the affiliate references in `docs/PRD.md`: feature F7, the assumptions list, the affiliate link accuracy criterion (now 7 links), the active affiliate cards line, and the third-party integrations table.

---

## [2.9.0] - 2026-07-16 (branch only, not deployed)

### Deferred: native track player, kick detection, and video screen mode
- Built and validated a native in-page audio player for `music.html`: a Web Audio-routed `<video>` element (two test tracks), a scrub-bar player UI, an onset-based kick detector tuned against a real track with `ffmpeg`, a beat-synced screen pulse, a rarity-gated loud-moment flash, audio-scaled laser beam counts, and a "Video" screen mode that draws the playing track's own frames onto the stage screens.
- Not merged to `main`: the player currently points at large local test files (multiple GB) that cannot be committed to this repo (GitHub rejects pushes over 100MB via normal git, and even Git LFS caps at 2GB/file on GitHub.com, well under these files' size). A live "Play" button pointing at nothing would be broken for real visitors.
- Full implementation kept on branch `feature/native-audio-player` (pushed to GitHub) so the work isn't lost. To resume: host a real track externally (object storage plus CDN, or a video host that serves a direct file URL) and point the `<video src>` at it, then merge the branch. See Known Technical Debt below.

---

## [2.8.3] - 2026-07-16

### Added: stage console panel on `music.html`
- Combined the two Mixcloud embeds and the three platform links (Last.fm, Mixcloud, YouTube) into a single `.stage-console` panel docked over the center visualizer screen. The panel is `position: fixed` and independently scrollable (`overflow-y: auto`), so it stays pinned in place and scrolls on its own without affecting the main page scroll. Styled with a dark glass background and a themed thin scrollbar to read as content displayed on the screen rather than a floating card.
- Removed the old in-flow `.section` block, `.mixcloud-embed`, and `.platform-grid` markup and styles that this replaces.

### Changed: visualizer mode buttons on `music.html`
- Hidden the Bars, Volumetric, Origami, Ghost, and Noise mode buttons; only Stars, Vortex, Squares, Tunnel, and Fence remain visible. The modes themselves are unchanged in code.
- The random mode auto-cycle now only picks from the five visible modes (Stars, Vortex, Squares, Tunnel, Fence), so the hidden modes no longer appear during automatic cycling either.

### Documentation
- Added a full mobile audit of `music.html` to `docs/PRD.md`'s Explicitly Deferred Items as a future action item, since the visualizer canvas and fixed stage console were tuned for desktop viewports first.

---

## [2.8.2] - 2026-07-11

### Fixed: Mixcloud embed width on `music.html`
- The two Mixcloud player iframes had a `width="660px"` HTML attribute that was silently overridden by `.mixcloud-embed iframe { width: 100% }`, so the embeds actually stretched to the full `.section` width (up to ~1036px) instead of the intended 660px.
- Gave `.mixcloud-embed` a `max-width` of `calc(3 * 220px + 2 * 1rem)` (692px) and centered it, so the embeds now match the width of the three-card platform-grid row (Last.fm, Mixcloud, YouTube) directly below them.

---

## [2.8.1] - 2026-07-11

### Fixed: floor reflection ghosting near the DJ booth
- The panoramic screens' bloom effect (an upscaled, offset redraw of already-rendered panel pixels) was being mirrored onto the glossy floor by `drawReflection()`, and that mirrored band overlapped the DJ booth's position, making the booth appear doubled and blurry. Clipped a hole in the reflection draw over the booth's footprint so the reflection no longer washes over it.

### Changed: DJ booth redesign
- Replaced the flat, single `fillRect` booth panel with an actual structure: a front fascia (angled toward the crowd), raked side cheeks, and a solid base, all merged into one continuous silhouette running from the top deck down to the floor. The old design ended in a thin, near-invisible riser that read as an abrupt cutoff; the new one is grounded.
- Moved the "AZQATO" wordmark off a fixed spot at the top of the stage truss (the old `drawULogo`, now removed) and onto the booth's fascia, keeping the same gold gradient and glow treatment. Sizing now accounts for `letterSpacing` and fits both the width and height of the fascia's text box, fixing an overflow bug where the letters bled past the panel's edges.
- Added a top deck with a back rail (visible thickness along the rear edge instead of a flat cutoff), two CDJ silhouettes with small static jog-wheel accents (previously oversized glowing circles), and a plain static mixer panel between them, replacing the animated audio-reactive LED grid that used to sit there.
- Removed the center laser-triangle overlay (`drawTriangle`) that floated above the booth.
- Enlarged the booth overall and added top margin above the wordmark so it isn't crowded by the deck.

---

## [2.8.0] - 2026-07-10

### Changed: `music.html` visualizer overhaul

**Screen layout**
- Replaced the 5-screen Brooklyn Mirage layout (center + 2 wings + 2 outer panels) with a cleaner 3-screen layout: one wide center screen (42% canvas width) and two independent side panels (22% each) with a visible gap between center and sides. Side panels are flat (no rotation).
- `drawOuterScreen` removed entirely; only `drawWingScreen` remains for the side panels.

**WebGL shader modes** (added 7 new GPU visualizers, modes 5-9 plus two added mid-session):
- **Origami** (mode 5, `@XorDev`): soft-shaded folded-paper layers with bounce lighting and palette color cycling.
- **Tunnel** (mode 6, CC0): star-shaped SDF tunnel with per-layer rotation, postprocess vignette and contrast.
- **Ghost** (mode 7, seb chevrel 2019): ray-marched ghost dancers scene with SDF bodies, AO, soft shadows, and palette coloring; reuses the volumetric noise texture as `iChannel0`.
- **Fence** (mode 8, CC0): layered hexagonal grid animation with animated palette and camera drift.
- **Noise** (mode 9, Inigo Quilez MIT): value noise with fractal octaves, alternates between Cartesian and polar projection every 3 seconds.
- Previously added: **Vortex** (mode 3, CC-BY-NC-SA-4.0 @WorkingClassHacker) and **Squares** (mode 4, CC0).

**Mode system**
- Mode count increased from 5 to 10 (modes 0–9); `% 10` cycling.
- Auto-advance now picks a **random** mode on each 30-second tick (no immediate repeat) instead of cycling sequentially.
- Default mode on page load changed from Bars (0) to **Squares** (4).
- Removed Julia, Plasma, Mandelbrot, Newton, and Burning Ship canvas fractal modes (and their dead `computeFractal_REMOVED` code block).

**UI / text**
- Hero badge changed from "🎵 Now playing" to "🎵 Azqato's Music".
- H1 heading ("Azqato's Music") made visually hidden (1×1 px clip) while remaining in the DOM for SEO and screen readers.
- Canvas logo text changed from "AZ" to "AZQATO"; vertical position tuned.
- Footer "Built by Azqato." background/blur pill now wraps tightly around the text instead of spanning the full footer width.
- Mode buttons updated to match new 10-mode list: Bars, Volumetric, Stars, Vortex, Squares, Origami, Tunnel, Ghost, Fence, Noise.

---

## [2.7.0] - 2026-07-09

### Changed
- **Roadmap milestone: Code Extraction + Shared Assets (first half).** Extracted the CSS that was byte-identical across all 12 pages into a single external `styles.css`: the 12 shared design tokens (`:root`), the universal reset, the scrollbar-gutter fix, `body`, the entire nav component (`nav`, `.nav-inner`, `.nav-logo`, `.nav-toggle`, `.nav-links` and its states), the nav's 860px collapse breakpoint, and `footer`. Every page now links `<link rel="stylesheet" href="styles.css" />` instead of repeating roughly 100 lines of identical CSS in its own inline `<style>` block.
- Page-specific `:root` overrides (`--discord`/`--discord-hover` on `discord.html`/`index.html`/`invests.html`, `--spotify` on `music.html`, `--coffee`/`--coffee-hover` on `support.html`) remain in each page's own inline `<style>` block, since CSS custom properties cascade additively across multiple `:root` rules; only the 12 common tokens moved to `styles.css`.
- Renumbered six patch-note entries that had drifted into the `2.7.x` range (favicon change, nav logo scrollbar-gutter fix, Leveraged Strategies URL update, `invests.html` `html{}` rule merge, `invests.html`/`codes.html`/`youtube.html`/`discord.html`/`about.html`/`links.html` layout pass, VIX Strategy URL casing) down to `2.6.11`-`2.6.16`, since none of them were the actual "Code Extraction + Shared Assets" roadmap milestone and the true `v2.7.0` needed to be free for this entry.

### Deferred
- Extracting the shared `<nav>` markup and its toggle `<script>` out of the 12 HTML files themselves is intentionally not done here: it requires deciding between a JS-injected nav (no build step, but the nav is briefly absent until JS runs) and a minimal build step (nav stays in static HTML, but the project currently has none). The `styles.css` extraction above has no such trade-off and was safe to do immediately.
- Auto-detecting the active nav link via `window.location.pathname` and adding `@media (prefers-reduced-motion: reduce)` remain outstanding from the same roadmap milestone.

---

## [1.0.0] - 2026-06-06

### Added
- Initial release of the portfolio site.
- Self-contained `index.html` with zero external dependencies.
- Project card grid with icon, name, description, tags, GitHub link, optional demo link, star count, and last-updated fields.
- Tag filter bar, auto-generated from the `PROJECTS` array; filters the grid in real time.
- Project count label that updates to reflect the active filter.
- Sticky nav bar with logo and GitHub profile link; collapses nav links on mobile.
- Hero section with status badge, headline, bio, and two CTA buttons.
- Language-specific tag colour classes: `lang-js`, `lang-ts`, `lang-py`, `lang-cs`, `lang-html`, `lang-css`, `lang-go`, `lang-rust`, `lang-java`.
- Hover animations on cards: lift, border highlight, top-edge gradient.
- Fully responsive layout (320 px → 2560 px).
- CSS custom properties for easy retheme via `:root` variables.
- `README.md` with setup and deployment instructions.
- `PRD.md` documenting requirements, user stories, and design tokens.
- `PATCHNOTES.md` (this file).

---

## [1.1.0] - 2026-06-06

### Added
- Three live projects populated from their READMEs: Net Worth Tracker, VIX Strategy, and Lantern.

### Changed
- Project card title now links to the live GitHub Pages site (`demo` URL) instead of the GitHub repository, making the primary action open the running app.
- GitHub repository link retained as a separate icon button on each card alongside the live-site (↗) button.

---

## [1.2.0] - 2026-06-06

### Changed
- Project tags simplified to category-only labels: Net Worth Tracker and VIX Strategy tagged `Finance`; Lantern tagged `Social`. Removed tech-stack tags (JavaScript, Chart.js, Dashboard, Privacy, Tailwind CSS) from the filter bar.
- Nav "Projects" link replaced with "Index", pointing to `https://azqato.github.io/`.
- Removed "Browse Projects" secondary CTA button from the hero section.

---

## [1.2.1] - 2026-06-06

### Changed
- README title updated from "Azqato Portfolio" to "Azqato's Portfolio".
- Added live site link (`https://azqato.github.io/`) directly below the README title.

---

## [1.2.2] - 2026-06-06

### Added
- ⚡ emoji favicon added to all pages via inline SVG data URI with no external image file required.

---

## [1.3.0] - 2026-06-07

### Added
- `support.html`: dedicated support page with a personal pitch, Buy Me a Coffee CTA (buymeacoffee.com/azqato), and an affiliate partners grid (6 placeholder cards: Tesla, Robinhood, M1 Finance, Webull, Coinbase, Public).
- "Support" nav link added to `index.html` pointing to `support.html`.
- "Support" nav link on `support.html` highlights as active to signal current page.
- Affiliate card design: square logo area, promo badge, description, and CTA button.
- Pitch card on support page with gradient top border, avatar, bio, and signature pulled from the buymeacoffee About section.

---

## [1.3.1] - 2026-06-07

### Changed
- Buy Me a Coffee CTA section moved above the About Azqato pitch card so the support ask is the first thing visitors see after the hero.
- CTA paragraph replaced with the full buymeacoffee disclaimer: investment intent statement and fund-use caveat.
- Removed the "Opens buymeacoffee.com/azqato, One-time or monthly, 100% goes to the journey" sub-line from the CTA.
- Removed duplicate investment paragraph from the pitch card body since it now lives in the CTA above.
- All em dashes replaced with commas across `support.html` for improved readability.

---

## [1.3.2] - 2026-06-07

### Changed
- CTA disclaimer paragraph left-aligned for improved readability, while the emoji, heading, and button remain centered.

---

## [1.4.0] - 2026-06-07

### Added
- `about.html`: dedicated About page with hero section and the Azqato pitch card (bio, role line, signature).
- "About" nav link added to all pages pointing to `about.html`, with active state highlighted on `about.html`.
- `.nav-links a.active` CSS rule added to `index.html` to support active nav highlighting.

### Changed
- Nav standardised across all pages: Portfolio, About, GitHub, Support. "Index" (external azqato.github.io link) replaced with "Portfolio" (relative `index.html` link) on all pages.
- About Azqato pitch card moved from `support.html` to `about.html`. `support.html` now focuses solely on the Buy Me a Coffee CTA and affiliate partners.
- Footer simplified to "Built by Azqato" across all pages, removing the redundant GitHub link from footer text.

---

## [1.4.1] - 2026-06-07

### Changed
- About page bio expanded with full background story: gaming origins, Twitch and YouTube content creation, B5TA community on RuneScape and Discord, web development work, and closing call to join the journey.
- Role line updated from "Investor, Developer, Community Builder" to "Content Creator, Web Developer, Community Leader" to better reflect the full bio.
- Em dash removed from closing paragraph ("adventure, one built on...").

---

## [1.5.0] - 2026-06-07

### Added
- Clan B5TA project card: community website for the RuneScape clan founded in 2014, tagged `Social` and `Gaming`, linking to the live GitHub Pages site and repo.
- `Gaming` added as a new filter tag category.

---

## [1.5.1] - 2026-06-07

### Changed
- Clan B5TA tag simplified from `Social, Gaming` to `Social` only. `Gaming` filter category removed; current categories are `Finance` and `Social`.

---

## [1.6.0] - 2026-06-07

### Added
- Cat Food Center project card: mobile-first PWA for evaluating cat food via barcode scan or search, tagged `Tools`, linking to the live GitHub Pages site and repo.
- `Tools` added as a new filter tag category.

### Changed
- Net Worth Tracker tagged with `Tools` in addition to `Finance`.

---

## [1.6.1] - 2026-06-07

### Changed
- Cat Food Center icon updated from 🐱 emoji to the project's own `favicon.svg` via the new `iconUrl` field.

### Added
- `iconUrl` optional field on project entries: accepts a URL to an image or SVG and takes precedence over `icon` when set.

---

## [1.7.0] - 2026-06-07

### Changed
- Public affiliate card: real referral link added (`share.public.com/azqato`), promo updated to "Free $20", description updated to match.
- Robinhood affiliate card: real referral link added (`join.robinhood.com/robertg273/`), promo updated to "Free $5–$200 Stock", description updated to match.
- M1 Finance affiliate card: real referral link added (`m1.finance/BVZBG3OqOfMj`), promo updated to "Free $75 Bonus", description updated to reflect $10,000 funding requirement and M1 Premium benefit.
- Affiliate section note updated from "Placeholder links" to "Some links are live, others are coming soon."

---

## [1.7.1] - 2026-06-07

### Changed
- Tesla affiliate card: real referral link added (`ts.la/robert459550`), promo updated to "Free 3 Months FSD", description updated to reflect 3 months of Full Self-Driving or $400 off Solar or Powerwall.

---

## [1.7.2] - 2026-06-07

### Changed
- M1 Finance affiliate card description updated to exact wording specified.

---

## [1.7.3] - 2026-06-07

### Changed
- Affiliate section note replaced with a plain-English disclaimer explaining how referral links work.

### Removed
- Webull and Coinbase placeholder cards removed from the affiliate grid.

---

## [1.7.4] - 2026-06-07

### Added
- Lyft affiliate card: 50% off first ride up to $10 (`lyft.com/invite/ROBGOLDY630855`).

---

## [1.8.0] - 2026-06-08

### Added
- `/docs/` directory created to house all project documentation.
- `docs/TRD.md`: Technical Reference Document covering system architecture, tech stack, data models, internal data flow, state management, third-party integrations, performance requirements, and known technical debt.
- `docs/DESIGN.md`: Design system document covering color palette (all CSS custom properties), typography, spacing, breakpoints, component patterns, accessibility standards, and motion rules.
- `docs/PRFAQ.md`: Press release and FAQ (internal and external).
- `docs/TENETS.md`: Product principles with 5 prioritized tenets.
- `docs/METRICS.md`: Success metrics, targets, measurement methods, and reporting cadence.
- `docs/ROADMAP.md`: Milestone table with current phase, planned features, and deferred items.
- `docs/SECURITY.md`: Security model covering auth, data storage, third-party trust, attack surface, and dependency policy.
- `docs/RUNBOOK.md`: Operational runbook with local setup, build, deploy, rollback, environment configs, common errors, and monitoring.

### Changed
- `PRD.md` moved from project root to `docs/PRD.md` and expanded with problem statement, target user personas, assumptions, and measurable success criteria.
- `PATCHNOTES.md` moved from project root to `docs/PATCHNOTES.md`.
- `README.md` updated with tech stack table, prerequisites section, environment variable reference (none), expanded deploy instructions, link to `/docs/`, and updated file overview reflecting the new `docs/` structure.

### Removed
- `PRD.md` from project root (moved to `docs/PRD.md`).
- `PATCHNOTES.md` from project root (moved to `docs/PATCHNOTES.md`).

## [1.9.0] - 2026-06-08

### Added
- ComposerAtlas project card: curated strategy library and education hub for Composer.trade investing, featuring strategy pages with plain-English logic breakdowns, risk profiles, metrics tables, and a glossary of systematic investing concepts. Tagged `Finance` and `Tools`.

## [1.9.1] - 2026-06-08

### Changed
- ComposerAtlas and Cat Food Center tagged with `Education` to reflect their educational content.
- `Education` added as a new filter tag category.

---

## [1.9.2] - 2026-06-09

### Changed
- Buy Me a Coffee CTA paragraph split: main text ends with `*` asterisk; disclaimer moved below the button in smaller italic text.

---

## [1.9.3] - 2026-06-09

### Added
- Boaty McBoatface Ventures project card: humorous marketing site for a fictional New England canvas exo-skeleton water displacement company, tagged `Meme`.
- `Meme` added as a new filter tag category.

---

## [2.0.0] - 2026-06-09

### Added
- `links.html`: Social and platform links hub, organized into sections: Community and Streaming, YouTube, Music, Social, Investing, and More. All external links from the old website consolidated here.
- `youtube.html`: YouTube channels page showcasing all four channels (Azqato, Azqato Streams, Azqato Mixes, Azqato Chills) as cards with thumbnail photos, channel descriptions, and subscribe buttons.
- `invests.html`: Azqato Invests resource hub with 14 curated sections: Platforms, Careers, ETFs, Companies, Ratings, Screeners, Real Estate, Charts, Databases, Economic Indicators, Education, Guides, Indices, Information, and News.
- `music.html`: Music page featuring the two Spotify playlists (BANGERS, ADDICTIONS) with cover art, plus links to Last.fm, Mixcloud, and YouTube Mixes.
- `accounts.html`: Gaming accounts page listing Azqato's profiles across Steam, League of Legends, Teamfight Tactics, and RuneScape.
- `privacy-policy.html`: Full privacy policy page covering Consent, Information Collection, Log Files, Cookies, DART Cookies, CCPA, GDPR, Children's Information, Affiliate Links, Financial Disclaimer, and Entertainment Purposes.
- `img/` directory with 14 image assets migrated from the old website: profile photos (`home-hero-profile.jpg`, `about-profile.jpg`, `logo-cat-avatar.jpg`), YouTube channel thumbnails (`yt-thumb-azqato.jpg`, `yt-thumb-streams.jpg`, `yt-thumb-mixes.jpg`, `yt-thumb-chills.jpg`), larger channel images (`yt-channel-*.jpg`), Spotify playlist covers (`music-playlist-bangers.jpg`, `music-playlist-addictions.jpg`), and music logo (`music-logo-small.jpg`).
- Profile photo (`home-hero-profile.jpg`) added to the `index.html` hero section as an 80px circular avatar.
- "All Links →" secondary CTA button added to the `index.html` hero actions, pointing to `links.html`.
- Profile photo (`about-profile.jpg`) added to the `about.html` pitch card avatar, replacing the ⚡ emoji.
- `Links`, `YouTube`, and `Invests` nav links added to all pages.
- Privacy Policy footer link added to all pages.

### Changed
- `index.html` hero description expanded to mention content creation, gaming, investing, music production, and streaming, preserving the intro text from the old website's landing page.
- Nav expanded from 4 links (Portfolio, About, GitHub, Support) to 7 links (Portfolio, About, Links, YouTube, Invests, GitHub, Support) across all pages.
- Footer on all pages updated from "Built by Azqato" to include a "Privacy Policy" link.
- `about.html` pitch avatar size increased from 60px to 72px to better display the profile photo.

### Removed
- `oldwebsite/` directory and all its contents deleted after full content migration.

---

## [2.0.1] - 2026-06-09

### Changed
- League of Legends accounts on `accounts.html` updated to Riot ID format: `Chief Rocka` → `서주프#zoop` and `Azqato` → `Azqato#zoop`.
- Both LoL op.gg links updated to the new URL format (`op.gg/lol/summoners/na/`).

---

## [2.0.2] - 2026-06-09

### Changed
- TFT accounts on `accounts.html` updated to metatft.com with Riot ID format: `서주프#zoop` and `Azqato#zoop`. Links updated from lolchess.gg to `metatft.com/player/na/`.
- RuneScape accounts updated: `Hctibaru` replaced with `ironqato`; both links updated from runeclan.com to runepixels.com (`/players/<name>/skills`).

---

## [2.0.3] - 2026-06-09

### Changed
- Privacy Policy link moved from all page footers to the More section on `links.html` as a button.
- Footers across all 9 pages simplified back to "Built by Azqato" only.

---

## [2.0.4] - 2026-06-09

### Changed
- Footer byline updated to "Built by Azqato." on all pages. The period is outside the link element so it renders in `--text-muted` rather than the accent green.

---

## [2.1.0] - 2026-06-10

### Added
- Stock Methodology project card: educational site documenting a fundamentals-driven individual stock and ETF investing methodology, covering 10 evaluation metrics (PEG, P/E FWD, RSI, revenue/EPS growth, cash/debt, 52W range), a Finviz screener guide, Seeking Alpha watchlist setup, and VIX-based index investing strategies. Tagged `Finance` and `Education`.

---

## [2.1.1] - 2026-06-10

### Changed
- All links to the GitHub profile (`github.com/Azqato`) now open in the same tab. Removed `target="_blank" rel="noopener"` from all 20 occurrences across 9 pages (nav links, footer bylines, hero CTA, and links page button).

---

## [2.2.0] - 2026-06-10

### Added
- TQQQ Strategies project card: educational wiki-style site documenting six leveraged ETF strategies side by side: 3 Sig, 6 Sig, 9 Sig, TQQQ For The Long Term, Holy Grail, and HFEA. Each strategy has a dedicated page covering rules and logic, performance notes, risks, and sources. Tagged `Finance` and `Education`. Live at `https://azqato.github.io/leveraged-strategies/`.

---

## [2.2.1] - 2026-06-10

### Changed
- TQQQ Strategies card icon updated from ⚡ to 🚀 to match the site's favicon.

---

## [2.2.2] - 2026-06-10

### Changed
- TQQQ Strategies project card renamed to "Leveraged Strategies" ahead of a planned site rename.

---

## [2.2.4] - 2026-06-11

### Changed
- Fixed HTML-encoded em dash (`&mdash;`) in `index.html` hero bio paragraph. Previous audit only searched for the literal `—` character and missed the entity form.
- `docs/PRD.md` Writing Style section updated to note that em dashes appear in two forms in HTML (`—` and `&mdash;`) and both are prohibited. Audits must search for each form independently.

---

## [2.2.3] - 2026-06-11

### Changed
- Em dashes removed from all HTML pages (accounts.html, index.html, invests.html, youtube.html) and all documentation files (PRD.md, PATCHNOTES.md, ROADMAP.md, DESIGN.md, TRD.md, METRICS.md, SECURITY.md, TENETS.md, PRFAQ.md, RUNBOOK.md) and README.md. Replaced with comma, colon, semicolon, parentheses, or period based on context.
- Version headers in PATCHNOTES.md updated from `[x.y.z] — YYYY-MM-DD` format to `[x.y.z] - YYYY-MM-DD` for consistency.
- `docs/PRD.md` updated with a Writing Style section documenting the no-em-dash methodology and preferred punctuation alternatives.

---

## [2.3.0] - 2026-06-13

### Added
- New introductory landing page at `index.html`, designed as the front door for first-time visitors. It introduces who Azqato is across gaming, content creation, investing, music, and community, then routes visitors onward rather than opening straight into the project grid.
- Discord join as the primary call to action, featured both in the hero and in a dedicated closing CTA band (`discord.gg/39JrFNY7qS`), styled with the official Discord brand color (`#5865f2`) and logo.
- "Explore the site" card grid linking to all eight key destinations: Projects, About, YouTube, Music, Invests, Gaming Accounts, Links, and Support, each with an icon and one-line description.
- Hero with an easygoing introduction and a secondary "Explore the site" anchor button, plus an intro blurb with a short bio and category pills (Gaming, Investing, Music, Web Dev, Community).
- `--discord` and `--discord-hover` CSS custom properties on the landing page.

### Changed
- Site structure reworked so the landing page is the default entry point. The project grid (cards, tag filter, hero) moved from `index.html` to `projects.html`; the new introductory landing page now occupies `index.html`.
- Navigation label renamed from "Portfolio" to "Projects" across all pages, and the link now points to `projects.html`.
- Nav logo on every page links home to `index.html` (the new landing page). The project grid page's logo, previously `href="#"`, now also points to `index.html`.
- `projects.html` page title updated from "Azqato | Portfolio" to "Azqato | Projects".

### Notes
- The landing page follows the existing design system (GitHub dark theme, `#00d4a0` accent, system font stack, zero dependencies) and is self-contained with inline CSS.
- The site now comprises 10 pages.

---

## [2.3.1] - 2026-06-13

### Added
- "Home" and "Discord" links added to the global navigation. Home points to the landing page (`index.html`); Discord points to the community invite (`discord.gg/39JrFNY7qS`) and opens in the same tab, matching the GitHub link convention.

### Changed
- Navigation reordered across all 10 pages to: Home, About, Discord, Invests, Links, Projects, YouTube, GitHub, Support.
- Landing page hero introduction reworded for a more confident, knowledgeable first impression (removed the "music nerd" phrasing and the "front door / come hang out" close).
- Landing page intro blurb refined for tone: now notes B5TA has thrived on RuneScape and Discord for over a decade, and splits "music production" and "DJ mixes" into separate highlighted lanes.
- Highlighted the connecting "and" before "web development" in the intro lanes so it carries the same accent styling as the other lanes.

---

## [2.3.2] - 2026-06-13

### Added
- No Fee Apartments project card: curated directory of no-broker-fee apartment buildings across New York City, Boston, and San Francisco. Tagged `Tools` and `Real Estate`. Links to `nofeeapartments.net`.
- LV Guest List project card: free guest list access for Las Vegas's top nightclubs and dayclubs. Tagged `Social`. Links to `lvguestlist.com`.
- `Real Estate` added as a new filter tag category.

### Changed
- `projects.html` hero stripped down to title and description only: removed the avatar image, "Available for collaboration" badge, and CTA buttons.
- `projects.html` hero description rewritten as a concise rocket pitch: "Finance dashboards, social platforms, educational tools, and a few projects that refuse to take themselves seriously. Every one is live and built to actually be used. Pick a tag and dig in."
- Spacing between the hero description and the Projects section header tightened: hero bottom padding reduced from `3rem` to `1.5rem`; section top padding reduced from `3rem` to `1.5rem`.

---

## [2.4.0] - 2026-06-13

### Added
- `discord.html`: dedicated Discord page listing all four community servers (Azqato, Azqato Invests, B5TA, League of Azqato) as cards with permanent invite links, descriptions, and Discord-blue Join Server buttons.
- `--discord` and `--discord-hover` CSS custom properties on `discord.html`.

### Changed
- Nav Discord link updated from the external `discord.gg` invite URL to `discord.html` across all 11 pages, so visitors browse all servers before choosing one to join.
- Azqato main Discord invite updated from the temporary link (`discord.gg/39JrFNY7qS`) to the permanent invite (`discord.gg/sKGKC3JFSE`) in `index.html` and `links.html`.
- `docs/PRD.md` site structure table updated to include `discord.html`.
- The site now comprises 11 pages.

---

## [2.4.1] - 2026-06-13

### Changed
- Discord server card icons updated: Azqato 🐱, Azqato Invests 💸, B5TA ⚔️ (unchanged), League of Azqato 🖥️.
- `discord.html` hero description rewritten as a general community pitch, removing per-server references in favour of a broader invitation.

---

## [2.5.0] - 2026-06-13

### Changed
- Documentation consolidated from 10 files to 4: `README.md` (root), `docs/PRD.md`, `docs/DESIGN.md`, `docs/PATCHNOTES.md`.
- `docs/TRD.md`, `docs/TENETS.md`, `docs/PRFAQ.md`, `docs/SECURITY.md`, `docs/RUNBOOK.md`, `docs/METRICS.md`, and `docs/ROADMAP.md` removed; all content absorbed into `docs/PRD.md` under dedicated sections.
- `README.md` rewritten as a developer-only reference: removed marketing language, updated file overview to 11 pages, updated nav description to reflect `discord.html` and the `class="active"` pattern, added "Adding a Discord Server" instructions.
- `docs/DESIGN.md` updated: fixed card border-radius to `10px`, hover transform to `translateY(-2px)`, and card gap to `1rem` to match actual implementation; updated `--discord` and `--discord-hover` note to reflect both `index.html` and `discord.html`; added Discord server card component pattern; updated all typography and spacing values to current code.
- `docs/PRD.md` expanded with consolidated Architecture, Tenets, FAQ, Security, Runbook, Metrics, Roadmap, and Documentation Process sections; added F8 (Discord Page) and F10 (Landing Page) to Feature List; updated site structure table to 11 pages; updated Discord server data model with all four permanent invite links; updated project list to 11 current projects.
- Roadmap in `docs/PRD.md` updated: v2.4.0 milestone renamed to "discord.html: four server cards, sitewide nav update" to match what actually shipped; planned code-extraction milestone renumbered to v2.6.0.

### Removed
- `docs/TRD.md`
- `docs/TENETS.md`
- `docs/PRFAQ.md`
- `docs/SECURITY.md`
- `docs/RUNBOOK.md`
- `docs/METRICS.md`
- `docs/ROADMAP.md`

---

## [2.6.0] - 2026-06-14

### Added
- Prompts project card: personal reference library of reusable Claude Code prompts for recurring development, documentation, and maintenance tasks. Zero-dependency, hash-based routing, one-click copy; works offline from any browser. Tagged `Tools` and `Education`. Live at `https://azqato.github.io/prompts/`.

---

## [2.6.1] - 2026-06-15

### Changed
- ComposerAtlas demo link updated from `https://azqato.github.io/ComposerAtlas/` to `https://azqato.github.io/composer` to match the new deployment directory.

---

## [2.6.2] - 2026-06-15

### Added
- "Azqato Projects" resource card added as the first card on `invests.html`, listing all five finance-related projects: Net Worth Tracker, VIX Strategy, ComposerAtlas, Stock Methodology, and Leveraged Strategies.

---

## [2.6.3] - 2026-06-15

### Fixed
- "Azqato's Projects" card title in `invests.html` corrected from "⚡ Azqato Projects".

---

## [2.6.4] - 2026-06-15

### Fixed
- Discord link in the `invests.html` hero paragraph updated from the direct `discord.gg` invite URL to `discord.html`, consistent with the rest of the site.

---

## [2.6.5] - 2026-06-27

### Added
- Azqato's Tools project card: collection of free, browser-based utilities including a Markdown editor with live preview and HTML export, a Favicon Downloader, a Link Cleaner that strips tracking parameters, and a Nasdaq 100 Screener. Tagged `Tools`. Live at `https://azqato.github.io/tools/`.

---

## [2.6.6] - 2026-06-27

### Changed
- "Tools" nav link added to all 11 pages after "Projects", pointing to `https://azqato.github.io/tools/` and opening in the same tab. Nav order is now: Home, About, Discord, Invests, Links, Projects, Tools, YouTube, GitHub, Support.

---

## [2.5.1] - 2026-07-02

### Added
- Twitch Prime affiliate card on `support.html`: explains that Amazon Prime members can use their one free monthly Twitch channel subscription on Azqato's channel at no extra cost. Links to `twitch.tv/azqato`.

---

## [2.5.2] - 2026-07-05

### Fixed
- **Nav bar horizontal overflow between 601px and ~754px on all 11 pages.** The desktop nav (10 links, `gap: 1.5rem`, no wrap) only had a single `display: none` breakpoint at `max-width: 600px`; above that width the full-width link row didn't fit until the viewport reached ~754px, forcing the whole page to overflow horizontally by 51-55px on every page in that range (confirmed via headless Chrome DOM measurement, not screenshots, since `document.documentElement.scrollWidth > clientWidth` in that window). Replaced the abrupt hide-at-600px behavior with a hamburger menu: nav links collapse behind a `.nav-toggle` button below 860px (safe margin above the ~754px content width) and open as a dropdown panel, restoring mobile/tablet navigation that was previously just missing below 600px with no fallback. Implemented identically across all 11 pages (markup, CSS, and a small inline toggle script per page, consistent with the site's no-shared-file architecture).
- **CSS Grid bare `1fr` tracks reverting to unclamped columns on mobile.** `.platform-grid` (`accounts.html`), `.resource-grid` (`invests.html`), `.link-grid` (`links.html`), and `.channel-grid` (`youtube.html`) used `minmax(Npx, 1fr)` at desktop width but their `@media (max-width: 600px)` overrides reverted to a bare `1fr` (or `1fr 1fr`), which has an implicit `min-width: auto` rather than `0`; a card with long unbreakable content could force the grid, and the page, wider than the viewport. Changed the mobile overrides to `minmax(0, 1fr)` (and `repeat(2, minmax(0, 1fr))` for the two-column cases) to match the desktop guard.
- **Redundant spacing from `margin-top` stacked on top of a flex `gap`.** Six elements (`.hero-actions` in `index.html`/`projects.html`, `.pitch-signature` in `about.html`/`support.html`, `.playlist-btn` in `music.html`, `.affiliate-link-btn` in `support.html`) carried their own `margin-top` despite already being spaced by their flex-column parent's `gap`, doubling the intended gap. Removed the redundant margins; parent `gap` now provides the sole spacing.

---

## [2.6.16] - 2026-07-09

### Changed
- Updated all VIX Strategy references to the renamed lowercase URLs: live site `https://azqato.github.io/vix` (`invests.html` card and `projects.html` `demo`) and repo `https://github.com/Azqato/vix` (`projects.html` `github`).

---

## [2.6.15] - 2026-07-09

### Added
- `--discord` and `--discord-hover` color tokens on `invests.html` to support a Discord-branded hero button.

### Changed
- `invests.html` restructured to the `discord.html` layout pattern: removed the "Community investing resources" hero badge, replaced the large `.section-head` blocks with discord-style `.section-header` sections (accent-bar `.section-title` + `.section-desc` + bottom-border separator), and retitled the two sections "Projects" and "Curated Resources".
- `invests.html` hero "Join the Discord" button restyled to match the homepage `.btn-discord` (blue `--discord` background, white text, inline Discord SVG logo, lift-and-glow hover); the secondary "Explore the projects" button aligned to the homepage secondary style.
- `index.html` both "Join the Discord" buttons repointed from the external `discord.gg/sKGKC3JFSE` invite to the internal `discord.html` page (removed `target="_blank"`/`rel`, now same-site navigation).
- `codes.html` reformatted to the invests/discord layout: removed the "Developer tools & AI prompts" hero badge and both hero CTA buttons, replaced `.section-head` with the discord-style `.section-header` (Title/Description/separator), and merged its duplicate `html {}` rules.
- `youtube.html` reformatted the same way: removed the "▶ Subscribe & watch" hero badge and added a "Channels" `.section-header` (Title/Description/separator) above the channel grid.
- `discord.html` hero heading changed from "Join Azqato's Discord" to "Azqato's Discord".
- `about.html` removed the "Investor, Developer, Community Builder" hero badge.
- `links.html` removed the "Find me everywhere" hero badge and changed the hero description from "All my platforms, communities, and channels in one place." to "Find me everywhere."

### Removed
- Unused `.hero-badge` / `.hero-badge::before` / `@keyframes pulse` CSS from `invests.html`, `codes.html`, and `youtube.html` (badge markup removed on those pages). The same now-unused CSS remains in `about.html` and `links.html` and is flagged for later cleanup.

---

## [2.6.14] - 2026-07-08

### Changed
- Merged two adjacent `html { }` rules in `invests.html` into a single block (`overflow-y: scroll` + `scroll-behavior: smooth`). Cosmetic cleanup only; no behavior change.

---

## [2.6.13] - 2026-07-08

### Changed
- Updated the Leveraged Strategies featured card link on `invests.html` from `https://azqato.github.io/leveraged-strategies/` to `https://azqato.github.io/leverage/`.

---

## [2.6.12] - 2026-07-08

### Fixed
- **Nav logo position shifted slightly between pages.** `.nav-inner` centers itself with `margin: 0 auto` inside a `max-width: 1100px` wrapper, and Windows Chrome/Edge reserve real horizontal space for a vertical scrollbar only when a page's content is tall enough to scroll. Pages that fit within the viewport (`accounts.html`, `codes.html`, `youtube.html`) had no scrollbar and therefore a few pixels more usable width than longer pages, so the centered nav-inner (and the "Azqato" logo inside it) landed at a slightly different horizontal position depending on page length. Added `html { overflow-y: scroll; }` to every page so the scrollbar gutter is always reserved, whether or not the page actually needs to scroll; confirmed via headless Chrome measurement that `.nav-logo`'s `getBoundingClientRect().left` is now identical across all 12 pages at every tested width.

---

## [2.6.11] - 2026-07-08

### Changed
- Site favicon changed from the ⚡ emoji to 🦁 across all 12 pages (inline SVG data-URI favicon, unchanged everywhere else).
- The "About" card icon in the homepage explore grid (`index.html`) changed from 👋 to 🦁 to match the new favicon.

---

## [2.6.10] - 2026-07-08

### Fixed
- Corrected the Azqato Mixes channel link on `youtube.html` to `https://www.youtube.com/@AzqatoMixes` (previously pointed to the wrong channel).

---

## [2.6.9] - 2026-07-08

### Changed
- Reordered the `invests.html` featured project cards so the strategy projects lead: Stocks, Leveraged Strategies, ComposerAtlas, Net Worth Tracker, VIX Strategy, Stock Screener.
- Renamed the "Stock Methodology" featured card to "Stocks" on `invests.html` (link target unchanged: `https://azqato.github.io/stocks/`). The `projects.html` card retains its original name.

---

## [2.6.8] - 2026-07-08

### Added
- `invests.html` redesigned to lead with Azqato's own investing projects. New hero with a primary "Join the Discord" CTA and a secondary "Explore the projects" CTA that smooth-scrolls to the project showcase.
- Featured project showcase: six large clickable cards (Net Worth Tracker, VIX Strategy, ComposerAtlas, Stock Methodology, Stock Screener, Leveraged Strategies), each with a description, hover lift, gradient top-bar, and sliding arrow. Card icons mirror each project's own favicon emoji.
- Stock Screener link (`https://azqato.github.io/stocks/screener.html`) added to the projects list.
- Writing-style guard: a `.githooks/pre-commit` hook that blocks any commit introducing an em dash into an HTML or documentation file, enforcing the no-em-dash policy in the Writing Style section of `docs/PRD.md`. Enabled per clone with `git config core.hooksPath .githooks`.

### Changed
- Curated resource grid moved below the project showcase under a new "Curated Resources" heading; the old text-only "Azqato's Projects" resource card was replaced by the featured cards.

### Fixed
- Removed a stray em dash from a historical patch note entry in `docs/PATCHNOTES.md` (grid-collapse fix description), bringing all documentation into compliance with the no-em-dash policy.

---

## [2.6.7] - 2026-07-05

### Added
- ProteinPulse project card: browser-based calorie and protein tracker with daily logging, customizable goals, a carry-forward model, and weekly and monthly graphs. Fully client-side with Excel import and export. Tagged `Tools` and `Health`. Live at `https://azqato.github.io/protein/`.
- `Health` added as a new filter tag category.

---

<!-- Template for future entries:

## [x.y.z] - YYYY-MM-DD

### Added
-

### Changed
-

### Fixed
-

### Removed
-

-->

---

## Azqato Invests history (v0.1.0 to v1.1.1, before the docs merge)

Azqato Invests' own PATCHNOTES.md, merged word for word (Merged 2026-10-02); headings moved down a level and prefixed "Invests". Its versions were a separate line; from 2.12.0 Invests changes are main entries above. "PRD.md" and the other file names here mean the invests files, now merged (PRD Part 2).

Every change to this project, newest first. Versions follow semantic versioning and stay below 1.0.0 until the site launches (see Conventions in PRD.md). Dates come from the system clock.

### Invests v1.1.1 - 2026-10-02 - Documentation audit

#### Changed

- README.md rewritten for the live site: the address, the five sections as they are now, the status, and the doc list (HOSTING.md marked as a record).
- LICENSE.md: permission requests go to https://github.com/Azqato/azqato.github.io/issues; github.com/Azqato/invests no longer exists.
- PRD.md: every statement that described the site as unpublished, the old section names or the separate repository is marked with the current state, original text kept (Decisions D4, D5, D12, D20; Constraints; Feature list; Runbook; Monitoring; Security; Deprecation and Removal, including the retired pre-v1.1.0 addresses; Press Release and FAQ facts). Roadmap items P13 to P17 moved from inside Writing Style to Future updates; P13.4 (delete the empty repository) marked done. New Documentation Versus Reality entries 13 to 17 and a new entry under Documentation audits.
- DESIGN.md: the intro, Sidebar, Breadcrumbs and pager, Search, Theme button, the 640px breakpoint and the measured pairings note brought up to date for v1.0.1 and v1.1.0.
- HOSTING.md and UI-REVIEW.md marked as records, with what came after.

#### Tested

- Docs only: no page or script changed, so no browser test (Testing Cadence). `python scripts/check.py` still passes.

### Invests v1.1.0 - 2026-10-02 - Sections by topic

#### Changed

- Navigation restructured at the author's request: the sidebar groups are Individual Stocks (Overview, Philosophy, Stock metrics, Screener), Indices & ETFs (Overview, Market Overview), VIX Strategy (Overview, VIX Dashboard, VIX Custom builder), Leveraged Strategies (Overview and the six strategies) and Resources (Curated resources, Finviz and Seeking Alpha setup guides, FAQ). Before: Learn, Tools, Strategies, Resources, FAQ. Each topic group's first page is its landing page: the old Learn Overview became Individual Stocks, and Index & ETF methodology became Indices & ETFs. No page content changed.
- Addresses moved with the groups: learn/, tools/, strategies/ and faq.html are gone; pages live in stocks/, indices/, vix/, leveraged/ and resources/ (PRD, Site map). No redirects, by the author's decision: the old addresses had been live about an hour.
- Breadcrumbs read Home > group > page; the pager follows the sidebar order; the Home cards, the footer's FAQ link, search's popular pages and the browser tests use the new addresses.
- PRD: Site map, Folder structure and the D7 redirect list updated; roadmap items P15 (azqato.com's colors), P16 (one VIX page) and P17 (SEO and landing-page review) added.

#### Tested

- `python scripts/check.py`: 21 pages, 0 failures (0 broken internal links). `python scripts/browser.py`: 0 failures, the usual 9 notes.

### Invests v1.0.1 - 2026-10-02 - Pager and sidebar note

#### Changed

- Pager: each button fits its text instead of taking half the page. Next sits at the right edge even when it's alone (Home), Previous at the left (FAQ), so there's no empty half-width column (assets/css/site.css).
- Home and Resources: the gap above the pager is 32px like every other page; invests.html's last section no longer adds its 48px bottom padding there.
- Sidebar: the "Educational use only. Not financial advice." note sits at the bottom of the sidebar, on two lines (scripts/site.py wraps it in `.site-sidebar-foot`; site.css pins it). When open groups fill the sidebar it follows them, 32px below.
- Docs: the session handover (HANDOVER.md, never committed) moved into PRD.md: the live state under Current phase, P10 marked done for steps 1 to 3, P13 (post-launch list: D7 redirects, the author's review, the two dead Resources links, deleting the empty Azqato/invests repository after testing) and P14 (folding into azqato.com's structure), and four Never rules (the private project and the backup bundle, staging by name, stopping only your own servers). Repository Hygiene and the Runbook describe `invests/` as the single source of truth.

#### Tested

- `python scripts/check.py`: 21 pages, 0 failures. `python scripts/browser.py`: 0 failures, the usual 9 notes. Pager measured in headless Edge at 1550px and 390px on Home, Learn/Metrics and FAQ; sidebar note measured at the bottom of the sidebar at 2100x1250.

### Invests v1.0.0 - 2026-10-02 - Live

#### Changed

- Published at https://azqato.com/invests/ as part of azqato.github.io v2.11.0 (D20 go-ahead). Post-deploy check passed (PRD, Current phase). The separate repository is retired; `invests/` in azqato.github.io is the single source of truth.

### Invests v0.18.0 - 2026-10-02 - Merging into the main site

#### Changed

- Hosting (Question 18, option D, D21): the site moves into the azqato.github.io repository as a self-contained `invests/` folder, served at https://azqato.com/invests/. `SITE_URL` in scripts/site.py is now https://azqato.com/invests/, and canonical links, og:url and sitemap.xml use azqato.com's clean addresses (for example https://azqato.com/invests/learn/metrics).
- History (Question 16): the private project's name was replaced with "private project" in every past commit with `git filter-repo`; all 24 commits kept with new ids. A backup of the old history stays outside the repository and is never pushed.
- Runbook: Deploy and Rollback rewritten for the main repository.
- Missing values show an en dash (–) instead of an em dash on the screener and Market Overview, 27 places (Question 19), so the main repository's em-dash hook passes. check.py now fails on any em dash in a page file.

### Invests v0.17.1 - 2026-10-02 - Hosting analysis

#### Added

- docs/HOSTING.md: the hosting options (GitHub Pages, a Cloudflare Worker, publishing into the main repo's invests/ folder, a full merge, a subdomain), compared, with a recommendation (Question 18).
- The author's answers to Questions 16 and 17 recorded in PRD.md; Question 18 added.

### Invests v0.17.0 - 2026-10-02 - Site-wide checks, documentation and publish plan (P7 to P9)

Development plan P7 (steps 1 to 8), P8 and P9, at the author's request. Nothing was pushed or published (D20). Each step's findings are recorded under its phase in docs/PRD.md.

#### Added

- Every page has `<link rel="canonical">` and og:url with its published address under https://azqato.github.io/invests/ (`SITE_URL` and `page_url()` in scripts/site.py). All six sharing tags are now on all 21 pages.
- sitemap.xml at the root, listing the 21 pages, generated by scripts/site.py. No robots.txt: azqato.github.io owns the origin (PRD, P9.3).
- The D7 redirect list (19 old addresses, one hop each) and the redirect-page mechanism for GitHub Pages, under Deprecation and Removal in docs/PRD.md.
- Runbook: Build (every script, in order, with the expected output), Deploy and Rollback for GitHub Pages (written, not run), more Common errors.
- Conventions, filled in from the code and the git history.
- Questions 16 (what becomes public with the repository: its history and the Template Interface files) and 17 (azqato.com/invests and invests.html, with a recommendation), both for the author.
- LICENSE.md names the issue tracker for permission requests: https://github.com/Azqato/invests/issues, open once the repository is public.
- `.gitignore`: `__pycache__/`.

#### Changed

- The author's private project is no longer named anywhere in the docs (P9.6), because github.com/Azqato/invests, created by the author on 2026-10-02, will be public. D2 is unchanged in meaning; earlier commits in the local history still contain the name (Question 16).
- PRD: the milestone table (M4 to M8 complete, M9 and M10 in progress), Current phase, the verification checklist (every section dated 2026-10-02), System architecture, Tech stack, Folder structure, Data models, Security, Repository Hygiene, Social Sharing Tags, Metrics and Documentation Versus Reality (entries 5, 7 and 8 resolved; 9 to 12 added).
- DESIGN.md: the Home page, Footer, Breakpoints, focus and Page layouts notes marked with what was built, the earlier text kept.
- README.md: status and live-site lines brought up to date; a link to docs/UI-REVIEW.md.

#### Fixed

- Screener layout shift: Lighthouse measured CLS 0.175 on mobile, because the disclaimer under the table moved down when the data arrived. The table area now holds 70vh of room while loading; CLS 0.003 on the rerun.
- Feed text in HTML: the screener and Market Overview put tickers and names from the stock feeds into the page with `innerHTML` unescaped. scripts/site.py now wraps their `res.json()` in `azqClean()`, which removes `<` and `>` from every text value in a fetched feed.
- `.gitignore`'s comment named tools/snapshot.py; it's scripts/snapshot.py.

#### Removed

- The empty `previews/` folder left from the width previews.

#### Checks run

- Fresh snapshots (stocks 860ee2b9, vix 37eeadd1, leverage c86321cd, azqato.github.io 58767b54), then `python scripts/inventory.py`, `python scripts/site.py` (21 pages, 242 search entries, 47 em dashes replaced) and `python scripts/check.py`: 21 pages, 0 failures.
- `python scripts/browser.py` after the fixes: 0 failures, the same 9 notes as before (feeds deliberately blocked in the test, the stocks feed's 2026-09-30 data, the VIX allorigins fallback).
- Lighthouse 13.5.0, mobile, in Edge: Home LCP 1.7 s, CLS 0, TBT 0 ms; Screener LCP 2.1 s, CLS 0.003, TBT 0 ms; 9 Sig LCP 1.7 s, CLS 0, TBT 0 ms. Accessibility, best practices and SEO 100 on all three.
- Keyboard and focus in headless Edge: skip link, focus order, drawer and search focus in and out, landmarks, accessible names.
- Outside links: 96 checked, 2 dead (dividendstocksonline.com, expired certificate; www.denvercondomania.com, times out), both source content on Resources, left as they are for P11 (D19). 8 more refused automated requests, which isn't a dead link.
- Em dashes: none in this site's own text or any page. Secrets: none.
- Not browser-tested: the canonical, og:url and sitemap additions are head tags and a new file, checked by script only; Deploy and Rollback weren't run (D20).

### Invests v0.16.1 - 2026-10-02 - VIX Custom builder order

#### Changed

- VIX Custom builder: "Your Categories" (the ticker inputs) sits above "Your Custom Allocation", after the reading and tier line, at the author's request.

#### Fixed

- The VIX section headings inside a header row (such as "Your Categories") no longer carry the article heading's 48px top margin, which left a large gap at the top of their box.

### Invests v0.16.0 - 2026-10-02 - UI review fixes

Every decision in docs/UI-REVIEW.md, built and then tested. Its "Done" section has the full detail.

#### Added

- An "Azqato.com" group in the sidebar with azqato.com's links, shown on phones, where its top bar is hidden.
- Three Home cards, in the source's card style, for the sections no source card covered: Market Overview & VIX tools, Curated Resources and FAQ.
- site.js labels each VIX table cell with its column heading, for the phone layout.
- A "Swipe sideways for more columns →" line above the screener table on phones.

#### Changed

- Page width, option C: content runs full width to 1400px on every page; the stocks pages' 820px and the VIX pages' 1100px caps are lifted; Resources and the FAQ give back the empty "On this page" column; Market Overview's grid fills the width.
- One footer per page: the source footers that repeat it are hidden (kept in the page), and the VIX disclaimer and copyright lines move into the site footer.
- Home: one grid of 10 project cards instead of "Explore the site" plus "Projects"; emoji icons share one size and tile; on phones the icon sits beside the title.
- No text under 12px (scripts/site.py `min_font`, and site.css).
- Sidebar groups collapse unless they hold the current page.
- Phones: breadcrumb, "On this page", footer and sidebar links at least 24px tall; FAQ toggles 48px.
- Stocks table figures use the site font with tabular digits.
- The stocks pages' tag ("Strategy Q&A" and the others) is a plain label, not a pill.
- Stock metrics: subtitles line up with their headings.
- Screener: the disclaimer is a left-aligned paragraph; the ticker column casts a shadow; on phones the tier chips wrap and the filter box is full width.
- Market Overview: card names wrap.
- Resources: masonry columns.
- VIX tables are stacked cards on phones.
- VIX Custom builder: the result (reading, tier, chart, breakdown) comes before the ticker inputs, and its tier line reads like the Dashboard's.
- VIX pages: mono font is SF Mono, Consolas or Liberation Mono; the tool sections have less padding.
- VIX Strategy: site headings, borders and card styles.
- Leverage callouts: 15px text.

#### Fixed

- The VIX tools showed CACHED on the second page opened within 30 minutes, for the same live reading; a reading under 30 minutes old now shows LIVE (STALE still marks an old one).
- QQQ and TQQQ looked underlined (Courier New's Q).
- Home and Resources card titles sat far below their icons (the article heading margin).
- Market Overview card names were cut off on phones.

#### Removed

- The "Explore the site" tiles on Home (this site's own, not source content; their sections are cards in the one grid).
- The width previews (previews/, scripts/previews.py) and check.py's skip for them, once option C was chosen.

### Invests v0.15.0 - 2026-10-02 - Width previews

#### Added

- previews/: three page-width options (A, grids wide with prose capped; B, one column of about 1100px; C, everything full width), each on Market Overview, Stock metrics and Resources, built by scripts/previews.py. The real pages are unchanged.

#### Changed

- scripts/check.py skips previews/.

### Invests v0.14.4 - 2026-10-02 - UI review

#### Added

- docs/UI-REVIEW.md: a full-scroll review of every page in headless Edge, with the issues found and suggested fixes, for the author to decide on. No page was changed.
- The author's decisions on the review, in docs/UI-REVIEW.md.

### Invests v0.14.3 - 2026-10-02 - VIX hero size

#### Changed

- The VIX pages' sections have 40px top and bottom padding instead of the source's landing-page spacing, and a section's first heading drops the template's 48px top margin.
- The VIX Strategy hero fits its content instead of filling 90% of the window (the source built it as a full-page landing section), in both themes, at the author's request.

### Invests v0.14.2 - 2026-10-02 - Rule: no data feeds here

#### Added

- PRD Constraints: this repo holds no data feeds, data files or data-fetching jobs; the only automation is the GitHub Pages or Cloudflare Pages build that publishes the site.

### Invests v0.14.1 - 2026-10-02 - Roadmap: old repos

#### Added

- PRD Future updates, P12: after launch, the stocks and vix repos become redirects and data feeds only, and the VIX feed gets a second source in place of allorigins.

### Invests v0.14.0 - 2026-10-02 - Wider layout and light-mode legibility

#### Changed

- Page content starts at the sidebar instead of being centered, and uses up to 1400px (Home's and the VIX pages' own centered containers too), at the author's request.
- Light mode: darker body and muted text, stronger lines, larger card text.
- VIX Strategy in light mode: a light hero background, a dark headline, and no scanlines (the source's were made for its dark page). Dark mode is unchanged.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.13.0 - 2026-10-02 - Tests for P2 to P6

#### Added

- scripts/browser.py: browser tests in headless Edge (page errors in both themes and at phone width, sideways scroll, WCAG AA text contrast, the shell's controls, the FAQ, live data and feed fallbacks).

#### Changed

- Light-theme data colors darkened to pass contrast, the screener tiers and VIX ticker colors given light counterparts, white text on the light VIX button, and a lighter red for the stocks badge in dark (DESIGN.md, Data colors).
- The VIX ticker colors in strategy.js and custom.js are CSS variables with the source colors as fallback; chart.js reads their values for the donut (scripts/site.py patches the copies).

#### Fixed

- The leverage pages' risk notices were laid out as a row by the template's `.callout`, which made TQQQ FTLT and Holy Grail scroll sideways on phones.
- scripts/check.py compares text with spaces and punctuation removed, so items split across tags are no longer reported missing.

#### Removed

- None.

### Invests v0.12.0 - 2026-10-02 - P6: Tools

#### Added

- Screener, Market Overview, VIX Dashboard and VIX Custom builder, in tools/, with their scripts in assets/js/stocks/ and assets/js/vix/.
- An integrity hash and `crossorigin` on Chart.js 4.4.0 (Question 12).

#### Changed

- The stocks tools' local `data/` fallback now points to azqato.github.io/stocks/data/, since this site has no data folder; the first source is still raw.githubusercontent.com.
- The VIX pages load the reading from azqato.github.io/vix/data/vix.js instead of a local `data/vix.js`.
- The VIX donut chart's center text, label and border colors follow the theme (assets/js/vix/chart.js).
- 12 em dashes in the tool pages and their inline scripts, and 1 in screener.js, were replaced (Question 14). The dashes that stand for a missing value ("(-)" in the methodology, and the dash the tools show in empty cells) are kept.
- The screener's links to the Metrics and Indices pages keep opening in a new tab, as in the source.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.11.0 - 2026-10-02 - P5: Strategies

#### Added

- VIX Strategy (strategies/vix.html), with its live VIX reading from azqato.github.io/vix/data/vix.js.
- The leveraged strategies landing and 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA, in strategies/leveraged/.
- An "On Composer Atlas" note on TQQQ FTLT (three strategies), Holy Grail (two) and HFEA (the database page and the symphony id, since Atlas has no link to a single entry; Question 4).

#### Changed

- 19 em dashes in the VIX Strategy page and its inline script, and 15 in the VIX scripts it shares with the tools, were replaced (Question 14; inventory/em-dashes.md lists each one).

#### Fixed

- None.

#### Removed

- None. The leverage sites' main.js isn't carried; it only drove their own navigation.

### Invests v0.10.0 - 2026-10-02 - P4: Learn and FAQ

#### Added

- Learn: the landing (from stocks' home page), Philosophy, Stock metrics, Index & ETF methodology, and the Finviz and Seeking Alpha setup guides, in learn/.
- FAQ (faq.html): all 37 questions and answers, with a filter box and links that open the answer they point to.

#### Changed

- Links between the stocks pages now point to the new addresses; section anchors are unchanged. Relative links between pages in the same folder are written plainly (scripts/site.py).

#### Fixed

- None.

#### Removed

- None. The stocks sidebar's "On This Page" list is replaced by the shell's own; its highlighting code in script.js is carried but finds nothing to highlight.

### Invests v0.9.0 - 2026-10-02 - P3: Home and Resources

#### Added

- Home (index.html): invests.html's intro and Discord button, five new tiles into the site's sections, and all 7 project cards. The Stocks, Stock Screener, VIX Strategy and Leveraged Strategies cards now link inside the site.
- Resources (resources/index.html): all 15 categories, all 71 links (referral links included) and the disclaimer, word for word.

#### Changed

- Links that pointed at the old copies now point at the live sites: azqato.github.io/composer to composeratlas.com, and invests.html's relative `discord.html` to azqato.com/discord.
- Source snapshots refreshed before the move (P1.4); nothing had changed.

#### Fixed

- None.

#### Removed

- None. invests.html's own nav script isn't carried: it only opened azqato.com's menu, which the site's copy of that nav replaces.

### Invests v0.8.0 - 2026-10-02 - P2: the shell

#### Added

- scripts/site.py: builds every page from the source snapshots, with one shared shell (top bar with azqato.com's nav above it, sidebar, breadcrumbs, pager, footer, search dialog) and the source content moved whole inside it. Needs BeautifulSoup 4.
- assets/css: Template Interface's theme.css, base.css and components.css and documentation-site's styles.css (as docs.css), copied unchanged from commit ed840da; site.css, this site's own styles; src-stocks.css, src-vix.css and src-leverage.css, the sources' stylesheets scoped to their content.
- assets/js: theme.js (light and dark, system theme first, adapted from the template's theme-toggle.js), site.js (drawer, "On this page", search, FAQ filter, adapted from documentation-site's script.js), and search-index.js (generated; loads when search first opens).
- A "Skip to content" link (Question 8) and the 💰 favicon.
- `_sources/templateinterface/`: a snapshot of the template files used, at ed840da.

#### Changed

- The Python scripts moved from `tools/` to `scripts/`, since the Tools section's pages live in `tools/`. The docs' references were updated; older patch notes keep the old paths.
- scripts/check.py: skips `assets/` and `scripts/`; the em dash check now fails only on an em dash used as punctuation (followed by a word), so a lone dash standing for a missing value, as the screener shows, passes; inventory items in the source sites' own navigation (region nav or aside) are skipped, since the shell replaces that navigation. The literal em dash left in the script was replaced with its escape.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.7.0 - 2026-10-02 - Host: a new invests repository; stocks stays the data source

#### Added

- None.

#### Changed

- D21 changed: the stocks repository is not renamed. The site lives in its own new `invests` repository with no data feeds; stocks keeps its workflows and data and serves them at azqato.github.io/stocks/data/ (same origin as the site). The earlier D21 text and P9 note are kept, marked as superseded.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.6.0 - 2026-10-02 - Host: the renamed stocks repository

#### Added

- D21: at publish time the stocks repository is renamed to `invests` and becomes Azqato Invests, keeping its data workflows, data and history; a new `stocks` repository holds the redirects. P9 step 1 lists what to check before the rename.

#### Changed

- None.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.5.0 - 2026-10-01 - The remaining open questions answered

#### Added

- Development plan step P7.10: the author reviews the drafted sections once the MVP is ready (Question 15).

#### Changed

- Answered Questions 1, 4, 7, 11, 13, 14 and 15 (recorded in PRD.md). The site will be a GitHub Pages project site at azqato.github.io/invests/ from a public repository named `invests` (D4 updated, old text kept; P9 now checks the collision with invests.html first). HFEA links to its Composer Atlas community entry. Permission requests go to the repository's issue tracker. Traffic is measured only by host counts and search consoles. What's being merged now names alert-on-failure.yml (Documentation Versus Reality entry 3 resolved). Em dashes in moved text are replaced and logged, and tools/check.py now fails on them. The drafted sections wait for review after the MVP.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.4.0 - 2026-10-01 - Development plan P0 and P1: setup, snapshots and inventories

#### Added

- A local git repository (branch `main`, no remote, nothing pushed), with `.gitattributes` pinning LF line endings and `.gitignore` excluding `_sources/`.
- tools/snapshot.py: downloads read-only copies of the source pages, their scripts and stylesheets into `_sources/` and records each commit. First snapshot: stocks 60a599e (12 files), vix cd92561 (8), leverage c86321c (9), azqato.github.io 58767b5 (invests.html).
- tools/inventory.py and inventory/: one inventory per source page, 20 in all, 2,898 items, listing every heading, paragraph, list item, table row, link, control, chart and script in page order with its full text. A check confirmed all 4,096 visible text fragments of the source pages are in the inventories.
- tools/check.py: read-only checks for titles, links, template demo text, em dashes and inventory coverage. Tested against planted failures.

#### Changed

- Answered Questions 2, 3, 5, 6, 8, 9, 10 and 12 (recorded in PRD.md): keep azqato.com's nav (D9 confirmed), section-folder addresses, a local git repository, "Azqato Invests" as the brand, add a skip link, the site's own themes on Home, remove the template's remaining demo parts, and add an integrity hash to Chart.js.
- Findings from P1 recorded: the stocks fallbacks are relative `data/` paths, and azqato.github.io/stocks/data/ can replace them (Background findings, Documentation Versus Reality entry 8); the screener and Market Overview insert feed values with `innerHTML` unescaped (Security); the tools' data colors and the VIX charts' labels (DESIGN.md); 28 visible em dashes in source text (Question 14).
- Milestone M3 complete; M4 in progress. Folder structure, Repository Hygiene, Browser Testing and the Runbook's common errors updated.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.3.0 - 2026-10-01 - Step-by-step development plan

#### Added

- A Development plan in PRD.md's Roadmap, at the author's request: phases P0 to P11 mapped to milestones M3 to M11, each with what it needs first, numbered steps and substeps, and what "done" means. It covers setup and the blocking questions, source snapshots and page inventories, the shell, each section's pages, the tools and their data, site-wide checks, documentation, the publish plan, publishing and the redirects, and the correction pass. It proposes a folder layout pending Question 3.

#### Changed

- None.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.2.0 - 2026-10-01 - First documentation audit: the doc set, and README as the front door

#### Added

- docs/PRD.md: the whole plan from README.md, moved word for word by script (core rule, decisions D1-D20, site map, sources, Composer Atlas, background findings, assumptions, next steps and points to settle), plus every section the documentation prompt requires, from the problem statement to the FAQ. Its Risks and Open Questions section lists 15 numbered questions, each with the default applied meanwhile. Sections the audit drafted (tenets, personas, user stories, goals, success criteria, metrics, press release, FAQ) say so.
- docs/DESIGN.md: the design details and template ratings from README.md, moved word for word, plus the design system read from Template Interface at commit 61acfcb: both palettes with every token's use, typography, spacing, breakpoints, components, accessibility (with contrast ratios measured by script) and motion.
- docs/PATCHNOTES.md: this file.
- docs/TODO.md: the ideas file, with its placeholder only.
- LICENSE.md: all rights reserved, with the AI and search referencing carve-out, no waiver, no warranty, and not financial advice.
- Defaults adopted where the project had no rule, recorded in PRD.md: writing style, browser testing, verification environment, testing cadence, repository hygiene, licensing, social sharing tags, page titles, and deprecation and removal for this site's own pages.
- The audit's date and process, under Documentation audits in PRD.md.

#### Changed

- README.md rewritten as the public front door: what the site is, a plain statement that there's no hosted instance yet (with links to the four current sites), what it will offer, who it's for, status, the core rule in short, and links to the docs. Two lines of the old README weren't moved and are kept here. Its opening line read:
  > Project plan for Azqato Invests: one site, in its own repo, that merges the stocks, vix and leverage sites with the current invests.html page, built on the documentation-site template.

  Its status line read:
  > **Status: paused (2026-10-01).** Planning is done apart from the points the move to an independent repo reopened (see To settle). The documentation prompt is approved but was stopped partway, before it wrote anything; it reruns for the independent repo when you say to resume. No site files exist yet.
- Headings changed in the move: "Assumptions (correct any that are wrong)" became "Assumptions", with "Correct any that are wrong." as its first line; "Next steps" became "Next steps (from the plan)" under the Roadmap; the "To settle along the way:" list sits under Risks and Open Questions.
- Next steps 1 and 2 of the plan are done (resume; move the plan into docs), as noted in the Roadmap.

#### Fixed

- None. The writing-style sweep of README.md, the only text file before the audit, found 0 em dashes, 0 `&mdash;` entities and 0 double hyphens used as punctuation. The new files were swept the same way after writing, with the same result outside the rule text that names the character.

#### Removed

- None. No plan content was removed: a script copied each part of the plan from the original file, and a check confirmed every non-empty line of the old README.md is in PRD.md or DESIGN.md, apart from the two lines quoted above and the headings listed under Changed.

### Invests v0.1.0 - 2026-10-01 - The plan

Reconstructed by the 2026-10-01 audit; the folder has no version history.

#### Added

- README.md with the project plan: the core rule (preserve everything), the decisions, the 21-page site map, the Composer Atlas mapping, the four sources being merged, background findings, assumptions, next steps, points to settle, and ratings of all 21 Template Interface templates.
- D20: everything stays local until the author says otherwise.

#### Changed

- The plan was corrected for the move to an independent repo: D4 and D5 changed (their old text kept after "Before:"), D8 now says the design comes from Template Interface rather than azqato.github.io, D9 and the dark-mode assumption were marked to re-check, and the design details, background findings, next steps and points to settle were updated to match.

#### Fixed

- None.

#### Removed

- From the points to settle: where this site's docs live in the azqato.github.io repo, moot once the site became its own repo. The design detail about extending azqato.github.io's tools/build-nav.py to pages in an `invests/` folder was replaced by one saying this site would carry its own copy of the nav, if D9 stays.

## Azqato's Prompts history (v1.0.0 to v1.112.0, before the move)

Azqato's Prompts' own PATCHNOTES.md from the archived Azqato/prompts repository, merged word for word (merged 2026-10-12); headings moved down a level and version headings prefixed "Prompts". Its versions were a separate line; from 2.19.0 prompts changes are main entries above. File names here (`prompts-data.js`, `p/`, `docs/PRD.md` and so on) mean that repository's files; the current process is in `codes/prompts/docs/PRD.md`.

All notable changes to this project are documented here. Entries are listed in reverse chronological order. Each version entry includes the version number, date, and a summary of what changed.

---

### Prompts v1.112.0 - 2026-10-07

Updated by: Claude (Opus 5.5), at the author's request.

#### Added

- E-commerce Site prompt (`prompts/ecommerce-site.md`, share page `p/ecommerce-site.html`). It builds a landing page, a filterable catalogue, product pages, and a cart drawer from one product data file. Every feature is described in the prompt itself: sold-out options kept visible and labelled, delivery and returns under Add to cart, a free-delivery threshold in the cart, removable filter chips, and where focus lands after each action. It asks about the shop first, never invents proof, keeps payment keys in environment variables, and shows a plain notice instead of checkout when no provider is chosen.
- README line, mirror, sitemap. PRD Future update 25; DESIGN 1.15.2 (focus-stop count).

#### Notes

Combined from three of the author's wireframe templates (E-commerce Product Page, Landing Page, E-commerce Storefront), chosen from a rating of the whole library. Readers cannot see the templates, so nothing in the prompt refers to them. Checked against the Prompt Content Rules: no push or publish instruction, and no account of the author's.

---

### Prompts v1.111.0 - 2026-10-04

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Brand Identity, Phase 3: after the render checks it builds `brand/concepts/index.html`, a page that shows every concept side by side on light and dark, with the lockup, the symbol at 16, 32, and 96px, a one-line intent, and a link to the render check. It gives the page's path before asking for a pick, and adds any new concept or color variation asked for at the pick.
- PRD Future update 24.

#### Notes

Found in the M21 test run on Template Interface (v0.18.0 there): the prompt asked for a pick with no way to see the concepts together, and the author asked for one. The full run otherwise worked as written: all eight phases, the offline Brand Design page, and a 14-slide deck that passed its checks. Checked against the Prompt Content Rules: no push or publish instruction, and no account of the author's.

---

### Prompts v1.110.0 - 2026-10-04

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Brand Identity gains Phase 8: `brand/index.html`, a committed client deck that presents the whole brand project in a consulting style. It is 16:9 slides with action titles, section trackers, footers, and source lines, with a switch to a scrolling report view and one slide per printed page. Fourteen slides run from the title and executive summary to next steps and an appendix, all drawn from the docs and `brand/`. It links to `presentation.html` and never to the uncommitted offline Brand Design page. It ends on a headless Edge check of both views. The description now mentions the deck (141 characters), and the intro paragraph says eight phases.
- README's Brand Identity line mentions the deck. PRD Future update 23.

#### Notes

From the author's Template Interface TODO list, item 2 (2026-09-27), with their answers on 2026-10-04: a separate front page rather than a replacement for `presentation.html`, both a deck and a report view, committed, and tested by running the prompt on Template Interface. Checked against the Prompt Content Rules: no push or publish instruction, and no account of the author's.

---

### Prompts v1.109.0 - 2026-10-03

Updated by: Claude (Opus 5.5), at the author's request.

#### Added

- SEO Audit, the twenty-third prompt. It measures a built site against the technical search checklist (rendering, robots.txt, sitemap, noindex, redirects, 404s, canonicals, titles and descriptions, one H1, structured data, breadcrumbs, orphan pages, images, Core Web Vitals), shows a plan and waits for a yes, fixes what code can fix, reruns every check, and lists what only the reader can do. Description 145 characters. Checked against the Prompt Content Rules: it forbids committing, pushing, and deploying, and names no account of the author's.

#### Changed

- README lists the new prompt. PRD counts and Future update 22; DESIGN.md's focus-stop count (1.15.1).

#### Notes

From a pasted post listing twenty SEO fixes. Two facts were checked by web search on 2026-10-03, because they postdate or may postdate the model's training: Google retired FAQ rich results for all sites on 2026-05-07 (FAQPage markup is still read but earns no rich result), and the Core Web Vitals thresholds are LCP 2.5s, INP 200ms, and CLS 0.1. The post's "load in under 2 seconds" and "add FAQ schema" were adjusted to match.

---

### Prompts v1.108.0 - 2026-10-03

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Condense Docs prompt, revised from its first run (v1.107.0):
  - A new step 0 makes the pass undoable. It checks git status, records the starting commit, and stops if a doc has uncommitted changes. It never commits, stashes, or resets. Outside git, it copies the docs elsewhere first. The report says how to review or restore each file. The author suggested this.
  - Read finds the docs' own rules about keeping history (keep resolved rows, never delete, completeness first) and raises each as a question. On this site three such rules were found only by chance.
  - Read also runs the scripts that read the docs and saves their counts, to compare afterwards.
  - The ledger allows one row for a repeating pattern, with its count. It adds "dated audit result" as a kind.
  - It treats a version table that repeats the changelog as a duplicate.
  - It lists instructions that write to a structure being removed, and updates them. Ones in files it must leave alone become questions.
  - A standing question asks whether conflicts are fixed to what the code shows. With a yes, it may read just enough code to settle a number.
  - Proof gains three checks: every version in removed history has a changelog entry, section references resolve across documents, and term matching ignores case.
  - The report adds the undo commands and each file's difference from its estimate.
- Documentation prompt: "update afterwards (patch notes, version history)" now says "(patch notes, and the version line)". It never required a version table; this site's PRD did.
- `js/prompts-data.js` resynced.

---

### Prompts v1.107.0 - 2026-10-03

Updated by: Claude (Opus 5.5), at the author's request.

The first run of the Condense Docs prompt on this repository. The docs were condensed and nothing was removed: every cut passage was mapped to where its information lives, and a script checked each one.

#### Changed

- `docs/PRD.md` 45,500 words to about 26,000. Sections 18 and 19 keep only open items; their resolved rows and answered questions are recorded in the patch notes of the releases that resolved them. Section 27's built Future updates and finished Scoped sections keep their titles, `**Built in vX**` lines, differing decisions, and sources; the full proposals are in their releases' patch notes. Section 36 is now a link to this file instead of a table repeating it, and section 30's folder tree a link to section 13's. About sixty "since vX" phrases became present-tense statements.
- Three project rules changed, on the author's answers: tenet 4 and section 18 no longer keep resolved rows; section 19 removes an answered question once it is folded in; section 33's "Completeness beats brevity" became "Every fact kept once, in its home". Releases now bump the PRD version line instead of adding a version history row.
- `docs/DESIGN.md` 1.15.0: history phrasing moved here, two "Corrected in v1.28.0" paragraphs and a duplicated bullet removed.

#### Fixed

Seventeen conflicts between copies, each resolved to what the code shows: search described as absent in PRD sections 5, 21, 26, and 35; share pages 29 lines, not 21; `index.html` 56 lines, `css/style.css` 676, `js/script.js` 470; section 30's tree of 52 files and 18 prompts (63 and 22); the mirror called hand-maintained and unenforced; twenty-six focus stops, not fourteen; section 10b's 21 strings; "mandatory" browser checks after every change in PRD 29 and DESIGN 12c, against section 20; section 14 saying DESIGN does not describe the error view; section 16's "four places" and "exactly four files"; the stale debt row on DESIGN's template; DESIGN's two `.sidebar-nav` max-heights (`100dvh - 140px`) and its old Copy `aria-label`; and the README calling the Documentation prompt a whole-codebase read.

---

### Prompts v1.106.0 - 2026-10-03

Updated by: Claude (Opus 5.5), at the author's request.

#### Added

- Condense Docs, the twenty-second prompt. It shortens a project's documentation without losing information: docs describe the present, each fact lives in one place with links from the others, history moves to the changelog, finished roadmap items become a short Done list, and the reasons behind decisions stay. Before removing anything it shows a ledger of every cut passage and where its information will live, and waits for a yes; afterwards a script checks every row. Kept separate from the Documentation prompt, which checks the docs against the code.

#### Changed

- README lists the new prompt. PRD counts and Future update 21; DESIGN.md's focus-stop count (1.14.1).

---

### Prompts v1.105.0 - 2026-09-30

Updated by: Claude (Opus 5.5), at the author's request.

#### Added

- `tools/dashboard.py` builds this repository's progress dashboard from its sources, with the standard library only. Steps, questions, and stuck items come from the new `dashboard/state.json`; the latest results from git; the latest release from this file; the roadmap from PRD section 27. `tools/dashboard.css` holds the styles it inlines.
- The dashboard's Roadmap now shows everything: every milestone with its scoped findings, every Future update, every deferred item, and every verification checklist row, with completed items dimmed.
- A "May be stale" banner, shown by one small inline script when no progress has been recorded for 30 minutes and the task is not finished.
- Under each section, the source it reads. A source that cannot be read is named rather than shown as empty.

#### Changed

- The Progress Dashboard prompt is rewritten around a generated page: one source per section, a small generator in the project's own language, atomic writes only on change, honest times (last recorded in the top bar, generated in the footer), the stale banner, the full roadmap, folding any existing status page in, and a verify step. New description and intro.
- `CLAUDE.md`: the dashboard rule now says to update `state.json` and run the generator after every step, and never edit the page by hand.
- PRD sections 13, 20, and 27; Future update 20 added.

#### Fixed

- The dashboard never highlighted the step in progress: the page used a class the stylesheet did not define.

---

### Prompts v1.104.0 - 2026-09-29

Updated by: Claude (Opus 5.5), at the author's request.

#### Added

- Search. With twenty-one prompts the list was no longer quick to scan, so a search box now sits at the top of the prompt list, and inside the Prompts menu on phones.
  - It filters the sidebar links, and the home cards when the home view is showing, by title and description as you type. Every word must appear, in any order and any case.
  - Enter opens the first match. Escape clears the box, and a second Escape closes the phone menu.
  - With no match, "No prompts match" is shown and announced to screen readers.
  - The query is kept while you move between prompts, and not saved across a reload.
- PRD section 10b describes it.

#### Fixed

- The Prompts menu chevron added in v1.99.0 animated its rotation, which DESIGN.md section 12b forbids (only color, border, background, and opacity may transition). It now flips instantly.
- DESIGN.md's focus-stop count below 1024px, which said four with the menu closed; it is three.

#### Changed

- PRD: open question 11 answered; the Search milestone complete; the non-goal on search reversed; the prompt-count metric has no fixed ceiling; the FAQ, feature list, and line counts updated. DESIGN.md 1.14.0.

---

### Prompts v1.103.0 - 2026-09-29

Updated by: Claude (Opus 5.5), at the author's request.

#### Added

- LinkedIn Audit prompt, the twenty-first, with its share page, built from a post of seven LinkedIn prompts the author pasted. The seven are merged into one run written to a single offer:
  - it asks for the profile (LinkedIn's "Save to PDF" export, or pasted text) and the offer, audience, proof, and posting rate, and never signs in to LinkedIn or fetches the profile;
  - it scores photo, banner, headline, about, featured, experience, and recommendations out of ten against tests fixed before scoring, lists what confuses a stranger, and names the one fix that matters most;
  - it then writes ten headlines (the best three explained, one to test first), an about summary, three featured items, experience bullets that start with a result, a banner line, twelve post ideas over four weeks with a comment strategy, and two recommendation requests;
  - it uses only results the person gives, leaves `[number]` placeholders rather than inventing figures, counts character limits (220, 2,600, 2,000) by script, and ends with a scorecard table and the counts.
- PRD Future update 19 records it, and open question 11 asks whether to build search now that the library passes roughly twenty prompts.

#### Changed

- README lists the new prompt. PRD prompt and file counts updated (twenty-one prompts, 58 files). DESIGN.md 1.13.2 updates the focus-stop count to twenty-four on a wide screen.

---

### Prompts v1.102.0 - 2026-09-29

Updated by: Claude (Opus 5.5), at the author's request.

#### Added

- Project Defaults prompt, the twentieth, with its share page. It gives a project the Documentation prompt's rules and structure in one quick pass, without reviewing the code or the existing documents:
  - creates /docs, the four documents, and docs/TODO.md where missing, with every required section as a heading and the line "Not yet written. A Documentation run fills this in.";
  - writes the standing policies into the PRD (writing style, browser testing, verification environment, testing cadence, repository hygiene, licensing, sharing tags and page titles for a site, deprecation and removal, working practice) plus a verification checklist;
  - adds robots.txt, LICENSE.md, and sitemap.xml only where missing and where the conditions allow.
- The project's own rules and documents are the source of truth: existing text is never changed, documents are never moved or merged, and every clash with a default is listed as a numbered question.
- It fetches the Documentation prompt for the exact wording of each default, so the defaults are kept in one place.
- PRD Future update 18 records it, built in this version.

#### Changed

- README lists the new prompt. Prompt counts in the PRD updated to twenty, and DESIGN.md 1.13.1 updates the focus-stop count (twenty-three on a wide screen, four below 1024px).
- PRD section 30: the markup row's line counts corrected (`index.html` 52 lines, share pages 29 lines).

---

### Prompts v1.101.0 - 2026-09-29

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Every share page gives AI agents clearer instructions. The old line ended "and follow it", which an agent could read as "run it now", against the Copy button's "ask if I would like to run it". The body now:
  - shows the prompt's description beside its title, since fetch tools drop the head where the description lived;
  - says the page only links to the prompt, and gives the one raw Markdown URL;
  - says to read the prompt in full and word for word, and to use curl if the fetch tool summarizes or shortens pages (Claude Code's passes pages through a small model);
  - says the prompt is the code block under "## Prompt", and the text above it is for people;
  - says to do what the person asked, and ask before running it if they have not said to.
- Checked with Claude Code's own fetch tool against the live Launch Video page: the head tags were dropped and the body text, with the URL, was kept.
- `tools/prompts-mirror.py` writes the new text; all nineteen share pages resynced. PRD sections 13 and 32a updated.

---

### Prompts v1.100.1 - 2026-09-29

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Documentation prompt: removed "Fetch the full prompt first, in case this one was cut off: …" from the end of its opening paragraph. Since v1.100.0 the Copy button sends Claude to the prompt's page, which links the full raw Markdown, so the line is no longer needed.

---

### Prompts v1.100.0 - 2026-09-29

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- The Copy button on every prompt copies a short pointer instead of the full prompt text. There is no full-text option, since every tool these prompts are used with can fetch a page. For Launch Video it copies:

  `Review the full prompt on this website, provide a summary of what it does and then ask if I would like to run it: https://azqato.github.io/prompts/p/launch-video.html`

  The link is the prompt's public share page, so the person pasting it can see it goes to this site. The agent fetches that page and follows the raw Markdown link it names (v1.98.0). The link always uses the live address, even when the site is opened from disk.
- `js/script.js`: new `SITE_URL`, `COPY_POINTER`, and `publicUrl()`; the button's `aria-label` and failure text updated. The home page intro and README describe the new behavior.
- Launch Video prompt: the video, plan, and share copy now go in a `brag/` folder rather than `brag-output/`. If /brag has no option for the folder, Claude renames `brag-output/` to `brag/` when it finishes.
- PRD section 10 records the pointer format as the rule for every prompt; sections 4, 13, and 23 follow. DESIGN.md 1.13.0, section 7.

---

### Prompts v1.99.0 - 2026-09-29

Updated by: Claude (Opus 5.5), at the author's request.

#### Fixed

- On phones and tablets the prompts were hard to read because the navigation filled the screen. Below 1024px the sidebar became a sticky top bar that wrapped all nineteen prompt links, so it grew with every prompt added and stayed pinned over the text. Measured in headless Edge at 477px wide, the bar was 398px tall and the prompt heading began 418px down.
- The prompt list is now a menu. The top bar holds the logo, a **Prompts** button, and Support, and is 65px tall at every width below 1024px. The button opens the list beneath the bar as one column that scrolls inside itself; picking a prompt or pressing Escape closes it. The button carries `aria-expanded` and `aria-controls`.
- Found by running the site's Mobile Responsive Audit prompt at 375, 700, 900, 1023, 1150, 1440, and 1920px. No width had horizontal overflow before or after, closed or open, and nothing changed at 1024px and above.

#### Changed

- `index.html`, `js/script.js` (`setMenuOpen()`, `initMenu()`), and the 1023px block of `css/style.css`.
- DESIGN.md 1.12.0: sections 7 and 9 describe the menu. PRD: Future update 17, built; sections 4, 13, and 23 updated.
- docs/TODO.md reset; its "fix mobile" idea became Future update 17.

---

### Prompts v1.98.0 - 2026-09-29

Updated by: Claude (Opus 5.5), at the author's request.

#### Fixed

- AI agents could not read a prompt from its share page. `p/<slug>.html` forwards to `index.html#/<slug>`, where JavaScript loads the prompt, and an agent's fetch runs no JavaScript; the `.md` files are not on Pages either. Every share page now points to the prompt's raw Markdown on GitHub (`main`), in two places:
  - in the head, a `<link rel="alternate" type="text/markdown">` right after the meta description;
  - in the body, a visible line: "AI agents: fetch the prompt as plain Markdown at <URL> and follow it.", since text-converting fetch tools drop head tags.
- People in a browser are still forwarded to the prompt as before.

#### Changed

- `tools/prompts-mirror.py` builds the raw URL from each prompt's slug and writes both links; all nineteen share pages resynced.
- PRD section 32a records the rule; sections 13 and 20 updated.

---

### Prompts v1.97.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Added

- Prompt Writing prompt, the nineteenth: it writes a new prompt, or reviews one already in use, against ten rules drawn from how language models work, then explains each change in a line and offers to try the prompt once on a real case.
- PRD section 11, Prompt Writing Rules: nine rules for every prompt (facts from the context, not memory; investigate before concluding; exact work goes to tools; a way to say "I don't know"; show the output's shape; end on a check that can pass or fail; scoring that cannot be gamed; a focused prompt; and supplying what a model cannot know about itself). Section 12 step 3 now checks them.
- PRD section 20, Reference notes: the author's notes on a video about how language models are built, the source of the rules. The file stays local, excluded through `.git/info/exclude`, so it is never published.
- PRD Future update 16 records the work, built in this version.

#### Changed

- Audited all eighteen existing prompts against the new rules. Thirteen already met them. Five were tightened:
  - Add Prompt: ends by running the project's checks and saying which passed, with length limits counted by script.
  - GitHub Wiki: a new Step 5 checks by script that every link between pages resolves and every page is in the sidebar, reports what changed and what could not be checked, and says not to push the wiki.
  - Mobile Responsive Audit: ends with a report of every width and page checked, the measurements, the fixes, and the gaps.
  - Brand Identity: contrast ratios are computed with a script from the hex values, not estimated.
  - Documentation: title and sharing-tag lengths are counted by script, and patch-note dates come from the system clock.
- DESIGN.md section 10: focus-stop count updated for nineteen prompts (twenty-two stops). DESIGN.md is now 1.11.10.
- docs/TODO.md reset to its empty placeholder; its one idea became Future update 16.

---

### Prompts v1.96.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Documentation prompt: description and intro rewritten in plain, benefit-first language: what running it gives you (a project anyone can pick up, four clear documents, your own rules and ideas kept, defaults only where nothing is decided, no extra cost on a large project), in one paragraph instead of four long, technical ones.
- Documentation prompt: less weight on TODO.md at the start. The intro now mentions it in one clause; steps 2 and 5 no longer name it (step 5's closing sentence about TODO questions and discrepancies is removed); and the survey paragraph only name it and point to its section. The details (never consolidated or moved, moving a list kept elsewhere, not acting on ideas during the audit, reporting whether it was read) now live in the `/docs/TODO.md` section.
- Documentation prompt: the "Fetch the full prompt first" sentence now ends the opening paragraph, in the author's wording, instead of standing above it.
- Documentation prompt: removed the progress dashboard. Its folder-structure line and its ignore-file rule are gone, so the prompt sets documentation defaults only. It also no longer adds a Roadmap entry proposing a dashboard, nor keeps a separate rule for an existing dashboard section in CLAUDE.md.
- Progress Dashboard prompt: now carries the two rules moved out of the Documentation prompt: the dashboard is never added to an ignore file, and where the project's docs describe its folder structure, dashboard/ is listed there as a project file that is never merged into the docs. Its standing rule is also recorded in the PRD's working-practice section where there is one, and an existing rule in CLAUDE.md is left as it is.

---

### Prompts v1.95.1 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Documentation prompt: the fetch-first instruction is now one sentence: fetch the full prompt first, in case the pasted one was cut off, with only the raw file linked. The `blob` link and the fallback wording are gone.

---

### Prompts v1.95.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Documentation prompt: pasting it into Claude Code could cut it off, since it is about 70 KB. Its first line now tells Claude to fetch the full, latest version from `https://raw.githubusercontent.com/Azqato/prompts/main/prompts/documentation.md` (the raw form of `https://github.com/Azqato/prompts/blob/main/prompts/documentation.md`, which is also named), follow the fenced block under its "## Prompt" heading, and prefer it wherever it differs from the pasted text. If the fetch fails, Claude carries on with what was pasted and says at the start of its summary that it may be incomplete and where the pasted text ended. The intro explains why.

#### Notes

The raw address is used first because the `blob` address returns GitHub's web page around the file rather than the file itself. The prompt now depends on `prompts/documentation.md` staying at that path on `main`, so renaming or moving it should be treated like retiring a public address.

---

### Prompts v1.94.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Brand Identity prompt: it now begins with a read-only pass. Claude reads every markdown documentation file in the project in full (README, CLAUDE.md, PRD, DESIGN, patch notes or changelog, and any other `.md` that describes the project, skipping dependency folders and build output) to understand the current state of the site, without creating, editing, or moving anything and without asking questions yet. It notes what bears on the brand: the product, audience, tone of voice, existing logo, colors, fonts, tokens, and style rules, the site's current look and pages, past design decisions and their reasons, anything that must not change, and the project's working rules. Disagreements between documents are noted, not resolved. It summarizes its findings with the file each came from, and Phase 1 builds on that summary instead of re-reading the same files.
- The intro describes the pass.

---

### Prompts v1.93.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Brand Identity prompt: the Brand Design page's "What it shows" gains a fourth section, **Other brand images**, so nothing made over time is missed, including files from an earlier run of the prompt or from other work. It looks through the rest of `brand/` (concepts, mockups, the guidelines PDF, the presentation) and the site's own asset folders for logos, symbols, wordmarks, favicons, app and touch icons, share images, social banners, and web manifests, skipping dependency folders, build output, and caches. It lists only files that exist now, grouped by where they live, with each file's path shown. On the gated page these files are copied into the build under `brand/other/`, so the file handler still accepts only paths inside the brand folders.

---

### Prompts v1.92.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Brand Identity prompt: the Brand Design page is now always built, with no question at the end. Its form depends on the site:
  - A site with a signed-in area for internal pages: the gated page as in v1.91.0, behind the same access check, with the protected file handler and its tests.
  - A public site with no way to restrict a page, or no site at all: an offline page, `brand/brand-design.html`. It is one self-contained file that opens by double-click and links to each file by relative path. It lists the files as they were when written, since a page opened from disk cannot read its folder; running the phase again refreshes it. It uses the new brand's own palette. It is added to `.gitignore` (creating the file with only that line if there is none), so it is never committed or published, and it is checked opened from disk and absent from `git status`.
  - Claude says which form it chose and why.
- The intro, the scope rule, and the README describe both forms. The prompt now has seven phases.

---

### Prompts v1.91.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Brand Identity prompt: a new optional Phase 7 adds a Brand Design showcase page to the reader's site, so their team can preview, open, and download every file in `brand/` without opening the repository. It runs only if the reader says yes, since it is the one part of the prompt that changes the project; the scope rule and intro say so.
  - Placement: next to the site's other internal pages, behind the same access check. If the site has no protected area, it asks where to put the page rather than making brand files public.
  - Content: one section per brand folder (logo system, brand kit, render checks), each a responsive grid of 150px preview tiles with open and download links. Files meant for dark backgrounds preview on the brand's dark color. Files are read from disk on each request, so new ones appear without code changes.
  - Safety: files are copied into the build output and served through one protected handler that accepts only paths inside the brand folders and returns 404 for anything else, with tests for an empty path, an outside path, `../` traversal, a lookalike `brandx/` folder, and a missing file.
  - Styling uses the site's own tokens and works at phone width. It finishes by updating the project's PRD, patch notes, and README, and by a local headless browser check, including that a signed-out visitor is refused.
- The specification named one framework's handler syntax and build folder; the prompt keeps those as examples so it works on any stack.
- README: the Brand Identity description mentions the optional page.

---

### Prompts v1.90.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- `CLAUDE.md` default rules: headless Edge stays for local checks, with one named exception, a single load of a link a `docs/TODO.md` idea points to when the web fetch tool cannot read it, never signed in. Open question 10 is answered, and PRD section 20 matches.
- Roadmap: the skip-to-content link and copy-result live region are scheduled for the next session. Search keeps its trigger of roughly twenty prompts (eighteen today).

---

### Prompts v1.89.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Added

- **Frontend References**: a setup prompt that writes a standing "Frontend references" rule into CLAUDE.md, at user scope (recommended) or for the current project. Claude uses seven outside references only when building a new page, when told something looks bad, or when one is named: a DESIGN.md from Refero Styles or awesome-design-md for style, Component Gallery (and, optionally, 21st.dev) for components, Kinetics for motion, whatships and HyperFrames for demo videos, and Impeccable for a final pass. The project's own design system comes first; nothing is installed or called without asking; nothing is filled in from memory; each site is dated 2026-09-28 with what its terms allow. Future update 15.

#### Changed

- PRD section 21: prompts may name third-party sites they use directly as a resource. A list of links for browsing is still out of scope. This supersedes the earlier reading in update 3.
- README, PRD, and DESIGN counts updated for eighteen prompts and 52 files.

---

### Prompts v1.88.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Roadmap: the new idea in `docs/TODO.md`, a list of eight frontend reference sites, is researched and proposed as Future update 15: a Frontend References prompt that writes a standing rule into CLAUDE.md, with the reuse terms each site states, a choice of user or project scope, and three open questions. It is a proposal; nothing is built.
- `docs/TODO.md` is back to its placeholder, since the idea now lives in the Roadmap.

---

### Prompts v1.87.0 - 2026-09-28

Updated by: Claude (Opus 5.5), at the author's request.

Five new prompts and two improvements, adapted from Meng To's `mengto/skills` repository (MIT licence). Each is written in this site's own words, with the parts tied to Codex, to one person's accounts, or to committing and pushing left out.

#### Added

- **Design Review**: a read-only review of a site's design. Every finding cites the exact element, is classed as a quality defect or as decoration with no job, and is ranked P0 to P3; the fix is removal first. No AI-authorship guesses, no taste score, no redesign.
- **Video to Prompt**: reads a screen recording with ffprobe and ffmpeg, frame by frame at each beat, and writes one prompt detailed enough to rebuild it, including mobile and reduced-motion behavior. Uses stitched viewport captures for full-page stills.
- **Score to Target**: an anchored rubric written before scoring, items scored separately from real evidence, and rounds of fixes until every item reaches the bar, with no rounding up. Independent judging is optional.
- **Animation Performance**: measures offscreen CSS animations and canvas or WebGL loops at several scroll positions, pauses what is offscreen, fixes leaks in cleanup, and re-measures. Commits nothing.
- **Landing Page**: landing and pricing modes. Asks for the one action, audience, objections, and real proof, then writes the outline, copy, FAQ, and indexing advice. Missing proof stays a marked placeholder.

#### Changed

- Brand Identity: concepts and the brand kit are checked for one focal point, a job for every effect, and nothing that could be pasted onto an unrelated brand.
- Mobile Responsive Audit: screenshots are taken before, at the key moment, and after in the same framing, looked at before being trusted, and labelled as phone-width browser checks rather than device tests.
- README, PRD sections 13, 18, 21, 27, and 30, and DESIGN section 10 updated for seventeen prompts and 50 files.

#### Notes

Seven more of the repository's ideas were considered and left out: skills that commit and push (section 11 forbids it), one that manages several sessions, ones tied to the author's own accounts or game, and about seventy style cards and effect recipes, which are parts for a build rather than prompts.

---

### Prompts v1.86.0 - 2026-09-27

Updated by: Claude (Opus 5.5), at the author's request.

#### Changed

- Documentation prompt: says how to handle CLAUDE.md. Claude Code loads it automatically only from the project root (or `.claude/CLAUDE.md`), so an audit that folded it into the PRD would silently drop the project's rules. It is now a Project File: kept at the root and never consolidated, moved, or deleted. Each of its rules is recorded in the PRD's Working Practice, with a line saying CLAUDE.md is the copy Claude reads and that the two change together, and any difference between them is flagged under Questions rather than resolved. A CLAUDE.md that is a single `@docs/CLAUDE.md` import is accepted where it exists but never created unprompted, and the audit creates no CLAUDE.md unless its own rules need one.
- Documentation prompt: CLAUDE.md added to the folder tree and to the list of files that stay at the root; the intro and the Working Practice spec mention it.
- Launch Video prompt: rendering now defaults to Hyperframes' own Chrome headless shell, installed (after asking) into the Hyperframes cache with `npx hyperframes browser ensure`, and never the Chrome or Edge already on the machine. The prompt checks with `npx hyperframes browser path` that the renderer points into that cache, and stops rather than rendering with a system browser. Edge was tried and does not work, so the prompt says not to substitute it. The pinned build also keeps the rendered video the same on every machine.
- This repository: `CLAUDE.md` gains a Default rules section (no subagents; headless Edge only, for local checks; no state-changing checks against production; fetch and check docs/TODO.md before pushing; update the PRD and patch notes after every change). PRD section 20 records it.

---

### Prompts v1.85.0 - 2026-09-27

#### Changed

- Roadmap: Search moved from Deferred to a planned milestone. The trigger stays the same: it will be built when the library passes roughly twenty prompts (twelve today).

---

### Prompts v1.84.0 - 2026-09-27

Builds Future update 7 from the ideas list: a prompt that uses the `latent-spaces/brag` repository directly instead of any version of it written here.

#### Added

- `prompts/launch-video.md`, the Launch Video prompt, with its share page `p/launch-video.html`. It installs the open-source `/brag` Claude Code plugin once and runs it to make a launch video of the reader's project, with music, sound effects, and share copy, in a `brag-output/` folder. It builds no video pipeline of its own and copies none of the plugin's files.
  - Full workflow, at the author's choice: it always runs `/brag --full`, because on Opus 5.5 `/brag` otherwise switches itself to the lighter `/brag-slim`. It checks for Node.js 22 or newer, ffmpeg, and the Hyperframes command line, and asks before installing anything missing.
  - Installed at user scope, at the author's choice, so every project on the machine and any other prompt can use it without installing it again. Claude runs `claude plugin marketplace add latent-spaces/brag` and `claude plugin install brag@brag` (user scope is that command's default), or, where it cannot run the `claude` command, gives the reader the two `/plugin` commands and the scope to choose. The commands were checked against the Claude Code plugin documentation rather than recalled.
  - It says how to update the plugin, since plugins from third-party marketplaces do not update themselves, asks once for tone, format, length, music, sound effects, voiceover, and title with defaults drawn from the project, and asks whether `brag-output/` should be kept out of version control.
  - Audited against PRD section 11: no push, commit, or publish instruction, and no reference to the author's accounts. Naming the plugin's public repository is the point of the prompt and takes no action on any account.
- The README lists it.

#### Changed

- Motion Design prompt: its introduction points to Launch Video for a story-style video of a whole project, as the two make different kinds of video.
- PRD: Future update 7 marked built, with the two decisions that differ from its recommendation. Twelve prompts and 40 files in sections 13, 16, 18, 23, and 30. The verification checklist's repository structure line re-checked against `git ls-files` after the addition. `sitemap.xml` now lists twelve share pages, written by the mirror sync.
- DESIGN.md 1.11.7: the focus-stop count for twelve prompts is fifteen.

---

### Prompts v1.83.0 - 2026-09-27

#### Changed

- Ideas list: the entry about using the `latent-spaces/brag` repository directly became PRD section 27, Future update 7, "Launch Video: run the /brag skill directly", and was removed from `docs/TODO.md`, which is back to its placeholder. Nothing is built yet; the update waits for the author's decision.
- Finding recorded with it: nothing was lost. The site never used the repository directly. Future update 2 (v1.66.0) took only the launch copy and alt text idea from its README into the Motion Design prompt, and kept that prompt's own renderer by choice. Motion Design is a different kind of video, not a version of `/brag`.

---

### Prompts v1.82.0 - 2026-09-27

#### Fixed

- This site's dashboard showed its last step, "Push and confirm the Roadmap is live", as in progress after the task had finished. That step could only be marked done after the push, and the dashboard only reaches the live site through a push, so the final update never went live. The page was republished with every step done and the final summary.

#### Changed

- Progress Dashboard prompt, new default rule: where a task ends with the project being published, the final update (every step done, the summary at the top) is written before publishing, so the finished page goes live with the rest. Publishing, and confirming that something is live, are never steps on the page, since the live copy could never show them done; they are reported in the conversation instead. The rule does not tell the reader to publish anything, which stays their decision (PRD section 11).

---

### Prompts v1.81.0 - 2026-09-27

#### Changed

- Documentation prompt: when a project has no progress dashboard, the Roadmap entry it adds now proposes building one by running the Progress Dashboard prompt, linked by its share page (`/p/progress-dashboard.html`). The entry does not restate the dashboard's layout, branding, or rules, so a change to the dashboard is made in one prompt only. The description of the CLAUDE.md section it keeps was shortened for the same reason.
- Kept in the Documentation prompt on purpose: `/dashboard` in the enforced folder tree, and the Repository Hygiene rule that it is public project content and never ignored. Those are rules about the repository, which that prompt owns.

#### Notes

The link is to a public page and takes no action on any account, so it is within PRD section 11. If the Progress Dashboard prompt is ever renamed, its old share page must redirect to the new one (section 32), or this link breaks.

---

### Prompts v1.80.0 - 2026-09-27

Future dashboards made with the Progress Dashboard prompt now match this site's dashboard in layout, while keeping each project's own branding.

#### Changed

- Progress Dashboard prompt, layout: "choose the panels for this task" is replaced by one fixed layout, written out in full: sidebar with section counts (a scrolling strip below 900px, no script), sticky top bar with the update time and percent complete, four summary figures, a progress card, tables for steps, questions, stuck items, and results, a Roadmap section wherever the project's docs keep one (re-read on every update, never copied by hand), a footer, empty states that keep the layout still, and status pills that carry a word as well as a color. This site's dashboard is linked as a working example, but the written lines are the specification, so the prompt works when the page cannot be reached. The link is read-only and takes no action on any account, so it stays within the portability rule in PRD section 11.
- Progress Dashboard prompt, branding: the dashboard changes layout and structure only. Where CLAUDE.md records no dashboard style, Claude takes the colors and fonts from the project's existing branding (its design doc, CSS custom properties or theme file, and brand files), fills any gap from the nearest brand color, shows where each color came from, and records it in CLAUDE.md after confirmation. It asks for colors only where the project has no branding. The example's gold-on-black colors are never copied. The density question is gone, since the layout now fixes it.
- Fonts: the brand's fonts lead each font stack with system fallbacks, and are never downloaded or linked, keeping the page free of network requests.

#### Notes

This site's own dashboard keeps its gold-on-black palette, which is the style recorded in `CLAUDE.md` and which the prompt reads first.

---

### Prompts v1.79.0 - 2026-09-27

#### Added

- `dashboard/index.html`: a Roadmap section, read from PRD section 27 each time the page is built, so it cannot drift from the PRD. It lists the milestones not yet complete, every Future updates entry marked built (with its version) or proposed (with the first clause of its recommendation), and the deferred items, above a card with the verification checklist meter (2 of 32 sections verified) and the count of ideas in `docs/TODO.md`. The sidebar links to it, with a count of open milestones and proposed updates.

#### Changed

- PRD section 27: Future updates 1 to 5 each gained a `**Built in v1.66.0.**` line, matching entry 6. Until now only the paragraph above them said they had shipped, which a reader landing on one entry, or the dashboard, could not see. Section 20 records that a built entry always gets that line.
- `CLAUDE.md`: the recorded layout includes the Roadmap section.
- Status pills no longer capitalise their text automatically, which had turned version numbers into "V1.66.0".

---

### Prompts v1.78.0 - 2026-09-27

#### Changed

- `dashboard/index.html`: rebuilt on the layout of the author's admin-dashboard template. A sidebar with the brand, the current task, and section links with counts; a sticky top bar with a live dot, the update time, and the percent complete; four summary figures; a progress card; and tables for steps, questions, stuck items, and results, with word-and-color status pills and empty states. The colors stay the ones `CLAUDE.md` records (near-black, `#141414` panels, gold to amber), at the author's request, instead of the template's graphite and amber.
- The template's shared stylesheets and script are not linked. The page must load nothing from the network, so only the styles it uses are written inline, and the template's drawer, which needs a script, becomes a scrolling strip of section links below 900px.
- `CLAUDE.md`: the layout recorded beside the style, so later dashboards match. PRD section 20 notes it.

#### Notes

Checked at desktop width and inside a 375px frame. Headless Edge on Windows will not size its window below about 490px, so a phone-width screenshot needs the page in a narrow frame; at the asked-for 390px the screenshot was cropped, not overflowing.

---

### Prompts v1.77.0 - 2026-09-27

#### Changed

- Progress Dashboard prompt: removed the cleanup rule for projects set up under the old `.dashboard/` layout (moving the old folder and removing its `.gitignore` line). The prompt now names only `dashboard/`.
- Documentation prompt: the enforced folder tree shows `/dashboard` at the root, marked public, for projects that keep one. The Repository Hygiene bullet says only that `/dashboard` is public project content, tracked, never ignored, and never consolidated; the discrepancy check for `.dashboard/` is gone. The two other mentions now read `/dashboard/index.html`, one calling it a public progress page instead of a live one.
- Unchanged on purpose: the Documentation prompt's general `.gitignore` rules (secrets, build output, lockfiles), which have nothing to do with the dashboard.

---

### Prompts v1.76.0 - 2026-09-27

Finishes the v1.74.0 change that made the progress dashboard public, which left four places in the Progress Dashboard prompt still written for a private page.

#### Changed

- Description: "a public HTML dashboard" instead of "a live" one.
- The introduction and the Dashboard rules now say the copy on disk is the live one, and the published copy shows the state as of the last time the project was published, which is the reader's decision.
- Latest results list files with paths relative to the project root, so no local path reaches the public page.
- Claude gives the page's public address as well as its path, where the project is published somewhere it can name.
- The standing-rule line written into CLAUDE.md now says the page is published and nothing private goes on it, so a later session reading only that line still keeps it clean.

---

### Prompts v1.75.0 - 2026-09-27

#### Added

- PRD section 27, Verification checklist: the 32 PRD and DESIGN.md sections that describe the code, each marked verified with a date or not yet verified. Two are verified: the repository structure in sections 13 and 30, checked against `git ls-files` (38 files, seven folders). The rest are checked a section at a time as later updates touch them.
- PRD section 20: the rule that does that checking, in its own subsection.

#### Notes

- The author confirmed the licence's one grant: the prompts may be copied, adapted, and run, and not republished as a collection. No change to `LICENSE.md`.
- Considered and not done: telling the Progress Dashboard prompt to keep its build script inside `dashboard/`. The folder is now public, so the script would be published with it, and it would assume every project has Python. Editing the page directly is enough for most tasks.

---

### Prompts v1.74.0 - 2026-09-27

The progress dashboard is now public, so progress on a long task can be watched from the live site.

#### Changed

- Progress Dashboard prompt: the page lives at `dashboard/index.html` instead of `.dashboard/index.html`, and is tracked and published with the project instead of ignored. New rules: nothing private on the page (no secrets, keys, personal details, or private paths; questions about those stay in the conversation), a `noindex` tag since it is a working page, `progress-dashboard/` if `dashboard/` is already taken, and cleanup of the older setup (move a `.dashboard/` page, remove the ignore line, and remove `.gitignore` if that leaves it empty). The standing-rule line names the new path.
- Documentation prompt: the Repository Hygiene default now treats `dashboard/` as project content, never ignored and never consolidated, and reports a leftover `.dashboard/` or an ignore line for either as a discrepancy. Its other mentions of the path updated.
- This site: the dashboard moved to `dashboard/index.html` and is live at `/prompts/dashboard/`. `.gitignore` removed, since its only entry is gone and the Repository Hygiene rule says a project that generates nothing carries no ignore file. `CLAUDE.md` and PRD sections 13, 20, 30, and 32 updated.

#### Notes

The rename was required, not a style choice: GitHub Pages builds with Jekyll unless a `.nojekyll` file is present, and Jekyll skips folders whose names start with a dot, which is why `/prompts/.gitignore` already returned 404. The live page shows the state as of the last push; the ten-second reload only shows something new between pushes when opened from disk.

---

### Prompts v1.73.0 - 2026-09-27

The Documentation prompt now sets a project up rather than verifying all of it at once. On another project of about 150 source files, the old full crawl was estimated at 400,000 to 700,000 tokens, and the run stopped to ask for a smaller scope, against the prompt's own rule.

#### Changed

- Documentation prompt, goal and steps: the goal is the right files, structure, sections, and standing rules, with the docs checked against the code where that is cheap. Step 1 surveys the codebase (listing, manifests, configuration, entry points, routing, data models, build and deploy files) instead of reading everything, and finds what changed since the last audit. Step 3 checks in three passes: the rules check against the prompt, quick factual checks (folder tree, tech stack, Runbook commands, the newest patch notes entry against the latest commit), then the sections touched by changes since the last audit. Where a live public site exists, a one-off spot check of its public pages is allowed. Step 4 fixes every gap in the same run, and writes unchecked sections from the survey with their claims marked uncertain.
- New verification checklist in the Roadmap spec: every PRD and DESIGN.md section that describes the code, marked verified with a date or not yet verified. A new Working Practice rule has each later update check the sections it touches, never the whole list at once.
- New cost paragraph: no reading every file, no offering a choice of scope, no time or token estimates, and every gap confirmed by reading the file before it is reported, not from a search result.
- Ideas files under another name: moved only when the ideas are all the file holds. A mixed file has its ideas copied into docs/TODO.md and is left untouched, with a question about emptying it. Instructions inside it are recorded as ideas and not carried out.
- Sitemaps: where a site has none, one is created listing only the pages reachable without signing in, named in robots.txt where the project owns it, with a comment if the production address is not live yet.
- Logic fixes found while checking: writes are now limited to the files the prompt names, which now includes the root files and style fixes it had always asked for (the old wording limited them to the documentation files). Conventions come from a sample of files. The writing style sweep uses searches. The PRD records the audit's date, so the next audit can find what changed.
- Introduction and description rewritten to match. PRD section 33 describes the new process.

#### Notes

This site's own PRD has no verification checklist yet. The next audit of this site adds it.

---

### Prompts v1.72.0 - 2026-09-27

#### Changed

- Documentation prompt: the one-pass paragraph now says to do the whole audit in the session, without spawning subagents, parallel agents, or background tasks, however large the codebase. The introduction says the same in a phrase. Mirror and share page resynced.

---

### Prompts v1.71.0 - 2026-09-27

Answers the questions from the v1.70.0 audit, and adopts the progress dashboard to test it here.

#### Added

- `sitemap.xml` at the root: the site root and all eleven live share pages, twelve URLs, with no `lastmod` so a sync does not change it needlessly. Answers open question 9.
- `LICENSE.md` at the root, answering open question 7. The Documentation prompt's default (all rights reserved, source-available, AI and search referencing permitted, training by request, no waiver, permission requests on the GitHub issue tracker, platform and third-party notes, no warranty), adjusted by one grant: anyone may copy, adapt, and run the prompts on their own projects. The default grants nothing, but PRD section 11 already said the prompts "may be reused by anyone", and an existing rule wins over a default. Republishing the prompts as a library, product, course, or dataset is not granted.
- `CLAUDE.md` at the root: the progress dashboard rule for long tasks and its style (dark, medium density, gold `#FFB800` with a gold-to-amber gradient, taken from the look of 1000xstocks.com), recorded at the author's request to test the Progress Dashboard prompt on real work. This release was its first task.
- `.gitignore`: the repository's first ignore file, with one entry, `.dashboard/`.
- `docs/PRD.md` section 32b, Licensing, and a section 20 subsection on the progress dashboard.

#### Changed

- `tools/prompts-mirror.py`: `--sync` now writes `sitemap.xml` and the check fails if it is missing or stale. Its closing reminder now says to browser-test only a major update, matching section 20, instead of after every sync. The sitemap's comment avoids a double hyphen, which XML forbids inside comments; the first version wrote `--sync` there and failed to parse.
- `docs/PRD.md`: open questions 6 (the copy button, confirmed working by the author), 7, and 9 answered. Sections 13 and 30 describe the new root files and the ignore file, with the file count at 38. Section 27 entry 6 records the dashboard as built against its recommendation, and why. Section 29 notes that `--sync` writes the sitemap. Section 32 lists `sitemap.xml`, `LICENSE.md`, and the configuration files in the public surface table.
- `README.md`: one line under Author on what the licence allows.

#### Notes

`tools/prompts-mirror.py` changed, so this is a major update under PRD section 20. An assumption check and a browser test from disk ran once before pushing.

---

### Prompts v1.70.0 - 2026-09-27

A full documentation audit, run with the site's own Documentation prompt as of v1.69.0, in one pass.

#### Changed

- `docs/PRD.md` section 33: step 4 of After any documentation change now defers to section 20's Testing Cadence. The Documentation prompt replaces a browser rule that runs after every change and gives no project-specific reason. The old wording was: "Load `index.html` from disk and confirm the site still works, if anything outside `/docs` was touched." A prompt edit touches files outside `/docs` and is still minor under section 20, so the two rules disagreed. Recorded as discrepancy 18.
- `docs/PRD.md` section 33: Running an audit describes the one-pass run, the closing Questions list, and how `docs/TODO.md` ideas and the progress dashboard proposal are handled, and records this run as the last.
- `docs/PRD.md` section 27: the self-audit milestone, planned since v1.38.0, is complete, with a note on where each of its six findings stands. Two milestones added for the ideas list and its first batch. The current phase mentions the ideas list and the eleven prompts. Future updates entry 6 proposes a progress dashboard for this repository, as the prompt requires for a project without one, and recommends against it for now, since tasks here rarely reach its threshold.
- `docs/PRD.md` section 19: open question 9, whether to add a `sitemap.xml` now that eleven share pages exist, with none created meanwhile. The marker-search note now accounts for `docs/TODO.md`, whose name matches a literal search for TODO.
- `docs/PRD.md` section 18: discrepancies 18 and 19, both resolved, and the list of what this audit checked and found accurate.

#### Fixed

- `docs/DESIGN.md` 1.11.6: section 4a called the stylesheet 536 lines; it is 569. Discrepancy 19.

#### Notes

Checked and found accurate: the prompt mirror, all eleven share pages' tags and titles, the per-route title logic, the stylesheet's section order and breakpoints, the file and line counts, and the README's required sections. The writing style sweep across all 34 tracked files found no violation: the one literal em dash and five HTML entity forms are the known instances that name the forms they prohibit, and no double dash is used as punctuation. Nothing outside `/docs` changed, so no browser test or assumption check was needed.

---

### Prompts v1.69.1 - 2026-09-27

#### Fixed

- `docs/PRD.md` sections 13 and 30: the file count is 34, not 32. v1.66.0 added the Progress Dashboard and Assumption Check prompts and their share pages, four files, but the count rose by only the two prompts. Found by comparing the stated count with `git ls-files` during a documentation check.

---

### Prompts v1.69.0 - 2026-09-27

#### Changed

- `prompts/documentation.md`: the audit now runs in one go. It no longer stops to ask during the run: it applies the prompt's defaults, and where none applies it takes the most conservative option (keep the existing text, mark the point as a discrepancy or uncertain, and create, move, or delete nothing hard to undo). Every question it raises goes into a numbered Questions list at the end of the step 5 summary, each with the default applied meanwhile and where it is recorded, so they can be answered by number afterwards.
  - `docs/TODO.md` ideas are no longer asked about after step 3. They stay untouched and are listed among the closing questions; on a yes afterwards, the five-step process runs as before.
  - Later sessions still ask about the ideas every time before pushing, as the author set in v1.61.0.
  - The page description matches.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.68.0 - 2026-09-27

#### Changed

- `prompts/documentation.md`: where a project's `CLAUDE.md` has no Progress dashboard section, the audit no longer asks about one, which v1.67.0 had it do. It adds an entry under "Future updates" in the PRD Roadmap proposing a live progress page for long tasks, with what, why, how, size, open questions, and a recommendation for that project, unless the Roadmap already covers it. The author decides in a later session, as with every Roadmap entry. A declined entry moves to the Roadmap's deferred items with the reason, so later audits do not propose it again. An existing section is still kept unchanged and recorded in Working Practice.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.67.0 - 2026-09-27

#### Changed

- `prompts/documentation.md`: two small additions for projects that use the Progress Dashboard prompt.
  - The consolidation sweep keeps a "Progress dashboard" section in `CLAUDE.md` (a style, or a standing rule for long tasks) unchanged, and records it in the PRD's Working Practice, so a documentation run never removes a choice the author made. Where there is none, the audit asks once, with its other questions, whether the author wants one. On a yes it shows the `CLAUDE.md` lines and writes them once confirmed. On a no it creates nothing and records the decision, with the date, in Working Practice so later audits do not ask again. The dashboard stays opt-in, since a rule turned on by default would spend usage on every long task in every project.
  - Repository Hygiene treats `.dashboard/` as a one-session working folder: listed as ignored when it exists, never described as project content, and reported as a discrepancy if it is not ignored or is already tracked.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.66.0 - 2026-09-27

Builds all five Future updates proposed in v1.64.0.

#### Added

- `prompts/progress-dashboard.md`: the Progress Dashboard prompt, the tenth. Claude keeps `.dashboard/index.html` for a long task, a single self-contained page that opens by double-click and reloads every ten seconds, showing the steps and their status, anything stuck, questions waiting for the reader with the default it will take, and the latest results. Claude maintains it in the same session: no agents, subagents, or plugins are installed, at the author's request, where the source idea used a separate agent. It asks for a style once and records it in `CLAUDE.md`, keeps working on the default when a question waits, and asks before writing a standing rule for long tasks, showing the lines first.
- `prompts/assumption-check.md`: the Assumption Check prompt, the eleventh. Read-only: Claude lists its assumptions about the code for the current task, marked verified (with file and line) or guessed (with the reason), checks the cheap guesses, proposes the smallest fix or check for the rest, and stops for review.
- `p/progress-dashboard.html` and `p/assumption-check.html`: their share pages, generated by `tools/prompts-mirror.py`.
- `README.md`: both prompts added to What You Will Find Here.

#### Changed

- `prompts/motion-design.md`:
  - Optional effects in Build: liquid glass (a cloned scene through three displacement maps), goo, an iris, a flood transition, and footage loaded all-intra as a blob URL.
  - Four key stills shown before the full build, after the beat map.
  - Sound effects may now be downloaded from a free library whose license allows commercial use without attribution, as the author chose, with each file's source and license in `sounds/CREDITS.md`. Music is still never downloaded.
  - The mix is normalized to -14 LUFS, and the render is scanned for single-frame pops.
  - Four gotchas: `backdrop-filter: url()` in Chromium, flood timing, `visibility: visible` under a hidden parent, and video seeking on a simple local server.
  - States are suggested so the sequence shows what the project does, photos or footage and references are optional inputs, and the report ends with neutral launch copy and alt text.
- `prompts/brand-identity.md` and `prompts/game-setup.md`: an optional references question. Claude reads what it can, asks for screenshots of what it cannot open, and says which qualities it takes from each.
- `prompts/documentation.md`: Testing Cadence now covers an assumption check as well as the browser test. Right before a major update ships, the change's assumptions are listed as verified or guessed, the cheap guesses are checked, and the rest are shown, then the browser test runs once. A large change that depends on something unread checks that one thing first. Shipping is defined for projects that are never pushed or deployed and run from local files: the moment the major update is finished. Minor updates get neither check. The summary now lists any claim written from inference rather than from reading the code. Working Practice and the page description match.
- `docs/PRD.md`: section 20 adopts the assumption check before the browser test for a major update. Section 27 records all five updates as shipped, with the decisions taken. Prompt and file counts updated in sections 13, 16, 23, 30, and 32a, the folder tree gains both files, and the section 23 focus-stop count is now fourteen.
- `docs/DESIGN.md` 1.11.5: the section 10 focus-stop count updated to fourteen.
- `js/prompts-data.js`: resynced, with the two new entries appended last.

#### Notes

Both new prompts were audited against the Prompt Content Rules in PRD section 11: no instruction to push, commit, or publish, and no reference to the author's accounts. Their descriptions are 145 and 147 characters. No site code changed, so this is a minor update under section 20 and shipped on the mirror check.

---

### Prompts v1.65.0 - 2026-09-27

#### Changed

- `prompts/documentation.md`: the `docs/TODO.md` template now shows the format instead of an empty comment: one idea bullet with a source bullet indented beneath it, both in angle brackets. The prompt treats them as a placeholder, never an idea, so a list holding only the placeholder is empty, and it puts the placeholder back when the last idea is removed.
- `docs/TODO.md` and `docs/PRD.md` section 20: the same placeholder and rule for this repository.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.64.0 - 2026-09-27

#### Changed

- `docs/PRD.md` section 27: a new "Future updates" part with five proposed updates, turned from the ideas list's first item, which asked for six posts on X to be analyzed. X could not be read, so the author pasted their text; the one repository linked was read directly. The entries:
  1. Motion Design: optional effects (liquid glass, goo, iris, flood transitions, footage), a single-frame pop scan and -14 LUFS loudness, and four new gotchas. From the @twoclipping post.
  2. Motion Design: launch copy and alt text, and states that tell the project's story. From the @shiri_shh post and the `latent-spaces/brag` README.
  3. Design references asked for in Brand Identity, Motion Design, and Game Setup, with no link directory on the site. From the @himanshubuildss and @vullnetademaj posts.
  4. A new Progress Dashboard prompt. From the @Voxyz_ai post.
  5. A new Assumption Check prompt. From the @kloss_xyz post.
- `docs/TODO.md`: the item removed, since the Roadmap and these notes now hold it. The list is empty.

---

### Prompts v1.63.0 - 2026-09-27

#### Changed

- `prompts/documentation.md`: the Gather step for `docs/TODO.md` ideas now says how hard to try before asking. Turning six posts on X into Roadmap updates, three read attempts failed or returned only a title. A link now gets at most two attempts: the web fetch tool, then one headless Edge load with a normal browser user agent. Logging in, using the author's accounts or cookies, and third-party mirrors or scrapers are ruled out. An error, a login wall, or only a title or preview counts as unreadable. Claude then asks for the text of every unreadable source in one message, listed by author and link, or asks straight away if the author says to skip the attempts.
- `docs/PRD.md` section 20: the same rule for this repository.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.62.0 - 2026-09-27

#### Changed

- `prompts/documentation.md`: an idea in `docs/TODO.md` is now treated as a brief for Claude to work out, not text to copy into the Roadmap. v1.61.0 said to add each idea "written as a planned update", which would have turned a note such as "analyze these six posts" into a Roadmap entry saying the same thing. On the author's yes, each idea now goes through five steps:
  - **Gather:** read what it points to, and ask for the text of any source that cannot be read, such as a post behind a login, rather than guessing from the link.
  - **Interpret:** work out the concept the author means.
  - **Relate:** judge how it applies to the project.
  - **Propose:** write one or more updates in Claude's own words, each with what, why, how, rough size, open questions, and a recommendation (which may be not to do it), ending with a "Based on:" line naming its sources.
  - **Report:** remove the idea, log which entries it became, and list them in the summary for the author to edit. The author chose to have entries written and then reported, rather than approved as drafts first.

  The TODO.md template, the audit rule, the later-session rule in Working Practice, the summary requirement, and the page description are updated to match.
- `docs/PRD.md` section 20 and `docs/TODO.md`: the same process and template wording for this repository.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.61.0 - 2026-09-27

#### Added

- `docs/TODO.md`: the author's list of ideas for future updates. It began as `PROMPTS.md` at the root, created in the GitHub editor, and was moved here with `git mv` and put in the new template. Of its two items, the request to change the Documentation prompt is done in this release and removed; the request to analyze six posts for prompts stays until the author decides whether it goes in the Roadmap.

#### Changed

- `prompts/documentation.md`: two additions.
  - **`docs/TODO.md`.** The prompt creates it from a fixed template if it is missing, adds it to the folder tree, and exempts it from the consolidation sweep, so it is never merged, moved, or deleted. A list found under another name, such as `PROMPTS.md`, is moved to it with its ideas. The file belongs to the author, so Claude adds nothing to it and puts its own suggestions in the Roadmap. Its ideas are never built directly: the audit asks whether to move them into a "Future updates" part of the PRD Roadmap, removes each one moved and logs where it went, then asks whether to work on any now. A Working Practice rule carries this to every later session: check the list only when about to push (or when a major update is finished, where nothing is pushed), fetch first so an edit made on GitHub is never overwritten, and ask every time. The summary reports what happened to it.
  - **Testing Cadence**, a new default beside Browser Testing and Verification Environment. It runs the browser test in headless Edge once, right before a major update ships, and never between edits. A major update changes behavior, layout, scripts, styles, routing, the build, or dependencies; wording, docs, and data are minor and need only cheap non-browser checks. Unlike the other defaults, it replaces an existing rule requiring a browser test after every change, where that rule gives no project-specific reason, because an earlier version of this prompt may have written it. The old wording is quoted in the patch notes, and a rule with a real reason is kept and flagged instead.
  - The page description covers both.
- `docs/PRD.md` section 20: adopts the new cadence. A browser test from disk in headless Edge now runs only before a major update, meaning a change to `index.html`, the stylesheet, the script, the mirror tool, or the page template. Prompt text and docs ship on the mirror check alone. This replaces the every-change browser check in force from v1.0 to v1.60.0, whose wording was: "Then open `index.html` from disk, not from a server, and check the home list, one prompt page, the copy button, and a direct hash link. The script catches mirror drift and malformed prompt files; it cannot catch a rendering or layout problem, so it replaces none of this. Loading the page is still the only real test this project has." A new subsection sets the ideas-list check before every push.
- `docs/PRD.md` section 30: the four-file rule now names `docs/TODO.md` as its one exception, and the folder trees and file counts in sections 13 and 30 include it. The count is 30.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.60.0 - 2026-09-25

#### Added

- `prompts/motion-design.md`: the Motion Design prompt, the ninth in the library. It makes a short, looping UI motion video entirely in code: one shape morphing through eight to twelve interface states, driven by an on-screen cursor, in time with a song.
  - It reads the project first, so the states, colors, and font can come from the project's own UI, and flags any doc rule it would break, offering to update the docs, work in a separate `motion/` folder, or stop.
  - It asks once for the states, the color scheme, a royalty-free song the reader supplies (it never downloads music), the format (square, 16:9, or 9:16), the length, and the font, follows up on anything unclear, and shows the states on the song's beat grid for approval before writing code.
  - Every style is computed from time in a `seek(t)` function, with closed-form springs summed per target change, so any frame renders exactly and the last frame matches the first. The tab indicator and toggle knob stretch by riding different springs on each edge, and drags follow the cursor directly. A `?preview` mode scrubs the animation with the song playing.
  - Beats come from librosa, or from numpy and the stated tempo. Neither detects downbeats, so the reader confirms beat 1 by ear. Interface sounds are synthesized or supplied, and placed by their measured peaks.
  - A contact sheet with one frame per beat is checked before the full render. The render takes four Playwright screenshots per frame, blends them with ffmpeg `tmix` and `framestep` for motion blur at 60fps, and encodes an H.264 MP4 with the mixed audio. The loop join is checked for stutter.
- `p/motion-design.html`: its share page, generated by `tools/prompts-mirror.py`.
- `README.md`: the prompt added to What You Will Find Here.

#### Changed

- `js/prompts-data.js`: resynced, with the new entry appended last.
- `docs/PRD.md`: prompt and file counts updated in sections 13, 16, 23, 30, and 32a, the folder tree gains the new file, and the section 23 focus-stop count is now twelve.
- `docs/DESIGN.md` 1.11.4: the section 10 focus-stop count updated to twelve.

#### Notes

The details most likely to have changed since the model's training data were confirmed by web search on 2026-09-25: Geist is under the SIL Open Font License and installs locally from `@fontsource/geist`; `librosa.beat.beat_track` returns beats and a tempo estimate but no downbeats, which is why the prompt asks the reader to confirm beat 1; and ffmpeg's `tmix` averages frames with equal weights by default, so `tmix=frames=4` followed by `framestep=4` turns 240 subframes a second into 60fps with motion blur.

Audited against the Prompt Content Rules in PRD section 11: no instruction to push, commit, or publish, and no reference to the author's accounts. The description is 135 characters.

---

### Prompts v1.59.0 - 2026-09-24

#### Changed

- `prompts/game-setup.md`: Phase 1 now checks the project's docs for rules the prompt would break, and says so before anything else.
  - The rules it looks for: no build step, no npm dependencies, running from `file://` with no server, and a strict Content Security Policy.
  - The reasons it gives for each: browsers block JavaScript modules and asset loading from `file://`, so a three.js game needs at least a local server. A game also needs `connect-src 'self'` to load assets, `'wasm-unsafe-eval'` for Rapier and the model decoders, and `worker-src blob:` for the decoder workers.
  - Each conflict is quoted with its file and line, at the top of the Phase 1 message. The reader chooses to update the docs (confirming the wording first), adapt within the rule at a stated cost (no build step means no TypeScript, no model compression, and no test tooling), or stop.
  - Nothing is changed or built until the reader answers. The page description says so.
- `js/prompts-data.js`: resynced.

#### Notes

This came from the author asking whether a game made with this prompt could live within this site's own constraints. The answer was partly: a built game can be hosted on GitHub Pages with no server, but it cannot run from `file://`, without dependencies, or without a build step, which are exactly the rules a project like this one writes into its docs.

---

### Prompts v1.58.0 - 2026-09-24

#### Changed

- `prompts/game-setup.md`: the prompt now asks rather than guesses when it lacks information.
  - Phase 1's one message adds a Documentation item: what the existing docs are missing, out of date on, or contradict about the game, and the details only the reader can supply, such as the game's name, audience, or story.
  - If the answers leave the core loop, the controls, or the win and lose conditions unclear, it asks a short follow-up instead of inventing them, and Phase 2 does not start until the game is clear enough to build.
  - The closing docs update asks for any missing information before writing, and never fills a gap with invented details.
  - Before this, Phase 1 already asked once and waited, but vague answers could be filled in by the model, and the docs were written at the end without a check.
  - The page description says so.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.57.0 - 2026-09-24

#### Added

- `prompts/game-setup.md`: the Game Setup prompt, the eighth in the library. It sets up a three.js browser game and builds a small playable vertical slice on top of it.
  - It reads the project, then asks once about the game: genre, camera, core loop, desktop or mobile, `WebGPURenderer` or `WebGLRenderer`, plain three.js or React Three Fiber, physics, and art direction, each with a recommended default.
  - The setup: Vite and strict TypeScript; separate modules for the engine, input, audio, assets, game logic, and UI; a fixed-step loop with interpolation, a clamped frame delta, and a pause when the tab is hidden; a state machine from boot to game over; action-based input across keyboard, mouse, gamepad, and touch, with remapping; compressed glTF assets with disposal checked against `renderer.info`; unlocked Web Audio; versioned saves; recovery from a lost graphics context; a stated performance budget; accessibility defaults; and a debug mode behind `?debug`.
  - After one checkpoint it builds the smallest complete core loop (menu, play, win or lose, restart) and verifies it with type checks, Vitest unit tests, and a Playwright smoke test that fails on console errors and saves screenshots, which it looks at.
  - It tells the model to check the installed three.js version's docs instead of relying on memory, since the API changes often, and it deploys nothing.
- `p/game-setup.html`: its share page, generated by `tools/prompts-mirror.py`.
- `README.md`: the prompt added to What You Will Find Here.

#### Changed

- `js/prompts-data.js`: resynced, with the new entry appended last.
- `docs/PRD.md`: prompt and file counts updated in sections 13, 16, 23, 30, and 32a, the folder tree gains the new file, and the section 23 focus-stop count is now eleven.
- `docs/DESIGN.md` 1.11.3: the section 10 focus-stop count updated to eleven.

#### Notes

Brainstormed with the author, who chose the name. The three.js details most likely to have changed since the model's training data were confirmed by web search on 2026-09-24: `WebGPURenderer` imports from `three/webgpu` with automatic WebGL2 fallback, custom shaders on it are written in TSL because `ShaderMaterial` and `onBeforeCompile` do not carry over, and SwiftShader in a headless browser provides WebGL but no WebGPU adapter. The renderer question and the smoke test instructions were written to match.

Audited against the Prompt Content Rules in PRD section 11: no instruction to push, commit, or publish (the prompt forbids deploying), and no reference to the author's accounts. The description is 140 characters.

---

### Prompts v1.56.0 - 2026-09-23

#### Changed

- Renamed the iPhone and iPad Simulator prompt to **iOS Simulator**, at the author's request for a two-word title. iOS Simulator is Apple's own name for the tool the prompt runs, and it covers iPhone and iPad alike. The description and prompt text are unchanged.
- `prompts/iphone-ipad-simulator.md` became `prompts/ios-simulator.md`, moved with `git mv` so its history follows.
- `p/ios-simulator.html`: the new share page, generated by `tools/prompts-mirror.py`.
- `p/iphone-ipad-simulator.html`: retired rather than deleted, because it has been a public address since v1.54.0. It now carries the retired marker and forwards to `index.html#/ios-simulator` in one hop, with tags describing the renamed prompt. It is the first share page to be retired.
- `README.md`: the prompt's bullet uses the new name.
- `docs/PRD.md`: the retired items table in section 32 gains the rename, the file counts in sections 13 and 30 are now 25, and the folder trees note the retired page.
- `js/prompts-data.js`: resynced under the new slug.

---

### Prompts v1.55.0 - 2026-09-23

#### Changed

- `prompts/iphone-ipad-simulator.md`: Step 1 now checks for macOS before anything else. The iOS Simulator is part of Xcode, which runs only on macOS, and there is no iOS emulator for Windows or Linux, so before this the prompt would have failed on its first `xcodebuild`. On a non-Mac it now installs nothing, identifies the project type, and explains the three routes, marking which fit: a rented cloud Mac, where the full prompt runs; a cloud simulator build streamed to a browser simulator such as Appetize.io, which the reader can click through but which the prompt's automated checks cannot drive; and Expo Go on a real iPhone, for Expo and React Native apps only. Running macOS in a virtual machine on non-Apple hardware is left out, since Apple's license does not allow it. The page description says the prompt needs a Mac and what it does otherwise.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.54.0 - 2026-09-23

#### Added

- `prompts/iphone-ipad-simulator.md`: the iPhone and iPad Simulator prompt, the seventh in the library. It checks the Mac and the installed Xcode, installs what is missing, builds the reader's app for the iOS Simulator, and launches it on the smallest, a standard, and the largest iPhone. Every main screen is screenshotted in light and dark mode and at the largest accessibility text size, and the screenshots are looked at, not assumed. It works with native Xcode projects, Swift packages, and Expo, React Native, Flutter, and Capacitor apps, and ends with a report of each problem, its screenshot, its likely cause in the code, and a proposed fix.
  - It asks once, before installing anything, whether to include **iPad** (suggested when the app targets it): the smallest and largest iPads, all four orientations, Split View, Slide Over, and Stage Manager, and keyboard and pointer support.
  - And whether to include **iPhone Duo**, Apple's foldable: the Xcode 27.1 beta installed alongside the current Xcode, both displays, and each fold pose. It requires Apple silicon and macOS 26.6 or later.
  - Its ground rules: it never handles the reader's Apple ID password, keeps any existing Xcode, builds for the simulator only and signs, uploads, or submits nothing, installs dependencies as locked, and changes no app code beyond the minimum a new SDK needs to build until the reader chooses the fixes.
- `p/iphone-ipad-simulator.html`: its share page, generated by `tools/prompts-mirror.py`.
- `README.md`: the prompt added to What You Will Find Here.

#### Changed

- `js/prompts-data.js`: resynced, with the new entry appended last.
- `docs/PRD.md`: prompt and file counts updated in sections 13, 16, 23, 30, and 32a, the folder tree gains the new file, and the section 23 focus-stop count is now ten.
- `docs/DESIGN.md` 1.11.2: the section 10 focus-stop count updated to ten.

#### Notes

Written from a social media post announcing that the Xcode 27.1 beta can install an iPhone Duo simulator, build an app, and launch it. At the author's request the prompt covers regular iPhone development, with iPad and iPhone Duo as options it asks about. The Xcode 27.1 beta, its iPhone Duo simulator, and the Apple silicon and macOS 26.6 requirements were confirmed by web search on 2026-09-23, since they postdate the model's training data. The post also named another vendor's model and tool; the prompt is written for Claude Code and names neither.

Audited against the Prompt Content Rules in PRD section 11: no instruction to push, commit, or publish, no reference to the author's accounts, and every sign-in left to the reader. The description is 144 characters.

---

### Prompts v1.53.0 - 2026-09-23

#### Changed

- `prompts/brand-identity.md`: now six phases. The author has marked this the prompt's final revision.
  - **New Phase 5, Brand kit**, in `brand/kit/`: a 1200x630 link preview image, a 400x400 profile picture that survives a circular crop, X (1500x500) and LinkedIn (1584x396) banners, `tokens.css` and `tokens.json` with the palette and type, a WCAG contrast table in DESIGN, an email signature PNG at twice its display size (most mail clients do not show SVG), and a `site.webmanifest` that is created but not linked, per the scope rule. Each image is rendered from SVG and passes the render check.
  - **Phase 4** gains a favicon that switches to a lighter variant in dark mode, and 192px regular and maskable icons for the manifest.
  - **Phase 6, Presentation** (formerly Phase 5): gets print styles and is also saved as `brand/brand-guidelines.pdf` with headless Edge, the file to hand to a printer or collaborator.
  - The render check now covers Phases 3 to 6, and the page description covers the kit and the PDF.
- `README.md`: the Brand Identity bullet mentions the kit and the PDF.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.52.0 - 2026-09-23

#### Changed

- `prompts/brand-identity.md`: Phase 5 mockups. If the reader has placed mockup photos in `brand/mockups/`, the logo is set onto them, matching each photo's perspective and lighting, and the presentation references them by relative path. Without photos, the mockups are built in CSS and SVG as before, but now with 3D perspective tilts, soft layered shadows, paper, card, and fabric textures, and lighting gradients, because flat vector mockups read as diagrams rather than objects. Downloading stock images was considered and ruled out: licensing is unclear, it needs the network, and it would bring in files the reader did not choose. The logo files themselves stay SVG only, since every other format is made from them. The page description explains both routes.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.51.0 - 2026-09-23

#### Changed

- `prompts/brand-identity.md`: revised after a line-by-line review with the author. Each change below answers one question from that review; the prompt's structure, phases, and tone are otherwise as written.
  - **Render check.** A new section, used in Phases 3, 4, and 5, has every logo judged from a rendered image rather than its SVG code: a contact sheet at 16, 32, and 512px, in color and grayscale, on light and dark, screenshotted in headless Microsoft Edge (Chrome if Edge is missing) and then looked at. Before this the legibility check had no method, so it could only ever pass.
  - **Concept A** takes its palette from the brief (one or two colors plus black and white) instead of a fixed black, white, and gold, which ignored the brief's color constraints and is itself a luxury cliché.
  - **Concept B** sets the name in an open-license typeface and customizes one or two details, instead of hand-drawing letterforms as SVG paths, which models do poorly. The typeface and its license are recorded in DESIGN.
  - **Existing brand.** The brief gains an `[existing brand]` field. When one is found, Phase 3 adds a fourth concept, D. Evolved, which refines the current brand, and A, B, and C take it only as a suggestion.
  - **Phase 4 specs.** Adds `favicon.ico`, keeps app icon marks inside the central 80% so masked crops cannot cut them, gives the 1024 icon a solid background (the App Store rejects transparency), and sets a minimum line and gap of about 1mm for embroidery. When no image converter is installed, PNGs are rendered in headless Edge, and anything still missing is listed with the command to produce it.
  - **Presentation fonts.** The page loads the brand typeface from Google Fonts as its only external link, which resolves the conflict between "self-contained" and a type specimen. The finished page is screenshotted and reviewed.
  - **Scope rule.** The prompt must not change the project's site or app. Everything stays in `brand/` and the two `## Brand Identity` sections until the reader decides how to use it.
  - The page description's three paragraphs are updated to match. The frontmatter description is unchanged.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.50.0 - 2026-09-23

#### Removed

- `prompts/brand-identity.md`: the `Input from the user: $ARGUMENTS` line. `$ARGUMENTS` is filled in only when a prompt is saved as a slash command; pasted from this site it arrived as literal text, which is why v1.48.0 had to tell the reader to replace it. Nothing is lost: Phase 1 already reads the project for the brand details and asks in one message for anything it cannot find.
- `prompts/brand-identity.md`: the page's last paragraph, which explained the placeholder. Its other sentence, that the prompt pauses for gaps in the brief and for the concept choice, repeated the first paragraph.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.49.0 - 2026-09-23

#### Changed

- `prompts/brand-identity.md`: Phase 1 now reads `PRD.md` and `DESIGN.md` as well as the README, `CLAUDE.md`, `package.json`, landing page copy, and existing brand or style files before filling in the brief. A project with a product document usually already states its audience, its purpose, and any color or font constraints, which are four of the brief's six fields. The page description lists the two new files. Written as `DESIGN.md` rather than `Design.md`, matching the rest of the prompt since v1.48.0.
- `js/prompts-data.js`: resynced.

---

### Prompts v1.48.0 - 2026-09-23

#### Added

- `prompts/brand-identity.md`: the Brand Identity prompt, the sixth in the library. It runs a brand identity project in five phases: a brand brief built from the project's own files, a competitive analysis of five to eight brands in the industry, three hand-written SVG logo concepts for the reader to choose from, a full logo system in `brand/logo/` checked at 16px, in grayscale, and on light and dark backgrounds, and a self-contained presentation page, `brand/presentation.html`, with mockups, palette, type specimen, and rationale. Its written output goes into a `## Brand Identity` section of `docs/PRD.md` and `docs/DESIGN.md`.
- `p/brand-identity.html`: its share page, generated by `tools/prompts-mirror.py`.
- `README.md`: the prompt added to What You Will Find Here.

#### Changed

- The supplied prompt text was changed in two ways, both mechanical. `docs/Design.md` became `docs/DESIGN.md` throughout, to match the file the Documentation prompt produces; on a case-sensitive file system the two names would be separate files. Line breaks lost when the text was pasted were restored where two sentences had run together, such as "usage guidelines) If either file". No wording was changed.
- `js/prompts-data.js`: resynced, with the new entry appended last.
- `docs/PRD.md`: prompt and file counts updated in sections 13, 16, 23, 30, and 32a, the folder tree gains the new file, and the section 23 focus-stop count is now nine.
- `docs/DESIGN.md` 1.11.1: the section 10 focus-stop count corrected to nine.

#### Notes

Audited against the Prompt Content Rules in PRD section 11 before publishing: no instruction to push, commit, or publish, and no reference to the author's accounts or services. The description is 146 characters, inside the 150 character sharing target. The prompt's `$ARGUMENTS` line is left as written, since it is where a reader puts their brand details; the page description says to replace it, and that the prompt will ask if it is left in.

Verified from `file://` in headless Edge: the home list shows six cards with Brand Identity last, the prompt page renders with its title, four description paragraphs, and the full 71-line prompt, and the share page forwards to it. The mirror check passes with no notes.

---

### Prompts v1.47.0 - 2026-09-23

#### Removed

- `js/script.js`: the Copy link button added in v1.46.0. Beside Copy it was confusing: two buttons both labelled Copy, one copying the prompt and one a link, made the page's main action less obvious. The copy code returned to its v1.45.0 form, and the `SITE_URL` constant, used only by Copy link, went with it.
- `css/style.css`: `.link-btn`, and the `max-width: 400px` media query that existed only to fit a third button in the header bar at 320px.

#### Changed

- `README.md`: the sharing sentence now says to copy the address from the browser.
- `docs/PRD.md`: sections 8, 10, 10a, 13, 14, 15, 23, 27, 29, 30, 31, 32, and 32a updated. Section 32a records why the button was removed.
- `docs/DESIGN.md` 1.11: the Copy link spec and the 400px breakpoint removed.

#### Notes

Sharing still works as it did in v1.46.0. The share pages and their tags are unchanged, and over https the address bar still shows `p/<slug>.html`, which is the link that gets copied and previews as the prompt. Opening the site from disk shows the `#/` address instead, as before.

Verified locally before pushing. Over `python -m http.server` the header bar shows Expand and Copy, the address bar is rewritten, the title carries the site name, and a click on Copy does not toggle the block. The bar was measured in the DOM at 320, 375, 414, 768, 1024, 1280, and 1920px without the removed media query: one line and no horizontal overflow at each. From `file://` a prompt page renders with the same two buttons.

---

### Prompts v1.46.0 - 2026-09-23

#### Added

- `p/`: one generated share page per visible prompt, `p/<slug>.html`. Each carries that prompt's `og:title`, `og:description`, `og:url`, `og:type`, `og:site_name`, and `twitter:card`, a `<title>` in the form "Prompt Audit - Azqato's Prompts", and a meta refresh plus a plain link forwarding to `index.html#/<slug>`. A link renderer never sees the `#/<slug>` part of a URL and runs no script, so until now every prompt link previewed as the home page, observed in Discord on 2026-09-23. A share page is a real file at a real path, so a renderer can read it. Its Content Security Policy is `default-src 'none'`, since it loads nothing.
- `index.html`: the same six tags, describing the site. `og:title` is "Claude Code Prompts", the home heading, so it does not repeat `og:site_name`.
- `js/script.js`: a Copy link button in the prompt header bar, between the collapse toggle and Copy. It copies the published https share address whatever the page was opened from, and reports success and failure exactly as Copy does, through the same code path.
- `js/script.js`: over http and https the address bar is rewritten to the view's share address after rendering, with `history.replaceState()`, so copying from the address bar gives the same link as Copy link. The router now reads the slug from a `p/<slug>.html` path when there is no hash, and listens for `popstate` as well as `hashchange`, guarded so one navigation renders once. On `file://` the browser forbids the rewrite and the hash route stays.
- `tools/prompts-mirror.py`: writes the share pages on `--sync` and checks them. The check fails on a missing page, a page that differs by a byte from what its prompt would generate, a page with no visible prompt that is not marked retired, a title over 70 characters or containing the site name, and a description over 200 characters or not ending on a full stop. Titles over 60 and descriptions over 150 are printed as notes. `--sync` never deletes a share page.
- `docs/PRD.md` section 32a: the Social Sharing Tags and Page Titles policy, covering the share pages, the six tags, the budgets, the title form, how the share address reaches the person sharing, and how a share page is retired.

#### Changed

- Prompt page titles now carry the site name: "Documentation - Azqato's Prompts" rather than "Documentation". Finding 5 of the self-audit in PRD section 27.
- Three prompt descriptions were over the 150 character sharing target and were tightened, and Prompt Audit's, already inside it, was reworded to lead with what it finds. This also changes the home page cards, since they show the same text. All five now run 140 to 149 characters.
  - Documentation, 186 to 141: "Scan a whole codebase and consolidate its documentation into four files: a README, plus a detailed PRD, design guide, and changelog in /docs."
  - GitHub Wiki, 202 to 148: "Build or update a repository's GitHub wiki from its documentation, curated into Home, Product Overview, Patch Notes, and other pages with a sidebar."
  - Mobile Responsive Audit, 170 to 148: "Check every page at seven screen widths for overflow and layout bugs, fix the root causes, and verify with DOM measurements rather than screenshots."
  - Prompt Audit, 148 to 149: "Find the instructions in a project's prompts, skills, and CLAUDE.md files that were written for older models, and fix the ones that now hold it back."
- `css/style.css`: `.link-btn` joins the shared button rule and both copy states. The shared rule gains `white-space: nowrap`, the header bar a 12px gap between its label and its buttons, and a new `max-width: 400px` query trims the bar's padding, the button gap, and the buttons' padding, so the label and three buttons fit one line at 320px.
- `README.md`: one sentence on Copy link, in What This Is.
- `js/prompts-data.js`: resynced.
- `docs/PRD.md`: sections 8, 9, 10, 10a, 12, 13, 14, 15, 16, 17, 20, 23, 27, 28, 29, 30, 31, and 32 updated for the share pages, the new button, and the address rewrite. Section 12 gains a sixth step in Renaming and in Removing, because a prompt now has one public address of its own. Open question 8 is answered, and self-audit findings 3 and 5 are closed. The roadmap milestone is complete.
- `docs/DESIGN.md` 1.10: Copy link specced, the third breakpoint documented, and the button inventory, CSS structure, and shell template updated.

#### Fixed

- `docs/PRD.md` section 20, "Where to look first": the prompt edit row still sent the reader to "the README table and tree", which the README has not had since v1.26.0. It is the same stale instruction discrepancy 17 recorded in four other places, surviving in a fifth. Now names the README prompt list.
- `docs/PRD.md` and `docs/DESIGN.md`: the `index.html`, `css/style.css`, and `js/script.js` line counts, which had drifted, corrected in place under the mechanical-fact exception.

#### Notes

Verified before pushing. Locally over `python -m http.server`: a share page forwards to its prompt and the address bar is rewritten back to the share address; a hash route is rewritten to its share address; home is rewritten to the root; a sidebar click from a rewritten address routes and rewrites again; the back button returns to the previous prompt; a click on Copy link does not toggle the collapse. From `file://`: a share page forwards, and the prompt renders with the new title and all three buttons. The header bar was measured in the DOM at 320, 375, 414, 768, 1024, 1280, and 1920px, one line and no horizontal overflow at each. The mirror check was run against a planted orphan page, the same page marked retired, and a hand-edited share page, and failed, passed, and failed as it should.

Not verified: how any particular service renders the cards. That depends on the service, and is checked by pasting a link after the deploy.

---

### Prompts v1.45.0 - 2026-09-23

#### Changed

- `prompts/prompt-audit.md`: the command is now `/claude-api prompt-audit and apply the proposed changes`. The bare `/claude-api prompt-audit` produced a report and a proposed diff and edited nothing, because the skill's audit guide applies edits only when the request explicitly asks for them. With the added words it edits the files directly for every high- and medium-confidence finding, and leaves low-confidence findings in the report untouched.
- `prompts/prompt-audit.md`: the card description now says the command fixes what it finds, and the page body says so too. The page now advises running it on a committed working tree, because nothing pauses for approval and the edits can land before the report is on screen, so `git diff` is where they are reviewed and reverted. It also says how to get the report alone: drop "and apply the proposed changes" and run the bare `/claude-api prompt-audit`, which edits nothing.
- `README.md`: the Prompt Audit line now says it fixes the patterns rather than reporting them.
- `js/prompts-data.js`: resynced.

#### Notes

The wording was tested before publishing, twice. In this repository the request routed to the audit guide and ran without pausing, but found nothing to apply, since v1.43.0 already had. In a second project it made real edits, with four observations recorded here. It applied only high- and medium-confidence findings, and every edit traced to a reported finding. It applied the edits before presenting the report, which the page now warns about. It initially left the low-confidence findings out of its report, which was caught and corrected in that session. And it also updated that project's own PRD and patch notes, because that project's instruction file requires docs to match every change, which is the project's rule operating rather than the audit reaching outside its scope.

With words after it the request is no longer a bare subcommand, so the skill reaches the audit through its general routing rather than its subcommand table. Both tests show that routing holds, but it depends on the skill's wording, which can change between Claude Code versions without this page knowing.

---

### Prompts v1.44.0 - 2026-09-23

#### Added

- `docs/PRD.md` section 27: a roadmap milestone and a scoped item, "Per-prompt social sharing cards". A link to a prompt should render a card with that prompt's title and a short summary. Today every prompt link renders the site's generic card, observed in Discord on 2026-09-23 with the Prompt Audit link. The item records the cause, the standard, a proposed approach, the decisions needed first, and how to verify it.
  - The cause is the architecture, not only the missing tags. A link renderer requests the URL without its `#` fragment and runs no JavaScript, so every prompt link is the same `index.html` to it, and tags in that file can describe only the home page.
  - The standard is the Social Sharing Tags default from the Documentation prompt, since this PRD states no sharing policy of its own. The item spells out how each rule applies here: six tags, a unique absolute `og:url` per prompt, no site name in `og:title`, a 150 to 200 character description in complete sentences, and no images.
  - The proposed approach is one generated static share page per prompt, with the tags and a meta refresh to the prompt's hash route. It is generated and verified by `tools/prompts-mirror.py`, so no dependency is added and the Content Security Policy stays unchanged.
  - The decisions needed first are the share path shape, which becomes a permanent public address once pasted anywhere; whether to tighten the existing descriptions, four of which exceed the 150 character target and one the 200 ceiling, or add a separate short field; and how the share URL reaches someone copying from the address bar.

#### Fixed

- `docs/PRD.md` section 27, finding 3 of the self-audit: it said the Social Sharing Tags default asks for a marketing-focused tone that section 11 prohibits. It never did. The prompt has asked for an educational tone since v1.37.0, and the phrase appears only in that finding. A correction was added beside the original text rather than replacing it, so the record shows what was believed and when.

#### Changed

- `docs/PRD.md` section 19, open question 8: now points at the new roadmap item, which settles the canonical domain half of the question from section 17 and proposes an answer to the architecture half.

---

### Prompts v1.43.0 - 2026-09-23

#### Changed

- `prompts/documentation.md`: five instructions removed or rewritten after a `/claude-api prompt-audit` pass found them written in a register that current models over-apply, or contradicting another line of the same prompt.
  - The read-only paragraph no longer says "Do not skip a step because it looks obvious or because you think you already know the answer". The rule that a step which finds nothing must say so stays, since that is an output requirement rather than a push.
  - Step 5, "Do not skip any document. Every single file in /docs must be reviewed and updated", was removed and step 6 became step 5. It repeated step 2, and "must be updated" contradicted the Merge rule, which leaves text alone where the code agrees with it.
  - "Be thorough." and "When in doubt, include it." were removed from the completeness paragraph. The reasoning around them, completeness over brevity in `/docs` and why, is unchanged and still carries the quality bar.
  - "1) Consolidate all of the files in docs into 4 main documents" was removed and the list renumbered. It restated the scan paragraph directly above it with a narrower scope (`/docs` only, where the scan covers the whole project), so the two gave different instructions for the same step.
  - The README rule "Be as thorough as possible while ensuring readability" now reads "Cover every required section, and where completeness and readability pull apart, brevity wins", since the old wording pointed in two directions at once.

#### Fixed

- `prompts/prompt-audit.md`: the page description said the command would "remove" dated patterns. It proposes changes and applies them only when asked, which is what the page body and the README already said. The v1.42.0 notes claimed this wording had been corrected; it had been corrected in the body but not in the description.
- Discrepancy 17 is now fully corrected. v1.42.0 fixed the stale README Files table instruction in Adding step 5 only. The same instruction survived in `docs/PRD.md` Renaming step 3, Removing step 3, and the section 16 binding rules list, and in the `prompts/add-prompt.md` page description. All four now name the prompt list under "What You Will Find Here". The v1.42.0 entry and its version history row are left as written, as section 33 requires.

#### Notes

The audit found nothing written for a specific older model, no retired model names, and no API code, tool definitions, or skill files. The other prompts were left unchanged. Five low-confidence items were reported and not edited: three uses of emphasis that carry a stated reason, and two factual claims with no verification date (the headless minimum viewport in Mobile Audit and the renderer clip lengths in the Social Sharing Tags section).

---

### Prompts v1.42.0 - 2026-09-23

#### Added

- `prompts/prompt-audit.md`: the **Prompt Audit** prompt, the fifth in the library and the first whose prompt is a single command rather than a block of text. `/claude-api prompt-audit` runs the built-in skill's audit over a project's skills, its `CLAUDE.md` and `AGENTS.md` instruction files, its tool descriptions, and any standalone prompts, and reports the patterns written for an earlier generation of model that now hold a current one back.
- `js/prompts-data.js`: the mirrored entry, appended, so the prompt sorts last in the sidebar and the home list.
- `README.md`: a line for it under "What You Will Find Here", written for a general reader like the four beside it.

#### Changed

- Four counts in `docs/PRD.md` that a fifth prompt made stale: the project is 15 files rather than 14 in section 13, `prompts/` holds five `.md` files rather than four in the section 13 tree, the section 23 note that a taxonomy is unnecessary now says five prompts, and section 30 says fifteen files. The section 30 tree lists the new file. All corrected in place under the mechanical-fact exception in section 33, since a count carries no intent.
- The section 16 line recording that no prompt instructs its reader to push now covers five prompts, with the new one verified on 2026-09-23 and the original four left at their 2026-08-23 date, since that verification happened then and the record says when.

#### Fixed

- Section 12 of `docs/PRD.md`, step 5 of Adding Prompts, said to "add a row to the Files table and the file structure tree in `README.md`". The README has carried neither since v1.26.0 rewrote it for a general reader and moved all structure into the PRD. The instruction had outlived the thing it described for sixteen releases and was only caught because adding the fifth prompt exercised the step for the first time since the rewrite. Logged as discrepancy 17 and corrected rather than left flagged, because the intent, keeping the README's prompt list in step with the data file, survived intact and only the mechanism changed.

#### Notes

The description was written from the pasted tip but does not repeat two things in it. The tip named a specific model version as the reason to run the audit, which is left out: a version number in a published prompt description ages with that version, and the reason to run this is that instruction files accumulate, which is true regardless of what shipped. The tip also said the command "removes" anti-patterns; the description says it reports them and proposes changes, which is what the skill actually does.

`prompt-audit` was verified as a real subcommand before the page was written rather than taken on faith from the tip, since publishing a command that does not exist is the one failure a prompt library cannot recover from. It is non-interactive, establishes its own scope and target model, states its assumptions rather than stopping to ask, and produces a report.

---

### Prompts v1.41.0 - 2026-09-18

#### Added

- `prompts/documentation.md`: a **Repository Hygiene** section, placed after Security because it is the enforcement and verification side of a sentence Security already carries, that no secret is hardcoded and every environment variable is listed but never its value. The default is stated outright: the repository carries an ignore file and a `.gitattributes`, commits its lockfile, keeps every secret out of history, and names its default branch `main`.
- Nine rules behind that default, each with its reasoning: secrets kept out by an ignore rule with `.env*` and a `!.env.example` negation so the key-name file travels and the value file never does; an ignore file wherever anything is generated; lockfiles committed rather than ignored; every ignore entry naming something the project actually produces; ignoring not untracking; generated output committed on purpose being recorded rather than forbidden; line endings pinned; large binaries kept out of history; and the remote, default branch, and history notes recorded in the PRD.
- A verification sub-list of seven read-only checks, including the one that cannot be answered by reading a file: no tracked file matches a pattern the ignore file claims to exclude.
- `.gitignore` and `.gitattributes` in the enforced folder structure tree, with a paragraph on the way they differ from every other root file: a nested copy of either is legitimate rather than a mistake, because version control reads an ignore or attributes file in any directory and applies it downward, which is how one part of a repository narrows a rule the root file sets. An audit that finds one in a subdirectory records what it does and leaves it there, the same treatment a sitemap named on a `Sitemap:` line already gets.
- Section 27 of `docs/PRD.md`: finding 6 in the self-audit entry, recording that this is the first default in the prompt that this repository already satisfied.

#### Fixed

- The findings in section 27 of `docs/PRD.md` ran 1, 2, 3, 5, 4, 6. Finding 5 was inserted above finding 4 in v1.40.0 by anchoring on the wrong paragraph, which went unnoticed because nothing reads that list in order until a sixth entry arrives. Resequenced. No wording changed.
- Section 30 of `docs/PRD.md` said "Thirteen files, five folders". The repository has tracked 14 since `.gitattributes` landed in v1.36.0, and section 13 was corrected then while this copy was missed. Corrected in place under the mechanical-fact exception in section 33, since a file count carries no intent. This is the third time the same pattern has produced a stale fact, and the same technique caught it: grep for the thing that changed rather than trusting that the section already edited was the only mention.

#### Notes

The section was researched rather than written from memory, and the research changed four things. A blanket `eol=lf` breaks a Windows batch script, so the rule now pairs the repository-wide setting with an explicit `eol=crlf` for formats that need it; the first draft would have shipped that defect. The `.env*` and `!.env.example` negation replaced a vaguer instruction to keep secrets out. Lockfiles got their own rule, because the inversion people actually commit is ignoring the dependency directory and the lockfile that pins it together. And the ignore file is now described as prevention rather than protection, since treating it as a security control is how a project ends up with one and no scanning.

Two boundaries are stated rather than left implied. Commit message style and branching pattern stay with Conventions, which reads them from the history, so that no two sections govern one topic. And a secret found in history is reported with a rotation recommendation, never remediated: rewriting history is destructive, it is outside the audit's write scope, and it does not undo an exposure that became public the moment it was pushed.

This repository already met the default before the section existed, which has not happened with any other policy added to this prompt. It has no ignore file and section 13 already explains why, which is exactly what the "a project that generates nothing says so" clause asks for. `.gitattributes` pins `* text=auto eol=lf`, and the reasoning that section generalises came from this project in v1.36.0. `js/prompts-data.js` is the generated-output-committed-on-purpose case, and section 13 already names what regenerates it and what keeps it in step.

The prompt block is now 51,144 characters, up from 43,713. It has grown 124 percent this session, from 22,785. That number is recorded each release rather than acted on, and the rule for what would ever come out still does not exist.

---

### Prompts v1.40.0 - 2026-09-09

#### Added

- `prompts/documentation.md`: a **Page Titles** section, placed after Social Sharing Tags because the two share a layer, a condition, and a field. Both govern what a page says about itself in its head, both apply only where the project serves a site, and both have an opinion about the same brand string. The default sets the shape `<unique page name> - <brand>` under two limits: the first 30 characters must identify the page on their own, and the whole title stays at 60 or fewer.
- The two numbers are stated as measuring different things rather than as a compromise. Truncation removes from the end, so a title is read at two lengths at once: the first 30 characters are what survives a crowded tab strip, and the full 60 is what a search result renders. Front-loading satisfies both, so nothing has to be traded off. The front budget is 30 rather than 50 because a tab is measured in pixels, and a title of capitals and wide letters fills the same physical tab as a longer one in lowercase.
- The uniqueness rule is written against the first 30 characters rather than against the whole title. Two titles that differ only after character 30 are the same title as far as a tab is concerned, so requiring unique titles is the weaker test and requiring unique prefixes is the one that matters.
- A verification sub-list of six read-only checks, covering presence, length, prefix uniqueness with collisions reported as pairs, separator consistency, brand placement, and per-route title reading on a client-rendered site. The last of those exists because a title set once in the head and never updated passes a source check and fails in a browser.
- Section 27 of `docs/PRD.md`: a fifth finding in the self-audit entry, recording that this site now falls under a policy it only half meets.

#### Notes

Three decisions were put to the author while the section was drafted, and all three are recorded here because each rules out a reading someone would otherwise reach for later.

The hard limit is 30 on the front of the title and 60 on the whole, not 30 on the whole. A 30-character total was considered and rejected on arithmetic: `Azqato's Prompts - ` costs 19 characters before the page name begins, so a 30-character ceiling leaves 11 for the page name and two of this site's four prompts already do not fit. The only way to reach 30 total is to drop the brand from every page, which removes it from exactly the two places it was earning its keep, the search result and the bookmark. Truncation past 30 is not a failure under this rule, it is the mechanism working: what gets eaten is the brand, which the favicon has already said.

The homepage rule states the principle and stops. It leads with the brand, and whether anything follows is the project's call, with the bare site name and no separator named explicitly as a valid answer where the brand is already what people search for. The cost of the bare name is recorded next to it, since the homepage is usually the page where a stranger in a search result most needs telling what the site is.

The checks are a sub-list rather than one prose bullet, which is a departure from Social Sharing Tags. Deprecation and Removal already nests a sub-list at the same indent, so the form is not new to the prompt, and a list of assertions is easier to work through mechanically than the same assertions in a paragraph.

The prompt block is now 43,713 characters, up from 38,086. It has grown 92 percent this session, from 22,785 at the start. That is worth watching rather than acting on: every section added has been a policy the author asked for, but a prompt long enough that a reader skims it stops being enforced, and there is no rule yet for what would ever come out.

---

### Prompts v1.39.1 - 2026-09-08

#### Changed

- `prompts/documentation.md`: The sorting instruction now names the two kinds in the sentence that introduces them: "sort them into two kinds: Documentation Files and Project Files". Previously the reader met the categories only in the two sentences that followed and had to infer that a sort into named buckets was being described.
- Capitalised the two later uses to match, so the terms read as defined labels rather than as ordinary noun phrases. A named category that changes case between uses looks like two different things.

#### Notes

The prompt block is now 38,086 characters, up from 38,047.

---

### Prompts v1.39.0 - 2026-09-08

#### Changed

- `prompts/documentation.md`: The codebase scan line now tells the audit to scan the whole project for markdown and text files, not only `/docs`, and to sort what it finds into two kinds before consolidating anything. Documentation files are folded into the four main documents. Project files stay where they are, meaning anything a tool, a platform, or the product itself depends on, such as `LICENSE.md` or a markdown file that ships as content rather than describing it. A doc that is genuinely better maintained where it sits stays there and gets a pointer from the PRD.
- The sorting rule is what makes the wider scan safe. Consolidation removes the original, so widening the search without a test for what must not be absorbed would turn a documentation pass into something that can delete a dependency. The test given is whether anything other than a reader depends on the file.
- The clause about a markdown file that ships as content is the one this repository needs most. All four prompts are `.md` files that read exactly like documents, and an audit run here without that sentence could fold `prompts/*.md` into the PRD and delete the product.

#### Notes

Applied as a single-line change to the existing scan instruction rather than as a rewrite of numbered item 1, which is where this rule was first drafted. Placing it in the scan line puts it before the consolidation steps, which is the order it has to run in.

The author's text read "Documentation Files gets consolidated". Corrected to "Documentation files get consolidated" for subject-verb agreement and to match the lower-case "Project files" in the next sentence. No other wording was changed.

The pasted source also had the blank line removed between the `PRD.md` description and the `---` that follows it. Not applied, and treated as a copy-paste artifact rather than an edit: in markdown, text directly above `---` becomes a setext heading. It renders harmlessly inside the fenced block on the site, but the prompt is copied into other contexts where it would not.

The prompt block is now 38,047 characters, up from 37,543.

---

### Prompts v1.38.0 - 2026-09-07

A planning release. No behaviour changed and no file outside `/docs` was touched.

#### Added

- Section 27 of `docs/PRD.md`: a **Scoped** subsection recording the self-audit of this project against the documentation standard as it stands at v1.37.0, and a milestone row for it. The prompt gained six sections since this project was last audited against it in v1.27.0, and the gap had never been written down.
- The findings of the partial read-only pass run on 2026-09-07, recorded in that subsection rather than discarded. The pass was stopped before anything was written, so these are observations with their reasoning attached, not decisions:
  - `robots.txt` must **not** be created in this repository. The site is served from `https://azqato.github.io/prompts/`, a subdirectory rather than an origin, so a file at this root would deploy to `/prompts/robots.txt` where no crawler reads it. The governing `https://azqato.github.io/robots.txt` belongs to a different repository and returned 404 when checked. This is the outcome the prompt's own subdirectory clause prescribes.
  - `sitemap.xml` would be valid at this root, since a sitemap covers URLs under its own location and `/prompts/` is the whole site, but it could hold only one URL. Every route here is a fragment and a crawler never sees a fragment.
  - The social sharing tags collide with an existing rule. The default asks for a marketing-focused description; section 11 prohibits marketing language. Section 11 wins under the prompt's own precedence rule, and the collision is noted as something worth addressing in the prompt, since any project with a house style will hit it.
  - `LICENSE.md` remains open question 7 and was deliberately not acted on.

#### Changed

- Open question 8 in section 19 now points at the roadmap entry, so a reader arriving at the question finds the scheduled work rather than a dead end.

#### Notes

The audit was scoped out at the author's request rather than deferred on its merits, so it is a planned milestone rather than a Deferred entry. The distinction matters in section 27: Deferred items carry a reason they will not be done.

---

### Prompts v1.37.0 - 2026-09-07

#### Added

- `prompts/documentation.md`: A **Social Sharing Tags** section, placed after Licensing because the two cover the same layer, what a page tells a machine about itself rather than what it shows a reader. The default requires six tags on every shareable page (`og:title`, `og:description`, `og:url`, `og:type`, `og:site_name`, `twitter:card`), sets character budgets of 60/150/20 with hard ceilings of 70/200, turns images off by default, and lists the pages that are deliberately excluded. Like every policy in that prompt it yields to a rule the project already states, and it applies only where the project actually serves a site, the same condition already attached to `robots.txt` and `sitemap.xml`.
- The section is written as a policy record rather than an instruction to edit pages. The audit reads the tags that exist, writes the rule into the PRD, and reports any page that fails it as a discrepancy. This is deliberate: the prompt's read-only guarantee for steps 1 through 3 is followed by a write scope limited to the four documentation files, so a section that told the model to rewrite every page head would contradict the constraint the prompt states most strictly. The compliance checks are recorded as checks to run, and are explicitly read-and-report.
- Section 19 of `docs/PRD.md`: open question 8. This site now falls under a policy it does not meet. `index.html` carries a `<meta name="description">` and nothing else, so a pasted link renders from the title tag alone.

#### Changed

- The prompt's page description in `prompts/documentation.md` now lists Social Sharing Tags among the required PRD sections, keeping the description and the prompt body in agreement.

#### Notes

The source text supplied for this section named a specific chat platform as the rendering target. That naming is generalised in the prompt to "one chat platform" and "the strictest renderer", with the reasoning kept intact, on the same grounds section 11 applies to services and accounts: a prompt is copied into other projects, and a rule that names a product ages with that product. The behaviour it is written against, a narrow card that falls back to the title tag, is what actually matters and is stated directly.

The prompt block is now 37,543 characters, up from 31,766.

---

### Prompts v1.36.1 - 2026-08-24

A follow-through release. v1.36.0 added `.gitattributes` and documented the decision, but left five other places in `docs/PRD.md` describing the state before it.

#### Fixed

- Section 13 said the project is 13 files and that there is no `.gitattributes`, in a paragraph explaining the consequence of not having one. It is now 14 files, and that paragraph describes what the file does and why the mirror needs it. The tree lists it.
- Discrepancy 15 in section 18 ended with "whether to pin LF with a `.gitattributes` is open question 5". Marked resolved, with the note that `tools/prompts-mirror.py` still normalizes line endings and that this is now redundant on purpose rather than load-bearing.
- The deploy comparison in section 20 instructed normalizing line endings before comparing local against deployed, because `core.autocrlf` rewrites the working tree. That is no longer true of a current checkout. It now says the comparison is valid as it stands, and that normalizing anyway costs nothing and keeps the check correct against a clone made before v1.36.0.
- The technical debt table in section 30 still carried the missing `.gitattributes` as open debt. Struck out as fixed, which makes four struck rows.
- Four stale line counts, corrected in place under the mechanical-fact exception in section 33 rather than flagged, since a line count carries no intent: `css/style.css` is 567 lines rather than 540, in three places across sections 13 and 30, and `index.html` is 42 lines rather than 31, in section 20 of this document and section 12c of `docs/DESIGN.md`. Both had been stale since v1.28.0 added the Content Security Policy and the copy button's failed state.

#### Notes

Worth recording why this release exists at all. The v1.36.0 change was one new file and a closed open question, which is about as small as a change gets here, and it still left five statements in the PRD false and four numbers wrong. The reason is that this document deliberately repeats facts across sections so each one can be read on its own, which section 33 states as the standard. The cost of that standard is exactly this: a fact that changes has to be chased through every place it appears, and the copy nobody was editing is the one that goes stale. Discrepancy 16, logged in v1.29.0, was the same failure with the same cause. The check that catches it is grepping for the thing that changed rather than trusting that the section it was changed in was the only one mentioning it.

#### Verified

- Grepped for `gitattributes`, `autocrlf`, and every stale line count across all tracked files, then read each match rather than assuming the replacement was right.
- Re-rendered in Edge across all six routes. Unchanged, as expected: documentation only.
- `tools/prompts-mirror.py` clean.

---

### Prompts v1.36.0 - 2026-08-24

Closes open question 5, which has been open since v1.28.0.

#### Added

- `.gitattributes`, pinning `* text=auto eol=lf`. A checkout now produces LF on any machine, whatever its `core.autocrlf` is set to. This repository stores LF, so nothing about the stored content changes; what changes is that the working tree can no longer disagree with it.
- The file carries a comment explaining why, because the reason is not obvious from the rule. The line breaks inside the `raw` strings in `js/prompts-data.js` are JSON escape sequences rather than real newlines, so git never rewrites them. Under `core.autocrlf=true` and with no `.gitattributes`, a checkout therefore produced CRLF source files under `prompts/` while their mirrored copies stayed LF, and the two stopped matching byte for byte with nothing actually wrong.

#### Notes

The counter-argument recorded in section 19 was that `tools/prompts-mirror.py` already normalizes line endings on both sides, so the problem was handled. That was true, and it was judged insufficient for two reasons.

The failure mode is silent rather than loud. A literal comparison does not error, it reports a difference that is not there, and the natural response to the mirror check reporting drift on all four prompts is to run `--sync` and rewrite a file that was already correct.

And normalizing inside the tool puts the burden on every tool that touches these files, rather than on the repository. It had already cost two debugging cycles, both in this project: it broke the first version of the mirror script in v1.28.0, discovered only because a file had just been restored with `git checkout`; and in v1.35.0 a `git checkout` mid-session left an edit script unable to match its own target text, which surfaced as an unhelpful "not unique (0)" assertion rather than as anything mentioning line endings.

The deployed site is unaffected either way, since GitHub Pages serves what the repository stores and that was always LF.

#### Verified

- Tested against a real checkout rather than by reading the rule. Both `prompts/documentation.md` and `js/prompts-data.js` were deleted and restored with `git checkout`, which is the exact operation that produced CRLF before. Both came back LF, and `tools/prompts-mirror.py` passed clean afterwards: four prompts, no orphans, all frontmatter present. That is the scenario that broke the first mirror script, so it is the one worth testing.
- Re-rendered in Edge across all six routes. Unchanged, as expected: no file the browser loads was modified.

---

### Prompts v1.35.0 - 2026-08-24

#### Changed

- `prompts/documentation.md`: The enforced folder structure now shows `sitemap.xml` at the repository root and excludes it from the rule that moves stray files into `/docs`, alongside the README, the licence, and `robots.txt`.

#### Added

- The reasoning that separates a sitemap from the two files listed beside it, because treating all three as one rule is how an audit either moves a working file or leaves a broken one alone. `robots.txt` is root by requirement: crawlers read it from the origin root and nowhere else. `sitemap.xml` is root by default: a sitemap is scope-limited by its own location, so one at `/docs/sitemap.xml` may only list URLs under `/docs/` and entries outside that path are ignored, while one at the root can list the whole site. That makes the root the position that is always correct without being the only correct one.
- The cross-submission exception, which is the part that changes what an audit should do. A sitemap named on a `Sitemap:` line in `robots.txt` is trusted for the entire host wherever it sits. So a sitemap outside the root is valid exactly when robots.txt points at it, and an audit that finds one there checks for that line rather than assuming the file is broken or relocating it. The same condition as `robots.txt` applies throughout: this is only relevant where the project actually serves a site.

#### Verified

- Re-rendered in Edge across all six routes. Every route unchanged, all four prompt pages open collapsed and toggle correctly, no error view. The Documentation prompt matches its source fenced block exactly, confirming the mirror carries the edit.
- `tools/prompts-mirror.py` resynced and passed clean.

---

### Prompts v1.34.0 - 2026-08-24

#### Changed

- `prompts/documentation.md`: The enforced folder structure now shows `LICENSE.md`. The licensing policy added in v1.33.0 already said the file goes at the repository root, but the structure diagram did not list it, so the two could be read as disagreeing and the diagram is the part a model follows literally.
- `LICENSE.md` is excluded from the rule that moves stray documentation into `/docs`, alongside the README. It is root only for the same reason the README is: it is one of the two files a person or a tool expects to find without looking. Stated explicitly in the prompt because hosting platforms detect a licence by looking in specific locations, the repository root is the most widely recognised of them, and a licence filed under `/docs` may not be detected at all.

- `robots.txt` is listed at the root as well, and excluded from the same move rule. This one is a hard requirement rather than a convention: crawlers fetch it from exactly one address, the origin root, and read it from nowhere else, so a copy under `/docs` is not a robots policy at all, it is an unreferenced text file. The licensing policy added in v1.33.0 already required `robots.txt` to stay open and consistent with the licence, but said nothing about where it lives, which left the one detail that determines whether it does anything.

#### Added

- A never-move rule for licences. Where a project already has a licence file, under any name and in any location, it stays exactly where it is and is documented in place. An existing licence is a decision the project already made, and this audit records those rather than overruling them. `LICENSE.md` is created only where no licence exists.
- Two conditions on `robots.txt`, since the structure diagram would otherwise read as an instruction to create one everywhere. It applies only where the project actually serves a site: a library or a CLI has no origin to put one on and should not get one. And where a site is served from a subdirectory of a larger domain, the PRD says so, because the robots.txt governing it belongs to the domain owner and may not be the project's to write. This project is an example: it serves from `/prompts/` under a domain whose root it does not own.

#### Notes

This release was written once with the file under `/docs`, then reverted before it was committed and rewritten with it at the root. The `/docs` version had a real problem: the structure rule would have relocated an existing root licence, which can stop a repository being reported as licensed. The reasoning survived the reversal and is now the justification for keeping it at the root rather than for moving it, which is why this note exists at all: the argument is worth more than the position it was first written to support.

#### Verified

- Re-rendered in Edge across all six routes, unchanged. The Documentation prompt matches its source fenced block exactly. Mirror check clean.

---

### Prompts v1.33.1 - 2026-08-24

#### Changed

- `prompts/documentation.md`: The licensing policy now names the licence file as `LICENSE.md` rather than as a plain text file, at all five places it referred to one. The licence is a document people read, it belongs to the same markdown doc set as the four files this audit already writes, and every platform that detects a licence file recognises the `.md` extension, so nothing is lost by it.

#### Verified

- Re-rendered in Edge across all six routes, unchanged. The Documentation prompt is 29,137 characters and matches its source fenced block exactly. Mirror check clean.

---

### Prompts v1.33.0 - 2026-08-24

A licensing default policy for the Documentation prompt, supplied by the author.

#### Added

- `prompts/documentation.md`: A **Licensing** section, placed after Security since both concern what a project asserts rather than how it is built. Like every policy in this prompt it yields to what the project already has: where a project has a well defined licence, the audit names it, points at the file, and states what it permits, and the default applies only where there is no licence or where a bare licence name sits in a README with no licence text behind it.
- The default posture is all rights reserved, source-available rather than open source. Publish a LICENSE that grants nothing, because the repository is published so it can be read and publishing is not a grant. The reasoning is the part that makes the rule usable: a permission given to everyone cannot easily be withdrawn from one person, and the goal is usually not to stop copying but to retain the ability to act against a specific bad actor. Those two goals conflict the moment the licence hands out broad permissions.
- The NO WAIVER clause is called out as load-bearing, since a long history of tolerating copies is the first thing an infringer points at. Also stated: the asymmetry rule, that widening a grant is one sentence and narrowing a granted right is not, so when in doubt grant less and offer the request route; and that a licence is never asserted without licence text, because a bare name with no file is an ambiguity rather than a grant.
- One standing carve-out, for AI and search referencing. Search engines, AI assistants, answer engines, and other automated systems may crawl, index, store for retrieval, quote, summarise, link to, and cite the work, with attribution requested rather than required and no permission to ask for. Being cited in an AI answer is the modern equivalent of ranking: it costs nothing and gains distribution, and enforcing against a citation works against the project's own purpose. The line is drawn at three distinct things: referencing is granted, substitution is not, and training data is not granted by default but is routed to the request path with a note that it is not usually refused. Retrieval-and-cite is what actually produces the citations, so this keeps the benefit without handing over a training licence.
- Three things the licence must not claim: it does not purport to override a hosting platform's terms, since a public repository already grants that platform's users whatever its terms say and the licence should state that those operate independently rather than pretend to withhold them; it does not claim third-party data derived from an external API or public source; and it does not restrict rights that cannot be restricted, such as fair use or fair dealing.
- The required LICENSE sections are listed, and the machine-readable layer is required to stay consistent with the licence: `robots.txt` stays fully open with a comment marking that as deliberate, and the LICENSE is named authoritative if the two ever disagree. A grants-nothing licence beside an open `robots.txt` is a contradiction a cautious crawler operator may resolve the wrong way.

#### Changed

- The permission-request route was generalized. The policy as supplied named a specific repository's issue tracker as the example. Section 11 of `docs/PRD.md` prohibits a prompt from referencing services or accounts belonging to the author, and discrepancy 8 in section 18 records two prompts being deleted in v1.19.0 partly for exactly that. The prompt now says to route to a public tracker rather than private email and to name that tracker's address for the repository being audited, which preserves the reasoning, that a visible record suits a posture whose enforcement depends on permissions being specific and traceable, without embedding one project's address in a prompt meant to run anywhere.

#### Notes

**This repository has no LICENSE file**, so by the policy just written it falls to the default. That was not acted on in this release, for two reasons. A licence is a legal assertion published under the author's name rather than a documentation change, so it is the author's call rather than a default to inherit silently. And the posture deserves a deliberate answer here in particular: this site exists to hand people prompts to copy and use, which is not obviously the same posture as all rights reserved. Recorded as open question 7 in section 19. Declining the default and saying why is a valid answer; leaving no licence and no note is the only outcome that carries a real cost, because it leaves a reader guessing.

#### Verified

- Re-rendered in Edge across all six routes. Every route unchanged, all four prompt pages open collapsed and toggle correctly, no error view.
- The Documentation prompt grew to 28,907 characters and the rendered page carries the new section, matching the fenced block in `prompts/documentation.md` exactly, which confirms the mirror carries the edit rather than a stale copy.
- `tools/prompts-mirror.py` resynced and passed clean: four prompts, no orphans, all frontmatter present.

---

### Prompts v1.32.0 - 2026-08-24

A working practice change rather than a product change. Nothing about the site itself is different.

#### Removed

- `docs/PRD.md` section 20: "Never push or publish without being asked. Publishing is the author's decision." The author gave standing authorization on 2026-08-24 for this repository, so every change here now ships as soon as it is documented and verified. There is no approval step and nothing waits for a release window.

#### Changed

- `docs/PRD.md` section 20 gains a Publishing subsection recording the authorization, its date, and its scope, along with the reasoning. The reasoning is worth keeping because it is specific to this project rather than a general claim that pushing is safe: the site is static, with no database, no user data, no session, and no server-side state, so a bad deploy cannot corrupt or lose anything. Rollback is one revert and one push and takes about as long as the deploy did.
- The Never list keeps an entry in the same position, rewritten: never push a change that has not passed the checks. Removing the approval step does not remove the verification, and with the pause gone the verification is the only thing left between an edit and the live site. That is a stronger reason to run it than existed before, not a weaker one.
- `docs/PRD.md` section 29, Deploy: the same change, stated where the deploy procedure actually lives so a reader following the runbook does not have to have read section 20 first.

#### Notes

Three boundaries were written into the change rather than left implied.

**It covers this repository only.** The authorization was given about this project, so it does not travel to any other repository.

**It does not shorten the procedure before a push.** The mirror check must still print OK, the page must still be opened from disk and looked at, and the patch notes and version history row are still written before the push rather than after. A release that is live and undocumented is precisely the state this project's documentation practice exists to prevent.

**It is unrelated to the rule in section 11** that no prompt's text may instruct its reader to push. That rule is about the content this site publishes to other people, not about how this site is maintained, and the two were easy to conflate because both used the word "push". Section 29 now says so explicitly.

#### Verified

- Re-rendered in Edge across all six routes. No change, which is the expected result: this release touches only documentation, and no file the browser loads was modified.
- `tools/prompts-mirror.py` passed clean without needing a resync, since no prompt source changed: four prompts, no orphans, all frontmatter present.

---

### Prompts v1.31.0 - 2026-08-24

A second default policy for the Documentation prompt, on where a change is verified.

#### Added

- `prompts/documentation.md`: A **Verification Environment** section, placed after Browser Testing since the two answer adjacent questions about how a project checks its own work. The default is to verify locally and never against production, unless the request explicitly asks for a production check. Local means whatever the project's own setup produces: the file opened from disk, a local server, a development build.
- The section gives the reason rather than only the rule, because a rule without one gets dropped the first time it is inconvenient. Testing against production means the change has already shipped, so the test can only report what users are already seeing. It also puts load, writes, or test data onto a live system, and it turns a failure into something the author has to roll back rather than something they fix before pushing.
- **It separates two things that are easy to conflate.** Verifying functionality is local. Confirming a deploy arrived is a separate step, run against production after the push, and it is a comparison rather than a test: fetch the deployed artifact and check it matches what was already verified locally. That is legitimate and is explicitly not an exception to the rule, because it answers a different question. Without saying this the policy would appear to forbid the post-push check this project has done for two releases.
- Two further clauses. Where local and production genuinely differ in a way that can hide a bug, the Runbook must name what differs and what class of bug can therefore only appear once deployed, since a reader who does not know a gap exists cannot compensate for it. And a destructive or state-changing check is never pointed at production, covering writes, deletes, migrations, seeded records, and anything that sends mail or a webhook; where a live system is the only way to exercise something, stop and ask.
- `docs/PRD.md` section 20: The rule stated explicitly for this repository, along with the deploy-confirmation procedure and the two ways local and deployed differ here.

#### Changed

- Nothing about how this project works. It has described its check as opening `index.html` from disk since v1.0, which is the rule already. The prompt now requires that to be written down rather than implied, so section 20 says it outright. This is the merge rule working as intended: the project already had a rule, so the default did not overrule it, it documented it.

#### Notes

The two environment differences recorded for this project are worth stating here too, because both are the kind of thing a local check silently cannot catch. Hash routing resolves against a directory rather than a domain root, so a path assumption that holds at `file://` can break under `/prompts/`. And `file://` is a secure context, so `navigator.clipboard` is available locally exactly as it is over `https://`, which means a local check cannot catch the copy button failing for a secure-context reason. That second one is a genuine limit on the verification gap already recorded as open question 6, not a reassurance.

#### Verified

- Re-rendered in Edge across all six routes, per the policy added in v1.30.0. Every route unchanged: the home view and an unknown slug both render four cards, all four prompt pages open collapsed and toggle correctly, no route renders the error view.
- The Documentation prompt grew to 24,682 characters and the rendered page carries the new section, matching the fenced block in `prompts/documentation.md` exactly, which confirms the mirror carries the edit.
- `tools/prompts-mirror.py` resynced and passed clean: four prompts, no orphans, all frontmatter present.

---

### Prompts v1.30.0 - 2026-08-24

A browser testing policy, added to the Documentation prompt as a default and then applied to this repository and to the one other prompt that drives a browser.

#### Added

- `prompts/documentation.md`: A **Browser Testing** section, placed beside Writing Style because it has the same shape: document the project's rule if it states one, and only adopt the default where it does not. The default is to drive Microsoft Edge and never Chrome. Where there is no JavaScript runtime on the maintenance machine, end-to-end testing means driving a headless browser directly, and Chrome is typically the owner's day-to-day browser, so driving it disturbs a live session. Edge runs the same engine, so nothing about the results changes.
- Three clauses were added around the rule itself, because the bare instruction leaves the obvious gaps unanswered. It applies to every browser a test drives rather than only the one named in a config file, since an ad hoc headless invocation from a shell command is testing too, and that is the form this project actually uses. The resolved binary path belongs in the Runbook, because it differs by platform and is the first thing that breaks on a new machine. And a project that genuinely needs a second engine should say which browsers it targets and why, rather than dropping the default silently.
- `docs/PRD.md` section 29: This repository's own browser testing rule, adopted from that default since it stated none. Records the Edge path on this machine, the exact headless invocation used, and two constraints that are not obvious: the Content Security Policy blocks inline scripts, so a driver has to be a real same-origin file rather than injected markup, and a DOM dump cannot exercise the Clipboard API, which is why the copy button's paths remain unverified.

#### Changed

- `prompts/mobile-responsive-audit.md`: The verification methodology section opened with "Headless Chrome enforces an effective minimum viewport", which is an instruction to drive Chrome and directly contradicted the new default. It now names Edge, defers to any rule the project states, and describes the viewport floor as a property of any headless Chromium browser, which is what it always was. The measurements are unchanged because the engine is the same.

#### Notes

Worth stating plainly: every browser check in this project up to and including v1.29.0 used Chrome, this session included. The policy is new, not newly enforced, and the patch notes for v1.28.0 and v1.29.0 accurately record Chrome as what was used at the time. They are left alone, because they describe what happened rather than what the rule is now.

#### Verified

- The full render check was re-run in Edge across all six routes, which is both the verification for this release and the first exercise of the policy. Every route matches what Chrome produced: the home view and an unknown slug both render four cards, all four prompt pages open collapsed with the label reading "Expand" and toggle to "Hide", and no route renders the error view.
- The Documentation prompt now renders at 22,785 characters and the new section reaches the page: the rendered text contains both "Browser Testing" and the Edge rule. That count matches the fenced block in `prompts/documentation.md` exactly, which confirms the mirror in `js/prompts-data.js` carries the edit rather than a stale copy.
- `tools/prompts-mirror.py` resynced the data file and then passed a clean check: four prompts, no orphans in either direction, all frontmatter present.

---

### Prompts v1.29.0 - 2026-08-24

The prompt block is now collapsible, and collapsed when a page opens. The first new component on the site since v1.0.

#### Added

- `js/script.js`: A collapse toggle in the code block header bar, sitting immediately left of the copy button. It is a real `<button>` carrying `aria-expanded` and `aria-controls="prompt-body"`, both kept in step with its visible label. Its label names the action it performs rather than the state it is in, "Expand" when the block is hidden and "Hide" when it is shown, which is the convention the copy button already sets.
- **The entire header bar is the click target, not only the button.** The listener sits on `.code-block-header`, which carries `cursor: pointer`. A click on the toggle reaches the same handler by bubbling, so there is no second listener on the button and no way for the two to fire against each other. Clicks originating inside `.copy-btn` return early, so copying never collapses the block that was just copied.
- The button exists alongside the clickable bar rather than instead of it, because the bar is a `div`: it cannot be focused, cannot be reached by keyboard, and carries no accessible name or state. The bar is deliberately given no ARIA role, since the button inside it is already the accessible control and labelling the container would announce the same action twice.
- `css/style.css`: `.code-block-actions`, a flex row with an 8px gap holding the toggle and the copy button, so the header is a label on the left and an action group on the right.
- `docs/DESIGN.md` section 5: A full Collapse Toggle spec, and the code block spec now documents the action group, the pointer cursor on the bar, and the collapsed default.
- `docs/PRD.md` section 10a: Prompt Collapse Behavior. This is the first lettered section in the PRD. It is numbered `10a` rather than inserted as a new section 11 because nine releases of these notes cite that document by section number, and renumbering would silently invalidate every one of those references. The convention is now stated in section 33, which previously said only that sections are appended.

#### Changed

- **The prompt block is collapsed when a prompt page opens**, on every load and every navigation. The prompts run to several hundred lines; the Documentation prompt alone rendered as roughly 350 lines of unbroken text directly beneath the title. That buried the description, which is the part explaining what the reader is about to copy, off the top of the screen on arrival.
- This appears to contradict the tenet that the code block is the product, and does not. Copy works whether the block is shown or hidden, because the text stays in the DOM and only its display is suppressed, so the primary action is still one click from arrival. The rule that actually mattered, that the header bar with the copy button is visible without scrolling on desktop, now holds on every prompt at every length rather than only on short ones. `docs/DESIGN.md` section 12c records the reconciliation instead of leaving a future reader to spot the tension and resolve it the wrong way.
- `css/style.css`: The toggle shares the copy button's rule outright, as `.copy-btn, .code-toggle`, rather than getting a second button treatment. The two are pixel-identical at rest because they are literally the same declarations, which is a property that cannot drift. `docs/DESIGN.md` section 12a now states this as the rule for adding any peer control.
- `docs/PRD.md` section 24: The assumption bullet on trusted input still described `escapeHtml()` as not escaping quotes, which stopped being true in v1.28.0. The v1.28.0 pass updated sections 30 and 31 for that change and missed this one, so the document contradicted itself for a release. Corrected, and logged as discrepancy 16 in section 18. The underlying assumption still holds and is restated at the level where it is still true: nothing validates a prompt file and the markdown renderer is hand-rolled, so the content being author-written is what makes it safe.

#### Notes

Three things were considered and deliberately not done.

**No animation.** The collapse is `display: none`, not a height transition, and the toggle has no rotating chevron. `docs/DESIGN.md` section 12b permits transitioning only `color`, `border-color`, `background`, and `opacity`; an animated open needs `height` and a chevron needs `transform`. An earlier draft used a swapped glyph pair to stay inside that rule, which was dropped once the label became a word, since a word button beside a word button does not need one. The rule this implies is now written down: show and hide, do not animate open and closed.

**No persistence.** The block collapses again on every navigation. Remembering the reader's choice would mean `localStorage`, and section 31 of the PRD states as a privacy property that no browser storage API appears anywhere in the codebase. That is worth more than the convenience. Recorded under possible future work in section 23 so the reason is visible if it is ever reconsidered, rather than the idea simply reappearing.

**No hover treatment on the bar.** A build in progress lit the toggle up whenever the header was hovered, on the reasoning that the bar is the real click target and ought to say so. In use it reads as a glitch rather than as feedback, because the pointer can be several hundred pixels from the element that changed. It was removed before release. The pointer cursor carries the affordance on its own, and the design notes now say not to add it back.

#### Verified

- Checked in headless Chrome from `file://`, driven by a real script rather than inspected statically, since every behaviour here is a click result. Fifteen assertions: the toggle is a `<button>`, its `aria-controls` resolves to an element that exists, it precedes the copy button in the DOM and to its left on screen, the label is leftmost, the bar reports `cursor: pointer`, and the two buttons render at identical heights. The block starts hidden with the label reading "Expand" and `aria-expanded` false. Clicking the button, the bar, and the label each toggle it correctly, with the label and the ARIA state moving together every time. Clicking copy changes neither. The prompt text is intact while hidden, the header keeps the copy button visible, and its bottom border is removed while collapsed.
- After the hover treatment was removed, confirmed that no `.code-block-header:hover` rule remains in the stylesheet, that the toggle does not match that selector in the rendered page, and that the toggle and copy button compute to identical colour and background at rest.
- Both states were also captured as screenshots at 1280x900 and looked at, because a passing assertion about a computed style is not the same as the layout being right.

---

### Prompts v1.28.0 - 2026-08-23

Acted on all four open questions raised by the v1.27.0 audit, after the author answered each one. This is the first release since v1.18.0 in which the site was actually rendered and checked.

#### Added

- `tools/prompts-mirror.py`: A check and resync tool for the mirror between `prompts/*.md` and `js/prompts-data.js`, which section 19 has named the project's highest-value invariant and its weakest assumption since v1.18.0. `python tools/prompts-mirror.py` reports drift, an entry with no source file, a source file with no entry, a duplicate slug, missing `title` or `description` frontmatter, and a missing fenced prompt block, exiting non-zero on any of them. Those last three matter because `parsePrompt()` falls back silently for each: a prompt missing its title ships as a page titled with its slug rather than as an error anyone would notice. `--sync` rewrites the data file from source and appends any new prompt to the end of the array, since array order is display order. It refuses to sync when an entry has no source file, because deleting a prompt is a deliberate act with a documented procedure that also touches the README and these notes.
- The script uses only the Python standard library, is never loaded by the page, and is not a build step. Deleting it leaves the site byte-identical, which is the test the PRD now states for whether something is tooling or a dependency. It also ends the pattern of rewriting the resync procedure from scratch in every session.
- `index.html`: A Content Security Policy, delivered as a `<meta http-equiv>` because GitHub Pages does not allow custom response headers on a project site. `default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'none'; base-uri 'none'; form-action 'none'; object-src 'none'`. The reason is not XSS hardening, which is marginal on a page with no external resources, no inline handlers, and no untrusted input. The reason is that it makes the no-dependency rule enforceable by the browser rather than by discipline: a future session that reaches for a CDN script or adds a `fetch()` now gets a hard, visible failure instead of a working page that has quietly broken the guarantee the whole architecture exists to protect. Tenet 1 becomes a runtime property instead of a written one.
- `frame-ancestors` was deliberately left out, because it is ignored in a meta tag and including it would imply a protection that is not there.
- `js/script.js`: A failure path on the copy button. A missing Clipboard API, which is how an insecure context presents itself rather than as a rejection, or a rejected write now shows "Copy failed" for two seconds with a matching `aria-label` telling the reader to select the text manually. Success and failure share one code path and differ only in label, class, and `aria-label`, so their timing and reset behaviour cannot drift apart.
- `css/style.css`: A `.copy-btn.copy-failed` state in `--color-negative`. This is the first use of that token, which had been defined and unreferenced since v1.0.

#### Changed

- `js/script.js`: `escapeHtml()` now escapes both quote forms as well as `&`, `<`, and `>`. `renderInline()` writes a markdown link target straight into `href="..."`, so a quote in a description's link target could previously break out of the attribute. It was never exploitable, because every byte of content is author-written, but it was the sharpest edge in the codebase and the fix is five characters. Entities decode back in both text content and `textContent`, so the rendered page and the copied prompt are unchanged.
- `js/script.js`: The slug is now escaped wherever it is interpolated into an attribute, in `buildSidebar()` (`href` and `data-slug`) and `renderHome()` (`href`). Slugs are filename-derived and safe today; this is the same fix applied consistently rather than left half-done in the one place it was noticed.
- `docs/DESIGN.md`: Both discrepancies flagged in v1.27.0 are corrected rather than left standing, after the author confirmed neither preserved an intended design. The section 11 CSS file structure list is now read from the stylesheet: the `.site-layout` class that never existed is gone, `.site-wrapper` is correctly described as the grid rather than as flex, the order matches the file, and the four omitted blocks are listed. The section 12 shell template now includes the `.sidebar-sticky` wrapper the sidebar layout depends on, plus the meta description, the nav `aria-label`, the `aria-live` region, and the new policy, with its three load-bearing elements called out. Rebuilding the shell from the old template would have broken the layout.
- `docs/PRD.md`: Sections 7, 13, 16, 18, 19, 20, 23, 26, 27, 29, 30, 31, and 32 updated for the four changes. The technical debt table in section 30 now shows three items struck out as fixed. Section 31 gained a Content Security Policy subsection recording the policy, the reasoning, and how it was verified. Section 20 adds running the mirror check to the mandatory post-change procedure, and adds never weakening the policy to the "Never" list, on the grounds that a change needing `script-src` relaxed is a change adding a dependency.
- `docs/PRD.md`: Section 7 now permits maintenance tooling explicitly, with the boundary stated: not part of the deployed artifact, never runs in a browser, no third-party package, and the site unchanged if it is deleted.

#### Fixed

- A latent line ending mismatch, found while testing the new script rather than by reading anything. `core.autocrlf` is true system-wide, this repository has no `.gitattributes`, and it stores LF. So git hands a Windows clone CRLF source files, while the `raw` values inside `js/prompts-data.js` stay LF forever, because they are JSON escapes rather than real line breaks and git never rewrites them. A literal comparison would have reported drift on all four prompts in a fresh clone with nothing actually wrong, and the first version of the mirror script did exactly that the moment a file was restored with `git checkout`. The script now normalizes line endings on both sides, since they are a property of the checkout rather than of the content, and always writes the data file with LF. Whether to pin this repository-wide with a `.gitattributes` is recorded as open question 5.

#### Verified

- **The site was rendered for the first time since v1.18.0**, in headless Chrome from `file://`, closing the verification gap that release opened and that v1.27.0 recorded. Three routes checked: the home view (four cards, five nav links, the hero heading), a prompt page (`#/documentation`, correct `h1`, copy button present), and an unknown slug (`#/does-not-exist`, falls through to the home view as designed). No error view on any of them. The card hover treatment built in v1.18.0 had been specified, styled, and documented for ten releases without anyone loading the page.
- **The Content Security Policy was verified enforced, not merely accepted.** A policy that is silently ignored also renders a working page, so passing was not evidence of anything on its own. The page was loaded from `file://` with an inline script and a real remote CDN script injected. Without the policy both executed, which confirms the test itself was valid. With the policy both were blocked, while the favicon data URI, the two same-directory scripts, the stylesheet, and all three routing cases continued to work. `'self'` behaves unusually on `file://` in some browsers and breaking local loading would have violated tenet 2, so this was tested before being committed to rather than after.
- **The mirror script was verified against real drift**, not just against a passing repository. A check that never fails is worthless: a byte was appended to a prompt file, the check failed with the correct message and a non-zero exit, `--sync` repaired it, and the check passed again. It was also confirmed to pass with a CRLF file in the working tree, which is the case that broke the first version.

#### Notes

`tools/` is the fifth folder and the thirteenth file in the project, and the first addition to the repository that is not part of the deployed site. The line drawn in section 7 is deliberate and worth restating: it is tooling rather than a dependency because it never runs in a browser, is never required to build, serve, or deploy, and can be deleted without changing the site. Nothing automates it. There is still no hook and no continuous integration, so it depends on the procedure in section 20 being followed, exactly as the manual page check does.

---

### Prompts v1.27.0 - 2026-08-23

Full documentation audit, run by pointing this project's own Documentation prompt at this repository. The whole codebase was read first, then every document in `/docs` in full, then each was compared against the code before anything was written.

#### Added

- `docs/PRD.md`: Sections 21 through 35, the fifteen sections the Documentation prompt requires that this PRD had never carried. Target Users (the two real personas behind the one-line scope note in section 6, plus the non-user the site deliberately does not serve), User Stories, Feature List (shipped, deliberately not built with the reason for each, and possible future work), Assumptions, Success Criteria, Tenets, Roadmap, Metrics, Runbook, Technical Reference, Security, Public Surface and Retired Items, Documentation Audit Process, Press Release, and Frequently Asked Questions.
- `docs/PRD.md`: Section 26, seven tenets ordered by priority, each stating the tradeoff it resolves rather than a principle everyone would agree with. No dependencies ever, it must run from a file on disk, the markdown file is the truth, write down why not just what, documentation records rather than overrules, a prompt must be safe for a stranger, and small enough to hold in your head.
- `docs/PRD.md`: Section 28, Metrics, which records that this project measures nothing and cannot without breaking a tenet. Analytics would mean a third-party script, GitHub Pages exposes no logs to the repository owner, and the site makes no network calls. The north star, prompts retrieved rather than rewritten, is explicitly not instrumentable. What is actually tracked is six manual checks, and a performance budget is stated structurally: four same-origin requests, roughly 200 KB, zero runtime network calls, and no fifth request permitted because it would mean a dependency.
- `docs/PRD.md`: Section 29, the Runbook, written for someone who has just cloned the repository. Prerequisites are a browser and nothing else, with the five browser features actually required. Records that there is no port because there is no server, that there is no build at all, and that the environment variable reference is empty. Includes the resync procedure for `js/prompts-data.js`, the one-line deploy, rollback, and an eight-row common-errors table covering every failure mode identified during the audit.
- `docs/PRD.md`: Section 30, Technical Reference, carrying what section 7 states as constraints. Both data models with every field, type, source, and fallback; a function-by-function contract table for `js/script.js` standing in for the API surface the project does not have; an explicit statement that there is no state management and no storage API is used anywhere; and nine items of known technical debt, each with the correct fix and the reason it has not been done.
- `docs/PRD.md`: Section 31, Security. Confirms by reading every file that no secret, credential, token, or environment variable exists anywhere, that no cookie or browser storage is used, and that no third party receives any data. Records the attack surface honestly rather than claiming there is none: `innerHTML` used for all rendering, `escapeHtml()` not escaping quotes while a markdown link target is written into an `href`, and repository compromise as the realistic worst case. States the dependency policy as a rule: no dependency may be added, for any reason.
- `docs/PRD.md`: Section 32, the item-by-item public surface list the removal policy in section 12 is applied against, which that policy previously required without providing. Nine addressable items each marked public or internal with the consequence of removing it, the state of the empty `REDIRECTS` map, and a complete retired-items table covering all eleven removals since v1.0 so a reader who finds a reference to something deleted can resolve it.
- `docs/PRD.md`: Section 33, Documentation Audit Process, recording how these documents are produced and how they should be handled going forward: the four-file rule, how an audit is run, and the seven writing rules that bind the documents even when nobody is running the prompt.
- `docs/DESIGN.md`: Section 4a, the spacing system. Base unit 2px with a preferred 4px rhythm, derived from the values actually in the stylesheet rather than invented, with a fifteen-step scale mapping each value to what uses it. Records that spacing is deliberately not tokenized and why, and that horizontal padding is the only spacing that changes responsively.
- `docs/DESIGN.md`: Section 12a, Component Patterns. The shared container pattern (surface, border, 10px radius), the interactive state progression, rules for buttons and cards, and an explicit statement that forms and modals do not exist and should not, because a form implies submission which implies a server.
- `docs/DESIGN.md`: Section 12b, Animation and Motion. One duration and one easing curve, `0.15s ease`, used everywhere, with the reasoning for allowing no second value. A complete five-row inventory of everything that moves, and the rules: transition only colour, border, background, and opacity, never `all`, never a layout-affecting property, reveal rather than shift, no entrance animation, and no loading state.
- `docs/DESIGN.md`: Section 12c, notes for a model working on the design. The context that is invisible when editing a single rule: the design is inherited from four sibling sites rather than invented, restraint is the design, the code block is the product, and the specific declarations that are load-bearing.
- `docs/DESIGN.md`: A component spec for the error and status panel, which had shipped since v1.0 in both `js/script.js` and `css/style.css` and appeared in no document. Includes the reasoning for styling it as a neutral information panel rather than an alert.
- `README.md`: Sections the new standard requires and the old README did not have: who the site is for, current status, and a "Learn More" section pointing at `/docs` and naming what each document carries.

#### Changed

- `README.md`: Rewritten to the general-reader standard adopted in v1.26.0. The previous README was written for a developer and carried a Files table of internal paths, a file structure tree, the prompt markdown format, "Running Locally", and the full add, rename, and remove procedures, all of which the standard now bars from the README and routes to `/docs`. It now describes what the site is, what each prompt does in plain language, who it is for, and where the technical detail lives. Nothing was lost: every relocated item landed in sections 29, 30, or 33 of `docs/PRD.md`. Length went from 141 lines to 55.
- `docs/DESIGN.md`: Section 10, Accessibility, rewritten from five bullets. Now states the target as WCAG 2.1 Level AA, carries a contrast table with the warning that muted text on surface is the tightest pair on the site, lists what is implemented including the `aria-live` region and the global `focus-visible` rule, and sets out keyboard navigation expectations. Two gaps are recorded rather than omitted: there is no skip-to-content link, so a keyboard user passes seven stops before reaching the copy button on a prompt page, and that count grows with every prompt added; and the copy confirmation is announced only through an `aria-label` change.
- `docs/DESIGN.md`: Section 9 expanded from a two-row table to the full rule set below 1024px. `height: auto` on `.sidebar-sticky` and `flex-basis: 100%` on `.sidebar-nav` are marked load-bearing, because both are the v1.11.0 bug fixes and each looks like an ordinary declaration that could be tidied away, which would silently reintroduce a shipped bug.
- `docs/DESIGN.md`: Section 2 no longer describes `--color-negative` and `--color-warning` as "unused at v1.0". Both are still unused at v1.27.0. Added why they are reserved rather than deleted, and noted that the error view deliberately does not use `--color-negative`.
- `docs/PRD.md`: Section 13 said `css/style.css` was 509 lines. It is 536, and has been since v1.18.0. Corrected in place rather than flagged, under the mechanical-fact exception now stated in section 33: a line count carries no intent, so nobody could have meant it.
- `docs/PRD.md`: The closing paragraph of section 19 said the Em Dash Audit and Project Onboarding prompts "were retired behind redirects". Those redirects were deleted in v1.24.0. The sentence described the v1.23.0 state and v1.24.0 did not catch it. Corrected. The v1.23.0 patch note still describes the redirects and is deliberately left alone, because a patch note records what happened at the time while that paragraph describes the current state.
- `docs/PRD.md`: Section 19 claimed there were no TODO, FIXME, or HACK markers anywhere in the repository. A literal search now matches in three files. Every match is prose naming the markers, including the sentence making the claim. Reworded to carry the same "naming the thing" exemption that section 11 gives the em dash rule.
- `docs/PRD.md`: Section 19 rewritten. Added a limits-of-the-analysis subsection recording that nothing was executed, no page was rendered, the contrast ratios were not recomputed, the browser support claim is a judgment rather than a checked matrix, and the Pages configuration is unreadable from the repository. The open questions list was replaced with four new numbered questions.
- `docs/PRD.md`: Sections 6 and 7 gained cross-references to the new sections that carry their detail.

#### Fixed

- Nothing. No defect was found in the code. The audit was read-only through step 3 and every write landed in the four documentation files.

#### Discrepancies recorded rather than corrected

Six new rows were added to the section 18 table in `docs/PRD.md`, numbered 9 through 14. Two blocks in `docs/DESIGN.md` were annotated in place rather than fixed, under the merge rule: **the CSS file structure list in section 11**, which names a `.site-layout` class that does not exist, describes `.site-wrapper` as flex when it is the grid, lists the blocks out of the file's actual order, and omits four blocks entirely; and **the shell template in section 12**, which omits the `.sidebar-sticky` wrapper that the sidebar layout depends on, along with the meta description and two ARIA attributes. Rebuilding the shell from that template would break the layout, so each now carries an inline note recording the observed reality and directing the reader to `index.html` and `css/style.css` as authoritative. Both remain open question 1 for the author.

#### Audit findings, no change required

- **Mirror integrity: clean.** All four `prompts/*.md` files are byte-identical to their `js/prompts-data.js` entries, with no orphan in either direction.
- **Em dash sweep: zero violations.** All three forms were searched independently across all twelve files. Eight matches, every one an instance that names the character it prohibits: three in section 11 of `docs/PRD.md`, one in the Documentation prompt's Writing Style section, its mirror in `js/prompts-data.js`, and two historical patch notes describing the rule. All are exempt under section 11. No double dash is used as punctuation anywhere. Every document written in this audit was checked the same way before being saved.
- **Security sweep: clean.** No secret, credential, token, API key, or environment variable anywhere in the repository. No `fetch`, `XMLHttpRequest`, `localStorage`, `sessionStorage`, or `indexedDB` in any file. The only outbound URLs are the W3C SVG namespace inside the favicon data URI and two links to the author's own domain.
- **No orphan CSS.** Every class used in `index.html` and `js/script.js` is defined in `css/style.css`.
- **Prompt Content Rules: clean.** No prompt instructs its reader to push, commit, or publish, and none references the author's accounts, services, or paths.
- **No TODO, FIXME, or HACK markers.** See the note above on why a literal search matches anyway.

---

### Prompts v1.26.0 - 2026-08-23

#### Changed

- `prompts/documentation.md`: Repurposed the README specification. The README is now the public front door, written for a general reader rather than a developer, and asks for what the site offers in plain language, who it is for, current status, and where to learn more. Install steps, commands, ports, environment variables, build instructions, version numbers, and dependency lists are explicitly barred from it and belong in `/docs`. This holds for every project regardless of type: developers are served by `PRD.md`, so the README never has to compromise for them.
- `prompts/documentation.md`: Relocated the evicted technical content rather than duplicating it. The Runbook section now opens by stating that it carries everything a developer needs to run the project, since the README deliberately does not, and assumes a reader who has just cloned the repository. It gained a Prerequisites bullet (runtime, package manager, and system requirements, each at the version the project actually needs rather than the newest available), absorbed installation order, start command, and default port into its local setup bullet, and gained an environment variable reference covering key names, what each does, and whether it is required, never the values.
- `prompts/documentation.md`: Replaced the "Do not pad" standard. In `/docs`, and in `PRD.md` above all, completeness now beats brevity: a section that restates context to stand on its own is doing its job, because a reader may arrive at it directly and should not have to assemble an answer from three other sections. The standard still bars filler, marketing language, and sentences carrying no new information, on the principle that thorough means more facts rather than more words around the same facts. The README is named as the exception and stays tight.
- `prompts/documentation.md`: The live site link is now satisfiable by a plain statement that there is no hosted instance, so a required section can no longer invite invention on a project that has never been deployed.
- `js/prompts-data.js`: Resynced the `documentation` entry from its source `.md` file.
- `docs/PRD.md`: Recorded this release in the version history.

#### Removed

- `prompts/documentation.md`: The `ReadMe` PRD section added alongside the README repurpose. Every bullet in it was already required elsewhere: the tech stack by Technical Requirements, installation and build and deploy by Runbook, and environment variables by both Runbook and Security. Three sections claiming the same facts is the duplication the README change set out to remove, relocated rather than fixed, so the section was dropped and the two bullets it uniquely contributed (prerequisites, default port) were folded into Runbook. This also removed a duplicated artifact line and the `ReadMe` casing inconsistency.

---

### Prompts v1.25.0 - 2026-08-23

#### Added

- `prompts/documentation.md`: The read-only constraint from the retired Project Onboarding prompt, at the top of "Steps to follow". Steps 1 through 3, the codebase crawl and the read of every existing document, now forbid writing, editing, renaming, deleting, and moving any file, along with installers, migrations, formatters, builds that write output, and any state-changing version control command. Writing begins at step 4 and is limited to the documentation files the prompt names. This was the one part of Project Onboarding not carried over in v1.22.0, on the reasoning that the Documentation prompt exists to write files. Scoping it to the analysis steps rather than the whole run resolves that: the prompt already required a full scan before touching any documentation, and this makes the requirement enforceable instead of advisory.
- `prompts/documentation.md`: Also carried over the instruction not to skip a step because it looks obvious, and to say so explicitly when a step turns up nothing rather than staying silent.

#### Changed

- `prompts/documentation.md`: The steps in "Steps to follow" are now numbered, so the read-only constraint can name the range it applies to. Step 1 gained "read files rather than inferring from their names" and step 2 gained "read each in full", both from the retired prompt.
- `js/prompts-data.js`: Resynced the `documentation` entry from its source `.md` file.
- `docs/PRD.md`: Recorded this release in the version history.

---

### Prompts v1.24.0 - 2026-08-23

#### Removed

- `js/script.js`: All three `REDIRECTS` entries. The map is now empty. `github-wiki-setup` to `github-wiki` (added v1.17.0) and the two added in v1.23.0 all pointed at prompt slugs, and prompt slugs are not a public surface.

#### Changed

- Corrected the definition of public facing, which the redirect policy depends on. The public surface of this project is the deployed page, `index.html` and the asset paths it loads. Everything under `prompts/` is source. A prompt's slug is derived from its source filename rather than being a contract of its own, so renaming or removing a prompt is an internal change and needs no redirect. The router already renders the home view for an unrecognized slug, so an old hash resolves to a working page.
- `js/script.js`: The `REDIRECTS` map is kept, empty, with its comment rewritten to explain when an entry would be warranted. The mechanism costs one property lookup per navigation and would otherwise have to be rebuilt if a genuine public address is ever retired.
- `docs/PRD.md`: Rewrote both procedures in section 12. "Renaming Prompts" no longer pairs a slug change with a redirect and drops the four rules for the map, keeping the permanence, no-chaining, and no-reuse rules scoped to genuine public addresses in "Removing Prompts". "Removing Prompts" now draws the line at the deploy boundary rather than at whether a prompt is visible in the navigation. Updated the section 14 flow description, the section 16 binding rules, the section 18 redirect bullet, and the section 20 working practice.
- `prompts/documentation.md`: The Deprecation and Removal section defined public facing as anything with an address someone could be holding, which swept in source files. It now draws the line at the deploy boundary, states that a source file is not public facing even when its name appears in a built URL, and requires the PRD to say where the project puts that boundary, since the rule cannot be applied without knowing which side a file is on.
- `README.md`: Rewrote the "Renaming a Prompt" and "Removing a Prompt" sections to match, and corrected the note added in v1.23.0 that described the two retirements as redirected.
- `js/prompts-data.js`: Resynced the `documentation` entry from its source `.md` file.
- `docs/PRD.md`: Recorded this release in the version history.

Patch notes for v1.17.0 and v1.23.0 still describe redirects that no longer exist. They are left as they are, since they record what happened at the time.

---

### Prompts v1.23.0 - 2026-08-23

#### Removed

- `prompts/em-dash-audit.md`, `prompts/project-onboarding.md`: Retired. The Documentation prompt absorbed both in v1.22.0, the em dash rule as its Writing Style section and the onboarding analysis as its Conventions, Documentation Versus Reality, Risks and Open Questions, and Working Practice sections.
- `js/prompts-data.js`: Removed the two corresponding entries. Four prompts remain: Add Prompt, Documentation, Mobile Audit, and GitHub Wiki.
- `README.md`: Removed the two rows from the Files table and the two lines from the file structure tree.

#### Added

- `js/script.js`: Two `REDIRECTS` entries, `em-dash-audit` to `documentation` and `project-onboarding` to `documentation`. Unlike the three prompts deleted in v1.19.0, these two were live in the sidebar and home list, so their slugs are public addresses that people may hold. Section 12 of `docs/PRD.md` requires a redirect in that case, not a plain delete. The map now holds three entries.

#### Changed

- `prompts/documentation.md`: The description named the Em Dash Audit and Project Onboarding prompts, which no longer exist. Rewritten to describe the same capability without referring to them.
- `README.md`: The hash routing example used `index.html#/em-dash-audit`, and the prompt markdown format example used the Em Dash Audit frontmatter. Both now use live prompts. Added a note to the hidden prompts paragraph explaining why these two retirements got redirects when the v1.19.0 deletions did not.
- `docs/PRD.md`: Section 11 referred to the Em Dash Audit prompt as the place the prohibited characters are quoted; it now points at the Writing Style section of the Documentation prompt. Updated the section 13 file counts (12 files, four prompts), the section 18 mirror and redirect map bullets, and closed the open question from v1.22.0.
- `js/prompts-data.js`: Resynced the `documentation` entry from its source `.md` file.

---

### Prompts v1.22.0 - 2026-08-23

#### Added

- `prompts/documentation.md`: Absorbed the Project Onboarding and Em Dash Audit prompts as required PRD sections. The prompt now produces a document that covers what those two prompts produced separately, in one pass.
- `prompts/documentation.md`: New "Conventions" section, deriving the house style from the code rather than from any style guide the project contains. Covers naming, formatting, organization, comment density, error handling, and commit and branching style read from version control history. Where a convention is inconsistent it records which form is dominant and which files deviate, so the next contributor matches the majority rather than the last file they opened.
- `prompts/documentation.md`: New "Writing Style" section carrying the em dash rule as a default: prohibited in all three forms, searched independently because a search for one will not catch the other, CSS custom properties untouched, the six replacements including the permitted single hyphen, and the exemption for instances that name the character they prohibit. The prompt applies the style to every document it writes, then sweeps the rest of the project and records what it found.
- `prompts/documentation.md`: New "Documentation Versus Reality" section, recording each discrepancy rather than quietly fixing it, with the code treated as the truth about what is and the documentation as the truth about what was intended. Resolved entries stay in the table with a note on how they were resolved.
- `prompts/documentation.md`: New "Risks and Open Questions" section, covering what the analysis did not understand, fragile areas, what is dangerous to change, work already in progress, and numbered open questions that are folded back in as answered rather than deleted.
- `prompts/documentation.md`: New "Working Practice" section, written as concrete instructions rather than principles: what to check before editing, what never to do with the reason attached, a table mapping each kind of change to the file to open first, and how to verify a change.
- `prompts/documentation.md`: Four new standards in the audit preamble, carried over from Project Onboarding. Merge rather than overwrite, since documentation holds intent that cannot be reconstructed from code. Every policy in the specifications is a default that applies only where the project states no rule of its own, with conflicts flagged rather than silently resolved. Read files rather than inferring from their names, and mark uncertainty as uncertainty. Do not pad.

#### Changed

- `prompts/documentation.md`: Frontmatter description and on-page description updated for the wider scope.
- `README.md`: Updated the Files table row for the Documentation prompt.
- `js/prompts-data.js`: Resynced the `documentation` entry from its source `.md` file.
- `docs/PRD.md`: Recorded this release in the version history.

`prompts/em-dash-audit.md` and `prompts/project-onboarding.md` were left in place. Both are live on the site, so their slugs are public addresses, and removing either would need a redirect under the policy in `docs/PRD.md` section 12. Whether they stay as standalone prompts now that the Documentation prompt covers their ground is an open question for the author.

---

### Prompts v1.21.0 - 2026-08-23

#### Changed

- `prompts/documentation.md`: The removal policy is now a default rather than an override. The prompt checks first whether the project already states a removal rule of its own, in its docs, a contributing guide, or a consistent pattern in the changelog and code. If it does, that rule is documented and left alone, on the grounds that the audit records how a project works rather than overruling how it has decided to work. Where an existing rule and the default differ, both are kept and the difference is flagged for the author instead of one silently replacing the other. The public-facing versus internal rule from v1.20.0 applies only where the project states no rule at all.
- `js/prompts-data.js`: Resynced the `documentation` entry from its source `.md` file.
- `docs/PRD.md`: Recorded this release in the version history.

---

### Prompts v1.20.0 - 2026-08-23

#### Changed

- `prompts/documentation.md`: The Deprecation and Removal section added in v1.19.0 asked the model to state whatever removal rule a project already had. It now prescribes this site's rule instead: a redirect is decided by whether the thing being removed is public facing, not by the fact that it is being removed. Anything with an address someone outside the project could be holding (URL, route, slug, permalink, published artifact, exported name) is retired behind a redirect or equivalent shim. Anything internal is pruned entirely, with no redirect, alias, stub, or tombstone. The prompt tells the model to adapt the mechanism to whatever the project has, to record the reasoning, and to say so explicitly if the project has no redirect mechanism at all.
- `prompts/documentation.md`: The section also now requires the public surface list to be specific enough to answer the question for any given file, states that compatibility entries are permanent, never chained, and never reused for different content, and records that historical changelog entries are not rewritten when something is deleted.
- `js/prompts-data.js`: Resynced the `documentation` entry from its source `.md` file.
- `docs/PRD.md`: Recorded this release in the version history.

---

### Prompts v1.19.0 - 2026-08-23

#### Removed

- `prompts/consolidate-documents.md`, `prompts/docs-folder-audit.md`, `prompts/documentation-audit.md`: Deleted. All three were documentation prompts superseded by the Documentation prompt, and had been hidden from the sidebar and home list since v1.9.0. No redirects were added. A redirect exists to keep a public URL working, and a prompt that has been off the navigation since v1.9.0 is not one anyone is being handed. Adding three permanent redirect entries would have been maintenance in exchange for nothing.
- `js/prompts-data.js`: Removed the three corresponding entries. Six prompts remain.
- `README.md`: Removed the three rows from the Files table and the three lines from the file structure tree.

#### Added

- `docs/PRD.md`: New "Removing Prompts" subsection in section 12. The rule is that a redirect is decided by whether the thing being removed is public facing, not by whether it is being removed. A live prompt's slug is a public address and gets retired behind a redirect. Anything already off the navigation is deleted outright. The same test applies to any file in the repository. Includes the five-step delete procedure and the note that historical patch notes are left alone.
- `README.md`: New "Removing a Prompt" section summarizing the policy and pointing at the PRD for the procedure.
- `prompts/documentation.md`: New "Deprecation and Removal" section in the required PRD sections, covering the project's removal policy, an explicit list of what is publicly addressable, and a record of retired items. Any project documented with this prompt now has to state its own version of the rule rather than deciding it case by case.

#### Changed

- `prompts/documentation.md`: The description compared this prompt to Consolidate Documents and Documentation Audit by name, both now deleted. Rewritten to describe the depth it folds into the PRD without referring to prompts that no longer exist. Also corrected "Tenents" to "Tenets" in the required sections list.
- `js/prompts-data.js`: Resynced the `documentation` entry from its source `.md` file.
- `docs/PRD.md`: Updated the section 13 file counts (14 files, six prompts), added the removal rule to section 16, marked item 8 of the section 18 discrepancy table resolved by deletion, rewrote the two bullets in section 18 that described the hidden prompts in the present tense, closed two open questions in section 19, and added the delete case to section 20.

---

### Prompts v1.18.0 - 2026-08-23

#### Added

- `css/style.css`: Built the card hover treatment on the home prompt list. `docs/DESIGN.md` had specified `--color-card-hover` as a card hover background and `--color-purple` as a gradient accent since v1.0, but neither token was ever referenced and `.prompt-list-item:hover` explicitly set `background: none`. Each list item is now a bordered, rounded card on `--color-surface` with a 12px gap between cards, hovering to `--color-card-hover` with an accent border and a 2px teal to purple gradient bar across the top. The bar is an absolutely positioned `::before` rather than a real `border-top`, so the card does not shift by 2px when it appears, and `overflow: hidden` clips it to the corner radius.
- `docs/PRD.md`: Sections 13 through 20, written by a full read-only onboarding pass over the repository. Structure map, architecture and flow traced from the code, code conventions derived from the files, the complete list of binding rules with their sources, stack and deployment, a documentation versus reality table, risks and open questions, and a working practice section covering what to check before editing and where to look for each kind of change.
- `docs/PRD.md`: The single hyphen is now a documented replacement in the section 11 Writing Style table, with a note that the prohibition covers only the em dash character, the `&mdash;` entity, and the double dash, and that instances naming the prohibited character are left in place.

#### Changed

- Ran the Em Dash Audit across the project. Replaced 25 literal em dashes with single hyphens: the titles of `docs/PRD.md`, `docs/DESIGN.md`, and `docs/PATCHNOTES.md`, and all 20 version headings in this file. Replaced one prose em dash in the v1.11.0 entry with a comma, three in the section 8 `/docs/` bullets of `docs/PRD.md` with colons, and one double dash used as punctuation in `prompts/documentation-audit.md` with a colon. The em dashes inside the section 11 prohibition list and inside the Em Dash Audit prompt were left alone, since those lines exist to name the character.
- `prompts/em-dash-audit.md`: The prompt now instructs that a single hyphen is permitted and encouraged where context justifies it, and is preferred in document titles, section headings, and version lines, since it is the closest visual match to the em dash it replaces. Also added an instruction to leave instances that the text needs in order to mean anything.
- `js/prompts-data.js`: Resynced the `em-dash-audit` and `documentation-audit` entries from their source `.md` files.
- `docs/DESIGN.md`: Rewrote the Home Page Prompt List component spec for the card layout, added the card hover to the animation allowance in section 13, and bumped the document to 1.6.
- `docs/PRD.md`: The `**Version:**` header field now tracks the current release rather than sitting at 1.0 forever. Recorded that GitHub Pages publishes `main` at the repository root by manual push, which the onboarding pass could not determine from the repository alone. Marked items 2, 5, and 6 of the section 18 discrepancy table as resolved and rewrote the open questions list.

---

### Prompts v1.17.0 - 2026-08-23

#### Added

- `js/script.js`: A `REDIRECTS` map and a redirect step in `route()`. A retired slug now rewrites the hash to the current one, which re-enters the router and renders the right prompt with a canonical address bar. Every redirect is guarded on its target existing, so a stale entry falls through to the home view instead of trapping the reader in a dead end. First entry: `github-wiki-setup` to `github-wiki`.
- `docs/PRD.md`: New "Renaming Prompts" subsection in section 12, making the redirect practice canonical. A slug is a public URL, so a slug change is always paired with a redirect rather than done bare. Documents the five-step rename procedure and four rules for the map: entries are permanent, redirects never chain, retired slugs are never reused for a different prompt, and every redirect is guarded on its target. Also records that historical patch notes and version history rows are not rewritten during a rename.
- `README.md`: New "Renaming a Prompt" section summarizing the practice and pointing at the PRD for the full procedure.

#### Changed

- `prompts/github-wiki-setup.md` renamed to `prompts/github-wiki.md`, with the slug changed from `github-wiki-setup` to `github-wiki` so it matches the title set in v1.16.0. Renamed with `git mv` to preserve file history. The old URL (`index.html#/github-wiki-setup`) keeps working through the new redirect map. This is the rename that v1.16.0 deliberately deferred for lack of a redirect mechanism.
- `js/prompts-data.js`: Updated the slug for that entry. The `raw` value was resynced from the renamed `.md` file rather than hand-edited.
- `README.md`: Updated the Files table and file structure tree to the new filename.
- `css/style.css`: Widened the content area. `--content-max` changed from a flat `820px` to `max(820px, calc(75vw - 56px))`, so the content block measures 75vw on wide screens while the 820px floor holds line length steady on laptops. The floor also protects the layout below the 1023px breakpoint, where the sidebar collapses to a full-width top nav and a bare `75vw` would have shrunk the content instead of widening it. Mobile rendering is unchanged.
- `docs/DESIGN.md`: Updated the Content Area max width spec and documented why the `max()` floor is load-bearing.
- `docs/PRD.md`: Recorded this release in the version history.

---

### Prompts v1.16.0 - 2026-08-23

#### Changed

- `prompts/github-wiki-setup.md`: Renamed the prompt from "GitHub Wiki Sync" to "GitHub Wiki". The frontmatter `description` and body were left as they are, since both still describe the prompt accurately. The slug stays `github-wiki-setup` so existing direct links (`index.html#/github-wiki-setup`) keep working, and the filename is unchanged.
- `js/prompts-data.js`: Resynced the `github-wiki-setup` entry from its source `.md` file.
- `README.md`: Updated the Files table description to the new title.
- `docs/PRD.md`: Recorded this release in the version history.

Earlier patch notes and version history rows that mention "GitHub Wiki Sync" were deliberately left alone. They are a record of what the prompt was called at the time.

---

### Prompts v1.15.0 - 2026-08-23

#### Added

- `prompts/project-onboarding.md`: Ninth prompt, "Project Onboarding". Puts a model through an eight-phase, read-only intake of an unfamiliar project before it is allowed to change anything: structure map, identity and purpose, a full read of every documentation file, technical foundation (dependencies, scripts, build, test, deploy), architecture traced from real entry points rather than from the docs, conventions derived from the code itself, a documentation-versus-reality cross-check, and an explicit risks-and-unknowns pass. Phases 1 through 8 forbid all writes, installs, and state-changing version control commands.
- The deliverable is not a chat briefing. Everything established is merged into `PRD.md`, the single file the prompt is permitted to write, so the understanding survives the session. The merge is additive: it preserves intent and rationale that cannot be reconstructed from code, matches the PRD's existing heading structure and tone, and where findings contradict the PRD it keeps both and marks the conflict for a human to resolve rather than silently correcting the document from code. No other file is touched, including the README and these patch notes; errors found elsewhere are reported instead.
- `js/prompts-data.js`: Regenerated to include `project-onboarding`.

#### Changed

- `README.md`: Added `prompts/project-onboarding.md` to the Files table and the file structure tree.
- `docs/PRD.md`: Recorded this release in the version history.

---

### Prompts v1.14.0 - 2026-07-06

#### Changed

- `prompts/github-wiki-setup.md`: Renamed the "Changelog" wiki page to "Patch Notes" (`Patch-Notes.md`) throughout the prompt's frontmatter description, on-page description, and prompt text, to match this site's own terminology (`docs/PATCHNOTES.md`) rather than the more generic "Changelog" label.
- `js/prompts-data.js`: Regenerated to mirror the renamed page.

---

### Prompts v1.13.0 - 2026-07-06

#### Changed

- `prompts/github-wiki-setup.md`: Reworked into "GitHub Wiki Sync" (title and description regenerated to match). Added an update mode: if the wiki repo already exists, the prompt pulls the current pages, diffs them against the README, PRD, PATCHNOTES, DESIGN, and any other project docs, and summarizes outdated sections, missing features, stale links, and content drift before editing anything. Page creation is no longer a fixed set beyond Home, Product Overview, and Changelog; the prompt now uses judgment on wiki information architecture, creating pages like FAQ, Roadmap, Architecture, Getting Started, Troubleshooting, or API Reference wherever a topic is distinct and cohesive. Added a step to create or keep a `_Sidebar.md` page in sync with the full current page structure.
- `js/prompts-data.js`: Regenerated to mirror the reworked `github-wiki-setup.md`.
- Also caught and fixed two more em dashes in the prompt's body text, in the Product Overview and Changelog descriptions, that were missed in the previous pass, replacing both with parentheses per the site's em dash prohibition.
- `README.md`: Updated the `github-wiki-setup.md` Files table description to match the reworked prompt.
- `docs/PRD.md`: Recorded this release in the version history.

---

### Prompts v1.12.0 - 2026-07-06

#### Added

- `prompts/github-wiki-setup.md`: Eighth prompt, "GitHub Wiki Setup". Reviews every documentation markdown file in a project, then sets up a GitHub wiki sourced from them. Checks first whether the wiki repo is initialized (GitHub only creates it after one manual page is added via the web UI) and stops to ask if it isn't. Curates, rather than dumps verbatim, content into a Home page (overview plus table of contents), a Product Overview page (stable current-state PRD sections), a Changelog page (condensed patch notes), and any other page mapping to a distinct PRD section. Rewrites internal/planning language for a public audience and drops internal-only notes.
- `js/prompts-data.js`: Regenerated to include `github-wiki-setup`.

#### Changed

- `README.md`: Added `prompts/github-wiki-setup.md` to the Files table and file structure tree.
- `docs/PRD.md`: Recorded this release in the version history.

---

### Prompts v1.11.0 - 2026-07-05

#### Fixed

- `css/style.css`: Ran the Mobile Audit prompt against the live site (headless Chrome via CDP, `scrollWidth`/`clientWidth`/`getBoundingClientRect()` measurements at 375–1920px, not screenshots) and found the mobile/tablet header (< 1024px) was badly broken. Root cause: `.sidebar-sticky` sets `height: 100vh` for the desktop vertical sidebar, and the `@media (max-width: 1023px)` block that converts it into a horizontal header never reset that height, so the header stayed full-viewport-tall with its logo/nav/support button vertically centered inside, pushing all page content roughly 1200px below the fold on a typical mobile screen. Added `height: auto` to `.sidebar-sticky` in that media query.
- `css/style.css`: Secondary bug in the same header: `.sidebar-nav` shared its row with `.sidebar-logo` instead of dropping to its own line, squeezing the 5 nav links into a ~150px-wide column that stacked one link per row instead of wrapping across the full width (the existing `margin-bottom` on `.sidebar-logo` already implied the intended layout was logo-then-nav-below). Added `flex-basis: 100%` to `.sidebar-nav` in the same media query so it wraps full-width beneath the logo.
- No page-level horizontal overflow, `overflow` shorthand conflicts, bare `1fr` grid overflow, flex `min-width: auto` overflow, or margin/gap double-spacing were found anywhere else at any of the seven audited breakpoints across the home page and all seven prompt detail pages.

---

### Prompts v1.10.0 - 2026-07-05

#### Added

- `prompts/mobile-responsive-audit.md`: Seventh prompt, "Mobile Audit". Audits every page of a site at seven fixed breakpoints (375px to 1920px) for horizontal overflow, container overflow, unwrapped toolbars, modal sizing, and clipped text. Targets four specific CSS bug patterns: the `overflow` shorthand canceling `overflow-x`, bare `1fr` grid tracks forcing page overflow from wide content, flexbox children ignoring their parent's width due to default `min-width: auto`, and doubled spacing from `margin` stacking with a flex/grid `gap`. Verifies fixes by injecting a debug script to read `scrollWidth`/`clientWidth` and bounding rectangles rather than relying on screenshots, since headless browsers enforce a minimum viewport width. Flags any fix that changes content presentation for a design decision before implementation, and ends by updating the project's existing changelog and planning docs.
- `js/prompts-data.js`: Regenerated to include `mobile-responsive-audit`.

#### Changed

- `README.md`: Added `prompts/mobile-responsive-audit.md` to the Files table and file structure tree.
- `docs/PRD.md`: Recorded this release in the version history.

---

### Prompts v1.9.0 - 2026-06-27

#### Added

- `js/script.js`: Support for an optional `hidden` frontmatter flag on prompts. `parsePrompt` reads `hidden` (true/yes/1), and `buildSidebar` and `renderHome` skip any prompt where it is set. `findPrompt` and routing are unchanged, so hidden prompts stay reachable by direct link (`index.html#/<slug>`).

#### Changed

- `prompts/consolidate-documents.md`, `prompts/docs-folder-audit.md`, `prompts/documentation-audit.md`: Added `hidden: true` to the frontmatter. These three prompts are retired from the sidebar and home list but kept on the backend; existing direct links still resolve. The newer Documentation prompt supersedes them in the navigation.
- `js/prompts-data.js`: Regenerated to mirror the three `hidden: true` frontmatter additions.
- `README.md`: Noted which prompts are hidden from navigation and still reachable by direct link.
- `docs/PRD.md`: Documented the `hidden` frontmatter flag in the navigation and prompt markdown sections, and recorded the release in the version history.
- `docs/DESIGN.md`: Documented the optional `hidden: true` key in the prompt markdown template and version history.

---

### Prompts v1.8.0 - 2026-06-27

#### Added

- `prompts/documentation.md`: Sixth prompt. The most comprehensive of the documentation prompts. Crawls the entire codebase first, then consolidates all documentation into four core files (README.md at the root; PRD.md, DESIGN.md, and PATCHNOTES.md in `/docs`), creates any missing files, and enforces the correct folder structure. Folds the full depth of a larger doc suite into a single PRD with required sections for Tenets, Roadmap, Metrics, Runbook, Technical Requirements, Security, a Press Release, and an FAQ, so the project can be understood from `/docs` alone without reading code.
- `js/prompts-data.js`: Regenerated to include `documentation`.

#### Changed

- `README.md`: Added `prompts/documentation.md` to the Files table and file structure tree.
- `docs/PRD.md`: Added an "Adding Prompts" process note documenting the standing workflow for adding a new prompt and keeping documentation in sync, and recorded this release in the version history.

---

### Prompts v1.7.0 - 2026-06-14

#### Added

- `prompts/docs-folder-audit.md`: Fifth prompt. Audits every document in `/docs` against the current codebase. Crawls all files first to build a complete picture of the project, then reviews each doc in `/docs` for outdated, missing, or inaccurate content and rewrites it. Ends with a per-file summary of what changed and why.
- `js/prompts-data.js`: Regenerated to include `docs-folder-audit`.

#### Changed

- `README.md`: Added `prompts/docs-folder-audit.md` to the Files table and file structure tree.

---

### Prompts v1.6.0 - 2026-06-13

#### Changed

- `style.css` → `css/style.css`: Moved stylesheet into a dedicated `css/` subfolder.
- `prompts-data.js` → `js/prompts-data.js`: Moved prompt data file into a dedicated `js/` subfolder.
- `script.js` → `js/script.js`: Moved main script into the `js/` subfolder.
- `index.html`: Updated `<link>` and `<script>` references to reflect new asset paths (`css/style.css`, `js/prompts-data.js`, `js/script.js`).
- `README.md`: Updated Files table and file structure tree to reflect new `css/` and `js/` folder layout.
- `docs/DESIGN.md`: Updated shell template, CSS file structure heading, and version history.

---

### Prompts v1.5.0 - 2026-06-13

#### Added

- `prompts/add-prompt.md`: Fourth prompt. A meta-prompt for adding new prompts to the site. Accepts a raw prompt text and instructs Claude Code to generate the title and one-line description, create the markdown file in `prompts/`, mirror it into `prompts-data.js`, update the Files table in `README.md`, and add a version entry to `docs/PATCHNOTES.md`.
- `prompts-data.js`: Regenerated to include `add-prompt`.

#### Changed

- `README.md`: Added `prompts/add-prompt.md` to the Files table and file structure tree.

---

### Prompts v1.4.0 - 2026-06-13

#### Added

- `prompts/consolidate-documents.md`: Third prompt. Consolidates all project documentation into four core files: README.md at the root, and PRD.md, DESIGN.md, and PATCHNOTES.md inside `/docs`. Creates any missing files with required sections. Enforces the correct folder structure and moves misplaced files. A leaner alternative to the Documentation Audit prompt, targeting four documents instead of eleven.
- `prompts-data.js`: Regenerated to include `consolidate-documents`.

#### Changed

- `README.md`: Added `prompts/consolidate-documents.md` to the Files table and file structure tree.

---

### Prompts v1.3.0 - 2026-06-13

#### Changed

- `index.html`: Sidebar logo updated from "Prompts." to "Azqato's Prompts." Added Support button to the bottom of the sidebar, linking to `https://azqato.github.io/support.html` in a new tab.
- `script.js`: Homepage h1 updated from "Prompts." to "Claude Code Prompts." (teal dot preserved). Browser tab title updated to "Azqato's Prompts" on home view. Prompt pages now set the tab title to just the prompt name, with no site suffix.
- `style.css`: `.sidebar-sticky` changed from `max-height: 100vh` to `height: 100vh` with `display: flex; flex-direction: column` so the Support button pins to the bottom via `margin-top: auto`. `.sidebar-nav` gains `flex: 1` to fill available space. Added `.sidebar-support` and `.support-btn` styles with hover state matching the site's teal accent. Mobile breakpoint updated to flow the support button inline with nav links.
- `docs/DESIGN.md`: Updated sidebar spec, navigation spec (support button added), hero section spec, shell template, and version history.
- `docs/PRD.md`: Updated navigation section to document the support button.
- `README.md`: Project title updated to "Azqato's Prompts".

---

### Prompts v1.2.0 - 2026-06-13

#### Changed

- `prompts/em-dash-audit.md`: Removed "Finally, push everything to GitHub." from the prompt text. Prompts are shared publicly and must not instruct users to push to any remote repository. Rewrote the closing instruction to: "After making these changes, ensure the patch notes and documentation files are all up to date describing the changes you just made." Updated the frontmatter description and on-page description paragraph to remove all mention of pushing to GitHub.
- `prompts-data.js`: Regenerated to mirror the updated `em-dash-audit.md`.
- `docs/PRD.md`: Added a Prompt Content Rules section to the Writing Style rules. Documents that prompts must not include GitHub push instructions or any account-specific actions, and requires this to be audited before any new prompt is published.

---

### Prompts v1.1.0 - 2026-06-13

#### Added

- `prompts/documentation-audit.md`: Second prompt. Runs a full documentation audit on any project: reads all source files and existing docs, then creates or updates the complete suite of eleven documents (README, PRD, TRD, DESIGN, PATCHNOTES, PRFAQ, TENETS, METRICS, ROADMAP, SECURITY, RUNBOOK) to their required specifications. Also enforces the correct folder structure, moving any misplaced files into `/docs`.

#### Removed

- `first prompt example.txt.txt`: Source text for the first prompt. Content is now canonical in `prompts/em-dash-audit.md`. No longer needed.
- `message.txt`: Source text for the documentation audit prompt. Content is now canonical in `prompts/documentation-audit.md`. No longer needed.

#### Changed

- `prompts-data.js`: Regenerated to include both `em-dash-audit` and `documentation-audit`.
- `docs/PATCHNOTES.md`: Corrected v1.0.0 design decisions note about footer (period is not teal; it inherits the muted text color).

---

### Prompts v1.0.0 - 2026-06-13

**Initial release.**

#### Added

- `index.html`: Single-page shell (sidebar, content area, footer). Renders the home view and every prompt view via hash-based routing. No per-prompt HTML files.
- `prompts/em-dash-audit.md`: First prompt, authored in markdown. Documents the full em dash audit workflow for Claude Code projects, covering both the literal Unicode character and the `&mdash;` HTML entity form, double dash punctuation handling, CSS custom property exceptions, and context-sensitive replacement rules (comma, colon, semicolon, parentheses, period). Includes instructions to update `docs/PRD.md` with a Writing Style section and push all changes to GitHub after the audit is complete.
- `prompts-data.js`: Embedded copy of every prompt markdown file as `window.PROMPTS_DATA`, loaded via a `<script>` tag. This lets the site read prompt content with no server, so it runs by opening `index.html` directly (`file://`) while keeping the `.md` files as the readable source.
- `style.css`: Full design system stylesheet. Implements the Azqato brand system: `#0d1117` background, `#161b22` surface, `#00d4a0` teal accent, system font stack, CSS Grid sidebar layout, code block component, copy button with state transitions, home page prompt list, hero section, responsive breakpoints at 1024px and 768px, reduced motion support.
- `script.js`: Parses the embedded prompt markdown (frontmatter, description, fenced prompt block), builds the sidebar dynamically, handles hash routing, and provides copy-to-clipboard behavior using the native Clipboard API. On click, reads the rendered `<code>` element's text content, writes it to clipboard, updates the button label to "Copied!" for 2 seconds, then resets to "Copy".
- `README.md`: Project overview, how-it-works, files table, docs table, file structure, prompt markdown format, design summary, running locally instructions, and instructions for adding new prompts.
- `docs/PRD.md`: Product requirements. Covers problem statement, solution, goals, non-goals, audience, technical requirements, page structure, navigation, copy button behavior, writing style rules (em dash prohibition in all forms, replacement guidelines, general tone), and prompt addition workflow.
- `docs/DESIGN.md`: Full design specification. Covers design direction, color system with all CSS custom property tokens, typography scale, layout grid, sidebar spec, content area spec, code block component spec, copy button spec, home page prompt list spec, hero section spec, favicon, signature elements, navigation states, footer, responsive behavior, accessibility requirements, CSS file structure, architecture and templates, and what-not-to-do rules.
- `docs/PATCHNOTES.md`: This file.

#### Design Decisions

- Prompts are authored as markdown files in `prompts/`, not as hand-written HTML. Adding a prompt is a content task, not an HTML task.
- The site runs with zero dependencies and no server. Because browsers block `fetch()` on `file://`, prompt markdown is embedded in `prompts-data.js` and loaded with a `<script>` tag, which the browser permits from local disk. The `.md` files remain the canonical, readable source and `prompts-data.js` mirrors them.
- Inherited the Azqato brand system directly from the Stocks methodology site and ComposerAtlas. Consistent accent color (`#00d4a0`), surface colors, sidebar layout, and `h2::before` vertical bar are intentional cross-site design continuity.
- Footer reads "Built by Azqato." with only the wordmark "Azqato" as a teal link. The trailing period sits outside the link and inherits the muted text color, so it is neither colored nor clickable.
- No syntax highlighting at v1.0. Prompt text is plain monospace. The goal is readability and copy speed, not code presentation.
- Code block header bar pattern (label left, copy button right) mirrors common documentation site conventions (Stripe, Tailwind, GitHub) and provides instant affordance for the primary user action.
- Emoji favicon (`💬`) chosen to distinguish the Prompts site from other Azqato properties visually in browser tabs while remaining zero-dependency.
