# PRD — Azqato Stock Methodology Site

**Version:** 3.24.0
**Status:** Current
**Author:** Azqato
**Last Updated:** 2026-07-02

---

## Problem Statement

Retail investors face a fundamental problem: markets are noisy, opinions are everywhere, and financial media profits from attention rather than accuracy. Beginner and intermediate investors have no structured, opinionated, non-commercial resource that explains not just what metrics to use, but why each one matters, how to read it, and what a complete evaluation actually looks like end-to-end.

Most investing resources either oversimplify (buy low, sell high) or overwhelm (Bloomberg Terminal). Neither helps a motivated person build a repeatable process. Azqato's methodology exists to fill that gap: a documented, first-person framework for long-term equity investing built from years of practice, refined through mistakes, and presented without any commercial incentive.

---

## Target Users

**Primary: Self-directed retail investor, beginner to intermediate**
- Has a brokerage account or is close to opening one
- Has heard terms like P/E ratio and RSI but cannot apply them confidently
- Invests from income (regular contributions), not a lump-sum windfall
- Is prone to panic-selling or chasing hype stocks without a framework to anchor decisions
- Follows Azqato on Twitch, YouTube, or Discord (B5TA community)

**Secondary: Intermediate investor looking to formalize a process**
- Already investing but decisions are ad hoc
- Wants a structured methodology to compare against their current approach
- Comfortable with spreadsheets but not with coding or professional research tools

**Not the target user:**
- Day traders or swing traders (this methodology is explicitly buy-and-hold)
- Professional fund managers or analysts (this is not Bloomberg or FactSet)
- People seeking hot tips or stock picks

---

## Goals

1. Give any motivated reader enough understanding to evaluate a stock using the 12-metric framework
2. Explain the philosophical foundation so readers internalize the rules rather than mechanically applying them
3. Provide practical tool setup guides so readers can replicate the workflow (Finviz + Seeking Alpha)
4. Offer a live Nasdaq 100 screener that applies the methodology's scoring model transparently
5. Cover index/ETF investing separately with appropriate timing-signal frameworks
6. Remain accurate and trustworthy long-term without requiring constant editorial updates

---

## Non-Goals

- Not providing financial advice or personalized recommendations
- Not providing real-time data in editorial content (the screener is a labeled, separate tool)
- Not building a trading platform, portfolio tracker, or brokerage integration
- Not supporting user accounts, authentication, or any backend
- Not covering options, futures, crypto, forex, or any non-equity asset class
- Not covering day trading, swing trading, or technical pattern trading

---

## User Stories

- As a beginner investor, I want to understand what PEG ratio means so that I can evaluate whether a stock's valuation is justified by its growth.
- As an investor who bought at the wrong time, I want to learn when not to buy so that I stop entering positions at peak hype.
- As someone who panicked and sold winners, I want to understand the cost of selling so that I never make that mistake again.
- As a Seeking Alpha user, I want to know exactly which columns to configure so that my watchlist matches the methodology.
- As someone with a lump sum to invest, I want to understand when and how to deploy it into index funds so that I make the mathematically sound decision.
- As a Finviz user, I want the exact filter settings for the methodology so that I can find candidates without doing manual research from scratch.
- As someone overwhelmed by market noise, I want a philosophical framework so that I can distinguish signal from sentiment.
- As an investor wanting to see all 100 Nasdaq companies scored, I want the interactive screener so that I can identify which ones pass or fail the methodology.

---

## Feature List

### MVP (shipped)

- 8 educational pages with sidebar navigation (Home, Philosophy, Metrics, Screener, Finviz, Seeking Alpha, Indices, FAQ)
- 12-metric evaluation framework documented with examples, how-to-read guides, and caveats
- 9-section philosophy page (belief and long game, ownership model, research process, GVD framework, offense cadence, Wall Street critique, hype/weak-hands, leadership cycles, knowledge building)
- 31-item FAQ accordion
- Step-by-step Finviz screener setup guide
- Step-by-step Seeking Alpha watchlist setup guide (12-column layout)
- Index/ETF methodology with VIX action levels, AAII sentiment, RSI, 52W range, structural quality metrics, DCA vs lump sum
- Interactive Nasdaq 100 screener with relative percentile scoring model (100 tickers, daily data feed), expandable to the full S&P 500 on demand via a toggle
- Scoring model: 5 forward metrics ranked against peers, each scored 0–20 by percentile, total /100, Pass/Watch/Fail verdicts
- Methodology popup explaining the scoring model in plain language with worked examples
- Daily yfinance data pipeline via GitHub Actions (no API key required)
- Screener loads its feed directly from GitHub (works even when the file is opened locally), with an offline localStorage cache
- Per-stock breakdown popup (click any row) and percentile-based cell colors that track the score
- Responsive design (desktop, tablet, mobile)
- "On This Page" anchor navigation with IntersectionObserver scroll tracking
- Open Graph and Twitter Card social cards on all pages
- Accessibility: WCAG AA contrast, aria attributes, focus styles, reduced motion support

### Future (post-launch)

- Deeper coverage of index fund types (sector ETFs, international allocation, bond tent strategy)
- Historical backtests of the scoring model showing Pass/Watch/Fail predictive power
- Email or RSS changelog subscription for site updates
- Additional illustrative examples using historical market events
- Separate pages for Growth, Value, and Dividend stock frameworks
- Conference call research guide (how to listen, what to note, how to log insights)

---

## Constraints

- No backend, no server, no database. Static files only.
- No paid APIs or subscriptions in the primary data path (yfinance is free)
- No external font loading (system fonts only)
- No frontend JavaScript libraries or frameworks
- Content must remain accurate without date-bound updates (no "as of today" editorial references)
- Data pipeline must run within GitHub Actions free tier limits
- No user-facing API keys or credentials of any kind
- Site must be instantly servable by opening index.html in a browser. The screener reads its feed from GitHub raw, so it also works when opened as a local `file://`

---

## Assumptions

- GitHub Pages will remain free for this use case indefinitely
- yfinance will remain a viable data source for Nasdaq 100 tickers
- Yahoo Finance data quality is sufficient for educational screening purposes (not institutional-grade)
- The Nasdaq 100 constituent list changes infrequently enough that annual manual review is acceptable
- Seeking Alpha's column configuration UI will not change frequently enough to invalidate the setup guide
- Finviz's free tier filter set will remain available without requiring an account

---

## Success Criteria

- All 12 metrics explained clearly enough that a reader with no finance background can apply them
- Philosophy content covers all major behavioral and conceptual foundations of the strategy
- FAQ answers the most common investor questions (31 items) without requiring outside research
- Screener shows all 100 Nasdaq 100 tickers with current scores, updated daily automatically
- Site loads with no errors and no external requests in any modern browser
- Mobile-readable at 375px minimum width
- No real-time data, no company-specific live recommendations, no financial advice language
- Navigation is consistent and correct on all 8 pages (10 nav items total)
- All pages render a preview card when shared on Discord, X, or Slack

---

## Tenets

Listed in priority order. When two tenets conflict, the higher one wins.

**1. Accuracy over coverage**
Document fewer things correctly than more things loosely. A reader who trusts this site trusts it because every claim they can verify turns out to be right. One wrong statement costs more than ten missing ones.

**2. Permanence over freshness**
Every page should be as useful in five years as it is today. Real-time data, current prices, and company-specific snapshots age immediately. Conceptual frameworks, calibrated thresholds, and illustrative examples do not. When choosing between a vivid current example and a durable hypothetical one, choose the hypothetical.

**3. The reader is motivated, not passive**
Someone reading this site has already decided to learn. Do not pad content to hold attention. Dense, accurate prose is better than diluted prose with callouts. Respect the reader's time by getting to the point.

**4. Tools serve the methodology, methodology does not serve the tools**
Finviz and Seeking Alpha are referenced because they are the best free tools for this workflow, not because they are partners or sponsors. If better tools emerge, the guides should be rewritten without sentiment. The scoring model exists to make the methodology testable, not to make the screener impressive.

**5. Simplicity is a feature**
Zero frontend dependencies, no build tools, no login. This is a deliberate choice. Every dependency is a maintenance burden and a failure point. The site works by opening a file in a browser. That is worth protecting.

**6. Separate the tool from the editorial**
The screener presents live third-party data. The educational pages use hypothetical examples. These are different things and must never be confused. The distinction preserves the integrity of both: live data is labeled and timestamped; educational content is durable and non-specific.

**7. Opinions over hedging**
This methodology has a point of view. It says to buy quality and hold it. It says to ignore short-term price movements. It says selling winners early is almost always wrong. These are controversial positions that real investors disagree with. State them directly. A hedged methodology is not useful to anyone.

---

## Roadmap

### Current Phase: Operational (v3.x)

The site is live, fully featured, and running automated daily data refreshes. The core methodology is documented end-to-end. The screener is scoring all 100 Nasdaq 100 tickers daily. Documentation has been consolidated into four files (README, PRD, DESIGN, PATCHNOTES).

### Milestone Table

| Milestone | Target | Status |
|-----------|--------|--------|
| v1.0.0 — Initial release (3 pages, light theme) | 2026-06 | Complete |
| v1.9.0 — Philosophy page, 12 metrics, content expansion | 2026-06 | Complete |
| v2.x — Social cards, FAQ expansion, punctuation audit, sitewide nav | 2026-06 | Complete |
| v3.0.0 — Leveraged Strategies nav link | 2026-06 | Complete |
| v3.4.0 — Interactive screener + data pipeline | 2026-06 | Complete |
| v3.7.0 — yfinance pipeline, constituent fix | 2026-06 | Complete |
| v3.12.0 — New 5-factor scoring model | 2026-06 | Complete |
| v3.13.0 — Methodology popup on screener | 2026-06 | Complete |
| v3.14.0 — Documentation consolidation (this audit) | 2026-06-27 | Complete |
| v3.15.0 — Relative percentile scoring model | 2026-06-27 | Complete |
| v3.16.0 — Per-stock popup, GitHub-direct loading, FMP removed | 2026-06-27 | Complete |
| v3.17.0–v3.18.0 — Constituent auto-sync; screener.js extraction | 2026-06-27 | Complete |
| v3.19.0 — Mobile hamburger nav; wider popups | 2026-06-28 | Complete |
| v3.20.0 — Tighter verdict bands (Pass 80 / Watch 50 / Fail <50) | 2026-06-28 | Complete |
| v3.21.0 — Per-stock popup shows only scored metrics | 2026-06-29 | Complete |
| v3.22.0 — Expand to S&P 500 toggle (second daily feed) | 2026-06-29 | Complete |
| v3.23.0 — Trading-day (Mon-Fri) refresh; constituents moved to Saturday | 2026-06-29 | Complete |
| v3.24.0 — "Protecting gains after a strong run" theme (FAQ + home + philosophy + indices) | 2026-07-02 | Complete |
| v4.0.0 — Additional philosophy sections; scoring backtest | TBD | Planned |
| Historical screener performance backtest | TBD | Planned |
| Conference call research guide | TBD | Planned |

### Feature Breakdown by Phase

**v3.x (current):** Screener with daily data, relative percentile scoring, methodology popup, documentation consolidation.

**v4.x (planned):** Mobile hamburger nav, additional philosophy content, potential Growth/Value/Dividend standalone pages.

**Post-v4:** Backtests, conference call guide, deeper index/ETF content.

### Explicitly Deferred

- Email/RSS subscription: low priority, no backend, static site constraint makes this complex
- Historical backtests: valuable but requires a separate data collection effort
- Options/crypto/forex coverage: out of scope permanently; this methodology is equities-only

---

## Metrics

### North Star Metric

**Return visit rate:** The percentage of readers who come back within 30 days. A reader who returns has found the content trustworthy and useful enough to consult again. One-time visitors may be curious; return visitors are building a habit.

### Acquisition Metrics

| Metric | Target | Timeframe | Measurement |
|--------|--------|-----------|-------------|
| Monthly unique visitors | 1,000+ | 6 months post-launch | GitHub Pages analytics or Plausible |
| Referral traffic from Discord/Twitch | 30% of sessions | Ongoing | UTM parameters on shared links |
| Organic search impressions | 5,000/month | 12 months | Google Search Console |

### Engagement Metrics

| Metric | Target | Timeframe | Measurement |
|--------|--------|-----------|-------------|
| Average session duration | 4+ minutes | Ongoing | Analytics |
| Pages per session | 2.5+ | Ongoing | Analytics |
| Screener usage rate | 20% of visitors open screener | Ongoing | Analytics (page views) |
| FAQ engagement | 40% of FAQ visitors expand 3+ items | Ongoing | Analytics (events) |

### Retention Metrics

| Metric | Target | Timeframe | Measurement |
|--------|--------|-----------|-------------|
| Return visitor rate (30-day) | 25%+ | Ongoing | Analytics |
| Screener return rate | 40% of screener users return within 7 days | Ongoing | Analytics |

### Performance Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Page load time (LCP) | Under 1.5s on 3G | Lighthouse / PageSpeed Insights |
| JavaScript bundle | Under 5KB | File inspection |
| CSS bundle | Under 50KB | File inspection |
| Time to Interactive | Under 2s | Lighthouse |
| Uptime | 99.9% (GitHub Pages SLA) | GitHub status page |
| screener.json freshness | Updated within 25 hours of previous | GitHub Actions run log |

### Reporting Cadence

- Performance metrics: monthly Lighthouse audit
- Acquisition and engagement: monthly review
- Retention: monthly review
- screener.json freshness: visible in screener "as of" timestamp, checked ad hoc

---

## Runbook

### Local Setup (from a fresh machine)

1. Install a modern browser (Chrome, Firefox, Safari, or Edge)
2. Install Python 3.12+ (only needed for the data pipeline)
3. Clone the repository: `git clone https://github.com/Azqato/stocks.git && cd stocks`
4. Install the pipeline dependency: `pip install yfinance`
5. Open `index.html` in a browser — the site works immediately for all pages except the screener data fetch
6. For the screener to load live data locally, run: `python3 -m http.server 8080` and visit `http://localhost:8080/screener.html`

### Build

There is no build step. The site is pure static files.

### Deploy

1. Commit changes to the `main` branch
2. Push to GitHub: `git push origin main`
3. GitHub Pages automatically serves the updated files within 1–2 minutes
4. Verify deployment at `https://azqato.github.io/stocks/`

GitHub Pages is configured to serve from the repository root. No additional configuration is needed.

### Data Pipeline (Automated)

Two screener data feeds are refreshed automatically, staggered so the default Nasdaq 100 view always has priority:

- **Nasdaq 100** (`data/screener.json`): trading days (Mon-Fri) at 23:00 UTC via `.github/workflows/screener-data.yml`
- **S&P 500** (`data/screener_sp500.json`): trading days (Mon-Fri) at 23:30 UTC via `.github/workflows/screener-data-sp500.yml` (the larger ~500-symbol fetch runs second so it never delays the Nasdaq 100 refresh)
- **Constituent sync** (`data/nasdaq100.json` + `data/sp500.json`): Saturdays at 23:00 UTC via `.github/workflows/constituents.yml`; regenerates a feed only if that index's membership changed
- **Trigger manually:** GitHub Actions tab → the relevant workflow → Run workflow (use this to seed the S&P 500 feed the first time)
- **Run locally:** `python3 scripts/fetch_screener_data.py --list data/nasdaq100.json --out data/screener.json` (the `--list`/`--out` args default to the Nasdaq 100; point them at `data/sp500.json` / `data/screener_sp500.json` for the S&P 500)
- **Output:** each feed holds its index's tickers with price, market cap, cash, debt, growth metrics, P/E, PEG, and timestamps
- **No API key required** for the yfinance pipeline

### Rollback

To revert to a previous version of the site:

```bash
git log --oneline        # find the commit hash
git revert <hash>        # creates a new revert commit
git push origin main     # deploys the revert
```

To revert `data/screener.json` to a known-good version:

```bash
git checkout <hash> -- data/screener.json
git commit -m "revert screener.json to <hash>"
git push origin main
```

### Environment Configs

| Environment | URL | Notes |
|-------------|-----|-------|
| Production | `https://azqato.github.io/stocks/` | Served by GitHub Pages from `main` |
| Local | `http://localhost:8080` | `python3 -m http.server 8080` from repo root |

No staging environment. Changes are previewed locally before pushing to main.

### Common Errors

| Error | Likely Cause | Fix |
|-------|-------------|-----|
| Screener shows no data | `data/screener.json` missing or empty | Run the pipeline manually or wait for the next 23:00 UTC weekday cron run |
| Screener shows stale data banner | screener.json older than 24 hours | Check GitHub Actions — if last run failed, trigger manually |
| GitHub Action fails with HTTP 429 | yfinance rate limit (Yahoo Finance throttling) | Wait and re-run; the pipeline has per-symbol retry logic |
| Page shows unstyled HTML | `style.css` path wrong | Check that style.css is in the same directory as the HTML file |
| Social card image missing | `og-image.png` not at site root | Verify the file exists at root; regenerate with the PowerShell snippet in DESIGN.md |
| Screener sorts wrong | `Infinity`/negative sentinels in sort logic | Negative P/E and PEG are mapped to worst-rank; debt-free companies sort to top of Cash/Debt |
| Screener shows "Couldn't load the data" | Offline, or `raw.githubusercontent.com` unreachable | Check connectivity; the page retries the same-origin copy and a localStorage cache |

### Monitoring

- **Uptime:** GitHub Pages status at `githubstatus.com`
- **Pipeline runs:** GitHub Actions tab in the repository
- **Data freshness:** The screener "as of" timestamp in the top bar
- **Errors:** Browser DevTools console on any page

---

## Technical Requirements

### System Architecture

The site is a fully static architecture. No server processes any requests. No database stores any state. All computation (screener scoring, sorting, filtering) happens client-side in the browser.

```
[GitHub Repository]
       │
       ├── main branch (HTML, CSS, JS, data/)
       │         │
       │    GitHub Pages → serves static files at azqato.github.io/stocks/
       │
       └── GitHub Actions (cron)
                 │
                 ├── Mon-Fri 23:00 UTC → fetch_screener_data.py --list nasdaq100.json → commits data/screener.json
                 │
                 ├── Mon-Fri 23:30 UTC → fetch_screener_data.py --list sp500.json     → commits data/screener_sp500.json
                 │
                 └── Sat 23:00 UTC     → update_constituents.py → regenerates changed feed(s)
```

### Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| HTML | HTML5 semantic | Browser-native |
| CSS | CSS3 custom properties | Browser-native |
| JavaScript | ES6 (vanilla) | Browser-native |
| Data pipeline | Python 3 | 3.12+ |
| Data library | yfinance | Latest |
| Hosting | GitHub Pages | Free tier |
| CI/CD | GitHub Actions | Free tier |
| Data format | JSON | — |
| Version control | Git | — |

### Folder Structure

```
stocks/
├── README.md                          ← Developer front door
├── index.html                         ← Home page
├── philosophy.html                    ← Philosophy (9 sections)
├── metrics.html                       ← 12-metric glossary
├── screener.html                      ← Interactive Nasdaq 100 screener (app: markup + CSS)
├── screener.js                        ← Screener logic (data load, scoring, render, popup)
├── finviz.html                        ← Finviz setup guide
├── seekingalpha.html                  ← Seeking Alpha setup guide
├── indices.html                       ← Index/ETF methodology
├── faq.html                           ← FAQ accordion (31 items)
├── style.css                          ← Design system stylesheet
├── script.js                          ← Accordion + IntersectionObserver (content pages)
├── og-image.png                       ← Social card image (1200×630)
├── data/
│   ├── nasdaq100.json                 ← Nasdaq 100 constituent list (auto-synced)
│   ├── sp500.json                     ← S&P 500 constituent list (auto-synced)
│   ├── screener.json                  ← Nasdaq 100 daily metrics feed
│   └── screener_sp500.json            ← S&P 500 daily metrics feed
├── scripts/
│   ├── fetch_screener_data.py         ← yfinance → screener feed (--list/--out; runs per index)
│   └── update_constituents.py         ← Wikipedia → nasdaq100.json + sp500.json (weekly auto-sync)
├── img/                               ← Historical screenshots
├── .github/
│   └── workflows/
│       ├── screener-data.yml          ← Nasdaq 100 feed (Mon-Fri 23:00 UTC)
│       ├── screener-data-sp500.yml    ← S&P 500 feed (Mon-Fri 23:30 UTC)
│       └── constituents.yml           ← Constituent sync (Sat 23:00 UTC)
└── docs/
    ├── PRD.md                         ← This file
    ├── DESIGN.md                      ← Design specification
    └── PATCHNOTES.md                  ← Full changelog
```

### Data Models

**nasdaq100.json**

```json
[
  { "t": "NVDA", "n": "NVIDIA" },
  { "t": "AAPL", "n": "Apple" }
]
```

Array of 100 objects. `t` = ticker symbol (string), `n` = company name (string). Multi-class rule: when a company has multiple share classes in the index (e.g., Alphabet GOOGL/GOOG), only the Class A voting shares are listed.

**screener.json**

```json
{
  "updated": "2026-06-27T23:51:56.164931Z",
  "source": "yahoo",
  "stocks": {
    "NVDA": {
      "t": "NVDA",
      "name": "NVIDIA",
      "price": 192.53,
      "marketCap": 4663269130240.0,
      "cash": 53171998720.0,
      "debt": 12814000128.0,
      "revTTM": 85.2,
      "epsTTM": 214.5,
      "peFwd": 21.483,
      "epsFwd": 87.88,
      "revFwd": 81.4,
      "pegFwd": 0.59,
      "priceUpdated": "2026-06-27T23:51:56.164931Z",
      "fundamentalsUpdated": "2026-06-27T23:51:56.164931Z"
    }
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `updated` | ISO 8601 string | Timestamp of the pipeline run |
| `source` | string | Data source identifier ("yahoo") |
| `t` | string | Ticker symbol |
| `name` | string | Company name |
| `price` | number | Current stock price (USD) |
| `marketCap` | number | Market capitalization (USD) |
| `cash` | number | Total cash and equivalents (USD) |
| `debt` | number | Total debt (USD) |
| `revTTM` | number | Revenue growth TTM (%) |
| `epsTTM` | number | EPS growth TTM (%) |
| `peFwd` | number | Forward P/E (price ÷ current-FY EPS) |
| `epsFwd` | number | Forward EPS growth (%) — GAAP basis |
| `revFwd` | number | Forward revenue growth (%) |
| `pegFwd` | number | PEG ratio (Yahoo `pegRatio` field, long-term growth based) |
| `priceUpdated` | ISO 8601 string | Timestamp of price data |
| `fundamentalsUpdated` | ISO 8601 string | Timestamp of fundamentals data |

### API Design (Internal Data Flow)

The site has no traditional API. The internal data flow for the screener is:

1. `screener.html` loads in the browser, defaulting to the Nasdaq 100 universe
2. On load it reads any cached copy of the active feed from `localStorage` and renders it immediately, then fetches the latest `screener.json` from GitHub — `raw.githubusercontent.com/.../data/screener.json` first (so it works even when the file is opened locally), falling back to the same-origin `data/screener.json`
3. On success the fresh feed replaces the data and is written back to the localStorage cache; if every source fails, the last cached copy is kept (or a "Couldn't load" message is shown)
4. **Expand to S&P 500:** clicking the toggle lazy-fetches `data/screener_sp500.json` the same way (separate localStorage cache key) and swaps it into the table; both datasets are held in memory so toggling back to the Nasdaq 100 is instant. On-screen labels (`.universe-name` spans, page title) swap to match. If the S&P 500 feed hasn't been generated yet, the view stays on the Nasdaq 100 with an explanatory message
5. If the feed is more than 24 hours old, an informational stale banner is shown (the daily refresh likely hasn't run)
6. `computeScoreMap()` ranks the loaded stocks and computes each one's relative percentile score and per-metric points client-side — so scores are relative to whichever universe is active
7. `render()` applies sort, filter, and column visibility to produce the table DOM; clicking a row opens a per-stock breakdown popup
8. No data is sent to any server; the only network requests are the read-only fetches of the public feeds

### Screener Scoring Model (v3.15+)

A relative, percentile-based model. Each stock is ranked against its loaded Nasdaq 100 peers on five forward metrics; each metric awards 0–20 points by percentile rank; the five sum to a score of 0–100. (This replaced the v3.12 absolute-threshold model.)

| Metric | Direction | Value ranked |
|--------|-----------|--------------|
| Revenue Growth FWD | higher is better | `revFwd` |
| EPS Growth FWD | higher is better | `epsFwd` |
| P/E vs EPS Growth | lower is better | `peFwd / epsFwd`; a negative `peFwd` (unprofitable) or `epsFwd ≤ 0` (shrinking forward earnings) ranks worst rather than cheapest or dropped |
| PEG FWD | lower is better | `pegFwd` (Yahoo); when forward P/E ≤ 0, ranks worst and the column shows our own negative `peFwd / epsFwd` instead of Yahoo's misleading positive |
| Cash vs Debt | higher is better | `cash / debt` (no debt ranks best) |

**Percentile → points:** `points = clamp(40 × (percentile − 0.25), 0, 20)`. Bottom quartile (≤ 25th percentile) scores 0; top quartile (≥ 75th) scores 20; the median scores 10. Ties take the average rank.

**Score:** sum of the five metric points, rescaled to /100 across whichever metrics a stock has (missing metrics are dropped). A stock at the median on all five scores 50.

**Verdict bands:** Pass ≥ 80, Watch 50–79, Fail < 50.

**Factors chip:** count of metrics scoring 15+/20 (roughly the top third of the peer group on that metric).

**Relative-scoring caveats:** because grades are peer-relative, a stock's score can change when *other* companies' numbers change, and roughly the bottom third of the index always lands in Fail. Scores are computed over the currently loaded set (normally all 100 from the daily feed).

**Cell colors:** every colored cell follows the same percentile ranking, not absolute thresholds — green = top quartile on that metric, red = bottom quartile, amber = middle half, gray = no data. The TTM growth columns are ranked for color only (they do not feed the score). A negative forward P/E or PEG renders red and sorts as a worst (expensive) value, never a cheap one.

**Per-stock popup:** clicking any row opens a focused breakdown for that stock — for each of the five scored metrics, its value, percentile, and 0–20 points, color-coded, with the total score and verdict. The unscored TTM context rows are not shown in the popup (they remain in the main table). Reuses the modal component.

### State Management

Client-side state lives in two places:

1. **DOM:** Sort column, sort direction, active filter chip, column visibility, search query — all derived from UI interactions and re-applied on each render
2. **localStorage:** A cached copy of the public daily feed, used only as an offline fallback. No credentials are stored.

No cookies. No session storage. No server-side state.

### Third-Party Integrations

| Service | Purpose | Authentication | Data Sent |
|---------|---------|---------------|-----------|
| Yahoo Finance (via yfinance) | Daily data pipeline (server-side, in GitHub Actions) | None (public) | Ticker symbols in HTTP requests |
| GitHub (raw + Pages) | Static hosting and the screener's data feed | None for reads | None (read-only fetch of a public JSON file) |
| GitHub Actions | CI/CD scheduling | GitHub account (owner only) | None from users |

### Performance Requirements

| Metric | Target |
|--------|--------|
| Largest Contentful Paint (LCP) | Under 1.5s on 3G |
| Time to Interactive (TTI) | Under 2s on 3G |
| JavaScript | `script.js` ~49 lines (content pages); `screener.js` ~490 lines (loaded only on the screener page) |
| CSS total | Under 50KB (style.css: ~850 lines) |
| screener.json size | Under 100KB for 100 tickers |
| Font requests | 0 (system fonts only) |

### Known Technical Debt

| Debt | Description | Correct Solution |
|------|-------------|-----------------|
| Constituent name quality | New tickers added by the auto-sync use cleaned Wikipedia names, which may be slightly longer than the curated short names | Hand-edit `data/nasdaq100.json` names after a sync if desired (existing names are preserved automatically) |
| screener.json committed to repo | The data file is versioned alongside code, bloating git history over time | Move to GitHub Releases or a separate artifact storage for generated data files |

---

## Security

### Authentication Model

None. The site is fully public. There are no user accounts, no sessions, no login flows, and no credentials of any kind. The screener only performs a read-only fetch of a public JSON feed.

### Authorization Model

No role-based access. All content is publicly readable. The only write access is the GitHub Actions workflow committing `screener.json`, which is governed by GitHub's repository permissions (owner-only push to main).

### Data Storage

The site stores no user data. The only browser storage is:

- **localStorage:** a cached copy of the public daily feed (offline fallback only). No credentials, no PII.
- **No cookies.**
- **No analytics that collect PII** (if analytics are added, use a privacy-preserving tool like Plausible).

### Environment Variables

No secrets are used or hardcoded. (A legacy `FMP_API_KEY` GitHub Actions secret from an earlier version is no longer referenced by any workflow and can be deleted.)

### Third-Party Trust

| Service | Data Received | Notes |
|---------|--------------|-------|
| Yahoo Finance | Ticker symbols (server-side, in the pipeline) | Public endpoints, no user PII |
| GitHub (raw + Pages) | Read-only file fetches | Serves static files / the public JSON feed |
| GitHub Actions | None from end users | Repository automation only |

### Known Attack Surface

| Area | Risk | Mitigation |
|------|------|------------|
| screener.json injection | Malicious content in the data file could be rendered as HTML | The data file is owner-controlled (only the GitHub Action writes it). Cell values come from number formatting; ticker/name come from the static constituent list. No user-supplied HTML is rendered. |
| Dependency supply chain | yfinance is a third-party library | Pin yfinance version in the Actions workflow; monitor for new releases. |
| GitHub Pages serving | Cached stale content | GitHub Pages cache is controlled by GitHub; not a controllable risk at this layer. |

### Dependency Policy

- Frontend: zero dependencies. No monitoring required.
- Backend: one dependency (yfinance). Monitor the yfinance GitHub repository for security advisories. Pin to a specific version in the Actions workflow rather than using `latest` for production stability.

---

## Press Release

**FOR IMMEDIATE RELEASE**

### Free Tool Lets Everyday Investors Apply a Proven Fundamentals Framework to the Entire Nasdaq 100

**New site from independent investor Azqato gives retail investors a complete methodology, interactive screener, and step-by-step guides — all without paying for a subscription or selling their data**

*Seattle, WA — June 2026* — Azqato, an independent long-term investor and content creator, today launched a comprehensive public resource at `azqato.github.io/stocks` documenting the complete individual stock picking methodology he has refined over years of active investing. The site combines in-depth educational content, practical tool setup guides, and a live interactive screener that evaluates every Nasdaq 100 company against a 5-factor scoring model, updated daily.

The site addresses a real gap in publicly available investing education. While financial media is abundant, structured, non-commercial investing frameworks are rare. Most free resources either oversimplify or exist to sell something. Azqato's site does neither: it documents a real methodology built from practice, presented with the same directness he brings to his Twitch streams and YouTube videos.

The site covers twelve evaluation metrics (revenue growth, EPS growth, P/E, PEG, cash, debt, RSI, 52-week range, gross margin, and net margin), a nine-section philosophy page on long-term conviction investing, thirty Q&A items in an interactive accordion, and setup guides for both Finviz and Seeking Alpha. For index investors, a separate methodology covers VIX action levels, AAII sentiment signals, dollar-cost averaging, and lump-sum deployment strategy. The interactive Nasdaq 100 screener scores all 100 constituents daily using a transparent algorithm and shows each stock's Pass, Watch, or Fail verdict at a glance.

"I kept explaining the same framework to the same questions over and over in streams and Discord," said Azqato. "Building this site meant I could say: here, read this. It is everything I know about how to evaluate a stock, written down in one place, for free."

The site is available now at `azqato.github.io/stocks`. No account required. No email address. No subscription.

**About Azqato**
Azqato is an independent investor and content creator focused on long-term, fundamentals-driven equity investing. He publishes investing methodology content on Twitch, YouTube, and Discord (B5TA community), and maintains a suite of free public tools and sites at `azqato.github.io`.

---

## Frequently Asked Questions

### External FAQ (User-Facing)

**1. What is this site?**
A free educational resource documenting Azqato's individual stock picking methodology. It explains which metrics to evaluate, how to read them, how to find candidates using Finviz, how to track them in Seeking Alpha, and how to think about index/ETF investing alongside individual stocks.

**2. Who is this for?**
Beginner to intermediate retail investors who want a structured, non-commercial framework for long-term equity investing. Especially useful for people who follow Azqato on Twitch, YouTube, or Discord (B5TA community).

**3. Is this financial advice?**
No. This site documents one investor's personal methodology. Nothing here is a recommendation to buy or sell any specific security. Every page includes an "Educational use only. Not financial advice." disclaimer.

**4. How do I use the site?**
Start at the Home page to see the strategy overview and the 10-metric framework. Read Philosophy if you want to understand the mindset behind the rules. Use Metrics as a reference when evaluating a specific signal. Use Finviz and Seeking Alpha pages to set up your research tools. Use the Screener to see how all 100 Nasdaq companies score against the methodology today. Use FAQ when you have questions about the strategy.

**5. What are the 12 metrics?**
Revenue Growth TTM, Revenue Growth FWD, EPS Growth TTM, EPS Growth FWD, P/E FWD, PEG FWD, Total Cash, Total Debt, RSI, 52-Week Range, Gross Margin, and Net Margin. The first 10 are tracked in the screener. Gross Margin and Net Margin are evaluated during research.

**6. What is the Nasdaq 100 screener?**
An interactive tool that applies the methodology's 5-factor scoring model to all 100 Nasdaq 100 companies. Data is updated daily from Yahoo Finance. Each company receives a score from 0 to 100 and a Pass, Watch, or Fail verdict. This is a screening and educational tool, not a buy/sell signal generator.

**7. How does the screener score stocks?**
Each stock is ranked against the other Nasdaq 100 companies on five forward metrics: Revenue Growth FWD, EPS Growth FWD, P/E vs EPS Growth, PEG FWD, and Cash vs Debt. Each metric awards 0–20 points by percentile (bottom quarter scores 0, the median 10, the top quarter 20), and the five sum to a score of 0–100. Pass is 80+, Watch is 50–79, Fail is under 50. It is a relative ranking, so a high score means a stock looks better than most of the index right now rather than that it cleared a fixed target. The Methodology button on the screener explains it with a worked example.

**8. How often is the screener data updated?**
On trading days (Monday through Friday) at 23:00 UTC via an automated pipeline. Weekends are skipped because the US market is closed. The "as of" timestamp in the screener header shows when the data was last refreshed.

**9. Where does the screener data come from?**
Yahoo Finance, fetched on trading days by a Python script (using the free yfinance library) that runs in GitHub Actions and commits the result. No API key is required, and there is nothing to configure — the page just reads the published feed from GitHub.

**10. Does the screener use real-time data?**
No. It uses data from the most recent pipeline run (refreshed once per trading day at 23:00 UTC). Prices shown reflect the close or after-hours price at the time of the last fetch.

**11. What is the Palantir story?**
A first-person account where Azqato bought Palantir at $9, sold at $45, and watched it go to $150. It is the single most important lesson documented on the site: selling a business because the price went up is a category mistake. Price and value are not the same thing. It lives on the FAQ page.

**12. Do I need to pay for anything?**
No. The site is entirely free with nothing to configure. Finviz's screener is free (no account needed). Seeking Alpha has a free account tier that covers the 12-column watchlist setup described. The screener's daily data feed is free and requires no API key.

**13. Do you cover short selling, options, or crypto?**
No. This methodology covers long-only equity investing with a buy-and-hold time horizon. Derivatives and crypto are outside scope.

**14. What is the recommended portfolio size?**
10–20 stocks. Fewer than 10 concentrates risk; more than 20 dilutes conviction. Every position should be high-conviction within that range.

**15. When should I sell a stock?**
The short answer: rarely. The methodology's default posture is to hold quality positions through volatility. Selling is appropriate when the fundamental thesis has changed (not just because the price moved), or when the balance sheet or margins have deteriorated materially over multiple quarters.

**16. How do I find stocks to evaluate?**
Use the Finviz guide to set up a screener that filters for candidates meeting the methodology's basic thresholds. Then move candidates to a Seeking Alpha watchlist (12-column setup guide on the site) to track them over time.

**17. Is Dollar-Cost Averaging or lump-sum investing better?**
For regular income-stream investing (each paycheck), DCA-style contributions are the right default. For a one-time pool of money, lump-sum investing beats DCA on average in about 2/3 of historical 12-month windows, rising to roughly 90% at 36 months. The Indices page covers both approaches in detail.

**18. What does the VIX have to do with investing?**
VIX is a fear gauge: it measures implied volatility in S&P 500 options. When VIX is elevated (25+), fear is high, and broad market prices are typically lower. This makes it a useful contrarian indicator for timing index and ETF purchases. The Indices page covers VIX action levels (5 bands from below 15 to above 45).

**19. What is AAII sentiment?**
The AAII Investor Sentiment Survey is a weekly poll of retail investor outlook (bullish, neutral, or bearish). Published Thursdays since 1987. It is used as a contrarian indicator: when more than 60% of respondents are bearish, that historically marks or precedes major market bottoms. The Indices page has the full framework.

**20. Why does holding for more than 12 months matter?**
Tax treatment. In the US, positions held more than 12 months qualify for long-term capital gains tax rates (15–20%) rather than short-term rates (22–37% ordinary income). The hidden cost of impatience includes paying the higher rate on every gain realized too early.

**21. How is this different from just buying an S&P 500 index fund?**
An index fund is a valid and often superior choice for most investors. This methodology adds a layer: identifying individual companies with above-average growth trajectories at reasonable valuations, which may outperform a broad index over long periods if the fundamentals thesis is correct. Both approaches have a place: the Indices page covers ETF investing as a distinct and complementary strategy.

**22. Is the site code open source?**
Yes. The repository is public on GitHub. The code is simple enough to read directly: one CSS file, one JS file, one Python script.

**23. What sites does Azqato also run?**
The portfolio site at `azqato.github.io`, ComposerAtlas (a strategy research tool), and a Leveraged Strategies site. The stock methodology site links to Leveraged Strategies in the sidebar nav.

**24. What if I disagree with the methodology?**
The methodology is opinionated by design. It says to buy quality and hold it, to ignore short-term price movements, and to treat selling winners as almost always wrong. These are real positions that real investors disagree with. If you have a different framework, this site may still be useful as a reference for how to evaluate specific metrics, even if the overall philosophy does not match yours.

**25. How do I get help or report an issue?**
Reach out in Azqato's Discord (B5TA community) or open a GitHub issue on the repository.

---

### Internal Stakeholder FAQ

**What is the return on investment for maintaining this site?**
The site serves two functions: it converts interested viewers into engaged community members who understand the methodology deeply, and it serves as a reference that reduces repetitive explanation in streams and Discord. Both contribute to the quality of the community around Azqato's content.

**What are the success metrics?**
Return visitor rate (25%+ within 30 days) and average session duration (4+ minutes). These indicate that readers are finding the content trustworthy and useful enough to consult repeatedly. See the Metrics section above for the full table.

**What is the roadmap direction?**
Deepen existing content before adding new content. The philosophy and metrics pages are more valuable when they are exceptionally thorough than when new pages are added at average quality. The next meaningful additions are a mobile navigation improvement and a conference call research guide.

**How do we ensure the methodology stays accurate over time?**
The site is deliberately designed to avoid time-sensitive claims. All editorial content uses hypothetical examples, conceptual frameworks, and calibrated thresholds rather than current prices or live company data. Threshold updates (e.g., "strong gross margin is 50%+") require review when market structures change, but this is infrequent.

**How is the screener data quality monitored?**
The "as of" timestamp in the screener header shows the last refresh time. If the daily pipeline fails, GitHub sends an email notification to the repository owner. The pipeline is designed to retry failed symbol fetches automatically and commit whatever data was successfully retrieved.

**What is the documentation strategy going forward?**
Four files: README.md (developer front door), PRD.md (this file, the comprehensive reference), DESIGN.md (design system), PATCHNOTES.md (full changelog). All major changes are documented in PATCHNOTES.md. PRD.md is updated when product requirements, architecture, or process changes significantly. Documentation changes are included in version increments.

---

## Site Structure Reference

### Navigation Order (10 items)

Home → Philosophy → Metrics → Screener → Finviz → SeekingAlpha → Indices → FAQ → Leveraged Strategies → Support

**Nav label rule:** Every sidebar nav label is a single token (no spaces) except the two trailing external links. Labels: Home, Philosophy, Metrics, Screener, Finviz, SeekingAlpha, Indices, FAQ, Leveraged Strategies, Support.

### Pages and Their Section IDs

| Page | Section IDs ("On This Page") |
|------|------------------------------|
| `index.html` | `#section-strategy`, `#section-metrics-grid`, `#section-reference`, `#section-portfolio` |
| `philosophy.html` | `#section-possible`, `#section-ownership`, `#section-research`, `#section-gvd`, `#section-offense`, `#section-wall-street`, `#section-hype`, `#section-leadership`, `#section-knowledge` |
| `metrics.html` | `#metric-rev-ttm`, `#metric-rev-fwd`, `#metric-eps-ttm`, `#metric-eps-fwd`, `#metric-pe-fwd`, `#metric-peg-fwd`, `#metric-cash`, `#metric-debt`, `#metric-rsi`, `#metric-52w`, `#metric-gross-margin`, `#metric-net-margin` |
| `finviz.html` | `#section-purpose`, `#section-step1`, `#section-step2`, `#section-step3`, `#section-coverage`, `#section-quickref` |
| `seekingalpha.html` | `#section-account`, `#section-portfolio-create`, `#section-tickers`, `#section-columns`, `#section-sort`, `#section-done` |
| `indices.html` | `#section-types`, `#section-dca`, `#section-lumpsum`, `#section-framework`, `#section-vix`, `#section-timing`, `#section-aaii`, `#section-quality`, `#section-signals`, `#section-sa-setup` |
| `faq.html` | No "On This Page" block (accordion pattern) |
| `screener.html` | No "On This Page" block (app page, no long-form sections) |

### Content Philosophy (Enforced Rules)

- No real-time data in editorial content
- All illustrative examples use hypothetical labels ("High-growth tech co.", "Accelerating")
- No company-specific live examples (the Palantir story is the one named historical exception)
- No em dashes in any form: ` -- `, `—`, or `&mdash;`
- No "- Azqato" suffix on `<title>` or `og:title`
- No financial advice language
- "Educational use only. Not financial advice." in every page's sidebar footer

### Key Concepts Documented (Video Transcript Analysis)

The following concepts were integrated from video transcript analyses. This table preserves the full concept inventory.

| Concept | Site Location |
|---------|--------------|
| Long-term thinking / compounding mindset | philosophy.html (Section 0, Stay on Offense), index.html |
| Belief that significant wealth-building is possible | philosophy.html (Section 0) |
| Plan-to-100 time horizon / underestimating multi-decade compounding | philosophy.html (Section 0) |
| Short-termism / dopamine-culture trap | philosophy.html (Section 0) |
| Stay on offense: regular investing discipline | philosophy.html (Section 4) |
| SWOT analysis framework | philosophy.html (Section 2) |
| Sequential evaluation: business first, then financials, then valuation | philosophy.html (Section 2) |
| Revenue growth as primary screener | metrics.html (Revenue TTM + FWD) |
| Revenue deceleration warning signal (quarterly trend) | metrics.html (Revenue TTM) |
| Peak hype avoidance | philosophy.html (Section 5.5), faq.html |
| Weak-hands cascade mechanics | philosophy.html (Section 5.5), faq.html |
| Buy cadence: at least twice a month | philosophy.html (Section 4) |
| Grow income over cutting expenses | philosophy.html (Section 4) |
| Balance sheet strength (cash > debt) | metrics.html (Cash, Debt), philosophy.html (Section 2) |
| Balance sheet advantage in rate-hiking cycles | metrics.html (Total Cash) |
| Gross margin trends and thresholds | metrics.html (Gross Margin), index.html reference table |
| Net margin trends and thresholds | metrics.html (Net Margin), index.html reference table |
| Margins as competitive-position signal | philosophy.html (Section 7) |
| Wall Street prices margin trends | philosophy.html (Section 7) |
| Market cap vs potential mental model | index.html |
| Short-term vs long-term price drivers | philosophy.html (Section 1) |
| Opportunities outside tech | philosophy.html (Section 7) |
| Double/lose-50% decision framework | philosophy.html (Section 2) |
| Diversification: 10–20 stocks | index.html, faq.html |
| GVD framework: growth/value/dividend stocks | philosophy.html (Section 3) |
| Risk-on vs risk-off market environments | philosophy.html (Section 3), faq.html |
| Stocks as ownership (farmland analogy) | philosophy.html (Section 1) |
| Wall Street incentive misalignment | philosophy.html (Section 5) |
| Revenue and net income up and to the right TTM | metrics.html, philosophy.html |
| Dividends as crash-deployment capital | philosophy.html (Section 3) |
| Always research why margins move | metrics.html (Net Margin), philosophy.html (Section 7) |
| Competitive complacency / market leadership cycles | philosophy.html (Section 6) |
| Unprofitable stocks: position sizing rules | faq.html |
| Study business models for pattern recognition | philosophy.html (Section 7) |
| Conference call discipline | philosophy.html (Section 7) |
| Dollar-cost averaging as the default | indices.html (DCA section), faq.html |
| Lump-sum superiority on average; dry-powder trap; hybrid | indices.html (Lump-Sum), faq.html |
| Broad-market vehicles: VT, VTI + VXUS | indices.html (DCA section) |

---

## Documentation Process

### How This File Is Maintained

This PRD is the comprehensive reference for the project. It should be updated whenever:
- A new feature ships that changes the product requirements, architecture, or user stories
- A new page or major section is added to the site
- The scoring model or methodology thresholds change materially
- The data pipeline changes in a way that affects data model fields or quality
- The roadmap or metrics targets change

Updates to this file are versioned in PATCHNOTES.md like any other change.

### How PATCHNOTES.md Is Maintained

Every code change, content change, or documentation change gets a new entry. Format:

```
## v<MAJOR>.<MINOR>.<PATCH> — YYYY-MM-DD — Title

Brief summary sentence.

### Added
- What was added

### Changed
- What was changed

### Fixed
- What was fixed

### Removed
- What was removed
```

Version bumps follow semantic versioning:
- MAJOR: breaking changes, complete redesigns, migration events
- MINOR: new features, new pages, new sections
- PATCH: bug fixes, copy corrections, small improvements

### What NEVER Goes in Memory or Documentation as a Standalone File

- Ephemeral task lists or in-progress work
- PR descriptions (these belong in the commit and PR)
- Debugging sessions (the fix is in the code; the commit message has the context)
- Time-sensitive market commentary
- Specific current stock data or prices
