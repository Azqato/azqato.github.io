# DESIGN.md — Azqato Stock Methodology Site

**Version:** 1.1  
**Status:** Active  
**Author:** Azqato

---

## 1. Design Direction

**Aesthetic:** GitHub Dark-inspired. Clean, information-dense, developer-credible. The site should feel at home next to other Azqato properties (portfolio, VIX Strategy, ComposerAtlas), using the same visual language, same color tokens, same interaction patterns.

**Tone:** Direct, educational, no hype. This is not a marketing page. It is a methodology document.

**Audience reading mode:** Slow and deliberate. People come here to learn, not browse. The design should respect reading: generous line height, clear hierarchy, anchor navigation that keeps users oriented in long content.

**Design lineage:** Follows the Azqato brand system established at `azqato.github.io`. The accent color (`#00d4a0`), surface colors, border tones, and interaction patterns are consistent with the portfolio site and ComposerAtlas.

---

## 2. Color System

All colors are defined as CSS custom properties in `:root`.

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-bg` | `#0d1117` | Page background |
| `--color-surface` | `#161b22` | Card and sidebar backgrounds |
| `--color-border` | `#30363d` | All borders and dividers |
| `--color-accent` | `#00d4a0` | Primary interactive color: links, active nav, hover borders, section bar |
| `--color-accent-hover` | `#00e6b0` | Hover state for accent elements |
| `--color-accent-light` | `rgba(0,212,160,0.08)` | Subtle tinted backgrounds (how-to-read boxes, accordion hover, FAQ teaser) |
| `--color-tag-bg` | `#21262d` | Tag pill and watchlist badge backgrounds |
| `--color-card-hover` | `#1c2128` | Card/table-header hover background |
| `--color-text-primary` | `#eef3f7` | Body copy, headings |
| `--color-text-secondary` | `#cbdae6` | Subtitles, captions, lead text, metric card definitions. Slightly cooler/softer than primary. |
| `--color-positive` | `#3fb950` | Positive values, good badges |
| `--color-negative` | `#f85149` | Negative values, red flag badges |
| `--color-warning` | `#ffa657` | Caution flags, caveat boxes, amber values |
| `--color-purple` | `#bc8cff` | Gradient accent on card hover (top border) |

**Rationale:** The `#00d4a0` teal-green is the Azqato brand signature across all projects. It replaces the previous `#1A6B4A` deep green used in v1.0.0. The dark background palette is drawn directly from the azqato.github.io DESIGN.md. Text on background passes ~15:1 contrast ratio; muted text on background is ~4.8:1, meeting WCAG AA.

---

## 3. Typography

**Font stack:** System fonts only. No external font loading.

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
```

**Monospace (data, tickers, numbers):**

```css
font-family: 'SF Mono', 'Consolas', 'Liberation Mono', 'Courier New', monospace;
```

| Role | Size | Weight | Color | Notes |
|------|------|--------|-------|-------|
| H1 (page title) | 1.875rem | 700 | `--color-text-primary` | Letter-spacing -0.3px |
| H2 (section title) | 1.375rem | 700 | `--color-text-primary` | Has `::before` vertical accent bar |
| H2 (metric block) | 1.5rem | 700 | `--color-text-primary` | Same accent bar; slightly larger |
| H3 (subsection) | 1.0625rem | 600 | `--color-text-primary` | |
| Body | 1rem | 400 | `--color-text-primary` | Line height 1.6 |
| Lead / intro | 1rem | 400 | `--color-text-secondary` | Line height 1.65 |
| Caption / note | 0.78rem | 400 | `--color-text-secondary` | |
| Metric value / num | 0.85rem | 400 | Contextual | Monospace stack |
| Ticker symbol | 0.875rem | 600 | `--color-accent` | Monospace stack |

**Note on v1.0.0 fonts:** The original design used IBM Plex Serif (headings), IBM Plex Sans (body), and IBM Plex Mono (data) from Google Fonts. This was replaced in v1.1.0 with the system font stack to align with the broader Azqato brand and eliminate the external font dependency.

---

## 4. Layout

### Grid

```
Desktop (>= 1024px): 2-column grid
[ Sidebar (220px) | Content (1fr) ]

Tablet / Mobile (< 1024px): Single column
Sidebar collapses to a sticky top nav bar
```

### Sidebar (Left Navigation)

Persistent on desktop. Contains:
- Site logo (`Azqato.` with teal dot accent)
- Page nav links: Home, Philosophy, Metrics, Screener, Watchlist, Indices, FAQ, Leveraged Strategies, Support
- On pages with multiple named sections: an "On This Page" anchor block below the Support link (see below)
- Small footer: "Educational use only. Not financial advice."

**Sidebar width:** 220px  
**Sidebar background:** `--color-surface` (`#161b22`)  
**Sidebar border:** 1px solid `--color-border` on the right  
**Active nav link:** `--color-accent` text, 3px left border in accent, weight 600  
**Inactive link color:** `--color-text-secondary`

### Content Area

**Max width:** 820px  
**Padding:** 32px top/bottom, 28px left/right on desktop; 20px on mobile

---

## 5. Component Specs

### Section Heading (h2)

All h2 elements include a `::before` pseudo-element: a 3px wide, 1.1em tall vertical bar in `--color-accent`, rendered inline via `display: flex; align-items: center; gap: 0.5rem`. This is the signature section delineation from the Azqato portfolio site.

---

### Tables

Used for: holdings snapshot, metric data comparisons.

```
- Header row: bg --color-card-hover (#1c2128), text uppercase 0.6875rem, color --color-text-secondary
- Body rows: alternating via rgba(255,255,255,0.02) on even rows
- Wrapper: border 1px solid --color-border, border-radius 8px, overflow: hidden
- Padding: 10px 14px per cell
- Number columns: right-aligned, monospace font
- Ticker column: --color-accent, bold, monospace
- Positive values: --color-positive (#3fb950)
- Negative values: --color-negative (#f85149)
- Caution values: --color-warning (#ffa657)
- Hover row: bg --color-accent-light (rgba teal tint)
```

### 52W Range Bar

Inline range visualization using a 4px track with an 8px dot positioned via `left: var(--pos)` CSS custom property set inline. Dot color `--color-accent`. Track color `--color-border`.

---

### Metric Cards (Index Page Grid)

10 cards in a 2-column grid on desktop, 1-column on mobile.

```
- bg: --color-surface
- border: 1px solid --color-border
- border-radius: 10px
- padding: 18px
- Hover: bg --color-card-hover, border rgba(0,212,160,0.5), translateY(-2px), box-shadow with teal tint
- Hover top border: 2px gradient (--color-accent to --color-purple) via ::before
- Card name: 0.9375rem, weight 700, --color-accent
- Card def: 0.85rem, --color-text-secondary
```

---

### Accordion (FAQ Page)

```
- Container: border 1px --color-border, border-radius 10px, overflow hidden
- Trigger: bg --color-surface, no border, font 0.9375rem weight 500
- Trigger hover: bg --color-accent-light
- Icon: "+" / "-" in --color-accent, right-aligned
- Body: max-height 0 → max-height 6000px, 200ms ease-in-out
- Content: padding 22px 20px, bg rgba(0,212,160,0.04), --color-text-secondary text
- Palantir story: border-left 3px solid --color-accent, --color-text-primary text
```

---

### Status Badges

Pill-shaped badges with 999px border-radius.

```
Good:     bg rgba(63,185,80,0.12),  text --color-positive, border rgba(63,185,80,0.3)
Caution:  bg rgba(255,166,87,0.12), text --color-warning,  border rgba(255,166,87,0.3)
Negative: bg rgba(248,81,73,0.12),  text --color-negative, border rgba(248,81,73,0.3)
Neutral:  bg --color-tag-bg,        text --color-text-secondary, border --color-border
```

---

### How-to-Read Box

```
bg: --color-accent-light (rgba teal)
border-left: 3px solid --color-accent
border-radius: 0 6px 6px 0
padding: 14px 18px
```

### Caveat Box

```
bg: rgba(255,166,87,0.08)
border-left: 3px solid --color-warning
border-radius: 0 6px 6px 0
text: --color-text-secondary, strong labels in --color-warning
```

---

### Hero Badge

```
Pill badge below hero headline and description (after .hero-sub)
margin-top: 16px (inline, separates badge from description above)
bg: --color-tag-bg
border: 1px solid --color-border
border-radius: 999px
text: --color-positive, 0.75rem
```

---

### Watchlist Ticker Tags

```
font-family: monospace
bg: --color-tag-bg
border: 1px solid --color-border
border-radius: 6px
text: --color-accent, weight 600
Hover: border rgba(0,212,160,0.5), bg --color-accent-light
```

---

### Favicon

All pages use an emoji SVG data URI favicon:

```html
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📈</text></svg>">
```

---

## 6. Signature Element

**The signature design element is the left sidebar "On This Page" anchor navigation, present on all content pages.**

As the user scrolls, the corresponding sidebar link highlights in `--color-accent` teal using a scroll-based `IntersectionObserver`. This gives every page "you are here" awareness without heavy UI. Borrowed from documentation sites like Stripe Docs or MDN, applied to a financial education context.

The "On This Page" block appears below the Support link (bottom of the main nav list) on every page that has named sections. The observer in `script.js` derives which sections to watch from the hrefs of `.metric-links a` elements, so no per-page configuration is needed.

The `h2::before` vertical accent bar is the secondary signature element; it appears on every section heading site-wide and visually ties the stocks site to the Azqato portfolio design language.

---

## 7. Navigation

### Sidebar Links

- **Inactive:** `--color-text-secondary`, weight 500
- **Hover:** `--color-text-primary`
- **Active / current page:** `--color-accent`, weight 600, 3px left border in accent
- **"On This Page" sub-links:** Smaller, indented, highlighted via IntersectionObserver on scroll. Appear below Support on any page with named sections.

### Tablet / Mobile (below 1024px)

Sidebar collapses to a sticky top bar with light blur backdrop (`backdrop-filter: blur(12px)`). Metric sub-links are hidden. Active state uses bottom border instead of left border.

---

## 8. Footer

```
Border-top: 1px solid --color-border
Background: --color-bg (#0d1117)
Text: --color-text-secondary, 0.8rem, center-aligned
Links: --color-accent
Padding: 28px 32px
```

---

## 9. Responsive Behavior

| Breakpoint | Changes |
|------------|---------|
| `< 1024px` | Sidebar becomes top nav bar, backdrop blur, metric sub-links hidden, bottom-border active state |
| `< 768px` | Cards become 1-column, h1 reduces to 1.5rem, h2 reduces to 1.2rem, padding reduces to 20px/16px |

---

## 10. Accessibility

- All color combinations meet WCAG AA contrast minimums (primary text ~15:1, muted text ~4.8:1)
- Accordion items use `aria-expanded` and `aria-controls` attributes
- Tables include `<caption class="visually-hidden">` and `<th scope>` attributes
- Focus styles preserved on all interactive elements (`focus-visible` outline in `--color-accent`)
- `prefers-reduced-motion` disables card transforms and accordion transitions

---

## 11. File Map

```
style.css structure (in order):
  :root (CSS variables)
  Reset / base
  Layout (site-wrapper flex, site-layout grid)
  Sidebar
  Main content
  Footer
  Typography (h1, h2 with ::before bar, h3, body, lead, caption)
  Tables (wrap, thead, tbody, ticker, value coloring, range bar)
  Hero (badge, thesis, sub)
  Section container
  Metric cards (index page grid)
  Metric blocks (metrics page full entries)
  Accordion (faq page)
  Badges (good/caution/negative/neutral)
  FAQ teaser
  Ticker tags (watchlist)
  Media queries (tablet < 1024px, mobile < 768px)
  Reduced motion
```

---

## 12. What Not To Do

- No light/white backgrounds (dark theme only, consistent with Azqato brand)
- No gradient backgrounds (the only gradient is the 2px top border on card hover)
- No external font loading (system fonts only)
- No stock chart widgets or live data embeds
- No animations beyond: card hover lift, accordion expand/collapse, sidebar link highlight
- No full-bleed hero images
- No em dashes in any copy
- No decorative animations or motion for motion's sake
- Do not deviate from the `#00d4a0` teal accent; it is the cross-site brand color
- No "- Azqato" brand suffix on `<title>` tags or `og:title` values. The `<title>` tag uses only the page H1 text. `og:title` is always identical to `<title>`.

---

## 13. Content Philosophy (v1.4.0+)

This site documents a methodology, not a live portfolio. All content should be written to remain accurate over time regardless of current market conditions.

**Rules:**
- No real-time data references. Do not use current prices, current RSI readings, or any value that will be stale within weeks.
- No company-specific examples for educational illustrations unless the example refers to a specific historical event. The Palantir story (buy at $9, sell at $45, outcome $150) is the one named exception; it is a first-person historical account, not a live recommendation.
- Metric examples must use clearly hypothetical labels ("High-growth tech co.", "Slow-growth value co.") or generic category descriptions ("enterprise software platforms", "cloud infrastructure").
- Moat type examples should describe categories of companies, not name specific companies (e.g., "enterprise software platforms" rather than a specific ticker).
- Historical references are acceptable when they clearly describe a past event: "a company that declined X% during a downturn and recovered" is fine; "Company X currently trades at Y" is not.

**Why:** The site is educational. Naming specific companies as live examples implies ongoing endorsement and creates stale content as market conditions change. Category descriptions teach the concept without anchoring to a specific stock's current situation.

---

## 14. Version History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | June 2026 | Initial design: light wiki theme, IBM Plex fonts, deep green `#1A6B4A` accent |
| 1.1 | June 2026 | Dark theme rebrand: aligned to Azqato brand system. New teal accent `#00d4a0`, system fonts, GitHub Dark-inspired palette, h2 accent bars, card hover effects, emoji favicon |
| 1.4 | June 2026 | Content philosophy formalized. No real-time data in examples. Hypothetical labels for all illustrative tables. Named company moat examples replaced with category descriptions. Content Philosophy section added (Section 13). |
| 1.5 | June 2026 | Two setup guide pages (watchlist.html, screener.html). Nav expanded to 6 items. Text readability: `.hero-sub`, `.lead`, `.guide-step-body` changed to `--color-text-primary`. New guide component CSS system (`.guide-step`, `.step-num`, `.ui-text`, `.guide-note`, etc.). P/E FWD section deepened with P/E vs EPS Growth comparison. |
| 1.6 | June 2026 | indices.html added. Nav restructured to 7 items (Home, Metrics, Screener, Watchlist, Indices, FAQ, Support). Sitewide readability: `.accordion-content`, `.metric-card-def`, `.guide-note` changed to `--color-text-primary`. Global `td` nowrap removed (wrapping enabled); preserved on `.num` and `.ticker-cell`. FAQ Q5 rewritten; Q7 (capital gains) added. Capital gains content added to homepage. |
| 1.7 | June 2026 | Text color refinement: `--color-text-primary` updated to `#eef3f7` (brighter white), `--color-text-secondary` differentiated to `#cbdae6` (soft blue-gray for subtitles/captions). |
| 1.8 | June 2026 | "On This Page" sidebar nav extended sitewide. Philosophy page gains 7 section anchor links. All content pages (index, screener, watchlist, indices) gain section IDs and "On This Page" blocks. Block position moved from nested under the active page nav link to a standalone `<li>` after the Support link. `IntersectionObserver` in `script.js` generalized to derive section targets from link hrefs, eliminating the hardcoded `.metric-block` selector. |
| 1.9 | June 2026 | Hero badge repositioned on `index.html`: moved from above the headline to below `.hero-sub`. `.hero` padding-bottom reduced from 36px to 16px for visual balance. |
| 3.0 | June 2026 | "Leveraged Strategies" nav link added sitewide above Support (external link to `azqato.github.io/leveraged-strategies/`). Nav is now 9 items. |
| 3.1 | June 2026 | Philosophy page expanded from 7 to 9 sections (new: "It Is Possible, and the Game Is Long" at top; "Hype, Sentiment, and the Weak-Hands Cascade" after Wall Street). Existing sections gained subsections (balance-sheet-as-personal-finance in Research; margins-as-competitive-position in Building Investment Knowledge; buy cadence and income focus in Stay on Offense). Content-only; no new components. |
| 3.2 | June 2026 | FAQ aligned with philosophy v3.1.0: one new accordion question ("Is getting wealthy in the stock market realistic, and how long does it take?"); three existing answers deepened (offense cadence/income, balance-sheet cousin analogy, gross-margin position-of-power framing); cross-link added from the hype question to `philosophy.html#section-hype`. Content-only. |
| 3.3 | June 2026 | Two new sections on `indices.html`: Dollar-Cost Averaging (`#section-dca`) and Lump-Sum Investing (`#section-lumpsum`), placed between Types of Index Funds and Fundamentals vs. Technicals; focus on VT and VTI + VXUS. New FAQ question (`answer-dca`). Reuses existing components (`.metric-grid`/`.metric-card`, `.how-to-read`, `.caveat-box`, `h3`); no new CSS. |
| 3.4 | June 2026 | Interactive Nasdaq 100 screener added as a new standalone page (introduced as `screenapp.html`) plus a daily data pipeline (`scripts/fetch-screener-data.mjs`, `.github/workflows/screener-data.yml`, `data/`). Dense full-width app layout distinct from the sidebar template, built on existing `style.css` tokens. |
| 3.5 | June 2026 | File renames: the Finviz guide `screener.html` → `finviz.html`; the watchlist guide `watchlist.html` → `seekingalpha.html`; the interactive screener `screenapp.html` → `screener.html`. All sitewide nav hrefs, cross-links, `og:url` metas, and references in the data pipeline and docs updated to match. Nav labels unchanged (the "Screener" nav item points to `finviz.html`; the interactive screener at `screener.html` remains out of nav by request). |
| 3.6 | June 2026 | Nav labels renamed: "Screener" → **Finviz**, "Watchlist" → **SeekingAlpha**. The interactive screener added to the sidebar nav as **Screener** (after Metrics) on all pages; nav is now 10 items. `screener.html` adopted the shared site sidebar in place of its custom top-bar nav — the app header trimmed to title + screen pill + "as of" + search, with a `max-width: 1023px` override so the app flows/scrolls normally when the sidebar collapses to a top bar. |
| 3.7 | June 2026 | Screener data pipeline moved from FMP (Node) to **yfinance** (Python) — no API key, full Nasdaq 100 coverage, all symbols refreshed daily. Nasdaq 100 constituent list fact-checked and corrected against stockanalysis.com / Wikipedia (added NVDA + 10 others; removed 10 delisted/dropped names). Not a visual-design change; pipeline/data only. |
| 3.8 | June 2026 | Screener gains a sortable **Cash/Debt** ratio column in the Balance Sheet group (after Total Cash/Debt), color-coded to the cash-vs-debt thresholds; zero-debt names show `∞` and sort to the top. |
| 3.9 | June 2026 | Forward metrics aligned to Seeking Alpha's current-fiscal-year ("0y") basis: P/E FWD = price ÷ current-FY EPS estimate (was yfinance `forwardPE` / next-year); Revenue & EPS Growth FWD use the 0y consensus growth. P/E FWD now matches SA. Pipeline/data only; no visual change. |
| 3.10 | June 2026 | Consolidated dual-class listings: removed GOOG (Class C), kept GOOGL (Class A voting). Multi-class rule documented (list only Class A voting shares). Screener now 100 tickers. |
| 3.11 | June 2026 | P/E FWD switched to Yahoo `priceEpsCurrentYear` (exact Seeking Alpha match); PEG FWD switched to Yahoo `pegRatio` (SA-style, long-term-growth based, ~±0.1). EPS Growth FWD kept GAAP-basis but labeled with a `*` tooltip; footer disclaimer corrected to credit Yahoo Finance. |
