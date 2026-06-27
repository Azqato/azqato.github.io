# PRD — Azqato Stock Methodology Site

**Version:** 2.0  
**Status:** Current  
**Author:** Azqato  
**Last Updated:** June 2026

---

## 1. Overview

### 1.1 Goal

A static educational website documenting Azqato's individual stock picking methodology. The site serves as both a personal reference and a public educational resource. It covers the quantitative evaluation framework (12 metrics), the qualitative research process, the philosophical foundations of long-term conviction investing, and practical tool setup guides for Finviz and Seeking Alpha.

### 1.2 Target Audience

- Beginner to intermediate retail investors
- People who follow Azqato's content across Twitch, YouTube, or Discord (B5TA community)
- Anyone interested in a fundamentals-first, buy-and-hold approach to long-term equity investing

### 1.3 Non-Goals

- No trading signals or real-time data
- No financial advice or personalized recommendations
- No user accounts or backend of any kind
- No third-party charting widgets or paid APIs

---

## 2. Site Structure

### Pages

| Page | File | Purpose |
|------|------|---------|
| Home | `index.html` | Strategy overview, 10-metric summary grid, reference table, portfolio vs watchlist framework |
| Philosophy | `philosophy.html` | Full conceptual foundation: stocks as ownership, research methodology, GVD framework, market environments, Wall Street context, market leadership cycles, building investment knowledge |
| Metrics Glossary | `metrics.html` | Deep explanations of all 12 metrics with illustrative examples and how-to-read guidance |
| Finviz Screener Setup | `finviz.html` | Finviz stock screener filter configuration guide |
| Seeking Alpha Watchlist | `seekingalpha.html` | Seeking Alpha 12-column watchlist configuration guide |
| Indices & ETF | `indices.html` | VIX, RSI, structural quality metrics, and ETF watchlist setup for index investing |
| FAQ | `faq.html` | Philosophy and practice Q&A in accordion format |

### Shared Assets

| File | Purpose |
|------|---------|
| `style.css` | Full design system stylesheet |
| `script.js` | Accordion behavior and IntersectionObserver sidebar highlight (metrics page) |

### Navigation Order

Home → Philosophy → Metrics → Screener → Watchlist → Indices → FAQ → Support

**Nav link label rule:** Every sidebar navigation link must be a single word. The labels are: Home, Philosophy, Metrics, Screener, Watchlist, Indices, FAQ, Support. OG titles and page H1 headings may be longer; the nav label must never be.

---

## 3. Page-by-Page Requirements

### 3.1 Home Page (`index.html`)

**Sections (in order):**

1. **Hero:** Headline thesis ("Buy companies with strong growth fundamentals. Hold them. Do not sell."), sub-description, then the "📈 Methodology Documentation" badge below the description.

2. **Strategy Overview:** 6-paragraph overview covering: the core approach (buy quality, hold, compounding), watchlist vs portfolio distinction, the cost of early selling, long-term capital gains tax advantage, diversification rule (10-20 stocks), and market cap vs potential mental model.

3. **The 10 Metrics:** 10 metric cards in a 2-column grid, each linking to the full entry on `metrics.html`. Note: Gross Margin and Net Margin are supplementary signals that appear in the glossary but not in the core screener grid. A footer note links to those metric entries.

4. **What Strong Metrics Look Like:** 9-row reference table with Strong Signal, Caution Zone, and What It Confirms for each key metric including Gross Margin and Net Margin rows.

5. **Portfolio vs. Watchlist:** 4-paragraph explanation of entry criteria for portfolio positions vs watchlist names and how to manage the transition between them.

6. **FAQ Teaser:** Links to the Palantir story on `faq.html` and to the Philosophy page.

---

### 3.2 Philosophy Page (`philosophy.html`)

Nine sections covering the conceptual and philosophical foundation of the methodology. This page preserves all concepts from the transcript analysis that do not fit neatly into the quantitative metrics framework.

**0. It Is Possible, and the Game Is Long** (`#section-possible`)
- Belief as a structural prerequisite: no one builds significant wealth without first believing it is achievable; belief sustains consistency through years of unremarkable progress
- Ordinary starting points reach large outcomes; starting size determines how long it takes, not whether it works
- Plan-to-one-hundred framing: assume you live to 100 and reverse-calculate; a 40-year-old is past the first quarter, a 50-year-old at halftime; no long-term fortune was built on short-term thinking
- People underestimate multi-decade compounding: the city-skyline analogy (impossible in one year, routine over twenty)
- The short-termism trap: instant-results culture and dopamine incentives push against the long horizon and trigger destructive impatience

**1. Stocks as Ownership, Not Symbols**
- The Buffett farmland analogy: buy productive assets, think in years not days
- The franchise mental model: same logic as owning an operating business
- Why the ownership frame creates noise immunity
- Explicit framing of short-term vs long-term price drivers: short-term is driven by narrative, sentiment, hype, institutional flows, options mechanics, and macro news; long-term is driven by revenue growth, EPS growth, and margin expansion

**2. How to Research a Company**
- Sequential evaluation: business model first, then financials, then valuation
- Why the order matters: starting with numbers creates rationalization bias toward businesses that may be fundamentally flawed
- SWOT analysis framework: Strengths, Weaknesses, Opportunities, Threats (Opportunities and Threats are the most investment-relevant dimensions)
- SWOT application: every major technological shift disrupts some businesses and accelerates others; SWOT forces positioning relative to the current environment
- The double/lose-50% test: what are the realistic odds of doubling in 3-5 years vs losing 50%? Opportunities drive the first number; threats and balance sheet health drive the second.
- Read the balance sheet like a person's finances: the cousin analogy (heavy debt and little cash = fragile; high cash/investments and low debt = resilient); strong balance sheets create the optionality to go on offense when others are forced to retrench

**3. Growth, Value, and Dividend Stocks**
- Growth stocks: high revenue growth, high P/E multiples, best in risk-on environments, worst in risk-off (50-80% drawdowns possible)
- Value stocks: below intrinsic value, slower growth, stable cash flows, resilient in risk-off (lower multiples compress less)
- Dividend stocks: consistent income payments, fall only 20-30% in conditions that drop growth stocks 50-80%, provide deployment capital during crashes
- Risk-on vs risk-off environments: definition, triggers, which stock types win in each
- Dividends as crash-deployment capital: income continues during price declines, providing buying power at exactly the moments when quality companies are most discounted
- 2022 as the textbook example: Fed rate hikes caused 50-80% drawdowns in growth stocks; value and dividend stocks held; an investor who understood all three types both preserved capital and had cash to buy discounts

**4. Stay on Offense**
- Regular investing is psychologically critical, not just mathematically important
- The offensive investor: adds consistently, never desperate to time entries, does not panic-sell because they are always planning the next buy
- The defensive investor: no capital to deploy, every price movement becomes a fear-driven decision, produces destructive behavior
- Amount matters less than consistency: $200/month for 20 years outperforms $2,000/month with panic behavior
- Concrete cadence: buy at least twice a month regardless of market conditions; a fixed schedule removes the timing question and replaces it with which quality business to add next
- Grow income over cutting expenses: there is a floor on how much you can cut, no ceiling on what you can earn; the offensive mindset depends on having capital to deploy

**5. Wall Street vs the Individual Investor**
- AUM fee structure: income grows with assets managed, not returns generated; this misaligns incentives with client wealth building
- Short-term performance management: quarter-to-quarter appearance matters more than long-term outcomes for client retention
- Herd mentality: institutional managers go risk-off together (amplifying downside) and risk-on together (amplifying upside)
- The S&P 500 embarrassment: most actively managed funds cannot consistently beat a mechanical index fund over time
- Practical implication: do not outsource conviction; volatility is not evidence of error; the people generating volatility are playing a different game

**5.5. Hype, Sentiment, and the Weak-Hands Cascade** (`#section-hype`)
- Saturating attention is not a buy signal: when a stock is the topic everywhere, the easy upside is usually gone and the valuation is typically stretched; broad ownership leaves little marginal buying and a lot of positioning that can unwind
- The weak-hands cascade mechanism: late buyers near a peak hold no conviction, sell as price slips, push the next cohort underwater, and trigger successive waves of selling; a stock can fall for months while the company keeps posting record numbers (business and price decouple in the short term)
- The defense: build positions before broad attention arrives; anchor decisions to long-term fundamentals (revenue growth, EPS growth, margins) rather than sentiment, narrative, or momentum-list status; sentiment sets price this quarter, fundamentals set it over years

**6. Market Leadership Cycles**
- No company stays at the top of the market cap rankings for 30-40 years
- The complacency mechanism: near-monopoly status shifts organizational culture from builders to protectors; engineers lose influence; product quality declines slowly; by the time a disruption arrives, the company lacks the culture to respond
- Implications for holding: continuous reassessment of whether the moat is intact, whether management is building or protecting, whether competitors are taking share
- The opportunity: the next generation of dominant companies likely already exists as small or mid-cap names; studying patterns of past market leaders builds the pattern recognition to identify them early

**7. Building Investment Knowledge**
- Studying historical and current business models: pattern recognition that lets you identify quality before it is widely priced in
- Why sectors beyond technology matter: great long-term compounders exist in consumer brands, specialty retail, financial services, and other non-tech categories
- Margins reveal competitive position: the multi-year direction of gross and net margins signals a position of power (rising: pricing power, cost control, defensible) or weakness (eroding: forced price cuts, rising cost to win sales); Wall Street pays up for margin expansion and sells margin compression as evidence of an emerging threat; durable margin trends are the quantified version of SWOT strengths and threats
- Conference call discipline: free, public, and almost universally ignored by casual investors. The texture of what is happening is in the call, not the press release.
- The twice-listen rule: first listen misses nuance; second listen surfaces it; every time
- 2x playback speed: doubles research capacity without information loss; build the tolerance for it
- 50-100 calls per earnings season: the information advantage compounds over time
- Always research why margins move: never accept a gross or net margin change without finding the explanation in the call; is it durable or a one-time event?

---

### 3.3 Metrics Glossary (`metrics.html`)

Twelve metrics in full educational format. Each metric entry includes: what it measures, why it matters, how to read it (range badges), at least one illustrative example table with hypothetical data, and a caveat box.

**Metrics 1-10: Core Screener Metrics**

These are the primary signals reviewed when evaluating any position and are available as Finviz screener filters (or equivalents).

1. **Revenue Growth TTM:** Trailing 12-month actual revenue growth. Ground truth on business momentum. Includes the quarterly deceleration warning signal: a pattern of +20%, +15%, +10%, +5% across four quarters signals a business approaching plateau even when absolute growth is still positive.

2. **Revenue Growth FWD:** Analyst consensus forward revenue estimate. The relationship between FWD and TTM reveals whether growth is accelerating or decelerating. Strong FWD + strong TTM = high-conviction setup.

3. **EPS Growth TTM:** Trailing 12-month earnings per share growth. Confirms that revenue growth is compounding into profit growth. Revenue growing but EPS declining signals margin compression.

4. **EPS Growth FWD:** Consensus forward EPS estimate. Primary input to the PEG ratio. Accelerating FWD trajectory signals operating leverage that will compound returns even without price movement.

5. **P/E FWD:** Forward price-to-earnings ratio. Primary valuation anchor. Most important signal: P/E below the EPS growth rate means the stock is underpriced relative to its earnings trajectory. Also compare to 5-year average and sector median.

6. **PEG FWD:** Forward price/earnings-to-growth ratio. The single most important number in this methodology. Below 1.0 = potentially undervalued relative to growth. Above 2.0 = growth already priced in.

7. **Total Cash:** Cash, equivalents, and short-term investments. Net cash positive (cash > debt) = maximum optionality. Important nuance: cash-heavy balance sheets also provide an earnings advantage during Fed rate hiking cycles (interest income vs zero interest expense for debt-free companies).

8. **Total Debt:** All short and long-term debt obligations. Risk assessed relative to cash and free cash flow. High fixed-rate long-term debt differs significantly from high-rate short-term floating obligations.

9. **RSI:** Relative Strength Index. Entry timing signal only. Below 30 = significantly oversold, high priority review. Above 70 = overbought, not the moment to initiate.

10. **52-Week Range:** Annual price range. Entry timing signal. Lower 25% of range = favorable entry context when paired with low RSI. Upper 90% = do not initiate.

**Metrics 11-12: Business Quality Metrics**

These are evaluated during research but not available as direct Finviz screener filters.

11. **Gross Margin:** Revenue minus cost of goods sold as a percentage of revenue. 50%+ = strong (typical of software, premium brands). Under 30% = elevated risk. Direction matters: rising = position of strength; falling = competitive pressure or pricing deterioration.

12. **Net Margin:** Net income as a percentage of revenue. 30%+ = elite. 25-30% = excellent. 10-25% = good. Under 10% = requires context. Rising trajectory signals operating leverage. Always research why margins move.

---

### 3.4 Finviz Screener Setup (`finviz.html`)

Finviz stock screener configuration guide for discovering candidates. Free tier, no account required.

**Filters covered:**
- Market Cap (Mid to Large)
- Forward P/E
- PEG
- EPS Growth Next Year
- EPS Growth Next 5 Years
- Sales Growth Quarter over Quarter
- Total Debt/Equity
- RSI (14)
- 52-Week Low

**Purpose:** Discovery tool that generates a candidate list for deeper evaluation in Seeking Alpha. Not a buy signal generator.

---

### 3.5 Seeking Alpha Watchlist (`seekingalpha.html`)

Seeking Alpha 12-column individual stocks watchlist configuration. Free account, no credit card required.

**Columns configured:**
Symbol, Market Cap, Price, Change %, Revenue Growth FWD, EPS Growth FWD, P/E Non-GAAP FWD, PEG Non-GAAP FWD, Total Cash, Total Debt, RSI (14), 52 Week Range

---

### 3.6 Indices & ETF Investing (`indices.html`)

Separate methodology for evaluating broad market indices and ETFs. Key insight: indices cannot go to zero; individual stocks can. This asymmetry makes technicals the primary framework for index investing (when to buy) vs fundamentals for individual stocks (what to buy).

**Sections:**
- Types of index funds: Broad Market, Growth, Dividend, Value, Sector-Specific, International
- Dollar-Cost Averaging: DCA as the right default for most investors regardless of the timing signals; VT and VTI + VXUS as the broad-market vehicles (what-to-buy is already solved, so only the schedule matters); removes emotion, removes timing, matches paycheck investing, builds the habit; terminology note (paycheck investing is closer to repeated small lump sums than formal DCA)
- Lump-Sum Investing: LSI beats DCA on average (~2/3 over a 12-month window, ~90% at 36 months per Vanguard) because markets trend up and money invested sooner compounds longer; timing/regret risk; the "dry powder" trap (waiting for a dip underperforms); the hybrid approach (invest 1/2 to 1/3 now, DCA the rest over 3-6 months); reconciled with the VIX/AAII framework (signals are for deploying cash already earmarked to invest, not for pausing regular contributions)
- Fundamentals vs. Technicals: why the question is different for indices
- VIX: The Fear Gauge: five action level ranges with market condition descriptions and deployment postures
- Leveraged ETFs caveat: when to use 2x/3x ETFs (VIX > 45 recovery plays only)
- RSI and 52W Range for index/ETF context
- AAII Investor Sentiment Survey: weekly retail investor poll (since 1987, ~150K members, published Thursdays). Used as a contrarian indicator: bearish readings above 60% historically mark or precede major market bottoms; below 25% bearish signals elevated optimism and caution for new entries. Highest-conviction entries combine elevated AAII bearish readings with elevated VIX (three-tier framework: either elevated, both elevated, both at extremes).
- Structural Quality Metrics: YTD Performance, 5Y Return, 10Y Return, Yield, Expense Ratio
- "What Strong Signals Look Like" reference table (nine signals: four timing, five structural)
- Seeking Alpha ETF watchlist setup

---

### 3.7 FAQ (`faq.html`)

Accordion-style Q&A covering philosophy and practice. Ten questions:

1. **Why do you never sell your stocks?** Asymmetric cost of selling: holding a loser leaves the asset; selling a winner loses the gain permanently.

2. **The Palantir Story:** First-person account. Bought at $9, sold at $45, watched it go to $150. The rule that came out of it: selling a business because the price went up is a category mistake. Price and value are not the same thing. (Visually distinguished with accent treatment.)

3. **How do you build a watchlist?** Fundamentals must pass the full screen; timing must be right. Patience is a strategy.

4. **What makes a company worth holding long-term?** Four things: durable revenue growth, expanding or stable margins, strong balance sheet (or credible path), and a moat.

5. **Do you use technical analysis?** Minimally for individual stocks (RSI and 52W range for entry timing only). Significantly more for indices (VIX + RSI + range as primary framework, because indices cannot go to zero).

6. **Why does holding for over 12 months matter beyond investment returns?** Long-term capital gains tax treatment (15-20% vs 22-37% ordinary income rate). Tax-deferred compounding. The hidden cost of impatience is paying the higher rate.

7. **What is the biggest mistake beginner investors make?** Selling winners too early and holding losers too long. Compounding requires time in quality assets.

8. **How many stocks should I hold?** 10-20. Fewer concentrates risk; more dilutes conviction. Every position should still be high-conviction within that range.

9. **When is the wrong time to buy a great company?** When everyone is talking about it. Peak coverage = peak valuation. Late buyers without business conviction create weak-hands cascades when prices pull back.

10. **What should I think about position sizing?** Core positions (profitable, established) get meaningful allocations. Speculative positions (unprofitable, binary outcomes) get small allocations regardless of prior wins.

11. **How does market environment affect which stocks perform best?** Risk-on favors growth; risk-off hits growth stocks hardest (50-80% drawdowns possible). Value and dividend stocks hold up better in risk-off. Understanding this cycle does not mean avoiding growth. It means holding through volatility with understanding and having structure to deploy capital at discounts. Links to Philosophy page for the full GVD framework.

12. **Is getting wealthy in the stock market realistic, and how long does it take?** (`answer-longgame`) Belief as a prerequisite; the plan-to-one-hundred horizon (40 is the first quarter, 50 is halftime); underestimating multi-decade compounding (city-skyline analogy); the short-termism trap. Mirrors the philosophy.html "It Is Possible, and the Game Is Long" section; links to `philosophy.html#section-possible`.

13. **Should I invest all at once or spread it out over time?** (`answer-dca`) DCA as the default for regular income-stream investing (VT or VTI + VXUS); LSI mathematically superior on average for a one-time pool; the hybrid (1/2 to 1/3 now, DCA the rest over 3-6 months); the dry-powder trap; reconciliation with the VIX/AAII signals. Links to `indices.html#section-dca` and `indices.html#section-lumpsum`.

> Note: the FAQ has grown well beyond this list (currently ~30 accordion items; see PATCHNOTES v2.3.0 and later). This numbered summary is not exhaustive. The v3.2.0 pass also aligned several existing answers with the philosophy v3.1.0 additions: the offense answer gained the buy-at-least-twice-a-month cadence and income-over-expenses focus; the balance-sheet answer gained the personal-finance (cousin) analogy; the gross-margin answer gained the position-of-power vs weakness framing and why Wall Street prices margin trends; and the "wrong time to buy a great company" answer now links to `philosophy.html#section-hype`.

12. **What is the AAII Investor Sentiment Survey and how do I use it when investing in indices?** Weekly retail investor poll (since 1987, ~150K members). Used as a contrarian indicator: bearish above 60% historically marks or precedes major bottoms. Action levels parallel the VIX framework. Highest-conviction entries combine elevated AAII bearish readings with elevated VIX. Links to the full `#section-aaii` framework on indices.html.

---

## 4. Content Philosophy

- No real-time data. No live portfolio snapshots. All illustrative examples use hypothetical labels or category descriptions.
- The Palantir story ($9 buy, $45 sell, $150 outcome) is the one named historical exception, presented as a first-person account rather than a recommendation.
- All examples use generic descriptors ("High-growth tech co.", "Quality compounder", "Accelerating", "Decelerating").
- No em dashes or double hyphens in copy. Punctuation alternatives (commas, colons, semicolons, parentheses, and periods) are used instead to improve readability and flow. This applies to all HTML pages and documentation files. When auditing, search for all three forms: ` -- ` (double hyphen with spaces), `—` (raw Unicode em dash, U+2014), and `&mdash;` (HTML entity). The `&mdash;` entity is easy to overlook in HTML source and must be explicitly included in any audit search.
- No financial advice language. Disclaimer in sidebar footer on every page: "Educational use only. Not financial advice."
- The methodology explicitly covers all three stock types (growth, value, dividend) even though the primary focus is on growth stock selection. This breadth prevents the site from appearing to be a single-strategy prescription.

### Punctuation style guide

**Audit checklist:** When checking any file for prohibited em dashes, search for all three forms:
1. ` -- ` (double hyphen with surrounding spaces)
2. `—` (raw Unicode em dash, U+2014)
3. `&mdash;` (HTML entity; especially easy to miss in HTML source)

When a dash would normally appear in copy, use the following alternatives based on context:

- **Comma:** The default replacement in most cases. Keeps the sentence flowing without drawing attention to itself.
- **Colon:** Used when introducing a list, explanation, or elaboration after a complete clause.
- **Semicolon:** Used when connecting two closely related independent clauses that could each stand alone.
- **Parentheses:** Used for asides or supplementary information that is not central to the main point.
- **Period:** Used when splitting a sentence into two produces a cleaner result. Shorter sentences are often clearer.

---

## 5. Social Cards (Open Graph)

Every page must include Open Graph and Twitter Card meta tags in the `<head>` so that links shared on Discord, X, Slack, and similar platforms render a preview card.

### Title and description convention

- **`<title>` and `og:title`:** Both equal the page H1 text exactly. No brand suffix. "- Azqato" is never used anywhere. `<title>` and `og:title` are always identical.
- **`og:description` and `<meta name="description">`:** Both equal the lead paragraph on the page exactly. They are always identical.
- `twitter:title` and `twitter:description` always mirror `og:title` and `og:description`.

### Required tags (all pages)

```html
<meta name="description" content="...">
<!-- Open Graph / Discord -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://azqato.github.io/stocks/PAGE.html">
<meta property="og:title" content="Page Title">
<meta property="og:description" content="...">
<meta property="og:image" content="https://azqato.github.io/stocks/og-image.png">
<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="...">
<meta name="twitter:image" content="https://azqato.github.io/stocks/og-image.png">
```

### Per-page values

`og:title` and `<title>` are identical. `og:description` and `<meta name="description">` are identical.

| Page | `og:url` | `og:title` / `<title>` | `og:description` / `<meta name="description">` |
|------|----------|------------|-----------------|
| `index.html` | `.../stocks/` | Stock Picking Methodology | A disciplined, metrics-driven approach to long-term equity investing. No day trading. No panic selling. No noise. |
| `philosophy.html` | `.../stocks/philosophy.html` | The Philosophy of Long-Term Conviction Investing | The concepts that sit behind every rule in this methodology. Understanding why the rules exist makes them easier to follow when markets are moving fast and the temptation to react is strongest. |
| `metrics.html` | `.../stocks/metrics.html` | Stock Evaluation Metrics Explained | Ten metrics. Each one earns its place. This page explains what each signal measures, why it matters for long-term investing decisions, and how to interpret the numbers. All examples are illustrative and use hypothetical figures to demonstrate how each metric works in practice. |
| `finviz.html` | `.../stocks/finviz.html` | How to Set Up a Finviz Stock Screener For Free | How to configure Finviz's free stock screener to surface candidates that align with the methodology. Use this as a discovery tool to find stocks worth evaluating further in Seeking Alpha. |
| `seekingalpha.html` | `.../stocks/seekingalpha.html` | How to Build a Stock Watchlist in Seeking Alpha For Free | Step-by-step guide to creating a free Seeking Alpha account and configuring a portfolio to track individual stocks with the exact 12-column layout used in this methodology. |
| `indices.html` | `.../stocks/indices.html` | Indices & ETF Investing | A separate methodology for evaluating broad market indices and ETFs. Different assets require different frameworks. Where individual stock picking is driven primarily by company fundamentals, index investing is driven primarily by market sentiment, timing signals, and structural efficiency. |
| `faq.html` | `.../stocks/faq.html` | Stock Investing Q&A | The thinking behind the strategy. Questions about how decisions are made, why certain rules exist, and what the long-term mindset actually looks like in practice. |

### Image

`og-image.png` is a static 1200x630 PNG stored at the site root. It shows the site favicon (📈, U+1F4C8) centered on the `#0d1117` background, rendered as a white monochrome icon via Segoe UI Emoji. Discord uses `summary_large_image` format (minimum 600x315, recommended 1200x630). The image must exist at the declared URL; a missing image silently produces a card with no preview.

To regenerate the image, run this PowerShell snippet from the site root:

```powershell
Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap(1200, 630)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.Clear([System.Drawing.Color]::FromArgb(255, 13, 17, 23))
$font = New-Object System.Drawing.Font("Segoe UI Emoji", 380, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
$sf = New-Object System.Drawing.StringFormat
$sf.Alignment = [System.Drawing.StringAlignment]::Center
$sf.LineAlignment = [System.Drawing.StringAlignment]::Center
$g.DrawString([System.Char]::ConvertFromUtf32(0x1F4C8), $font, (New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)), (New-Object System.Drawing.RectangleF(0,0,1200,630)), $sf)
$bmp.Save("og-image.png", [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose(); $bmp.Dispose()
```

---

## 6. Design System

- GitHub Dark-inspired palette: background `#0d1117`, surface `#161b22`, teal accent `#00d4a0`
- Text primary `#eef3f7`, text secondary `#cbdae6`
- System font stack, no external font loading
- CSS Grid sidebar layout with sticky positioning on desktop
- Responsive: sidebar collapses to sticky top nav below 1024px
- Full design specification in `docs/DESIGN.md`

### "On This Page" sidebar navigation

Every page with multiple named sections includes an "On This Page" anchor-link block in the sidebar navigation. This block appears below the Support link (last item in the main nav) and is consistent across all pages. On mobile (below 1024px) the block is hidden alongside the rest of the sidebar sub-navigation.

**Pages and their section IDs:**

| Page | Section IDs |
|------|-------------|
| `index.html` | `#section-strategy`, `#section-metrics-grid`, `#section-reference`, `#section-portfolio` |
| `philosophy.html` | `#section-possible`, `#section-ownership`, `#section-research`, `#section-gvd`, `#section-offense`, `#section-wall-street`, `#section-hype`, `#section-leadership`, `#section-knowledge` |
| `metrics.html` | `#metric-rev-ttm`, `#metric-rev-fwd`, `#metric-eps-ttm`, `#metric-eps-fwd`, `#metric-pe-fwd`, `#metric-peg-fwd`, `#metric-cash`, `#metric-debt`, `#metric-rsi`, `#metric-52w`, `#metric-gross-margin`, `#metric-net-margin` |
| `finviz.html` | `#section-purpose`, `#section-step1`, `#section-step2`, `#section-step3`, `#section-coverage`, `#section-quickref` |
| `seekingalpha.html` | `#section-account`, `#section-portfolio-create`, `#section-tickers`, `#section-columns`, `#section-sort`, `#section-done` |
| `indices.html` | `#section-types`, `#section-dca`, `#section-lumpsum`, `#section-framework`, `#section-vix`, `#section-timing`, `#section-aaii`, `#section-quality`, `#section-signals`, `#section-sa-setup` |

**Implementation:** The `IntersectionObserver` in `script.js` automatically highlights the active section link as the user scrolls. It derives section targets from the hrefs of `.metric-links a` elements on the page, so it works for all pages without per-page configuration. The FAQ page (`faq.html`) uses an accordion pattern and does not have an "On This Page" block.

---

## 6. Success Criteria

- All 12 metrics explained in plain language with hypothetical illustrative examples
- Philosophy page covers all major conceptual content from the transcript analyses
- FAQ includes practical Q&A on portfolio construction, timing mistakes, market environments, and position sizing
- Site loads with no dependencies and no errors in any modern browser
- Mobile-readable at 375px minimum width
- No real-time data, no company-specific current recommendations, no financial advice language
- Navigation consistent and correct on all 7 pages (8 items including Support)

---

## 7. Key Concepts Documented (Source: Video Transcript Analyses, June 2026)

The following concepts were analyzed from video transcripts and integrated into the site. This section preserves the full concept list for future reference since the original temp analysis file has been deleted. A second transcript ("How to Get Filthy Rich in the Stock Market") was analyzed in the v3.1.0 pass, adding the belief/long-game, hype/weak-hands, margins-as-competitive-position, balance-sheet-as-personal-finance, and buy-cadence concepts to the philosophy page.

| Concept | Site Location |
|---|---|
| Long-term thinking / compounding mindset | philosophy.html (Section 0: The Long Game, Stay on Offense), index.html strategy |
| Belief that significant wealth-building is possible | philosophy.html (Section 0) |
| Plan-to-100 time horizon / underestimating multi-decade compounding | philosophy.html (Section 0) |
| Short-termism / dopamine-culture trap | philosophy.html (Section 0) |
| Stay on offense: regular investing discipline | philosophy.html (Section 4) |
| SWOT analysis framework | philosophy.html (Section 2) |
| Sequential evaluation: business → financials → valuation | philosophy.html (Section 2) |
| Revenue growth as primary screener | metrics.html (Revenue TTM + FWD) |
| Revenue deceleration warning signal (quarterly trend) | metrics.html (Revenue TTM) |
| Peak hype avoidance | philosophy.html (Section 5.5: Hype, Sentiment, and the Weak-Hands Cascade), faq.html (Q9) |
| Weak hands cascade mechanics | philosophy.html (Section 5.5), faq.html (Q9) |
| Buy cadence: at least twice a month | philosophy.html (Section 4) |
| Grow income over cutting expenses | philosophy.html (Section 4) |
| Balance sheet strength (cash > debt) | metrics.html (Total Cash, Total Debt), philosophy.html (Section 2: balance sheet like a person's finances) |
| Balance sheet advantage in rate-hiking cycles | metrics.html (Total Cash) |
| Gross margin trends and thresholds | metrics.html (Gross Margin), index.html reference table |
| Net margin trends and thresholds | metrics.html (Net Margin), index.html reference table |
| Margins as competitive-position signal (power vs weakness); Wall Street prices margin trends | philosophy.html (Section 7: Margins reveal competitive position) |
| CEO and management quality | philosophy.html (Building Investment Knowledge), faq.html (Q4 moat) |
| Market cap vs potential mental model | index.html (Strategy section) |
| Short-term vs long-term price drivers | philosophy.html (Section 1) |
| Opportunities outside tech | philosophy.html (Section 7) |
| Double/lose-50% decision framework | philosophy.html (Section 2) |
| Diversification: 10-20 stocks | index.html (Strategy section), faq.html (Q8) |
| GVD framework: growth/value/dividend stocks | philosophy.html (Section 3) |
| Risk-on vs risk-off market environments | philosophy.html (Section 3), faq.html (Q11) |
| Stocks as ownership, not symbols (farmland analogy) | philosophy.html (Section 1) |
| Wall Street incentive misalignment | philosophy.html (Section 5) |
| Recurring revenue / SaaS business model premium | philosophy.html (implied in business model study), faq.html (Q4 moat) |
| Revenue and net income up and to the right TTM | metrics.html (Revenue TTM, EPS TTM), philosophy.html |
| Dividends as crash-deployment capital | philosophy.html (Section 3) |
| Always research why margins move | metrics.html (Net Margin caveat), philosophy.html (Section 7) |
| Monopoly risk / competitive complacency | philosophy.html (Section 6: Market Leadership Cycles) |
| Market leadership cycles | philosophy.html (Section 6) |
| Unprofitable stocks: position sizing rules | faq.html (Q10) |
| Study business models for pattern recognition | philosophy.html (Section 7) |
| Conference call discipline (listen twice, 2x speed) | philosophy.html (Section 7) |
| Dollar-cost averaging as the default for most investors | indices.html (DCA section), faq.html (DCA vs lump sum) |
| Lump-sum investing superiority on average; the dry-powder trap; hybrid deployment | indices.html (Lump-Sum section), faq.html (DCA vs lump sum) |
| Broad-market vehicles: VT, VTI + VXUS | indices.html (DCA section) |
