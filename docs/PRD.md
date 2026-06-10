# PRD — Azqato Stock Methodology Site

**Version:** 1.0  
**Status:** Draft  
**Author:** Azqato  
**Last Updated:** June 2026

---

## 1. Overview

### 1.1 Goal

Build a static educational website that clearly documents Azqato's individual stock picking methodology. The site should serve as both a personal reference and a public educational resource. It must explain the 10 core evaluation metrics in plain language, showcase real examples, and communicate the philosophy behind long-term conviction investing.

### 1.2 Target Audience

- Beginner to intermediate retail investors
- People who follow Azqato's content across Twitch, YouTube, or Discord (B5TA community)
- Anyone curious about a fundamentals-first, buy-and-hold approach to stock picking

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
| Home | `index.html` | Strategy overview, holdings snapshot, watchlist snapshot, navigation hub |
| Metrics Glossary | `metrics.html` | Deep explanations of all 10 metrics with META as example |
| FAQ / Philosophy | `faq.html` | Expandable FAQ, Palantir story, long-term mindset |

### Shared Assets

| File | Purpose |
|------|---------|
| `style.css` | All global styles |
| `script.js` | Accordion behavior for FAQ |

---

## 3. Page-by-Page Requirements

### 3.1 Home Page (`index.html`)

**Sections (in order):**

1. **Site Header / Nav** — Logo (Azqato text mark), links to Metrics, FAQ. Minimal top bar.

2. **Hero** — One-line thesis statement. Example: "Buy companies with strong growth fundamentals. Hold them. Do not sell."

3. **Strategy Overview** — Short intro paragraph (3-5 sentences) explaining the core philosophy: long-term conviction, no panic selling, watchlist-driven entry timing.

4. **Metric Overview Grid** — 10 cards, one per metric. Each card: metric name, one-sentence plain-English definition, link to full entry on `metrics.html`. Not a table — use a two-column card grid.

5. **Individual Stonks Snapshot** — A clean table showing current holdings. Columns: Symbol, Price (at time of capture), P/E FWD, PEG FWD, RSI, 52W Range. Source note below table.

   Current holdings to include:
   ADBE, AMD, AMZN, AXP, BRK.B, CRM, DELL, ELF, GOOGL, HUBS, INTU, LULU, META, NOW, NVDA, PLNH, REGN, TEAM, TOST, WDAY, ZM

6. **Potential Buys Snapshot** — Same format, showing the watchlist:
   ACN, APP, AXON, BBY, BX, CELH, COUR, CRCL, GS, HNST, HOOD, IFJPY, IMAX, LZ, MNDY, MSFT, NFLX, NKE, PINS, RVLV, SOFI, TER, TTD, UBER, VEEV

7. **FAQ Teaser / CTA** — One line: "Why I never sell. Read the Palantir story." Link to `faq.html`.

8. **Footer** — Disclaimer: "This site is for educational purposes only. Nothing here is financial advice."

---

### 3.2 Metrics Glossary (`metrics.html`)

Each metric entry must include:

- **Name** — Full name and abbreviation
- **What it measures** — One sentence plain definition
- **Why it matters** — 2-3 sentences on how it influences buy decisions
- **How to read it** — What values are good, what are red flags
- **META Example** — Real data from Seeking Alpha screenshots
- **Notes / Caveats** — Edge cases, sector differences, limits of the metric

#### Metric Entries Required

---

**1. Revenue Growth TTM (Trailing Twelve Months)**

- What: Actual revenue growth over the past 12 months, reported vs. prior period
- Why: Confirms the company is growing its top line in reality, not just projection
- How to read: Higher is generally better; compare to sector median
- META example: Revenue FWD shown as 22.48% in watchlist data
- Caveat: TTM looks backward; a company can have slow TTM but accelerating FWD

---

**2. Revenue Growth FWD (Forward)**

- What: Analyst consensus estimate for revenue growth in the next fiscal year
- Why: Shows what the market expects; used alongside TTM to see trajectory
- How to read: Strong FWD > strong TTM = acceleration story. Both strong = conviction play.
- META example: 22.48% FWD from watchlist, EV/Sales FWD at 5.89 per valuation sheet
- Caveat: Estimates can miss. Cross-check with management guidance.

---

**3. EPS Growth TTM (Earnings Per Share, Trailing)**

- What: Percentage growth in earnings per share over the past 12 months
- Why: Confirms the company is not just growing revenue but growing profit
- How to read: Positive and accelerating is ideal. Compare to P/E to assess if growth is priced in.
- META example: 13.52% EPS growth FWD shown in watchlist
- Caveat: EPS can be inflated by buybacks. Check diluted share count.

---

**4. EPS Growth FWD (Forward)**

- What: Consensus analyst estimate for EPS growth in next 12 months
- Why: Core input to PEG calculation. High FWD EPS growth can justify a higher P/E.
- How to read: EPS growth of 20%+ at a P/E under 25 is typically attractive
- META example from Seeking Alpha: Dec 2026: 8.53%, Dec 2027: 12.28%, Dec 2028: 14.20%, Dec 2029: 21.53%
- Caveat: Street estimates are often conservative on high-quality compounders

---

**5. P/E FWD (Forward Price-to-Earnings)**

- What: Current stock price divided by estimated earnings per share for the next 12 months
- Why: Primary valuation anchor. Shows what you are paying for future earnings.
- How to read: Lower P/E FWD = cheaper on earnings basis. But growth rate context is required (see PEG).
- META example: P/E FWD of 18.18 (2026 estimate), declining to 11.66 by 2029 if estimates hold
- META sector comparison: META P/E FWD is 41.27% above sector median but 18.92% below its own 5Y average
- Caveat: P/E alone misleads. A P/E of 50 on a 60% grower can be cheap. A P/E of 12 on a 2% grower can be expensive.

---

**6. PEG FWD (Forward Price/Earnings-to-Growth)**

- What: Forward P/E divided by the forward EPS growth rate. Normalizes valuation by growth.
- Why: The most important single number in this methodology. A PEG under 1.0 typically signals undervaluation relative to growth.
- How to read:
  - PEG < 1.0 = potentially undervalued
  - PEG 1.0 to 2.0 = fairly valued to slightly rich
  - PEG > 2.0 = growth already priced in
- META example: PEG FWD = 0.88. Below 1.0, suggesting META's earnings growth is not fully priced in at current levels.
- Caveat: PEG is only as good as the growth estimate. Use alongside balance sheet health.

---

**7. Total Cash**

- What: Total cash, cash equivalents, and short-term investments on the balance sheet
- Why: A strong cash position gives a company optionality: acquisitions, buybacks, R&D investment, or surviving a downturn without dilution.
- How to read: Compare against Total Debt. Net cash (Cash > Debt) is a positive signal. Watch for cash burn rate on unprofitable companies.
- META example: $81.18B cash vs. $86.77B debt. Near net-neutral. Context: META generates massive free cash flow, so debt is manageable.
- Caveat: Absolute cash figures must be viewed relative to company size and operational burn

---

**8. Total Debt**

- What: All short and long-term debt obligations
- Why: Debt amplifies risk during downturns and can eat into earnings via interest expense. Low debt = resilience.
- How to read: Debt/Cash ratio under 1.0 is ideal. Companies with Debt/Cash above 3x need scrutiny.
- META example: $86.77B debt, but META has ~$150B+ in annual revenue and strong free cash flow. Debt service is not a concern.
- Holdings example from watchlist: HUBS has $247.29M debt vs $1.69B cash — very clean balance sheet.
- Caveat: Not all debt is equal. Low-interest long-term debt for a growing company is very different from high-interest short-term obligations.

---

**9. RSI (Relative Strength Index)**

- What: A momentum oscillator (0-100 scale) that measures the speed and change of recent price movements
- Why: Used to identify entry timing. A lower RSI suggests a stock has been sold off and may be at a better entry point.
- How to read:
  - RSI > 70 = overbought (potentially extended, wait for pullback)
  - RSI 40-60 = neutral
  - RSI < 30 = oversold (potential entry opportunity if fundamentals are intact)
- META example: RSI of 40 at time of research. Neutral-to-mildly oversold. Not chasing.
- LULU example: RSI of 34 — significantly oversold. Worth monitoring for entry.
- Caveat: RSI is a timing signal only. It does not replace fundamental research. A stock with RSI of 25 can still go lower if the business is deteriorating.

---

**10. 52-Week Range**

- What: The lowest and highest price the stock has traded at over the past 52 weeks
- Why: Provides context for where the current price sits. Buying near 52W lows often provides better risk/reward.
- How to read: A stock at 20-40% of its 52W range may be undervalued or in a temporary drawdown. A stock near its 52W high is either a strong compounder or running hot.
- META example: 52W Range $520.28 - $798.25. At $584, META is near the low end of its range — roughly 12% above the 52W low.
- NOW example: 52W Range $81.24 - $211.48. Currently at $106.97 — sitting in the lower third of its range.
- Caveat: 52W lows can be cheap for a reason. Always confirm fundamentals before reading a low price as an opportunity.

---

### 3.3 FAQ Page (`faq.html`)

**Format:** Accordion-style expandable questions. Each question expands to show a detailed answer on click.

**Required Questions and Content:**

---

**Q: Why do you never sell your stocks?**

A: Selling a great company too early is one of the most common and costly mistakes in long-term investing. Read the Palantir story below.

---

**Q: The Palantir Story (Palantir, PLTR)**

5-paragraph essay — required content:

> **Paragraph 1 — The Setup**
> In the early going, Palantir looked like exactly what it was: a data analytics company with government contracts and a polarizing founder. The stock was volatile, the valuation was debated endlessly, and the path to profitability was not obvious. Buying in at $9 per share felt like a calculated risk. The technology was real, the contracts were real, and the data infrastructure thesis — that the world would increasingly need tools to process and act on massive datasets — seemed durable.
>
> **Paragraph 2 — The Early Win**
> Watching a stock climb from $9 to $45 is genuinely exciting. At 5x, the math feels incredible. The inner monologue starts: "This is more than I expected. This is a huge gain. Maybe I should lock it in before it corrects. What if it gives it all back?" These thoughts feel rational. They feel responsible. They feel like prudent risk management. They are not. They are fear dressed up as discipline.
>
> **Paragraph 3 — The Sell**
> The position was sold at $45. After taxes and the emotional weight of the decision, the feeling was one of relief. That relief is the lie that bad habits tell you. At the moment of the sale, the only information acted on was price history. The business was not re-evaluated. The competitive moat was not reassessed. The long-term thesis was not revisited. A number on a screen triggered an emotional response, and the position was closed.
>
> **Paragraph 4 — The Lesson**
> Palantir went to $150. The same number of shares that were sold for $45 — had they been held — would have been worth more than three times more. But the lesson is not about the dollar figure. The lesson is about the framework error. Selling a great business because the price went up is a category mistake. Price and value are not the same thing. A rising price on a quality compounder is not a warning sign. It is confirmation.
>
> **Paragraph 5 — The Rule**
> The rule that came out of this experience is simple: do not sell. Not because it is always correct — nothing in markets is always correct — but because the cost of being wrong when you sell is asymmetric. If you hold a company that goes down 50%, you still own the asset. If you sell a company that goes up 300%, that gain is gone forever. Patience is not passive. It is a decision that is made every single day the position is held. Palantir was a lesson paid for in forgone returns. It only had to happen once.

---

**Q: How do you build a watchlist?**

A: A watchlist is a live queue of companies worth owning but not yet at the right price or valuation entry point. A company enters the watchlist when: the fundamentals pass the 10-metric screen, the business model is understood, and the RSI or 52W position suggests it may be extended. A company moves to the portfolio when RSI cools, price drops into range, or a catalyst makes the risk/reward compelling.

---

**Q: What makes a company worth holding long-term?**

A: Four things: durable revenue growth, expanding margins, strong balance sheet (or clear path to one), and a moat — something that makes the business hard to replicate. If those four things are intact, price fluctuations are noise.

---

**Q: Do you use technical analysis?**

A: Minimally. RSI and 52W range are the two technical signals used. They are entry timing tools only, not directional calls. Fundamentals determine whether to own something. Technicals influence when.

---

**Q: What is the biggest mistake beginner investors make?**

A: Selling winners too early and holding losers too long. This is the opposite of what compounding requires. The strategy here inverts that: hold winners indefinitely and only add new positions when the fundamentals and timing align.

---

## 4. Content Notes

- Use real data from the screenshots throughout: do not fabricate figures
- All Seeking Alpha data should be cited as "Source: Seeking Alpha" in table footnotes
- No financial advice language anywhere — include a clear disclaimer in the footer
- All prose should be in plain English; avoid jargon without definitions
- No em dashes in any copy

---

## 5. Success Criteria

- All 10 metrics are explained in plain language with real examples
- META is used as a consistent reference throughout `metrics.html`
- The Palantir story is formatted as a readable 5-paragraph essay in the FAQ accordion
- Site loads with no dependencies and no errors in any modern browser
- Mobile-readable at 375px width minimum
- Navigation between pages works correctly with consistent header/footer
