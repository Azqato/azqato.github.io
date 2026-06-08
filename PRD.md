# Product Requirements Document — Azqato Portfolio

## Overview

A personal portfolio website that serves as a centralized showcase for all of Azqato's GitHub projects. The site is intentionally simple: a single HTML file with no external dependencies, deployable anywhere static files are served.

---

## Goals

- Give visitors a fast, readable overview of all public projects.
- Make it trivially easy to add new projects without touching the layout.
- Load instantly on any device or connection — no JavaScript frameworks, no CDN fonts.
- Reflect a developer-first aesthetic (dark theme, code-adjacent visual language).

## Non-Goals

- CMS or database integration.
- GitHub API auto-sync (projects are added manually to keep control over ordering and descriptions).
- Analytics or tracking of any kind.
- Multi-page routing.

---

## User Stories

| As a…         | I want to…                                      | So that…                                          |
|---------------|-------------------------------------------------|---------------------------------------------------|
| Visitor       | Browse all projects in a grid                   | I get a quick overview without reading a wall of text |
| Visitor       | Filter projects by technology tag               | I can find projects relevant to my interests      |
| Visitor       | Click a card to go directly to the GitHub repo  | I can dive into the source immediately            |
| Visitor       | See a live-demo link when one exists            | I can try the project without cloning it          |
| Owner (Azqato)| Add a project by editing one JS object          | Maintenance is fast and low-friction              |
| Owner         | Retheme the site by changing CSS variables      | Visual updates don't require touching layout HTML |

---

## Functional Requirements

### F1 — Project Cards
- Each card displays: icon, name, description, technology tags, GitHub link, optional demo link, optional star count, optional last-updated date.
- Cards link to the project's GitHub URL in a new tab.
- Cards lift slightly on hover to signal interactivity.

### F2 — Tag Filtering
- A filter bar above the grid lists every unique tag from the `PROJECTS` array.
- Clicking a tag hides cards that don't include that tag.
- An "All" button resets the view.
- The project count label updates to reflect the current filter.

### F3 — Navigation
- A sticky top nav includes the site logo and a direct link to the GitHub profile.
- On mobile (< 600 px), nav links collapse to keep the bar clean.

### F4 — Hero Section
- A short headline, bio blurb, an "available" status badge, and two CTA buttons.
- No JavaScript required for this section.

### F5 — Zero Dependencies
- The site is plain HTML/CSS/JS files with no external scripts, stylesheets, or fonts loaded.
- Works offline after the initial load.

### F6 — About Page (`about.html`)
- Linked from the main nav as "About".
- Hero section with status badge, headline, and subtitle.
- Pitch card: avatar, name, role line, bio paragraphs, and signature.
- Active nav state highlights "About" when on `about.html`.

### F7 — Support Page (`support.html`)
- Linked from the main nav as "Support".
- Buy Me a Coffee CTA section: prominent branded button linking to `buymeacoffee.com/azqato`, left-aligned disclaimer with investment intent and fund-use caveat.
- Affiliate partners grid: square logo cards each showing a branded icon area, company name, promo badge, description, and CTA button.
  - Live links: Public (`share.public.com/azqato`), Robinhood (`join.robinhood.com/robertg273/`), M1 Finance (`m1.finance/BVZBG3OqOfMj`).
  - Placeholder links (real URLs pending): Tesla, Webull, Coinbase.
- Active nav state highlights "Support" when on `support.html`.

### F8 — Consistent Navigation
- All pages share an identical nav structure: Portfolio, About, GitHub, Support.
- The current page's nav link is highlighted via the `.active` class.
- Footer is consistent across all pages: "Built by Azqato" with a single GitHub profile link.

---

## Design Tokens

| Token           | Value     | Purpose                        |
|-----------------|-----------|--------------------------------|
| `--bg`          | `#0d1117` | Page background                |
| `--surface`     | `#161b22` | Card / nav surface             |
| `--border`      | `#30363d` | Borders and dividers           |
| `--accent`      | `#58a6ff` | Primary interactive colour     |
| `--green`       | `#3fb950` | Status badge / success         |
| `--purple`      | `#bc8cff` | Secondary accent               |
| `--text`        | `#e6edf3` | Body text                      |
| `--text-muted`  | `#8b949e` | Secondary / label text         |

---

## Constraints

- Must render correctly in the latest versions of Chrome, Firefox, Edge, and Safari.
- Must be usable at viewport widths from 320 px to 2560 px.
- Page weight (HTML + inline CSS + inline JS) must stay under 50 KB uncompressed.
- No cookies, localStorage, or external requests.

---

## Future Considerations (out of scope for v1)

- Optional GitHub API integration to auto-populate star counts.
- Dark/light mode toggle.
- Animated section transitions.
- Contact / hire-me section.
- Project detail pages or modal pop-ups with extended README previews.
