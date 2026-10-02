# UI-REVIEW.md - Azqato Invests

A review of the user interface, the author's decisions on it, and what was built (v0.16.0, 2026-10-02). The findings below are kept as they were found; the "Done" section says what changed for each.

## How the review was done

- **Date:** 2026-10-02, on the v0.14.3 build.
- **Method:** every page was scrolled top to bottom in headless Edge (Playwright, `channel="msedge"`), at:
  - 1440px wide, in light and dark;
  - 390px wide (a phone), in light.

  Each viewport was captured, and a probe measured small text, tap targets and line lengths.
- **Overall:** dark mode holds up well everywhere. Nearly every issue below shows up in light mode, on the phone, or in both.
- **Content rule:** every fix suggested here changes presentation only. None cuts or rewords source content (core rule).

## Author's decisions (2026-10-02)

Decided in the brainstorming session; nothing is built yet.

| Topic | Decision |
|---|---|
| Footers | Merge into the site footer: one footer per page, carrying any wording only the source footers had (for example the VIX "Past performance is not indicative of future results"). |
| Home | Merge "Explore the site" and "Projects" into one grid. |
| Page width | **C, everything full width to 1400px** (chosen 2026-10-02 from three previews: A, grids wide with prose capped at about 75 characters; B, one column of about 1100px; C, everything full width). |
| Phone | VIX tables stack as cards; the screener gets a pinned ticker column and a scroll shadow. |
| Small text | 12px floor; table headers about 11.5px uppercase. |
| Sidebar | Collapse the groups that don't hold the current page. |
| VIX pages | Same status wording on the Dashboard and Custom; result (reading and donut) first on Custom; VIX Strategy uses the site's headings and boxes. |
| LIVE vs CACHED | Investigate as a bug and fix it in this site's copy. |
| Resources | Masonry columns. |
| Icons | Keep emoji, but pick a matching style and size. |
| FAQ chip | Restyle "Strategy Q&A" as a plain label, not a button. |
| Table fonts | Figures use the site's sans font with tabular (aligned) digits. |
| Azqato nav on phones | Fold its links into the menu drawer. |
| Tap targets | At least 24px on phones, by padding; text size unchanged. |
| Width examples | Build the three example pages together with the other fixes, as previews that don't change the real site. **Built 2026-10-02:** previews/index.html (made by scripts/previews.py), with Market Overview, Stock metrics and Resources in each option. All three lift the stocks pages' 820px cap and give back the empty "On this page" column on Resources and the FAQ. **Removed 2026-10-02** once C was chosen. |

Still open: the metric heading subtitles on Stock metrics, and the Market Overview card names and column count (these follow the width decision).

## Done (v0.16.0, 2026-10-02)

Every decision above is built, and the findings below are fixed except where noted. Each change is presentation only: no source wording was cut or rewritten, and scripts/check.py still finds every inventoried item on its page.

| Item | What changed | Where |
|---|---|---|
| Page width (C) | The stocks pages' 820px cap (`.content-inner`) and the VIX pages' 1100px cap (`.container`, 720px `.section-lead`) are lifted, so content runs to the site's 1400px limit. Market Overview's grid fills the width (5 cards across at 1440px instead of 3). Pages whose "On this page" list is empty (Resources, FAQ) give its 240px column back to the content. | site.css, "Full-width content" |
| Footers | One footer per page. Source footers that only repeat the site footer ("Built by Azqato.", "Educational use only. Not financial advice.") stay in the page with class `site-dup`, hidden, so nothing is deleted. The VIX pages' disclaimer ("This is not financial advice... Past performance is not indicative of future results.", and on Custom "Tickers you enter here are not verified against a live quote.") and "© 2026 VIX Strategy. Built with no backend. Powered by VIX." move into the site footer as `site-footer-note`; their call-to-action ("View Live Strategy", "Read the Full Pitch", "View Core Strategy") stays in the page. | site.py `merge_footers`, `footer(page, notes)` |
| Home | "Explore the site" is gone; Home has one grid in the source's project-card style: Stocks, Stock Screener, Market Overview & VIX tools, VIX Strategy, Leveraged Strategies, Curated Resources, FAQ, then the outside projects (Automate Fundamentals, ComposerAtlas, Net Worth Tracker). Three cards are added (Market Overview & VIX tools, Curated Resources, FAQ) for the sections no source card covered; all seven source cards are kept. 10 cards make two full rows of 5 at 1440px. | site.py `split_invests`, `home_cards` |
| Icons | The emoji stay; each sits in the same 44px rounded tile at the same size. On phones the icon sits beside the title, so the cards are no longer tall and mostly empty. | site.css, "Home: one grid" |
| Small text | No source text is under 12px: scripts/site.py raises any `font-size` under 12px or 0.75rem in the source stylesheets and inline page styles (`min_font`). Table headers, labels, badges, chip counts and the sidebar card are set to 12px or more in site.css. The probe found 0 text under 12px on all 21 pages at 1600px and 390px. | site.py `min_font`; site.css, "Text size floor" |
| Sidebar | Each group is a `<details>`: it opens when it holds the current page and the rest open on click, with a chevron. On Home every group starts closed. | site.py `sidebar`; site.css, "Sidebar" |
| Azqato nav on phones | At 900px and below the azqato.com bar is hidden, and its links appear as an "Azqato.com" group in the menu drawer. | site.py `sidebar`; site.css |
| Tap targets | On phones, breadcrumb, "On this page", footer and sidebar links are at least 24px tall (sidebar 32px), and the FAQ toggles are 48px with a larger +. Links inside paragraphs stay as they are (the 24px rule exempts inline links); the probe's remaining small targets are all of that kind. | site.css, "Tap targets" |
| Table fonts | Figures in the stocks tables use the site font with tabular digits (`font-variant-numeric: tabular-nums`) instead of SF Mono/Consolas. The guides' `.ui-text` (on-screen labels) keeps its mono font. | site.css, "Tables" |
| Metric subtitles | The subtitle under each Stock metrics heading lines up with the heading (the source's 11px indent and -4px margin removed). | site.css |
| FAQ chip | The stocks pages' tag ("Strategy Q&A", "The 12 Signals" and the others) is a plain uppercase label with no border or background. | site.css, `.hero-badge` |
| Screener | The disclaimer under the table is a normal left-aligned paragraph at 14px. The pinned ticker column casts a shadow. On phones the tier chips wrap, the filter box is full width, the ticker column is narrower, and a "Swipe sideways for more columns →" line sits above the table. | site.css, "Screener" |
| Market Overview | Card names wrap instead of being cut off. | site.css |
| Resources | Masonry columns (CSS `columns: 260px`), so cards of different lengths stack without tall empty boxes. Cards read down each column, then across. | site.css, "Resources" |
| Card headings | The article's 32px heading margin no longer pushes Home and Resources card titles away from their icons. | site.css |
| VIX: tables on phones | The VIX tables become stacked cards at 640px and below; site.js gives each cell its column heading as `data-label`, including rows the tools add after loading (a MutationObserver). | site.js; site.css, "VIX pages" |
| VIX: status wording | The Custom builder's tier line reads like the Dashboard's ("VIX 15.45 → VIX 15–25 - Moderate Fear" instead of "Tier: 2"). | site.py `vix_inline` |
| VIX: LIVE vs CACHED | **Cause:** vix.js saves each reading for 30 minutes (`REFRESH_TTL`). The first VIX page fetched the feed and showed LIVE; the next page within 30 minutes read the same saved reading and showed CACHED, though it was the same live number. **Fix:** a saved reading under 30 minutes old now shows LIVE; one older than that, used because the feed failed, still shows STALE. Checked: Dashboard then Custom both show LIVE. | site.py `vix_inline` |
| VIX: Custom result first | The Custom builder shows the reading and the tier line first. **Changed v0.16.1 at the author's request:** "Your Categories" (the ticker inputs) then sits above "Your Custom Allocation" (the chart) and the breakdown, so the inputs come before the results they drive. | site.py `build_page` |
| VIX: Strategy Summary | The tool sections' padding drops from 48px to 32px, so the single accordion item doesn't sit in a large empty box. | site.css |
| VIX: QQQ looked underlined | Courier New's Q has a tail that reads as an underline. The VIX pages' mono font is now SF Mono, Consolas or Liberation Mono, with Courier New last. | site.css |
| VIX Strategy page style | Section headings use the site's heading font and size with no green underline; the alternating section backgrounds become a thin line between sections; cards, stat boxes and the table use the site's border, radius and background. The hero is unchanged. | site.css |
| Leverage callouts | Callout text is 15px (was 14.4px). | site.css |

Not changed: the leveraged pages' tables keep their layout; with the wider column they no longer wrap badly at 1440px. The items hidden on phones on the strategy pages stay as they are (no change needed).

## Site-wide

1. **Two or three footers on one page.**
   - The pages that came from the stocks repo end with:
     - the source's centered "Built by Azqato.";
     - a tiny, left-aligned "Educational use only. Not financial advice." block;
     - the site footer, which says the same thing.
   - The VIX pages also carry their own footer: the disclaimer, a copyright line, "Built with no backend. Powered by VIX." and "Built by Azqato".
   - *Suggested fix:* hide the source footers and keep the site footer. The wording is only hidden, not removed, so no content is lost. The VIX disclaimer could move into the page as a notice if its extra wording ("Past performance is not indicative of future results") should stay visible.
2. **Some text is very small.**
   - Table headers in the stocks pages are 9.6 to 10.4px (metrics, example-label, metric-label).
   - Badges are 11.5px, and callout text is small.
   - The screener's group headers are about 9.9px.
   - The VIX gauge labels are 9.9 to 10.4px, and the VIX disclaimers are also tiny.
   - The sidebar footer text is 11.5px.
   - *Suggested fix:* nothing under 12px, and table headers at about 11.5px.
3. **Pages use the width unevenly.**
   - Market Overview, the FAQ, Resources and the VIX Strategy page stop at about 780px, leaving empty space to the right.
   - The paragraphs on VIX Custom (about 1052px) and the leveraged strategy pages (about 1004px) run long enough to be hard to read.
   - On pages with "On this page", the prose sits at about 570 to 780px with a gap before that list. Wide tables, such as the action levels on Index & ETF methodology, are cramped there.
   - *Suggested fix:* let cards and grids fill the width, and cap paragraphs at about 75 characters.
4. **The sidebar is long.**
   - Resources and FAQ only appear after you scroll the sidebar.
   - *Suggested fix:* collapse the groups that don't hold the current page, or give the sidebar its own scroll.
5. **Small tap targets on the phone.**
   - Breadcrumb links, inline links, "On this page" links and the top bar's "Azqato" link are 13 to 19px tall.
   - *Suggested fix:* at least 24px.
6. **The Azqato nav bar is cut off on the phone.**
   - It ends mid-word ("Co...") with no sign that it scrolls sideways.
   - *Suggested fix:* a fade at its right edge, or fold it into the menu.
7. **Fonts are mixed in the stocks tables.**
   - Mono and sans fonts sit side by side in the same tables.
   - *Suggested fix:* pick one for the figures.
8. **Subtitles under the metric headings are indented oddly** on Stock metrics.

## Home

1. **"Explore the site" and "Projects" overlap.**
   - The Learn, Tools and Strategies tiles show up again as the Stocks, Leveraged Strategies, VIX Strategy and Stock Screener cards.
   - *Suggested fix:* merge them, or make Projects only the outside projects.
2. **The last card sits alone.**
   - The Projects grid leaves Stock Screener by itself in its row.
3. **The icons and the phone cards.**
   - The project icons are a mix of emoji and look inconsistent.
   - On the phone the cards are tall and mostly empty, with the icon floating on top.

## Screener

1. **Only two columns show on the phone.**
   - At 390px the table shows Ticker and Tier only. The other ~15 columns are off to the side, with nothing showing that the table scrolls.
   - *Suggested fix:* a scroll shadow or hint, a pinned ticker column, or a compact phone view.
2. **The tier chips** (All, S+, S, A...) are cut off on the right on the phone.
3. **The "Filter by symbol" box** is clipped on the phone.
4. **The disclaimer under the table** is centered small print.
   - *Suggested fix:* a normal left-aligned paragraph.

## Market Overview

1. **Only three columns at any width.**
   - The grid stays at 3 columns, about 780px wide, even at 1440px.
   - *Suggested fix:* 4 to 6 columns on wide screens.
2. **The card names (`.market-card-name`)** are clipped at 390px.
3. **Hard to scan.**
   - The colored bar on top of each card (green or red, for up or down) is the clearest signal. The name and ticker labels above it are tiny.

## VIX Dashboard and VIX Custom builder

1. **The phone layout is the weakest on the site.**
   - The Allocation Breakdown table squeezes its description column into one-word lines and cuts text off on the right.
   - The Tier Reference table is clipped on the right.
   - *Suggested fix:* stack both tables as cards on the phone.
2. **The two pages word the same reading differently.**
   - The Dashboard's status line reads "VIX 16.39 → VIX 15-25 - Moderate Fear". Custom's reads "VIX 16.39 → Tier: 2".
   - *Suggested fix:* use the same wording on both.
3. **LIVE and CACHED disagree.**
   - Loaded at the same moment with the same reading, the Dashboard showed LIVE (green) and Custom showed CACHED (amber).
4. **An oversized box for one item.**
   - "Strategy Summary" holds a single accordion item in a large empty box, with too much space around it.
5. **The result is far down the page on Custom.**
   - The reading and the donut sit below the inputs, so the result you came for is a long way down.
6. **Ticker labels look like links.**
   - In light mode the QQQ and TQQQ labels are underlined.

## Strategies

1. **Cramped tables.**
   - Tables in the narrow column next to "On this page" are cramped, and some cells wrap badly.
2. **Small callout text.**
   - Callouts such as "Composer symphony ID" and the formula box on HFEA are fine, but their text is small.
3. **Two styles on one site.**
   - The VIX Strategy page uses the VIX source's headings and boxes, so it doesn't match the leveraged pages.
4. **Hidden text on phones is harmless.**
   - The items that are visually hidden on phones on the strategy pages do no harm. No change needed.

## Resources

1. **Narrow grid.**
   - The 3-column cards stop at about 800px.
2. **Uneven card heights.**
   - Category sizes vary a lot (Real Estate has 9 links and Charts has 2), so cards in the same row leave tall empty boxes.
   - *Suggested fix:* a masonry or column layout.
3. **Mixed icons.**
   - The category icons are small emoji next to uppercase titles, the same mix as on Home.

## FAQ

1. **It stops at about 780px.**
   - The question list is clean, but it stops at that width.
2. **A chip that looks clickable.**
   - The "Strategy Q&A" chip looks like a button but does nothing.
3. **Small toggles on the phone.**
   - The + toggles work but are small.

## Top 5, if only a few get done

1. One footer on every page.
2. Phone views for the VIX tables (stacked cards) and the screener (at least show that it scrolls sideways).
3. Nothing under 12px.
4. Let the grids (Market Overview, Resources, FAQ) fill the width, and cap paragraph length.
5. Merge "Explore the site" and "Projects" on Home.
