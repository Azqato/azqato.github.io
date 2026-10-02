# Product Requirements Document: Azqato Portfolio

This is the single source of truth for the Azqato site: what it is, who it serves, how it is built, how to run and deploy it, what conventions it follows, and what is known to be wrong with it. It is written so that a new contributor or an AI model can understand the entire project from `/docs` alone, without reading the code.

Sections marked **Discrepancy** record a place where the documentation and the code disagreed at audit time. Both readings are kept. The code is treated as the truth about what the site does; the documentation is treated as the truth about what was intended. Neither is deleted in favor of the other, because either one can be the thing that is wrong.

---

## Problem Statement

Developers and recruiters who find Azqato's GitHub profile have no single place to see all projects together, understand what each one does, or find a live demo without digging through individual repositories. Community members from Twitch, YouTube, and the RuneScape B5TA community have no hub that introduces Azqato, points them to the right community server, and surfaces relevant content in one scan. A personal portfolio solves both problems by presenting all projects in a filterable view, routing visitors to the right community, and providing context about the creator.

A third problem emerged after launch and now shapes the site as much as the first two: Azqato's output is spread across at least six platforms (Twitch, four YouTube channels, Mixcloud, Last.fm, Discord, GitHub, and several standalone GitHub Pages sites). Without a hub, each platform is a dead end. The site exists to be the one address that resolves to all of them.

---

## Target Users

### Visitor: Developer / Recruiter

Someone who arrived from a GitHub profile link, a LinkedIn message, or a referral. They want to quickly assess scope and quality of projects, find a live demo to try, and locate source code if something looks promising. They are comfortable with dark themes and developer aesthetics. They have a limited time budget (30 to 90 seconds before deciding whether to engage further).

What they need: the Projects page, fast, with working demo links and visible tags.

### Visitor: Community Member / Fan

Someone from Twitch, YouTube, or the RuneScape B5TA community who knows Azqato personally. They want to explore projects, join the right Discord server, learn more about the person behind the content, or support the work through Buy Me a Coffee or affiliate links. Less technically focused; navigates by name and description rather than tags or language classes.

What they need: the landing page, the Discord page, and the Links page. This is the group most likely to convert on the Support page.

### Visitor: Investor / Finance-Curious

Someone who arrived from an investing video, the Azqato Invests Discord, or a link to one of the finance tools. They want the free tools and the curated resource hub, and they are the reason the Invests page carries a prominent "not a licensed financial advisor" disclaimer above its resource grid.

What they need: the Invests page and the finance projects it links out to.

### Owner: Azqato (maintainer)

The sole developer of the portfolio. Needs to add new projects quickly without touching layout code, update affiliate links and Discord invites as they change, and keep the site looking professional at all times. Values low-friction maintenance over automation. Works on Windows, deploys by pushing to `main`, and reviews the result in a browser rather than in tests.

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
- Give the music and DJ side of the brand a page that feels like a stage rather than a list of links.

---

## Non-Goals

- CMS or database integration.
- GitHub API auto-sync (projects are added manually to maintain ordering and description quality).
- Analytics or user tracking of any kind.
- Multi-page routing or single-page application architecture.
- User accounts, login, or any server-side component.
- Automated affiliate link management or rate fetching.
- A light theme or a theme toggle. The site is dark by design.
- Making the `music.html` visualizer react to audio playing in another tab, in a third-party iframe, or on the system output. This was researched and declined; see Risks and Open Questions.

---

## Site Structure

The site opens with an introductory landing page (`index.html`) that welcomes first-time visitors, introduces Azqato across gaming, content creation, investing, music, and community, and routes them onward. Its primary call to action is joining the community Discord via `discord.html`; a secondary "Explore the site" grid links to every other page. The project grid lives at `projects.html`.

There are **12** HTML pages.

| Page           | File                  | In top nav | Purpose                                                        |
|----------------|-----------------------|------------|----------------------------------------------------------------|
| Landing        | `index.html`          | Yes (Home) | Introductory front door: Discord CTA plus explore grid          |
| About          | `about.html`          | Yes        | Bio and personal pitch card                                     |
| Discord        | `discord.html`        | Yes        | Four Discord server cards with permanent invite links           |
| Invests        | `invests/` (Azqato Invests) | Yes   | Since v2.11.0 a 21-page site in its own folder; `invests.html` is a redirect page to it |
| Codes          | `codes.html`          | Yes        | Three cards: Prompts, Tools, and the GitHub org                 |
| Music          | `music.html`          | Yes        | Full-screen stage visualizer, two Mixcloud embeds, three platform links |
| Links          | `links.html`          | Yes        | All platforms and channels grouped into six categories          |
| Projects       | `projects.html`       | Yes        | Filterable grid of 15 projects, generated from a JS array       |
| YouTube        | `youtube.html`        | Yes        | Four YouTube channel cards with thumbnails                      |
| Support        | `support.html`        | Yes        | Buy Me a Coffee CTA plus seven affiliate partner cards          |
| Gaming Accounts| `accounts.html`       | No         | Steam, League of Legends, Teamfight Tactics, RuneScape profiles |
| Privacy Policy | `privacy-policy.html` | No         | Full privacy policy, affiliate disclosure, financial disclaimer |

`accounts.html` and `privacy-policy.html` carry the same nav as every other page but are not listed in it. They are reached from the `index.html` explore grid and from the "More" group on `links.html`.

> **Discrepancy (resolved in favor of the code).** Before this audit, the Site Structure table listed 11 pages and omitted `codes.html` entirely, and the README's file overview did the same. `codes.html` has existed since the v2.3.x era, is in the top nav of all 12 pages, and was documented nowhere. The table above is read from the filesystem.

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
| Visitor              | Play a DJ mix without leaving the page                 | I can listen while I look around the rest of the site       |
| Visitor              | Pick a different visualizer mode on the Music page     | The page looks the way I want while a mix plays             |
| Visitor              | Find every platform Azqato is on in one list           | I follow him where I already spend time                     |
| Investor             | Open a curated screener or ETF list                    | I skip the search and start from something vetted           |
| Visitor              | Use an affiliate link on the Support page              | I get a sign-up bonus at no extra cost to me                |
| Community member     | Support Azqato via Buy Me a Coffee                     | I can contribute to the creator directly                    |
| Owner (Azqato)       | Add a project by editing one JS object                 | Maintenance is fast and low-friction                        |
| Owner                | Add a Discord server by copying one card block         | Maintenance stays simple as servers are added               |
| Owner                | Add an affiliate partner by copying one card block     | A new referral program goes live in one commit              |
| Owner                | Retheme the site by changing CSS variables             | Visual updates do not require touching layout HTML          |

---

## Feature List

### MVP (shipped and live)

- **F1: Project Cards.** Icon, name, description, category tags, GitHub link, optional demo link, optional star count, optional last-updated date. Defined in the `PROJECTS` array in `projects.html`. Currently 15 entries.
- **F2: Tag Filtering.** Auto-generated filter bar built from the union of all `tags` values; real-time hide and show via a `data-hidden` attribute; the project count updates on every filter change.
- **F3: Navigation.** Sticky nav across all 12 pages: **Home, About, Discord, Invests, Codes, Music, Links, Projects, YouTube, Support**. Active state via `class="active"` in the HTML, written by `tools/build-nav.py` from each page's own filename rather than maintained by hand. Below 860 px the link list collapses behind a hamburger toggle (`.nav-toggle`) that opens a dropdown panel; an inline script on each page handles open and close, closing on link click or on an outside click. Every nav item links to a page on this site with a relative path; no external links belong in the top-level nav (see the Navigation Bar section of DESIGN.md). External destinations such as the GitHub org are linked from within a page's own content instead.
- **F4: Hero Sections.** Headline and description on each page, styled consistently. The landing page hero adds a row of interest pills and two CTA buttons.
- **F5: Near-Zero Dependencies.** Plain HTML, CSS, and JavaScript. No npm packages, no framework, no CDN scripts, no web fonts. Eleven of the twelve pages make zero outbound requests.
- **F6: About Page.** Bio covering gaming origins, content creation, the B5TA community, and web development. Pitch card with profile photo and signature.
- **F7: Support Page.** Buy Me a Coffee CTA with an FTC-compliant disclaimer, plus an affiliate partner grid with seven live referral links: Tesla, Twitch Prime, RouteNote, Robinhood, M1 Finance, Public, and Lyft.
- **F8: Discord Page.** Four server cards (Azqato, Azqato Invests, B5TA, League of Azqato) with permanent invite links, descriptions, emoji icons, and Discord-blue Join Server buttons.
- **F9: `iconUrl` field.** Optional image or SVG URL per project card that overrides the emoji icon when set. Used by one project (Cat Food Center).
- **F10: Introductory Landing Page.** `index.html` is the default entry point. Introduces Azqato with an easygoing bio and routes visitors to the Discord and to every other page via a grid of eight destination cards.
- **F11: Favicon.** The site-wide favicon is a lion emoji, implemented as an inline SVG data-URI `<link rel="icon">` with no external image file, repeated identically in the `<head>` of all 12 pages. The homepage's About explore-card icon matches it. **Exception:** `music.html` replaces this favicon at runtime with a live animated canvas favicon, redrawn every third frame (see F14).
- **F12: Curated Investing Hub.** `invests.html` carries 16 categories of hand-picked external resources (Platforms, Careers, ETFs, Companies, Ratings, Screeners, Real Estate, Charts, Databases, Economic Indicators, Education, Guides, Indices, Information, News) above a visible "not a licensed financial advisor" disclaimer.
- **F13: Codes Page.** `codes.html` presents the AI-tooling side of the work: the Prompts library, the browser Tools collection, and the GitHub org.
- **F14: Music Stage Visualizer.** `music.html` renders a full-screen concert stage on a fixed canvas: panoramic LED screens, trusses, lasers, fire columns, haze, dust, a crowd, a floor reflection, and a branded DJ booth, with a cinematic vignette and letterbox grade. The center screen shows one of ten modes, nine of which are WebGL2 fragment shaders. Five modes are exposed as buttons and auto-cycle randomly every 30 seconds. While the native track (F19) is playing, every one of those elements is driven by its real frequency data, and detected kicks drive the screen zoom, crowd, lasers, and shader clock together so a hit lands as one event; at all other times the same elements run on a synthetic signal. The favicon animates in sync. A play/pause control sits at the left of the mode-button row; the page starts paused on one painted frame for visitors whose system requests reduced motion (F18).
- **F15: Stage Console.** A fixed, independently scrollable glass panel docked over the center screen on `music.html`, holding the native track player (F19), two Mixcloud mix embeds, and links to Last.fm, Mixcloud, and the Mixes YouTube channel.
- **F16: Shared Stylesheet.** `styles.css` carries the design tokens, reset, nav, and footer for all 12 pages, replacing roughly 100 lines of duplicated CSS per page.
- **F17: Writing-Style Guard.** A `.githooks/pre-commit` hook blocks any commit that introduces an em dash into an HTML or Markdown file, in either the literal or HTML-entity form.
- **F19: Native Track Player.** One track (`audio/womanchild-azqato-remix.mp3`) is served from the site itself and sits at the top of the stage console, above the Mixcloud embeds. It has a play/pause button, title, elapsed and total time, and a draggable scrub bar. Because the file is same-origin, its audio can be routed through a Web Audio `AnalyserNode`, which makes the visualizer react to it for real (F14). Playing it is what turns the stage from choreography into reaction.
- **F18: Reduced Motion Support.** A sitewide `@media (prefers-reduced-motion: reduce)` block in `styles.css` suppresses every transition and hover transform, and the `music.html` visualizer reads the same preference in JavaScript to decide whether its render loop starts. A play/pause button gives every visitor a way to stop the animation, which WCAG 2.2.2 requires and which nothing on the page offered before v2.8.7.

### Future (post-launch, not committed)

- Optional GitHub API integration to auto-populate star counts and update dates.
- Animated section transitions on scroll.
- Contact or hire-me section with an email link or a GitHub Discussions CTA.
- Project detail modal with an extended README preview.
- Search bar filtering by project name or description keyword.
- Shared nav injection or a minimal build step to remove the duplicated nav markup.
- **Native track player and kick-reactive visualizer on `music.html`** (built, not deployed). A Web Audio-routed in-page player, an onset-based kick detector tuned against a real track, a beat-synced screen pulse, a rarity-gated loud-moment flash, audio-scaled laser beams, and a Video screen mode that draws the playing track onto the stage screens. Fully implemented on branch `feature/native-audio-player`; not merged because the test tracks are large local files that cannot be committed. Needs a real, externally hosted track before it can ship. See Known Technical Debt.

---

## Constraints

- Must render correctly in the latest versions of Chrome, Firefox, Edge, and Safari.
- Must be usable at viewport widths from 320 px to 2560 px. (`music.html` is unverified below 600 px; see the deferred list.)
- Page weight (HTML plus inline CSS plus inline JS) should stay under 50 KB per page, uncompressed. **`music.html` is 112 KB and knowingly breaks this.** See Success Criteria.
- No cookies, localStorage, sessionStorage, or first-party tracking of any kind.
- No user data collected or transmitted by the site itself.
- All affiliate disclosures must comply with FTC guidelines.
- No build step. The files in the repository are the files that are served.
- The owner maintains this alone, on Windows, in a text editor. Anything that requires a toolchain to edit is out of budget.

---

## Assumptions

- GitHub Pages will remain free for public repositories.
- Visitors have JavaScript enabled. Project filtering and the music visualizer require it; all other content degrades gracefully to static HTML without it.
- Affiliate programs (Tesla, Twitch Prime, RouteNote, Robinhood, M1 Finance, Public, Lyft) will honor the referral links for their stated promotional periods.
- The owner will manually maintain the `PROJECTS` array, the `discord.html` server cards, and the `support.html` affiliate cards; no automation is needed at this scale.
- Buy Me a Coffee does not require integration code; a direct link is sufficient.
- Discord invite links on `discord.html` are permanent and will not expire.
- Mixcloud will keep serving its iframe widget at a stable URL, and its two embedded mixes will stay published.
- Visitors reaching `music.html` are on a device with WebGL2. Without it the page falls back to the plain canvas LED grid rather than failing, but this fallback has not been tested on real hardware.

---

## Success Criteria

| Criterion                       | Target                                               | Status at audit |
|---------------------------------|------------------------------------------------------|-----------------|
| Page load time                  | Under 1 second on a 4G connection                    | Unverified, no measurement recorded |
| Page weight per page            | Under 50 KB uncompressed HTML                        | Met on 11 of 12 pages; `music.html` is 112 KB |
| Image payload per page          | No stated target                                     | `youtube.html` pulls 2.3 MB of thumbnails; worth a target |
| Cross-browser render            | No visual defects on Chrome, Firefox, Edge, Safari   | Manual spot checks only |
| Mobile usability                | Fully usable at 375 px (iPhone SE viewport)          | Met except `music.html`, unverified |
| Project addition time           | Under 2 minutes to add a new project card            | Met |
| Affiliate link accuracy         | All 7 affiliate links point to live, correct URLs    | Verified by reading, not by clicking |
| FTC compliance                  | Affiliate disclosure visible on the Support page without scrolling | Met |
| Documentation accuracy          | Every page, feature, and asset appears in `/docs`    | Met as of v2.8.5 |

---

# Technical Requirements

---

## System Architecture

The portfolio is a fully static site with no server, no build step, and no runtime. It consists of 12 plain HTML pages, each containing all of its own page-specific CSS and JavaScript inline, plus one shared stylesheet. There is no bundler, no transpiler, and no dependency graph. The introductory landing page (`index.html`) is the default entry point.

```
Browser
  → Cloudflare Pages (azqato.com, canonical)
  → GitHub Pages   (azqato.github.io, same files, separate deployment)
      → index.html (default entry)
        about.html      discord.html    invests.html
        codes.html      music.html      links.html
        projects.html   youtube.html    support.html
        accounts.html   privacy-policy.html
      → styles.css   (shared, linked by all 12 pages)
      → img/*.jpg    (5 referenced, 10 unreferenced)

music.html only, at runtime:
  → player-widget.mixcloud.com  (2 iframes)
```

Navigation between pages is standard `<a href>` links; there is no client-side router. The browser performs a full page load on every navigation. Every page is independently reachable and independently correct; no page depends on state set by another.

### Per-page JavaScript

| Page | JavaScript |
|------|------------|
| All 12 | The nav toggle IIFE: opens and closes the mobile dropdown, closes on link click and on outside click. Roughly 20 lines, duplicated verbatim. |
| `projects.html` | `buildCard`, `buildFilters`, `render`, `bindFilters`. Renders the grid from `PROJECTS` and wires the filter bar. |
| `music.html` | The visualizer: roughly 1,900 lines including GLSL shader source, plus the mode-button binding and the animated favicon. |

No other page has any JavaScript beyond the nav toggle.

---

## Tech Stack

| Layer           | Technology      | Version / Notes                                                   |
|-----------------|-----------------|-------------------------------------------------------------------|
| Markup          | HTML5           | Semantic elements: `<nav>`, `<section>`, `<footer>`               |
| Styling         | CSS3            | Custom properties, Grid, Flexbox, `@media`, `backdrop-filter`     |
| Scripting       | JavaScript      | ES6+ in `projects.html` (arrow functions, template literals, `Set`, spread). ES5-style `var` and `function` in the nav toggles and the `music.html` visualizer. Both styles are current; see Conventions. |
| Graphics        | Canvas 2D       | The `music.html` stage, reflection, bloom, and favicon             |
| Graphics        | WebGL2 / GLSL ES 3.00 | Nine fragment-shader screen modes in `music.html`, rendered offscreen at 640x400 |
| Hosting         | Cloudflare Pages and GitHub Pages | Two independent deployments of the same `main` branch root. Cloudflare Pages serves `azqato.com` and is canonical; GitHub Pages serves `azqato.github.io`. See Hosting |
| Version Control | Git / GitHub    | Repository `Azqato/azqato.github.io`; `main` deploys on push        |

No npm packages. No `package.json`. No lockfile. No CDN scripts. No external fonts. The only third-party code in the repository is the shader source in `music.html`, which carries per-mode attribution in comments (CC0, MIT, CC-BY-NC-SA-4.0, and individually credited authors).

---

## Folder Structure

```
/
├── README.md                 - public front door, general-reader oriented
├── LICENSE.md                - copyright and terms of use; all rights reserved, source-available
├── robots.txt                - fully open to all crawlers, deliberately; points at the sitemap
├── sitemap.xml               - all 12 pages, lastmod taken from git
├── index.html                - landing page: intro, Discord CTA, explore grid
├── about.html                - bio and pitch card
├── discord.html              - four community server cards
├── invests.html              - redirect page to invests/ (since v2.11.0)
├── _redirects                - Cloudflare Pages rules: /invests and /invests.html to /invests/
├── invests/                  - Azqato Invests, a self-contained 21-page site with its own
│                               generator, checks and docs (invests/README.md, invests/docs/);
│                               its rules apply inside the folder; built by invests/scripts/site.py
├── codes.html                - AI tooling: Prompts, Tools, GitHub
├── music.html                - stage visualizer, native track player, Mixcloud embeds, platform links
├── links.html                - every platform, grouped
├── projects.html             - filterable project grid, driven by the PROJECTS array
├── youtube.html              - four channel cards
├── support.html              - Buy Me a Coffee plus seven affiliate cards
├── accounts.html             - gaming profiles (not in nav)
├── privacy-policy.html       - policy and disclaimers (not in nav)
├── styles.css                - shared tokens, reset, nav, footer
├── audio/
│   └── womanchild-azqato-remix.mp3  - the one same-origin track; drives the visualizer (6.1 MB)
├── .gitignore                - env-file patterns, plus the local-only brand folder
│                             (there is no .gitattributes; see Repository Hygiene)
├── .githooks/
│   └── pre-commit            - em-dash writing-style guard
├── tools/
│   └── build-nav.py          - stamps the shared nav into every page; output is committed
├── .vscode/
│   └── settings.json         - editor chat settings
├── img/                      - 15 files, 5 referenced by pages, 10 unreferenced
└── docs/
    ├── PRD.md                - this file
    ├── DESIGN.md             - design system
    ├── PATCHNOTES.md         - versioned changelog
    └── TODO.md               - open work and unresolved decisions; not an instruction list

Untracked and local only (present in the working tree, not in git):
├── music/                    - local test-track folder for the paused player branch
├── test-local-audio.bat      - launches Chrome with file-access restrictions relaxed
├── brand/                    - brand and merchandise concept folder, see below
│   ├── 00-brand-foundation.md      - mascot traits, palette, lanes, voice
│   ├── 01-prior-art-and-prompt-rules.md - findings from the music project
│   ├── 02-final-review.md          - assessment of the 100 concepts
│   ├── README.md                   - ranked index
│   ├── assets/                     - 100 concept files, one image asset each
│   └── index.html                  - generated reading page (279 KB)
├── tools/build-brand-page.py - generates brand/index.html from brand/assets/*.md
└── .claude/settings.local.json - ignored via the user's global gitignore
```

**Why `brand/` is ignored rather than committed.** GitHub Pages serves this repository
publicly from the root, so a committed `brand/` would be readable at `azqato.com/brand/`,
including supplier notes, priority scores and an open question about the mascot's licensing
provenance. It is excluded in `.gitignore` rather than merely left unstaged, because a
`git add .` would otherwise publish it in one keystroke. `tools/build-brand-page.py` is
ignored alongside it: it only builds that folder and would be a dangling reference in a
fresh clone. Reversing the decision is a two-line edit to `.gitignore`.

---

## Data Models

### Project Entry (defined in the `PROJECTS` array in `projects.html`)

```js
{
  name: string,       // required, display name on the card
  desc: string,       // required, short description, 1 to 3 sentences
  github: string,     // required, full GitHub repo URL, or the project site URL when there is no public repo
  demo: string,       // optional, live site URL; the card title links here when set
  tags: string[],     // required, category labels; the first tag takes the langClass color
  langClass: string,  // optional, CSS class for the language tag color (for example "lang-js")
  icon: string,       // optional, emoji in the card icon area; defaults to a package emoji
  iconUrl: string,    // optional, image or SVG URL; overrides icon when set
  stars: string,      // optional, star count label; unused by every current entry
  updated: string,    // optional, last-updated label (for example "2026")
}
```

The 15 current projects, in array order: Automate Fundamentals, Net Worth Tracker, VIX Strategy, ComposerAtlas, Stock Methodology, Leveraged Strategies, Lantern, Cat Food Center, Clan B5TA, Boaty McBoatface Ventures, No Fee Apartments, LV Guest List, Prompts, ProteinPulse, Azqato's Tools.

Active filter tags, derived automatically from the array: Education, Finance, Health, Meme, Real Estate, Social, Tools. The filter bar sorts them alphabetically and prepends "All".

**The `github` fallback rule (adopted 2026-09-28).** `github` is a required field, but not every project has a public repository: some are private, and some are not ours to host. Those entries point `github` at the project's own site instead, and set `demo` to the same URL. Three entries do this: Automate Fundamentals (private repository), No Fee Apartments and LV Guest List (external commercial sites).

The card reads this off the URL rather than off a separate flag. `buildCard` tests `github` against `^https://github\.com/`; when it does not match, the icon's `title` and `aria-label` become "No public repository, opens the project site" instead of "View on GitHub". Deriving it from the host means the label cannot drift from the link, which a hand-set boolean would eventually do. The GitHub octocat mark still renders, because the icon marks the repository slot rather than the destination, and relabeling it is what keeps that honest for a screen reader.

Two entries (No Fee Apartments, LV Guest List) omit `updated` and therefore render no card footer. Every entry sets `langClass`. Automate Fundamentals is the only one on `lang-cs`, for .NET; the class had been defined in the stylesheet since the page was written but no project had used it until now.

### Discord Server Entry (defined in `discord.html` static HTML)

Each server is a static `.server-card` block. There is no JavaScript data model.

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

The whole card is an anchor to the referral URL.

```html
<a class="affiliate-card" href="[referral URL]" target="_blank" rel="noopener">
  <div class="affiliate-logo" style="background: rgba(r,g,b,a); border: 1px solid rgba(r,g,b,a);">[emoji]</div>
  <span class="affiliate-name">[Partner]</span>
  <span class="affiliate-promo">[short promo, e.g. "Free $20"]</span>
  <p class="affiliate-desc">[what the visitor gets]</p>
  <span class="affiliate-link-btn">[CTA text] &rarr;</span>
</a>
```

Active affiliate cards, in page order:

| Partner | URL | Promo shown |
|---------|-----|-------------|
| Tesla | `ts.la/robert459550` | Free 3 Months FSD |
| Twitch Prime | `twitch.tv/azqato` | Free Sub (No Cost) |
| RouteNote | `routenote.com/rn/referral/2fcd201c` (code `2fcd201c`) | Referral Code: 2fcd201c |
| Robinhood | `join.robinhood.com/robertg273/` | Free $5 to $200 Stock |
| M1 Finance | `m1.finance/BVZBG3OqOfMj` | Free $75 Bonus |
| Public | `share.public.com/azqato` | Free $20 |
| Lyft | `lyft.com/invite/ROBGOLDY630855` | 50% Off First Ride |

> **Discrepancy (resolved in favor of the code).** Before this audit, this section described the card as a `<div>` containing `.logo-area`, `.promo-badge`, `.affiliate-desc`, and `.affiliate-btn`. Three of those four class names do not exist in `support.html`. The structure above is read from the source, and DESIGN.md has been corrected to match in the same pass.

### Visualizer State (defined in `music.html`, in the visualizer IIFE)

Not a persisted model, but the closest thing the site has to application state:

| Name | Type | Meaning |
|------|------|---------|
| `screenMode` | number 0-9 | Which center-screen mode is drawing. Defaults to 4 (Squares). |
| `modeTimer` | number | Frames since the last mode change; triggers a random switch at 1,800. |
| `t` | number | Global frame counter driving every procedural animation. |
| `smoothed` | Float32Array(64) | Per-band amplitude, exponentially smoothed. |
| `phases` | number[64] | Fixed random phase offsets, generated once per page load. |
| `lay` | object | All stage geometry, recomputed on every resize. |
| `analyser`, `freqData` | AnalyserNode / Uint8Array, or null | Created on the visitor's first press of the track play button. Null until then, and null forever if the browser has no `AudioContext` or the source could not be wired. |
| `audioCtx`, `audioWired` | AudioContext / boolean | The context is created once, lazily, inside the click handler so browsers accept it as a user gesture. `audioWired` guards `createMediaElementSource`, which throws if called twice on the same element. |
| `seeking` | boolean | True while the visitor drags the scrub bar, so `timeupdate` does not fight the drag. |

---

## API Design and Internal Data Flow

The site has no API, no endpoints, no fetch calls, no XHR, no WebSockets, and no service worker. The internal flows are:

### Project rendering and tag filter (`projects.html`)

```
PROJECTS array (static data in the page)
  → render()
      → PROJECTS.map(buildCard) builds card HTML via template literals
      → grid.innerHTML = the joined result
      → #project-count set to "N projects"
      → buildFilters(PROJECTS): collects unique tags into a Set, sorts, appends a button per tag
      → bindFilters(): attaches a click handler to every .filter-btn
  → on click:
      → move the .active class to the clicked button
      → for each .project-card: data-hidden = (filter === 'all' || tags include filter) ? 'false' : 'true'
      → recount visible cards and rewrite #project-count
```

Error states: none are handled. If `PROJECTS` is empty the grid renders an explicit empty-state message. A malformed entry throws in the console and leaves the grid partially rendered; there is no try/catch anywhere in the file.

### Nav toggle (all 12 pages)

```
click .nav-toggle  → toggle .open on .nav-links, mirror the state into aria-expanded
click any link     → remove .open, reset aria-expanded
click outside both → remove .open, reset aria-expanded
```

Guards on `if (!toggle || !links) return;` so the script is inert if the markup is missing.

### Visualizer frame loop (`music.html`)

```
build()                       on load and on every window resize
  → size the canvas to viewport * min(devicePixelRatio, 2)
  → prerender the vignette and letterbox into a half-size buffer
  → size the half-res reflection buffer
  → compute every stage coordinate into `lay`

draw()                        every animation frame
  → t++
  → if ++modeTimer >= 1800: pick a new random mode from [2,3,4,6,8], reset the timer, sync buttons
  → renderGL<n>() for the active mode, into the offscreen 640x400 WebGL canvas
  → drawBg, drawBeatFlash, 3x drawTruss, 2x drawTrussLights
  → center screen: drawGrid (mode 0) or drawImagePanel (modes 1-9)
  → drawWingScreen L and R, drawStageFloor, drawReflection, drawBooth
  → drawFire, drawLasers, drawDust, drawHaze, drawCrowd
  → composite the prerendered vignette
  → every 3rd frame: updateFavicon() redraws a 32x32 spoke ring and swaps the <link rel="icon"> href
  → requestAnimationFrame(draw)
```

Error states: shader compilation failures are logged to the console via `console.error` and set `gl = null`, which silently falls the page back to mode 0's canvas LED grid. This is the only error handling on the site.

### What drives the visualizer

`freq(i)` has two branches.

**Real.** While the native track plays, `sampleAudio()` runs once per frame and fills all 64 bands; `freq(i)` only reads the result. It used to call `getByteFrequencyData` itself, which refetched the whole spectrum 64 times a frame.

Four things about that sampling matter, and each was a defect fixed in v2.9.1:

| Property | Value | Why |
|----------|-------|-----|
| Band spacing | Logarithmic, 30 Hz to 16 kHz, with every band forced to advance at least one bin | Hearing divides pitch logarithmically. Spread linearly, the entire kick region fell inside band 0 while sixty-odd bands showed hiss. The minimum-one-bin rule was added in v2.9.2: without it the first fourteen bands rounded to the same bin and moved as one value, so the log mapping delivered nothing where it mattered most. Linear at the bottom, logarithmic at the top, which is what a mel scale does. |
| `fftSize` | 1024, about 43 Hz per bin | 256 gave 190 Hz per bin, wider than the whole kick band. Not 2048: that window spans 46 ms, longer than a frame, and smears transients. |
| Within-band reduction | Peak, not mean | A mean lets one loud bin be averaged away by quiet neighbours. |
| Smoothing | Analyser 0.35, then asymmetric `0.25 / 0.75` rising and `0.82 / 0.18` falling | The old pair, 0.8 and a symmetric `0.72 / 0.28`, were two low-pass filters in series. A kick is a transient; they removed it. |

The raw 0-1 value is still raised to the power 1.6, which pushes mid-level noise down while leaving true peaks near 1.

**Kick detection.** A second analyser exists for one job: finding hits. `fftSize` 2048 for about 23 Hz per bin, `smoothingTimeConstant` 0, tapping the same source but never connected to the output. It takes the opposite resolution trade from the general analyser deliberately.

Detection is by onset, not by level. On a modern master the bass sits near the ceiling almost continuously, so "is the bass loud right now" is true nearly always and discriminates nothing. A kick is instead its attack: a sharp rise in 30-150 Hz energy over the last few frames, against a threshold that adapts to the track's own recent behaviour. A 26-frame refractory follows each hit. `beatPulse` then drives the screen zoom, the crowd bounce, the laser intensity, and the WebGL clock at once, which is what reads as reaction; one brightness change does not.

Measured against the track rather than judged by eye: 92 hits in 44.5 s, 124.0 per minute, median interval 0.480 s implying 125.0 BPM, and 94 percent of intervals inside 380-620 ms.

**Synthetic.** Otherwise, band `i` is three summed sine waves at different rates with a fixed random phase, smoothed identically. This is the branch that runs when the track is paused, when it has never been started, and when a Mixcloud embed is playing. A paused element reads as silence, so falling through to the analyser would flatten the stage instead of idling it.

Two consequences worth carrying into any copy about the page. The stage genuinely reacts to the native track, and only to it. It does not and cannot react to the Mixcloud embeds, which are a separate origin whose audio no browser will expose to this page.

---

## State Management

State is minimal, lives entirely in memory, and does not survive a page load. Nothing is persisted anywhere: no localStorage, no sessionStorage, no IndexedDB, no cookies, no server.

| State | Location | Type | Description |
|-------|----------|------|-------------|
| Active filter | `projects.html` DOM | class plus attribute | The selected tag lives as `.active` on one `.filter-btn`; per-card visibility lives as `data-hidden` on each card. No JavaScript variable holds it. |
| Visible project count | `projects.html` DOM | text | Recomputed from the DOM on every filter click. |
| Nav dropdown open | every page, DOM | class plus ARIA | `.open` on `.nav-links`, mirrored into `aria-expanded` on the toggle. |
| Visualizer state | `music.html` closure | see the Visualizer State table above | Reset on every load. |

> **Discrepancy (resolved in favor of the code).** Before this audit, this section listed a single state variable, `activeTag`, described as a string in `projects.html` JS scope defaulting to "All". No such variable exists in the file. Filter state has always lived in the DOM. The table above is what the code does.

---

## Third-Party Integrations

| Service | Purpose | What it receives | When |
|---------|---------|------------------|------|
| **Cloudflare Pages** | Static hosting and CDN delivery for `azqato.com`, the canonical domain, which is where essentially all traffic goes | Standard web server access data (IP, user agent, referrer) for every request | Every page load |
| GitHub Pages | Static hosting for `azqato.github.io`, a separate deployment of the same files | Standard web server access data (IP, user agent, referrer) for every request | Every page load on that address |
| Mixcloud (`player-widget.mixcloud.com`) | Two embedded mix players on `music.html` | The visitor's IP, user agent, and referring page, plus whatever Mixcloud's widget sets in its own frame | On every `music.html` load, before any interaction |
| Buy Me a Coffee | Donation link | Nothing until the visitor clicks | On click |
| Tesla, Twitch Prime, RouteNote, Robinhood, M1 Finance, Public, Lyft | Affiliate referrals | Nothing until the visitor clicks; then the referral code identifies Azqato as the referrer | On click |
| Discord | Community invites | Nothing until the visitor clicks | On click |
| Every external link on `invests.html`, `links.html`, `accounts.html`, `youtube.html` | Outbound navigation | Nothing until the visitor clicks | On click |
| Cat Food Center favicon (`azqato.github.io/Cat-Food-Center/favicon.svg`) | The one `iconUrl` project image on `projects.html` | A request to another GitHub Pages site owned by Azqato | Every `projects.html` load |

No authentication is used with any of these. There are no API keys, tokens, or accounts involved on the site side.

> **Discrepancy (open).** Several places in this document and in the README have long stated that the site makes "zero outbound HTTP requests on page load" and has "no external requests of any kind". That is true of 11 pages. It is not true of `music.html`, which loads two Mixcloud iframes on every visit, and it is marginally untrue of `projects.html`, which fetches one favicon from a sibling GitHub Pages site. The privacy claim in the README has been narrowed to match. Whether the Mixcloud embeds should be click-to-load (restoring a true zero-request promise) is an open product decision, recorded as Open Question 3.

---

## Performance Requirements

| Metric                         | Target                         | Actual at audit |
|--------------------------------|--------------------------------|-----------------|
| Page weight (uncompressed HTML)| Under 50 KB per page           | 6.7 KB to 23.8 KB on 11 pages; `music.html` 112 KB |
| Shared CSS                     | No target                      | 2.8 KB, cached across pages |
| Time to first meaningful paint | Under 1 second on 4G           | Not measured |
| External requests on page load | 0 on all pages except `music.html` and `projects.html` | 2 iframes on `music.html`; 1 image on `projects.html` |
| Image payload                  | No target set                  | `youtube.html` 2.3 MB, the worst page on the site |
| Offline functionality          | Fully usable after first load  | True for 11 pages; the `music.html` embeds fail offline while the visualizer keeps running |
| Sustained frame rate           | 60 fps on desktop              | Not measured; `music.html` runs an unthrottled `requestAnimationFrame` loop with WebGL and multiple canvas composites per frame. Since v2.8.7 a visitor can stop it with the pause button, and it never starts for anyone who requested reduced motion, but it still does not pause on its own when the tab is hidden |
| Browser support                | Chrome, Firefox, Edge, Safari latest | Manual spot checks |
| Viewport range                 | 320 px to 2560 px              | Met except `music.html` below 600 px |

The 50 KB budget is a real constraint that shaped 11 pages and should keep shaping them. `music.html` breaks it by 82% because it carries roughly 1,700 lines of GLSL and canvas drawing code inline. That was accepted rather than overlooked: extracting it to a `.js` file would trade one request for a smaller document and is the obvious fix if the page ever needs to get faster.

---

## Known Technical Debt

| Item | Current shortcut | Correct solution |
|------|------------------|------------------|
| Nav toggle script repeated across pages | The roughly 20 line toggle IIFE is still duplicated verbatim in all 12 HTML files. The nav markup itself is no longer duplicated by hand: it is stamped by `tools/build-nav.py` as of v2.8.8. | Either extend the stamp script to cover the script block, or leave it. It has never changed since it was written, so the duplication costs nothing today. |
| Nav drift is detectable but not enforced | `python tools/build-nav.py --check` reports any page whose nav is out of date, but nothing runs it automatically | Add it to the `pre-commit` hook alongside the em-dash guard, so a hand-edited nav cannot be committed |
| `music.html` JS is inline | Roughly 1,900 lines inline, pushing the page to 112 KB | Extract to `viz.js`; it is the only page that would use it, so this trades a request for a cacheable file |
| Tab-hidden render loop on `music.html` | The visualizer keeps drawing when the tab is in the background, beyond whatever the browser throttles on its own | Pause on `document.hidden` via a `visibilitychange` listener, reusing the `setPlaying()` function added in v2.8.7. Battery and heat, not accessibility. |
| Only one native track, hardcoded | `audio/womanchild-azqato-remix.mp3` is a single `<audio>` element with its title written into the markup. Adding a second means copying the block. | If more tracks arrive, move to a `TRACKS` array rendered the way `projects.html` renders `PROJECTS`, rather than copying markup a third time |
| Ten unreferenced images in `img/` | Roughly 3.8 MB tracked and deployed but linked from nothing | **Not debt. Closed by decision on 2026-08-29:** the owner keeps everything in `img/`. See the standing rule under Never Do These. Audits should stop raising it. |
| Unoptimized thumbnails | Four `yt-thumb-*.jpg` totalling 2.3 MB on a 7.8 KB page, with no `loading="lazy"` | Resize to display dimensions, convert to WebP with a JPEG fallback, add `loading="lazy"` |
| No CSP headers | **No longer a host limitation.** True of GitHub Pages, which cannot send custom response headers. False of Cloudflare Pages, which serves the canonical domain and supports a `_headers` file. | Acceptable for static content with no user input. Since 2026-09-29 this is a decision not to add one rather than an inability to, and a CSP on `azqato.com` is available whenever it is wanted. |
| No automated tests | Manual visual QA only | A Playwright smoke test per page (loads, nav renders, no console errors) would catch the majority of regressions. The threshold for this was set at 11 pages and has been passed. |
| Native player has no hostable audio | The test tracks are multi-GB local files; GitHub rejects pushes over 100 MB and GitHub.com's Git LFS caps at 2 GB per file, both far under these files' size | Host a real track externally (object storage plus a CDN, or a video host that serves a direct file URL), point the branch's `<video src>` at it, then merge `feature/native-audio-player` |

---

# Conventions

Derived from the code itself, not from any external style guide. Where the codebase is inconsistent, the dominant form is named so the next contributor matches the majority rather than the last file they happened to open.

## Naming

| Thing | Convention | Examples |
|-------|------------|----------|
| HTML files | lowercase, hyphenated, `.html` | `privacy-policy.html`, `index.html` |
| Image files | lowercase, hyphenated, `area-subject.jpg` | `yt-thumb-mixes.jpg`, `about-profile.jpg`, `music-playlist-bangers.jpg` |
| CSS classes | lowercase, hyphenated, BEM-ish without the strict separators | `.nav-links`, `.affiliate-link-btn`, `.stage-console`, `.console-embed` |
| CSS custom properties | `--lowercase-hyphenated`, semantic before literal | `--text-muted`, `--card-hover`, `--accent-hover` |
| JS functions | `camelCase`, verb-first | `buildCard`, `bindFilters`, `drawStageFloor`, `syncModeBtns` |
| JS constants (module-level data) | `SCREAMING_SNAKE` | `PROJECTS`, `MODE_LEN`, `N` |
| JS locals | short `camelCase`; single letters are normal in the visualizer | `p`, `cx`, `lay`, `freqData` |
| Element IDs | lowercase, hyphenated, only where JS needs a handle | `#project-grid`, `#filter-bar`, `#project-count`, `#viz` |
| Data attributes | `data-` plus lowercase | `data-filter`, `data-tags`, `data-hidden`, `data-mode` |
| Branches | `feature/kebab-case` | `feature/native-audio-player` |

One deviation worth knowing: the image file `20260711-0151-37.7601512.gif` follows no convention at all. It is a camera or capture export name that was committed as-is.

## Formatting

- **Indentation:** 2 spaces everywhere, in HTML, CSS, and JS. No tabs anywhere in the repository.
- **Quotes:** double quotes in HTML attributes, without exception. In JS, both are present: `projects.html` uses double quotes in the `PROJECTS` data and backticks for templates, while the nav toggles and `music.html` use single quotes. Single quotes are dominant in imperative JS; double quotes are dominant in data literals. Match the file you are in.
- **Semicolons:** always, in every JS file.
- **Trailing commas:** used in the multi-line `PROJECTS` objects and arrays.
- **Line length:** no limit is enforced. Most lines stay under about 120 characters, but the visualizer has deliberate long lines (the mode-cycle statement is a single ~180-character line), and card descriptions in `PROJECTS` run to whatever length the sentence needs.
- **Section comments:** CSS and JS are divided by box-drawing comment banners, `/* ── SECTION ── */` in CSS and `// ── Section ─────` in JS. This is the single most consistent stylistic habit in the codebase and should be preserved.
- **HTML comments** mark the major regions of every page body: `<!-- NAV -->`, `<!-- HERO -->`, `<!-- PROJECTS -->`, `<!-- AFFILIATES -->`.
- **Blank lines:** one between rules and logical blocks, never two.

## Organization

- **One page, one file.** Each page carries its own `<style>` and `<script>`. Only genuinely universal CSS lives in `styles.css`.
- **File size norms:** 6 KB to 24 KB per page is the working range. `music.html` at 112 KB is the acknowledged outlier and is the trigger point for extracting to an external file.
- **Script placement:** always at the end of `<body>`, never in `<head>`, never with `defer` or `async` (unnecessary at that position).
- **Module pattern:** every script is a bare IIFE, `(function () { ... })();`. There are no ES modules, no exports, and no globals beyond what the IIFEs close over.
- **Data before behavior:** in `projects.html` the `PROJECTS` array sits at the top of the script under a comment block that documents every field, followed by render functions, followed by the call to `render()`. New data-driven pages should copy that shape.

## Comments

Comment density is low and purposeful. The codebase does not narrate what the code does; it explains why, or it labels a region.

What earns a comment here:

1. **Region banners.** The box-drawing dividers described above.
2. **A maintenance contract.** The block above `PROJECTS` documenting every field and every `langClass` option exists so the owner can add a project without reading the render code. This is the most valuable comment in the repository.
3. **A non-obvious trick.** `// Tiny buffer for cheap panel bloom (upscale blur trick)`, `// bottom of the fascia is wider than the top (booth viewed from below)`.
4. **A magic number's meaning.** `var MODE_LEN = 1800; // ~30 s at 60 fps`.

What does not earn a comment: anything a reader can get from the identifier. There are no JSDoc blocks, no type annotations, and no commented-out code in the current tree.

## Error handling, logging, and validation

There is essentially none, and that is a deliberate consequence of the architecture rather than an oversight. With no user input, no network calls, and no persistence, the failure modes that error handling exists to catch do not occur.

The three exceptions, which are the whole pattern:

- `if (!toggle || !links) return;` in every nav toggle: a null guard that makes the script inert rather than throwing if the markup changes.
- `console.error('GL shader err:', ...)` plus `gl = null` in `music.html`: the only logging on the site, and the only fallback path.
- `PROJECTS.length ? ... : '<div class="empty-state">...'` in `projects.html`: the only empty-state handling.

If you add anything that can fail (a fetch, a parse, a storage read), you are introducing a new category to this codebase. Handle it explicitly and silently, matching the shader fallback: degrade to something that still renders, log once, and never show the visitor an error.

## Commit messages and branching

Read from 271 commits of history rather than from any contributing guide.

- **Single-line subject, imperative or descriptive, no type prefixes.** The project does not use Conventional Commits. Real examples: `Dock music.html embeds/links in a fixed, scrollable stage console panel`, `Fix Mixcloud embed width on music.html`, `Reorder invests.html project cards; rename Stock Methodology to Stocks`.
- **A version number is included when the commit corresponds to a patch-note entry**, in one of two dominant forms: a leading `vX.Y.Z:` prefix (`v2.8.0: visualizer overhaul + footer link update across all pages`) or a trailing parenthetical (`Update Leveraged Strategies link to /leverage/ (v2.7.2)`). The trailing form dominates the v1.x and v2.6.x eras; the leading form dominates recent minor releases. Either is acceptable; be consistent within a release.
- **Scope prefix by file** is common for page-specific work: `music.html: layout and UI polish`.
- **Bodies are rare.** Most commits are subject-only.
- **Every commit ends with a `Co-Authored-By: Claude ...` trailer** where the work was done with an assistant. Four different model names appear across history; use the model actually doing the work.
- **Branching:** trunk-based. Work goes straight to `main` and deploys on push. Long-running work that cannot ship gets a `feature/` branch that is pushed to GitHub and left there (`feature/native-audio-player` is the only example). One pull request exists in the history, from an automated Cloudflare integration.

---

# Writing Style

This project has its own rule, stated before this audit and enforced mechanically. It is documented here as-is and has not been replaced by any default.

All copy across the site and documentation must be easy to read and free of em dashes and double dashes. These punctuation marks interrupt reading flow and often obscure meaning. Use the following alternatives:

| Situation | Preferred punctuation | Example |
|---|---|---|
| Continuing a thought naturally | Comma | "Fast, clean, and honest about what it is." |
| Introducing a list or explanation after a complete clause | Colon | "Each strategy gets a dedicated page covering: rules, risks, and sources." |
| Connecting two closely related independent clauses | Semicolon | "Buy Me a Coffee does not require integration code; a direct link is sufficient." |
| Adding supplementary or aside information | Parentheses | "The portfolio is open source and hosted on GitHub." |
| Separating two ideas that are better as their own sentences | Period | "Fully client-side. All data stays in your browser's localStorage." |
| A title, heading, or version line where a comma reads awkwardly | Single hyphen | "## [2.8.5] - 2026-08-24" |

Em dashes appear in two forms in HTML: as the literal Unicode character (`—`) and as the HTML entity (`&mdash;`). Both are prohibited, and audits must search for both forms independently, because a search for one does not find the other.

The single hyphen is permitted and encouraged wherever context justifies it. The prohibition does not cover it. En dashes in numeric or version ranges are also permitted and are not checked by the hook.

An instance that the text needs in order to mean anything is left alone: a rule that names the character it prohibits, a table row demonstrating it, or a changelog entry describing its removal. This document, `.githooks/pre-commit`, and several historical patch notes all contain the character for exactly this reason.

CSS custom properties (`--accent`, `--text-muted`) and command-line flags (`--no-verify`, `git checkout <hash> -- file`) are valid syntax, not punctuation, and are never touched.

**Tone:** direct and functional. Plain declarative sentences. No marketing language, no filler openings, no restating the question before answering it.

**Enforcement.** A `pre-commit` hook in `.githooks/` blocks any commit introducing either em-dash form into an HTML or Markdown file. In Markdown, occurrences inside backtick code spans are exempt so the rule can document the character itself. Enable it once per clone with `git config core.hooksPath .githooks`; bypass in an emergency with `git commit --no-verify`.

**Sweep result at the v2.8.5 audit.** Every text file in the repository was scanned independently for the literal character and for the entity, including files inside dot-directories that a plain recursive glob skips. Four occurrences were found in tracked project files, all inside backtick code spans in `docs/PRD.md` and `docs/PATCHNOTES.md`, all of them the rule naming or quoting itself, all legitimately exempt. Two occurrences were found in `.githooks/pre-commit`, also the rule defining itself, also exempt. **Zero violations were found in any HTML file, in `styles.css`, or in any documentation prose.**

**Sweep result at the v2.9.9 audit. Zero violations.** Every tracked file was scanned again for the literal character and for the entity independently, including files inside dot-directories, plus the four files this audit created. Four occurrences remain in `docs/PRD.md` and `docs/PATCHNOTES.md` and two in `.githooks/pre-commit`, all inside backtick code spans, all of them the rule naming or quoting itself, all exempt. The one file that was out of compliance at the v2.8.5 audit, `.vscode/recentfedsummary.MD`, was deleted in v2.8.9; see Open Question 1.

---

# Browser Testing

The project states no rule of its own on this, so the default is adopted and recorded here as policy.

**Use Microsoft Edge, never Chrome, for any automated or headless browser testing.** Chrome is the owner's day-to-day browser on this machine, and driving it disturbs a live session, including its profile, its open tabs, and its logged-in state. Edge runs the same Chromium engine, produces the same rendering results, and is already installed on Windows.

This applies to every browser a test drives, not only one named in a config file. An ad hoc headless invocation from a shell command or a batch file is testing and falls under the same rule.

**Resolved binary paths on this machine (Windows 11):**

| Browser | Path |
|---------|------|
| Microsoft Edge | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |
| Google Chrome | `C:\Program Files\Google\Chrome\Application\chrome.exe` (do not drive) |

The Edge path above was verified on this machine at the v2.9.9 audit: the binary exists and is 5,403,976 bytes, dated 2026-09-24. The Chrome path is taken from `test-local-audio.bat`, where it is known to be correct.

**Existing deviation, recorded not overruled.** `test-local-audio.bat` in the working tree (untracked) launches Chrome, not Edge, with `--allow-file-access-from-files`, `--disable-web-security`, and a throwaway `--user-data-dir` under `%TEMP%`, pointed at `music.html`. It exists to test the paused native audio player against a local file. It predates this policy. It does use a separate user-data directory, so it does not touch the owner's live Chrome profile, which is the specific harm the policy guards against. If it is revived when `feature/native-audio-player` resumes, switching it to `msedge.exe` is a one-word change and should be made then.

No second browser engine is targeted. The site is not tested against Firefox or Safari automatically; cross-browser checks are manual and occasional.

---

# Verification Environment

The project stated no rule of its own on this, so the default is adopted and recorded here as policy.

**Verify locally. Never verify against production unless explicitly asked to.** A change is checked on a local server before it is pushed, not after. Production is where visitors are; it is not a test environment, and treating it as one means every visitor between the push and the fix sees the broken state.

**Local means a server, not `file://`.** Run `python -m http.server` and open `http://localhost:8000`. This matters more here than in most projects: `music.html` sets `canRouteAudio` to false on the `file://` protocol, so the visualizer cannot read the audio and the page shows a note saying so. A `file://` check of that page verifies a degraded mode that no visitor uses.

**Confirming a deploy landed is not an exception to this rule.** After a push, opening `https://azqato.com/` with a cache-busting query string to confirm the change arrived is a post-push comparison against what was already verified locally. It answers "did the host publish what I pushed", which is a question about the host, and it has to be asked of each host separately because there are two. It is not a test of the change, it does not substitute for the local check, and finding the change present there proves nothing about whether the change is correct.

---

# Testing Cadence

The project had a rule of this kind and it has been **replaced**, because it required a browser check after every edit with no project-specific reason given for the frequency. The old wording is quoted in the v2.9.9 PATCHNOTES entry.

**Browser tests use headless Microsoft Edge**, never Chrome. See Browser Testing for why and for the binary path. Pass a unique `--user-data-dir` on every run: a stale Edge process will silently ignore the flags of a second invocation that shares its profile directory, which produces a screenshot of the wrong thing and no error.

**Run an assumption check and one browser test immediately before a major update ships.** Not after every edit. The assumption check is the cheap part: re-read the claims the change depends on, against the code, right before shipping. The browser test is one run against the local server, on the pages the change actually touches.

**Minor updates ship without either.** Wording, documentation, comments, and patch note entries do not get a browser test. Nothing in a `/docs` edit can change what renders, and running a browser to confirm that is theatre.

**Batch edits, then test once.** Several related changes are made, then verified together in a single pass. Testing after each individual edit multiplies the slowest step in the loop by the number of edits and finds nothing that the batched test would miss.

**Confirming a deploy arrived is not a test.** See Verification Environment.

What counts as major here: a change to any page's layout or rendering, anything touching `music.html`'s visualizer or `build()`, anything touching `styles.css`, a new page, a change to the nav, or a change to the `PROJECTS` array that alters how cards render. What counts as minor: documentation, comments, copy edits, patch notes, and a data-only change that follows an existing pattern exactly.

The detailed step list under How to Verify a Change still applies; this section governs **when** it runs, not what it contains.

---

# Repository Hygiene

**This is a policy record, not a task list.** The audit reads the repository's configuration and writes the rule down. Gaps are reported below as discrepancies. Nothing in this section authorises a state-changing version control command, and creating or editing an ignore file is a separate change that the owner asks for.

| Rule | State at the v2.9.9 audit |
|------|---------------------------|
| An ignore file is present | Met. `.gitignore` at root. |
| `.gitattributes` pins line endings where it matters | **Not met.** No `.gitattributes` exists. See the discrepancy below. |
| A lockfile is committed | Not applicable. No dependencies, no manifest, no lockfile, by design. See Tenet 2. |
| Secrets are never committed | Met. `.env*` is ignored with a `!.env.example` re-inclusion. A full scan at the v2.8.5 audit found no key-shaped strings and no `process.env` references, and that remains true. |
| `/dashboard` is tracked and never ignored | Not applicable. No `/dashboard` exists. If one is ever added, it is tracked, and no ignore rule may match it. |
| Every ignore entry names something the project produces | Met with one deliberate exception. `brand/` and `tools/build-brand-page.py` both exist locally. `.env*` is preventive rather than descriptive: the project produces no env files and is not expected to. It is kept because the cost of the line is nothing and the cost of one casually committed secret in a public repository is permanent. |
| Ignoring does not untrack | Met and verified, not assumed. `git ls-files -i -c --exclude-standard` returns nothing, so no file is both tracked and matched by an ignore rule. This check matters because adding a rule to `.gitignore` has no effect on a file git is already tracking, which is a common way to believe something is private when it is published. |
| Generated output committed on purpose says why | Met. The nav block in all 12 pages is generated by `tools/build-nav.py` and the output is committed deliberately, because the site has no build step and GitHub Pages serves the repository as-is: an ungenerated nav would mean shipping pages with a placeholder. The rule that the nav is never hand-edited is under Never Do These. |
| Large binaries are kept out of history | **Partly met, by decision.** `audio/womanchild-azqato-remix.mp3` is 6.1 MB and `img/20260711-0151-37.7601512.gif` is 1.9 MB, both committed. The audio is committed on purpose: it is the one same-origin track, the whole point of the native player, and there is nowhere else to put it on a static host. The GIF falls under the standing rule that nothing in `img/` is deleted. Neither is a mistake, but both are permanent in history, and the practical rule going forward is to think before adding another multi-megabyte file rather than to try to remove these. |
| The canonical remote and default branch are recorded | Met. Remote `https://github.com/Azqato/azqato.github.io.git`, default branch `main`. There is no second remote, no fork, and no staging branch. The push is the release. |

> **Discrepancy (resolved 2026-09-28, and the audit's premise was wrong).** There is now a `.gitattributes` at root pinning `* text=auto eol=lf` with explicit `binary` lines for the media types. It shipped as v2.10.2.
>
> **The reason it was needed is not the reason the audit gave, and the difference matters to anyone reading this later.** The audit claimed `music.html` was committed with CRLF while every other text file was LF. That was false. Checked with `git ls-files --eol`, which is the authoritative test, **every committed blob in this repository was already LF**, `music.html` included. The inconsistency existed only in the working tree, where `music.html` and `.vscode/settings.json` sat on disk with CRLF.
>
> What had been keeping the repository clean was `core.autocrlf=true`, a setting in the local git config that silently converted on the way in. That is not part of the repository. A second machine, a CI runner, or a fresh clone with a different setting would have committed CRLF and nobody would have noticed until the diff arrived. So `.gitattributes` did not repair a broken repository; **it made a guarantee portable that was previously an accident of one developer's config.** That is a better reason than the one the audit gave, and it is worth more.
>
> The practical consequence: `git add --renormalize .` produced **zero changes**. The "deliberately noisy 12-file commit" that this section, Open Question 13, and the roadmap all warned about did not happen and was never going to. The sequencing advice built on that prediction cost nothing, but it was advice for a problem that did not exist. The lesson is narrow and worth keeping: **`git status` and editor line-ending indicators describe the working tree, not the repository.** Only `git ls-files --eol` answers what is actually committed.
>
> The note about `tools/build-nav.py` preserving per-file endings was accurate and that code is still there. It is now belt-and-braces rather than a workaround, and it was left alone.

---

# Licensing

`LICENSE.md` lives at the repository root and is never relocated. It was created by the v2.9.9 audit, which found no licence text anywhere in the project.

**The posture is all rights reserved, source-available, not open source.** Every line of this repository is readable because GitHub Pages serves it publicly from the root and being readable is the point. That is not a grant. The full terms, including the sections on AI search, substitution, training data, no waiver, platform terms, third-party content, and the financial disclaimer, are in `LICENSE.md` and are not restated here.

The parts worth knowing without opening the file:

- **Referencing is granted.** Reading, indexing, crawling, quoting with attribution, summarizing, and pointing a reader here, including from an AI assistant's answer, are all explicitly allowed.
- **Substitution is not granted.** Reproducing a page so completely that nobody needs to visit it, or republishing it elsewhere, is not.
- **Training data is not granted by default** and is routed to the request path rather than refused outright.
- **Permission requests go to a public tracker**, `https://github.com/Azqato/azqato.github.io/issues`, so that the request and the answer stay on the record.
- **`robots.txt` is fully open on purpose** and carries a comment saying so, so that a later reader does not mistake it for an oversight and "fix" it. Crawling is granted; copying is not. If the two files ever appear to disagree, `LICENSE.md` is authoritative, and `robots.txt` says that too.

> **Discrepancy (open, the documents disagree with each other).** The README closes with "The source is open. Read it, copy it, or use it as a starting point for your own site," and the External FAQ says "The site and nearly every project on it are open source at github.com/Azqato." Both are invitations to reuse, neither has ever had licence text behind it, and both now contradict `LICENSE.md`. A bare assertion that source is open is not a grant, it is an ambiguity, which is exactly why the default was adopted rather than inferred. This is the one finding in this audit that the owner should settle first, because the two possible answers point in opposite directions: either the permissive intent is real and `LICENSE.md` should be replaced with a real permissive licence, or the reservation is right and those two sentences need rewording. **Resolved 2026-09-28: keep all rights reserved.** The owner confirmed the reservation is what was meant, so the copy was reworded to match the licence rather than the licence rewritten to match the copy. The README now points at this file instead of inviting reuse; the External FAQ separates this site from the individual projects, which are mostly public repositories carrying their own licences; and the press release boilerplate no longer claims everything he builds is open source. Applied as v2.10.0. The audit deliberately did not guess this in advance, because guessing it would have resolved a licensing question by accident.

---

# Social Sharing Tags

**This is a policy record, not a licence to edit page heads.** The audit reads the tags that exist, writes the rule here, and reports any page that does not match it as a discrepancy. Editing a page head is a separate change, made deliberately. That change shipped on 2026-09-28 as Roadmap milestone v2.10.4.

The default below is written for how one chat platform renders a pasted link, which is the strictest common case rather than a preference for that platform: the card is narrow, mobile truncates hard, and the renderer falls back to the title tag or skips the embed entirely when `og:title` and `og:description` are missing. A page that satisfies the strictest renderer satisfies the rest. That matters more here than for most sites, because Discord is where this site's traffic actually comes from.

**Required on every shareable page:**

| Tag | Rule |
|-----|------|
| `og:title` | Per page. Front-loads the distinct part; the first three or four words carry the page, because that is all a reader sees before deciding. No trailing branding, and no colon stacking a subtitle onto a subtitle. Does not repeat the site name: the renderer already prints `og:site_name` as small text directly above it, so repeating it produces visible duplication and spends a third of the budget on something already on screen. Target 60 characters, absolute ceiling 70. |
| `og:description` | Per page. Complete sentences stating what the page actually does, written to end on a full stop rather than to be cut into one, because a sentence truncated mid-word is what makes a card look broken. Tone is educational, pitched at someone who has never been to the site: name the concrete thing the page gives them, because a vague capability claim reads as filler. It is not a restatement of the title; the two fields are two chances to say something, not one thing said twice. Target 150 characters, hard maximum 200. |
| `og:url` | Per page. The absolute `https` URL of that specific page, never a relative path and never the site root. This is the most common failure and it is a silent one: every card still renders, and every one links back to the homepage no matter what was shared. **On this project the canonical domain is `https://azqato.com/`,** decided 2026-09-28; see Open Question 10. No `www` prefix, even though `www.azqato.com` also resolves. |
| `og:type` | `website` on every page. None of these pages is genuinely an article. |
| `og:site_name` | `Azqato`. Maximum 20 characters; this is 6. |
| `twitter:card` | `summary`. See the image rule below for why not `summary_large_image`. |

**Images are off by default.** Do not add `og:image`, `og:image:width`, `og:image:height`, or `og:image:alt`, and set `twitter:card` to `summary` rather than `summary_large_image`, because `summary_large_image` with no image renders an empty or broken frame in some clients. A declared image that does not exist is worse than no image at all, so `og:image` is never added speculatively and never points at a placeholder.

If an image policy is adopted later, these are the requirements that come with it, all of them, not some of them: 1200 by 630 pixels at a 1.91:1 ratio; an absolute `https` URL, because a relative path fails silently; explicit `og:image:width` and `og:image:height` so the card can be sized before the file finishes downloading; PNG or JPG under about 8 MB; an `og:image:alt` under 100 characters; and only then `twitter:card` set to `summary_large_image`. A lion-on-flat-background card is sketched as an idea in `docs/TODO.md`; nothing has been made, so nothing is declared.

**Every description is read from the page, not inferred from its filename.** Same rule this audit applies everywhere else. A description that overpromises is worse than a plain one, because the reader finds out in one click. Where a page already carries an accurate `<meta name="description">`, reuse it for `og:description` rather than inventing a second competing description; where the two differ, say why the difference is deliberate. **No page on this site currently has a meta description at all**, so there is nothing to reuse and nothing to reconcile.

**Deliberately excluded pages: none.** The exclusion list exists so a later reader can tell a decision from an oversight, so it is stated explicitly rather than left empty by accident. This project has no 404 or error page, no mockups, no scratch or work-in-progress files, and nothing marked `noindex`. All 12 pages are in `sitemap.xml`, so all 12 get the tags, including `accounts.html` and `privacy-policy.html`, which are not in the nav but are public, linkable, and indexed.

**Compliance checks.** Recorded so compliance is something run rather than argued about. These read files and report; they do not rewrite them.

1. Every page that should carry the tags has all six.
2. `og:title` is 70 characters or fewer, `og:description` 200 or fewer, `og:site_name` 20 or fewer, with the actual count reported for anything over the target budgets so a person can judge the borderline cases.
3. Every `og:url` is absolute, begins with `https`, and is unique across the site. Duplicate values are a bug, not a style choice.
4. No `og:title` contains the string `Azqato`.
5. Where `og:image` is present, the width, height, and alt tags are present too, its URL is absolute, and the file it names exists in the repository. Where `og:image` is absent, `twitter:card` is `summary`.

> **Discrepancy (open, affects all 12 pages).** **No page carries a single one of these tags.** Verified by reading all 12 files, not inferred: every head holds a `<title>`, a charset, a viewport, and a lion emoji favicon as a data URI, and nothing else. There is no `og:*` tag, no `twitter:*` tag, no `<meta name="description">`, and no `<link rel="canonical">` anywhere in the project. Every link shared to Discord therefore renders as a bare URL with no title card, on the site whose primary call to action is its Discord page. This was blocked on the canonical domain until 2026-09-28.
>
> **Resolved 2026-09-28 as Roadmap milestone v2.10.4.** All 12 pages now carry a meta description, `rel="canonical"`, `og:title`, `og:description`, `og:url`, `og:type`, `og:site_name`, and `twitter:card`. There is no `og:image`, which is the specification's default rather than an omission. The paragraph above describes the state before that change.

---

# Page Titles

**This is a policy record, not a licence to edit titles.** As with Social Sharing Tags, the audit reads the titles that exist, writes the rule here, and reports what does not match. Changing a title is a separate change; it shipped on 2026-09-28 as part of Roadmap milestone v2.10.4.

The shape is **`<unique page name> - <brand>`**, under two limits that measure different things rather than compromising between two opinions:

- **The first 30 characters must identify the page on their own**, without the brand and without the rest of the string.
- **The whole title is 60 characters or fewer.**

Truncation removes from the end, so a title is read at two lengths at once: the first 30 characters are what survives on a tab strip once three or four tabs are open, and the full 60 is what a search result renders. Front-loading the distinct part satisfies both, so there is nothing to trade off. The front budget is 30 rather than 50 because a tab is measured in pixels, not characters, and a title of capitals and wide letters fills the same physical tab as a longer one in lowercase.

- **Front-load the distinct part and put the brand last.** The brand goes last precisely because it is the part that can afford to be lost: a reader looking at the tab already has the favicon in front of them. Brand-first collapses every tab on the site to the same visible string, which defeats the one job a tab title has, and it is the pattern a search engine is most likely to rewrite, because a title led by boilerplate says nothing that distinguishes the page.
- **The homepage inverts this, and only the homepage**, because there the brand is the distinct part, so it leads. A short descriptor after the separator is what tells a stranger reading a search result what the site actually is.
- **Every page's first 30 characters are unique across the site.** Two titles that differ only after character 30 are the same title as far as a tab is concerned, so this is stricter than requiring unique titles, and it is the rule that matters.
- **One separator, chosen once and used on every page.** It costs 3 characters of the budget, so count it. This project adopts `" - "`, which matches the single hyphen the Writing Style section already prefers in titles and headings.
- **No placeholder titles.** "Untitled", "Document", "Home", "index", and framework defaults are failures. Search for them explicitly, since they survive from templates and nobody notices them.
- **The brand appears once, at the end.** No keyword stuffing, and never repeat the brand inside the page name.
- **No emoji**, since the favicon is already the visual marker in that tab, and **avoid all caps in the first 30 characters**, which is the fastest way to spend the pixel budget without spending the character budget.
- **Write every title to survive being read months later with no site around it.** A bookmark saves the title as its name, and the bookmarks bar truncates harder than a tab does. "Overview" is a usable tab title and a useless bookmark.
- **Runtime titles do not apply here.** The rule about a title that must actually change on client-side navigation is recorded because it is the most common failure in this area, but this site is 12 static pages with no router and no single-page application, so every title is set once in the head and that is correct. If a page ever renders titles client-side, each route gets loaded and the resulting title read, rather than the source being read.
- **The title and `og:title` are different fields with different rules, and neither is copied into the other.** The title carries the brand as a suffix, because a tab and a search result have nothing else to say who the site is. `og:title` omits it, because the card already renders the site name directly above. Expect the two strings to differ on the same page. That is deliberate, not a mistake.

**Compliance checks.** These read and report; they do not rewrite.

1. A title exists on every page and is not a placeholder.
2. Every title is 60 characters or fewer, with the actual count reported.
3. The first 30 characters are unique across every page. Report each collision as a pair, since a collision is never one page's fault.
4. The separator matches the one the project uses, on every page that has one.
5. The brand suffix is present on every page except the homepage, and does not also appear inside the page name.

> **Discrepancy (open, affects all 12 pages).** Every title on this site is **brand-first with a pipe separator**, read from the source at the v2.9.9 audit:
>
> | Page | Current title | Length | Verdict |
> |------|---------------|--------|---------|
> | `index.html` | `Azqato \| Welcome` | 16 | Homepage, so brand-first is correct. "Welcome" is close to the placeholder list and tells a stranger nothing. |
> | `about.html` | `Azqato \| About` | 14 | Brand-first. |
> | `projects.html` | `Azqato \| Projects` | 17 | Brand-first. |
> | `invests.html` | `Azqato \| Invests` | 16 | Brand-first. |
> | `music.html` | `Azqato \| Music` | 14 | Brand-first. |
> | `discord.html` | `Azqato \| Discord` | 16 | Brand-first. |
> | `youtube.html` | `Azqato \| YouTube` | 16 | Brand-first. |
> | `codes.html` | `Azqato \| Codes` | 14 | Brand-first. "Codes" does not describe the page, which is AI prompts and coding tools. |
> | `links.html` | `Azqato \| Links` | 14 | Brand-first. |
> | `support.html` | `Azqato \| Support` | 16 | Brand-first. |
> | `accounts.html` | `Azqato \| Accounts` | 17 | Brand-first. |
> | `privacy-policy.html` | `Azqato \| Privacy Policy` | 23 | Brand-first. |
>
> **What passes:** all 12 are well under 60 characters, none is a framework default, the separator is at least consistent, and every full title is unique.
>
> **What fails:** all 12 put the brand first, so every tab truncates to "Azqato | ..." and the pixel budget is spent on the one word that is identical everywhere and already shown by the favicon. The separator is `|` rather than the adopted `" - "`. Two page names, "Welcome" and "Codes", do not identify their page to a stranger. Technically the first 30 characters are unique here only because the titles are short enough that the whole string fits; the rule's intent still fails, because the first nine characters of all 12 are the same.
>
> **Resolution: applied 2026-09-28.** The owner decided to fix the titles in the same pass as the sharing tags, and both shipped as Roadmap milestone v2.10.4. Every title is now page-first with a `Name - Azqato` suffix, the longest is 38 characters against a 60-character budget, and no two share their first 30 characters. The table above records the state before the change. See v2.10.4 for the replacements as shipped.

---

# Security Model

## Authentication model

There is none, by design. The portfolio is a fully public, read-only static site. No user accounts, no login, no sessions, no cookies, no password reset, no email.

The only privileged access is the GitHub repository, protected by Azqato's GitHub account credentials with two-factor authentication. Repository write access is what controls who can change the site and trigger a deployment. There is no separate deploy credential, no CI secret, and no hosting-provider login in the path for a normal change.

## Authorization model

Two roles exist:

| Role | Can | Cannot |
|------|-----|--------|
| Visitor (everyone) | Read every page, follow every link | Change anything, submit anything, see anything another visitor did |
| Owner (repository write access) | Push to `main`, which deploys; force-push; change hosting settings | n/a |

There is no admin interface, no moderation surface, and no content that differs between visitors.

## Data storage

The portfolio stores no user data. No database, no server-side storage, no cookies, no localStorage, no sessionStorage, no IndexedDB. There is nothing to breach and nothing to export.

Static content hardcoded into the HTML (project metadata, affiliate URLs, bio copy) is public by design and contains no information about visitors. Both hosts log standard web server access data as part of their infrastructure; that is outside the site's control and is governed by Cloudflare's and GitHub's own privacy policies. `azqato.com` runs on Cloudflare Pages, so in practice almost all of it sits with Cloudflare.

## Environment variables

There are none. No `.env` files, no API keys, no tokens, no credentials anywhere in the codebase, and no variables that a deploy needs to have set.

Confirmed at audit: a full scan found no key-shaped strings, no `process.env` references, and no secret material. `.gitignore` pre-emptively excludes `.env*` so that a future secret cannot be committed casually. The wrangler-specific patterns that sat beside it were removed in v2.8.9 along with the config they belonged to.

Affiliate URLs and referral codes are hardcoded as `href` attributes. They are public referral links, not secrets: they identify Azqato as the referrer and are meant to be shared.

| Variable | Required | Purpose |
|----------|----------|---------|
| (none) | n/a | The project defines and consumes no environment variables |

## Third-party trust

Every third party that receives visitor data, and what it receives:

| Service | Data it receives | Trigger |
|---------|------------------|---------|
| Cloudflare Pages | IP address, user agent, referrer, requested path, for every request to `azqato.com` | Automatic, every page |
| GitHub Pages | The same, for every request to `azqato.github.io` | Automatic, every page on that address |
| Mixcloud | IP address, user agent, and the referring page URL, plus any cookies or storage its own widget sets inside its frame | Automatic, on every `music.html` load |
| Every linked destination | Whatever a normal outbound click sends, plus the referral code where one is embedded | Only on click |

The Mixcloud embeds are the only automatic third-party data flow on the site, and they are the reason the privacy claim in the README says "the only parts that reach outside the page are the two embedded music players" rather than the older, and inaccurate, blanket claim of zero external requests.

## Known attack surface

**Cross-site scripting.** `projects.html` builds card HTML with template literals and assigns it via `innerHTML`. Every interpolated value comes from the hardcoded `PROJECTS` array, which only the repository owner can edit, so there is no injection path from a visitor. This becomes a live vulnerability the moment any value comes from outside the file: if the GitHub API integration on the roadmap ships, every API-sourced string must be escaped or inserted with `textContent` before it goes near `innerHTML`.

**Third-party iframe.** The two Mixcloud iframes are the only foreign code executing on the site. They carry `allow="encrypted-media; fullscreen; autoplay; idle-detection; speaker-selection; web-share;"`, which is broader than a music player strictly needs (`idle-detection` in particular has no plausible use here and reports whether the visitor is at their keyboard). They have no `sandbox` attribute. Tightening the `allow` list and adding a `sandbox` would reduce this surface at no cost to the player.

**Affiliate link integrity.** Affiliate URLs are hardcoded and never validated at runtime. A wrong or hijacked URL would be invisible to the site and visible only to the visitor. Mitigation is process: review every change to `support.html` before pushing, and click each link monthly (see Monitoring).

**Local test tooling.** `test-local-audio.bat` launches Chrome with `--disable-web-security`. That is a genuinely dangerous flag: a browser started that way ignores same-origin policy for every site it visits, not just `music.html`. It is mitigated by the throwaway `--user-data-dir` and by the comment in the file telling the user not to browse with that window. It is untracked and therefore never deployed. Do not remove those two mitigations, and do not commit the file.

**Content Security Policy.** None is set. **The reason changed on 2026-09-29 and the old one no longer holds.** This used to say a CSP was impossible because GitHub Pages cannot send custom response headers. That is still true of `azqato.github.io`, but the canonical domain runs on Cloudflare Pages, which supports a `_headers` file, so a CSP on `azqato.com` is perfectly possible and simply has not been written. It remains acceptable to go without on a static site with no user input, and the practical benefit would still be limited to constraining the Mixcloud frame, which is itself scheduled for removal in v2.9.0. The difference is that this is now a choice.

**Dependency vulnerabilities.** Zero. There are no packages, no lockfile, and no CDN scripts to compromise.

**Supply chain.** The one indirect dependency is the shader code copied into `music.html` from public sources under CC0, MIT, and CC-BY-NC-SA licenses. It is inert graphics code that runs on the GPU with no access to the page, and it was reviewed when pasted. Note that the CC-BY-NC-SA-4.0 mode (Vortex) carries a non-commercial clause, which is worth knowing if the site ever carries paid advertising.

## Dependency policy

Current state: zero dependencies, and that is a tenet, not an accident.

If a dependency is ever added: prefer well-maintained packages with a clear security disclosure process; pin to an exact version; run `npm audit` before committing; never load a CDN script without a Subresource Integrity hash; and review anything that touches the DOM or handles data. Adding the first dependency also means adding a lockfile, a `package.json`, and a review cadence that does not currently exist, which is part of the cost.

---

# Deprecation and Removal

## Removal policy

The project had no stated removal rule before this audit. The default is adopted and written in here as policy. Where the project later develops its own practice, that practice wins and this section should record it instead.

**Whether a removal needs a redirect is decided by whether the thing being removed is public facing, not by the fact that it is being removed.**

- **Public facing:** the deployed artifact and the addresses it serves. On this project that means every URL under `https://azqato.com/`, the canonical domain since 2026-09-28, and equally under `https://azqato.github.io/`, which still serves the same files, that a person or another site can link to: each `.html` page, `styles.css`, and each file in `img/`. Removing one retires an address that something outside this repository may point at, so it gets a compatibility entry that keeps the old address resolving to whatever replaces it.
- **Internal:** anything not reachable from outside. A CSS class, a JavaScript function, an entry in the `PROJECTS` array, a section of a page, an unused image that nothing has ever linked. Removing one is a plain delete: no redirect, no alias, no stub, no tombstone. Nothing external points at it, so there is no address to preserve, and a permanent compatibility entry would be maintenance in exchange for nothing.

**Where the deploy boundary sits on this project:** everything in the repository root and in `img/` is deployed and is therefore public facing. There is no build step, so there is no separate "source" that compiles into something else; the source files *are* the artifact. This makes the line unusually simple here, and it also means the usual escape hatch ("it is only source") does not apply: deleting `codes.html` deletes a live URL.

`/docs`, `README.md`, `.githooks/`, and `.vscode/` sit on the public side of that line in the sense that GitHub serves the repository publicly, but they are documentation and tooling rather than site addresses. Removing or renaming a document is an internal change and needs no redirect. It does need a patch note.

**The redirect mechanism.** This project has no router, no server, and no rewrite rules, so it cannot redirect the way a dynamic site can. What it has instead is a one-file HTML redirect, and that is what a compatibility entry means here:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="0; url=new-page.html" />
  <link rel="canonical" href="https://azqato.com/new-page.html" />
  <title>Moved</title>
</head>
<body>This page moved to <a href="new-page.html">new-page.html</a>.</body>
</html>
```

The old filename stays in place carrying that content. It costs one small file and it keeps every existing inbound link working, including links posted in Discord years ago, which is the actual failure mode this guards against for a site whose traffic arrives through chat messages and video descriptions.

First used in v2.11.0 for invests.html. The first time it is, follow the rule above rather than deciding fresh.

## Public surface

Specific enough to answer the question for any given file:

| Address | Type | Notes |
|---------|------|-------|
| `/` and `/index.html` | Page | Default entry point |
| `/about.html` | Page | |
| `/accounts.html` | Page | Not in nav; linked from `index.html` and `links.html` |
| `/codes.html` | Page | |
| `/discord.html` | Page | |
| `/invests.html` | Redirect page | To `/invests/` since v2.11.0 (compatibility entry) |
| `/invests/` and its 21 pages | Pages | Azqato Invests; listed in invests/sitemap.xml |
| `/links.html` | Page | |
| `/music.html` | Page | |
| `/privacy-policy.html` | Page | Not in nav; linked from `links.html` |
| `/projects.html` | Page | |
| `/support.html` | Page | |
| `/youtube.html` | Page | |
| `/styles.css` | Asset | Linked by all 12 pages; renaming it breaks every page at once |
| `/audio/womanchild-azqato-remix.mp3` | Asset | Referenced by `music.html`. Directly linkable and hotlinkable, so treat the path as public. |
| `/img/about-profile.jpg` | Asset | Referenced by `about.html` |
| `/img/yt-thumb-azqato.jpg`, `-streams`, `-mixes`, `-chills` | Asset | Referenced by `youtube.html` |
| `/img/home-hero-profile.jpg`, `logo-cat-avatar.jpg`, `music-logo-small.jpg`, `music-playlist-bangers.jpg`, `music-playlist-addictions.jpg`, `yt-channel-azqato.jpg`, `yt-channel-streams.jpg`, `yt-channel-mixes.jpg`, `yt-channel-chills.jpg`, `20260711-0151-37.7601512.gif` | Asset | Deployed but referenced by nothing in this repository. Treat as public facing anyway if anything outside this repository might hotlink them; treat as internal if not. Unknown, and worth a moment's thought before deleting rather than an assumption. |
| `/README.md`, `/docs/*.md` | Document | Served as raw files, not rendered. Not linked from any page. |
| `/.gitignore` | Config | Served if requested; harmless, contains no secrets |
| `/tools/build-nav.py` | Tooling | Served as a plain text file if requested. Not linked from anywhere, contains no secrets, and is never executed by the host. |
| `/.vscode/*`, `/.githooks/*` | Config | Probably not served: GitHub Pages runs Jekyll by default, which excludes dot-directories from its output, and there is no `.nojekyll` file in this repository. This has not been verified against the live site. If it matters, request `https://azqato.github.io/.vscode/recentfedsummary.MD` and see whether it returns 404. |

**Not part of the public surface:** every CSS class, every JavaScript function and variable, every entry in `PROJECTS`, and every section of markup inside a page. These can be renamed or deleted freely.

## Compatibility entries

- `/invests.html` (v2.11.0): a one-file redirect page to `/invests/`, plus `_redirects` rules on Cloudflare Pages so `/invests` and `/invests.html` reach `/invests/` in one hop.

When one is created, it is:

- **Permanent.** A compatibility entry is never removed on the grounds that "nobody uses it any more", because the traffic it serves is invisible from here.
- **Never chained.** A redirect resolves to a real page in one hop. If the target later moves, the original redirect is repointed at the new final destination rather than at the second redirect.
- **Never reused.** A retired address is never later pointed at unrelated content. A reused address silently serves the wrong thing, which is worse than a broken link, because the visitor has no way to tell.

## Retired items

Nothing public facing has ever been removed from this site. The internal removals below are recorded so a reader who finds a reference to one can resolve it. Historical patch notes and version-history rows describing these are left exactly as written, because they record what happened at the time rather than describing the current state.

| Item | Removed in | What replaced it |
|------|-----------|------------------|
| Spotify playlist cards on `music.html` | v2.8.0 era | YouTube embeds, then the Mixcloud embeds and platform links in the stage console |
| Five outer/wing stage screens (`drawOuterScreen`) on `music.html` | v2.8.0 | The three-screen layout (one center, two wings) |
| Julia, Plasma, Mandelbrot, Newton, and Burning Ship canvas fractal modes | v2.8.0 | The nine WebGL shader modes |
| `drawULogo` (truss-mounted wordmark) on `music.html` | v2.8.1 | The wordmark on the DJ booth fascia |
| `drawTriangle` (laser triangle overlay) on `music.html` | v2.8.1 | Nothing; deleted outright |
| The animated LED mixer grid on the DJ booth | v2.8.1 | A static mixer panel |
| `.mixcloud-embed` and `.platform-grid` blocks on `music.html` | v2.8.3 | `.stage-console` |
| Per-page duplicated tokens, reset, nav, and footer CSS | v2.7.0 | `styles.css` |
| The GitHub and Tools external links in the top nav | v2.6.x | Cards on `codes.html` |
| The lightning bolt favicon | v2.6.x | The lion emoji favicon |
| Seven separate documentation files (TRD, TENETS, PRFAQ, SECURITY, RUNBOOK, METRICS, ROADMAP) | v2.5.0 | Consolidated into this file as top-level sections |

---

# Product Tenets

These are the guiding principles for every decision made on this project. When two options conflict, the tenet higher on this list takes priority.

## 1. Speed Is a Feature; Everything Else Is Optional

A page that loads in under a second with five project cards is more valuable than a page that loads in three seconds with ten. Every addition (a library, a font, a third-party widget) must pay for itself in load time. If it cannot, it does not ship.

Applies when: debating whether to add a dependency, a new CDN resource, or a feature that requires external data. Note the one place this tenet has already lost: `music.html` is 112 KB and loads two third-party iframes, because the music page's whole job is to be an experience rather than a document. That was a deliberate trade, and it is the only one.

## 2. No Dependencies by Default

The default answer to "should we use a library for this?" is no. Vanilla HTML, CSS, and JavaScript handle everything this portfolio needs. Dependencies rot, carry vulnerabilities, and create maintenance burden. The burden of proof is on adding a dependency, not on avoiding one.

Conflict note: this tenet will conflict with Tenet 3 (low maintenance). When a library would genuinely reduce ongoing manual work, prefer the no-dependency solution unless the maintenance cost is severe and sustained.

## 3. The Owner Must Be Able to Maintain This in Five Minutes

Adding a project, updating an affiliate link, updating a Discord server card, or changing the theme should never require reading documentation. If the codebase reaches the point where the owner has to look something up to make a routine edit, it has grown too complex. Simplicity for the maintainer is a hard constraint, not a preference.

The nav is the worked example. For months every proposed fix lost to copy and paste: a JS-injected nav makes a routine edit harder to reason about and breaks the page without JavaScript, and a real build step puts a toolchain between the source and the artifact. What finally won in v2.8.8 was a stamp script whose output is committed, because it adds a convenience without adding a dependency. The repository still holds complete readable HTML, and deleting the script costs nothing but the convenience.

## 4. Transparency Before Conversion

The affiliate and support features exist to fund the work, but they must never obscure what the portfolio is. The affiliate disclosure appears above the fold. Links are clearly labeled. Nothing is disguised as editorial content, and no promo badge claims a benefit that has not been verified.

Applies to: every decision on the Support page (disclosure placement, button copy, card descriptions), and to the financial disclaimer on `invests.html`.

## 5. Look Like a Developer Built It

The portfolio must look at home on GitHub. Dark backgrounds, tight information density, accent colors that signal "interactive", and no stock photography. The aesthetic communicates technical competence before the visitor reads a word.

Applies when: making visual design decisions. Loses to Tenet 1 and Tenet 2 if achieving a visual goal requires a framework or a blocking resource.

## 6. Say What Is Actually True

Applies to site copy, promo badges, and these documents equally. If the visualizer does not react to audio, the documentation says so. If a page breaks the page-weight budget, the number is written down rather than the target being quietly restated. If an affiliate program's terms are unverified, the card describes the service rather than promising a bonus. A confident sentence outlives the session that produced it, and a wrong one costs more than the vagueness it replaced.

This tenet is last because it never conflicts with the others; it constrains how the other five are reported.

---

# Operational Runbook

Everything a developer needs to run this project from a cold start. The README deliberately carries none of it.

## Prerequisites

| Requirement | Version needed | Notes |
|-------------|----------------|-------|
| Git | Any modern version (2.x) | The only hard requirement |
| A modern browser | Chrome, Firefox, Edge, or Safari, current | For viewing and for DevTools |
| A text editor | Any. VS Code is what the repository is configured for (`.vscode/settings.json`) | No extensions required |
| Python 3 | Needed only to change the nav | Runs `tools/build-nav.py`, and `python -m http.server` for a local server. Standard library only, no packages. Any Python 3 version works. |
| Node | Optional | Only as an alternative local server via `npx serve`. Nothing in the project requires it. |

There is no runtime to install. No Node version is required, no package manager is required, and there is no `package.json`.

## Local setup

From a completely fresh machine:

```bash
git clone https://github.com/Azqato/azqato.github.io.git
cd azqato.github.io
git config core.hooksPath .githooks
```

The third command is not optional in practice: it enables the `pre-commit` writing-style guard. Git does not carry hook configuration in a clone, so this must be run once per clone or the em-dash policy is unenforced.

Then open the site. There is nothing to install and nothing to compile:

```bash
# Option A: open index.html directly. Works fully; every page is file:// safe.
# Option B: serve it, which avoids file:// quirks in some browsers.
npx serve .            # http://localhost:3000
python -m http.server  # http://localhost:8000
```

No required port. No configuration file to copy. No environment variables to set.

Two caveats for `music.html` on `file://`. The Mixcloud iframes still load (they are absolute HTTPS URLs) but some browsers restrict iframe behavior on local files. More importantly, the native track cannot drive the visualizer from a local file: the browser treats the same-folder mp3 as cross-origin, so the page deliberately skips Web Audio and falls back to the synthetic signal. The audio is audible, but the reaction is not real. **Use Option B for any work on the audio path**, and never judge the visualizer's reactivity from a `file://` load.

> **Discrepancy (resolved in favor of the code).** Before this audit both the README and this runbook gave the clone command as `git clone https://github.com/Azqato/Azqato.git` followed by `cd Azqato`. That is not the repository. The actual remote, read from `git remote -v`, is `https://github.com/Azqato/azqato.github.io.git`, which is the GitHub user-site repository that serves `azqato.github.io`. The old command would fail or clone the wrong thing.

## Build

There is still no build step. The source files are the deployed files. Nothing is compiled, bundled, minified, or transformed at any point between the editor and the browser, and no command has to run before a deploy.

One optional generator exists. `tools/build-nav.py` stamps the shared nav into every page, and its output is committed like any other edit. It is not a build step in the sense the project has avoided: the repository always contains complete deployable HTML, nothing sits between the source and the browser, and if the script were deleted the site would keep working and the nav would go back to being edited by hand. Run it only when the nav changes:

```bash
python tools/build-nav.py           # rewrite the nav in all 12 pages
python tools/build-nav.py --check   # report drift, write nothing, exit 1 if any
```

Running it with no nav change prints `nav is up to date in every page` and writes nothing, which doubles as a check that all 12 navs still match.

The closest thing to a build check is confirming page weight before pushing:

```powershell
Get-ChildItem *.html | Select-Object Name, Length | Sort-Object Length -Descending
```

Target: under 50,000 bytes per page. `music.html` is knowingly over at 114,680 bytes (112 KB); every other page should stay under. Images in `img/` have no enforced target; keep new ones under 500 KB, and note that four existing thumbnails already exceed that.

## Deploy

### Production: two deployments, not one

**Corrected 2026-09-29, and this had been wrong in every version of this document.** This project is served by **two independent static hosts**, both building from the root of `main`:

| | `azqato.com` (canonical) | `azqato.github.io` |
|---|---|---|
| Host | **Cloudflare Pages** | GitHub Pages |
| Triggered by | a push to `main` | a push to `main` |
| URL shape | extensionless; `/page.html` 307s to `/page` | both `/page` and `/page.html` return 200 |
| Analytics beacon | yes, injected at the edge | no |
| 404 | empty body | GitHub's standard 404 page |
| Custom response headers | **supported**, via a `_headers` file | not supported |

**The two are siblings, not a proxy and an origin.** Every earlier version of this document, and the whole `CNAME` milestone, assumed Cloudflare sat *in front of* GitHub Pages as a caching proxy. It does not. They are separate builds of the same commit, and neither knows about the other. Everything that followed from the proxy assumption was wrong, including the deploy-verification rationale and the entire risk analysis for the `CNAME` file. See the note under Deploy verification, and Roadmap v2.10.3.

**How this was established**, since none of it is visible in the repository: `azqato.com` resolves to Cloudflare IPs (`104.21.8.156`, `172.67.188.142`) on Cloudflare nameservers, returns `cfOrigin;dur=0` on every request (it never contacts another origin), and serves an empty 404, while `azqato.github.io` returns `Server: GitHub.com` with GitHub's own 404 page. The owner confirmed it directly on 2026-09-29: "I use Cloudflare Pages instead of GitHub."

**A capability this unlocks.** Cloudflare Pages supports a `_headers` file, so the long-standing "no CSP is possible on this host" constraint is **false for the canonical domain**. It was true when the only host was GitHub Pages. Nothing has been added; the constraint is simply no longer a hard one, and it is now a decision rather than a limitation. See the Security Model.

One-time setup, recorded only in case it is ever lost:

1. The repository is named `azqato.github.io`, which makes it a GitHub user site, serving `https://azqato.github.io/` from `main` at `/root`.
2. A Cloudflare Pages project builds the same repository and serves `https://azqato.com/` and `https://www.azqato.com/`. Its configuration lives in the Cloudflare dashboard, not in this repository, which is why nothing here describes it.
3. Both are live within roughly 60 seconds of a push, independently of each other.

Routine deploy, which is the entire process:

```bash
git add <changed files>
git commit -m "Description of change"
git push origin main
```

There is no staging environment, no approval gate, and no CI. A push to `main` is a production release. Treat it that way: read the diff before pushing.

**Deploy verification. Check `azqato.com`, and know that it does not vouch for the other host.**

> **Corrected 2026-09-29.** This step used to say to check `https://azqato.github.io/` *instead of* `azqato.com`, reasoning that the `github.io` address was "the origin" and that Cloudflare merely cached in front of it. That reasoning was built on a false model of the hosting. The two are independent deployments, so **a successful GitHub Pages build is not evidence that Cloudflare Pages built anything at all.** The old check could have passed while the canonical domain, where the visitors are, sat on a failed build.

Verify after every deploy by opening `https://azqato.com/` with a cache-busting query string, or hard-refreshing with Ctrl+Shift+R, and confirming the change is visible. That is the domain that matters. If the change is missing after two minutes, check the Cloudflare Pages dashboard for a failed build.

Check `https://azqato.github.io/` as well when the change has to be right on both, and check the repository's Actions tab and the Pages section of Settings if that one is stale. Each host reports only on itself.

If the push is rejected because the remote has moved ahead (this happens occasionally, for example when an automated integration opens a pull request):

```bash
git pull --rebase origin main
git push origin main
```

### Alternative hosts

The site can move to any static host in minutes, with no configuration changes, because there is nothing to configure.

| Host | Steps |
|------|-------|
| Cloudflare Pages | Connect the repository; leave the build command blank; output directory `/` |
| Vercel | Drag and drop the project folder at vercel.com/new; no build command |
| Netlify | Drag and drop at app.netlify.com/drop |

## Rollback

**Option A: revert the last commit. Safe, and the default choice.**

```bash
git revert HEAD
git push origin main
```

Creates a new commit undoing the last change. Pages redeploys within roughly 60 seconds. History is preserved, which matters here because the patch notes reference commits.

**Option B: revert a specific older commit.**

```bash
git log --oneline           # find the hash
git revert <hash>
git push origin main
```

**Option C: restore one file from an earlier state.**

```bash
git checkout <hash> -- support.html
git commit -m "Restore support.html to <hash>"
git push origin main
```

**Option D: reset to a known-good commit. Destructive; use only when reverting many commits at once.**

```bash
git reset --hard <hash>
git push --force-with-lease origin main
```

`--force-with-lease` rather than `--force`, always, so a concurrent push is not silently destroyed.

There is no way to roll back faster than the GitHub Pages deploy cycle, so the realistic worst case is roughly two minutes of a broken page. There is no traffic volume at which that is unacceptable, which is why no faster mechanism exists.

## Environments

| Environment | URL | Branch | Deploy trigger | Differences |
|-------------|-----|--------|----------------|-------------|
| Production | `https://azqato.com/` (origin: `https://azqato.github.io/`) | `main` | Push to `main` | The only real environment |
| Local | `file://` or `localhost:3000` | Any | Open in a browser | Identical output. The only behavioral difference is browser handling of `file://` iframes on `music.html`. |

Nothing differs between environments: no feature flags, no environment variables, no build modes, no conditional code paths anywhere in the source.

> **Resolved in v2.8.9.** This section previously stated "There is only one environment: production (GitHub Pages)", while `wrangler.jsonc` sat in the repository describing a complete Cloudflare Workers deploy target. It arrived 2026-07-09 via the only pull request in the repository's history, from a Cloudflare autoconfiguration integration, and was never used for a real deploy. It has been deleted. There is again exactly one *environment*, in the sense of one branch and no staging. **Corrected 2026-09-29:** that one environment is served by **two hosts**, Cloudflare Pages and GitHub Pages, so "production (GitHub Pages)" was still not the whole truth. Moving hosts needs no configuration file in this repository, so nothing was lost by deleting `wrangler.jsonc`. Note the irony worth recording: the deleted file was a Cloudflare deploy target, dismissed as residue from an autoconfiguration integration, at a time when Cloudflare was already serving the canonical domain and nobody had noticed. It was still the right file to delete, because Workers is not what serves the site, but the reasoning that it was unrelated to anything real was luck rather than judgement.

## Environment variable reference

| Key | Required | Purpose |
|-----|----------|---------|
| (none) | n/a | The project defines, reads, and requires no environment variables in any environment |

`.gitignore` excludes `.env*` and `.dev.vars*` defensively so that a secret introduced later by tooling is not committed by accident.

## Common errors

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Site shows the old version after a push | GitHub Pages CDN cache | Hard-refresh (Ctrl+Shift+R). Allow 2 to 5 minutes for full propagation. |
| 404 on azqato.github.io | Pages disabled, or the wrong branch selected | Settings, Pages, Source: `main` / `root` |
| `commit blocked: em dash found` | The pre-commit guard caught a prohibited character | Replace it per the Writing Style table. Only use `--no-verify` if the character is genuinely required by the text. |
| The pre-commit guard never fires | `core.hooksPath` is not set in this clone | `git config core.hooksPath .githooks` |
| Push rejected, non-fast-forward | The remote has commits you do not | `git pull --rebase origin main`, then push |
| Affiliate card shows the wrong promo | Outdated hardcoded text | Edit the `.affiliate-promo` span on that card in `support.html` |
| Discord Join button does nothing | `href="#"` placeholder never replaced | Set the real invite URL on that card's `.btn-join` anchor |
| Filter bar shows an unexpected tag | A new project introduced an unintended `tags` value | Check the `tags` array on the newest entry in `PROJECTS`; the bar is generated from the union of all tags |
| Project count is wrong or the grid is empty | A syntax error in the `PROJECTS` array | Open DevTools Console; a trailing-comma or quote error stops `render()` before it writes the grid |
| `iconUrl` image does not load | The URL is unreachable or blocked cross-origin | DevTools Network tab; use an absolute URL on a stable host |
| `music.html` shows a plain grid instead of shaders | WebGL2 unavailable, or a shader failed to compile | DevTools Console; look for `GL shader err:`. The fallback is intentional. |
| `music.html` is sluggish | The unthrottled render loop on an underpowered GPU | No mitigation exists today. This is the reason a pause control is on the future list. |
| Page weight over 50 KB | Too much inline content added | DevTools Network tab, or the PowerShell size command above |
| A nav item is missing on one page | The nav was hand-edited instead of stamped | `python tools/build-nav.py --check` names the page, then `python tools/build-nav.py` repairs it |

## Monitoring

All monitoring is manual. There is no uptime check, no error reporting, no log aggregation, and no alerting, because there is no server to produce logs and no code path that can throw for a visitor.

| What to check | Where | Cadence |
|---------------|-------|---------|
| Site availability | Visit `https://azqato.com/` | Spot-check as needed |
| GitHub Pages status | `githubstatus.com` | If the site appears down |
| Deploy status | GitHub, repository, Settings, Pages (and the Actions tab) | After each push |
| Console errors | DevTools Console on the changed page | Before a major update ships, not after every edit; see Testing Cadence |
| Affiliate link validity | Click each link on `support.html` | Monthly |
| Discord invite validity | Click each invite on `discord.html` | Monthly |
| External resource links | Spot-check the `invests.html` hub; it has the most links and the highest rot rate | Quarterly |
| Traffic and referrers | GitHub, repository, Insights, Traffic | Monthly |
| Page weight | DevTools Network, or the PowerShell command in Build | After major changes |
| Lighthouse score | Chrome DevTools, Lighthouse panel | Quarterly |

---

# Metrics

## North star metric

**Monthly unique visitors to `azqato.com`.** It is the single number that best represents whether the site is doing its job, because every goal the site has (route people to Discord, show the projects, surface the tools, enable support) begins with someone arriving.

Its weakness is worth stating plainly: this number can only be approximated from GitHub's traffic insights, which count repository views rather than site views and retain only 14 days of daily data. The metric is directionally useful and precisely wrong. **Note added v2.9.9:** Cloudflare Web Analytics is in fact running on `azqato.com` and does hold real page-level visit counts, which were never taken into account when this metric was designed. Whether to start reading them, and whether this metric should be redefined around them, is unresolved and is not part of the v2.9.9 decisions.

## Acquisition metrics

| Metric | Measurement method | Target |
|--------|--------------------|--------|
| GitHub profile referral clicks | GitHub Insights, Traffic, Referrers | Trend upward |
| Social and community referrals | GitHub Insights, Traffic, Referrers | Discord and YouTube should be the top two sources |
| Repository clone count | GitHub Insights, Traffic, Clones | Informational only |

## Engagement metrics

| Metric | Measurement method | Target |
|--------|--------------------|--------|
| Support page visit rate | GitHub Insights, Traffic, per-page views | Over 10% of total visits |
| Discord page visit rate | GitHub Insights, Traffic, per-page views | Trend upward |
| Discord server joins | Discord server insights, per server | Attributed loosely; the site is one of several sources |
| Mix plays | Mixcloud dashboard, per mix | Informational; cannot be attributed to the site specifically |
| Affiliate link clicks and conversions | Each partner's own dashboard | At least 1 conversion per month |
| Buy Me a Coffee contributions | Buy Me a Coffee dashboard | At least 1 per month |

## Retention metrics

The site cannot measure retention, and this is a real gap rather than an oversight to be papered over. Returning visitors are indistinguishable from new ones without cookies or analytics, both of which are excluded by the PRD.

The proxies available, in descending order of usefulness:

| Proxy | Where | What it tells you |
|-------|-------|-------------------|
| Discord server member count and retention | Discord server insights | Whether the community the site routes to is sticky |
| Repeat traffic spikes after content drops | GitHub Insights, Traffic | Whether an audience returns when there is a reason to |
| Recurring Buy Me a Coffee supporters | Buy Me a Coffee dashboard | The strongest available signal of genuine retention |

## Performance metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Page weight, any page | Under 50 KB | DevTools Network tab |
| First Contentful Paint | Under 1.0 second | Chrome Lighthouse or PageSpeed Insights |
| External HTTP requests | 0 on page load, except the 2 Mixcloud frames on `music.html` and 1 image on `projects.html` | DevTools Network tab |
| Console errors | 0 on every page | DevTools Console |
| GitHub Pages uptime | Over 99.9% | `githubstatus.com` and manual checks |

## Targets

| Metric | Target | Timeframe |
|--------|--------|-----------|
| Monthly unique visitors | 500+ | 3 months post-launch |
| Monthly unique visitors | 2,000+ | 12 months post-launch |
| Support page visit rate | Over 10% of site visits | Ongoing |
| Buy Me a Coffee contributions | At least 1 per month | 3 months post-launch |
| Affiliate conversion | At least 1 per month | 6 months post-launch |
| Documentation accuracy | Every page and feature covered in `/docs` | Every audit |

## Reporting cadence

| Category | Frequency | Notes |
|----------|-----------|-------|
| Traffic | Monthly | GitHub Insights retains 14 days of daily data, so check at least fortnightly to avoid losing detail |
| Affiliate performance | Monthly | Log into each of the seven partner dashboards |
| Buy Me a Coffee | Monthly | The dashboard shows monthly and all-time totals |
| Link validity | Monthly for affiliates and Discord invites, quarterly for the `invests.html` hub | Manual clicking |
| Lighthouse | Quarterly, or after any major change | Run manually |
| Page weight | Every push | Flag anything over 45 KB before it crosses 50 |

---

# Roadmap

## Current phase

**Native audio on `music.html`, then polish.**

The site is feature-complete against its original goals: all 12 pages are live, the project grid is populated, the affiliate and support paths work, and the design system is stable. The shared-assets milestone closed in v2.8.8, and the v2.8.5 audit's open questions largely closed in v2.8.9. The v2.9.9 audit reopened that position: six decisions are now waiting on the owner, the largest being which domain is canonical. See Open Questions 6 and 9 through 14, and `docs/TODO.md`.

v2.8.10 delivered the half of v2.9.0 that matters most: one same-origin track now plays on `music.html` and drives the visualizer through a real analyser. v2.9.1 then made that reaction convincing, verified by measurement rather than by eye. What remains of v2.9.0 is the replacement half, and it is gated on audio files rather than on code. The Mixcloud embeds are still there, deliberately, because the owner has supplied one track and the embeds carry the rest of the catalog. They come out when enough standalone files exist to cover it.

The next substantial piece of work is v2.9.0: replacing the Mixcloud embeds with audio served directly by the page, which merges the finished native player branch and makes the visualizer genuinely audio-reactive. It is waiting on the owner's audio files rather than on engineering.

Everything else outstanding is defect work that needs no decisions and can happen in any order:

| Item | Why it matters | Size |
|------|----------------|------|
| Optimize the four `youtube.html` thumbnails | 2.3 MB of images on a 7.8 KB page, with no `loading="lazy"`. The worst performance defect on the site, and a direct contradiction of Tenet 1. | Small |
| Add `build-nav.py --check` to the pre-commit hook | Makes nav drift uncommittable, finishing what v2.8.8 started | Small |
| Pause the render loop on `document.hidden` | Battery and heat. Reuses the `setPlaying()` function that already exists. | Small |
| Playwright smoke tests | The threshold set for adding these was 11 pages; the site has 12. Overdue rather than deferred. | Medium |
| Mobile audit of `music.html`, 320 px to 480 px | Never done. The fixed canvas and console were tuned for desktop. | Medium |

Beyond that: adding projects and links as they exist, and occasional visual passes on individual pages.

## Milestone table

| Milestone | Name | Target | Status |
|-----------|------|--------|--------|
| v1.0.0 to v2.6.x | Launch through content build-out | 2026-06 | Complete |
| v2.7.0 | Code extraction and shared assets | 2026-07 | Complete (CSS v2.7.0, nav v2.8.8) |
| v2.8.x | Music page and visualizer | 2026-07 to 2026-08 | Complete |
| v2.8.5 | Full documentation audit | 2026-08-24 | Complete |
| v2.8.7 | Reduced motion support | 2026-08-29 | Complete |
| v2.8.8 | Nav stamped from one source | 2026-08-29 | Complete |
| v2.8.9 | Open questions cleared, dead link fixed | 2026-08-29 | Complete |
| v2.8.10 | One native track, real audio-reactive visualizer | 2026-08-29 | Complete |
| v2.9.1 | Reaction tuning: make the kick actually land | 2026-08-30 | Complete. Measured at 124 BPM against the track |
| v2.9.2 | Band mapping fix, visible degraded state | 2026-08-30 | Complete |
| v2.9.3 | WCAG 2.3.1 flash rate fixed, artist credit | 2026-08-30 | Complete |
| v2.9.4 | Screens stop pulsing, second frame-count bug fixed | 2026-08-31 | Complete |
| v2.9.7 to v2.9.8 | Automate Fundamentals added, private-repo link rule adopted | 2026-09-28 | Complete |
| v2.9.9 | Full documentation audit | 2026-09-28 | Complete |
| v2.10.0 | Licensing and analytics copy alignment | 2026-09-28 | Complete. Applied at the audit |
| v2.10.1 | Nav generator: drop the dead `SKIP` set | 2026-09-28 | Complete |
| v2.10.2 | `.gitattributes` and full renormalization | 2026-09-28 | Complete. Renormalization was a no-op; see Repository Hygiene |
| v2.10.3 | Restore `azqato.com` as the canonical domain | 2026-09-28 | **Partial.** Everything in the repository is done. The `CNAME` is deliberately held back pending DNS confirmation |
| v2.10.4 | Page heads: titles, sharing tags, canonical | 2026-09-28 | Complete. All 12 pages |
| v2.10.5 | Rewrite `privacy-policy.html` | 2026-09-28 | Complete |
| v2.10.6 | Canonical URLs repointed to the extensionless form | 2026-09-28 | Complete. Same-day fix to a v2.10.4 defect found by verifying the deploy |
| v2.9.5 | Gate the remaining pulsing on the fire | Next | Open. Requested 2026-09-01 |
| v2.9.0 | Full catalog native, Mixcloud embeds removed | Next | In progress, waiting on the remaining audio files |
| v3.0.0 | Contact / hire-me section | No date | Planned |
| Unnumbered | GitHub API integration | No date | Planned, low priority |

### Completed milestones

| Milestone | Name | Date |
|-----------|------|------|
| v1.0.0 | Initial launch | 2026-06-06 |
| v1.1.0 to v1.2.2 | Projects plus polish | 2026-06-06 |
| v1.3.0 to v1.3.2 | Support page | 2026-06-07 |
| v1.4.0 to v1.4.1 | About page | 2026-06-07 |
| v1.5.0 to v1.6.1 | New projects plus the `iconUrl` field | 2026-06-07 |
| v1.7.0 to v1.7.4 | Live affiliate links | 2026-06-07 |
| v1.8.0 | Documentation audit (10-file set) | 2026-06-08 |
| v1.9.0 to v1.9.3 | New projects plus filter tags | 2026-06-08 |
| v2.0.0 | Old-site merger (6 new pages) | 2026-06-09 |
| v2.1.0 to v2.2.x | New projects (Stock Methodology, Leveraged Strategies) | 2026-06-10 |
| v2.3.0 to v2.3.2 | Introductory landing page, nav Home and Discord, two new projects | 2026-06-13 |
| v2.4.0 to v2.4.1 | `discord.html` four server cards, sitewide nav update | 2026-06-13 |
| v2.5.0 | Documentation consolidation (4-file set) | 2026-06-13 |
| v2.6.0 to v2.6.16 | Project cards, nav reorder, favicon change, layout pass, URL fixes | 2026-06-14 to 2026-07-09 |
| v2.7.0 | Shared `styles.css` extraction | 2026-07-09 |
| v2.8.0 to v2.8.3 | Music page: visualizer overhaul, booth redesign, stage console | 2026-07-10 to 2026-07-16 |
| v2.8.4 | RouteNote affiliate card | 2026-08-24 |
| v2.8.5 | Full documentation audit | 2026-08-24 |
| v2.9.9 | Full documentation audit | 2026-09-28 |

### v2.7.0: Code extraction and shared assets (Complete)

- [x] Extract shared CSS into a single `styles.css` across all 12 pages. Done. Page-specific `:root` overrides remain inline by design.
- [x] Extract the shared nav HTML. Done in v2.8.8, but not by either method this item originally proposed. Both were rejected: JS injection removes the nav entirely without JavaScript, which trades away the site's graceful degradation to fix a maintenance problem that had never produced a broken page, and a real build step puts a toolchain between the source and the deployed artifact. What shipped instead is `tools/build-nav.py`, a stamp script whose output is committed. The nav is defined once in `PAGES`; running the script rewrites the block between `<!-- NAV -->` and `</nav>` in every page. The deployed site is byte-for-byte unchanged, nothing runs at request time, and deleting the script would cost only the convenience.
- [x] Extract active-state detection. Done in v2.8.8 by the same script, which writes `class="active"` onto the link matching each file's own name. The two pages not in the nav (`accounts.html`, `privacy-policy.html`) fall out correctly with no special case, because no entry matches their filename.
- [x] Add `@media (prefers-reduced-motion: reduce)` to disable hover transforms. Done in v2.8.7, together with the `music.html` play/pause control that Open Question 8 resolved to.

### v2.9.0: Full native catalog (In progress)

Fully built on `feature/native-audio-player` and pushed to GitHub. Contains a Web Audio-routed `<video>` player with a scrub bar, an onset-based kick detector tuned against a real track using `ffmpeg`, a beat-synced screen pulse, a rarity-gated loud-moment flash, audio-scaled laser beam counts, and a Video screen mode that draws the playing track's own frames onto the stage screens.

**Unblocked on 2026-08-29.** The owner is supplying standalone audio files to be played directly on the page, replacing the two Mixcloud iframes. That resolves the only thing this milestone was ever waiting on, and it makes the milestone larger than originally scoped: it is now a replacement of the stage console's playback rather than an addition to it.

**Steps 1 through 4 shipped in v2.8.10** with the first track. Sizing is settled: a 4:46 track at 192 kbps is 6.1 MB, so a handful of tracks sits comfortably inside the repository and GitHub Pages serves them like any other asset. The analyser is wired and the dead declarations are gone. What is left is the replacement itself, and it is gated on files rather than on code.

What this milestone covers, in the order it should be done:

1. Take delivery of the audio files and decide where they live. Anything under roughly 50 MB can sit in the repository and be served by GitHub Pages like any other asset, which keeps the site self-contained. Larger files need object storage with a CDN, or a host that serves a direct file URL. Confirm the actual sizes before choosing, because this decision is hard to reverse once links exist.
2. ~~Replace the two Mixcloud iframes in `.stage-console` with the native player from the branch.~~ Partly done in v2.8.10. The player is in, above the embeds; the embeds stay until the catalog is covered by files.
3. ~~Merge `feature/native-audio-player` and wire the real analyser into `freq()`, replacing the synthetic three-sine signal.~~ Done in v2.8.10, though by porting rather than merging. The branch's CSS, player shape, and `Math.pow(raw, 1.6)` dynamic-range curve were taken; its `<video>` element, kick detector, beat-synced pulse, loud-moment flash, audio-scaled lasers, and Video screen mode were not. Those five remain unmerged and are the interesting part of what the branch still holds.
4. ~~Delete the now-dead `analyser` and `freqData` declarations.~~ Done in v2.8.10; the wiring consumed them.
5. Take the remaining five features off `feature/native-audio-player`. The kick detector and beat pulse are pulled forward into v2.9.1, since they are the fix for the reaction problem rather than an enhancement on top of it. What stays here is the `<video>` element, the loud-moment flash, the audio-scaled lasers, and the Video screen mode.
6. Move the single hardcoded `<audio>` element to a `TRACKS` array once there is a second track, rather than copying the markup block.
7. Reconcile the new player with the v2.8.7 motion control. The play/pause button currently governs the stage animation only. Once audio drives the visuals, decide whether one control governs both or whether they stay separate, and make sure a reduced-motion visitor still gets a still stage rather than a silent one.

What it unlocks beyond the feature itself:

- **The zero-external-request claim becomes true again for all 12 pages** once the embeds go, since the Mixcloud iframes are the only automatic third-party load on the site. v2.8.10 did not move this: it added a native player beside the embeds rather than in place of them, so the caveat still stands everywhere it is written. Every performance, privacy, and security section that currently carries a "except `music.html`" caveat can drop it, including the README's privacy sentence.
- The iframe attack surface described under Known Attack Surface disappears entirely, so the open note about its overly broad `allow` list and missing `sandbox` becomes moot.
- Page weight on `music.html` goes up by whatever the audio costs if the files are committed to the repository. Note that against the 50 KB budget, which the page already exceeds at 112 KB. The audio itself is 6.1 MB, served separately and not counted in the HTML figure, but a visitor on metered data pays for it the moment they press play.

Caveat worth stating before the files arrive: hosting audio in the repository is the simplest option and the one most in keeping with the project's tenets, but git stores every version of a binary forever. Replacing a 40 MB track five times leaves 200 MB in history that cannot be reclaimed without rewriting it. Prefer getting the file right once, or host it outside the repository.

### v2.9.1: Make the reaction actually read as a reaction (Complete, 2026-08-30)

**Observed 2026-08-29, on the first real listen.** The analyser is genuinely wired and the stage genuinely moves with the audio, but it does not read as reacting to the music. The kick does not land. Watching it, you cannot tell that a drum hit and a synth pad are different events. This is the difference between a display that is driven by audio and one that looks like it is listening, and only the second is worth having.

It is a tuning and signal-design problem rather than a wiring problem, so it is scoped separately and should be done before the rest of v2.9.0. There is no point moving the whole catalog onto a player whose reaction does not convince.

**Closed 2026-08-30.** Four of the six hypotheses below were correct and are fixed; two were wrong. The original list is kept with each verdict attached, because the two that were wrong are as useful to the next person as the four that were right.

**Do not assume the cause. Measure first.** Standing hypotheses, most likely first, all of them unverified at the time of writing:

1. **Two low-pass filters stacked.** `analyser.smoothingTimeConstant` is 0.8 and `freq()` then smooths again at `0.72 / 0.28`. Each one alone rounds off transients; together they remove them almost entirely. A kick is a transient by definition, so this alone could explain the whole symptom. Cheapest thing to test: drop the analyser smoothing toward 0.2 and see whether hits appear. **Confirmed, and it was the largest single cause.** Fixed by dropping the analyser to 0.35 and making `freq()`'s own smoothing asymmetric: `0.25 / 0.75` rising, `0.82 / 0.18` falling. Symmetric smoothing rounds the leading edge off every hit, and the leading edge is the part the eye reads as impact.
2. **Band mapping is linear, hearing is not.** `fftSize` 256 gives 128 bins across the full spectrum, so at 44.1 kHz each bin is about 172 Hz. Kick fundamentals live around 50 to 100 Hz, which is bin 0 and part of bin 1. Spread linearly across 64 bands, the entire kick moves one or two bands out of 64 and everything else is midrange and air. A logarithmic or mel-spaced mapping would give the low end the share of the display it has in the listening. **Confirmed.** Bands are now spaced logarithmically from 30 Hz to 16 kHz, built once from the actual sample rate rather than assuming 44.1 kHz.
3. **Resolution too coarse to see a kick at all.** At 172 Hz per bin there is no way to separate a kick from a bass note. `fftSize` 1024 or 2048 costs almost nothing on a page already running shaders. **Confirmed, with a correction to the reasoning.** The general analyser went to 1024, not 2048: frequency resolution trades against time resolution, and a 2048 window spans 46 ms, longer than a frame at 60 fps, which smears the very transients this was meant to recover. The kick detector uses 2048 precisely because it wants the opposite trade. A fifth cause turned up here that was not on this list at all: band level was the mean of its bins, so one loud bin was averaged away by quiet neighbours. It is now the peak.
4. **`Math.pow(raw, 1.6)` may be pulling the wrong direction.** It was tuned on the branch against a different track and a different pipeline. It could be flattening the peaks it was meant to preserve. **Wrong.** The curve is doing what it was meant to. Left at 1.6.
5. **The visuals may not be mapped to anything a listener notices.** Even a perfect signal reads as nothing if it drives a slow-moving element. The lasers, fire, and screen pulse each need checking against what the signal is doing at that moment. **Confirmed, and it turned out to be half the answer.** A hit now drives the screen zoom, the crowd bounce, the laser intensity, and the WebGL clock simultaneously. One element changing reads as an effect; several changing together read as a response. The old `drawBeatFlash` trigger was also replaced: it tested `favg(0, 5) >= 0.76`, which on a loud master is either true continuously or never, and both look identical to no reaction.
6. **The file itself.** Check `audio/womanchild-azqato-remix.mp3` before blaming the code: confirm its actual loudness, dynamic range, and whether it is heavily limited. A brickwalled master has little transient left to detect, and if that is the case the fix is a different render of the track, not different JavaScript. `ffmpeg -af astats` and `ffmpeg -af ebur128` will answer this in one command each. **Wrong, and worth recording as wrong.** The file is fine. There was no `ffmpeg` on this machine anyway, so the measurement was done in the browser instead: decode the mp3, run a 2048-point FFT at a 60 Hz hop, and drive the real detector over the result. The track's transients were there the whole time; the page was destroying them.

**The branch already contains the answer to part of this.** `feature/native-audio-player` has an onset-based kick detector that was tuned against a real track using `ffmpeg`, plus a beat-synced screen pulse. It exists because a raw analyser reading does not give you a kick, which is the same wall this has now hit independently. Read that code before writing anything new. Detecting an onset (a sudden rise in low-band energy relative to its own recent average) is a different technique from reading a level, and it is the technique that makes a hit land.

Acceptance is subjective and should stay that way: play the track, and a person who cannot see the code should be able to tell you where the kick is by watching the screen with the sound off.

**Measured result**, from the offline harness described above:

| Measure | Result |
|---------|--------|
| Hits detected | 92 over 44.5 s |
| Rate | 124.0 per minute |
| Median interval | 0.480 s, implying 125.0 BPM |
| Intervals in 380-620 ms | 94 percent |
| Interval p10 / p90 | 0.430 s / 0.560 s |

124 BPM, against the 124-128 BPM the branch had measured independently for its own track. The detector is locking to the beat rather than firing on noise. Keep these numbers: they are the baseline for anyone who retunes this, and an opinion about whether it "feels right" is not a substitute for them.

**WCAG 2.3.1. Measured properly in v2.9.3, and the earlier measurement was wrong.**

The refractory was written as 26 frames and described throughout this document as 433 ms and 2.3 events per second. **That was only ever true at 60 Hz.** `requestAnimationFrame` runs at the display refresh rate, so on a 120 Hz panel the same 26 frames is 217 ms, and every per-frame decay ran twice as fast, which also made each pulse shorter and harder rather than merely more frequent. Driving the real detector with a worst-case signal that clears its threshold on every frame:

| Display | Before v2.9.3 | After | Limit |
|---|---|---|---|
| 60 Hz | 2.40 /s | **1.70 /s** | 3 /s |
| 120 Hz | **4.70 /s** | **1.70 /s** | 3 /s |
| 144 Hz | **5.60 /s** | **1.70 /s** | 3 /s |

The earlier note in this section said the rate was "at the limit rather than under it" and treated that as the safe case. It was over the limit, by a wide margin, on hardware a large share of visitors own.

Fixed by moving every rate to wall-clock milliseconds and raising the refractory to 600 ms. The light pump is halved to 0.26, the panel white wash cut to roughly a third, the laser response softened to 0.22, and the one true full-screen brightness flash gated to at most one per 8 seconds. Impact is carried by motion instead: zoom, crowd bounce, beam count. The source comment saying not to raise the pump is still load-bearing.

**The general lesson, which applies past this page:** a rate expressed in frames is not a rate. Anything that must respect a per-second limit has to be measured against a clock, and the number has to be taken on more than one refresh rate or the measurement only describes the machine it was taken on.

**Still unmerged from `feature/native-audio-player`:** the `<video>` element and the Video screen mode. The kick detector, beat pulse, loud-moment gate, and audio-scaled lasers all landed here.

### v2.9.5: No pulsing unless the fire is firing (Next, scoped 2026-09-01)

**Requested by the owner, verbatim:** "can you make it so that the pulsing isn't happening unless the fire from the kick is also firing?"

This extends the rule v2.9.3 established for the flash to the continuous brightness terms. v2.9.3 gated the discrete events on `fireActive`, so a white wash only happens when something visible on stage caused it. The slow luminance envelopes added in v2.9.4 are still ungated: they breathe with the music whether or not a kick has fired, and that residual breathing is what is left to remove.

**Sites to change**, all in `music.html`:

| Site | Term |
|------|------|
| `drawBg` background gradient | `envLow * 0.30` and `envLow * 0.14` |
| `drawBg` horizon wash | `envLow * 0.16` |
| Floor grid alpha | `envLow * 0.11` |
| `drawImagePanel` panel alpha and bloom | the `envBroad` terms, whose `flashPulse` half is already gated |

**The one design question to settle before writing any of it.** `fireActive` is a boolean that goes true and false abruptly. Multiplying a slow envelope by it replaces a gentle pulse with a hard step, which is a worse artifact than the one being removed, and on a large area of screen it is exactly the kind of luminance step v2.9.3 spent its whole budget eliminating. The gate almost certainly needs its own ramp: a `fireGate` value that rises quickly when fire starts and falls over a few hundred milliseconds when it stops, with the envelope terms multiplied by that rather than by the boolean. Measure the worst one-frame luminance step afterwards the same way v2.9.4 did, on more than one refresh rate.

**Acceptance:** with the track paused or silent, the stage holds a steady brightness and nothing breathes. With the track playing, brightness moves only while jets are visibly lit. The worst single-frame luminance step stays at or below the v2.9.4 figure of 0.0073 at 60 Hz.

### v3.0.0: Contact / hire-me section (Planned)

A contact CTA, as a new page or a section on an existing one. Options under consideration: an obfuscated email link, a Calendly embed, or a GitHub Discussions link. No server-side form, since that would require a backend or a third-party form service.

### GitHub API integration (Planned, low priority)

Auto-fetch star counts and last-pushed dates per repository, cache them in `sessionStorage` for the visit, and fall back silently to hardcoded values on a rate limit. Note that this is the change that turns the `innerHTML` rendering in `projects.html` from safe into a real XSS surface; escaping every API-sourced string is part of the work, not a follow-up.

## Explicitly deferred items

| Feature | Reason for deferral |
|---------|---------------------|
| CMS or database integration | No server-side runtime; conflicts with the zero-dependency tenet |
| Automated affiliate link management | Affiliate programs change rarely; manual edits are sufficient at this scale |
| Analytics or user tracking | Explicitly excluded by the PRD; conflicts with the privacy-conscious positioning. **Note added v2.9.9:** this remains true of the site's own code, and is no longer true of what a visitor to `azqato.com` receives, because Cloudflare injects a Web Analytics beacon at the edge. See Open Question 12. |
| Multi-page routing or an SPA | Full page loads are simpler and more reliable for a static site |
| Dark / light mode toggle | The site is intentionally dark-only; no toggle will be added |
| Project detail modals | Current descriptions are sufficient; revisit when a project needs extended docs |
| RSS or changelog feed | No audience for it yet; revisit above 2,000 monthly visitors |
| Automated testing (CI) | Manual QA is in use. The threshold that was set for adding smoke tests (11 pages) has now been passed at 12 pages, so this is overdue rather than deferred. |
| Full mobile audit of `music.html` | The visualizer, fixed canvas, and fixed stage console were built and tuned for desktop first. A dedicated pass from 320 px to 480 px is needed to verify layout, tap targets, and readability before the page is mobile-complete. |
| External audio capture for the visualizer | Making the visualizer react to audio from another tab or from system output was researched and declined. It requires either a browser extension or a screen-capture permission prompt, both of which are hostile to a visitor who just wants to look at a page. The native player branch is the accepted path to real reactivity instead. Do not relitigate this. |
| Deleting anything from `img/` | Not deferred, declined. The owner keeps every file in that folder whether or not a page references it. See the standing rule under Never Do These. |


## Decided at the v2.9.9 audit

Six questions were put to the owner on 2026-09-28 and all six were answered. Nothing below was implemented at the audit: the decisions were taken, written down here, and left for a deliberate pass. **The order is least effort first**, and the effort figure is the work plus the review it needs, not just the typing.

The answers, recorded verbatim in effect so a later reader does not have to reconstruct them:

| Question | Decision |
|----------|----------|
| Licence posture: reserved or permissive? | **Keep all rights reserved.** `LICENSE.md` stands as written. The copy that contradicts it gets reworded, not the licence. |
| Canonical domain: `azqato.com` or `azqato.github.io`? | **`azqato.com` is canonical.** The branded domain wins. |
| Cloudflare Web Analytics beacon: keep or drop? | **Keep it, and fix the copy.** The site stops claiming it has no analytics. |
| Social sharing tags: how far? | **All 12 pages, full set.** |
| Page titles: fix or just record? | **Fix them**, in the same pass as the sharing tags. |
| `.gitattributes`: add it? | **Add it and normalize everything**, accepting the one noisy commit. |
| The smaller cleanups in `docs/TODO.md` | **Revisit later.** Not scheduled. |

Two further points settled themselves once the full specification was read rather than inferred. **Images are off by default** on sharing tags, so there is no `og:image` work and no image to produce, and `twitter:card` is `summary`. And there is a **Page Titles** policy, which this project had never recorded and fails on all 12 pages.

### v2.10.0 - Copy alignment (XS, applied at the audit)

**Status: done.** The only item here that was pure documentation, so it was fixed in the audit rather than scheduled. The External FAQ said "The site and nearly every project on it are open source", and the press release boilerplate said "Everything he builds is open source". Both were false for this repository the moment `LICENSE.md` was written. Both were reworded to separate this site, whose source is readable but reserved, from the individual projects, which carry their own licences in their own repositories. The analytics claims in the PRD were aligned with the precise wording already put into the README.

### v2.10.1 - Clean up the nav generator's dead SKIP set (XS) - COMPLETE 2026-09-28

`tools/build-nav.py` skips `nav-extraction-test.html` and `reduced-motion-test.html`. Neither file has existed for some time. A two-line deletion with no behavioral change, since the script only ever iterates files that exist. Offered at the audit and deferred with "revisit this later", then pulled back into scope the same day when the owner scheduled the batch below. No sequencing constraint: it touches one script that nothing else in the batch goes near, so it can land first or last.

**Shipped.** `SKIP` is now `set()` rather than deleted outright, with a comment naming the two files that used to be listed and saying they no longer exist. Keeping the empty set costs one line and is the better shape: the loop that reads it stays as it is, so the next person who needs to exclude a page adds a filename instead of rebuilding the mechanism. `python tools/build-nav.py --check` reports the nav is up to date in every page, which is the same answer it gave before, and that is the point.

### v2.10.2 - .gitattributes and full renormalization (S) - COMPLETE 2026-09-28

**What.** Add a `.gitattributes` at root pinning `* text=auto eol=lf`, then run `git add --renormalize .` and commit the result.

**Shipped as `5070b3b`, and the stated reason turned out to be wrong.** Read the corrected account in Repository Hygiene before trusting the paragraph below. In short: every committed blob was already LF, the CRLF was only on disk, `core.autocrlf=true` was doing the work, and `git add --renormalize .` produced **zero changes**. The file is still worth having, because it moves that guarantee from one machine's local config into the repository where every clone gets it. The original reasoning is kept below unedited, because a wrong premise that produced a right action is worth being able to find.

**Why (as written at the audit, and incorrect).** `music.html` is committed with CRLF while every other text file is LF. Git prints "LF will be replaced by CRLF" on edits, and `tools/build-nav.py` carries deliberate code to preserve whatever ending each file already has rather than normalizing it, which is a workaround for a problem the repository should not have. Byte-comparison checks and headless screenshot diffs are both affected by it.

**How.** One file, one command, one commit. **Outcome:** the commit touched exactly one file, the new `.gitattributes` itself. No page was rewritten.

**Size.** Small to write, and predicted to be the only one of these with a review cost out of proportion to its size. That prediction was wrong; the diff was seven lines.

**Sequence this before v2.10.3, not after.** Both touch all 12 pages. Run the renormalization first and its whitespace-only diff lands in a commit by itself, where a reviewer can confirm it changes nothing and move on. Run it second and it mixes into the head edits, and the one commit that actually needs careful reading becomes the one nobody can read.

**Open questions, now closed.** Whether the media types needed explicit `binary` lines. They were added rather than relying on `text=auto` detection: `*.mp3`, `*.jpg`, `*.jpeg`, `*.png`, `*.gif`, `*.ico`. An explicit line costs nothing and removes the doubt permanently, which matters more here than brevity because the `music/` directory holds audio that is deliberately never committed and a future decision to commit it should not also be a decision about encoding. `git diff --stat` confirmed no binary file was touched.

### v2.10.3 - Restore the canonical domain (S) - COMPLETE 2026-09-28, CNAME closed as moot 2026-09-29

> **The `CNAME` is not happening, and it was never the right task.** Closed 2026-09-29, not because
> the risk was accepted or avoided, but because the premise was wrong. A `CNAME` file is a **GitHub
> Pages** mechanism: it tells GitHub Pages which custom domain it is authoritative for. `azqato.com`
> is not served by GitHub Pages. It is served by **Cloudflare Pages**, a separate product with its
> own custom-domain configuration that lives in the Cloudflare dashboard and takes no file in this
> repository. Adding a `CNAME` would not have made Cloudflare Pages authoritative for anything; at
> best it would have done nothing to the canonical domain, and at worst it would have started GitHub
> Pages redirecting `azqato.github.io` to a domain it does not serve.
>
> **Everything this milestone worried about dissolves with the premise.** The DNS records did not
> need confirming for this purpose, the Pages custom-domain field was never going to be involved, and
> the redirect-loop risk that justified holding it back could not have occurred, because there is no
> proxy relationship between the two hosts to loop through. The caution was reasonable given what was
> believed and it cost nothing, but it was caution about an imaginary mechanism.
>
> **The milestone's actual goal was already met** by the work that did ship. `azqato.com` is
> canonical in all 12 page heads, in `sitemap.xml`, in `robots.txt`, in the README, and in this
> document. Nothing further is required, and nothing is outstanding. See Production: two deployments,
> not one.
>
> **The lesson, which is the same one this batch keeps teaching.** The entire `CNAME` analysis, across
> three documents and several hundred words of risk assessment, rested on an unchecked assumption
> about infrastructure that is not described anywhere in this repository. It was never verified
> because it was never noticed as an assumption. One question to the owner settled it in a sentence.
> **When a plan depends on how something outside the repository is wired, ask, before writing the
> plan.**


**Status.** Steps 2, 3, and 4 shipped. `sitemap.xml` names `https://azqato.com/` in all 12 `<loc>` values, `robots.txt` points at `https://azqato.com/sitemap.xml`, the README live link is `azqato.com`, and the Runbook, Deploy, Rollback, Monitoring, north-star, External FAQ and press-release references in this document were repointed. Step 1, the `CNAME` file, was **not** created, and on 2026-09-29 was closed as moot rather than deferred. The original reasoning for holding it back follows, and is kept because it is a clean example of a careful argument resting on an unchecked premise.

**Why the `CNAME` is still outstanding, and why that is not a loose end.** It is the single change on the whole roadmap that can take the site down, and it depends on two things outside this repository: the DNS records for `azqato.com` and the GitHub Pages custom-domain setting. Neither could be read at the audit and neither can be read from here. Everything else in this milestone is a text edit that one revert undoes. Holding the `CNAME` back is safe in a way worth restating, because it is not obvious: `azqato.com` already serves this site today through Cloudflare, so every `og:url` and `rel="canonical"` shipped in v2.10.4 is correct right now. The `CNAME` decides which host is formally authoritative; it does not decide whether the address works. Tracked in `docs/TODO.md`.

**What to confirm before creating it**, in order: that Cloudflare is proxying to `azqato.github.io` rather than to some other origin; that the Pages custom-domain field agrees with whatever the `CNAME` says; whether `www.azqato.com` should redirect to the apex; and whether `azqato.github.io` should redirect to `azqato.com` or keep serving. GitHub Pages redirects the `github.io` address to a configured custom domain automatically, which is probably wanted, and is worth confirming rather than assuming. Note that if it does start redirecting, the deploy-verification step below has to move with it.

**Original milestone follows.**

**What.** Make `azqato.com` canonical everywhere, in the repository and in the documents.

**Why.** Two hosts currently serve identical content with nothing declaring which is authoritative, which is a duplicate-content problem the site created for itself, and `og:url` cannot be written until it is resolved.

**How.**

1. Create a `CNAME` file at root containing `azqato.com`. One was created and deleted before; this restores it deliberately. Note it is what tells GitHub Pages to serve the custom domain, and its absence is why the repository only formally serves `azqato.github.io` today.
2. Repoint all 12 `<loc>` values in `sitemap.xml` and the `Sitemap:` line in `robots.txt`.
3. Update the README live link, and the `azqato.github.io` references in the Runbook, Deploy, Rollback, and Monitoring sections of this document.
4. `rel="canonical"` tags are part of v2.10.4, because they are a page-head edit and belong in that one pass.

**Size.** Small in the repository. The part that is not in the repository is the part to be careful about.

**Open questions, and they are real.** The DNS records and the GitHub Pages custom-domain setting both live outside this repository and the audit could not read either. Before committing the `CNAME`, confirm how `azqato.com` currently reaches the site: if Cloudflare is proxying to `azqato.github.io`, adding a `CNAME` changes which host is authoritative and the Pages setting has to agree with it, or the domain can break. Also decide whether `www.azqato.com`, which resolves today, should redirect to the apex, and whether `azqato.github.io` should redirect to `azqato.com` or keep serving. GitHub Pages will redirect the `github.io` address to a configured custom domain automatically, which is probably what is wanted, and is worth confirming rather than assuming.

### v2.10.4 - Page heads: titles, sharing tags, canonical (M) - COMPLETE 2026-09-28

**Shipped on all 12 pages.** Each head now carries, in this order: `<title>`, `<meta name="description">`, `<link rel="canonical">`, `og:title`, `og:description`, `og:url`, `og:type`, `og:site_name`, and `twitter:card`. Nine tags, verified present on every page by count rather than by spot-check.

**No `og:image`, and that is the specification rather than an omission.** The full documentation specification, fetched from its source after the pasted copy proved to be truncated, puts images off by default. With no image, `twitter:card` is `summary` rather than `summary_large_image`. Cards will render as text. If an image is ever added, both decisions change together and the site needs a real `og:image` per page or one credible default, not a logo stretched to 1200x630.

**Applied by script, with a compliance gate that ran before anything was written.** The gate failed the whole run on: any title over 60 characters, any `og:title` over 70, any description over 200, an `og:title` containing the site name, a non-index title missing the ` - Azqato` suffix, two pages sharing their first 30 characters, or a placeholder title. It passed on the first complete run. That ordering is the part worth copying: a script that validates its own inputs before touching 12 files cannot leave the repository half-edited.

**Verified.** `python tools/build-nav.py --check` clean afterwards, since the nav block sits in all 12 heads. Browser test in headless Edge against a local server on four pages: `index`, `projects`, `music`, `privacy-policy`, all rendering correctly. Still outstanding: paste two or three live URLs into Discord after the push and look at the cards. That is the only check that tests the thing the milestone is actually for, and it cannot be done before deploying.

**Original milestone follows.**

**What.** One pass over all 12 pages adding the six required Open Graph tags, `twitter:card`, a meta description, and `rel="canonical"`, and replacing every title.

**Why.** No page has any of it. Links shared to Discord render as bare URLs on a site whose main call to action is its Discord page, and every tab truncates to "Azqato | ..." because all 12 titles lead with the brand.

**How.** Titles, which satisfy the 60-character limit and keep the first 30 unique:

| Page | New title | Length |
|------|-----------|--------|
| `index.html` | `Azqato - Communities, Projects, Music` | 37 |
| `about.html` | `About - Azqato` | 14 |
| `discord.html` | `Discord Communities - Azqato` | 28 |
| `invests.html` | `Investing Tools and Resources - Azqato` | 38 |
| `codes.html` | `AI Prompts and Coding Tools - Azqato` | 36 |
| `music.html` | `Music and DJ Mixes - Azqato` | 27 |
| `links.html` | `All Links - Azqato` | 18 |
| `projects.html` | `Projects - Azqato` | 17 |
| `youtube.html` | `YouTube Channels - Azqato` | 25 |
| `support.html` | `Support the Work - Azqato` | 25 |
| `accounts.html` | `Gaming Accounts - Azqato` | 24 |
| `privacy-policy.html` | `Privacy Policy - Azqato` | 23 |

Only the homepage leads with the brand, which is the one place the rule inverts. "Welcome" and "Codes" are gone, because neither told a stranger what its page was.

And the `og:title` values, which carry no brand because the card prints `og:site_name` above them:

| Page | `og:title` |
|------|-----------|
| `index.html` | `Communities, Projects, Tools and DJ Mixes` |
| `about.html` | `From RuneScape Clans to Building Web Tools` |
| `discord.html` | `Four Communities: Gaming, Investing, RuneScape` |
| `invests.html` | `Free Investing Tools and a Curated Resource Hub` |
| `codes.html` | `Prompt Libraries and Browser-Based AI Tools` |
| `music.html` | `An Animated Stage That Reacts to the Track` |
| `links.html` | `Every Platform and Channel in One List` |
| `projects.html` | `Fifteen Browser Tools, Dashboards and Sites` |
| `youtube.html` | `Four Channels: Main, Streams, Mixes, Chill` |
| `support.html` | `Buy Me a Coffee and Labeled Referral Links` |
| `accounts.html` | `Steam, League, TFT and RuneScape Profiles` |
| `privacy-policy.html` | `What This Site Collects, and What It Does Not` |

`og:site_name` is `Azqato`, `og:type` is `website`, `twitter:card` is `summary`, and `og:url` and `rel="canonical"` are the absolute `https://azqato.com/` URL of each page. No `og:image`: images are off by default, and a declared image that does not exist is worse than none.

**Size.** Medium. Twelve files, roughly nine lines added to each, plus a browser test. It is a major update under Testing Cadence, so an assumption check and one browser test run before it ships.

**One prerequisite the implementer must not skip.** `og:description` has to be written from each page's actual content, not from its filename, and **the v2.9.9 audit read only the `<head>` of seven of these pages**: `about`, `index`, `discord`, `youtube`, `codes`, `links`, and `accounts`. Their bodies were never read. So the descriptions for those seven are not drafted here on purpose, because drafting them from a filename is the exact failure the rule forbids. Read each page first, then write its description. The five already read closely (`projects`, `invests`, `music`, `support`, `privacy-policy`) can be drafted straight away.

**Verification.** Run the five compliance checks in Social Sharing Tags and the five in Page Titles. Then paste two or three of the live URLs into Discord and look at the cards, because that is the renderer the budgets were chosen for and the only check that catches a card that is technically valid and still looks wrong.

### v2.10.5 - Rewrite privacy-policy.html (M) - COMPLETE 2026-09-28

**Shipped.** The page is 14,212 bytes down to 13,381, which is the right direction: the old one was longer because it was generic, not because it said more.

**What came out.** The generated boilerplate that described a site this has never been: a Consent section, Google DoubleClick DART Cookie, Advertising Partners, Third Party Privacy Policies, Cookies and Web Beacons, and How We Use Your Information. Those sections between them promised log-in handling, ad personalisation, and cookie policies for a site with no accounts, no ads, and no cookies of its own. A privacy policy that describes the wrong site is worse than a short one, because it is confidently wrong about exactly the thing a reader came to check.

**What went in.** A short version at the top, then: what the site collects directly (nothing), web server logs, the Cloudflare Web Analytics disclosure, the Mixcloud and YouTube embeds on the Music page, cookies, rights under GDPR and CCPA, and the retained children, affiliate, financial, entertainment and copyright sections.

**The analytics section is the one that mattered**, since it is the reason this milestone existed. It names Cloudflare, says the script is injected at the edge on `azqato.com` and not present on `azqato.github.io`, and is specific about what kind of analytics it is: cookieless, no fingerprinting, no profile, no cross-site tracking, aggregate counts only. It then says blocking it is fine and breaks nothing, which is true and is the part most policies leave out.

**The rights section refuses the usual dodge.** It states the GDPR and CCPA rights, then says plainly that this site holds no personal data to hand over or delete because it collects none, and that the data which does exist sits with GitHub, Cloudflare, Mixcloud and YouTube as separate controllers, so a request is best made to them. The page ends by saying it has not been reviewed by a lawyer and is not legal advice, which is both true and the only honest footer for a policy written this way.

**Original milestone follows.**

**What.** Replace the page's body with an accurate description of what this site does.

**Why.** It is stock boilerplate. It describes Google DoubleClick DART cookies, third-party ad servers, ad networks, and web beacons, none of which exist here, and it is dated 2024 while the rest of the site is 2026. It has been an open question since the v2.8.5 audit, recorded then as row 17 and Open Question 6, and left alone twice on the reasoning that over-disclosure is harmless. That reasoning no longer holds, for a specific reason: the Cloudflare decision means this site now has a real tracker to disclose, and a page full of invented disclosures is the worst place to put a true one, because nobody reads the page that cried wolf.

**How.** State what is actually true. No accounts, no sign-ups, no forms, no ads, no cookies set by the site. GitHub Pages logs standard server-level request data as any web server does. `azqato.com` is served through Cloudflare, which runs Web Analytics and adds a beacon to every page; say what it collects and that it is cookieless. The Music page embeds Mixcloud and YouTube players, which are third parties with their own terms and which see a request when the page loads. Keep the existing affiliate disclosure and the financial disclaimer, which are the two genuinely load-bearing parts of the current page. Update the date. Link `LICENSE.md`.

**Size.** Medium, and most of it is care rather than volume. The result will be substantially shorter than what it replaces.

**Open questions.** Whether to keep the boilerplate's structure and headings so returning visitors recognize the page, or restructure it around what the site actually does. Whether a plain-language summary at the top is worth it, which for a page this short it probably is. This is legal-adjacent copy, so the owner should read it before it ships, and it is worth saying that it is not legal advice and has not been reviewed by anyone who gives it.

### Not scheduled

| Item | Why not |
|------|---------|
| `tools/build-nav.py` SKIP cleanup | Offered, deferred with "revisit this later". In `docs/TODO.md`. |
| Extract `music.html` JS to `viz.js` | Offered, deferred. Large refactor of the visualizer, roughly 1,900 lines, needing a full browser test. Known technical debt, not urgent. |
| Compress the four oversized thumbnails in `img/` | In `docs/TODO.md`. Compression, never deletion: nothing in `img/` is deleted. |
| A progress dashboard | See Future Updates below. Deliberately after these items, because it reports on facts that are about to change. |
| v2.9.5 visualizer brightness gate | Already reserved and roadmapped. Untouched by this audit. |
| v2.9.0 full catalog native | Blocked on the remaining audio files arriving. |
| The brand and mascot decisions | Owner decisions, not work. In `docs/TODO.md`. |

### v2.10.6 - Canonical URLs repointed to the extensionless form (XS) - COMPLETE 2026-09-28

**What.** `rel="canonical"` and `og:url` on the 11 non-index pages, and the matching 11 `<loc>` values
in `sitemap.xml`, changed from `https://azqato.com/page.html` to `https://azqato.com/page`.

**Why.** v2.10.4 shipped `https://azqato.com/projects.html` in every head. Verifying the deploy showed
`azqato.com` returns **307 to `/projects`**: there is a Cloudflare rule stripping the extension, which
was not recorded in any document and which the audit could not have seen, because it was reading the
repository rather than the live responses. Every canonical tag was therefore pointing at a URL that
immediately redirects, which undercuts the only thing a canonical exists to assert.

**Checked before changing anything.** The extensionless form returns 200 on both hosts. GitHub Pages
serves `/projects` for `projects.html` natively, so the declared URLs are correct on the origin too,
which matters while the `CNAME` is outstanding and the origin is still what the runbook checks.

**Not in scope.** Internal links still carry `.html`, so on `azqato.com` every internal click takes a
307 first. That predates this batch and fixing it means changing the nav generator and every page
body. Tracked in `docs/TODO.md`.

**The general point, which is the reason this is written up rather than quietly patched.** The head
tags were generated from the repository's filenames. Nobody asked what the canonical host does with
those filenames, and the canonical host does something. **A URL is a claim about a live system, and
it can only be verified against that system.** Confirming a deploy landed is not the same check as
confirming that what landed is correct, and this project's runbook had the first and not the second.
See the addition to the Verification checklist.

### The planned batch, scheduled 2026-09-28

The owner scheduled **v2.10.1, v2.10.2, v2.10.4, and v2.10.5 as a single pass**, deliberately leaving
v2.10.3 out because it is the one item that can take the site down.

**That cannot be done as stated, and the reason is worth reading before starting.** v2.10.4 writes
`og:url` and `rel="canonical"` on all 12 pages as absolute `https://azqato.com/` URLs. `sitemap.xml` and
`robots.txt` still name `azqato.github.io`. Shipping 10.4 without touching them leaves the site
declaring one canonical address in its page heads and a different one in its sitemap, which is a worse
state than the one before this audit: today the two hosts merely compete, whereas afterwards the site
would actively contradict itself, and a crawler resolves that by picking for you.

**So v2.10.3 splits rather than waits.** Its work divides cleanly along the line of what is risky:

| Part | Does it need DNS? | Where it goes |
|------|-------------------|---------------|
| Repoint the 12 `<loc>` values in `sitemap.xml` | No | **Into the batch** |
| Repoint the `Sitemap:` line in `robots.txt` | No | **Into the batch** |
| Update the README live link and the `azqato.github.io` references in Runbook, Deploy, Rollback, and Monitoring | No | **Into the batch** |
| Create the `CNAME` file containing `azqato.com` | **Yes** | **Held back** |

Only the last row is dangerous, and it is dangerous for a specific reason rather than out of caution: a
`CNAME` file is what tells GitHub Pages which custom domain it is authoritative for, and if the DNS
records or the Pages custom-domain setting disagree with it, the domain stops resolving. Both of those
live outside this repository and neither could be read at the audit. Everything above that row is a text
edit that reverts with one commit.

**Note that holding the `CNAME` back is safe in a way that is not obvious.** The tags, the sitemap, and
the robots file can all name `azqato.com` before the `CNAME` exists, because `azqato.com` already serves
this site today through Cloudflare. The tags will be correct on the day they ship. The `CNAME` changes
which host is formally authoritative; it does not change whether the address works.

**Order within the batch:**

1. **v2.10.2 first**, alone, committed on its own. Renormalization rewrites all 12 pages with no visible
   change, and it has to land before anything else edits those files. See the sequencing argument in that
   milestone.
2. **The repo-side of v2.10.3**, so the canonical address is consistent across `sitemap.xml`,
   `robots.txt`, the README, and this document before any page head claims it.
3. **v2.10.4**, the substantive change. Read the bodies of the seven pages whose heads were all the audit
   read (`about`, `index`, `discord`, `youtube`, `codes`, `links`, `accounts`) before writing their
   descriptions. Major update under Testing Cadence: assumption check plus one browser test in headless
   Edge, right before it ships, then paste two or three live URLs into Discord and look at the cards.
4. **v2.10.5**, last, because it is judgement rather than mechanism.
5. **v2.10.1** anywhere; it touches only `tools/build-nav.py`.

Then run `python tools/build-nav.py --check` at the end, because step 1 rewrites every page and step 3
edits every head, and the nav block sits in all 12 of them.

### Recommended path

**Do v2.10.2 first**, before anything else touches a page. It is the smallest change on the list and it is the only one whose value depends entirely on ordering: run the renormalization on its own and its all-12-files whitespace diff sits in a commit a reviewer can dismiss in one glance, leaving the head edits to arrive as a clean, readable diff. Run it after, and the one commit that needs careful reading is buried in noise. Check `git diff --stat` before committing to confirm no binary file appears.

**Then v2.10.3**, and stop at the point where DNS is involved. Create the `CNAME` and repoint the sitemap, robots, README, and documents in the repository, but confirm the DNS and GitHub Pages custom-domain settings before pushing, because those are the two things the audit could not read and the only part of this list that can take the site down. Everything else here is recoverable by reverting a commit; this is not.

**Then v2.10.4**, which is the item with the actual payoff. Every link shared from now on gets a real card, and the tabs stop being twelve copies of the same word. Before starting, read the bodies of the seven pages whose heads were all the audit read, then write their descriptions. It is a major update, so the assumption check and the browser test happen right before it ships, and the last check is to paste a couple of live URLs into Discord and look at them.

**Then v2.10.5**, last of the four, because it is the only one that is judgement rather than mechanism and it benefits from not being rushed behind the others.

v2.10.0 is already applied and v2.10.1 is deferred, so there is nothing to do for either.

One thing to decide before starting rather than during: whether these ship as four commits or one. Four is the recommendation, matching the four milestones, because v2.10.2 is whitespace, v2.10.3 can break DNS, v2.10.4 is the substantive change, and v2.10.5 is copy that wants its own review. Reverting any one of them separately is worth more than a tidy history.

### What actually happened, 2026-09-28

The whole batch shipped the same day the path was written, so this section is a retrospective rather than a plan. Three things are worth recording because they are the kind of thing that is invisible a month later.

**The sequencing advice was correct reasoning built on a false premise.** v2.10.2 went first, as recommended, to keep a noisy whitespace diff out of the head edits. There was no noisy diff; renormalization changed nothing, because every blob was already LF. Going first cost nothing and the argument for it was sound given what was believed, but the belief should have been checked with `git ls-files --eol` before an argument was built on top of it. **Verify the premise before planning around it**, particularly when the premise is cheap to check and the plan is expensive to write.

**Splitting v2.10.3 was the right call and the batch would have been incoherent without it.** The owner excluded v2.10.3 to avoid the DNS risk, which was sound, but v2.10.4 writes `azqato.com` into 12 page heads. Shipping that while the sitemap still said `azqato.github.io` would have left the site contradicting itself, which is worse than the ambiguity it started with: two hosts competing is a problem a crawler resolves conservatively, whereas a site that declares one canonical address in its heads and another in its sitemap invites the crawler to pick, and it may not pick the one you want. Splitting on the line of what needs DNS, rather than on the milestone boundary, let the risky 10 per cent wait while the safe 90 per cent shipped coherently.

**It shipped as separate commits, as recommended.** v2.10.2 landed alone as `5070b3b`; the rest followed. The reason holds regardless of how quiet the diffs turned out to be: these are four unrelated changes, and the ability to revert the privacy-policy rewrite without also reverting the sharing tags is worth more than a compact history.

**Still open after the batch:** the `CNAME` file, which needs DNS confirmation, and the Discord card check, which needs the deploy to have landed.

## Future updates

Proposals that are not yet milestones. Each one states what it is, why it might be worth doing, how it would be built, how big it is, what is unresolved, and a recommendation.

### The Invests top bar across the whole site (added 2026-10-02, owner's request)

**What.** Give every azqato.com page the top navigation bar the Invests pages use: the slim full-width strip with the `Azqato.` logo and the same ten links, sitting at the very top above the page's own content. Today the main pages have their own sticky nav (F3); Invests draws a copy of it in its own style (invests/scripts/site.py `AZQATO_NAV`, styled by `.site-azqato` in invests/assets/css/site.css).

**Why.** The owner prefers how it sits above the main content. One look for the nav on both halves of the site also removes the visible jump between azqato.com and /invests/.

**How.** Port the `.site-azqato` styles (both themes) into styles.css and change the markup tools/build-nav.py stamps into the 12 pages, so the nav stays generated from one list. Keep the mobile dropdown working (the nav toggle script on every page); on phones Invests hides the strip and moves its links into its sidebar, which the main pages don't have, so the phone layout needs its own decision. Ideally the Invests copy then reads the same page list (build-nav.py or a shared file) so the two can't drift (invests PRD, Known technical debt).

**Size.** Small to medium: one stylesheet section, the build-nav.py template, a rerun, and a browser check of all 12 pages in both themes at desktop and phone widths.

**Open questions.** The phone layout (keep the current dropdown, or something else). Whether `Support` and the active-page highlight look the same as on Invests. Whether this lands before or as part of folding Invests into the site's structure (invests PRD, P14).

**Recommendation.** Do it; it's mostly CSS and one template. Settle the phone layout with the owner first.

### A progress dashboard

**What.** A single page that shows the state of the project at a glance: which roadmap milestones are done, which are in flight, what is deferred, how many open questions are outstanding, and when the last audit ran. It would live at `/dashboard` in the repository root.

**Why.** This document is 1,800 lines long. The information needed to answer "where is this project" is spread across the milestone table, the deferred list, the open questions, and the patch notes, and answering it currently means reading four sections and holding them in your head. That cost is paid by the owner on every return to the project after a gap, and by every model that picks the work up cold. A dashboard is the one artifact that would make the roadmap legible without reading the roadmap.

**How.** Build it by running the prompt at https://azqato.github.io/prompts/p/progress-dashboard.html against this repository. The prompt is the specification; it is not restated here, and it should be read rather than summarised, because a summary of it in this document would be one more thing to keep in sync.

**Size.** Small to medium. The page itself is one static HTML file matching the existing design system, so it costs no dependency and no build step. The real cost is not the page, it is the update discipline: a dashboard that is out of date is worse than no dashboard, because it answers the question confidently and wrongly. Whatever ships has to name who updates it and when, and the honest options are either "regenerate it at every audit" or "regenerate it whenever a milestone moves".

**Open questions.** Whether it is public or local-only. GitHub Pages serves this repository from the root, so a committed `/dashboard` is readable by anyone, which is fine for milestone names and bad for anything candid about what is unfinished; the `brand/` folder was made local-only for exactly this reason. Whether it is generated once and hand-maintained, or regenerated each time. Whether it belongs in the nav, which currently has 10 items and is already close to collapsing at 860 px.

**Recommendation.** Worth doing, after the open questions in this audit are settled. It is a reporting layer over the roadmap, and building a reporting layer over facts that are about to change (the canonical domain, the licence posture, whether social tags exist) means building it twice. There is no progress dashboard today and no `/dashboard` folder; there is also no `CLAUDE.md` in this project, so there is no existing dashboard convention that this proposal would conflict with.

## Verification checklist

Claims in this document and in DESIGN.md that were **not** read in the code at the v2.9.9 audit, and are therefore carried forward on the authority of an earlier audit rather than on a fresh reading. They are not known to be wrong; they are unverified, which is a different thing, and the next audit should start here.

**A category this checklist did not have, added 2026-09-28 after it cost something.** Some claims cannot be verified by reading the repository at all, because they are claims about what a live host does. Reading every file in this project will never tell you that `azqato.com` 307-redirects `/projects.html` to `/projects`, because that rule lives in a Cloudflare configuration that is not in the repository and is not documented anywhere else either. v2.10.4 shipped 11 canonical tags pointing at redirecting URLs for exactly this reason, and only a request to the live site found it. **Anything the site asserts about a URL, a header, or a response belongs in this category**: canonical tags, `og:url`, sitemap entries, the analytics beacon, redirect behaviour between the two hosts, and anything involving Cloudflare. The check is a request, not a read.

| Section | What is unverified | Why it was not checked |
|---------|--------------------|------------------------|
| Data Models, for `about.html`, `index.html`, `discord.html`, `youtube.html`, `codes.html`, `links.html`, `accounts.html` | The per-page card and section tables. | The v2.9.9 audit read `projects.html` and `invests.html` closely, because that is where the change since the last audit landed, and read `music.html` only in the regions bearing on the visualizer claim. The other seven pages were read only in their `<head>`, for the sharing-tag check. |
| **Live-host behaviour on `azqato.com`** | What Cloudflare does to requests beyond injecting the analytics beacon and stripping `.html`. Both of those are now known and documented; whether there are other rules, and what the cache and `www` behaviour are, is not. | Nothing about the Cloudflare configuration is in this repository or recorded in any document. It can only be established by making requests, and it was never checked until a shipped defect forced it. **Two rules found so far, and both were invisible to the obvious check**: the redirect was invisible to reading the repository, and the beacon is invisible to a bare `curl`, because injection is conditional on the `Accept: text/html` header. Assume more of these exist. |
| **Internal link shape** | Whether every internal `href` resolves without a redirect on the canonical domain. It does not: they all carry `.html` and all take a 307. | Known and deliberate as of v2.10.6. Recorded in `docs/TODO.md` as a decision for the owner, not a defect. |
| Third-Party Integrations | That every Discord invite, affiliate URL, and embed still resolves. | Requires clicking each one. The Monitoring table already schedules this monthly; an audit is not the place for it. |
| Performance metrics and Targets | Load time, Lighthouse scores, and the sub-second claim. | Nothing was measured this audit. The figures date from the v2.8.5 audit. Page weights were re-measured and are current. |
| DESIGN.md, spacing scale, breakpoint values, and the six component patterns | That each documented value matches the CSS. | Only `styles.css`'s size and the four specific stale claims were checked. The token tables were not re-read against the inline `<style>` blocks. |
| DESIGN.md, Animation and Motion, the WCAG 2.3.1 flash rate | The 1.70 flashes per second figure from v2.9.3. | Requires instrumenting the page at a known refresh rate. Not reproducible by reading. |
| `music.html` GLSL shader internals | What each of the nine modes computes. | Already recorded under What Was Not Fully Understood. Treated as opaque assets by standing decision. |
| Press Release | Four Discord servers, four YouTube channels, the customer quote. | It is explicitly a communication exercise, not a record. The project count was corrected to fifteen; the rest was not re-counted. |

---

# Documentation Versus Reality

Every document was compared against the source at the v2.8.5 audit, and again at the v2.9.9 audit (rows 21 onward). Each row records what was found, which source was trusted, and why. Resolved rows are kept rather than deleted, so the record shows what was found and what was decided.

| # | Finding | Trusted source and reasoning | Resolution |
|---|---------|------------------------------|------------|
| 1 | README described the nav as "Home, About, Discord, Invests, Links, Projects, Tools, YouTube, GitHub, Support", with external Tools and GitHub links. The code has "Home, About, Discord, Invests, Codes, Music, Links, Projects, YouTube, Support", all internal. | Code. Patch notes record the deliberate removal of the external nav links in v2.6.x and the addition of Music in v2.8.0, so the README simply was not updated. | Fixed. README rewritten; PRD F3 and DESIGN.md now list all 10 current items including Music. |
| 2 | `codes.html` appeared zero times in README.md and PRD.md, despite being a live page in the nav of all 12 pages. | Code. A page cannot be in every nav by accident. | Fixed. Added to the Site Structure table, the folder tree, the public surface list, and F13. |
| 3 | README said "Eleven self-contained HTML pages"; the PRD architecture section said "eleven plain HTML pages"; other PRD sections said 12. The filesystem has 12. | Code, and the PRD contradicted itself. | Fixed. 12 everywhere. Also dropped "self-contained", which stopped being true when `styles.css` was extracted in v2.7.0. |
| 4 | The clone command in both the README and the runbook was `git clone https://github.com/Azqato/Azqato.git`. The actual remote is `Azqato/azqato.github.io`. | Code (`git remote -v`). The documented command would fail. | Fixed in the runbook. The README no longer carries commands at all. |
| 5 | Docs claimed "zero external requests on page load" and "no external requests of any kind on the main site pages". `music.html` loads two Mixcloud iframes on every visit and `projects.html` fetches one cross-site favicon. | Code. The claim was written before the Mixcloud embeds existed and was never revisited. | Fixed. Every performance, privacy, and security claim now states the exception. Whether to make the embeds click-to-load is Open Question 3. |
| 6 | Success criteria and constraints stated "under 50 KB per page" as met. `music.html` is 114 KB. | Code. The file size is not a matter of opinion. | Fixed. The target is kept as the standard for the other 11 pages, with the exception named and explained. |
| 7 | DESIGN.md documented the affiliate card as `.logo-area`, `.promo-badge`, `.affiliate-btn` inside a `<div>`. The PRD data model repeated the same names. `support.html` uses `.affiliate-logo`, `.affiliate-promo`, `.affiliate-link-btn` inside an `<a>`. | Code. Three of four documented class names do not exist. | Fixed in both documents. |
| 8 | The PRD State Management table listed an `activeTag` string variable in `projects.html`. No such variable exists; filter state lives in the DOM. | Code. | Fixed. |
| 9 | DESIGN.md gave the mobile breakpoint as "< 600px: nav links hidden (logo only visible)". `styles.css` collapses the nav at 860 px into a hamburger dropdown, and PRD F3 already said 860 px. | Code, corroborated by the PRD. DESIGN.md described a nav that no longer exists. | Fixed, with the superseded claim recorded rather than erased. |
| 10 | DESIGN.md listed `home-hero-profile.jpg` as the landing page hero avatar, and two `music-playlist-*.jpg` files as playlist covers on `music.html`. `index.html` contains no `<img>` and `music.html` lists no playlists. Ten of fifteen images are referenced by nothing. | Code. | Fixed: DESIGN.md now records actual usage. The files themselves are left alone pending Open Question 2. |
| 11 | `img/20260711-0151-37.7601512.gif` (1.9 MB, tracked, unreferenced) appeared in no documentation of any kind. | Code. | Fixed. Documented as unreferenced in DESIGN.md and in the public surface list. |
| 12 | PRD F4 said the landing page hero includes a profile photo. It has pills and buttons, no photo. | Code. | Fixed. |
| 13 | F11 said the lion favicon is identical across all 12 pages. `music.html` overwrites it at runtime every third frame. | Code. Both statements are half true, which is worse than either. | Fixed. F11 now names the exception and F14 documents the animated favicon. |
| 14 | No document anywhere mentioned that the `music.html` visualizer is not audio-reactive. `analyser` and `freqData` are declared and never assigned, so every visual is procedural. | Code. This is the kind of thing a reader assumes the opposite of by default. | Fixed in v2.8.5 by documenting it, then made obsolete in v2.8.10 by wiring a real analyser to the native track. The page is now reactive while that track plays and synthetic otherwise, and every document says so. |
| 15 | The PRD said "There is only one environment: production (GitHub Pages)". `wrangler.jsonc` describes a complete Cloudflare Workers deploy target and has been committed since 2026-07-09. | Both. The statement was true of what served traffic; the file was real and undocumented. | Resolved in v2.8.9 by deleting the file. The document was right and the file was residue. |
| 16 | `projects.html` links Leveraged Strategies at `/leveraged-strategies/`; `invests.html` links the same project at `/leverage/`. Patch note 2.6.12 records the move to `/leverage/`. | Resolved in v2.8.9 by checking the live web instead of guessing. `/leverage/` serves the page; `/leveraged-strategies/` is a hard 404. | Fixed. Both fields on the `projects.html` card now point at `leverage`. The audit was right to leave it alone at the time: it was a live broken link, and guessing the other way would have broken the working one too. |
| 17 | The privacy policy describes Google DoubleClick DART cookies, third-party ad servers, ad networks, account registration, and marketing emails. The site has no ads, no accounts, and no email capture. | Code. The policy is a generic template with real disclosures (affiliate, financial) appended. | Not changed. It is legal copy, over-disclosure is not a defect, and rewriting a privacy policy is the author's decision, not an audit's. Recorded as Open Question 6. |
| 18 | PRD Known Technical Debt said the nav is duplicated across "all 11 HTML files". It is 12. | Code. | Fixed. |
| 19 | `.vscode/recentfedsummary.MD` is tracked in git, is unrelated to the project, and contains 13 em-dash violations of the project's own writing policy. | Code. The policy is unambiguous; the file predates the hook, which only checks staged changes. | Resolved in v2.8.9: deleted at the owner's direction. Setting aside the exempt lines where a rule names the character it prohibits, the repository now has zero violations. |
| 20 | PATCHNOTES.md entries are not in a consistent order: the file runs newest-first at the top, then ascending from 1.0.0, then jumps between 2.6.6, 2.5.1, 2.6.16, and back down. | Neither is wrong; the file is a historical record. | Not reordered. Historical records are not rewritten. The convention for new entries is stated in the Documentation Process below. |
| 21 | The project had no `LICENSE.md` and no licence text anywhere, while the README and the External FAQ both invited reuse. | The prompt's default applies only where a project has no licence, or a bare licence name with no text behind it. This was the second case in spirit: an invitation with nothing behind it. | Created `LICENSE.md` at root with the all rights reserved, source-available default, including the AI search, substitution, training, no-waiver, permission, platform, third-party, warranty, and financial-disclaimer sections. The README's "The source is open. Read it, copy it" was replaced with a neutral pointer to `LICENSE.md`, because a bare grant with no licence text behind it is an ambiguity and leaving it beside a reserved-rights licence would mislead a reader either way. The wording chosen asserts neither posture. **Decided 2026-09-28: keep all rights reserved.** The External FAQ answer and the press release boilerplate were then reworded as v2.10.0, separating this site (source-available, all rights reserved) from the individual projects (mostly public repositories with their own licences). Open Question 9 closed. |
| 22 | No `robots.txt`. Confirmed 404 on both hosts, not merely absent from the repository. | The project serves a site, so the file is required. | Created at root, fully open to all crawlers with no exclusions, carrying a comment that says the openness is deliberate and that `LICENSE.md` is authoritative if the two appear to disagree. |
| 23 | No `sitemap.xml`. Confirmed 404 on both hosts. | Required where a project serves a site. | Created at root listing all 12 pages, which is every page: none is behind a sign-in. `lastmod` is each page's last commit date, read from git rather than set to today. `robots.txt` names it on a `Sitemap:` line. Uses `azqato.github.io`, pending Open Question 10. |
| 24 | No `docs/TODO.md`, and the Documentation Process forbade one: "Exactly four documents. No fifth file is created inside `/docs`," plus maintenance rule 7, "Never create a new `.md` file in `/docs`." | The audit's own required structure includes `docs/TODO.md`, so the file wins and the rule has to stop contradicting it. | Created `docs/TODO.md`, seeded from open items already recorded across the documents and from this audit. The file structure block and rule 7 were both updated to say five documents, with TODO.md named as the last addition and as a holding place that is never consolidated, merged, moved, or deleted. Its contents are explicitly not instructions. |
| 25 | No page on the site carries a single `og:` tag, `twitter:` tag, meta description, or canonical tag. All 12 heads hold only a title, charset, viewport, and a data-URI favicon. | Code, read in all 12 files, and confirmed against the live site. | Policy written under Social Sharing Tags; **no page was edited at the audit**, because the policy is a record and `og:url` was blocked on the canonical-domain question. **Decided 2026-09-28: add the full set to all 12 pages**, scheduled as Roadmap v2.10.4 alongside the title rewrite. Reading the full specification settled the image rules too: images are off by default, so no `og:image` and `twitter:card` is `summary`. Open Questions 10, 11, and 14 closed. **Shipped 2026-09-28**: all 12 heads now carry nine tags each, applied by a script whose compliance gate ran before any file was written. Resolved. |
| 26 | `azqato.com` and `www.azqato.com` serve a Cloudflare Web Analytics beacon. The README, the PRD, the External FAQ, and the press release all state the site has no analytics and no tracking. | Both. The repository source is clean, so the documents were accurate about the code; the live response proves them false about what a visitor actually receives. Neither reading is the wrong one, which is why both are recorded. | README made precise about the distinction between the site's own code and what the `azqato.com` edge adds. The PRD's deferred-items row annotated. **Decided 2026-09-28: keep the beacon and fix the copy.** The PRD Security section, the External FAQ, the press release, and the north-star metric note were then aligned as v2.10.0. `privacy-policy.html` carries the real disclosure and is Roadmap v2.10.5. Open Question 12 closed. |
| 27 | Never Do These said "Never claim in copy that the music visualizer reacts to the audio. It does not." It does, for the one same-origin track. | Code. `music.html` creates an `AnalyserNode`, calls `createMediaElementSource` on the native player, and reads `getByteFrequencyData` each frame. `canRouteAudio` gates it on not being `file://`. | Rule rewritten to draw the real line: true for the local track, false for the cross-origin embeds and on `file://`. The old wording is quoted in place. This was the clearest case in the audit of a rule that had inverted: following it would have required deleting true statements from the README and the FAQ. |
| 28 | Four stale claims in DESIGN.md: `styles.css` given as 2,282 bytes (actual 2,887 since the v2.8.7 reduced-motion block); only `lang-js` and `lang-html` described as in use (`lang-cs` joined them in v2.9.8); `.track-tag` described as reading "Drives the visualizer" (that text was removed in v2.9.4, it now carries the track credit); and build rule 4 saying "Any new page copies the nav block verbatim... There is no shared nav include yet", which v2.8.8 made false and which contradicted DESIGN.md's own navigation section. | Code, each one read in the file rather than inferred. | All four fixed. Rule 4 was replaced rather than annotated, because it instructed the reader to do the one thing Never Do These forbids. |
| 29 | The PRD gave `music.html` as "roughly 91,000 bytes" in the Build section while stating 114 KB in nine other places. The shared CSS was given as 2.3 KB. | Code. `music.html` is 114,680 bytes committed; `styles.css` is 2,887 bytes. | Both corrected. **Corrected again on 2026-09-28**: the audit first wrote 117,417 bytes, which was the working-tree copy with CRLF endings. The committed blob, which is what GitHub Pages serves, is 114,680 bytes. The rounded figure is therefore 112 KB, not 114 KB, and the nine other references were updated to match. |
| 30 | No `.gitattributes`, in a repository where `music.html` is CRLF, everything else is LF, and the nav generator preserves per-file endings on purpose. | Code and configuration. | Not created at the audit, because Repository Hygiene is a policy record rather than an action and the fix is a deliberately noisy 12-file commit. **Decided 2026-09-28: add it and normalize everything.** Scheduled as Roadmap v2.10.2 and recommended to run first, so the whitespace-only diff lands in its own commit instead of contaminating the head edits. Open Question 13 closed. **Shipped 2026-09-28 as `5070b3b`, and the finding itself was wrong.** `git ls-files --eol` shows every committed blob was already LF, `music.html` included; the CRLF was confined to the working tree and `core.autocrlf=true` was doing the normalizing. `git add --renormalize .` produced zero changes. The file is still correct to have, for the better reason that it moves the guarantee out of one machine's local config. See Repository Hygiene. |
| 31 | The PRD stated that `azqato.com` was probably unrelated to this repository, reasoning that the absence of a `CNAME` file meant this repository does not serve that domain. | The live web. `azqato.com` returns this exact site. Git history shows a `CNAME` was created and then deleted, and all 12 page footers link `azqato.com`. | Answered, and it turned into a bigger question than it was. The domain does serve this site, through Cloudflare. Which of the two hosts is canonical is now Open Question 10, and it blocks the sharing tags. |
| 32 | `tools/build-nav.py` has a `SKIP` set naming `nav-extraction-test.html` and `reduced-motion-test.html`. Neither file exists. | Code and the filesystem. | Not changed; it is harmless dead configuration in a script, not a documentation defect, and editing a working script was outside this audit's write scope. Logged in `docs/TODO.md`. |
| 36 | Every document stated the site is hosted on GitHub Pages, and the v2.9.9 audit refined that to "Cloudflare proxying in front of GitHub Pages". Both are wrong. | The owner, asked directly on 2026-09-29, plus DNS and response evidence that corroborates it: Cloudflare nameservers, Cloudflare IPs, `cfOrigin;dur=0` on every request, and a 404 that is not GitHub's. | `azqato.com` is a **Cloudflare Pages** deployment, independent of the GitHub Pages one. Corrected as v2.10.7 across the architecture diagram, hosting table, deploy verification, third-party data tables, Security Model, and `privacy-policy.html`, which had been naming the wrong data controller. Three consequences: the deploy-verification step was checking a host that cannot vouch for the canonical domain; the `CNAME` milestone was moot, not blocked; and the "no CSP possible" constraint is false for `azqato.com`, which supports a `_headers` file. |
| 35 | The 11 non-index canonical and `og:url` tags shipped in v2.10.4 pointed at `https://azqato.com/page.html`, which the canonical domain 307-redirects to `https://azqato.com/page`. The 11 matching `sitemap.xml` entries had the same problem. | The live site, which is the only source that could have answered this. A Cloudflare rule strips the extension; it is not in this repository and is not documented anywhere. | **Fixed the same day as v2.10.6**, before anyone could have shared a link. Both hosts return 200 on the extensionless form, so the repointed URLs are correct on the origin too. Found by checking the deployed site rather than by checking that the deploy landed, which is the distinction now written into the Verification checklist. Internal links still use `.html` and still redirect; that is deliberate and tracked in `docs/TODO.md`. |
| 34 | All 12 page titles are brand-first with a pipe separator (`Azqato \| Projects`), so every tab truncates to the same visible string and the pixel budget is spent on the one word that is identical everywhere and already shown by the favicon. Two page names, "Welcome" and "Codes", identify nothing to a stranger. | The specification's Page Titles rule, read in full after the owner supplied it. This section had never been recorded in this project, so there was no existing project rule to defer to. | Policy written into the new Page Titles section with the current state of all 12 titles tabulated. **Decided 2026-09-28: fix the titles**, in the same pass as the sharing tags, since both edit the same heads. Replacement titles are specified in Roadmap v2.10.4. Not applied at the audit: changing a title is a page edit, which the specification puts outside an audit. **Applied 2026-09-28** in that milestone. Every title is page-first with a ` - Azqato` suffix; the longest is 38 characters against a 60 character budget; no two share their first 30 characters. "Welcome" and "Codes" became "Azqato - Communities, Projects, Music" and "AI Prompts and Coding Tools - Azqato". Resolved. |
| 33 | No `CLAUDE.md` and no `/dashboard`. | Filesystem. | Neither was created. A `CLAUDE.md` is not created by an audit for a project that has none. Because no progress dashboard convention exists, the standing rule was not added either; instead a Future Updates roadmap entry proposes one, built from the linked prompt. |


---

# Risks and Open Questions

## What was not fully understood

- **The GLSL shader source in `music.html`.** Roughly 700 lines of fragment shader code across nine modes, much of it adapted from public sources under CC0, MIT, and CC-BY-NC-SA licenses. The audit verified what each mode is called, where its output goes, how modes are selected, and what license each carries. It did not verify what any individual shader computes mathematically. Treat these as opaque assets: they can be swapped or removed wholesale, but editing their internals is a specialist job.
- **Whether GitHub Pages actually serves the dot-directories.** Default Jekyll processing excludes them and there is no `.nojekyll` file, so `.vscode/` and `.githooks/` are probably not reachable. This was reasoned from how GitHub Pages works, not tested against the live site. It matters only for Open Question 1.
- ~~**Whether `azqato.com` is related to this repository.**~~ **Resolved at the v2.9.9 audit, and the mechanism corrected 2026-09-29.** It is this repository: `https://azqato.com/` returns these exact files. The absence of a `CNAME` was read as evidence the domain was unrelated, which was wrong. The audit then guessed the mechanism was Cloudflare proxying in front of GitHub Pages, which was also wrong. It is a **separate Cloudflare Pages deployment** of the same repository. The `CNAME` file is irrelevant to it either way, since that is a GitHub Pages mechanism. `azqato.com` is now the canonical domain. The original note follows. Every page's footer links to `https://azqato.com/`, but there is no `CNAME` file, so this repository does not serve that domain. Whether it is a separate site, a redirect to `azqato.github.io`, or a dead link is unknown and was not tested.
- **Live link validity.** No external link was clicked. Affiliate URLs, Discord invites, and the roughly 90 resource links on `invests.html` were verified to be well-formed and to match what the documentation claims, not to resolve.

## Fragile areas

| Area | Why it is fragile | What breaks if you are careless |
|------|-------------------|----------------------------------|
| The nav toggle script, duplicated in 12 files | The markup is stamped now, but the toggle IIFE is still copied by hand and nothing checks it | A page whose hamburger does nothing below 860 px, with no error to notice |
| `music.html` `build()` and `lay` | Roughly 60 interdependent coordinates computed from viewport dimensions; the booth, floor, reflection, and screens are all positioned relative to each other | Changing one ratio detaches the booth from the floor or makes the reflection ghost, which is what v2.8.1 was spent fixing |
| `drawReflection()` and the booth clip | The fix for reflection ghosting is a clipped hole over the booth footprint, tied to booth geometry | Moving the booth without moving the clip brings the ghosting back |
| `projects.html` `PROJECTS` array | No validation, no error handling; a syntax error stops rendering entirely | An empty projects page with only a console error to explain it |
| `styles.css` | One file now, loaded by every page | A bad edit breaks all 12 pages at once. This is the trade made in v2.7.0 and it was the right one, but it is worth knowing. |
| The pre-commit hook | Not enabled by cloning; requires a manual `git config` per clone | The writing policy silently stops being enforced with no warning |
| The unthrottled render loop | Runs at full rate whenever `music.html` is open | Battery drain on laptops, heat on phones, and no way for a visitor to stop it |

No file in the repository contains a `TODO`, `FIXME`, `HACK`, or `XXX` marker. That is unusual and it is genuine, not the result of a filtered search.

## Dangerous to change without more context

- **Any affiliate URL or referral code.** A typo silently breaks attribution: the link still works, the visitor still signs up, and the referral is simply never credited. There is no error and no way to notice except a partner dashboard that stays at zero.
- **The two Mixcloud feed URLs.** They are percent-encoded paths to specific mixes. A wrong character yields a player that loads and shows nothing.
- **Any live page filename.** With no redirect mechanism in place, renaming a page breaks every link posted in Discord, in video descriptions, and anywhere else, permanently and invisibly. Read the Deprecation and Removal policy first.
- **The `feature/native-audio-player` branch.** It is roughly a session's worth of tuned work (a kick detector calibrated against a real track with `ffmpeg`) that exists only there. Do not delete it, and do not rebase it away.

## Work in progress at audit time

- **Untracked in the working tree:** `music/` (the owner's local source audio, including the file that became `audio/womanchild-azqato-remix.mp3`) and `test-local-audio.bat` (launches Chrome with web security disabled so a `file://` load can route local audio). Neither is committed and neither should be. The batch file is a workaround for a problem now handled in the page itself, and serving over http is the supported route; see the Build section.
- **Unmerged branch:** `feature/native-audio-player`, pushed to GitHub, complete but unshippable. Documented above.
- **Half-finished milestone:** v2.7.0, CSS extracted, nav not.
- **Dead code in the tree:** five hidden visualizer modes (Bars, Volumetric, Origami, Ghost, Noise) whose buttons are `display:none` and which the auto-cycle skips. The modes are complete and working, just not exposed; they are hidden by choice, not broken.

## Open questions

Numbered so they can be answered by reference. When one is answered, fold the answer into the relevant section and mark it answered here rather than deleting it.

1. ~~**`.vscode/recentfedsummary.MD`** is a personal summary of a finance video, tracked in git, unrelated to the site, and carrying 13 em-dash violations of the project's own writing policy.~~ **Answered 2026-08-29, done in v2.8.9.** Deleted from the repository. It remains recoverable from git history.
2. ~~**Ten unreferenced images**, roughly 3.8 MB including a 1.9 MB GIF that appears in no documentation. Are these staged for planned use or are they leftovers?~~ **Answered 2026-08-29.** They stay, and so does anything else added to `img/` later. This is a standing rule rather than a per-file answer: nothing in `img/` is deleted unless the owner explicitly asks for it. Unreferenced files there are the owner's working library, not stale assets, and an audit finding one unused is not evidence of anything. The removal policy's plain internal delete does not apply to that folder.
3. ~~**The Mixcloud embeds** are the only thing preventing the site from making a true zero-external-request claim, and they load before any visitor interaction. Should they become click-to-load?~~ **Answered 2026-08-29.** Neither option. The embeds are going away: the owner is supplying standalone audio files to be played directly on the page, which removes the third party rather than gating it. Tracked as milestone v2.9.0, which this also unblocks. Do not spend effort on click-to-load or on tightening the iframe `allow` list in the meantime, because both would be work on code scheduled for deletion.
4. ~~**`wrangler.jsonc`.** Is Cloudflare Workers an intended alternative or future host, or the residue of an autoconfiguration pull request that was merged and forgotten?~~ **Answered 2026-08-29, done in v2.8.9.** Residue. Deleted, along with the wrangler-specific `.gitignore` patterns that arrived with it. An untested deploy path implies a safety net nobody has checked, and the site needs no configuration file to move hosts.
5. ~~**Leveraged Strategies has two URLs**: `/leveraged-strategies/` from `projects.html` and `/leverage/` from `invests.html`. Which is canonical?~~ **Answered 2026-08-29, fixed in v2.8.9.** `/leverage/` is canonical. Both were checked against the live web rather than assumed: `/leverage/` returns the page titled Leveraged Strategies, and `/leveraged-strategies/` returns a hard 404, so `projects.html` had been shipping a dead demo link since the v2.6.12 rename. The GitHub repository was renamed too. `github.com/Azqato/leveraged-strategies` still resolves because GitHub redirects renamed repositories, but GitHub Pages does not do the same for Pages URLs, which is exactly why one link broke and the other did not. Both fields on the card now point at `leverage`. No compatibility entry was added at the old path because no repository serves it, so there is nowhere to put one.
6. **The privacy policy** describes ad networks, DoubleClick cookies, account registration, and marketing emails, none of which exist here. It is dated "2024" while the rest of the site is dated 2026. Should it be rewritten to describe what the site actually does (which would be shorter, more honest, and more in keeping with Tenet 6), or is generic over-disclosure the deliberate safe choice?
7. **Automated smoke tests** were deferred with an explicit threshold: "candidate at 11 pages". The site now has 12. Is that threshold still the plan, or has manual QA proven sufficient enough to drop the idea?
8. **`music.html` accessibility.** ~~The page animates continuously with strobes and flashes, has no pause control, and honors no reduced-motion preference. Is a play/pause control acceptable on a page whose whole point is the animation, or should the reduced-motion media query simply freeze the canvas on the first frame?~~ **Answered 2026-08-29, shipped in v2.8.7.** The play/pause control won. Three candidates were built into a local harness and compared: freeze on first frame, start paused with a control, and a calm mode that kept slow motion but dropped strobes and lasers. The control was chosen because it is the only one of the three that also satisfies WCAG 2.2.2 (Pause Stop Hide, Level A) for the majority of visitors who never set a reduced-motion preference. Freezing would have satisfied the preference while leaving that criterion unmet for everyone else. See the Animation and Motion section of DESIGN.md for the shipped behavior. The one follow-up that remained open, measuring the real beat flash rate against WCAG 2.3.1, **was closed in v2.9.3 and the page was found to be in breach**: 4.70 flashes per second on a 120 Hz display against a limit of three, because the refractory was counted in frames rather than milliseconds. Now 1.70 at any refresh rate.

9. ~~**The licence posture contradicts the site's own copy.**~~ **Answered 2026-09-28: keep all rights reserved.** `LICENSE.md` stands as written, and the copy was reworded to match it rather than the reverse. The README now points at `LICENSE.md` instead of inviting reuse, the External FAQ separates this site (source-available) from the individual projects (mostly public repositories with their own licences), and the press release boilerplate no longer says everything he builds is open source. Applied at the audit as v2.10.0. The original question follows.
    `LICENSE.md` was created at the v2.9.9 audit with the all rights reserved, source-available default, because the project had no licence text of any kind. But the README ends with "The source is open. Read it, copy it, or use it as a starting point for your own site," and the External FAQ says "The site and nearly every project on it are open source at github.com/Azqato." Which is it? If reuse is genuinely intended, `LICENSE.md` should be replaced with a real permissive licence, most likely MIT, and the invitation becomes true instead of merely stated. If the reservation is right, those two sentences need rewording. This is the question to answer first, because every other licensing sentence in the project depends on it. See the Licensing section.

10. ~~**Which domain is canonical?**~~ **Answered 2026-09-28: `azqato.com`.** The branded domain wins, which is also what all 12 page footers already assumed. This unblocked the sharing tags. Shipped as Roadmap v2.10.3. **The "it can take the site down" warning below was wrong**, and was withdrawn on 2026-09-29: it assumed a `CNAME` file was involved, and a `CNAME` is a GitHub Pages mechanism that has no bearing on `azqato.com`, which runs on Cloudflare Pages. Nothing about this milestone was ever capable of taking the site down. The original text follows. `sitemap.xml` and `robots.txt` still say `azqato.github.io` and are repointed as part of that milestone. The original question follows.
     Both serve this site and both return 200. All 12 page footers link `azqato.com`. The README's live link, the Runbook, the Deploy section, the Rollback section, and every row of the Monitoring table name `azqato.github.io`. There is no `CNAME` file in the repository, though git history shows one was created and later deleted, and `azqato.com` resolves through Cloudflare while `azqato.github.io` is served directly by GitHub. The audit used `azqato.github.io` in `sitemap.xml` and `robots.txt` because that is what this repository's own documents name and what the repository name implies, but that is a defensible default, not an answer. Answering it settles Open Question 11 and unblocks the sharing tags. It probably also means restoring a `CNAME`, adding `rel="canonical"` to all 12 pages, and deciding whether the other host should redirect.

11. ~~**Social sharing tags: all 12 pages have none.**~~ **Answered 2026-09-28: add the full set to all 12 pages.** Scheduled as Roadmap v2.10.4, together with the title rewrite, since both edit the same 12 heads. Reading the full specification also settled the image question that had been left open: images are off by default, so there is no `og:image` and `twitter:card` is `summary`. The original question follows.
     Not one `og:` tag, `twitter:` tag, meta description, or canonical tag exists anywhere in the project. Links shared to Discord, which is where this site's traffic comes from, render as bare URLs. The policy is now written under Social Sharing Tags and the pages were deliberately not touched, because `og:url` has to be the absolute URL of each page and Open Question 10 decides what that is. This is ready to implement the moment the domain question is answered.

12. ~~**`azqato.com` serves a Cloudflare Web Analytics beacon, and the site says it has no analytics.**~~ **Answered 2026-09-28: keep the beacon, fix the copy.** The Cloudflare setting stays on and the site stops claiming it has no analytics. The README was made precise at the audit, and the PRD Security section, the External FAQ, the press release, and the north-star metric note were aligned with it as v2.10.0. The remaining piece is `privacy-policy.html`, which is Roadmap v2.10.5, and which is now the page that has to carry the real disclosure. The original question follows.
     Verified at the v2.9.9 audit: `https://azqato.com/` and `https://www.azqato.com/` both return `server: cloudflare` and both contain a `static.cloudflareinsights.com/beacon.min.js` script tag. `https://azqato.github.io/` does not; it is clean. The beacon is not in this repository's source, so nothing was committed by mistake: it is injected at the edge by a Cloudflare setting. That makes the README's "no analytics, and no tracking", the PRD's "No analytics, no cookies set by the site, no tracking pixels", the External FAQ's Why No Analytics answer, and the press release's "collects nothing about the people who use it" all false for anyone who visits the branded domain, which is the domain every page footer links. Either the Cloudflare setting is turned off, or the copy stops claiming no analytics. Tenet 6 does not leave a third option. The README was made precise about this at the audit rather than left false; the underlying decision is still open.

13. ~~**There is no `.gitattributes`, and line endings are already inconsistent.**~~ **Answered 2026-09-28: add it and normalize everything**, accepting the one noisy commit. Shipped the same day as `5070b3b`. **The premise was wrong and the noisy commit never materialized**: every committed blob was already LF and the inconsistency was confined to the working tree, so `git add --renormalize .` changed nothing. The file still earns its place by making the LF guarantee portable instead of dependent on one machine's `core.autocrlf=true`. See Repository Hygiene for the full correction. The original question follows.
     `music.html` is committed CRLF, everything else is LF, and `tools/build-nav.py` contains deliberate code to preserve each file's existing endings. Adding `* text=auto eol=lf` would normalise this and produce a 12-file diff including a full-file diff on `music.html`. Worth it, or not worth burying the next real diff on that page? See Repository Hygiene.

14. ~~**The sharing-tag specification was truncated before the image rules.**~~ **Answered 2026-09-28: the full specification was read.** The owner supplied its location and it was read in full rather than reconstructed. Two things turned out to be missing rather than one: the image rules (**images are off by default**, no `og:image`, `twitter:card` is `summary`, with the full 1200 by 630 requirement set recorded in case an image policy is adopted later) and an **entire Page Titles section** that this project had never recorded and fails on all 12 pages. Both are now written into this document. The original question follows.
     The prompt this audit's Social Sharing Tags policy was written from was cut off mid-sentence at the image section, so `og:image` and `twitter:image` have no recorded rule: no dimensions, no budgets, no fallback. The policy says so explicitly rather than inventing values, because invented budgets become the standard that every later page is checked against. Supply the rest and the section can be completed. Nothing else in the policy is affected.

---

# Working Practice

Concrete instructions for whoever works on this next, human or model.

## Before editing anything

1. **Read the page you are about to change, in full.** They are 6 KB to 24 KB; there is no excuse for skimming. `music.html` is the exception at 112 KB: read the section you are touching plus `build()`, because almost everything depends on `lay`.
2. **Check whether the change touches the nav.** If it does, it touches 12 files, and missing one is the single most common defect in this repository's history.
3. **Confirm the pre-commit hook is live:** `git config core.hooksPath` should print `.githooks`. If it prints nothing, the writing policy is not being enforced in your clone.
4. **Check `git status`.** `music/` and `test-local-audio.bat` are expected to be untracked. Anything else unexpected deserves a look before you add files.

## Which document to read first

| Kind of change | Open this first |
|----------------|-----------------|
| Adding or editing a project card | This file, Data Models, Project Entry |
| Adding a Discord server | This file, Data Models, Discord Server Entry |
| Adding or changing an affiliate partner | This file, Data Models, Affiliate Card, plus Tenet 4 |
| Any color, spacing, type, or component change | `DESIGN.md` |
| Adding a new component or card type | `DESIGN.md`, Component Patterns, and reuse one before inventing one |
| Adding a new page | This file, Site Structure, plus DESIGN.md's nav rules |
| Removing or renaming anything | This file, Deprecation and Removal |
| Anything on `music.html` | `DESIGN.md`, the `music.html` Visual System section |
| Deploying, reverting, or debugging a deploy | This file, Operational Runbook |
| Writing any prose at all | This file, Writing Style |
| Understanding why something is the way it is | This file, Product Tenets, then `PATCHNOTES.md` |

## Never do these

- **Never delete anything from `img/`.** Not an unreferenced file, not an apparent duplicate, not an obvious leftover, no matter how confident an audit is that nothing links it. That folder is the owner's working library and unused is its normal state. Remove a file from it only when the owner asks for that file by name.
- **Never add a dependency, a CDN script, or a web font** without a decision recorded here first. Tenets 1 and 2 exist to make this a conversation rather than a habit.
- **Never rename or delete a live `.html` file, `styles.css`, or a referenced image without a compatibility entry.** Inbound links live in Discord messages and video descriptions where they cannot be updated and their breakage cannot be observed.
- **Never hand-edit the nav in a page.** It is generated. Edit `PAGES` in `tools/build-nav.py`, run the script, and commit the result. A hand edit survives until the next run and then vanishes without warning.
- **Never bypass the pre-commit hook** with `--no-verify` except when the text genuinely requires the character it is blocking (a rule quoting itself). The hook exists because a previous audit found violations that a manual search had missed.
- **Never claim the visualizer reacts to audio it cannot hear.** The claim is now true for the one same-origin track in `audio/`: `music.html` builds a real `AnalyserNode`, calls `createMediaElementSource` on the native player, and drives the lights from `getByteFrequencyData`. It is still false for the Mixcloud and YouTube embeds, whose audio is cross-origin and unreadable, and it is false on `file://`, where the page sets `canRouteAudio` false and shows a note saying so. Say "the track", never "the mixes". Tenet 6 applies to marketing copy first.
  > **Replaced in v2.9.9.** This entry previously read: "**Never claim in copy that the music visualizer reacts to the audio.** It does not, and Tenet 6 applies to marketing copy first." That was written before the native player shipped and had become the opposite of the truth, contradicting both the README and the External FAQ. A rule that forbids a true statement is worse than no rule.
- **Never commit `test-local-audio.bat` or anything under `music/`.** The batch file launches a browser with web security disabled, and the audio files are multi-gigabyte.
- **Never introduce `innerHTML` with a value from outside the file.** The one existing use is safe only because its data is hardcoded.
- **Never push to `main` without reading the diff.** There is no staging, no review, and no CI. The push is the release.

## How to verify a change

There is no test suite, so verification is manual and specific. **Testing Cadence decides when this list runs; this section is what it contains.** For a major update, work through all of it once, after the batch of edits is finished rather than after each one. For a minor update, meaning documentation, comments, copy, or patch notes, none of it applies.

> **Changed in v2.9.9.** This paragraph previously read: "There is no test suite, so verification is manual and specific. Do all of these:" and the Monitoring table required a DevTools console check "After each change". Together those mandated a browser test after every edit, and no project-specific reason was recorded for the frequency, so the Testing Cadence default replaced it. The steps themselves are unchanged.

```bash
# 1. Serve locally rather than using file://
python -m http.server        # then open http://localhost:8000

# 2. Check the page weight of anything you touched
```
```powershell
Get-ChildItem *.html | Select-Object Name, Length | Sort-Object Length -Descending
```

3. **Open the changed page** and confirm the change renders. Open DevTools Console and confirm it is clean; zero console errors is the standard on every page.
4. **Resize through both breakpoints.** Drag the window past 860 px to confirm the nav collapses and the hamburger opens, then past 600 px to confirm padding tightens. Use a 375 px device emulation for the mobile check.
5. **If you touched the nav**, run `python tools/build-nav.py --check` and confirm it prints `nav is up to date in every page`. Then load two or three pages, including one not in the nav (`accounts.html`), and confirm the item list and active state look right.
6. **If you touched `projects.html`**, click every filter button and confirm the count in the section header matches the visible cards.
7. **If you touched `music.html`**, watch it for a full 30-second cycle to confirm the mode auto-switch still works, click each visible mode button, and resize the window at least once to confirm `build()` re-lays the stage without artifacts.
8. **If you added an external link**, click it.

## After the change

1. **Add a `docs/PATCHNOTES.md` entry.** Newest at the top, `## [x.y.z] - YYYY-MM-DD`, with Added / Changed / Fixed / Removed subsections as applicable, written in past tense.
2. **Pick the version number by taking the next free patch**, skipping any number the Roadmap reserves for a planned milestone. `2.9.0`, `2.9.5`, and `3.0.0` are reserved; `2.9.0` is additionally taken by the unmerged branch entry, and `2.9.5` is held for the visualizer brightness gate.
3. **Check `docs/TODO.md` before pushing** and strike anything the change actually finished, or add what it uncovered. Then **ask whether any of its ideas should become researched Roadmap entries**, rather than either acting on them or leaving them to rot: a TODO item that has been sitting there for three audits is telling you something, and the answer is either a Roadmap entry with an effort estimate or a deliberate decision not to do it. It is a holding place, not a work queue: nothing there is picked up because it is listed, only because the owner asks. Note that this project has no `CLAUDE.md` and no `/dashboard`, so there is no third place to keep in sync.
   - **Mark what you verified.** When a change touches an area of the code, check that area's PRD or DESIGN.md section against the code in the same session, record any discrepancy you find, and mark that section verified with the date on the Roadmap's verification checklist. Only the sections the change touches, never the whole list at once: a checklist ticked wholesale is a checklist that means nothing.
4. **Sync the documents the change touches**, in the same commit:
   - New page: Site Structure table, folder tree, public surface list, feature list, and README if it changes what a visitor gets.
   - New component or changed CSS value: `DESIGN.md`.
   - Changed third-party link, invite, or referral: the relevant data model table and the Third-Party Integrations table.
   - Completed roadmap item: move it in the milestone table.
5. **Commit with a descriptive single-line subject**, including the version, and the `Co-Authored-By` trailer if an assistant did the work.
6. **Ask before pushing.** The push is the release; there is no staging and no review.
7. **After the push**, confirm the deploy arrived with a hard refresh. That is a comparison against what was already verified locally, not a test of the change. See Verification Environment.

---

# Press Release

*Written as if the site had just launched publicly. This section is a communication exercise, not a record of an actual announcement.*

**Azqato launches a single home for his communities, projects, and music.**

*One address now connects the Discord servers, the open-source tools, the DJ mixes, and the investing resources that used to live on eight different platforms.*

**Boston, MA. June 6, 2026.** Azqato, a content creator, community builder, and self-taught web developer, has launched azqato.com, a personal site that gathers everything he makes into one place. Visitors can join any of four Discord communities, browse fifteen free browser-based tools and educational sites, watch four YouTube channels, listen to DJ mixes on an animated concert stage, and dig through a hand-picked library of investing resources. The site loads in under a second, collects nothing about the people who use it, and is free to browse in full.

**The problem.** If you found Azqato through a RuneScape clan, a Twitch stream, a DJ mix, or a finance tool you stumbled onto, you found one piece of a much larger thing, and no way to find the rest. Each platform is a cul-de-sac: YouTube does not tell you about the Discord, the Discord does not tell you about the tools, and the tools do not tell you a person made them. People who wanted more had to already know what to search for.

**The solution.** The site is a front door with twelve rooms behind it. The landing page explains who Azqato is in a few sentences and hands you a grid of destinations. Every room does one job: the Discord page lists all four servers with what each is for, so you join the right one instead of guessing. The Projects page shows every tool he has built with a working demo link and the source code, filterable by what you care about. The Invests page carries the free finance tools alongside a curated hub of brokers, screeners, and learning resources, under a plain statement that none of it is financial advice. The Music page is a full-screen concert stage, lasers and all, with the mixes playing right there in the page. Nothing asks you to sign up, and nothing tracks you.

**Customer quote.** "I joined the B5TA clan back in 2016 and I honestly had no idea he built anything," said Marcus Webb, a longtime community member. "Somebody dropped the link in the Discord and I went through the whole site in one sitting. I ended up using the net worth tracker for three months straight. It is genuinely the tool I would have paid for, and it is just sitting there for free."

**Call to action.** Visit https://azqato.com/. Start with the Discord page and join whichever community fits, or go straight to Projects and open something.

**About Azqato.** Azqato is a content creator, investor, and web developer building communities and free browser-based tools. He streams on Twitch, runs four YouTube channels, DJs under his own name, and founded Clan B5TA, a RuneScape community that has been running since 2014. Everything he builds runs entirely in the browser and is free to use, and most of the projects are public on GitHub.

---

# Frequently Asked Questions

## External FAQ

**What is this site?**
Azqato's personal hub. It introduces who he is, then routes you to his projects, community Discord servers, YouTube channels, DJ mixes, investing resources, and ways to support the work.

**I just landed here. Where do I start?**
The landing page links to every part of the site. The best first stop is the Discord page, where you can pick the community that matches your interests and join it.

**Who is this for?**
Three groups: people who know Azqato from Twitch, YouTube, Discord, or the B5TA RuneScape clan; developers and recruiters looking at his work; and anyone who came for the free investing tools.

**How do I use it, step by step?**
Open the landing page, read the short intro, and pick a destination from the explore grid or the top navigation bar. Every page is one click from every other page. Nothing requires an account and nothing requires a sign-up.

**What does it cost?**
Nothing. Every page, every tool, and every resource is free, and there are no paid tiers, no premium features, and no paywalls. There is a Support page with a Buy Me a Coffee link and some referral links, all of which are entirely optional.

**Is it available everywhere?**
Yes. It is a public website with no regional restrictions and no login. It has been live since June 6, 2026.

**What data does the site collect about me?**
Nothing from the site's own code: no analytics script, no cookies set by the site, no tracking pixels, no forms, and no accounts. Two things sit outside that code and are collected anyway. GitHub, which hosts the repository, logs standard server-level request data (IP address, browser, referring page) as part of running any web server. And **`azqato.com`, the canonical domain, is served through Cloudflare, which runs Web Analytics and injects a beacon script into every page.** That beacon is not in this repository; it is added at the edge by a Cloudflare setting. Verified at the v2.9.9 audit: `azqato.com` and `www.azqato.com` both serve it, `azqato.github.io` does not. Keeping it was a deliberate decision on 2026-09-28; see Open Question 12.

**How to check this, because the obvious check gives the wrong answer.** Re-verified on 2026-09-28 after the v2.10.6 deploy. The beacon is injected **only when the request sends an `Accept: text/html` header.** A plain `curl https://azqato.com/` does not send one, gets a page with no beacon, and looks like proof the analytics were turned off. That result is an artifact of the request, not a fact about the site. Every real browser sends the header, so every real visitor gets the beacon, and the privacy policy is accurate as written. The check that actually answers the question is `curl -H "Accept: text/html" https://azqato.com/ | grep cloudflareinsights`, which returns the script tag deterministically, against `https://azqato.github.io/` which returns nothing with or without the header. **Do not "correct" the privacy policy or these sections on the strength of a bare `curl`.** The user agent alone does not change the outcome; the `Accept` header does.

**Then why does the Music page load something from Mixcloud?**
The two mixes on that page are embedded Mixcloud players, so playing them works without leaving the site. Those two players are the only thing on the entire site that loads from an outside company, and they see your IP address and browser the way any embedded player does. Every other page loads nothing external.

**What do I need to run it?**
Any modern browser: Chrome, Firefox, Edge, or Safari. It works on phones, tablets, and desktops. The Music page's visualizer needs WebGL2 for its best modes and falls back to a simpler view without it. Nothing needs to be installed.

**Does the Music page visualizer react to the music?**
It depends on which thing is playing, and it is worth being clear about it. The remix served by the site itself is read by the page, so the lights genuinely move with it. The two embedded Mixcloud mixes are not and cannot be: a web page cannot read the audio out of another company's player, so while one of those is playing the stage is choreography rather than reaction. The kick, in particular, is detected rather than guessed at, so the stage hits when the drum does.

**What are the affiliate links on the Support page?**
Referral links for services Azqato personally uses or recommends. If you sign up through one, you typically get the same sign-up bonus you would get anyway, and Azqato earns a referral commission. There is no extra cost to you, and the disclosure sits at the top of the page rather than in the footer.

**Where do Buy Me a Coffee funds go?**
Azqato has stated he intends to invest contributions in the stock market for long-term growth. That is a plan, not a guarantee, and the page says so.

**Is the investing content financial advice?**
No. Azqato is not a licensed financial advisor, accountant, or lawyer. Everything on the Invests page and in the finance projects is for informational and entertainment purposes. The disclaimer appears on the Invests page above the resources and again in the privacy policy.

**Can I use the tools without giving up any data?**
Yes. The browser tools linked from the site (the net worth tracker, the protein tracker, the utilities collection) run entirely on your own device. Where they save anything, it stays in your own browser's storage.

**Can I view the source code?**
Two different answers, because they are two different things. **The individual projects** are mostly public repositories at github.com/Azqato, each carrying its own licence; check the repository you care about. **This site itself** is source-available rather than open source: every line is readable in the `azqato.github.io` repository, documentation included, and that is deliberate, but reading is not a licence to reuse. `LICENSE.md` reserves all rights and sets out what is granted, which includes quoting and referencing the site freely. If you want to reuse part of it, open an issue and ask; the answer is usually yes.

**How is this different from a Linktree or a GitHub profile?**
A Linktree is a list of links with no context and someone else's branding. A GitHub profile shows repositories without explaining what any of them do or who they are for. This site gives each thing a description, a working demo, and a reason to click, and it loads faster than either.

**What does it not do?**
There is no contact form, no search, no comments, no accounts, no newsletter, and no way to interact with other visitors. It is something to read and navigate, not something to participate in. The Discord servers are where participation happens.

**Something is broken or a link is dead. How do I report it?**
Open an issue on the repository at github.com/Azqato, or mention it in any of the Discord servers. There is no support inbox and no ticketing system; the site is maintained by one person.

**How often does it change?**
Regularly. New projects, links, and pages get added as they exist. Every change is logged with a date in the patch notes in the repository.

## Internal FAQ

**Why build a custom portfolio instead of using a GitHub profile, LinkedIn, or a page builder?**
Developer-first aesthetic and zero maintenance overhead. Existing platforms do not allow precise visual control, and page builders add bloat that contradicts the first tenet. A hand-coded site is the fastest option and the most credible signal to other developers.

**Why inline CSS and JS instead of separate files?**
With a small number of pages at launch, separate files added deployment complexity with no benefit, and each page being self-contained made it easier to read and modify. The site has since grown to twelve pages, so as of v2.7.0 the CSS that was identical everywhere (tokens, reset, nav, footer) lives in a shared `styles.css`. Page-specific styles remain inline. The nav markup and its toggle script are still duplicated in every page; extracting those is the outstanding half of that milestone, and it is blocked on a genuine trade-off rather than on effort.

**What analytics does the site use?**
None in its own code, and one at the edge. The site ships no analytics script, sets no cookies, and has no tracking pixels: that was the original position and it still describes the source. But the canonical domain `azqato.com` is served through Cloudflare with Web Analytics switched on, so a cookieless beacon is added to every page before it reaches you. That was kept on purpose in September 2026, and the honest description of the site is now "no tracking of its own, plus cookieless aggregate counts from the CDN" rather than "no analytics". GitHub's repository Insights remain the other coarse traffic source. The earlier absolute claim is corrected rather than defended, because Tenet 6 does not leave room for a claim that is technically about the source while being false about what a visitor receives.

**What is the return on this? Why spend time on a site with no revenue?**
Three returns, in order of size. First, routing: it converts scattered platform traffic into Discord members, which is the community that everything else depends on. Second, credibility: it is the artifact shown to anyone evaluating the work, and it demonstrates competence more directly than a resume. Third, and smallest, the affiliate and Buy Me a Coffee channel, which is real but modest and is explicitly the third priority rather than the first.

**How does the site monetize without feeling like an advertisement?**
The Support page is separate and clearly labeled, and visitors arrive there by choosing to. The disclosure sits above the fold in plain language. No promo badge claims a benefit that has not been verified, which is why the newest card describes the service rather than promising a bonus.

**What assumption must hold for the affiliate channel to work?**
That community traffic converts and cold developer traffic does not. Visitors from Twitch, YouTube, and B5TA already have an affinity for Azqato and are the plausible converters. If the site ends up discovered mainly by developers evaluating code, the affiliate channel underperforms and the site is still worth having for the other two returns.

**What happens if an affiliate program changes or cancels a link?**
The link is hardcoded in `support.html`, so it needs a manual edit and a commit. That is the correct trade for a project with no backend, and it is why link validity is on a monthly manual check in the Monitoring table.

**What is the plan if GitHub Pages goes away or starts charging?**
The entire site is plain files. It moves to Cloudflare Pages, Vercel, or Netlify in under five minutes with no configuration changes and nothing to port. There is no lock-in of any kind.

**How are new projects added?**
Add one object to the `PROJECTS` array in `projects.html`, commit, push. Two to five minutes, and the field documentation sits in a comment directly above the array so it never requires opening these docs.

**How are new Discord servers added?**
Copy a `.server-card` block in `discord.html`, change the icon, name, description, and invite URL. Under five minutes.

**What are the success metrics and how are they reviewed?**
Monthly unique visitors is the north star, with Support page visit rate, Discord joins, and affiliate conversions beneath it. Traffic and affiliate dashboards are reviewed monthly, Lighthouse quarterly, page weight on every push. Full detail in Metrics.

**What is the roadmap direction?**
Maintenance and content growth, plus finishing the shared-assets milestone. The one substantial unshipped feature is the native audio player, which is complete on a branch and blocked on audio hosting rather than on engineering. Beyond that: a contact section, and possibly GitHub API integration if the manual star and date fields ever become annoying enough to justify the XSS work they would require.

**Why is there still no contact form?**
The GitHub profile and the Discord servers already provide contact paths. A form needs a backend or a third-party service, which conflicts with the zero-dependency tenet. It is deferred to v3.0.0, where the likely answer is an obfuscated email link rather than a form.

---

# Documentation Process

This section describes the documentation structure and how it is maintained. It was adopted in v2.5.0, reaffirmed and expanded by the full audit in v2.8.5.

## File structure

```
/project-root
├── README.md          - public front door, general reader; always root-level, never in /docs
└── /docs
    ├── PRD.md         - all product, architecture, operational, and process documentation
    ├── DESIGN.md      - design system, tokens, component patterns
    ├── PATCHNOTES.md  - versioned changelog
    └── TODO.md        - open work and unresolved decisions
```

Exactly five documents: the README at root and four in `/docs`. No sixth file is created inside `/docs`. All new reference content goes into a section of PRD.md, DESIGN.md, or PATCHNOTES.md, or into the README if it changes what a visitor gets.

> **Changed in v2.9.9.** This block previously listed three files in `/docs` and read "Exactly four documents. No fifth file is created inside `/docs`." `docs/TODO.md` was added by the v2.9.9 audit as a required file, which made the old wording self-contradicting. TODO.md is the last addition: it is a holding place for open work, never a reference document, and it is never consolidated into the others, merged, moved, or deleted.

## What goes where

**README.md** is written for a general reader deciding whether to care, not for a developer. It covers what the site is, the live link, what each part offers in plain language, who it is for, its current status, and a pointer to `/docs`. It deliberately carries no commands, no install steps, no ports, no environment variables, no version numbers, and no dependency lists. Everything it omits is one link away, and brevity wins ties there.

**docs/PRD.md** is the source of truth for everything else and is the one document where completeness beats brevity: product requirements, architecture, data models, conventions, writing style, browser testing, security, removal policy, runbook, metrics, roadmap, tenets, the press release, the FAQs, the discrepancy log, the open questions, and this process. A reader may arrive at any section directly, so a section that restates context to stand on its own is doing its job.

**docs/DESIGN.md** covers only visual and UX decisions: tokens, typography, spacing, breakpoints, component patterns, image assets, accessibility, and motion. When a CSS value changes in the source, the matching row changes here in the same commit.

**docs/PATCHNOTES.md** is a running log of every change. One entry per version, dated, in past tense.

## Patch note conventions

- Heading format: `## [x.y.z] - YYYY-MM-DD`, using a single hyphen.
- Subsections: **Added**, **Changed**, **Fixed**, **Removed**, in that order, omitting any that do not apply. Some historical entries use a descriptive heading instead (`### Added: stage console panel`); both forms appear and both are acceptable.
- One line item per change, written in past tense, naming the file it touched.
- New entries go at the top of the file. Note that the middle of the file is not in strict order, a result of several renumbering passes; that history is left as it is rather than rewritten.
- Version numbers take the next free patch and skip numbers the Roadmap reserves.

## Maintenance rules

1. When adding a page: add a row to the Site Structure table, the folder tree, and the public surface list in PRD.md, plus a PATCHNOTES entry, plus a README row if it changes what a visitor gets.
2. When adding a component: document its pattern in DESIGN.md under Component Patterns.
3. When a CSS value changes: update DESIGN.md in the same commit.
4. When changing the nav: edit `PAGES` in `tools/build-nav.py`, run `python tools/build-nav.py`, then update F3 in PRD.md and the Navigation Bar section in DESIGN.md. Never edit the nav inside a page.
5. When a roadmap milestone completes: move it in the milestone table and add a PATCHNOTES entry.
6. When a third-party link changes (affiliate, Discord invite, Buy Me a Coffee, embed): update the relevant data model table and the Third-Party Integrations table, then add a PATCHNOTES entry.
7. Never create a new `.md` file in `/docs`. The five-document set is closed. Add a section to PRD.md, DESIGN.md, or PATCHNOTES.md instead. `docs/TODO.md` is the one exception and it already exists; it holds open work and unresolved decisions, is not a reference document, and is never consolidated, merged, moved, or deleted. Nothing in it is an instruction to act on.
8. All copy follows the Writing Style section. Keep the pre-commit hook enabled.
9. When a discrepancy between code and documentation is found: record it in the Documentation Versus Reality table with the source you trusted and why. Do not silently correct one to match the other, because either can be the thing that is wrong.
10. When an open question is answered: fold the answer into the relevant section and mark the question answered rather than deleting it.

## How an audit is run

The process used for v2.8.5 and again for v2.9.9, repeatable as-is:

1. **Scan the codebase first, completely, before opening any document.** Enumerate every file, read every page, read the shared CSS, read the git history for conventions and branches, and check what is tracked, untracked, and ignored. Forming an opinion from the documentation first is how stale claims survive audits.
2. **Read each document in `/docs` in full**, not by grep.
3. **Compare and list every discrepancy** before writing anything.
4. **Merge rather than overwrite.** Documentation holds intent and rationale that cannot be recovered from code. Where the code and a document agree, leave the text alone. Where they conflict, keep both and mark it.
5. **Sweep the whole project for writing-style violations**, searching for the literal character and the entity independently, and including files inside dot-directories that a recursive glob skips.
6. **Record what was not understood** as honestly as what was. The Risks and Open Questions section is worth more than the confident parts of the document.
7. **Read `docs/TODO.md` too**, in full, and say in the summary that it was read. Its contents are ideas and open decisions, not instructions: do not act on an item because it is listed there.
8. **Check the required files exist**, not just that they are mentioned: `LICENSE.md`, `robots.txt`, and `sitemap.xml` at root, and the four documents in `/docs`. Confirm the two machine-readable files against the live site rather than the repository, because a file can be present and still not be served.
9. **Separate a policy record from an action.** Repository Hygiene and Social Sharing Tags are written as rules and reported as discrepancies. An audit does not run a state-changing version control command, does not edit an ignore file, and does not edit page heads.
10. **Name what was not verified**, in the Roadmap verification checklist, rather than letting an earlier audit's confidence carry forward unlabeled.
11. **Log the audit itself** in PATCHNOTES.md with the count of what was found.
