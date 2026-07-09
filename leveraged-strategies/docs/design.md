# DESIGN.md: Leveraged Strategies Site

**Version:** 1.3
**Status:** Active
**Author:** Azqato

---

## 1. Design Direction

**Aesthetic:** GitHub Dark-inspired wiki. Information-dense, developer-credible, calm. The site belongs to the Azqato family (portfolio, VIX Strategy, ComposerAtlas, Stock Methodology) and inherits the shared visual language: dark surfaces, teal accent, system fonts, restrained motion.

**Tone:** Direct and educational. This is a methodology reference, not a landing page. No hype, no marketing patterns, no urgency.

**Reading mode:** Long-form study. Strategy pages are documents people read top to bottom. The layout exists to keep readers oriented: persistent sidebar, in-page anchors, clear section hierarchy, generous line height.

**Design lineage:** Inherits the Azqato brand system from `azqato.github.io`. The `#00d4a0` teal accent, dark surface palette, and h2 accent bar are non-negotiable cross-site constants.

---

## 2. Color System

All colors defined as CSS custom properties in `:root` in `css/style.css`.

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg` | `#0d1117` | Page background |
| `--surface` | `#161b22` | Sidebar, cards, accordion triggers |
| `--border` | `#30363d` | Borders, dividers |
| `--accent` | `#00d4a0` | Links, active nav, h2 bar, hover borders, ticker text |
| `--accent-hover` | `#00e6b0` | Accent hover state |
| `--accent-light` | `rgba(0,212,160,0.08)` | Tinted backgrounds: callout boxes, row hover |
| `--card-hover` | `#1c2128` | Card and table header hover background |
| `--tag-bg` | `#21262d` | Pills, badges, ticker tags |
| `--text` | `#eef3f7` | Body copy, headings |
| `--text-muted` | `#cbdae6` | Captions, subtitles, supporting text |
| `--green` | `#3fb950` | Gains, favorable values |
| `--negative` | `#f85149` | Losses, drawdowns, risk flags |
| `--orange` | `#ffa657` | Caveats, caution callouts |
| `--purple` | `#bc8cff` | Card hover gradient partner color |

**Strategy color coding (new for this site):** Each strategy gets a subtle identity tint used only in its index card top border and its page hero badge. All other UI stays on the shared teal.

| Strategy | Tint token | Hex |
|----------|-----------|-----|
| 3 Sig | `--strat-3sig` | `#79c0ff` (light blue) |
| 6 Sig | `--strat-6sig` | `#e3b341` (amber) |
| 9 Sig | `--strat-9sig` | `#58a6ff` (blue) |
| TQQQ FTLT | `--strat-ftlt` | `#3fb950` (green, reuses positive) |
| Holy Grail | `--strat-grail` | `#bc8cff` (purple, reuses gradient partner) |
| HFEA | `--strat-hfea` | `#f0883e` (orange) |

The tints are decorative wayfinding only. They never replace `--accent` for interactive elements.

---

## 3. Typography

System fonts only. No external font loading.

```css
/* UI and body */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;

/* Data, tickers, numbers, allocation percentages */
font-family: 'SF Mono', 'Consolas', 'Liberation Mono', 'Courier New', monospace;
```

| Role | Size | Weight | Color | Notes |
|------|------|--------|-------|-------|
| H1 (page title) | 1.875rem | 700 | primary | Letter-spacing -0.3px |
| H2 (section) | 1.375rem | 700 | primary | Teal `::before` accent bar |
| H3 (subsection) | 1.0625rem | 600 | primary | |
| Body | 1rem | 400 | primary | Line height 1.6 |
| Lead / hero sub | 1.0625rem | 400 | primary | Line height 1.65 |
| Caption / note | 0.78rem | 400 | secondary | |
| Numbers / allocations | 0.85rem | 400 | contextual | Monospace |
| Ticker (TQQQ, QQQ, etc.) | 0.875rem | 600 | accent | Monospace |

---

## 4. Layout

### Grid

```
Desktop (>= 1024px): 2-column grid
[ Sidebar (220px) | Content (max 820px) ]

Below 1024px: single column
Sidebar collapses to sticky top bar with backdrop blur
```

### Sidebar

Persistent on desktop. Contents, top to bottom:

- Logo: `Azqato.` with teal dot
- Site label: "Leveraged Strategies"
- Page links: Home, then one link per strategy (derived from `/strategies/*.md`), then Support (external link to `https://azqato.github.io/support.html`)
- "On This Page" anchor links when on a strategy page (Overview, Rules and Logic, Performance Notes, Risks, Resources), highlighted on scroll via IntersectionObserver
- Footer line: "Educational use only. Not financial advice."

**Nav convention:** Every `.md` file added to `/strategies` implies a new page, a new nav entry in every page, and a new strategy card on the index. Support is always the last nav item and links externally.

Specs: 220px wide, `--surface` background, 1px right border. Active page link gets accent text, weight 600, and a 3px left accent border.

### Content Area

Max width 820px. Padding 32px vertical, 28px horizontal on desktop; 20px on mobile.

---

## 5. Components

### Section Heading (h2)

Every h2 carries a `::before` vertical bar: 3px wide, 1.1em tall, `--accent`, laid out with flex and 0.5rem gap. This is the cross-site Azqato signature and appears on all pages.

### Strategy Cards (Index Page)

Three cards in a 3-column grid on desktop (1-column below 768px).

```
bg: --surface
border: 1px solid --border
border-radius: 10px
padding: 20px
Top border on hover: 2px solid in the strategy's tint color via ::before
Hover: bg --card-hover, translateY(-2px), subtle teal-tinted shadow
Card title: 1.0625rem, weight 700, --accent
Card summary: 0.9rem, --text-muted
Card footer: "Read the strategy" link arrow in --accent
```

### Placeholder Blocks (Initial Build)

Until real content lands, each strategy section renders a placeholder block:

```
border: 1px dashed --border
border-radius: 8px
padding: 24px
text: --text-muted, italic, centered
content: "Content coming soon. Source: /strategies/<name>.md"
```

Dashed border distinguishes placeholders from finished content at a glance.

### Allocation Tables

For rebalancing rules and allocation targets once content lands.

```
Wrapper: 1px solid --border, radius 8px, overflow hidden
Header row: bg --card-hover, uppercase 0.6875rem, secondary text
Even rows: rgba(255,255,255,0.02)
Cell padding: 10px 14px
Numeric columns: right-aligned, monospace
Percentages and dollar figures: monospace, contextual color
Row hover: --accent-light
```

### Callout Boxes

Two variants, both left-bordered, radius 0 6px 6px 0, padding 14px 18px.

```
Info box:   bg --accent-light,        border-left 3px --accent
Risk box:   bg rgba(255,166,87,0.08),       border-left 3px --orange
```

Risk boxes are mandatory on every strategy page (leveraged ETF risk disclosure).

### Badges

Pill badges, 999px radius, used for strategy metadata (rebalance cadence, risk level).

```
Neutral:  bg --tag-bg, secondary text, --border border
Caution:  bg rgba(255,166,87,0.12), warning text and border tint
Negative: bg rgba(248,81,73,0.12), negative text and border tint
Positive: bg rgba(63,185,80,0.12), positive text and border tint
```

### Hero Badge (Strategy Pages)

Small pill above the h1 showing the strategy tint color as a dot plus a label such as "Quarterly Rebalancing" or "Buy and Hold". `--tag-bg` background, 1px border, 0.75rem text.

### Ticker Tags

Inline monospace pills for tickers (TQQQ, QQQ, AGG, etc.): `--tag-bg` background, 1px border, accent text weight 600, 6px radius. Hover tints border and background teal.

### Favicon

Emoji SVG data URI, consistent with the Azqato pattern:

```html
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚀</text></svg>">
```

---

## 6. Signature Element

**Primary:** The scroll-aware "On This Page" sidebar on strategy pages. As the reader moves through Overview, Rules, Performance, Risks, and Resources, the matching sidebar link lights up in teal via IntersectionObserver. Borrowed from documentation sites, it keeps long reads oriented without heavy UI.

**Secondary:** Strategy tint coding. The blue/green/purple top borders on index cards and hero badges give each strategy a quiet identity while everything interactive stays on brand teal.

---

## 7. Navigation

- Inactive links: `--text-muted`, weight 500
- Hover: `--text`
- Active page: `--accent`, weight 600, 3px left border
- Anchor sub-links: smaller, indented, scroll-highlighted
- Below 1024px: sticky top bar, `backdrop-filter: blur(12px)`, anchor sub-links hidden, active state moves to bottom border

---

## 8. Footer

1px top border, `--bg` background, centered `--text-muted` text at 0.8rem, accent links, 28px 32px padding. Content: "Built by [Azqato](https://azqato.github.io)." Matches the footer pattern used across all Azqato properties.

---

## 9. Responsive Behavior

| Breakpoint | Changes |
|------------|---------|
| `< 1024px` | Sidebar becomes blurred sticky top bar, anchor links hidden |
| `< 768px` | Strategy cards stack to 1 column, h1 1.5rem, h2 1.2rem, reduced padding, tables scroll horizontally in a wrapper |

---

## 10. Accessibility

- All text/background pairs meet WCAG AA (primary ~15:1, secondary ~4.8:1 on `--bg`)
- Strategy tints are never the only differentiator; cards and badges always carry text labels
- `focus-visible` outline in `--accent` on all interactive elements
- Tables use `<th scope>` and visually hidden captions
- `prefers-reduced-motion` disables card lifts and scroll-highlight transitions
- Skip-to-content link as the first focusable element on every page

---

## 11. File Map

```
css/style.css order:
  :root variables
  Reset / base
  Layout grid (sidebar + content)
  Sidebar and top-bar nav
  Typography (h1, h2 accent bar, h3, body, lead, captions)
  Hero (badge, title, sub)
  Strategy cards (index)
  Placeholder blocks
  Tables
  Callout boxes (info, risk)
  Badges and ticker tags
  Footer
  Media queries (1024px, 768px)
  Reduced motion

js/main.js:
  IntersectionObserver for anchor highlighting
  Mobile nav toggle (if needed)
  Nothing else. JS is enhancement only.
```

---

## 12. What Not To Do

- No light backgrounds. Dark theme only
- No external fonts, CDNs, libraries, or frameworks
- No live data, charts, widgets, or price embeds
- No gradients except the card hover top border treatment
- No motion beyond card hover lift and nav highlight transitions
- No full-bleed hero imagery
- No em dashes in any copy
- Never use a strategy tint color for interactive elements; teal `#00d4a0` is the only interactive accent
- No marketing language, countdowns, or calls to action

---

## 13. Content Philosophy

Carried over from the Azqato stock methodology site and applied here:

- No real-time data. Nothing that goes stale within weeks (current prices, current allocations as of a date)
- Historical references must clearly read as past events
- Performance discussion describes behavior and character (drawdown depth, recovery patterns), not predictions
- Every strategy page carries a risk callout covering leveraged ETF mechanics: daily reset, volatility decay, amplified drawdowns
- Attribution: credit original strategy authors and sources in the Resources section

---

## 14. Version History

| Version | Date | Summary |
|---------|------|---------|
| 1.3 | 2026-07-08 | Cross-project rebrand pass after this site was folded into the azqato.github.io monorepo. CSS custom property names renamed to match the shared root token names (e.g. `--color-bg` to `--bg`, `--color-text-primary` to `--text`, `--color-positive` to `--green`, `--color-strat-3sig` to `--strat-3sig`); all hex values unchanged, so this is a naming-only alignment, not a visual redesign. Pre-existing em dashes throughout the site's docs and copy also removed in a one-time cleanup. |
| 1.2 | June 2026 | Added HFEA orange tint token (`#f0883e`). Design doc count aligned with six strategies and seven pages |
| 1.1 | June 2026 | Added 3 Sig (light blue) and 6 Sig (amber) tint tokens. Documented /strategies nav convention. Footer updated to "Built by Azqato." pattern. Support link added as permanent last nav item |
| 1.0 | June 2026 | Initial design. Azqato dark brand system applied to a wiki layout. Strategy tint coding, placeholder block component, and strategy page template defined |
