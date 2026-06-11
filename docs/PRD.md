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
| Screener Setup | `screener.html` | Finviz stock screener filter configuration guide |
| Watchlist Setup | `watchlist.html` | Seeking Alpha 12-column watchlist configuration guide |
| Indices & ETF | `indices.html` | VIX, RSI, structural quality metrics, and ETF watchlist setup for index investing |
| FAQ | `faq.html` | Philosophy and practice Q&A in accordion format |

### Shared Assets

| File | Purpose |
|------|---------|
| `style.css` | Full design system stylesheet |
| `script.js` | Accordion behavior and IntersectionObserver sidebar highlight (metrics page) |

### Navigation Order

Home → Philosophy → Metrics → Screener → Watchlist → Indices → FAQ → Support

---

## 3. Page-by-Page Requirements

### 3.1 Home Page (`index.html`)

**Sections (in order):**

1. **Hero:** One-line thesis statement. "Buy companies with strong growth fundamentals. Hold them. Do not sell."

2. **Strategy Overview:** 6-paragraph overview covering: the core approach (buy quality, hold, compounding), watchlist vs portfolio distinction, the cost of early selling, long-term capital gains tax advantage, diversification rule (10-20 stocks), and market cap vs potential mental model.

3. **The 10 Metrics:** 10 metric cards in a 2-column grid, each linking to the full entry on `metrics.html`. Note: Gross Margin and Net Margin are supplementary signals that appear in the glossary but not in the core screener grid. A footer note links to those metric entries.

4. **What Strong Metrics Look Like:** 9-row reference table with Strong Signal, Caution Zone, and What It Confirms for each key metric including Gross Margin and Net Margin rows.

5. **Portfolio vs. Watchlist:** 4-paragraph explanation of entry criteria for portfolio positions vs watchlist names and how to manage the transition between them.

6. **FAQ Teaser:** Links to the Palantir story on `faq.html` and to the Philosophy page.

---

### 3.2 Philosophy Page (`philosophy.html`)

Seven sections covering the conceptual and philosophical foundation of the methodology. This page preserves all concepts from the transcript analysis that do not fit neatly into the quantitative metrics framework.

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

**5. Wall Street vs the Individual Investor**
- AUM fee structure: income grows with assets managed, not returns generated; this misaligns incentives with client wealth building
- Short-term performance management: quarter-to-quarter appearance matters more than long-term outcomes for client retention
- Herd mentality: institutional managers go risk-off together (amplifying downside) and risk-on together (amplifying upside)
- The S&P 500 embarrassment: most actively managed funds cannot consistently beat a mechanical index fund over time
- Practical implication: do not outsource conviction; volatility is not evidence of error; the people generating volatility are playing a different game

**6. Market Leadership Cycles**
- No company stays at the top of the market cap rankings for 30-40 years
- The complacency mechanism: near-monopoly status shifts organizational culture from builders to protectors; engineers lose influence; product quality declines slowly; by the time a disruption arrives, the company lacks the culture to respond
- Implications for holding: continuous reassessment of whether the moat is intact, whether management is building or protecting, whether competitors are taking share
- The opportunity: the next generation of dominant companies likely already exists as small or mid-cap names; studying patterns of past market leaders builds the pattern recognition to identify them early

**7. Building Investment Knowledge**
- Studying historical and current business models: pattern recognition that lets you identify quality before it is widely priced in
- Why sectors beyond technology matter: great long-term compounders exist in consumer brands, specialty retail, financial services, and other non-tech categories
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

### 3.4 Screener Setup (`screener.html`)

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

### 3.5 Watchlist Setup (`watchlist.html`)

Seeking Alpha 12-column individual stocks watchlist configuration. Free account, no credit card required.

**Columns configured:**
Symbol, Market Cap, Price, Change %, Revenue Growth FWD, EPS Growth FWD, P/E Non-GAAP FWD, PEG Non-GAAP FWD, Total Cash, Total Debt, RSI (14), 52 Week Range

---

### 3.6 Indices & ETF Investing (`indices.html`)

Separate methodology for evaluating broad market indices and ETFs. Key insight: indices cannot go to zero; individual stocks can. This asymmetry makes technicals the primary framework for index investing (when to buy) vs fundamentals for individual stocks (what to buy).

**Sections:**
- Types of index funds: Broad Market, Growth, Dividend, Value, Sector-Specific, International
- Fundamentals vs. Technicals: why the question is different for indices
- VIX: The Fear Gauge: five action level ranges with market condition descriptions and deployment postures
- Leveraged ETFs caveat: when to use 2x/3x ETFs (VIX > 45 recovery plays only)
- RSI and 52W Range for index/ETF context
- Structural Quality Metrics: YTD Performance, 5Y Return, 10Y Return, Yield, Expense Ratio
- "What Strong Signals Look Like" reference table
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

## 5. Design System

- GitHub Dark-inspired palette: background `#0d1117`, surface `#161b22`, teal accent `#00d4a0`
- Text primary `#eef3f7`, text secondary `#cbdae6`
- System font stack, no external font loading
- CSS Grid sidebar layout with sticky positioning on desktop
- Responsive: sidebar collapses to sticky top nav below 1024px
- Full design specification in `docs/DESIGN.md`

---

## 6. Success Criteria

- All 12 metrics explained in plain language with hypothetical illustrative examples
- Philosophy page covers all major conceptual content from the transcript analysis
- FAQ includes practical Q&A on portfolio construction, timing mistakes, market environments, and position sizing
- Site loads with no dependencies and no errors in any modern browser
- Mobile-readable at 375px minimum width
- No real-time data, no company-specific current recommendations, no financial advice language
- Navigation consistent and correct on all 7 pages (8 items including Support)

---

## 7. Key Concepts Documented (Source: Video Transcript Analysis, June 2026)

The following 30 concepts were analyzed from video transcripts and integrated into the site. This section preserves the full concept list for future reference since the original temp analysis file has been deleted.

| Concept | Site Location |
|---|---|
| Long-term thinking / compounding mindset | Philosophy (Stay on Offense), index.html strategy |
| Stay on offense: regular investing discipline | philosophy.html (Section 4) |
| SWOT analysis framework | philosophy.html (Section 2) |
| Sequential evaluation: business → financials → valuation | philosophy.html (Section 2) |
| Revenue growth as primary screener | metrics.html (Revenue TTM + FWD) |
| Revenue deceleration warning signal (quarterly trend) | metrics.html (Revenue TTM) |
| Peak hype avoidance | faq.html (Q9) |
| Weak hands cascade mechanics | faq.html (Q9) |
| Balance sheet strength (cash > debt) | metrics.html (Total Cash, Total Debt) |
| Balance sheet advantage in rate-hiking cycles | metrics.html (Total Cash) |
| Gross margin trends and thresholds | metrics.html (Gross Margin), index.html reference table |
| Net margin trends and thresholds | metrics.html (Net Margin), index.html reference table |
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
