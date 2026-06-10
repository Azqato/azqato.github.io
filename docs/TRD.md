# Technical Reference Document — Azqato Portfolio

## System Architecture

The portfolio is a fully static site with no server, no build step, and no runtime. It consists of nine plain HTML pages, each containing all of its own CSS and JavaScript inline. There is no bundler, no transpiler, and no dependency graph.

```
Browser → GitHub Pages (CDN) → index.html / about.html / support.html
                                links.html / youtube.html / invests.html
                                music.html / accounts.html / privacy-policy.html
```

Each page is self-contained. Navigation between pages is standard `<a href>` links — there is no client-side router. The browser performs a full page load on every navigation.

---

## Tech Stack

| Layer          | Technology            | Version / Notes                            |
|----------------|-----------------------|--------------------------------------------|
| Markup         | HTML5                 | Semantic elements: `<nav>`, `<main>`, `<section>`, `<footer>` |
| Styling        | CSS3                  | Custom properties, Grid, Flexbox, `@media` queries |
| Scripting      | JavaScript            | ES6+ (arrow functions, `const`/`let`, template literals, array methods) |
| Hosting        | GitHub Pages          | Free static hosting; deployed from `main` branch root |
| Version Control | Git / GitHub         | `main` branch; manual deploys on push |
| Editor Config  | VS Code               | `settings.json` in `.vscode/`              |

No npm packages. No CDN scripts. No external fonts. Zero runtime dependencies.

---

## Folder Structure

```
.
├── index.html           — Portfolio homepage: project grid, tag filter, hero
├── about.html           — About page: bio, pitch card, profile photo
├── support.html         — Support page: Buy Me a Coffee CTA, affiliate grid
├── links.html           — Links hub: all social/platform links by category
├── youtube.html         — YouTube channels: four channel cards with thumbnails
├── invests.html         — Invests hub: curated investment resource directory
├── music.html           — Music page: Spotify playlists + music platform links
├── accounts.html        — Gaming accounts: Steam, LoL, TFT, RuneScape profiles
├── privacy-policy.html  — Full privacy policy
├── img/                 — Image assets (profile photos, YT thumbnails, playlist covers)
├── README.md            — Developer setup and deployment guide
└── docs/
    ├── PRD.md           — Product requirements
    ├── TRD.md           — This file
    ├── DESIGN.md        — Design system and visual tokens
    ├── PATCHNOTES.md    — Versioned changelog
    ├── PRFAQ.md         — Press release and FAQ
    ├── TENETS.md        — Product principles
    ├── METRICS.md       — Success metrics
    ├── ROADMAP.md       — Milestones and planned features
    ├── SECURITY.md      — Security model
    └── RUNBOOK.md       — Operational runbook
```

---

## Data Models

### Project Entry (defined in `index.html` `PROJECTS` array)

```js
{
  name: string,       // required — display name on the card
  desc: string,       // required — one-sentence description
  github: string,     // required — full GitHub repo URL
  demo: string,       // optional — live site URL; card title links here if set
  tags: string[],     // required — category labels (Finance, Social, Tools)
  langClass: string,  // optional — CSS class for language tag color (e.g. "lang-js")
  icon: string,       // optional — emoji displayed in the card icon area
  iconUrl: string,    // optional — image/SVG URL; overrides icon when set
  stars: string,      // optional — star count displayed as a badge
  updated: string,    // optional — last-updated label (e.g. "Jun 2025")
}
```

**Current projects (v2.0.1):**

| Name                      | Tags                       | Language  | Has Demo |
|---------------------------|----------------------------|-----------|----------|
| Net Worth Tracker         | Finance, Tools             | JS        | Yes      |
| VIX Strategy              | Finance                    | JS        | Yes      |
| ComposerAtlas             | Finance, Tools, Education  | JS        | Yes      |
| Lantern                   | Social                     | JS        | Yes      |
| Cat Food Center           | Tools, Education           | JS        | Yes      |
| Clan B5TA                 | Social                     | HTML      | Yes      |
| Boaty McBoatface Ventures | Meme                       | HTML      | Yes      |
| Stock Methodology         | Finance, Education         | HTML      | Yes      |

### Affiliate Card (defined in `support.html` markup)

Each affiliate card is static HTML; there is no JavaScript data model. Structure:

```
<div class="affiliate-card">
  <div class="logo-area">         — brand color background + emoji/text logo
  <span class="promo-badge">      — short promo text (e.g. "Free $20")
  <p class="affiliate-desc">      — description of the offer
  <a class="affiliate-btn">       — CTA button linking to the referral URL
```

**Active affiliate cards:**

| Partner    | Promo                   | Referral URL                              |
|------------|-------------------------|-------------------------------------------|
| Tesla      | Free 3 Months FSD       | `ts.la/robert459550`                      |
| Robinhood  | Free $5–$200 Stock      | `join.robinhood.com/robertg273/`          |
| M1 Finance | Free $75 Bonus          | `m1.finance/BVZBG3OqOfMj`                |
| Public     | Free $20                | `share.public.com/azqato`                 |
| Lyft       | 50% Off First Ride      | `lyft.com/invite/ROBGOLDY630855`          |

---

## API Design

This project has no backend API. The only "API" is the internal data flow for the project grid filter:

### Internal Data Flow — Tag Filter (`index.html`)

```
PROJECTS array (static data)
  ↓ renderProjects(tag)
  ↓ filter: if tag === "All" → show all; else → card.tags.includes(tag)
  ↓ generate card HTML via template literal
  ↓ innerHTML assignment to #project-grid
  ↓ update #project-count text
```

### Filter Button Generation

```
PROJECTS array
  ↓ collect all unique tags via Set
  ↓ generate "All" button + one button per tag
  ↓ inject into #filter-bar
  ↓ attach click handler → calls renderProjects(tag)
```

### Active Nav State

```
window.location.pathname
  ↓ compare to each nav link's href
  ↓ add .active class to matching link
```

No fetch calls, no XHR, no WebSockets, no service workers.

---

## State Management

State is minimal and lives entirely in memory within each page load:

| State variable | Location              | Type    | Description                           |
|----------------|-----------------------|---------|---------------------------------------|
| `activeTag`    | `index.html` JS scope | string  | Currently selected filter tag ("All" by default) |

No persistent state. No localStorage, sessionStorage, IndexedDB, or cookies.

---

## Third-Party Integrations

| Service         | Purpose                                   | Auth                  | Data Sent              |
|-----------------|-------------------------------------------|-----------------------|------------------------|
| GitHub Pages    | Static hosting, CDN delivery              | GitHub account (owner)| None from visitors     |
| Buy Me a Coffee | Donation / support link                   | None (link only)      | User navigates to external site |
| Tesla           | Affiliate referral program                | None (link only)      | User navigates to ts.la |
| Robinhood       | Affiliate referral program                | None (link only)      | User navigates to robinhood.com |
| M1 Finance      | Affiliate referral program                | None (link only)      | User navigates to m1.finance |
| Public          | Affiliate referral program                | None (link only)      | User navigates to public.com |
| Lyft            | Affiliate referral program                | None (link only)      | User navigates to lyft.com |

All third-party interactions are outbound navigation — the portfolio itself does not call any external API or load any external resource.

---

## Performance Requirements

| Metric                        | Target                    | Current Status |
|-------------------------------|---------------------------|----------------|
| Page weight (uncompressed)    | < 50 KB per page          | index.html ~19 KB, about.html ~8 KB, support.html ~14 KB |
| Time to first meaningful paint | < 1 second on 4G         | Met (no blocking resources) |
| No external requests          | 0 external HTTP calls     | Met             |
| Offline functionality         | Fully usable after first load | Met (no CDN dependencies) |
| Browser support               | Chrome, Firefox, Edge, Safari latest | Met |
| Viewport range                | 320 px – 2560 px          | Met (CSS Grid responsive) |

---

## Known Technical Debt

| Item                                    | Current shortcut              | Correct solution                             |
|-----------------------------------------|-------------------------------|----------------------------------------------|
| Inline CSS repeated across pages        | Each page has its own full `<style>` block | Extract to a shared `styles.css` file |
| Inline JS repeated across pages         | Active nav detection JS duplicated in each page | Extract to a shared `nav.js` file |
| Hardcoded affiliate links in markup     | Links are static HTML strings | No change needed — deliberate for simplicity |
| No CSP headers                          | GitHub Pages does not support custom headers | Acceptable for a static content-only site |
| No automated tests                      | Manual visual QA only         | Could add Playwright or Cypress smoke tests |
| No build pipeline                       | Raw source files are deployed | Page count is now 9 — approaching the threshold where a shared nav include would justify a minimal build step |
