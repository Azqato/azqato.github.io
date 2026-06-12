# PATCHNOTES.md — Azqato Stock Methodology Site

---

## v2.4.0 — June 2026 — Open Graph Social Cards

**Open Graph and Twitter Card meta tags added to `index.html` so Discord, X, Slack, and similar platforms render a preview card when the link is shared. `og-image.png` (1200x630) added to the site root. PRD updated with Section 5 documenting the full requirement for all seven pages.**

### index.html

- `<meta name="description">` added
- Open Graph tags added: `og:type`, `og:url`, `og:title`, `og:description`, `og:image`
- Twitter Card tags added: `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`

### og-image.png (new)

- 1200x630 PNG at the site root
- Site favicon (📈, U+1F4C8) centered on `#0d1117` background, rendered as a white monochrome icon
- Referenced by all OG/Twitter image tags across the site

### docs/PRD.md

- Section 5 "Social Cards (Open Graph)" added: required tag template, per-page values table for all seven pages, image spec, and PowerShell regeneration snippet

---

## v2.3.0 — June 2026 — FAQ Expansion and Badge Text Corrections

**faq.html expanded from 11 to 30 accordion items. Hero badge text corrected sitewide to be distinct from each page's H1 title.**

### faq.html — Expanded Q&A (11 original, 19 new)

19 new accordion items added covering topics derived from all site pages:

| # | New Question |
|---|---|
| 3 | What is the "stocks as ownership" mental model? |
| 4 | What does "staying on offense" mean and why does it matter? |
| 5 | Can I trust Wall Street recommendations? |
| 6 | What is market leadership cycle and why does it matter? |
| 8 | How do you research a company before looking at any numbers? |
| 9 | What is the double/lose-50% test? |
| 11 | How do you build investment knowledge over time? |
| 13 | What is market cap vs. potential and why does it matter? |
| 14 | What does gross margin reveal about a business? |
| 15 | How do you think about a company's balance sheet health? |
| 16 | What is the revenue deceleration warning signal? |
| 17 | Why is PEG a better valuation signal than P/E alone? |
| 18 | What are Growth, Value, and Dividend stocks and how do they differ? |
| 20 | What is RSI and how do you use it as an entry signal? |
| 21 | What is the VIX and how should I use it when investing in indices? |
| 22 | How is investing in ETFs different from picking individual stocks? |
| 23 | What is an expense ratio and why does it matter for ETF investing? |
| 24 | What are leveraged ETFs and when are they appropriate? |
| 30 | Why do conference calls matter more than earnings press releases? |

### Hero badge text corrections

Five pages had badges that were identical or near-identical to their H1 title. Updated to purpose/type labels distinct from the page name:

| Page | Old Badge | New Badge |
|------|-----------|-----------|
| `philosophy.html` | 📖 Investment Philosophy | 📖 Mindset &amp; Principles |
| `metrics.html` | 📊 Metrics Glossary | 📊 The 12 Signals |
| `screener.html` | 🔍 Screener Setup Guide | 🔍 Candidate Discovery |
| `watchlist.html` | 📋 Watchlist Setup Guide | 📋 12-Column Tracking Setup |
| `faq.html` | ❓ FAQ &amp; Philosophy | ❓ Strategy Q&amp;A |

---

## v2.2.0 — June 2026 — Sitewide Hero Badge System

**Hero badge added to all seven pages and repositioned consistently below the page description. Badge position is now: headline, then description, then badge.**

### index.html

- `<div class="hero-badge">` moved from the top of the `.hero` section to after `.hero-sub`
- `margin-top: 16px` added inline to create consistent spacing between the description and the badge
- `.hero` `padding-bottom` reduced from `36px` to `16px` in `style.css` to visually center the badge between the description and the section divider

### Badges added (new)

| Page | Badge |
|------|-------|
| `philosophy.html` | 📖 Investment Philosophy |
| `metrics.html` | 📊 Metrics Glossary |
| `screener.html` | 🔍 Screener Setup Guide |
| `watchlist.html` | 📋 Watchlist Setup Guide |
| `faq.html` | ❓ FAQ & Philosophy |

All new badges use `margin-top: 16px` inline and appear after the page description inside the intro container (`.metrics-intro`, `.guide-intro`, or `.faq-intro`).

### indices.html

- Existing badge moved from above the `<h1>` to after the description paragraph, consistent with the sitewide pattern. `margin-bottom: 16px` replaced with `margin-top: 16px`.

---

## v2.1.0 — June 2026 — Sitewide "On This Page" Navigation

**"On This Page" sidebar anchor navigation extended from metrics.html to all content pages. Block repositioned to appear below the Support link on every page with named sections. IntersectionObserver generalized to work across all pages without per-page configuration.**

### Navigation changes

The "On This Page" anchor block was previously nested inside the Metrics nav item on `metrics.html` only. It is now:

- A standalone `<li>` element positioned below the Support link (bottom of the main nav list) on every page with named sections
- Present on six pages: index, philosophy, metrics, screener, watchlist, indices
- Hidden on mobile alongside other sidebar sub-navigation (existing behavior unchanged)
- Absent on `faq.html` where the accordion pattern is not suited to anchor-link navigation

### Pages updated

| Page | Sections added to "On This Page" |
|------|----------------------------------|
| `philosophy.html` | Stocks as Ownership, How to Research a Company, Growth/Value/Dividend, Stay on Offense, Wall Street vs the Individual, Market Leadership Cycles, Building Investment Knowledge |
| `index.html` | The Strategy, The 10 Metrics, What Strong Metrics Look Like, Portfolio vs. Watchlist |
| `screener.html` | What Finviz Is For, Step 1, Step 2, Step 3, Finviz Free Tier Coverage, Quick-Reference Summary |
| `watchlist.html` | Step 1: Create Account, Step 2: Create Portfolio, Step 3: Add Tickers, Step 4: Configure Columns, Step 5: Sort Order, Your Watchlist Is Ready |
| `indices.html` | Types of Index Funds, Fundamentals vs. Technicals, The VIX, Timing Signals, Structural Quality Metrics, What Strong Signals Look Like, Seeking Alpha Setup |
| `metrics.html` | Block moved from nested under Metrics link to after Support (position change only; links and IDs unchanged) |

### Section IDs added

All section IDs follow the `section-*` prefix convention (e.g., `section-ownership`, `section-strategy`). Existing `metrics.html` IDs (`metric-rev-ttm`, etc.) are unchanged.

### script.js

`IntersectionObserver` generalized. Previously hardcoded to observe `.metric-block` elements (metrics.html only). Now derives section targets from the `href` attributes of `.metric-links a` elements present on the page. Works across all pages with no per-page configuration. No behavioral change on `metrics.html`.

### docs/PRD.md

Section 5 updated with an "On This Page" sidebar navigation reference table listing all section IDs by page, plus implementation notes for the observer.

### docs/DESIGN.md

- Section 4 (Sidebar) updated: nav item list corrected to all 8 nav items; "On This Page" pattern documented
- Section 6 (Signature Element) updated: block now described as sitewide rather than metrics-only
- Section 7 (Navigation) sub-link description updated
- Version history: v1.8.0 entry added

---

## v2.0.0 — June 2026 — Sitewide Punctuation Audit

**Complete em dash and double hyphen removal across all seven active HTML pages and all three documentation files. No content changes; punctuation only. PRD.md updated with formal punctuation policy and audit checklist.**

### Policy

Per the punctuation policy documented in `docs/PRD.md` (Section 4), no em dashes or double hyphens (`--`) are permitted in copy. All instances replaced with contextually appropriate alternatives: comma (flowing continuation), colon (introducing an explanation or list), semicolon (two independent clauses), parentheses (aside or supplementary info), or period (sentence split).

When auditing for em dashes, all three forms must be checked: ` -- ` (double hyphen), `—` (raw Unicode U+2014), and `&mdash;` (HTML entity).

### Pages audited and cleaned

| File | Instances fixed |
|------|----------------|
| `philosophy.html` | ~20 instances |
| `metrics.html` | ~65 instances |
| `screener.html` | 2 instances |
| `watchlist.html` | 2 instances |
| `indices.html` | ~19 instances |
| `faq.html` | ~25 instances |
| `index.html` | 0 (already clean) |

### Docs audited and cleaned

| File | Instances fixed |
|------|----------------|
| `docs/PATCHNOTES.md` | ~17 instances |
| `docs/DESIGN.md` | 6 instances |
| `docs/PRD.md` | 0 prose instances (policy section updated) |

### docs/PRD.md

- **Section 4 (Content Philosophy):** Punctuation policy statement updated to explicitly name all three em dash forms to audit: ` -- `, `—`, and `&mdash;`
- **Punctuation style guide:** New "Audit checklist" block added at the top of the section, listing all three search targets with notes that `&mdash;` is especially easy to miss in HTML source

### Other fixes

- `screener.html`: Stale link `href="guide.html"` corrected to `href="watchlist.html"` (guide.html is an orphaned legacy page not in active nav)

### Legacy files removed

Three orphaned HTML files that were superseded by current pages and are not linked from the active nav were deleted:

| File removed | Replaced by |
|---|---|
| `finviz.html` | `screener.html` |
| `guide.html` | `watchlist.html` |
| `indexes.html` | `indices.html` |

### Notes

- `&ndash;` (`–`) in numeric ranges (e.g., VIX table `15 &ndash; 25`) was left untouched; en dashes for numeric ranges are correct
- CSS custom property names (`--color-text-primary`, `--color-text-secondary`, etc.) were left untouched; `--` is valid CSS variable syntax, not punctuation
- Backtick-wrapped code literals showing `--` as a UI display value (e.g., "PEG shows `--` when not applicable") were left untouched

---

## v1.9.0 — June 2026 — Major Content Expansion

**New Philosophy page. Two new business quality metrics (Gross Margin and Net Margin). Revenue deceleration signal added. Balance sheet rate-hiking advantage documented. FAQ expanded with four new questions. Strategy section deepened with diversification rule and market cap vs potential concept. All 30 concepts from video transcript analysis integrated into site content.**

### New Pages

| File | Description |
|------|-------------|
| `philosophy.html` | New full-length page covering the conceptual foundation of the methodology: stocks as ownership (Buffett farmland analogy), how to research a company (sequential evaluation and SWOT framework), the GVD framework (growth/value/dividend stocks and risk-on/risk-off environments), staying on offense as a psychological discipline, Wall Street incentive misalignment, market leadership cycles and complacency risk, and building investment knowledge through business model study and conference call discipline |

### Navigation Changes (all pages)

- `philosophy.html` added to sidebar nav between Home and Metrics on all seven pages
- Final nav order: **Home → Philosophy → Metrics → Screener → Watchlist → Indices → FAQ → Support**

### index.html

- **Strategy Overview expanded:** Added paragraph on the 10-to-20 stock diversification rule (fewer than 10 concentrates risk, more than 20 dilutes conviction)
- **Strategy Overview expanded:** Added paragraph on the market cap vs potential mental model, comparing current market cap to the addressable opportunity as an input to upside estimation
- **"The 10 Metrics" section:** Added note pointing to Gross Margin and Net Margin entries in the Metrics glossary as supplementary business quality signals
- **"What Strong Metrics Look Like" table:** Two new rows added: Gross Margin (strong: >50%, caution: <30%) and Net Margin (strong: >25%, caution: <10%)
- **FAQ teaser:** Updated to include a link to the new Philosophy page alongside the existing Palantir story link

### metrics.html

- **Sidebar nav:** Anchor links for Gross Margin and Net Margin added to the "On This Page" sub-nav
- **Revenue Growth TTM ("Why it matters"):** New paragraph added explaining the quarterly deceleration warning signal: a consistent pattern of declining quarterly growth rates (+20%, +15%, +10%, +5%) is one of the clearest warning signals available even when absolute growth is still positive
- **Total Cash ("Why it matters"):** New paragraph added explaining the rate-hiking earnings advantage: cash-heavy companies earn interest income at elevated rates while debt-heavy companies face rising interest expense, creating an earnings-level competitive divergence
- **New metric #11: Gross Margin.** Full metric block with what it measures, why it matters (margin direction as a signal of competitive position strength or weakness), how to read it (50%+ strong, 30-50% moderate, <30% caution, declining trend = red flag), gross margin by business type illustrative table, and caveat on cross-industry comparability
- **New metric #12: Net Margin.** Full metric block with what it measures, why it matters (operating leverage as the engine of earnings compounding), how to read it (30%+ elite, 25-30% excellent, 10-25% good, <10% context-required, negative = investigate), trajectory table, and caveat on always researching why margins move

### faq.html

- **"How many stocks should I hold?":** 10-20 rule: below 10 concentrates risk, above 20 dilutes conviction; full construction rationale
- **"When is the wrong time to buy a great company?":** Peak hype avoidance and the weak-hands cascade mechanism: late buyers without business conviction trigger selling cascades when prices pull back; the best entry points are before widespread attention arrives
- **"What should I think about position sizing?":** Core positions (profitable, established companies) vs speculative positions (unprofitable, binary outcomes); keep speculative positions small regardless of prior wins
- **"How does market environment affect which stocks perform best?":** Risk-on/risk-off states, how each affects growth vs value vs dividend stocks, dividends as crash-deployment capital; links to Philosophy page for full GVD framework

### philosophy.html (new)

Seven sections covering the full conceptual foundation of the methodology:

1. **Stocks as Ownership, Not Symbols:** Farmland and franchise mental models; productive asset framing; explicit short-term vs long-term price driver distinction
2. **How to Research a Company:** Sequential evaluation order (business model first, then financials, then valuation); SWOT framework; the double/lose-50% decision test
3. **Growth, Value, and Dividend Stocks:** The three stock types; risk-on and risk-off market environments; dividends as crash-deployment capital; 2022 as the textbook example
4. **Stay on Offense:** Why regular investing is psychologically critical; offensive vs defensive investor mindset; consistency over size
5. **Wall Street vs the Individual Investor:** AUM fee incentive structure; herd mentality as volatility amplifier; the S&P 500 proof point; do your own research
6. **Market Leadership Cycles:** No company stays dominant forever; the complacency mechanism; continuous thesis reassessment; the opportunity in next-generation companies
7. **Building Investment Knowledge:** Business model study for pattern recognition; conference call discipline (twice-listen rule, 2x speed, 50-100 calls per season); always research why margins move

### docs/PRD.md

- Complete rewrite. Previous version described the v1.0.0 three-page site with live META data. Updated to reflect the current 7-page site, all 12 metrics, the philosophy framework, the full FAQ, and a full 30-concept concept tracking table preserving the transcript analysis before the temp file was deleted.

---

## v1.8.0 — June 2026 — Launch Release

**Initial public launch. Yield label generalized on indices page. README updated to reflect full site scope.**

### indices.html

- **"4Y Avg Yield" renamed to "Yield"** throughout the page: metric card description, introductory paragraph, "What Strong Signals Look Like" summary table. The label now reflects yield broadly (trailing 12-month, 30-day SEC, or multi-year average) rather than anchoring to a specific averaging window.
- **"4Y Average Yield" section heading renamed to "Yield."** Section explanation updated: now describes yield as the dividend or distribution yield of an ETF, noting that the specific format (trailing 12-month, 30-day SEC, multi-year average) varies by platform and ETF type. The operative test remains yield vs. expense ratio regardless of how it is expressed.
- **Seeking Alpha ETF watchlist setup table:** "Yield" row retains the label "4Y Avg Yield" in the watchlist column reference, since that is the actual column name in Seeking Alpha's interface.

### README.md

- Full rewrite. Previous version was a v1.0.0 snapshot (3-page site, META live data, old project structure). Updated to reflect the full 7-page site, all metrics, the index/ETF methodology, design system summary, and current content philosophy.

---

## v1.7.0 — June 2026

**Text color refinement. Primary and secondary text tokens now distinct.**

### style.css

- `--color-text-primary` updated from `#e6edf3` to `#eef3f7`: slightly brighter, cleaner white for body copy and headings
- `--color-text-secondary` updated from `#e6edf3` to `#cbdae6`: soft blue-gray for subtitles, captions, lead text, and metric card definitions; visually distinct from primary without being muted or hard to read

---

## v1.6.0 — June 2026

**Indices & ETF guide added. Navigation restructured. Sitewide readability improvements. Long-term capital gains content. FAQ expanded.**

### New Files

| File | Description |
|------|-------------|
| `indices.html` | Full index and ETF investing guide: VIX action levels, fund types, structural quality metrics, Seeking Alpha ETF watchlist setup |
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
- **Fund Types section:** Six metric cards explaining broad market funds, growth funds, dividend funds, value funds, sector-specific funds, and international funds: their role, risk profile, and how each is used in a diversified ETF strategy
- **Fundamentals vs. Technicals section:** Educational explanation of why technicals dominate index investing while fundamentals dominate individual stock picking. Core insight: indices cannot go to zero; individual stocks can. This asymmetry shifts the analytical framework.
- **VIX: The Fear Gauge:** Full explanation of what VIX measures, why it is contrarian and mean-reverting, and five action level ranges (< 15, 15-25, 25-35, 35-45, > 45) with educational market condition descriptions and recommended deployment postures
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
- **`--color-text-secondary` unified with `--color-text-primary`** in `:root`. Changed from `#8b949e` to `#e6edf3`. All elements using the secondary token (metric card descriptions, accordion body text, lead paragraphs, captions, sidebar labels) now render at full legibility. Both color tokens resolve to the same value. This is a root-level change that applies universally; individual class overrides are not needed.
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

#### metrics.html: P/E FWD section

- **"Why it matters" section substantially expanded.** Added explicit explanation of the core P/E vs. EPS Growth comparison: when P/E FWD is lower than the EPS Growth FWD percentage, the growth rate outpaces the multiple paid: a strong signal that the stock is underpriced relative to its earnings trajectory. When P/E is higher than the EPS growth rate, the multiple exceeds what earnings can currently justify.
- This concept was previously implied through the PEG ratio explanation. It is now stated directly as the primary criterion for reading P/E FWD.
- **"How to read it" box updated.** First bullet now explicitly marks "P/E FWD below the forward EPS growth rate" as the primary signal. Secondary bullet covers sector/5Y comparison.
- **Caveat box updated.** Reinforces the direct P/E vs. growth comparison as the operative test, not just PEG.

#### index.html: "What Strong Metrics Look Like" table

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
- **Added:** "What Strong Metrics Look Like" reference table: 7-row directional guide showing strong signal ranges, caution zones, and what each metric confirms. Uses no company-specific data.
- **Added:** "Portfolio vs. Watchlist" section: 4-paragraph educational explanation of entry criteria and the patience mechanism. Replaces the removed data tables with methodology context.

#### metrics.html

- **Rewrote all 10 metric blocks.** Every META-specific example table replaced with hypothetical illustrative examples using generic labels ("High-growth tech co.", "Slow-growth value co.", "Accelerating / Stable / Decelerating").
- All real-time figures (META P/E 18.18, PEG 0.88, Cash $81.18B, Debt $86.77B, RSI 40, etc.) removed.
- Expanded educational prose for each metric; each block now explains what to look for across a range of companies, not how to read one company's current snapshot.
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

Full visual redesign to match the GitHub Dark-inspired aesthetic used across all Azqato properties (portfolio, VIX Strategy, ComposerAtlas). No content changes; all metric text, table data, and FAQ copy is unchanged. Changes are purely CSS, HTML head tags, and documentation.

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
