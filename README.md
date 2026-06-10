# Leveraged Strategies

A static, multi-page educational site covering six leveraged ETF strategies. Built with vanilla HTML, CSS, and JavaScript. No frameworks, no build tools. Hosted on GitHub Pages.

**Author:** Azqato
**Status:** Live (M3 complete)
**Live site:** https://azqato.github.io/leveraged-strategies/
**Repository:** https://github.com/Azqato/leveraged-strategies

---

## What This Site Is

A methodology library for six distinct leveraged ETF strategies. Each strategy gets its own dedicated page with a consistent structure: overview, rules and logic, performance notes, risks and caveats, and resources. The site is educational. It documents strategy frameworks, not live trades or recommendations.

## Pages

| Page | File | Description |
|------|------|-------------|
| Home | `index.html` | Landing hub introducing leveraged ETFs and linking to all strategies |
| 3 Sig | `3sig.html` | The 3% Signal quarterly rebalancing plan (Jason Kelly, unleveraged) |
| 6 Sig | `6sig.html` | The 6% Signal quarterly rebalancing plan (Jason Kelly, 2x leveraged) |
| 9 Sig | `9sig.html` | The 9% Signal quarterly rebalancing plan (Jason Kelly, 3x TQQQ) |
| TQQQ For The Long Term | `tqqq-ftlt.html` | Rules-based daily algorithm using SMA regime switching and RSI mean reversion (u/derecknielsen) |
| Holy Grail | `holy-grail.html` | TQQQ FTLT variant using TQQQ's own 200D SMA with SOXL mean reversion and 20% cash buffer |
| HFEA | `hfea.html` | Hedgefundie's Excellent Adventure: 55% UPRO / 45% TMF quarterly rebalanced risk parity |

## Project Structure

```
/
  index.html
  3sig.html
  6sig.html
  9sig.html
  tqqq-ftlt.html
  holy-grail.html
  hfea.html
  css/
    style.css
  js/
    main.js
  strategies/
    3sig.md          ← full content written
    6sig.md          ← full content written
    9sig.md          ← full content written
    tqqq-ftlt.md     ← full content written
    holy-grail.md    ← full content written
    hfea.md          ← full content written
  docs/
    prd.md
    design.md
    patchnotes.md
  README.md
```

- `/strategies` holds the source-of-truth markdown for each strategy. These are reference documents, not live-rendered content. Each file includes a `<!-- RESEARCH SOURCES -->` comment block with all research URLs used; this block is never ported to HTML.
- `/docs` holds the product requirements (`prd.md`), design system (`design.md`), and changelog (`patchnotes.md`).

## Tech Stack

- HTML5, CSS3, vanilla JavaScript only
- No external dependencies, no build step, no package manager
- System font stack, no external font loading
- Designed for GitHub Pages static hosting

## Running Locally

No build step required. Either open `index.html` directly in a browser, or serve the folder locally:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deploying

The site is live at **https://azqato.github.io/leveraged-strategies/**

To deploy updates: push to the `main` branch. GitHub Pages is configured to deploy from the repo root. The site is fully static and requires no additional configuration.

## Design

The site follows the Azqato brand system: GitHub Dark-inspired palette, teal accent (`#00d4a0`), wiki-style sidebar layout, and system fonts. See `docs/design.md` for the full design specification.

## Disclaimer

Educational use only. Nothing on this site is financial advice. Leveraged ETFs carry significant risk including volatility decay and amplified drawdowns.
