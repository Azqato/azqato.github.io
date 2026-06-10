# PATCHNOTES.md — Azqato Stock Methodology Site

---

## v1.8.0 — June 2026 — Launch Release

**Initial public launch. Yield label generalized on indices page. README updated to reflect full site scope.**

### indices.html

- **"4Y Avg Yield" renamed to "Yield"** throughout the page -- metric card description, introductory paragraph, "What Strong Signals Look Like" summary table. The label now reflects yield broadly (trailing 12-month, 30-day SEC, or multi-year average) rather than anchoring to a specific averaging window.
- **"4Y Average Yield" section heading renamed to "Yield."** Section explanation updated: now describes yield as the dividend or distribution yield of an ETF, noting that the specific format (trailing 12-month, 30-day SEC, multi-year average) varies by platform and ETF type -- the operative test remains yield vs. expense ratio regardless of how it is expressed.
- **Seeking Alpha ETF watchlist setup table:** "Yield" row retains the label "4Y Avg Yield" in the watchlist column reference, since that is the actual column name in Seeking Alpha's interface.

### README.md

- Full rewrite. Previous version was a v1.0.0 snapshot (3-page site, META live data, old project structure). Updated to reflect the full 7-page site, all metrics, the index/ETF methodology, design system summary, and current content philosophy.

---

## v1.7.0 — June 2026

**Text color refinement. Primary and secondary text tokens now distinct.**

### style.css

- `--color-text-primary` updated from `#e6edf3` to `#eef3f7` -- slightly brighter, cleaner white for body copy and headings
- `--color-text-secondary` updated from `#e6edf3` to `#cbdae6` -- soft blue-gray for subtitles, captions, lead text, and metric card definitions; visually distinct from primary without being muted or hard to read

---

## v1.6.0 — June 2026

**Indices & ETF guide added. Navigation restructured. Sitewide readability improvements. Long-term capital gains content. FAQ expanded.**

### New Files

| File | Description |
|------|-------------|
| `indices.html` | Full index and ETF investing guide -- VIX action levels, fund types, structural quality metrics, Seeking Alpha ETF watchlist setup |
| `watchlist.html` | Renamed from `guide.html`. Seeking Alpha individual stocks watchlist setup guide (content unchanged). |

### Navigation Changes (all pages)

Final nav order: **Home → Metrics → Screener → Watchlist → Indices → FAQ → Support**

- `guide.html` retired; replaced by `watchlist.html` with updated self-link
- Nav label "SA Watchlist" shortened to "Watchlist"
- Nav label "Finviz Screener" shortened to "Screener"
- "Indexes" renamed to "Indices"
- FAQ moved to position 6 (just above Support), making logical groupings: content (Home, Metrics), tools (Screener, Watchlist, Indices), help (FAQ, Support)

### indices.html (new)

- Full methodology page for index and ETF investing
- **Fund Types section:** Six metric cards explaining broad market funds, growth funds, dividend funds, value funds, sector-specific funds, and international funds -- their role, risk profile, and how each is used in a diversified ETF strategy
- **Fundamentals vs. Technicals section:** Educational explanation of why technicals dominate index investing while fundamentals dominate individual stock picking. Core insight: indices cannot go to zero; individual stocks can. This asymmetry shifts the analytical framework.
- **VIX -- The Fear Gauge:** Full explanation of what VIX measures, why it is contrarian and mean-reverting, and five action level ranges (< 15, 15-25, 25-35, 35-45, > 45) with educational market condition descriptions and recommended deployment postures
- **Leveraged ETFs caveat:** Explanation of when to use 2x/3x ETFs (VIX > 45 recovery plays only, not long-term holds)
- **RSI & 52W Range:** Applied to index/ETF context with how-to-read guidance
- **Structural Quality Metrics:** YTD Performance, 5Y Total Return, 10Y Total Return, 4Y Avg Yield (yield > expense ratio test), Expense Ratio with full tier breakdown (< 0.10% to > 0.75%)
- **"What Strong Signals Look Like" table:** 8-metric reference table with Type (Timing/Structural), Strong Signal, Caution Zone, and What It Confirms columns
- **Seeking Alpha ETF Watchlist Setup:** 10-column ETF portfolio setup with exact search terms; VIX tracking note; yield column caveat

### faq.html

- **Q5 (Technical Analysis) substantially rewritten.** Now explains why technicals are used minimally for individual stocks but significantly more for indices/ETFs. Core distinction: individual companies can go bankrupt to $0; broad market indices cannot. This asymmetry makes "what to buy" the primary question for stocks (answered by fundamentals) and "when to buy" the primary question for indices (answered by technicals). VIX cited as the most powerful timing tool for index investing.
- **New Q7 added: "Why does holding for over 12 months matter beyond investment returns?"** Full explanation of long-term vs. short-term capital gains tax treatment. Covers the rate differential (15-20% LTCG vs. 22-37% ordinary income for short-term), compounding advantage of tax deferral, and the hidden cost of selling before the 12-month threshold. Five-paragraph educational response.

### index.html

- **Strategy Overview section updated.** Added paragraph about long-term capital gains: holding positions for more than 12 months qualifies for the lower long-term rate; selling too early converts gains to ordinary income; the strategy's default posture of holding is both a better investment philosophy and the most tax-efficient one available.

### style.css

- **`.accordion-content`** color changed from `--color-text-secondary` to `--color-text-primary`. All FAQ accordion body text is now full-brightness readable.
- **`td`** `white-space` changed from `nowrap` to `normal`. All table cell text now wraps rather than clipping. `white-space: nowrap` preserved on `td.num` (numbers) and `td.ticker-cell` (tickers) where truncation is not a concern.
- **`--color-text-secondary` unified with `--color-text-primary`** in `:root`. Changed from `#8b949e` to `#e6edf3`. All elements using the secondary token -- metric card descriptions, accordion body text, lead paragraphs, captions, sidebar labels -- now render at full legibility. Both color tokens resolve to the same value. This is a root-level change that applies universally; individual class overrides are not needed.
- **`.guide-note`** color set to `--color-text-primary` (explicit, pre-dating the root unification).

---

## v1.5.0 — June 2026

**Two new setup guide pages. Navigation expanded to six items. Text readability improvements. P/E FWD educational content deepened.**

### New Files

| File | Description |
|------|-------------|
| `guide.html` | Step-by-step Seeking Alpha watchlist setup guide |
| `screener.html` | Finviz stock screener setup guide with recommended filter values |

### Changes

#### guide.html (new)

- Full step-by-step guide for creating a free Seeking Alpha account and configuring a portfolio watchlist with the exact 12-column methodology layout
- Emphasizes free tier (no credit card, no subscription required)
- Primary entry point: `seekingalpha.com/account/portfolio`
- Covers: account creation, portfolio creation, ticker addition, column customization (all 12 columns with exact Seeking Alpha search terms and categories), sort order setup
- Column reference table includes the exact search terms to use in Seeking Alpha's column picker for all 12 metrics (Symbol, Market Cap, Price, Change %, Revenue Growth FWD, EPS Growth FWD, P/E Non-GAAP FWD, PEG Non-GAAP FWD, Total Cash, Total Debt, RSI (14), 52 Week Range)
- Non-GAAP vs. GAAP callout box explaining why Non-GAAP is preferred for P/E and PEG
- Cross-links to Finviz screener guide for candidate discovery

#### screener.html (new)

- Full Finviz screener setup guide for finding new stock candidates aligned with the methodology
- Free screener, no account required. Entry point: `finviz.com/screener`
- Explains Finviz's role as a candidate discovery tool vs. Seeking Alpha as the full evaluation tool
- Step-by-step filter setup: Market Cap, Forward P/E, PEG, EPS Growth Next Year, EPS Growth Next 5Y, Sales Growth QoQ, Total Debt/Equity, RSI (14), 52-Week Low
- Recommended filter values with rationale for each
- Results table navigation: Valuation view, PEG sort, Technical view
- Coverage table showing which methodology metrics are directly available vs. proxy-only in Finviz free tier
- Quick-reference filter summary table
- Cross-links to Seeking Alpha watchlist guide

#### All pages (index.html, metrics.html, faq.html, guide.html, screener.html)

- **Navigation expanded.** Two new nav items added to all sidebars, between FAQ and Support:
  - `SA Watchlist` → `guide.html`
  - `Finviz Screener` → `screener.html`
- All five pages have consistent 6-item nav: Home, Metrics, FAQ, SA Watchlist, Finviz Screener, Support

#### style.css

- **Text readability improvement.** `.hero-sub` and `.lead` changed from `--color-text-secondary` to `--color-text-primary`. These classes are used for intro paragraphs and hero subtext sitewide; the previous muted color created unnecessary visual friction for body-level reading content.
- **Guide step body text.** `.guide-step-body p` and `.guide-step-body li` also use `--color-text-primary` for consistency with the above change.
- **New component classes added** for guide pages: `.guide-intro`, `.guide-steps`, `.guide-step`, `.guide-step-header`, `.step-num`, `.guide-step-title`, `.guide-step-body`, `.ui-text`, `.guide-note`, `.filter-strong`, `.filter-caution`

#### metrics.html -- P/E FWD section

- **"Why it matters" section substantially expanded.** Added explicit explanation of the core P/E vs. EPS Growth comparison: when P/E FWD is lower than the EPS Growth FWD percentage, the growth rate outpaces the multiple paid -- a strong signal that the stock is underpriced relative to its earnings trajectory. When P/E is higher than the EPS growth rate, the multiple exceeds what earnings can currently justify.
- This concept was previously implied through the PEG ratio explanation. It is now stated directly as the primary criterion for reading P/E FWD.
- **"How to read it" box updated.** First bullet now explicitly marks "P/E FWD below the forward EPS growth rate" as the primary signal. Secondary bullet covers sector/5Y comparison.
- **Caveat box updated.** Reinforces the direct P/E vs. growth comparison as the operative test, not just PEG.

#### index.html -- "What Strong Metrics Look Like" table

- **P/E FWD row updated.** Strong Signal changed from "Below 5Y avg + sector" to `P/E < EPS Growth %` as the primary criterion. Caution Zone updated to `P/E > EPS Growth %`. "What It Confirms" updated to reflect the growth-adjusted framing.

---

## v1.4.0 — June 2026

**Content generalization pass. Removed real-time data references. Expanded educational content.**

### Summary

All three pages audited for real-time or company-specific data that would become stale or imply a live recommendation. Such references replaced with educational prose and hypothetical illustrative examples. The Palantir story and all other explicit historical first-person accounts are retained.

### Changes

#### index.html

- **Removed:** "Individual Stonks" holdings table (21 rows of live portfolio data with prices, P/E, PEG, RSI, and 52W range values)
- **Removed:** "Potential Buys" watchlist ticker tag section
- **Added:** "What Strong Metrics Look Like" reference table -- 7-row directional guide showing strong signal ranges, caution zones, and what each metric confirms. Uses no company-specific data.
- **Added:** "Portfolio vs. Watchlist" section -- 4-paragraph educational explanation of entry criteria and the patience mechanism. Replaces the removed data tables with methodology context.

#### metrics.html

- **Rewrote all 10 metric blocks.** Every META-specific example table replaced with hypothetical illustrative examples using generic labels ("High-growth tech co.", "Slow-growth value co.", "Accelerating / Stable / Decelerating").
- All real-time figures (META P/E 18.18, PEG 0.88, Cash $81.18B, Debt $86.77B, RSI 40, etc.) removed.
- Expanded educational prose for each metric -- each block now explains what to look for across a range of companies, not how to read one company's current snapshot.
- PEG FWD illustrative table shows why P/E alone misleads using hypothetical growth rates.
- 52W Range section includes a combined RSI + range positioning table showing how the two signals reinforce each other.
- P/E FWD section includes two hypothetical tables: P/E compression over time (showing multiple expansion from growth), and P/E vs sector/5Y-average comparison.

#### faq.html

- **Q4 moat examples generalized.** Specific company names removed from the moat type examples. Replaced with category descriptions that teach the concept without anchoring to a specific stock:
  - "switching costs (Salesforce)" → "switching costs (enterprise software platforms deeply embedded in customer workflows)"
  - "network effects (Meta)" → "network effects (social and communication platforms where value scales with users)"
  - "scale advantages (Amazon)" → "scale advantages (cloud and logistics infrastructure where size creates a cost floor competitors cannot match)"
  - "regulatory moats (Regeneron)" → "regulatory moats (biotechnology and drug pipelines protected by patents and approval timelines)"
  - "brand (American Express)" → "brand (premium financial services and consumer goods where trust itself is the barrier)"
- **Palantir story unchanged.** Retained in full as a first-person historical account ($9 buy-in, $45 sale, $150 outcome). This is a named historical example, not a real-time recommendation.

#### docs/DESIGN.md

- **Section 13 added:** Content Philosophy. Documents the rule that all illustrative examples must use hypothetical labels or category descriptions, not real-time company data. Named exceptions (Palantir story) are explicitly noted.
- **Section 14 (Version History):** v1.4.0 entry added.

---

## v1.3.0 — June 2026

**Footer cleanup.**

- Removed "Educational use only. Nothing on this site constitutes financial advice." from the footer on all three pages. Disclaimer is retained in the sidebar footer where it already lives cleanly.
- Footer now reads only: "Built by Azqato" (linked to azqato.github.io).

---

## v1.2.0 — June 2026

**Navigation and branding updates.**

### Changes

#### All three HTML files (index.html, metrics.html, faq.html)

- **Sidebar brand renamed.** "Azqato." replaced with "Individual Stocks." (teal dot accent retained). Font size reduced from 1.1rem to 0.9rem to accommodate the longer text within the 220px sidebar width.
- **Support link added** to sidebar nav on all pages. Opens `https://azqato.github.io/support.html` in a new tab (`target="_blank" rel="noopener"`). Placed after FAQ in the nav order.
- **Footer updated** to match `azqato.github.io` pattern: "Built by [Azqato](link)" as the primary line, with the educational disclaimer on a second line. "Azqato" links to `https://azqato.github.io/`.

#### style.css

- `.sidebar-brand a`: `font-size` reduced from `1.1rem` to `0.9rem`; `letter-spacing` removed; `white-space: nowrap` added to prevent wrapping.

---

## v1.1.0 — June 2026

**Dark theme rebrand. Aligned to Azqato brand system.**

### Summary

Full visual redesign to match the GitHub Dark-inspired aesthetic used across all Azqato properties (portfolio, VIX Strategy, ComposerAtlas). No content changes -- all metric text, table data, and FAQ copy is unchanged. Changes are purely CSS, HTML head tags, and documentation.

### Changes

#### style.css

- **Color system replaced.** All CSS custom properties updated to the Azqato dark theme palette:
  - Background `#FAFAFA` → `#0d1117`
  - Surface `#FFFFFF` → `#161b22`
  - Border `#E2E6EA` → `#30363d`
  - Accent `#1A6B4A` (deep forest green) → `#00d4a0` (Azqato teal-green)
  - Accent light `#EBF5F0` → `rgba(0,212,160,0.08)` (dark-mode teal tint)
  - Text primary `#1A1F2E` → `#e6edf3`
  - Text secondary `#5A6070` → `#8b949e`
  - Positive `#16A34A` → `#3fb950`
  - Negative `#DC2626` → `#f85149`
  - Warning `#B45309` → `#ffa657`
  - Added: `--color-tag-bg: #21262d`, `--color-card-hover: #1c2128`, `--color-accent-hover: #00e6b0`, `--color-purple: #bc8cff`

- **Typography replaced.** Removed IBM Plex Serif / IBM Plex Sans / IBM Plex Mono (Google Fonts). Now uses system font stack (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`) with system monospace (`'SF Mono', 'Consolas', 'Liberation Mono', monospace`). Eliminates external font dependency, matches Azqato brand.

- **h2 accent bar added.** All `h2` elements now render with a `::before` vertical accent bar (3px wide, teal) via flexbox, matching the section title design from `azqato.github.io`.

- **Metric cards updated.** Added card hover effects: `translateY(-2px)`, box-shadow teal tint, accent border color, and 2px gradient top border (`--color-accent` to `--color-purple`) via `::before`. Matches project card hover behavior from the portfolio site.

- **Badges restyled.** Changed from solid backgrounds to semi-transparent tinted pills with matching border colors (consistent with Azqato pill pattern).

- **Tables.** Header now uses `--color-card-hover`. Table wrapper gets `border-radius: 8px`. Alternating rows use `rgba(255,255,255,0.02)`. Hover uses accent-tinted background.

- **Accordion.** Content background changed from solid `--color-accent-light` to `rgba(0,212,160,0.04)`. Trigger hover uses teal tint. Palantir story text changed to `--color-text-primary` (full brightness) to signal elevated importance.

- **Footer.** Changed from solid dark background to `--color-bg` with `border-top: 1px solid --color-border` (matches portfolio site pattern).

- **Sidebar collapse.** On tablet, collapsed sidebar now uses `backdrop-filter: blur(12px)` frosted glass effect.

#### All three HTML files (index.html, metrics.html, faq.html)

- Removed Google Fonts `<link>` tags (3 link tags per file: preconnect x2, fonts.googleapis.com)
- Added `📈` emoji SVG data URI favicon via `<link rel="icon" href="data:image/svg+xml,...">` 
- Sidebar brand updated: `Azqato.` with teal `<span>` on the period (matching `azqato.github.io` logo pattern)
- Hero badge added to `index.html`: "📈 Methodology Documentation" pill badge in `--color-positive`
- Hero thesis updated: "Do not sell." wrapped in `<span class="highlight">` for teal accent treatment

#### docs/DESIGN.md

- Full rewrite to reflect v1.1.0 design system
- Documents new dark palette, system font stack, component specs for dark theme
- Added version history table
- Removed IBM Plex references, updated all color tokens
- Added new sections: Hero Badge, Watchlist Ticker Tags, Favicon

---

## v1.0.0 — June 2026

**Initial release. Full site built from scratch.**

### Files Created

| File | Description |
|------|-------------|
| `index.html` | Home page |
| `metrics.html` | Metrics glossary (all 10 metrics) |
| `faq.html` | FAQ and philosophy (accordion) |
| `style.css` | Full design system stylesheet |
| `script.js` | Accordion behavior and IntersectionObserver sidebar highlight |
| `docs/README.md` | Project overview |
| `docs/PRD.md` | Product requirements document |
| `docs/DESIGN.md` | Design specification |
| `docs/PATCHNOTES.md` | This file |

---

### index.html

**Sections built:**
- Hero: one-line thesis statement and sub-headline
- Strategy Overview: 3-paragraph explanation of the core methodology
- The 10 Metrics: 2-column card grid, each card links to the full metric entry on `metrics.html`
- Individual Stonks: table of 21 current holdings with Symbol, Price, P/E FWD, PEG FWD, RSI, and 52W Range (visual range bar showing price position within annual range)
- Potential Buys: watchlist of 25 tickers displayed as tag badges (full numeric data not available from source screenshot at this time; can be expanded to full table format)
- FAQ Teaser: link to the Palantir story on `faq.html`
- Footer: disclaimer

**Holdings data source:** Seeking Alpha individual stocks view, June 2026.

**Holdings included (sorted by PEG FWD ascending):**
HUBS, NVDA, TOST, WDAY, CRM, ADBE, TEAM, DELL, INTU, META, LULU, NOW, AMD, REGN, AMZN, AXP, ELF, GOOGL, ZM, PLNH, BRK.B

**Watchlist tickers:**
ACN, APP, AXON, BBY, BX, CELH, COUR, CRCL, GS, HNST, HOOD, IFJPY, IMAX, LZ, MNDY, MSFT, NFLX, NKE, PINS, RVLV, SOFI, TER, TTD, UBER, VEEV

---

### metrics.html

**All 10 metrics documented with:**
- Name and full title
- What it measures (plain English definition)
- Why it matters (investment context)
- How to read it (range badges: good / caution / red flag)
- META example table (real data from Seeking Alpha screenshots)
- Caveat box (edge cases and limitations)

**Metrics covered:**
1. Revenue Growth TTM
2. Revenue Growth FWD
3. EPS Growth TTM
4. EPS Growth FWD
5. P/E FWD
6. PEG FWD
7. Total Cash
8. Total Debt
9. RSI
10. 52-Week Range

**Primary example company:** META Platforms (META), data from Seeking Alpha valuation/metrics page, June 2026.

**META data used:**
- P/E Non-GAAP (FWD): 18.18
- PEG Non-GAAP (FWD): 0.88
- Total Cash: $81.18B
- Total Debt: $86.77B
- RSI: 40
- 52W Range: $520.28 - $798.25
- EPS Growth estimates: Dec 2026: 8.53%, Dec 2027: 12.28%, Dec 2028: 14.20%, Dec 2029: 21.53%
- P/E estimates: 2025 Actual: 19.73, 2026: 18.18, 2027: 16.19, 2028: 14.17, 2029: 11.66

**Sidebar navigation:** Sticky left sidebar with in-page anchor links for all 10 metrics. Active link highlighted in accent green via IntersectionObserver scroll detection.

---

### faq.html

**Accordion items built:**

1. Why do you never sell your stocks?
2. The Palantir Story (visually distinguished with accent left border, italicized trigger)
3. How do you build a watchlist?
4. What makes a company worth holding long-term?
5. Do you use technical analysis?
6. What is the biggest mistake beginner investors make?

**Palantir story:** 5-paragraph essay. Covers the $9 buy-in, the $45 sale, the $150 outcome, and the framework rule derived from the experience. Formatted as an expandable accordion item with a left-border accent treatment to distinguish it visually.

---

### style.css

**CSS architecture (in order as built):**
1. `:root` CSS custom properties (color system, sidebar width)
2. Reset and base styles
3. Layout (site-wrapper flex container, site-layout grid)
4. Sidebar styles (sticky, scroll-independent, brand, nav, footer)
5. Main content area
6. Footer
7. Typography (H1 IBM Plex Serif, H2 IBM Plex Serif, H3 IBM Plex Sans, body IBM Plex Sans, mono for data)
8. Tables (header row, alternating rows, hover, ticker cells, positive/negative value coloring, 52W range bar)
9. Hero section
10. Section container
11. Metric cards (index page 2-column grid)
12. Metric blocks (metrics page full entries)
13. Accordion (FAQ page)
14. Badges (good / caution / negative)
15. FAQ teaser
16. Ticker tags (watchlist display)
17. Metrics intro header
18. Media queries: tablet (max 1023px), mobile (max 767px)
19. Reduced motion preference

**Color tokens used:**
- `--color-bg: #FAFAFA`
- `--color-surface: #FFFFFF`
- `--color-border: #E2E6EA`
- `--color-text-primary: #1A1F2E`
- `--color-text-secondary: #5A6070`
- `--color-accent: #1A6B4A`
- `--color-accent-light: #EBF5F0`
- `--color-positive: #16A34A`
- `--color-negative: #DC2626`
- `--color-warning: #B45309`

**Fonts:** IBM Plex Serif (headings), IBM Plex Sans (body/UI), IBM Plex Mono (data/ticker/numbers). Loaded from Google Fonts.

---

### script.js

**Accordion behavior:**
- Click any accordion trigger to expand its body (max-height transition, 200ms ease-in-out)
- Opening one item closes all others
- `aria-expanded` attribute toggled for accessibility
- Icon toggles between `+` and `-`

**Sidebar IntersectionObserver (metrics.html):**
- Observes all `.metric-block` sections
- When a section enters the viewport (with `-15% / -65%` root margin), the corresponding sidebar link receives `.active` class
- Provides "you are here" awareness as user scrolls through the 10 metrics

---

### Design decisions and notes

- No em dashes used anywhere in copy (per design spec)
- No gradient backgrounds, no dark mode, no chart widgets, no animations beyond accordion and sidebar highlight
- 52W Range column uses a CSS custom property `--pos` to position the dot on a 4px track bar, calculated as `(price - low) / (high - low)` as a percentage
- Potential Buys displayed as ticker tag badges rather than a full table because the source screenshot did not have legible numeric data. Can be converted to a full table format when source data is available
- PEG values below 1.0 highlighted in `--color-positive` green in the holdings table
- PEG values above 3.0 highlighted in `--color-warning` amber (ZM: 3.93)
- `PLNH` and `BRK.B` show `--` for PEG FWD as the metric is not applicable for these securities

---

## Planned Updates

- [ ] Add numeric data to Potential Buys table when Seeking Alpha source data is refreshed
- [ ] Add a "Last Updated" timestamp to both snapshot tables
- [ ] Consider adding Revenue FWD and EPS Growth FWD columns to the holdings table
- [ ] Consider adding a portfolio allocation section (% weight per holding)
- [ ] Mobile hamburger menu for the sidebar nav on small screens
