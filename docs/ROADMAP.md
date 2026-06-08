# Roadmap — Azqato Portfolio

---

## Current Phase

**Phase 1: Foundation Complete (v1.7.4)**

The core portfolio is live with project discovery, personal bio, and a monetization layer. All MVP features from the PRD are shipped: project grid with tag filtering, About page, Support page with Buy Me a Coffee and 5 active affiliate links, consistent navigation, and responsive design. The site is deployed on GitHub Pages at azqato.github.io.

---

## Milestone Table

| Milestone          | Name                           | Target Date       | Status      |
|--------------------|--------------------------------|-------------------|-------------|
| v1.0.0             | Initial launch                 | 2026-06-06        | Complete    |
| v1.1.0 – v1.2.2    | Projects + polish              | 2026-06-06        | Complete    |
| v1.3.0 – v1.3.2    | Support page                   | 2026-06-07        | Complete    |
| v1.4.0 – v1.4.1    | About page                     | 2026-06-07        | Complete    |
| v1.5.0 – v1.6.1    | New projects + iconUrl field   | 2026-06-07        | Complete    |
| v1.7.0 – v1.7.4    | Live affiliate links           | 2026-06-07        | Complete    |
| v1.8.0             | Documentation audit            | 2026-06-08        | Complete    |
| v2.0.0             | Code extraction + shared assets | TBD               | Planned     |
| v2.1.0             | GitHub API integration         | TBD               | Planned     |
| v2.2.0             | Dark/light mode toggle         | TBD               | Planned     |
| v3.0.0             | Contact / hire-me section      | TBD               | Planned     |

---

## Feature Breakdown Per Milestone

### v2.0.0 — Code Extraction + Shared Assets
- Extract shared CSS into a single `styles.css` file to eliminate duplication across pages.
- Extract shared nav JavaScript (active state detection) into a `nav.js` file.
- Extract shared nav HTML using a consistent pattern (either JS injection or a build step).
- Add `prefers-reduced-motion` media query to disable card hover transforms for users who prefer reduced motion.

### v2.1.0 — GitHub API Integration
- Auto-fetch star counts for each project via GitHub REST API on page load (with graceful fallback to hardcoded values).
- Auto-fetch last-pushed date per repository to keep "updated" fields current.
- Cache API responses in `sessionStorage` to avoid repeated calls within one visit.
- Add `X-RateLimit-Remaining` check and silent fallback if rate limit is hit.

### v2.2.0 — Dark/Light Mode Toggle
- Add a toggle button in the nav bar to switch between dark (current) and a light theme.
- Persist preference in `localStorage`.
- Respect `prefers-color-scheme` media query as the initial default.
- Define light-mode versions of all CSS custom properties.

### v3.0.0 — Contact / Hire-Me Section
- Add a new page or section with a contact CTA.
- Options under evaluation: email obfuscation link, Calendly embed, or GitHub Discussions link. No server-side form.
- Add "Hire Me" or "Contact" nav link.

---

## Explicitly Deferred Items

| Feature                           | Reason for deferral                                              |
|-----------------------------------|------------------------------------------------------------------|
| CMS or database integration       | No server-side runtime; adds infrastructure complexity that conflicts with the zero-dependency tenet |
| Automated affiliate link management | Affiliate programs change rarely; manual edits are sufficient at this scale |
| Analytics / user tracking         | Explicitly excluded from PRD; would conflict with the privacy-conscious aesthetic |
| Multi-page routing / SPA          | Three pages do not justify a router; full page loads are simpler and more reliable |
| Project detail modals / pages     | Current project descriptions are sufficient; deferred until there is a specific project that needs extended documentation |
| RSS / changelog feed              | No audience for it yet; revisit when monthly visitors exceed 2,000 |
| Automated testing (CI)            | Manual QA is sufficient at this scale; worth adding if the page count exceeds ~8 or if multiple contributors join |
