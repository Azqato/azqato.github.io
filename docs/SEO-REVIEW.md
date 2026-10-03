# SEO and Landing-Page Review (drafts for the owner)

Build pass item 13; Part 2, P17 in PRD.md. Written 2026-10-02 for the owner to review in one sitting. **Nothing here is live.** Every change below rewrites or moves source text, so each needs the owner's yes, page by page (core rule, D19). Answer with the IDs (S1, L2, M3 and so on): yes, no, or changed wording.

The audit covers all 30 live pages: the home page, 11 root pages and 19 Invests pages. Redirect pages and the local-only `brand/` folder are left out. It was measured by script from the built HTML; nav, header, footer and hidden duplicate blocks don't count toward word counts or links.

## 1. Audit

Targets used: a title of 30 to 65 characters; a meta description of 70 to 160; exactly one h1; no skipped heading levels; at least two links in the content to other pages on the site; and between 150 and 2,500 words, so a page is neither thin nor overlong.

| Page | Words | Findings |
|---|---:|---|
| `index.html` | 330 | ok |
| `about/` | 283 | title short (14: "About - Azqato"); no links in the content |
| `accounts/` | 35 | title short (24); thin; no links in the content |
| `codes/` | 78 | thin; no links in the content |
| `discord/` | 156 | title short (28); no links in the content |
| `links/` | 75 | title short (18); thin |
| `music/` | 30 | title short (27); description 172; thin (by design, it's a visualizer) |
| `privacy-policy/` | 1,193 | title short (23); one link in the content |
| `projects/` | 41 | title short (17); thin (the cards are drawn by script, so crawlers that skip scripts see no projects) |
| `support/` | 349 | title short (25); no links in the content |
| `youtube/` | 66 | title short (25); thin |
| `invests/` | 224 | ok |
| `invests/stocks/` | 1,368 | **no h1**; description 164 |
| `invests/stocks/metrics.html` | 6,270 | long; description 163; one link in the content |
| `invests/stocks/philosophy.html` | 6,366 | long; title 27; one link in the content |
| `invests/stocks/screener.html` | 2,060 | **no h1**; description 303 |
| `invests/indices/` | 6,706 | long (the landing page carries the whole method); description 161 |
| `invests/indices/market.html` | 47 | thin (a live tool); description 176; no links in the content |
| `invests/vix/` | 1,115 + tools | title 29; one skipped heading level; one link in the content |
| `invests/leveraged/` | 386 | ok |
| `invests/leveraged/3sig.html` | 1,637 | title 22; description 162; no links in the content |
| `invests/leveraged/6sig.html` | 1,423 | title 22; no links in the content |
| `invests/leveraged/9sig.html` | 1,768 | title 22; no links in the content |
| `invests/leveraged/hfea.html` | 1,722 | title 21; no links in the content |
| `invests/leveraged/holy-grail.html` | 1,815 | title 27; one link in the content |
| `invests/leveraged/tqqq-ftlt.html` | 1,674 | title 26; description 182; no links in the content |
| `invests/resources/` | 218 | one skipped heading level; no links to other site pages in the content |
| `invests/resources/faq.html` | 11,917 | long; title 20; description 167; one h1 and no other headings |
| `invests/resources/finviz.html` | 1,365 | description 187; one link in the content |
| `invests/resources/seekingalpha.html` | 1,130 | description 172 |

Every page has one topic and a unique title and description. The nav, sidebar and footer link every page to every other, so the low counts above are about links inside the text, which carry more weight with search engines.

## 2. Small fixes (no content moves)

| ID | Change | Pages |
|---|---|---|
| S1 | Add an h1. Individual Stocks: "Individual Stocks" (its hero has no heading). Screener: "Screener". | 2 |
| S2 | Longer titles, for example "About Azqato: Gaming, Streaming and Web Tools", "Azqato's Projects: Web Tools and Strategy Sites", "Leveraged ETF Strategy: 3 Sig (TQQQ) - Azqato Invests". Wording is yours to pick; the rule is the topic first, then the brand. | 21 |
| S3 | Trim descriptions over 160 to one sentence of 160 or less. The longest is the Screener's (303). The trimmed text would come from the source's own sentence. | 11 |
| S4 | Fix the two skipped heading levels (Resources, VIX). These are level changes only, no new words. | 2 |
| S5 | One "Related" line at the end of each leveraged strategy page, linking the other five, and one at the end of Metrics and Philosophy, linking each other and the Screener. These are new link lines, with no new prose. | 8 |
| S6 | Projects: put the project names and descriptions in the HTML, so the grid is readable without scripts. The script keeps the filtering. | 1 |
| S7 | FAQ (11,917 words, no headings): add an h2 per topic group, using the FAQ's existing groups. | 1 |

## 3. Landing-page drafts

The pattern for each group (PRD, Roadmap at a glance, item 13): what the section is, 3 to 5 cards, and a "Start here" button. The long text moves, word for word, to a Method page in the same group (section 4). The intro on each landing page is **the source's own first paragraph, unchanged**. The card blurbs and button labels are new and marked *(new)*.

### L1. Individual Stocks (`/invests/stocks/`)

- **h1:** Individual Stocks
- **Intro (source text):** "Buy companies with strong growth fundamentals. Hold them. Do not sell."
- **Start here button** *(new)*: "Read the method" → `stocks/method.html`
- **Cards** *(new blurbs)*:
  1. The Method: the strategy, the 10 metrics, and portfolio vs. watchlist.
  2. Stock metrics: every metric explained in plain English.
  3. Philosophy: why buy-and-hold on fundamentals.
  4. Screener: the Nasdaq 100 and more, ranked daily by these metrics.
- **Moves to the Method page:** The Strategy; The 10 Metrics; What Strong Metrics Look Like; Portfolio vs. Watchlist (all 1,368 words).

### L2. Indices & ETFs (`/invests/indices/`)

- **h1:** Indices & ETF Investing (unchanged)
- **Intro (source text):** "A separate methodology for evaluating broad market indices and ETFs. Different assets require different frameworks. Where individual stock picking is driven primarily by company fundamentals, index investing is driven primarily by market sentiment, timing signals, and structural efficiency."
- **Start here button** *(new)*: "Read the method" → `indices/method.html`
- **Cards** *(new blurbs; each opens a section of the Method page)*:
  1. When to buy: DCA, lump sum and the hybrid approach.
  2. Timing signals: the VIX, RSI, 52-week range and the 200-day average.
  3. Sentiment: the AAII survey as a contrarian signal.
  4. Fund quality: returns, yield and expense ratio.
  5. Market Overview: the live market table.
- **Moves to the Method page:** every h2 from "Types of Index Funds" through "Seeking Alpha Watchlist Setup for Indices" (about 6,600 words). This is the biggest win: the landing page drops from 6,706 words to about 200.

### L3. VIX Strategy (`/invests/vix/`)

- **h1:** Fear Is a Signal. Use It. (unchanged)
- **Intro (source text):** the hero paragraph and the live VIX reading stay as they are.
- **Start here button:** the existing "See the Live Strategy" button, unchanged.
- **Cards** *(new blurbs)*:
  1. The Method: why buy-and-hold struggles, and the 5 tiers.
  2. VIX Dashboard: today's tier and allocation.
  3. Custom builder: your own tiers and tickers.
  4. Risk Disclosure.
- **Moves to the Method page:** The Problem With Buy and Hold; The Insight; The Strategy; Why Now (about 900 words). The Dashboard, the Custom builder and the Risk Disclosure stay on the landing page, because the tools are what people come back for.
- **Question for you:** P16 just combined the VIX pages into one, at your request. Splitting the method back out is a partial reversal, so **no change is also a reasonable answer here**.

### L4. Leveraged Strategies (`/invests/leveraged/`)

- Already a landing page (386 words, six strategy cards). **Proposed: no change**, apart from S5's related links on the strategy pages.

## 4. Method-page drafts

Each Method page holds the moved text exactly as it is now, in the same order, with the same ids, so old `#section` links can be redirected to it.

| ID | Address | Title (new) | Description (source sentence) |
|---|---|---|---|
| M1 | `/invests/stocks/method.html` | The Azqato Stock Method: 10 Metrics, Buy and Hold | "A free, complete stock picking methodology for long-term investors: 12 plain-English metrics, portfolio construction rules, and a daily-updated Nasdaq 100 screener." |
| M2 | `/invests/indices/method.html` | Index & ETF Method: When to Buy, Signals and Fund Quality | "When to buy index funds and ETFs: VIX action levels, AAII sentiment signals, RSI timing, DCA vs lump-sum math, and structural quality metrics like expense ratio." |
| M3 | `/invests/vix/method.html` | The VIX Strategy Method: 5 Tiers, 4 ETFs | "A rules-based, VIX-driven portfolio strategy. Real-time ETF allocations that increase growth exposure when market fear peaks." |
| M4 | none (L4: no change) | | |

**Old section links.** A visitor with a bookmark such as `/invests/indices/#dollar-cost-averaging` would land on the new short page. The landing page can forward known section ids to the Method page with a small script (the same mechanism the 2.13.6 VIX redirects use). That keeps the compatibility rule: one hop, permanent.

**Note on the stocks description.** The source says "12 plain-English metrics", while the page's heading says "The 10 Metrics". This is the kind of inconsistency P11 lists; I left both as they are.

## 5. What I need from you

1. S1 to S7: yes or no each (S2 and S3: pick or edit the wording).
2. L1 to L3 and M1 to M3: yes, no, or edits. For L3, say whether the VIX method should split out at all.
3. The *(new)* card blurbs: approve or rewrite.

Once approved, these get built in one pass, with `check.py`'s inventory check confirming that nothing was lost in the move.
