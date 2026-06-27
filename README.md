# Azqato — Individual Stock Methodology

A static educational website documenting Azqato's individual stock picking and index/ETF investing methodology. Built as a personal knowledge base and public resource for investors interested in a fundamentals-driven approach to long-term equity investing.

---

## What This Is

This site explains the research framework used to build and maintain a long-term stock portfolio. It covers how to evaluate individual stocks using 10 core metrics, how to use Finviz to screen for candidates, how to configure a Seeking Alpha watchlist, how to approach index and ETF investing using technical signals, and why patient conviction defines the strategy.

No frameworks, no build tools, no dependencies. Pure HTML, CSS, and vanilla JavaScript.

---

## Pages

| File | Description |
|------|-------------|
| `index.html` | Home -- strategy overview, 10-metric summary, key reference table |
| `philosophy.html` | Conceptual foundation -- the long game and belief, stocks as ownership, research and SWOT, GVD framework, stay on offense, Wall Street context, hype and the weak-hands cascade, market leadership cycles, building investment knowledge |
| `metrics.html` | Full glossary of all 10 evaluation metrics with examples and how-to-read guidance |
| `finviz.html` | Finviz stock screener setup guide -- recommended filters and values for candidate discovery |
| `screener.html` | Interactive Nasdaq 100 screener -- rates every constituent against the methodology factors (score + Pass/Watch/Fail verdict). Shows the daily data feed if present, with an optional bring-your-own-key (FMP) refresh |
| `seekingalpha.html` | Seeking Alpha 12-column watchlist setup guide -- free account, exact column configuration |
| `indices.html` | Index and ETF investing guide -- fund types, dollar-cost averaging and lump-sum timing (VT, VTI + VXUS), VIX action levels, AAII sentiment, structural quality metrics, ETF watchlist setup |
| `faq.html` | FAQ and philosophy -- the Palantir story, capital gains strategy, technical analysis, long-term mindset |
| `style.css` | Full design system stylesheet |
| `script.js` | Accordion behavior, IntersectionObserver sidebar highlighting (metrics page) |
| `scripts/fetch_screener_data.py` | Python 3 script using `yfinance` (no API key) that pulls Nasdaq 100 metrics from Yahoo Finance into `data/screener.json` |
| `.github/workflows/screener-data.yml` | Daily GitHub Action that runs the fetch script and commits the refreshed data feed |
| `data/nasdaq100.json` | Canonical Nasdaq 100 constituent list (ticker + name), kept in sync with the authoritative index. **Multi-class rule:** when a company has more than one share class in the index (e.g. Alphabet GOOGL/GOOG), the screener lists only the **Class A voting** shares to avoid duplicate companies |
| `data/screener.json` | Generated data feed consumed by `screener.html` |

---

## Metrics Covered

1. Revenue Growth TTM
2. Revenue Growth FWD
3. EPS Growth TTM
4. EPS Growth FWD
5. P/E FWD (primary signal: P/E below EPS Growth % = underpriced relative to trajectory)
6. PEG FWD
7. Total Cash
8. Total Debt
9. RSI (Relative Strength Index)
10. 52-Week Range

---

## Index / ETF Metrics

| Metric | Type | Purpose |
|--------|------|---------|
| VIX | Timing | Fear gauge -- high VIX = buy signal for broad market exposure |
| RSI | Timing | Oversold positioning for index entry |
| 52W Range | Timing | Price positioning within annual range |
| YTD Performance | Structural | Relative ranking vs peer ETFs |
| 5Y Total Return | Structural | Medium-term track record |
| 10Y Total Return | Structural | Long-term structural advantage |
| Yield | Structural | Income vs cost of holding (yield > expense ratio test) |
| Expense Ratio | Structural | Annual fee drag -- under 0.25% is cheap |

---

## Design

- GitHub Dark-inspired palette. Teal accent `#00d4a0`, background `#0d1117`, surface `#161b22`
- System fonts only -- no external font loading
- CSS Grid sidebar layout with sticky positioning on desktop
- Responsive: sidebar collapses to sticky top nav below 1024px
- IntersectionObserver scroll-tracking sidebar on metrics.html
- Full design spec in `docs/DESIGN.md`

---

## Running Locally

No build step required. Open `index.html` in a browser or serve locally:

```bash
python3 -m http.server 8080
```

---

## Content Philosophy

No real-time data. No live portfolio snapshots. All illustrative examples use hypothetical labels or category descriptions. The Palantir story ($9 buy, $45 sell, $150 outcome) is the one named historical exception -- a first-person account, not a recommendation.

This applies to the site's editorial/teaching content. `screener.html` is a separate interactive tool: it presents live third-party metrics (Financial Modeling Prep) that are clearly labeled, timestamped, opt-in, and carry an educational-use disclaimer. The factor scores it computes are a mechanical application of the documented methodology, not buy/sell recommendations.

This site does not provide financial advice. It documents one investor's personal framework for evaluating equities over a long time horizon.

---

## Author

**Azqato** -- [azqato.github.io](https://azqato.github.io)
