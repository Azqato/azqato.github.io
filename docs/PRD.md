# Product Requirements Document: Azqato Portfolio

---

## Problem Statement

Developers and recruiters who find Azqato's GitHub profile have no single place to see all projects together, understand what each one does, or find a live demo without digging through individual repositories. Community members from Twitch, YouTube, and Discord have no hub that introduces Azqato, points them to the right community server, and surfaces relevant content in one scan. A personal portfolio solves both problems by presenting all projects in a filterable view, routing visitors to the right community, and providing context about the creator.

---

## Target Users

### Visitor: Developer / Recruiter

Someone who arrived from a GitHub profile link, a LinkedIn message, or a referral. They want to quickly assess scope and quality of projects, find a live demo to try, and locate source code if something looks promising. They are comfortable with dark themes and developer aesthetics. They have a limited time budget (30 to 90 seconds before deciding whether to engage further).

### Visitor: Community Member / Fan

Someone from Twitch, YouTube, or the RuneScape B5TA community who knows Azqato personally. They want to explore projects, join the right Discord server, learn more about the person behind the content, or support the work through Buy Me a Coffee or affiliate links. Less technically focused; navigates by name and description rather than tags or language classes.

### Owner: Azqato (maintainer)

The sole developer of the portfolio. Needs to add new projects quickly without touching layout code, update affiliate links and Discord invites as they change, and keep the site looking professional at all times. Values low-friction maintenance over automation.

---

## Goals

- Welcome first-time visitors with an introductory landing page that explains who Azqato is and routes them to the community Discord and the rest of the site.
- Give visitors a fast, readable overview of all public projects in one place.
- Provide a dedicated Discord page that surfaces all four community servers with permanent invite links.
- Make it trivially easy to add new projects without touching layout HTML.
- Load instantly on any device or connection with no JavaScript frameworks and no CDN fonts.
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

## Site Structure

The site opens with an introductory landing page (`index.html`) that welcomes first-time visitors, introduces Azqato across gaming, content creation, investing, music, and community, and routes them onward. Its primary call to action is joining the community Discord via `discord.html`; a secondary "Explore the site" grid links to every other page. The project grid lives at `projects.html`.

| Page           | File                  | Purpose                                               |
|----------------|-----------------------|-------------------------------------------------------|
| Landing        | `index.html`          | Introductory front door: Discord CTA + explore grid   |
| Projects       | `projects.html`       | Filterable grid of open-source projects               |
| About          | `about.html`          | Bio and personal pitch                                |
| Discord        | `discord.html`        | Four Discord server cards with permanent invite links  |
| Links          | `links.html`          | All platforms and channels in one place               |
| YouTube        | `youtube.html`        | Four YouTube channels                                 |
| Invests        | `invests.html`        | Investing projects showcase + curated resource hub    |
| Music          | `music.html`          | Spotify playlists and mixes                           |
| Accounts       | `accounts.html`       | Gaming profiles                                       |
| Support        | `support.html`        | Buy Me a Coffee CTA + affiliate partners              |
| Privacy Policy | `privacy-policy.html` | Full privacy policy                                   |

---

## User Stories

| As a...              | I want to...                                           | So that...                                                  |
|----------------------|--------------------------------------------------------|-------------------------------------------------------------|
| First-time visitor   | Land on an introductory page explaining who Azqato is  | I understand the brand before diving into specifics         |
| First-time visitor   | Browse all Discord servers and pick the right one      | I join the community that matches my interests              |
| Visitor              | Browse all projects in a grid                          | I get a quick overview without reading a wall of text       |
| Visitor              | Filter projects by category tag                        | I find projects relevant to my interests                    |
| Visitor              | Click a card title to open the live demo               | I can try the project without cloning it                    |
| Visitor              | Click the GitHub button on a card                      | I can read the source code directly                         |
| Visitor              | Read about Azqato's background on the About page       | I understand the person behind the projects                 |
| Visitor              | Use an affiliate link on the Support page              | I get a sign-up bonus at no extra cost to me                |
| Community member     | Support Azqato via Buy Me a Coffee                     | I can contribute to the creator directly                    |
| Owner (Azqato)       | Add a project by editing one JS object                 | Maintenance is fast and low-friction                        |
| Owner                | Add a Discord server by copying one card block         | Maintenance stays simple as servers are added               |
| Owner                | Retheme the site by changing CSS variables             | Visual updates don't require touching layout HTML           |

---

## Feature List

### MVP (shipped)

- **F1: Project Cards.** Icon, name, description, category tags, GitHub link, optional demo link, optional star count, optional last-updated date. Defined in the `PROJECTS` array in `projects.html`.
- **F2: Tag Filtering.** Auto-generated filter bar from `PROJECTS` array; real-time hide/show via `data-hidden` attribute; project count updates on filter change.
- **F3: Navigation.** Sticky nav across all pages: Home, About, Discord, Invests, Codes, Links, Projects, YouTube, Support. Active state via `class="active"` in HTML. Below 860px, the link list collapses behind a hamburger toggle button (`.nav-toggle`) that opens a dropdown panel; inline JS per page handles open/close, closing on link click or outside click. Every nav item links to a page on this site (relative path); no external links belong in the top-level nav (see DESIGN.md's Navigation Bar section). External destinations like the GitHub org or sibling project sites are linked from within a page's own content instead (a card, a footer credit, a button), not from the persistent nav.
- **F4: Hero Sections.** Headline and description on each page, styled consistently. Landing page hero includes profile photo, category pills, and CTA buttons.
- **F5: Zero Dependencies.** Plain HTML/CSS/JS; works offline after first load; no external fonts, no CDN scripts.
- **F6: About Page.** Bio with gaming origins, content creation, B5TA community, and web development. Pitch card with profile photo and signature.
- **F7: Support Page.** Buy Me a Coffee CTA with FTC-compliant disclaimer. Affiliate partner grid with five live referral links (Tesla, Robinhood, M1 Finance, Public, Lyft).
- **F8: Discord Page.** Four server cards (Azqato, Azqato Invests, B5TA, League of Azqato) with permanent invite links, server descriptions, emoji icons, and Discord-blue Join Server buttons.
- **F9: `iconUrl` field.** Optional image or SVG URL per project card that overrides the emoji icon when set.
- **F10: Introductory Landing Page.** `index.html` is the default entry point for first-time visitors. Introduces Azqato with an easygoing bio, routes visitors to the Discord and to every other page via a grid of destination cards.
- **F11: Favicon.** Site-wide favicon is a 🦁 emoji, implemented as an inline SVG data-URI `<link rel="icon">` (no external image file) and repeated identically in the `<head>` of all 12 pages. The homepage's "About" explore-card icon (`index.html`) matches the favicon.

### Future (post-launch, not committed)

- Optional GitHub API integration to auto-populate star counts and update dates.
- Dark / light mode toggle with `localStorage` persistence and `prefers-color-scheme` default.
- Animated section transitions on scroll.
- Contact or hire-me section with email link or GitHub Discussions CTA.
- Project detail modal with extended README preview.
- Search bar filtering by project name or description keyword.
- Shared `styles.css` and `nav.js` to eliminate duplication across pages.
- `@media (prefers-reduced-motion: reduce)` rule to disable card hover transforms.

---

## Constraints

- Must render correctly in the latest versions of Chrome, Firefox, Edge, and Safari.
- Must be usable at viewport widths from 320 px to 2560 px.
- Page weight (HTML + inline CSS + inline JS) must stay under 50 KB per page, uncompressed.
- No cookies, localStorage, sessionStorage, or external requests of any kind on the main site pages.
- No user data collected or transmitted.
- All affiliate disclosures must comply with FTC guidelines.

---

## Assumptions

- GitHub Pages will remain free for public repositories.
- Visitors have JavaScript enabled (filtering requires JS; static content degrades gracefully without it).
- Affiliate programs (Tesla, Robinhood, M1 Finance, Public, Lyft) will honor the referral links for their stated promotional periods.
- The owner will manually maintain the `PROJECTS` array and `discord.html` server cards; no automation is needed.
- Buy Me a Coffee does not require integration code; a direct link is sufficient.
- Discord invite links on `discord.html` are permanent and will not expire.

---

## Writing Style

All copy across the site and documentation must be easy to read and free of em dashes and double dashes. These punctuation marks interrupt reading flow and often obscure meaning. Use the following alternatives:

| Situation | Preferred punctuation | Example |
|---|---|---|
| Continuing a thought naturally | Comma | "Fast, clean, and honest about what it is." |
| Introducing a list or explanation after a complete clause | Colon | "Each strategy gets a dedicated page covering: rules, risks, and sources." |
| Connecting two closely related independent clauses | Semicolon | "Buy Me a Coffee does not require integration code; a direct link is sufficient." |
| Adding supplementary or aside information | Parentheses | "The portfolio is open source (MIT licensed) and hosted on GitHub." |
| Separating two ideas that are better as their own sentences | Period | "Fully client-side. All data stays in your browser's localStorage." |

Em dashes appear in two forms in HTML: as the literal Unicode character (`—`) and as the HTML entity (`&mdash;`). Both are prohibited. Audits must search for both forms independently.

This policy is enforced automatically by a `pre-commit` hook in `.githooks/` that blocks any commit introducing either form into an HTML or documentation file. In Markdown, occurrences inside backtick code spans are exempt so the rule can document the character itself. Enable the hook once per clone with `git config core.hooksPath .githooks`; bypass in an emergency with `git commit --no-verify`.

---

## Success Criteria

| Criterion                       | Target                                               |
|---------------------------------|------------------------------------------------------|
| Page load time                  | Under 1 second on a 4G connection                    |
| Page weight per page            | Under 50 KB uncompressed HTML                        |
| Cross-browser render            | No visual defects on Chrome, Firefox, Edge, Safari   |
| Mobile usability                | Fully usable at 375 px (iPhone SE viewport)          |
| Project addition time           | Under 2 minutes to add a new project card            |
| Affiliate link accuracy         | All 5 affiliate links point to live, correct URLs    |
| FTC compliance                  | Affiliate disclosure visible on support page without scrolling |

---

---

# Architecture and Technical Reference

*Consolidated from the former TRD.md.*

---

## System Architecture

The portfolio is a fully static site with no server, no build step, and no runtime. It consists of eleven plain HTML pages, each containing all of its own CSS and JavaScript inline. There is no bundler, no transpiler, and no dependency graph. The introductory landing page (`index.html`) is the default entry point.

```
Browser → GitHub Pages (CDN) → index.html
                                projects.html / about.html / discord.html
                                support.html / links.html / youtube.html
                                invests.html / music.html / accounts.html
                                privacy-policy.html
```

Navigation between pages is standard `<a href>` links; there is no client-side router. The browser performs a full page load on every navigation.

---

## Tech Stack

| Layer           | Technology      | Version / Notes                                                   |
|-----------------|-----------------|-------------------------------------------------------------------|
| Markup          | HTML5           | Semantic elements: `<nav>`, `<section>`, `<footer>`               |
| Styling         | CSS3            | Custom properties, Grid, Flexbox, `@media` queries               |
| Scripting       | JavaScript      | ES6+ (arrow functions, `const`/`let`, template literals, Set)    |
| Hosting         | GitHub Pages    | Free static hosting; deployed from `main` branch root            |
| Version Control | Git / GitHub    | `main` branch; deploys on push                                   |

No npm packages. No CDN scripts. No external fonts. Zero runtime dependencies.

---

## Data Models

### Project Entry (defined in `projects.html` `PROJECTS` array)

```js
{
  name: string,       // required, display name on the card
  desc: string,       // required, short description
  github: string,     // required, full GitHub repo URL or live site URL
  demo: string,       // optional, live site URL; card title links here if set
  tags: string[],     // required, category labels (Finance, Social, Tools, Education, etc.)
  langClass: string,  // optional, CSS class for language tag color (e.g. "lang-js")
  icon: string,       // optional, emoji displayed in the card icon area
  iconUrl: string,    // optional, image/SVG URL; overrides icon when set
  stars: string,      // optional, star count label
  updated: string,    // optional, last-updated label (e.g. "2026")
}
```

Current projects: Net Worth Tracker, VIX Strategy, ComposerAtlas, Stock Methodology, Leveraged Strategies, Lantern, Cat Food Center, Clan B5TA, Boaty McBoatface Ventures, No Fee Apartments, LV Guest List, Prompts, ProteinPulse, Azqato's Tools.

Active filter tag categories: Finance, Health, Social, Tools, Education, Meme, Real Estate.

### Discord Server Entry (defined in `discord.html` static HTML)

Each server is a static `.server-card` block. There is no JavaScript data model. Structure:

```html
<div class="server-card">
  <div class="card-top">
    <span class="card-icon">[emoji]</span>
    <span class="card-name">[Server Name]</span>
  </div>
  <p class="card-desc">[description]</p>
  <a class="btn-join" href="[permanent invite URL]" target="_blank" rel="noopener">
    [Discord SVG] Join Server
  </a>
</div>
```

Current servers: Azqato (`discord.gg/sKGKC3JFSE`), Azqato Invests (`discord.gg/WeCNCJ4x7S`), B5TA (`discord.gg/E2TA9xp`), League of Azqato (`discord.gg/yHtHYgR`).

### Affiliate Card (defined in `support.html` static HTML)

Each affiliate card is static HTML. Structure:

```html
<div class="affiliate-card">
  <div class="logo-area">         <!-- brand color background + emoji/text logo -->
  <span class="promo-badge">      <!-- short promo text, e.g. "Free $20" -->
  <p class="affiliate-desc">      <!-- description of the offer -->
  <a class="affiliate-btn">       <!-- CTA button linking to the referral URL -->
```

Active affiliate cards: Tesla (`ts.la/robert459550`), Robinhood (`join.robinhood.com/robertg273/`), M1 Finance (`m1.finance/BVZBG3OqOfMj`), Public (`share.public.com/azqato`), Lyft (`lyft.com/invite/ROBGOLDY630855`), Twitch Prime (`twitch.tv/azqato`).

---

## Internal Data Flow

### Tag Filter (`projects.html`)

```
PROJECTS array (static data)
  → buildCard(project) generates card HTML via template literal
  → buildFilters() collects unique tags via Set, generates filter buttons
  → bindFilters() attaches click handlers
  → click: set data-hidden="false" or "true" on each .project-card
  → update #project-count text
```

No fetch calls, no XHR, no WebSockets, no service workers.

### Active Nav State

The active nav link has `class="active"` set directly in the HTML on each page. There is no JavaScript-based routing or active-state detection.

---

## State Management

State is minimal and lives entirely in memory within each page load:

| State variable | Location                 | Type   | Description                                   |
|----------------|--------------------------|--------|-----------------------------------------------|
| `activeTag`    | `projects.html` JS scope | string | Currently selected filter tag (default: "All") |

No persistent state. No localStorage, sessionStorage, IndexedDB, or cookies anywhere on the site.

---

## Third-Party Integrations

| Service         | Purpose                                   | Data Sent from Portfolio |
|-----------------|-------------------------------------------|--------------------------|
| GitHub Pages    | Static hosting, CDN delivery              | None                     |
| Buy Me a Coffee | Donation link                             | User navigates externally |
| Tesla           | Affiliate referral                        | User navigates externally |
| Robinhood       | Affiliate referral                        | User navigates externally |
| M1 Finance      | Affiliate referral                        | User navigates externally |
| Public          | Affiliate referral                        | User navigates externally |
| Lyft            | Affiliate referral                        | User navigates externally |
| Discord         | Community servers (via discord.html links) | User navigates externally |

All external interactions are outbound navigation. The portfolio does not call any external API or load any external resource on page load.

---

## Performance Targets

| Metric                         | Target                         |
|--------------------------------|--------------------------------|
| Page weight (uncompressed)     | Under 50 KB per page           |
| Time to first meaningful paint | Under 1 second on 4G           |
| External requests on page load | 0                              |
| Offline functionality          | Fully usable after first load  |
| Browser support                | Chrome, Firefox, Edge, Safari latest |
| Viewport range                 | 320 px to 2560 px              |

---

## Known Technical Debt

| Item                               | Current shortcut                                    | Correct solution                                   |
|------------------------------------|-----------------------------------------------------|----------------------------------------------------|
| Inline CSS repeated across pages   | Each page has its own full `<style>` block          | Extract to a shared `styles.css`                   |
| Nav HTML repeated across pages     | Nav duplicated in all 11 HTML files                 | Extract to shared `nav.js` injection or build step |
| Active nav state in HTML           | `class="active"` hardcoded per page                 | Detect via `window.location.pathname` in `nav.js`  |
| No `prefers-reduced-motion` query  | Hover transforms fire for all users                 | Add `@media (prefers-reduced-motion: reduce)` rule |
| No CSP headers                     | GitHub Pages does not support custom response headers | Acceptable for static content-only; revisit if hosting changes |
| No automated tests                 | Manual visual QA only                               | Playwright or Cypress smoke tests; threshold met at 11 pages |

---

---

# Product Tenets

*Consolidated from the former TENETS.md.*

These are the guiding principles for every decision made on this project. When two options conflict, the tenet higher on this list takes priority.

---

## 1. Speed Is a Feature; Everything Else Is Optional

A page that loads in under a second with five project cards is more valuable than a page that loads in three seconds with ten. Every addition (a library, a font, a third-party widget) must pay for itself in load time. If it cannot, it does not ship.

Applies when: debating whether to add a dependency, a new CDN resource, or a feature that requires external data.

---

## 2. No Dependencies by Default

The default answer to "should we use a library for this?" is no. Vanilla HTML, CSS, and JavaScript handle everything this portfolio needs. Dependencies rot, have security vulnerabilities, and create maintenance burden. The burden of proof is on adding a dependency, not on avoiding one.

Conflict note: this tenet will conflict with Tenet 5 (low maintenance). When a library would genuinely reduce ongoing manual work, prefer the no-dependency solution unless the maintenance cost is severe and sustained.

---

## 3. The Owner Must Be Able to Maintain This in Five Minutes

Adding a project, updating an affiliate link, updating a Discord server card, or changing the theme should never require reading documentation. If the codebase reaches the point where the owner has to look something up to make a routine edit, it has grown too complex. Simplicity for the maintainer is a hard constraint, not a preference.

---

## 4. Transparency Before Conversion

The affiliate and support features exist to fund the work, but they must never obscure what the portfolio is. The affiliate disclosure appears above the fold. Links are clearly labeled. Nothing is disguised as editorial content.

Applies to: every decision on the Support page (disclosure placement, button copy, card descriptions).

---

## 5. Look Like a Developer Built It

The portfolio must look at home on GitHub. Dark backgrounds, monospaced typography influences, accent colors that signal "interactive", and no stock photo hero images. The aesthetic communicates technical competence before the visitor reads a word.

Applies when: making visual design decisions. Loses to Tenet 1 and Tenet 2 if achieving a visual goal requires a framework or a blocking resource.

---

---

# Press Release and FAQ

*Consolidated from the former PRFAQ.md.*

---

## Internal FAQ

**Q: Why build a custom portfolio instead of using GitHub profile, LinkedIn, or a page builder?**
The goal is a developer-first aesthetic and zero maintenance overhead. Existing platforms do not allow precise visual control, and page builders add bloat. A hand-coded site is the fastest and most credible signal to other developers.

**Q: Why inline CSS and JS instead of separate files?**
With a small number of pages at launch, separate files added deployment complexity with no benefit, and each page being self-contained made it easier to read and modify. The site has since grown to eleven pages, so CSS repetition across pages is now the leading item of known technical debt; extracting a shared stylesheet and nav include is planned (see Roadmap).

**Q: Why no analytics?**
The PRD explicitly excludes analytics and tracking. The portfolio represents a developer who cares about privacy, and tracking visitors would contradict that. GitHub Pages provides basic traffic data (clones, referrers) in the repository Insights tab as a lightweight alternative.

**Q: What happens if an affiliate program changes or cancels a referral link?**
Links are hardcoded in `support.html`. If a link breaks or a program ends, it requires a manual edit and a new commit. This is the correct trade-off for a project with no backend.

**Q: How does the portfolio monetize without feeling like an ad?**
The Support page is a separate, clearly labeled section. Visitors arrive there by clicking "Support" in the nav; it is opt-in. The affiliate disclosure is visible above the fold and written in plain language.

**Q: What assumption must be true for the affiliate channel to succeed?**
Visitors from Twitch, YouTube, and the B5TA community (who already have an affinity for Azqato) are more likely to convert on affiliate links than cold developer traffic. If the site is only discovered by developers evaluating code, the affiliate channel will underperform.

**Q: Why is there no contact form or hire-me section?**
GitHub profile and linked repositories already provide contact paths. A contact form would require a backend or third-party form service, which conflicts with the zero-dependency constraint. Deferred to a future version.

**Q: What is the plan if GitHub Pages goes down or becomes paid?**
The entire site is plain HTML files and can be deployed to Vercel, Netlify, or Cloudflare Pages in under five minutes with no configuration changes. There is no lock-in.

**Q: How will new projects be added after launch?**
Edit the `PROJECTS` array in `projects.html`, add the project object, commit, and push. GitHub Pages deploys within ~60 seconds. Estimated time per new project: 2 to 5 minutes.

**Q: How will new Discord servers be added?**
Copy an existing `.server-card` block in `discord.html`, update the icon, name, description, and `href` on the `.btn-join` link, commit, and push. Estimated time: under 5 minutes.

---

## External FAQ

**Q: What is this site?**
It is Azqato's personal hub. It opens with a short introduction to who Azqato is, then points you to projects, the community Discord servers, content channels, investing resources, and ways to support the work.

**Q: I just landed here. Where do I start?**
The landing page links to every part of the site. The best first stop is the Discord page, where you can join the community that fits your interests.

**Q: How do I find a specific project?**
Open the Projects page and use the filter buttons above the grid to narrow by category. Click a card title or the ↗ button to open the live version.

**Q: What are the affiliate links on the Support page?**
They are referral links for services Azqato personally uses or recommends. If you sign up through one, you get a signup bonus, and Azqato earns a referral commission. No extra cost to you.

**Q: What data does the site collect about me?**
None. No analytics, no cookies, no tracking pixels, no forms. GitHub Pages may log standard server-level access data (IP address, user agent) as part of its infrastructure.

**Q: Where do Buy Me a Coffee funds go?**
Azqato intends to invest the funds in the stock market for long-term growth. Circumstances may vary; there is no guaranteed use of funds.

**Q: Can I view the source code for this portfolio?**
Yes. The portfolio is open source and hosted on GitHub at github.com/Azqato.

---

---

# Security Model

*Consolidated from the former SECURITY.md.*

---

## Authentication and Authorization

There is no authentication. The portfolio is a fully public, read-only static site. No user accounts, no login, no sessions, no cookies.

The only privileged access is the GitHub repository, protected by Azqato's GitHub account credentials (username, password, and 2FA). Repository access controls who can push changes and trigger deployments.

All visitors have identical read-only access to all pages via `azqato.github.io`.

---

## Data Storage

The portfolio stores no user data. No databases, no server-side storage, no cookies, no localStorage, no sessionStorage, no IndexedDB.

Static content hardcoded in HTML files (project metadata, affiliate URLs, bio copy) is public by design and contains no personal information about visitors. GitHub Pages may log standard web server access data; this is outside the portfolio's control and governed by GitHub's privacy policy.

---

## Environment Variables and Secrets

There are no environment variables, no `.env` files, no API keys, no tokens, and no credentials anywhere in this codebase. Affiliate link URLs are public referral URLs hardcoded as HTML `href` attributes; they are not secrets.

---

## Third-Party Trust

The portfolio makes zero outbound HTTP requests on page load. No external resources are fetched, no CDN scripts are loaded, and no analytics pixels fire. When a visitor clicks a link, they navigate to a third-party site governed by that site's privacy policy.

---

## Known Attack Surface

**Cross-Site Scripting (XSS).** The `PROJECTS` array is hardcoded and rendered via `innerHTML` template literals. Only the repository owner can modify it, so the attack surface is limited to the repository itself. If GitHub API integration is ever added, all API-sourced strings must be escaped with `textContent` or a sanitizer before DOM insertion.

**Affiliate Link Integrity.** Affiliate URLs are hardcoded and not validated at runtime. All changes go through the owner's GitHub account (protected by 2FA). Review all changes to `support.html` and `discord.html` before merging.

**Content Security Policy.** GitHub Pages does not support custom HTTP response headers, so a CSP cannot be applied at the header level. Acceptable for a static, no-user-input site. If the project migrates to Vercel, Cloudflare Pages, or Netlify, adding a CSP would be a worthwhile improvement.

**Dependency Vulnerabilities.** Zero. No npm packages, no CDN scripts, no external stylesheets.

---

## Dependency Policy

Current state: zero dependencies. If a dependency is ever added: prefer well-maintained packages with a clear security disclosure process; pin to an exact version; run `npm audit` before committing; do not use CDN-hosted scripts without Subresource Integrity hashes; review any package that handles user data or DOM manipulation.

---

---

# Operational Runbook

*Consolidated from the former RUNBOOK.md.*

---

## Local Setup

### Prerequisites

- Git
- A modern browser (Chrome, Firefox, Edge, or Safari)
- A text editor (VS Code recommended)

### Steps

```bash
git clone https://github.com/Azqato/Azqato.git
cd Azqato
```

Open `index.html` in a browser:

```bash
# Option A: double-click index.html in File Explorer / Finder
# Option B: drag into a browser window
# Option C: local server (avoids file:// quirks on some browsers)
npx serve .            # http://localhost:3000
python -m http.server  # http://localhost:8000
```

No `npm install`. No build step. No configuration.

---

## Build

No build step. Source files are the deployed files.

To check file sizes before pushing (PowerShell):

```powershell
Get-ChildItem *.html | Select-Object Name, Length
```

Target: each HTML file under 50,000 bytes uncompressed. Images in `img/` have no strict size target; keep them web-optimized (under 500 KB each).

---

## Deploy

### GitHub Pages (production)

Initial setup (one-time):

1. Push the repository to GitHub.
2. Settings → Pages → Source: Deploy from a branch → `main` / `root`.
3. Save. Live at `https://azqato.github.io/` within ~60 seconds.

Routine deploy:

```bash
git add <changed files>
git commit -m "Description of change"
git push origin main
```

Verify: visit https://azqato.github.io/ and hard-refresh (Ctrl+Shift+R / Cmd+Shift+R). Check Settings → Pages or the Actions tab if the site does not update within 2 minutes.

### Alternative Hosts

| Host             | Steps                                                        |
|------------------|--------------------------------------------------------------|
| Vercel           | Drag and drop project folder at vercel.com/new; no build command |
| Netlify          | Drag and drop at app.netlify.com/drop                        |
| Cloudflare Pages | Connect repo; leave build command blank                      |

---

## Rollback

**Option A: Revert the last commit (safe, preferred)**

```bash
git revert HEAD
git push origin main
```

Creates a new commit that undoes the last change. GitHub Pages deploys the revert within ~60 seconds.

**Option B: Reset to a specific commit (destructive)**

```bash
git log --oneline          # find the target commit hash
git reset --hard <hash>
git push --force-with-lease origin main
```

Use only if reverting many commits at once.

**Option C: Restore a single file from a previous commit**

```bash
git checkout <hash> -- discord.html
git commit -m "Restore discord.html to <hash>"
git push origin main
```

---

## Environments

There is only one environment: production (GitHub Pages).

| Environment | URL                         | Branch | Deploy trigger    |
|-------------|-----------------------------|--------|-------------------|
| Production  | https://azqato.github.io/   | `main` | Push to `main`    |
| Local       | `file://` or localhost:3000 | N/A    | Open in browser   |

No `.env` files. No environment variables. No feature flags.

---

## Common Errors

| Symptom                           | Likely Cause                                      | Fix                                                                  |
|-----------------------------------|---------------------------------------------------|----------------------------------------------------------------------|
| Site shows old version after push | GitHub Pages CDN cache                            | Hard-refresh. Wait 2 to 5 minutes for full propagation.              |
| 404 on azqato.github.io           | GitHub Pages not enabled or wrong branch          | Settings → Pages → source: `main` / `root`                          |
| Affiliate card shows wrong promo  | Outdated hardcoded text in `support.html`         | Edit the `promo-badge` span in the relevant card                     |
| Discord Join button does nothing  | `href="#"` placeholder not replaced with real invite | Update the `href` on the `.btn-join` anchor in `discord.html`     |
| Filter bar shows unexpected tags  | New project added with unintended tag value       | Check `tags` array in the new project object in `projects.html`      |
| Project count is wrong            | JS filter logic or syntax error                   | Check DevTools Console for errors; verify `PROJECTS` array syntax    |
| `iconUrl` image not loading       | URL unreachable or cross-origin blocked           | Check DevTools → Network; use an absolute URL to a stable host       |
| Page weight over 50 KB            | Too much inline content added                     | Check file size with DevTools → Network → HTML file size             |

---

## Monitoring

All monitoring is manual.

| What to check           | Where                                                         | Cadence              |
|-------------------------|---------------------------------------------------------------|----------------------|
| Site availability       | Visit https://azqato.github.io/                               | Spot-check as needed |
| GitHub Pages status     | githubstatus.com                                              | If site appears down |
| Deploy status           | GitHub → repo → Settings → Pages                              | After each push      |
| Affiliate link validity | Click each link on `support.html`                             | Monthly              |
| Discord invite validity | Click each invite on `discord.html`                           | Monthly              |
| Traffic / visitors      | GitHub → repo → Insights → Traffic                            | Monthly              |
| Page weight             | DevTools → Network → check HTML file size                     | After major changes  |
| Lighthouse score        | Chrome DevTools → Lighthouse                                  | Quarterly            |

---

---

# Metrics

*Consolidated from the former METRICS.md.*

---

## North Star Metric

**Monthly unique visitors to the portfolio** (`azqato.github.io/`). This is the single number that best represents whether the portfolio is delivering value.

---

## Acquisition Metrics

| Metric                         | Measurement Method                              |
|--------------------------------|-------------------------------------------------|
| GitHub profile referral clicks | GitHub Insights → Traffic → Referrers           |
| Social / community referrals   | GitHub Insights → Traffic → Referrers           |
| Repository clone count         | GitHub Insights → Traffic → Clones              |

The portfolio has no analytics script. All acquisition data comes from GitHub Pages traffic insights.

---

## Engagement Metrics

| Metric                        | Measurement Method                           |
|-------------------------------|----------------------------------------------|
| Support page visit rate       | GitHub Insights → Traffic (per-page views)   |
| Discord page visit rate       | GitHub Insights → Traffic (per-page views)   |
| Affiliate link conversions    | Per-affiliate partner dashboard              |
| Buy Me a Coffee contributions | Buy Me a Coffee dashboard                    |

---

## Performance Metrics

| Metric                      | Target                | Measurement                              |
|-----------------------------|-----------------------|------------------------------------------|
| Page weight (any page)      | Under 50 KB           | DevTools → Network tab                   |
| First Contentful Paint      | Under 1.0 second      | Chrome Lighthouse or PageSpeed           |
| External HTTP requests      | 0 on page load        | DevTools → Network tab                   |
| GitHub Pages uptime         | Over 99.9%            | githubstatus.com / manual checks         |

---

## Targets

| Metric                        | Target                      | Timeframe             |
|-------------------------------|-----------------------------|-----------------------|
| Monthly unique visitors       | 500+                        | 3 months post-launch  |
| Monthly unique visitors       | 2,000+                      | 12 months post-launch |
| Support page visit rate       | Over 10% of portfolio visits | Ongoing              |
| Buy Me a Coffee contributions | At least 1 per month        | 3 months post-launch  |
| Affiliate conversion          | At least 1 per month        | 6 months post-launch  |

---

## Reporting Cadence

| Category             | Frequency  | Notes                                                         |
|----------------------|------------|---------------------------------------------------------------|
| Traffic              | Monthly    | GitHub Insights retains 14 days of daily data; review monthly |
| Affiliate performance | Monthly   | Log into each partner dashboard; note any conversions         |
| Buy Me a Coffee      | Monthly    | Dashboard shows all-time and monthly totals                   |
| Lighthouse           | Quarterly  | Run manually or after major changes                           |
| Page weight          | Every push | Check DevTools after any HTML change; flag if over 45 KB      |

---

---

# Roadmap

*Consolidated from the former ROADMAP.md.*

---

## Completed Milestones

| Milestone         | Name                                      | Date         |
|-------------------|-------------------------------------------|--------------|
| v1.0.0            | Initial launch                            | 2026-06-06   |
| v1.1.0 – v1.2.2   | Projects + polish                         | 2026-06-06   |
| v1.3.0 – v1.3.2   | Support page                              | 2026-06-07   |
| v1.4.0 – v1.4.1   | About page                                | 2026-06-07   |
| v1.5.0 – v1.6.1   | New projects + iconUrl field              | 2026-06-07   |
| v1.7.0 – v1.7.4   | Live affiliate links                      | 2026-06-07   |
| v1.8.0            | Documentation audit (10-file set)         | 2026-06-08   |
| v1.9.0 – v1.9.3   | New projects + filter tags                | 2026-06-08   |
| v2.0.0            | Old-site merger (6 new pages)             | 2026-06-09   |
| v2.1.0 – v2.2.x   | New projects (Stock Methodology, Leveraged Strategies) | 2026-06-10 |
| v2.3.0 – v2.3.2   | Introductory landing page, nav Home/Discord, two new projects | 2026-06-13 |
| v2.4.0 – v2.4.1   | discord.html: four server cards, sitewide nav update | 2026-06-13 |
| v2.5.0            | Documentation consolidation (4-file audit) | 2026-06-13 |
| v2.6.0            | Prompts project card                        | 2026-06-14 |
| v2.6.1 – v2.6.5   | Project card fixes and additions            | 2026-06-27 |

---

## Planned Milestones

| Milestone  | Name                              | Status   |
|------------|-----------------------------------|----------|
| Docs sync  | Document unpushed changes (see below) | TODO |
| v2.7.0     | Code extraction + shared assets   | Planned  |
| v2.8.0     | GitHub API integration            | Planned  |
| v2.9.0     | Dark / light mode toggle          | Planned  |
| v3.0.0     | Contact / hire-me section         | Planned  |

### Docs Sync: Document Recently Pushed Changes (TODO)

PATCHNOTES.md and DESIGN.md are behind the live site. The following shipped changes (commits up to `38007c1`) still need changelog entries and, where noted, DESIGN.md updates:

- `invests.html` restructured to the discord.html layout pattern: hero badge removed, `.section-head` replaced by discord-style `.section-header` (accent-bar `.section-title` + `.section-desc` + bottom-border separator), sections retitled "Projects" and "Curated Resources". Update DESIGN.md (the "Featured Project Card", "Section Heading", and "Hero CTA Buttons" entries are now stale).
- `invests.html` hero "Join the Discord" button restyled to match the homepage `.btn-discord` (blue `--discord`, Discord SVG logo); `--discord`/`--discord-hover` tokens added to the page.
- `index.html` both "Join the Discord" buttons repointed from the external `discord.gg` invite to the internal `discord.html` (dropped `target="_blank"`).
- `about.html` hero badge "Investor, Developer, Community Builder" removed.
- `discord.html` hero heading changed from "Join Azqato's Discord" to "Azqato's Discord".
- `codes.html` reformatted to the invests/discord layout (badge and hero CTA buttons removed, Title/Description/separator section header).
- `youtube.html` reformatted the same way (badge removed, "Channels" Title/Description/separator header added).
- `links.html` hero badge "Find me everywhere" removed; hero description changed to "Find me everywhere."
- Merged duplicate `html {}` rules in `codes.html` while restructuring.

Also apply the em-dash guard and pick the next version number(s) when writing these up. Note the stale `.hero-badge`/`@keyframes pulse` CSS left unused in `about.html` and `links.html` (candidate cleanup).

### v2.7.0: Code Extraction + Shared Assets

- Extract shared CSS into a single `styles.css` to eliminate duplication across 11 pages.
- Extract shared nav HTML using JS injection or a minimal build step.
- Extract active-state detection into `nav.js` (using `window.location.pathname`).
- Add `@media (prefers-reduced-motion: reduce)` rule to disable card hover transforms.

### v2.8.0: GitHub API Integration

- Auto-fetch star counts for each project via GitHub REST API on page load.
- Auto-fetch last-pushed date per repository.
- Cache responses in `sessionStorage` to avoid repeated calls within one visit.
- Silent fallback to hardcoded values if rate limit is hit.

### v2.9.0: Dark / Light Mode Toggle

- Toggle button in nav bar.
- Persist preference in `localStorage`.
- Respect `prefers-color-scheme` as initial default.
- Define light-mode CSS custom property overrides.

### v3.0.0: Contact / Hire-Me Section

- New page or section with a contact CTA.
- Options: email obfuscation link, Calendly embed, or GitHub Discussions link. No server-side form.

---

## Explicitly Deferred Items

| Feature                           | Reason for deferral                                                    |
|-----------------------------------|------------------------------------------------------------------------|
| CMS or database integration       | No server-side runtime; conflicts with zero-dependency tenet           |
| Automated affiliate link management | Affiliate programs change rarely; manual edits sufficient at this scale |
| Analytics / user tracking         | Explicitly excluded from PRD; conflicts with privacy-conscious aesthetic |
| Multi-page routing / SPA          | Full page loads are simpler and more reliable for a static site        |
| Project detail modals             | Current descriptions are sufficient; revisit when a project needs extended docs |
| RSS / changelog feed              | No audience yet; revisit when monthly visitors exceed 2,000            |
| Automated testing (CI)            | Manual QA currently in use; threshold for smoke tests met at 11 pages, candidate for v2.7.0 |

---

---

# Documentation Process

This section describes the documentation structure adopted in v2.5.0 and how it should be maintained going forward.

---

## File Structure

```
/project-root
├── README.md          - developer setup and reference; always root-level only
└── /docs
    ├── PRD.md         - all product, architecture, and operational documentation
    ├── DESIGN.md      - design system, tokens, component patterns
    └── PATCHNOTES.md  - versioned changelog
```

No additional documentation files should be created inside `/docs`. All new reference content belongs in one of these three files under the appropriate section.

---

## What Goes Where

**README.md** is for developers who just cloned the repo. It covers: what the project is, how to run it, how to add a project or Discord server, file overview, and a link to `/docs`. Do not include product rationale, design decisions, or marketing language. Keep it concise and command-focused.

**docs/PRD.md** is the source of truth for everything else: product requirements, architecture, tenets, FAQ, security model, operational runbook, metrics, roadmap, and this documentation process. When a doc from the old set would be added (e.g., a security note, a new runbook step, a roadmap update), add it to the relevant section of PRD.md.

**docs/DESIGN.md** covers only visual and UX decisions: color tokens, typography, spacing, breakpoints, component patterns, accessibility, and motion. When a new component is added to the site, add its pattern here. When a CSS value changes in the source, update the matching entry in DESIGN.md.

**docs/PATCHNOTES.md** is a running log of every change made. One entry per version, dated, with Added / Changed / Fixed / Removed sections. Write in past tense. Every meaningful commit should have a corresponding entry.

---

## Maintenance Rules

1. When adding a new page: add a row to the Site Structure table in PRD.md, a new file entry in the README File Overview, and a PATCHNOTES entry.
2. When adding a new component: document its CSS pattern in DESIGN.md under Component Patterns.
3. When a CSS value changes: update DESIGN.md to match. DESIGN.md must stay in sync with the source.
4. When changing the nav: update the nav description in README.md (link targets, page count).
5. When a roadmap milestone completes: move it from Planned to Completed in the Roadmap section of PRD.md and add a PATCHNOTES entry.
6. When a third-party integration changes (affiliate link, Discord invite, Buy Me a Coffee URL): update the relevant data model table in PRD.md and the source HTML, then add a PATCHNOTES entry.
7. Never create new `.md` files in `/docs`. All new documentation content goes into one of the three existing files.
8. All site and documentation copy must follow the Writing Style section (no em dashes, no double dashes). The `.githooks/pre-commit` guard enforces the em-dash rule at commit time; keep it enabled with `git config core.hooksPath .githooks`.
