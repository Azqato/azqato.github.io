# Product Requirements Document — Azqato Portfolio

## Problem Statement

Developers and recruiters who find Azqato's GitHub profile have no single place to see all projects together, understand what each one does, or find a live demo without digging through individual repositories. A personal portfolio solves this by presenting all projects in one scannable, filterable view alongside context about the builder.

---

## Target Users

### Visitor — Developer / Recruiter
Someone who arrived from a GitHub profile link, a LinkedIn message, or a referral. They want to quickly assess the scope and quality of projects, find a live demo to try, and locate the source code if something looks promising. They are comfortable with dark themes and developer aesthetics. They have a limited time budget (30–90 seconds before deciding whether to engage further).

### Visitor — Community Member / Fan
Someone from Twitch, YouTube, or the RuneScape B5TA community who knows Azqato personally and wants to explore the projects, learn more about the person behind the content, or support the work through Buy Me a Coffee or affiliate links. Less technically focused; navigates by project name and description rather than tags or language.

### Owner — Azqato (maintainer)
The sole developer of the portfolio. Needs to add new projects quickly without touching layout code, update affiliate links as they come in, and keep the site looking professional at all times. Values low-friction maintenance over automation.

---

## Goals

- Give visitors a fast, readable overview of all public projects in one place.
- Make it trivially easy to add new projects without touching layout HTML.
- Load instantly on any device or connection — no JavaScript frameworks, no CDN fonts.
- Reflect a developer-first aesthetic (dark theme, code-adjacent visual language).
- Provide a monetization path through Buy Me a Coffee and affiliate referral programs.
- Tell the full story behind the brand: community, gaming roots, content creation, and web development.

---

## Non-Goals

- CMS or database integration.
- GitHub API auto-sync (projects are added manually to maintain ordering and description quality).
- Analytics or user tracking of any kind.
- Multi-page routing or single-page application architecture.
- User accounts, login, or any server-side component.
- Automated affiliate link management or rate fetching.

---

## User Stories

| As a…          | I want to…                                          | So that…                                               |
|----------------|-----------------------------------------------------|--------------------------------------------------------|
| Visitor        | Browse all projects in a grid                       | I get a quick overview without reading a wall of text  |
| Visitor        | Filter projects by category tag                     | I can find projects relevant to my interests           |
| Visitor        | Click a card title to open the live demo            | I can try the project without cloning it               |
| Visitor        | Click the GitHub button on a card                   | I can dive into the source code directly               |
| Visitor        | Read about Azqato's background on the About page    | I understand the person behind the projects            |
| Visitor        | Use an affiliate link on the Support page           | I get a sign-up bonus at no extra cost to me           |
| Community member | Support Azqato via Buy Me a Coffee                | I can contribute to the creator directly               |
| Owner (Azqato) | Add a project by editing one JS object              | Maintenance is fast and low-friction                   |
| Owner          | Retheme the site by changing CSS variables          | Visual updates don't require touching layout HTML      |
| Owner          | Add new affiliate cards to the support page         | I can expand monetization as new partnerships form     |

---

## Feature List

### MVP (shipped in v1)

- **F1 — Project Cards:** icon, name, description, category tags, GitHub link, optional demo link, optional star count, optional last-updated date.
- **F2 — Tag Filtering:** auto-generated filter bar from `PROJECTS` array; real-time hide/show; project count updates.
- **F3 — Navigation:** sticky nav with Portfolio, About, GitHub, Support links; active state per page; collapses on mobile.
- **F4 — Hero Sections:** status badge, headline, bio blurb, and CTA buttons on each page.
- **F5 — Zero Dependencies:** plain HTML/CSS/JS; works offline after first load.
- **F6 — About Page:** bio with gaming origins, content creation, B5TA community, and web development; pitch card with avatar and signature.
- **F7 — Support Page:** Buy Me a Coffee CTA with disclaimer; affiliate partner grid with 5 live referral links (Tesla, Robinhood, M1 Finance, Public, Lyft); FTC-compliant affiliate disclosure.
- **F8 — Consistent Navigation:** identical nav and footer structure across all pages.
- **F9 — `iconUrl` field:** optional image/SVG URL per project card that overrides the emoji icon.

### Future (post-launch, not committed)

- Optional GitHub API integration to auto-populate star counts and update dates.
- Dark/light mode toggle.
- Animated section transitions on scroll.
- Contact / hire-me section with a form or email CTA.
- Project detail modal with extended README preview.
- Search bar for filtering by project name or description keyword.
- RSS or changelog feed for new project announcements.

---

## Constraints

- Must render correctly in the latest versions of Chrome, Firefox, Edge, and Safari.
- Must be usable at viewport widths from 320 px to 2560 px.
- Page weight (HTML + inline CSS + inline JS) must stay under 50 KB per page, uncompressed.
- No cookies, localStorage, sessionStorage, or external requests of any kind.
- No user data collected or transmitted.
- All affiliate disclosures must comply with FTC guidelines.

---

## Assumptions

- GitHub Pages will remain free for public repositories.
- Visitors have JavaScript enabled (filtering requires JS; static content degrades gracefully without it).
- Affiliate programs (Tesla, Robinhood, M1 Finance, Public, Lyft) will honor the referral links for their stated promotional periods.
- The owner will manually maintain the `PROJECTS` array; no automation is needed for v1.
- Buy Me a Coffee does not require integration code — a direct link is sufficient.

---

## Success Criteria

| Criterion                        | Target                                        |
|----------------------------------|-----------------------------------------------|
| Page load time                   | < 1 second on a 4G connection                 |
| Page weight per page             | < 50 KB uncompressed HTML                     |
| Cross-browser render             | No visual defects on Chrome, Firefox, Edge, Safari |
| Mobile usability                 | Fully usable at 375 px (iPhone SE viewport)   |
| Project addition time            | < 2 minutes to add a new project card         |
| Affiliate link accuracy          | All 5 affiliate links point to live, correct URLs |
| FTC compliance                   | Affiliate disclosure visible on support page without scrolling |
