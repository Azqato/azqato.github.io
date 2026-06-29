# Azqato — Individual Stock Methodology

A static educational website documenting Azqato's fundamentals-driven, long-term equity investing methodology. Covers stock evaluation, index/ETF timing signals, setup guides for Finviz and Seeking Alpha, and an interactive Nasdaq 100 screener.

**Live site:** [azqato.github.io/stocks](https://azqato.github.io/stocks/)

---

## Tech Stack

| Layer | Technology | Version / Notes |
|-------|-----------|----------------|
| HTML | HTML5 semantic | 8 pages, no preprocessor |
| CSS | CSS3 custom properties | 850+ lines, single file |
| JavaScript | Vanilla ES6 | `script.js` (content pages) + `screener.js` (screener app), no framework |
| Fonts | System fonts only | No external loading |
| Data pipeline | Python 3 + yfinance | Python 3.12, yfinance (latest) |
| Hosting | GitHub Pages | Serves from repo root |
| CI/CD | GitHub Actions | Mon-Fri cron at 23:00 UTC |
| Data format | JSON | `data/screener.json`, `data/nasdaq100.json` |

No npm. No build tools. No frontend dependencies.

---

## Prerequisites

- Any modern browser (Chrome, Firefox, Safari, Edge) for local viewing
- Python 3.12+ only if running or modifying the data pipeline
- `pip` for the single backend dependency (`yfinance`)

Node.js is not required.

---

## Installation

```bash
git clone https://github.com/Azqato/stocks.git
cd stocks
```

For the data pipeline only:

```bash
pip install yfinance
```

---

## Running Locally

No build step required. Open `index.html` directly in a browser, or serve with Python:

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080`. The screener fetches its data feed directly from GitHub (`raw.githubusercontent.com`), so it also works when `screener.html` is opened straight from disk as a `file://` URL — no local server required.

---

## Environment Variables

None. The frontend has no environment variables, and the yfinance data pipeline needs no API key or secret. (A legacy `FMP_API_KEY` GitHub Actions secret from an earlier version is no longer referenced and can be deleted.)

---

## Build and Deploy

This is a static site. There is no build step.

**Deploy:** Push to `main`. GitHub Pages serves directly from the repository root.

**Data pipeline (automated):** GitHub Actions runs `scripts/fetch_screener_data.py` on trading days (Mon-Fri) at 23:00 UTC, commits `data/screener.json` to the repo, and GitHub Pages serves the updated file immediately. The S&P 500 feed follows at 23:30 UTC; the constituent sync runs Saturdays at 23:00 UTC.

**Data pipeline (manual):** Go to Actions → "Refresh Screener Data" → Run workflow. Or run locally:

```bash
python3 scripts/fetch_screener_data.py
```

Output is written to `data/screener.json`.

---

## Project Structure

```
stocks/
├── README.md                         ← This file
├── index.html                        ← Home: strategy overview, metric grid, reference table
├── philosophy.html                   ← Conceptual foundation (9 sections)
├── metrics.html                      ← 12-metric glossary with examples
├── screener.html                     ← Interactive Nasdaq 100 screener (markup + CSS)
├── screener.js                       ← Screener logic (data load, scoring, render, popup)
├── finviz.html                       ← Finviz screener setup guide
├── seekingalpha.html                 ← Seeking Alpha watchlist setup guide
├── indices.html                      ← Index/ETF methodology and timing signals
├── faq.html                          ← Q&A accordion (30 items)
├── style.css                         ← Full design system stylesheet
├── script.js                         ← Accordion + IntersectionObserver sidebar
├── og-image.png                      ← Social card image (1200x630)
├── data/
│   ├── nasdaq100.json                ← Canonical Nasdaq 100 constituent list (100 tickers)
│   ├── sp500.json                    ← Canonical S&P 500 constituent list (~500 tickers)
│   ├── screener.json                 ← Generated Nasdaq 100 feed (Mon-Fri metrics)
│   └── screener_sp500.json           ← Generated S&P 500 feed (Mon-Fri metrics)
├── scripts/
│   ├── fetch_screener_data.py        ← Python pipeline: yfinance → screener feed (--list/--out)
│   └── update_constituents.py        ← Weekly auto-sync: Wikipedia → nasdaq100.json + sp500.json
├── .github/
│   └── workflows/
│       ├── screener-data.yml         ← Nasdaq 100 feed (Mon-Fri 23:00 UTC)
│       ├── screener-data-sp500.yml   ← S&P 500 feed (Mon-Fri 23:30 UTC)
│       └── constituents.yml          ← Constituent sync (Sat 23:00 UTC)
└── docs/
    ├── PRD.md                        ← Product requirements, architecture, runbook
    ├── DESIGN.md                     ← Design system specification
    └── PATCHNOTES.md                 ← Full changelog (v1.0.0 → present)
```

---

## Full Documentation

- [docs/PRD.md](docs/PRD.md) — Product requirements, architecture, runbook, roadmap, FAQ
- [docs/DESIGN.md](docs/DESIGN.md) — Design system, color tokens, typography, component patterns
- [docs/PATCHNOTES.md](docs/PATCHNOTES.md) — Full changelog (v1.0.0 to present)
