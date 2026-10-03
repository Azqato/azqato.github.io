# Product Requirements Document: Azqato Portfolio

This is the single source of truth for the Azqato site: what it is, who it serves, how it is built, how to run and deploy it, what conventions it follows, and what is known to be wrong with it. It is written so that a new contributor or an AI model can understand the entire project from `/docs` alone, without reading the code. Part 2, near the end, covers Azqato Invests, the 21-page investing site in `invests/` (Merged 2026-10-02).

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

What they need: the Invests page and the finance projects it links out to. (Since v2.11.0: Azqato Invests at azqato.com/invests/; its own users are in Part 2.)

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
- **F12: Curated Investing Hub.** `invests.html` carries 16 categories of hand-picked external resources (Platforms, Careers, ETFs, Companies, Ratings, Screeners, Real Estate, Charts, Databases, Economic Indicators, Education, Guides, Indices, Information, News) above a visible "not a licensed financial advisor" disclaimer. **Changed in v2.11.0:** `invests.html` is a redirect page; the hub is the Resources section of Azqato Invests (Part 2).
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
│                               generator and checks; its docs are Part 2 of this file
│                               (merged 2026-10-02; the main rules win, D22); built by invests/scripts/site.py
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
| Unoptimized thumbnails | Four `yt-thumb-*.jpg` totalling 2.3 MB on a 7.8 KB page, with no `loading="lazy"` | Resize to display dimensions, convert to WebP with a JPEG fallback, add `loading="lazy"` **Fixed in 2.12.6:** 160 px WebP copies, 30 KB in all, lazy-loaded; originals kept. |
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
| `/img/yt-thumb-azqato.jpg`, `-streams`, `-mixes`, `-chills` | Asset | Referenced by `youtube.html` until 2.12.6; kept |
| `/img/yt-thumb-*-160.webp` (four) | Asset | Referenced by `youtube.html` since 2.12.6 |
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

Applies to: every decision on the Support page (disclosure placement, button copy, card descriptions), and to the financial disclaimer on `invests.html` (since v2.11.0, the disclaimers across Azqato Invests).

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
| External resource links | Spot-check the `invests.html` hub; it has the most links and the highest rot rate (since v2.11.0 Azqato Invests' Resources page, invests/resources/) | Quarterly |
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
| Link validity | Monthly for affiliates and Discord invites, quarterly for the `invests.html` hub (now invests/resources/) | Manual clicking |
| Lighthouse | Quarterly, or after any major change | Run manually |
| Page weight | Every push | Flag anything over 45 KB before it crosses 50 |

---

# Roadmap

## Roadmap at a glance

Organized 2026-10-02 at the owner's request: every open item from both halves of the site in one place, in a suggested order. Each item's detail stays where it was written: Part 1 below, or Part 2, Invests: Roadmap (P numbers). Nothing here is scheduled until the owner says so.

**Now (waiting on the owner).** Changed 2026-10-02 by the owner: items 1 and 2 happen as one full review after item 15, and item 3 is done.

| # | Item | Where it's detailed | Status |
|---|---|---|---|
| 1 | Review the live Azqato Invests site and list changes | Part 2, P7.9 (in P13.2) | Moved: full review after item 15 |
| 2 | Review Invests' drafted sections: tenets, personas, user stories, goals, success criteria, metrics, press release, FAQ | Part 2, P7.10 (in P13.2) | Moved: full review after item 15 (a summary was shown to the owner 2026-10-02); D22 already settles Tenet 3 |
| 3 | Paste two or three live URLs into Discord and check the cards | docs/TODO.md | **Done 2026-10-02:** the owner checked them; the cards look right |

**Next: one site, one look (owner's requests, 2026-10-02).** These touch every page, so they're best done together, in this order.

| # | Item | Where it's detailed | Size |
|---|---|---|---|
| 4 | Pick the colors to keep for both halves (asks the owner first) | Part 2, P15; DESIGN.md, One palette for the whole site | **Done 2026-10-02** |
| 5 | The Invests top bar and theme button across the whole site, with a light palette for the 12 root pages | Future updates, below | Medium |
| 6 | The Invests footer across the whole site | Future updates, below | Small |
| 7 | Clean addresses for every page (`/discord`, not `discord.html`) | Future updates, below | Medium |
| 8 | Fold the Invests pages, generator and inventories into the main structure (docs part done in 2.12.0) | Part 2, P14 | Large; design needed |

**Next: Azqato Invests content and the old sites**

| # | Item | Where it's detailed | Size |
|---|---|---|---|
| 9 | Redirect the 19 old stocks, vix and leverage pages to their new addresses (changes those repos; ask first) | Part 2, P13.1 and Deprecation and Removal (D7) | Medium |
| 10 | The old repos become data feeds only; a second VIX data source | Part 2, P12 | Medium |
| 11 | Correct out-of-date content, including the two dead Resources links and the Holy Grail metrics | Part 2, P11 and P13.3 | Medium; each change needs the owner's approval |
| 12 | Combine the three VIX pages into one | Part 2, P16 | Medium |
| 13 | SEO and landing-page review of all 21 pages | Part 2, P17 | Large |

**Next: the main site**

| # | Item | Where it's detailed | Size |
|---|---|---|---|
| 14 | v2.9.5: no pulsing unless the fire is firing | v2.9.5, below | Small |
| 15 | Defect list: optimize the four `youtube.html` thumbnails; `build-nav.py --check` in the pre-commit hook; pause the render loop on `document.hidden`; Playwright smoke tests; mobile audit of `music.html` | Current phase, below | Small to medium each |

**Later**

| # | Item | Where it's detailed |
|---|---|---|
| 16 | v2.9.0: full native catalog (moved to Later by the owner, 2026-10-02; waiting on the owner's audio files) | v2.9.0, below |
| 17 | v3.0.0: contact / hire-me section, pointing to https://github.com/Azqato/azqato.github.io/issues (owner, 2026-10-02) | Below |
| 18 | ~~GitHub API integration (low priority)~~ Dropped for now (owner, 2026-10-02) | Below |
| 19 | ~~A progress dashboard~~ Dropped for now (owner, 2026-10-02) | Future updates, below |
| 20 | Extract `music.html`'s script to `viz.js` | Not scheduled, below |
| 15d | Smoke-test script, `tools/smoke.py`, run locally (moved from the build pass by the owner, 2026-10-02) | The next build pass, below |
| 21 | A brand per section and an emoji per page (favicon and title icon), the lion for the home page and any page without its own (owner's decision, 2026-10-02) | This list; to be written up as a Future update |

**Owner's answers for the next build pass (2026-10-02).** Recorded before building so the pass needs no further questions:

- **Theme (item 5):** phones keep the ☰ dropdown with the ☀️/🌙 button beside it; a first visit follows the system theme; the light colors are DESIGN.md's One palette for the whole site. The music visualizer stays dark in both themes; the page around it follows the theme. Discord hover color: `#4752c4` everywhere.
- **Emoji and brands (item 21):** Home 🦁, About 🙋, Discord 💬, Invests 💰, Codes 💻, Music 🎧, Links 🔗, Projects 🛠️, YouTube 📺, Support ☕, Gaming Accounts 🎮, Privacy 🔒; Invests sections: Individual Stocks 📈, Indices & ETFs 📊, VIX Strategy ⚡, Leveraged Strategies 🚀, Resources 📚. Any page without its own uses the lion. Section brands in the top bar: Azqato Invests, Azqato Music and Azqato Codes; every other page shows "Azqato."
- **Footer (item 6):** "© 2026 Azqato" plus links to every major section, following SEO practice (plain crawlable links, descriptive text). No sitemap link: search engines find sitemap.xml through robots.txt.
- **Clean addresses (item 7):** folders (`discord/index.html`, with `discord.html` as a redirect page). Opening pages straight from disk must keep working, so internal links point at `folder/index.html` the way Invests' do.
- **Invests (item 8):** scripts and inventories move to `tools/invests/`; Invests keeps its own layout but takes the shared palette and top bar, recolored in the same pass as item 5.
- **Old sites (items 9, 10):** the owner allows changes to the stocks, vix and leverage repos; `/leveraged-strategies/` also redirects; the vix job also writes `vix.json` as a second source and the blocked allorigins fallback goes.
- **Corrections (item 11):** remove the two dead Resources links; the Holy Grail figures load live from Composer Atlas on every page load, with a cached default when it can't be reached; all corrections go to the owner as one list.
- **One VIX page (item 12):** `/invests/vix/` with the strategy, then the live dashboard, then the custom builder, with jump links; the old dashboard and custom addresses redirect.
- **Landing pages (item 13):** each group's first page becomes a short landing page (what the section is, 3 to 5 cards, a "start here" button); its long text moves to a "Method" page in the group; reviewed all together.
- **Main site (items 14, 15, 20):** thumbnails get compressed copies and the originals stay; smoke tests are a local script; `music.html`'s script moves to `viz.js` in this pass.
- **Later or dropped:** the full music catalog is Later (item 16). The contact section (item 17) points to https://github.com/Azqato/azqato.github.io/issues. GitHub stats (18) and the progress dashboard (19) are dropped for now.
- **Pushing:** after each item is done and checked.

### The next build pass, sorted by effort (planned 2026-10-02)

Every item from Roadmap at a glance except Later, smallest first, each broken into its subtasks. Written before building, at the owner's request. The owner's answers it relies on are listed above.

**Status:** approved by the owner 2026-10-02 as recommended; in progress. Earlier: waiting on the owner's answer to one question: what this pass covers. Recommended: every row below in this order, with item 13 stopping at drafts for the owner's review, and item 7 moved up to run straight after item 5, because both rewrite every page's links. Each item is pushed when it's done and checked.

| # | Item | Subtasks | Effort |
|---|---|---|---|
| 15b | Block commits with an out-of-date nav | Add `python tools/build-nav.py --check` to `.githooks/pre-commit`; test it with a deliberately stale page | **Done 2026-10-02:** tested with a deliberately stale page (XS) |
| 15c | Pause the visualizer in hidden tabs | Pause and resume the render loop on `visibilitychange`, reusing `setPlaying()`; check it in Edge | **Done 2026-10-02:** visibilitychange pauses and resumes; a Pause stays paused (XS) |
| 14 | No pulsing unless the fire is firing (v2.9.5) | Gate the four `envLow` and `envBroad` brightness terms on the fire through a 150 to 250 ms eased gate, not a hard switch; confirm a paused or silent track holds steady brightness; re-measure the worst single-frame brightness step (limit 0.0073 at 60 Hz) | S |
| 15a | Compressed YouTube thumbnails | Make compressed copies of the four images, keeping the originals in `img/`; point `youtube.html` at the copies with `loading="lazy"`; record the bytes saved | **Done 2026-10-02:** four 160 px WebP copies, 2.37 MB to 30 KB, lazy-loaded; originals kept (S) |
| 6 | New footer on every page | "© 2026 Azqato" plus plain links to every main section (SEO practice: crawlable links, descriptive text; no sitemap link, since robots.txt lists sitemap.xml); stamp it from `tools/build-nav.py` into all 12 pages; match the Invests footer's style; update DESIGN.md | S |
| 21 | Emoji and section brands | An emoji favicon and title icon for each of the 12 pages and the Invests sections (list above); "Azqato Invests / Music / Codes" in the top bar on those pages; update the sharing tags if titles change | **Done 2026-10-02:** 2.13.1. Emoji favicons on every page and Invests section; Music and Codes brands in the top bar; titles unchanged (S) |
| 15d | Smoke-test script | `tools/smoke.py` (local, no GitHub Action): all 12 pages in Edge, both themes, desktop and phone widths; fails on console errors, broken links or sideways scroll; documented in the Runbook | **Moved to Later by the owner, 2026-10-02** (S to M) |
| 15e | Music page on phones | Test `music.html` from 320 to 480 px; fix layout, tap targets and the stage console; record the results | **Done 2026-10-02:** 2.13.2. Tested 320 to 480 px; console spans the screen, badge hidden, footer three lines, 24 px seek bar on touch (DESIGN, Music page on phones) |
| 11 | Content corrections | Remove the two dead Resources links; load the Holy Grail figures live from Composer Atlas on every page load with a cached default (first check that Atlas offers the figures in a form the page can fetch; if it doesn't, ask the owner); gather every other correction into one list for the owner | **Done 2026-10-02:** 2.13.3. Dead links removed; Holy Grail figures live from Composer Atlas with a cached default; corrections list C1 to C8 in Part 2, P11, for the owner (M) |
| 10 | Old repos become data feeds | The vix job also writes `vix.json`; the VIX pages read it as the second source; drop the blocked allorigins fallback; a clear "unavailable" state; confirm the stocks and vix jobs still run | **Done 2026-10-02:** 2.13.4 (vix v1.3.0). vix.json written by the job, read from raw GitHub as the second source; allorigins dropped; 8 s timeout; error state when all fail (Part 2, P12) (M) |
| 9 | Redirect the old sites | 19 redirect pages across the stocks, vix and leverage repos (old title, canonical, instant redirect, a fallback link); `/leveraged-strategies/` too; every data file keeps serving; after the push, check each old address reaches its page in one hop | M |
| 12 | One VIX page | Merge the three pages into `/invests/vix/` (strategy, then dashboard, then builder, with jump links), keeping everything (core rule); the old addresses become redirects; update the sidebar, search, sitemap and inventories; run `check.py` and `browser.py` | M |
| 5 | Top bar and theme button on every page | The light palette and new tokens in `styles.css`; swap literal colors for tokens on the pages that have them (`music.html` 137, `projects.html` 34, `support.html` 23, a few elsewhere); the nav template in `tools/build-nav.py` becomes the slim bar with ☀️/🌙 beside ☰ on phones; one shared theme script (system theme first, choice remembered); the visualizer stays dark; check all 12 pages in both themes | M to L |
| 7 | Clean addresses | Move 11 pages into folders, each `.html` left as a redirect page; fix relative paths one level deeper; nav links point at `folder/index.html` so opening from disk works (on azqato.com each click then takes one redirect to the clean address, as `.html` links do today; on azqato.github.io the address bar shows `/folder/index.html`, and canonical tags keep search engines on the clean form); update canonicals, sitemap.xml and og:url; check every old address and opening from disk | M to L |
| 20 | `music.html`'s script to `viz.js` | Move about 1,900 lines unchanged; test the visualizer, the audio reaction and every mode in Edge; confirm the page weight drops | L |
| 8 | Fold Invests in | Move its scripts and inventories to `tools/invests/` and fix their paths; Invests takes the shared palette and top bar; rerun `site.py`, `check.py` and `browser.py`; the pages and addresses stay | L |
| 13 | Landing pages and SEO (drafts only) | Audit all 21 pages (titles, descriptions, headings, internal links); draft four landing pages and four "Method" pages; the owner reviews them together | L |
| Review | Full review | The owner reviews the live site and Invests' drafted sections, after item 15 | Owner |

**Owner decisions that aren't work:** one brand or two; where the mascot came from; whether to start reading the Cloudflare analytics (docs/TODO.md). **Answered 2026-10-02 by the owner:** (1) brand: several brands, one per section, with a different emoji for each page; the home page and any page without its own use the lion. (2) The mascot is a lion because the owner likes cats. (3) Cloudflare analytics: much later.

**Declined or deferred:** Part 1's Explicitly deferred items and Part 2's Invests: Explicitly deferred.

**Recently done:** Azqato Invests launched (2.11.0, 2026-10-02), regrouped by topic (2.11.3) and its docs merged into these (2.12.0). The empty github.com/Azqato/invests repository is gone (P13.4).

## Current phase

**Azqato Invests (2026-10-02):** live at azqato.com/invests/; its docs merged into these (2.12.0). Its next steps are in Part 2, Invests: Roadmap, Current phase.

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

**Complete 2026-10-02.** `fireGate` eases toward 1 while the fire is lit and back to 0 after (250 ms time constant) and multiplies every term in the table below. Measured in headless Edge at about 78 fps as the mean luminance of the canvas: idle spread 0.0086 before, 0.0038 after; worst frame-to-frame step while playing 0.0042, under the 0.0073 recorded in v2.9.4 (a different method, so compare loosely).

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
| Dark / light mode toggle | The site is intentionally dark-only; no toggle will be added. **Reversed 2026-10-02 by the owner:** the Invests theme button comes to the whole site (Future updates) |
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
| `tools/build-nav.py` SKIP cleanup | Offered, deferred with "revisit this later". In `docs/TODO.md`. **Done as v2.10.1.** |
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

### The Invests top bar and theme button across the whole site (added 2026-10-02, owner's request)

**What.** Two changes, done together. (1) Give every azqato.com page the top navigation bar the Invests pages use: the slim full-width strip with the `Azqato.` logo and the same ten links, sitting at the very top above the page's own content. (2) Give the whole site the light and dark theme button Invests has (invests/assets/js/theme.js: follows the system setting until the visitor picks, remembers the choice in localStorage, sets `data-theme` on `<html>` before first paint), placed in that new top bar. The main site is dark-only today, so this also needs a light palette for styles.css; Invests' button then moves from its own top bar into the shared one. Today the main pages have their own sticky nav (F3); Invests draws a copy of it in its own style (invests/scripts/site.py `AZQATO_NAV`, styled by `.site-azqato` in invests/assets/css/site.css).

**Why.** The owner prefers how it sits above the main content. One look for the nav on both halves of the site also removes the visible jump between azqato.com and /invests/.

**How.** Port the `.site-azqato` styles (both themes) into styles.css and change the markup tools/build-nav.py stamps into the 12 pages, so the nav stays generated from one list. Keep the mobile dropdown working (the nav toggle script on every page); on phones Invests hides the strip and moves its links into its sidebar, which the main pages don't have, so the phone layout needs its own decision. Ideally the Invests copy then reads the same page list (build-nav.py or a shared file) so the two can't drift (invests PRD, Known technical debt).

**Size.** Medium: the nav is one stylesheet section, the build-nav.py template and a rerun; the theme button is a small script on every page (or one shared file) plus a full light palette for styles.css, which is the bulk of the work. Then a browser check of all 12 pages in both themes at desktop and phone widths.

**Open questions.** The light palette (pairs with the invests colors item, invests PRD P15, which asks the owner which colors to keep). The phone layout (keep the current dropdown, or something else; where the theme button sits on phones). Whether `Support` and the active-page highlight look the same as on Invests. Whether this lands before or as part of folding Invests into the site's structure (invests PRD, P14).

**Recommendation.** Do it; it's mostly CSS and one template. Settle the phone layout with the owner first.

### Clean addresses for every page (added 2026-10-02, owner's request)

**What.** Give the main site the same address style as Invests: `/discord`, `/invests`, `/links` instead of `discord.html`, `invests.html`, `links.html`. The `.html` files become redirect pages to their clean addresses, and every internal link, the nav, sitemap.xml, canonical links and og:url use the clean form.

**Why.** Shorter, tidier addresses that match /invests/, and one address per page.

**How.** Cloudflare Pages already serves `discord.html` at `/discord` (that's how canonical links work today), so most of the change is links and tags: build-nav.py's list, the Home and Links pages, sitemap.xml and every page head. A file can't be both the page and a redirect, so the content moves to `discord/index.html` (or the equivalent) and `discord.html` becomes the redirect page, under the removal policy (Compatibility entries). Check what GitHub Pages serves at azqato.github.io for the same addresses, and how links behave when a page is opened from disk (file://), which today works for every page.

**Size.** Medium: 12 pages, each with a redirect page and updated links, then a one-hop check of every old address after deploy.

**Open questions.** Folders (`discord/index.html`) or Cloudflare `_redirects` rules alone. Whether file:// support still matters (Local setup, Option A).

**Recommendation.** Do it, before or together with the shared top bar, since both touch every page's nav links.

### The Invests footer across the whole site (added 2026-10-02, owner's request)

**What.** Restyle the main site's footer to match the Invests footer: the slim bar with the brand, a short line of text and a row of links (invests/scripts/site.py, `footer()`, styled in invests/assets/css/site.css).

**Why.** The owner prefers how it looks on /invests, and it makes the two halves of the site read as one.

**How.** Port the footer styles into styles.css and change the footer markup on the 12 pages (ideally stamped by build-nav.py like the nav, so it can't drift). Decide which text and links the main footer carries; the Invests line about financial advice and referral links belongs to Invests only.

**Size.** Small.

**Open questions.** The footer's text and links for the main site.

**Recommendation.** Do it alongside the top bar and theme button entry, which already touches every page.

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
| 37 | Azqato Invests kept its own README, LICENSE and six documents in `invests/`, against the closed five-document set, and its D5 and Tenet 3 said it took no rules, docs or design from this site. | The owner, 2026-10-02: the main site's rules are the most up to date (Part 2, D22). | Fixed in 2.12.0: merged word for word into the five documents (Documentation Process). |
| 38 | Part 1 described `invests.html` as the investing hub (F12, the Investor persona, Tenet 4, Monitoring, Targets, the External FAQ), and DESIGN.md lists `invests.html` components. Since v2.11.0 it is a redirect page and the hub is Azqato Invests. | Code. | Each marked with the current state in 2.12.0, original text kept. Historical tables (the v2.10.4 title and description plans) are left as records. |
| 39 | DESIGN.md Rules for Staying Consistent, rule 6: "There is no light theme and none is planned." Azqato Invests ships a light and a dark theme, and the Roadmap plans its theme button for the whole site. | Both: the rule is true for the 12 root pages today. | Marked in DESIGN.md; resolved by the Future update that brings the theme button to the whole site. |
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
| Anything in `invests/` | Part 2 of this file, then DESIGN.md's Azqato Invests Visual System; Part 1 wins where they differ (D22) |
| Understanding why something is the way it is | This file, Product Tenets, then `PATCHNOTES.md` |

## Never do these

- **Never delete anything from `img/`.** Not an unreferenced file, not an apparent duplicate, not an obvious leftover, no matter how confident an audit is that nothing links it. That folder is the owner's working library and unused is its normal state. Remove a file from it only when the owner asks for that file by name.
- **Never add a dependency, a CDN script, or a web font** without a decision recorded here first. Tenets 1 and 2 exist to make this a conversation rather than a habit.
- **Never rename or delete a live `.html` file, `styles.css`, or a referenced image without a compatibility entry.** Inbound links live in Discord messages and video descriptions where they cannot be updated and their breakage cannot be observed.
- **Never hand-edit the nav or the footer in a page.** Both are generated (the footer since 2.13.0). The nav is generated. Edit `PAGES` in `tools/build-nav.py`, run the script, and commit the result. A hand edit survives until the next run and then vanishes without warning.
- **Never bypass the pre-commit hook** with `--no-verify` except when the text genuinely requires the character it is blocking (a rule quoting itself). The hook exists because a previous audit found violations that a manual search had missed.
- **Never claim the visualizer reacts to audio it cannot hear.** The claim is now true for the one same-origin track in `audio/`: `music.html` builds a real `AnalyserNode`, calls `createMediaElementSource` on the native player, and drives the lights from `getByteFrequencyData`. It is still false for the Mixcloud and YouTube embeds, whose audio is cross-origin and unreadable, and it is false on `file://`, where the page sets `canRouteAudio` false and shows a note saying so. Say "the track", never "the mixes". Tenet 6 applies to marketing copy first.
  > **Replaced in v2.9.9.** This entry previously read: "**Never claim in copy that the music visualizer reacts to the audio.** It does not, and Tenet 6 applies to marketing copy first." That was written before the native player shipped and had become the opposite of the truth, contradicting both the README and the External FAQ. A rule that forbids a true statement is worse than no rule.
- **Never commit `test-local-audio.bat` or anything under `music/`.** The batch file launches a browser with web security disabled, and the audio files are multi-gigabyte.
- **Never introduce `innerHTML` with a value from outside the file.** The one existing use is safe only because its data is hardcoded.
- **Use as few GitHub Actions as possible** (owner's rule, 2026-10-02). Tests and checks run as local scripts; GitHub Pages' own build is the only automation this repository relies on. A new Action needs the owner's say-so and a recorded reason.
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
No. Azqato is not a licensed financial advisor, accountant, or lawyer. Everything on the Invests page and in the finance projects is for informational and entertainment purposes. The disclaimer appears on the Invests page above the resources and again in the privacy policy. (Since v2.11.0: on every Azqato Invests page, in its sidebar and footer.)

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

# Part 2: Azqato Invests

Azqato Invests is the 21-page investing site in `invests/`, live at https://azqato.com/invests/ since 2026-10-02. Until 2026-10-02 it kept its own README, LICENSE and six documents in `invests/docs/`. They were merged here word for word (Merged 2026-10-02, main 2.12.0): its PRD is this Part, its DESIGN.md and UI-REVIEW.md are DESIGN.md's Azqato Invests Visual System, its PATCHNOTES.md is the Azqato Invests history at the end of PATCHNOTES.md, its LICENSE is folded into LICENSE.md, and its README, HOSTING.md and TODO.md are the last three sections of this Part. Headings gained an "Invests:" prefix so they don't collide with Part 1's.

**Which rules apply.** The main site's rules (Part 1, DESIGN.md and Documentation Process) are the most up to date and win wherever this Part differs (D22, the author's decision, 2026-10-02). This Part's own rules still apply where Part 1 has nothing to say, such as the core rule and the inventory checks. Where this Part says README.md, LICENSE.md, DESIGN.md, PATCHNOTES.md, UI-REVIEW.md, HOSTING.md or TODO.md, it means the invests files named above, now at their new places.

**Versions.** Invests had its own line, v0.1.0 to v1.1.1. From 2.12.0 the site's version numbers are combined: Invests changes are main 2.x entries in PATCHNOTES.md (the author's decision, 2026-10-02).

## Invests: Overview

This is the product requirements document for Azqato Invests: one site (since 2026-10-02 the `invests/` folder of the azqato.github.io repository, D21; first planned for its own repo) that merges the stocks, vix and leverage sites with the current invests.html page, built on the documentation-site template. It's the main reference for anyone working on the project, person or AI model. It holds the whole plan, the technical setup, the standing rules and how work is done here, so the project can be understood without reading any code.

- **Stage:** live since 2026-10-02 at https://azqato.com/invests/, as the `invests/` folder of the azqato.github.io repository, which is this project's single source of truth (Repository Hygiene). See Roadmap, Current phase, for what's next. Earlier text: planning is done apart from a few open points (see Risks and Open Questions). No site files exist yet. Where this document describes the site, it describes the plan, not code; the verification checklist in the Roadmap shows which sections have been checked, and against what.
- **Last documentation audit:** 2026-10-02 (see Documentation audits). The next audit starts from this date.
- **Other documents:** [README.md](#invests-readme-at-the-time-of-the-merge) is the short public front door. [DESIGN.md](DESIGN.md#azqato-invests-visual-system) covers how the site looks. [PATCHNOTES.md](PATCHNOTES.md#azqato-invests-history-v010-to-v111-before-the-docs-merge) logs every change. [TODO.md](#invests-todomd-at-the-time-of-the-merge-superseded) is the author's ideas list. [LICENSE.md](../LICENSE.md) sets the terms of use. [UI-REVIEW.md](DESIGN.md#invests-ui-review-record-2026-10-02) records the 2026-10-02 UI review and [HOSTING.md](#invests-hosting-options-record-2026-10-02) the hosting options (both records).
- **Where the plan came from:** until 2026-10-01 the whole plan lived in README.md. The documentation audit on that date moved it here and into DESIGN.md word for word. Text marked "Added by the 2026-10-01 audit" is new.

## Invests: Core rule: preserve everything

> Ingest everything and present it differently while preserving everything.

It's the same approach the stocks, vix and leverage sites were built on. It covers all four sources (stocks, vix, leverage and invests.html), applies to every part of the build, and overrides anything else in this plan.

- **Kept:** every page, section, paragraph, table, chart, tool, setting, data feed, link (referral links included), disclaimer and risk warning.
- **Changed:** only the presentation: the template, layout, navigation, theme and page addresses (old addresses redirect to the new ones).
- **Allowed:** correcting a link that points to an old address, such as the old Composer Atlas link. The link stays; only its destination changes.
- **Never without your sign-off:** cutting, trimming or summarizing away any content.

How it's checked:

1. Before a page moves, everything on it gets listed.
2. After it moves, every item on that list is checked against the new page.
3. A page isn't done until every item is accounted for.

The author's words when setting the rule (2026-10-01): "ingest everything and present it differently while preserving everything, just like the other websites we are consolidating into this. everythign should follow this rule and core ideology please make sure to document it in readme.md this is very important". As asked, README.md carries a short version of the rule; this section is the full one. Decision D3 applies it to everything.

## Invests: Problem statement

Azqato's investing material is split across four places, each a separate site with its own pages, styles and navigation:

- the stocks site: 9 pages of guides, a screener, Market Overview and an FAQ;
- the vix site: 3 pages, the VIX strategy, its dashboard and a custom builder;
- the leverage site: 7 pages, a landing page and six leveraged strategies;
- invests.html on azqato.com: one page of project cards and 15 categories of curated links.

**Changed 2026-10-02 (owner's review):** solved at launch; this records why the site exists. A visitor has to know which site holds what, and the sites link to one another rather than sharing one menu or one search. Some links point to an old GitHub Pages copy of Composer Atlas instead of the live site (see Composer Atlas).

Azqato Invests merges all four into one site with one navigation, one search and one design, while keeping every page, tool, link, disclaimer and risk warning (core rule). It's for people learning about investing or managing their own investments, for Azqato's Discord community, and for Azqato as the site's one maintainer.

## Invests: Target users

Personas drafted by the 2026-10-01 audit from the plan; the descriptions are illustrative.

1. **The learner.** New to investing, or to picking individual stocks. Reads the Learn pages (philosophy, stock metrics, index and ETF methodology; since v1.1.0 the Individual Stocks and Indices & ETFs sections), the setup guides and the FAQ. Needs plain explanations, numbered steps and risk warnings that are hard to miss. The template ratings describe the reading pages as being for "beginner-to-intermediate investors".
2. **The stock picker.** Manages their own portfolio and screens for ideas. Uses the Screener, Market Overview and the Metrics page. Needs a full-width, dense table, quick filters and current data.
3. **The strategy follower.** Runs, or is weighing, a rules-based strategy: the VIX strategy or one of the leveraged ones (3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail, HFEA). Checks the VIX Dashboard, reads the rules and risks, and compares with Composer Atlas. Needs today's reading, the exact rules and a direct link to the Atlas page.
4. **The Discord member.** Arrives from a link shared in Azqato's Discord. Needs to land on the right page and find related pages through the sidebar and search. Visitors arriving from elsewhere use the "Join the Discord" button to join.
5. **The maintainer (Azqato).** Keeps the site and the data pipelines running alone. Needs plain files with no build step, the pipelines left where they are (D6), and one place to change shared things.

## Invests: Goals

1. Everything from the four sources is on the new site: every inventory item accounted for on every page (core rule, D3).
2. One navigation, one search and one design across all 21 pages (D8, D12).
3. The tools keep working from the existing data feeds, with no pipeline moved (D6).
4. Light and dark themes, switched with one button (D10).
5. Composer strategies link to their Composer Atlas pages (D15, D16, D17).
6. Every old stocks, vix and leverage address keeps working by redirecting to its new page, once publishing is approved (D7, D20).
7. One look with azqato.com: shared colors, top bar, theme button and footer (added 2026-10-02 by the owner; Roadmap at a glance, items 4 to 8).

**Changed 2026-10-02 (owner's review):** goals 1 to 5 were met at launch (2026-10-02); goal 6 is open (Roadmap at a glance, item 9); goal 7 is new.

## Invests: Non-goals

- No accounts, sign-in or saved user data (Assumptions).
- No tracking or analytics scripts (Assumptions). (The site's own code adds none. azqato.com is served through Cloudflare, which injects its Web Analytics beacon, as the main site discloses; reading it is for much later, by the owner's decision.)
- No financial advice or personal recommendations. The site explains and shows data; invests.html already says "Nothing here is financial advice."
- No moving, copying or rebuilding the data pipelines; they stay in the stocks and vix repos (D6).
- No Net Worth Tracker pages, and none from the author's private project. Net Worth Tracker keeps only its home page card (D2).
- No sidebar entries for Composer Atlas, Net Worth Tracker or Automate Fundamentals (D18).
- No Composer Atlas links for concepts, only for Composer strategies (D17).
- No correcting out-of-date content during the move; a later roadmap item does that (D19).
- No cutting, trimming or summarizing content without the author's sign-off (core rule).
- No build step and no Node.js (Assumptions).
- No features that need a server, such as the template's page-feedback form, comments or a mailing list (Design details in DESIGN.md; template ratings).
- ~~No rules, docs or design taken from azqato.github.io (D5).~~ **Changed 2026-10-02 (owner's review):** removed; the main site's rules win (D22). **Audit 2026-10-02:** D5 was superseded by D21, and the author has since asked for azqato.com's colors (P15) and for the two sites' docs to merge; this stands only until those changes are made.
- ~~Nothing pushed, published or deployed until the author says so (D20).~~ **Changed 2026-10-02 (owner's review):** removed; the site is live and each push waits for the owner's word. (Launch go-ahead given 2026-10-02; each push still waits for the author's word.)

## Invests: User stories

- As a learner, I want the stock metrics, methodology pages and FAQ in one place so that I can learn the basics without working out which site holds what.
- As a learner, I want the Finviz and Seeking Alpha setup guides as numbered steps so that I can follow them while setting up my own account.
- As a stock picker, I want the screener's table to use the full page width so that I can compare many columns at once.
- As a stock picker, I want the Market Overview to show the latest scheduled data so that I can see where the market stands today.
- As a strategy follower, I want today's VIX reading and what it means for the strategy so that I can follow the rules without doing the arithmetic myself.
- As a strategy follower, I want each Composer strategy write-up to link to its Composer Atlas page so that I can check its backtested numbers.
- As any visitor, I want to search every page from the top bar so that I can find a topic without knowing which section holds it.
- As any visitor, I want a button that switches between light and dark and remembers my choice so that the site is comfortable to read.
- As a visitor with an old bookmark, I want old stocks, vix and leverage addresses to land on the matching new page so that my links still work. (Open: Roadmap at a glance, item 9; every other story was met at launch.)
- As a visitor, I want referral links disclosed so that I know when a link can earn Azqato a reward.
- As a Discord member, I want the home page's "Join the Discord" button so that I can join the community.
- As the maintainer, I want every source page checked against an inventory after it moves so that I know nothing was lost.
- As the maintainer, I want the new pages to read the data the existing pipelines already publish so that I don't have to move or rebuild them.

## Invests: Feature list

### MVP (must ship)

Everything in the Site map, with the core rule's inventory check passed for each page. **Shipped 2026-10-02** apart from the redirects (moved to P13). Since v1.1.0 the groups named below are Individual Stocks, Indices & ETFs, VIX Strategy, Leveraged Strategies and Resources (D12, Site map); the list keeps the plan's names:

- **Shell, on every page:** the top bar with the 💰 Azqato Invests name, search across every page and the ☀️/🌙 theme button (D10, D11); the sidebar with Learn, Tools, Strategies, Resources and FAQ (D12); breadcrumbs and previous/next links; an "On this page" list on reading pages but not on tool pages. azqato.com's top nav above it all, if D9 stays.
- **Home** (wiki-portal layout): the intro and "Join the Discord" button from invests.html, tiles into each section, and all 7 project cards with their text (D14, D18).
- **Resources:** all 15 curated categories with every link, referral links included, and the affiliate disclosure (D13).
- **Learn:** the landing page plus Philosophy, Stock metrics, Index & ETF methodology, the Finviz setup guide and the Seeking Alpha setup guide, from stocks.
- **FAQ:** from stocks, searchable as you type (D8, borrowed from help-center).
- **Strategies:** VIX Strategy (from vix), and the leveraged strategies landing page with 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA (from leverage). TQQQ FTLT, Holy Grail and HFEA keep their full write-ups, with Composer Atlas links (D15, D16).
- **Tools:** Screener and Market Overview (from stocks), VIX Dashboard and VIX Custom builder (from vix), reading the existing data feeds (D6).
- **Themes:** light and dark, starting from the visitor's system theme, with the choice saved in their browser (D10, Assumptions).
- **Redirects:** every old page under azqato.github.io/stocks/, /vix/ and /leverage/ redirects to its new home (D7). This means publishing, so it waits for the author's go-ahead (D20).

### Future (post-launch)

- Correct out-of-date content across the site, for example the Holy Grail page's missing factsheet numbers, which Composer Atlas now has (D19).
- Link HFEA to its entry in Atlas's community database once the way to link it is settled (To settle).
- sitemap.xml and robots.txt, once the site has pages and an address (D4). (Done: sitemap.xml generated; the main repository's robots.txt lists it.)
- The post-launch items P13 to P17 under the Roadmap's Future updates.
- Retire the old repos (added 2026-10-02, at the author's request; much later, when the author decides to clean them out): the stocks and vix repos become redirects to this site plus data feeds only (P12).
- Ideas from docs/TODO.md, turned into Roadmap entries only with the author's say-so (Working Practice).

## Invests: Constraints

- **Static files only.** Plain HTML, CSS and JavaScript, with no build step, no Node.js, and Python only for scripts (Assumptions). There's no server, so nothing that needs one (forms that submit, accounts, comments) is possible.
- **No data feeds in this repo (author's rule, 2026-10-02; D21).** This repo only displays the site. It holds no data files, no scheduled jobs or GitHub Actions that fetch or generate data, and no scripts that pull market data into it. All data is read at page load from the feed repos (stocks and vix), which run on their own. The only automation allowed here is the GitHub Pages or Cloudflare Pages build that publishes the site. A new data need goes into a feed repo, never here.
- **The data stays where it is.** Stock data is read from raw.githubusercontent.com/Azqato/stocks/main/data/ and the VIX reading from azqato.github.io/vix/data/vix.js (D6). The VIX file can't come from raw GitHub, which serves it as plain text with `X-Content-Type-Options: nosniff`, so browsers won't run it (Background findings).
- **Hosting.** azqato.com serves only the azqato.github.io repo, as a Cloudflare Pages build, so this repo needs its own hosting or extra Cloudflare setup (Background findings). The address isn't decided (D4). **Audit 2026-10-02:** settled by D21: the site is a folder of that repository, served by its Cloudflare Pages build at https://azqato.com/invests/ and by GitHub Pages at azqato.github.io/invests/.
- **Local only.** Nothing is pushed, published or deployed until the author says so (D20). That includes the D7 redirects, which change the live source sites. (The site itself went live on the author's go-ahead, 2026-10-02.)
- **Content.** The core rule overrides everything: nothing from the sources is cut, trimmed or summarized without sign-off. The author's private project stays out of any public docs (D2, Assumptions).
- **Templates.** The design comes from Template Interface, the author's private template repo. Its documentation-site template keeps all its demo pages in one file switched by URL hash, so it has to be split into one file per page (Design details in DESIGN.md). Its shared tokens in theme.css are never redefined (DESIGN.md).
- **People and time.** One maintainer. The plan sets no deadline or budget.

## Invests: Assumptions

Correct any that are wrong.

- Same stack as your other sites: plain HTML, CSS and JavaScript, no build step, no Node.js, Python for data scripts.
- No accounts and no tracking. The theme choice is saved only in the visitor's own browser.
- The site starts in the visitor's system theme until they press ☀️/🌙.
- Dark mode uses azqato.com's colors so it matches the shared nav; light mode uses the template's. To re-check along with D9.
- When the documentation prompt reruns, this plan becomes the PRD, DESIGN and PATCHNOTES docs in this repo's own `docs/` folder. If the repo is ever made public, the docs leave out the author's private project. Done 2026-10-02 (P9.6): its name was removed from every doc.

Added by the 2026-10-01 audit:

- The home page uses the site's own light and dark themes; wiki-portal contributes its layout only, not its violet palette. This is read from D8's wording ("wiki-portal's directory layout") and is Question 9.
- Visitors use a current version of Edge, Chrome, Firefox or Safari. documentation-site's CSS uses the `:has()` selector (for smooth scrolling and for locking the page while the menu is open), which older browsers ignore.
- The source sites' browser caches move over with their tools: the Market Overview keeps a cached copy of its feed in localStorage, and the VIX pages keep the last reading under the key `vix_last_known` (read from the source code on 2026-10-01).

## Invests: Success criteria

1. **Nothing lost:** for each of the 20 source pages, 100% of the items on its inventory are found on the new site (the core rule's check, done page by page).
2. **Everything reachable:** all 21 pages are linked from the sidebar or the home page, and site search returns each page for its own title.
3. **Data current:** on a weekday, the VIX reading shown is the one the vix pipeline last committed, and the Screener and Market Overview show the stocks pipeline's latest data.
4. **No errors:** every page loads in headless Edge with 0 console errors and 0 broken internal links, in both themes.
5. **Readable:** every text and UI color pairing in both themes meets WCAG AA contrast: 4.5:1 for body text, 3:1 for large text.
6. **Fast:** in a mobile Lighthouse run, Home, the Screener and one strategy page reach an LCP of 2.5 s or less, a CLS of 0.1 or less and a TBT of 200 ms or less (targets set by the 2026-10-01 audit; see Metrics).
**Changed 2026-10-02 (owner's review):** criteria 1 to 6 were met at launch (scripts/check.py, scripts/browser.py and the P7 Lighthouse run, 2026-10-02); 7 is open until the redirects (Roadmap at a glance, item 9).

7. **Old links work:** once publishing is approved, each of the 19 old stocks, vix and leverage page addresses reaches its new page in one hop (D7).

## Invests: Tenets

Drafted by the 2026-10-01 audit from the core rule and the decisions, in priority order: when two conflict, the higher one wins. The author may reorder or reword them (Question 15).

1. **Preserve before polish.** Nothing from the four sources is cut, trimmed or summarized without the author's sign-off, even when it's repetitive, out of date (D19) or awkward to fit the template. When content and layout disagree, the layout changes. A cleaner page that lost a paragraph is a failed move.
2. **Push only on the owner's word.** **Changed 2026-10-02 (owner's review):** the site is live; work is finished and verified locally and pushed only when the owner says so. Earlier title and text: **Local until told otherwise.** Nothing is pushed, published or deployed until the author says so (D20), not even a fix for something broken on a live site. Work is finished and verified locally, then waits. A ready change that sits unpublished costs nothing that can't be recovered; a publish can't be taken back.
3. ~~**This repo sets its own rules.**~~ **Changed 2026-10-02 (owner's review):** removed; D22. (**Audit 2026-10-02:** D5 was superseded by D21, so this tenet no longer matches the decisions; it waits for the author's review, P7.10. **Superseded 2026-10-02 by D22:** the main site's rules win.) Azqato Invests is independent (D5). Where azqato.github.io's docs, rules or design say something different, this repo's docs win. azqato.github.io is a source of facts, such as where a feed lives, never of rules.
4. **Reuse the feeds, don't move the pipelines.** Pages read the data the stocks and vix repos already publish, even when that's awkward, like loading the VIX reading from another site (D6). A second copy of a pipeline is a second thing to keep running.
5. **Template structure, source content.** (**Changed 2026-10-02 (owner's review):** softened: the look moves toward azqato.com's colors, top bar and footer, P15 and Roadmap at a glance items 4 to 8; the content rule is unchanged.) Layout, navigation and styling come from the chosen Template Interface templates (D8); words, numbers, links and warnings come from the sources. Template demo content always comes out, and source content never does.
6. **No accounts, no tracking.** If a feature needs sign-in, a server or a way to follow visitors, it's out, even when it would make success easier to measure. Anything the site keeps stays in the visitor's own browser.

## Invests: Decisions

| # | Area | Decision |
|---|---|---|
| D1 | Scope | Merge [stocks](https://github.com/Azqato/stocks), [vix](https://github.com/Azqato/vix), [leverage](https://github.com/Azqato/leverage) and the current [invests.html](https://github.com/Azqato/azqato.github.io/blob/main/invests.html) into one site, Azqato Invests |
| D2 | Scope | Net Worth Tracker and the author's private project stay separate. Net Worth Tracker keeps its card on the home page; the private project stays private, as its own README requires. **Changed 2026-10-02 (P9.6):** the private project's name was taken out, because this repository will be public; the decision itself is unchanged, and the earlier wording isn't repeated here for the same reason |
| D3 | Scope | Everything follows the core rule above |
| D4 | Hosting | **Changed 2026-10-01.** The site's address isn't decided yet (see To settle); azqato.github.io links to it. **Decided 2026-10-01:** azqato.github.io/invests/, a GitHub Pages project site from a public repository named `invests` (Question 1). Before: the home address was azqato.github.io/invests.html, served as azqato.com/invests. **Changed 2026-10-02 (D21):** https://azqato.com/invests/, the `invests/` folder of the azqato.github.io repository |
| D5 | Hosting | **Changed 2026-10-01.** Azqato Invests is its own independent repo, and this folder becomes it. azqato.github.io only links here; its rules, docs and design don't apply to this site. Before: the code lived in the azqato.github.io repo, with invests.html as the home page and the other pages in an `invests/` folder. **Superseded 2026-10-02 by D21:** the site lives in the azqato.github.io repository after all, in its own `invests/` folder with its own docs |
| D6 | Hosting | The data pipelines stay in the stocks and vix repos. The new pages read the stock data from GitHub, as the screener already does, and the VIX reading from the vix site (see Background findings) |
| D7 | Hosting | Every old page under azqato.github.io/stocks/, /vix/ and /leverage/ redirects to its new home. The old repos stay for data and history |
| D8 | Design | `documentation-site` for every inner page and `wiki-portal`'s directory layout for the home page, borrowing `help-center`'s searchable FAQ and step-by-step guides, `admin-dashboard`'s summary tiles and table styling for the tools, and `blog-article`'s reading-progress bar. The design comes from these Template Interface templates, not from azqato.github.io |
| D9 | Design | Every page shows azqato.com's top nav (Home, About, Discord, Invests, Codes, Music, Links, Projects, YouTube, Support) above the site's own top bar and sidebar. **To re-check:** this was decided when the site was going to live in the azqato.github.io repo (see To settle). **Confirmed 2026-10-01:** keep it |
| D10 | Design | Light and dark themes, switched with a ☀️/🌙 button |
| D11 | Design | The site's icon is 💰 |
| D12 | Content | **Changed 2026-10-02 (v1.1.0, the author's request):** pages are grouped by what the visitor invests in: Individual Stocks, Indices & ETFs, VIX Strategy, Leveraged Strategies and Resources, each topic group opening on its landing page (see Site map). Before: Pages are grouped by topic: Learn, Tools, Strategies, Resources and FAQ (see Site map) |
| D13 | Content | All 15 curated resource categories come over with every link, referral links included, and the affiliate disclosure |
| D14 | Content | The home page keeps the "Join the Discord" button and all 7 project cards |
| D15 | Composer Atlas | When the site refers to a Composer.trade strategy, it links to [Composer Atlas](https://composeratlas.com) |
| D16 | Composer Atlas | TQQQ FTLT, Holy Grail and HFEA keep their full write-ups, each with a clear link to its match on Composer Atlas (listed under Composer Atlas below) |
| D17 | Composer Atlas | Only Composer strategies link to Atlas. Concepts are explained on this site, without Atlas links |
| D18 | Other projects | Composer Atlas, Net Worth Tracker and Automate Fundamentals appear as home page cards and in-page links, never in the sidebar |
| D19 | Content | Out-of-date content moves over as it is, and a roadmap item added later corrects all of it. For example, the Holy Grail page says no factsheet data was available, but Composer Atlas now has the numbers |
| D20 | Working practice | Once development starts, everything stays local until you say otherwise: nothing is pushed, published or deployed (decided 2026-10-01). The author gave the go-ahead to publish on 2026-10-02; every later push still needs the author's word |
| D21 | Hosting | **Changed again 2026-10-02 (Question 18, option D):** the site moves into the azqato.github.io repository, for now as one self-contained `invests/` folder (pages, assets, scripts, inventories and docs), served at https://azqato.com/invests/ by that repository's Cloudflare Pages build (and at azqato.github.io/invests/ by GitHub Pages). Separate repositories were only for the first build and testing. This local repository keeps its own history; the main repository gets the files as a new commit. Folding the files into the main site's own structure is a later step. The stocks and vix repositories still hold the data. Before: **Changed 2026-10-02:** the stocks repository stays the data source and is not the host. The site lives in its own new public repository named `invests` (D4, D5) with no data feeds in it; the stock data workflows and files stay in stocks (D6), and the site reads them from azqato.github.io/stocks/data/, which is the same origin as azqato.github.io/invests/. The stocks repository keeps GitHub Pages on for its data folder while its old pages become D7 redirects. Before: at publish time the author renames the [stocks](https://github.com/Azqato/stocks) repository to `invests`, and it becomes Azqato Invests: the new site replaces its pages, while its data workflows, data files and history stay. This serves the site at azqato.github.io/invests/ (D4) without a new repository, and the stock data becomes same-repo files (updates D6 for stock data; the VIX reading still comes from the vix site). GitHub Pages doesn't redirect after a rename, so a new, small `stocks` repository holds the D7 redirect pages for the old azqato.github.io/stocks/ addresses. Nothing is renamed until the author's go-ahead (D20) |
| D22 | Working practice | **Decided 2026-10-02 by the author:** the main site's rules, docs and design are the most up to date rules and win where they differ from this Part. Supersedes D5 and Tenet 3. This Part's docs merged into the main docs the same day (Documentation Process) |

## Invests: Site map

21 pages from the 20 source pages (invests.html splits into Home and Resources). **Restructured 2026-10-02 (author's request, v1.1.0):** grouped by what the visitor invests in, not by page type; each topic group's first page is its landing page, listed as "Overview" in the sidebar. The pages had been live about an hour, so the old addresses were dropped without redirects (author's decision). The earlier map (Learn, Tools, Strategies, Resources, FAQ) is in PATCHNOTES.md, v1.0.1 and before.

```
Home                                index.html, from invests.html
│
├── Individual Stocks               stocks/index.html, landing, from stocks/index.html
│   ├── Philosophy                  stocks/philosophy.html
│   ├── Stock metrics               stocks/metrics.html
│   └── Screener                    stocks/screener.html
│
├── Indices & ETFs                  indices/index.html, landing, from stocks/indices.html
│   └── Market Overview             indices/market.html, from stocks/market.html
│
├── VIX Strategy                    vix/index.html, landing, from vix/index.html
│   ├── VIX Dashboard               vix/dashboard.html, from vix/strategy.html
│   └── VIX Custom builder          vix/custom.html
│
├── Leveraged Strategies            leveraged/index.html, landing, from leverage/index.html
│   └── 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail, HFEA (leveraged/<name>.html)
│
└── Resources
    ├── Curated resources           resources/index.html, from invests.html
    ├── Finviz setup guide          resources/finviz.html, from stocks/finviz.html
    ├── Seeking Alpha setup guide   resources/seekingalpha.html, from stocks/seekingalpha.html
    └── FAQ                         resources/faq.html, from stocks/faq.html
```

**On every page:** the site's top bar with 💰 Azqato Invests, search across every page and the ☀️/🌙 button, under azqato.com's top nav (D9).

**Home** (wiki-portal layout): the intro and "Join the Discord" button from invests.html, tiles into each section, and all 7 project cards with their text. (Since v0.16.0: one grid of 10 cards, the 7 project cards plus Market Overview & VIX tools, Curated Resources and FAQ; DESIGN.md, Home page.) The four cards that pointed to the old sites (Stocks, Stock Screener, VIX Strategy, Leveraged Strategies) now link inside the site; Automate Fundamentals, Composer Atlas and Net Worth Tracker link out.

**Inner pages** (documentation-site layout): the sidebar with the five sections, and the page itself with breadcrumbs, an "On this page" list and previous/next links.

DESIGN.md describes each layout in detail.

## Invests: What's being merged

| Source | Live now | Pages | Data |
|---|---|---|---|
| stocks | [azqato.github.io/stocks](https://azqato.github.io/stocks/) | 9: home, Philosophy, Metrics, Index & ETF methodology, Screener, Market Overview, FAQ, Finviz guide, Seeking Alpha guide | 6 GitHub Actions workflows: stock and ETF data daily, Market Overview 3 times a weekday, statements and index constituents weekly. The sixth, alert-on-failure.yml, is the failure alert (added 2026-10-01, Question 13; its trigger is read in P1 refreshes) |
| vix | [azqato.github.io/vix](https://azqato.github.io/vix/) | 3: About, Dashboard, Custom | 1 workflow updates the VIX reading 8 times a weekday |
| leverage | [azqato.github.io/leverage](https://azqato.github.io/leverage/) | 7: home, 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail, HFEA | None |
| invests.html | [azqato.com/invests](https://azqato.com/invests) (since 2026-10-02 a redirect to this site) | 1: intro with a Discord button, 7 project cards, 15 categories of curated links (some are referral links) | None |

20 pages in total. All four are plain HTML, CSS and JavaScript with no build step.

Added by the 2026-10-01 audit, read from GitHub that day:

- The files on each repo's main branch match the table. stocks: faq, finviz, index, indices, market, metrics, philosophy, screener and seekingalpha (.html). vix: custom, index and strategy. leverage: 3sig, 6sig, 9sig, hfea, holy-grail, index and tqqq-ftlt.
- stocks has six workflow files: alert-on-failure.yml, constituents.yml, market-overview.yml, screener-data-etfs.yml, statements.yml and stock-data.yml. The table's description covers the five data jobs; the sixth is alert-on-failure.yml, whose trigger wasn't read (Documentation Versus Reality, entry 3). vix has one, update-vix.yml. leverage has none.
- The sources are still changing. On 2026-10-01 the newest entry in stocks' patch notes was v4.9.6 (2026-09-29), and the main branches of stocks and vix both had commits from that day. Take each page's inventory when it moves, not from this table.

## Invests: Composer Atlas

Strategy link format: `https://composeratlas.com/strategies?slug=<slug>` (checked and live).

| Strategy here | On Composer Atlas |
|---|---|
| TQQQ For The Long Term | `tqqq-long-term` (original) and `zoops-tqqq-long-term-2026`, plus `zoops-upro-ftlt-2026`, its S&P 500 counterpart. The page already links the original. |
| Holy Grail | `holy-grail` (original) and `zoops-holy-grail-2026`. The page says no factsheet data was available; Atlas has the backtested metrics. |
| HFEA | No curated page. The Composer version the page cites (symphony `Cjb5ysKtJsPv6Tm3Fk0R`) is in Atlas's community database. |

3 Sig, 6 Sig and 9 Sig aren't Composer strategies, so they get no Atlas link.

invests.html and the leverage pages link to azqato.github.io/composer, a GitHub Pages copy. Those links change to composeratlas.com, the live site.

## Invests: Background findings

- **azqato.com only serves the azqato.github.io repo (affects D4).** azqato.com/invests is byte-for-byte the repo's invests.html, but azqato.com/stocks/, /vix/ and /leverage/ return 404. That repo's own docs say azqato.com is a Cloudflare Pages build of it, separate from GitHub Pages. A site in its own repo won't appear on azqato.com unless Cloudflare is set up to serve it too. (Resolved by D21: the site is a folder of that repo.)
- **Moot since the D5 change: a page and a folder can share the name `invests`.** This was checked for the old D5. In the azqato.github.io repo, music.html sits next to a music/ folder, and both azqato.com/music and azqato.github.io/music serve the page.
- **The screener and Market Overview already load their data from GitHub (behind D6)** (raw.githubusercontent.com/Azqato/stocks/main/data/), with a local copy as fallback. Pages elsewhere can read the same feeds without moving any pipelines.
- **The VIX reading can't come from raw GitHub (affects D6).** The VIX pages load it as a script, `data/vix.js`. raw.githubusercontent.com serves files as plain text with `X-Content-Type-Options: nosniff`, so browsers refuse to run them as scripts. azqato.github.io/vix/data/vix.js serves the same file as JavaScript, and the vix site stays up anyway to hold the D7 redirects.
- **The data bots are busy (behind D6).** Stocks and vix schedule about 68 data runs a week (28 for stocks, 40 for vix). Each run that produces new data commits it to its repo, and each commit redeploys that repo's site.
- **The name is already in use.** The stocks sidebar reads "Azqato Invests / Individual Stocks" and links to azqato.com/invests; the vix nav links there too.

Added by the 2026-10-01 audit:

- **Template Interface's shared colors are azqato.com's dark colors (affects D9 and the dark theme).** Template Interface's theme.css defines a dark palette: canvas `#0d1117`, surface `#161b22`, border `#30363d`, text `#e6edf3` and `#8b949e`, accent `#00d4a0`, success `#3fb950`. These match azqato.com's dark colors except the accent's hover shade (`#22e6b5` in theme.css, `#00e6b0` on azqato.com). A dark theme built on the shared tokens and one built on azqato.com's colors therefore come out the same apart from that shade, whichever way D9 goes. documentation-site's own palette is light (a white page with emerald `#0b7a52`) and wiki-portal's is a dark violet. Details are in DESIGN.md.
- **The vix pages load Chart.js 4.4.0 from jsDelivr without an integrity hash** (strategy.html and custom.html). See Security.
- **The source sites keep only market data in the browser.** The Market Overview caches its feed in localStorage, and the VIX pages cache the last reading under `vix_last_known`. None of the scanned stocks and vix pages uses cookies.
- **The stocks fallback may not survive the move (affects D6).** The Screener and Market Overview fall back to a local copy of the data when raw GitHub fails. If that fallback is a relative path (not read in this audit), it finds nothing on this site, which has no data folder. To keep the feed's behavior (core rule), it would need a new target, such as the copy the stocks site serves under azqato.github.io/stocks/ (not checked). **Checked 2026-10-01 (P1):** the fallbacks are relative: screener.js and market.html list each feed as raw GitHub first, then `data/<file>`. https://azqato.github.io/stocks/data/ serves the same files as JSON with `Access-Control-Allow-Origin: *`, so it can replace the relative path (P6).

## Invests: Roadmap

### Current phase

**Next, in order** (the whole site's list is Roadmap at a glance, in Part 1): P7.9 (the author reviews the live site); then the post-launch list under Future updates (P13); later P11, P12 and P14 to P17.

Updates, newest first:

**Update 2026-10-02, docs merged (main 2.12.0):** README.md, LICENSE.md and every file in docs/ merged into the main repository's README, LICENSE and docs, word for word; this PRD is Part 2 of docs/PRD.md. The author decided the main site's rules win (D22) and that the site's version numbers combine: from now on Invests changes are main 2.x entries in docs/PATCHNOTES.md. Next, in order, unchanged above.

**Update 2026-10-02, documentation audit (v1.1.1):** README.md, LICENSE.md and every file in docs/ checked against the live site and brought up to date; the findings are under Documentation Versus Reality (entries 13 to 17). The empty github.com/Azqato/invests repository is gone (P13.4). Next, at the author's request: merge these docs into the main repository's docs ("full re-read of everything and ingestion planning" first).

**Update 2026-10-02, restructured (v1.1.0):** the sidebar groups are now Individual Stocks, Indices & ETFs, VIX Strategy, Leveraged Strategies and Resources (Site map), at new addresses, without redirects (author's decision: live about an hour). The D7 redirect list under Deprecation and Removal points at the new addresses.

**Update 2026-10-02, live (azqato.github.io v2.11.0 to v2.11.1):** the author gave the go-ahead (D20) and the azqato.github.io repository was pushed. The site is live at https://azqato.com/invests/ and (GitHub Pages) azqato.github.io/invests/. What the merge added outside `invests/`: `invests.html` became a one-file redirect page to `invests/index.html`; a new `_redirects` sends `/invests` and `/invests.html` to `/invests/` with 301 on Cloudflare Pages (GitHub Pages ignores it); the nav (tools/build-nav.py), the Home explore card and the Links page button point at `invests/index.html`; sitemap.xml lists https://azqato.com/invests/ and robots.txt gained `Sitemap: https://azqato.com/invests/sitemap.xml`; the pre-commit hook skips `invests/inventory/`. Links use `index.html` explicitly so they also work from file://, where a folder link shows a directory listing. Post-deploy check (a comparison): the served page and asset files match the local copies byte for byte; /invests and /invests.html answer 301 to /invests/ in one hop; azqato.github.io/invests.html redirects; Home, the Screener and the VIX Dashboard load live data in both themes with no script errors. The separate local repository (`../invests`, last commit `9120a25`) is retired and will be deleted (Repository Hygiene). The working notes from the session that did this (an uncommitted HANDOVER.md) were moved into this document and deleted.

**Update 2026-10-02, hosting decided (v0.18.0):** Question 18 answered with option D: the site merges into the azqato.github.io repository as an `invests/` folder, at https://azqato.com/invests/ (D21). Canonical links, og:url and sitemap.xml now use azqato.com's clean addresses (no .html). This repository's history was rewritten to remove the private project's name (Question 16). The files are committed to the main repository locally; nothing is pushed.

**Update 2026-10-02, P7 to P9 done (v0.17.0):** the site-wide checks, the documentation pass and the publish plan, at the author's request ("do everything up to finishing P9"). Nothing was pushed or published (D20). What each step found is under its phase in the Development plan. In short:
- P7: the inventories pass against a fresh snapshot; all 21 pages are reachable from the sidebar and found by title in search; 0 broken internal links, and 2 of the 96 outside links are dead (source content, listed for P11); every page carries all the sharing tags; Lighthouse (mobile, in Edge) passes on Home, the Screener and 9 Sig after one fix to the Screener's layout shift; the keyboard walk, drawer and search focus, landmarks and skip link work; no em dashes or secrets; feed text is now cleaned before it is shown as HTML. Steps 9 and 10 (showing the author the site, and the author's review of the drafted sections) wait for the author.
- P8: every PRD and DESIGN.md section was checked against the site and the verification checklist is dated; Conventions, the Runbook and Folder structure are filled in from the code; TODO.md holds only its placeholder.
- P9: canonical links, og:url and sitemap.xml use https://azqato.github.io/invests/; the redirect list for the 19 old addresses is under Deprecation and Removal; Deploy and Rollback are written in the Runbook; the private project's name is out of the docs and LICENSE.md names the issue tracker. Waiting on the author: Question 16 (the repository's history and the template files before it goes public) and Question 17 (azqato.com/invests and azqato.github.io/invests.html).
- Next: P7.9 and P7.10 with the author, then P10 only on the author's go-ahead.

**Update 2026-10-02, UI review fixes built and tested (v0.16.0):** every decision in docs/UI-REVIEW.md is built (its "Done" section lists each change and where it lives). Page width: option C, everything full width, chosen from three previews, which were then removed. Tested once everything was built: `python scripts/check.py` 21 pages, 0 failures; `python scripts/browser.py` 0 failures (the same 9 notes as before: the stocks feed's 2026-09-30 data and the VIX fallback findings). A probe found no text under 12px on any page at 1600px or 390px. Behavior checks in headless Edge: both VIX tools show LIVE with the same tier wording; the Custom builder shows the result first; the sidebar opens only the current group; the source footers are hidden and the VIX disclaimer sits in the site footer; the VIX table cells carry their labels on phones; the azqato.com bar is hidden on phones and its links are in the menu. Every page was scrolled through again in light and dark at 1440px and in light at 390px.

**Update 2026-10-02, UI review:** every page was scrolled through in headless Edge (light and dark at 1440px, light at 390px). The findings and suggested fixes are in docs/UI-REVIEW.md and wait for the author's decisions; nothing was changed.

**Update 2026-10-02, P2 to P6 tested; paused for the author:** the deferred tests ran after P6.
- `python scripts/check.py`: 21 pages, 0 failures (titles, links, demo text, dashes, inventories).
- `python scripts/browser.py` (new; headless Edge): 0 failures. Every page loads with no script errors or failed requests in light and dark, at 1280px and 390px, with no sideways scroll, and passes WCAG AA text contrast at 1280px. The skip link, drawer, search (`/`, Ctrl+K, results for every section), theme button and its saved choice, FAQ filter and FAQ answer links work. The tools load live data, and the screener falls back to azqato.github.io/stocks/data/ with raw GitHub blocked.
- Fixed on the way: the leverage risk notices laid out as a row (the template's `.callout` is flex), which pushed TQQQ FTLT and Holy Grail sideways on phones; light-theme data colors below AA, including the VIX ticker colors, which were hard-coded in the scripts and didn't follow the theme (DESIGN.md, Data colors); a dark-theme red badge at 4.1:1, already in the source.
- Findings for the author, not changed (source behavior):
  - The stocks feed's newest data was from 2026-09-30 5:48 PM when tested on 2026-10-02, so the 2026-10-01 runs hadn't landed; that's the stocks repo's job.
  - With only vix.js blocked and no cached reading, the VIX Dashboard stays on "Fetching data…": its allorigins fallback is refused by the browser (CORS). With every feed blocked it shows its error state, and with a cached reading it shows that.
- Next: the author's review, then P7.

**Update 2026-10-02, P6 built:** the four tools: Screener, Market Overview, VIX Dashboard and VIX Custom builder. P2 to P6 are all built; the testing deferred from each phase runs next.

**Update 2026-10-02, P5 built:** Strategies: the VIX Strategy, the leveraged strategies landing and the six strategies, with Composer Atlas links.

**Update 2026-10-02, P4 built:** Learn (6 pages) and the FAQ.

**Update 2026-10-02, P3 built:** Home and Resources, split from invests.html. The source snapshots were refreshed first (P1.4); no source had changed since 2026-10-01.

**Update 2026-10-02, P2 built:** the shell is built: every page shares one top bar, sidebar, breadcrumbs, pager, footer and search, in light and dark, generated by scripts/site.py from the source snapshots. Testing waits until P6 is built, at the author's request (P2.12). The Python scripts moved from `tools/` to `scripts/`, because the Tools section's pages live in `tools/`.

**Update 2026-10-02:** D21 added: the stocks repository will be renamed to `invests` and host the site at publish time (P9). Nothing changes until then. **Changed the same day:** stocks stays the data source only; the site gets its own `invests` repository with no data feeds (D21).

**Update 2026-10-01:** building started. P0 (setup) and P1 (source snapshots and inventories) are done; P2, the shell, is next.

**Paused 2026-10-01 (usage limits), where work stopped:** every open question (1 to 15) is answered and recorded under Risks and Open Questions. P0 and P1 are complete and committed to the local git repository (`main`, no remote). scripts/check.py now fails on em dashes in page text (Question 14). Nothing is in progress and there are no uncommitted changes. To resume: start Development plan P2 (the shell), first refreshing the source snapshots with `python scripts/snapshot.py` and `python scripts/inventory.py` if the sources have changed. The drafted sections stay marked as drafted until the author's review after the MVP (P7.10).

**Planning, with the docs set up.** The plan is complete apart from the open points under Risks and Open Questions. The first documentation audit ran on 2026-10-01 and moved the plan into these docs. Building starts when the author gives the go-ahead, and everything stays local until the author says otherwise (D20).

### Next steps (from the plan)

1. You say when to resume.
2. The documentation prompt reruns for this independent repo, and this plan moves into its docs.
3. You give the go-ahead to start building. Everything stays local until you say otherwise (D20).
4. Proposed build order:
   1. The shell: template, the ☀️/🌙 button, the 💰 icon, sidebar and search, plus azqato.com's nav in both themes if D9 stays.
   2. Home and Resources, from invests.html.
   3. Learn and FAQ, from stocks.
   4. Strategies, from leverage and vix.
   5. Tools: screener, Market Overview, VIX Dashboard and Custom builder, reading the existing data feeds.
   6. Check every page against its inventory (core rule). Switching the old addresses to redirects means publishing, so it waits for your go-ahead (D20).

Steps 1 and 2 were completed on 2026-10-01: the author said to resume, and the documentation audit moved the plan into these docs. All four steps are done (2026-10-02); this list is kept as the record. What's next is under Current phase.

### Milestones

| # | Milestone | Target | Status |
|---|---|---|---|
| M1 | Plan: core rule, decisions D1-D20, site map, sources, template choice | 2026-10-01 | Complete |
| M2 | Documentation set (first audit) | 2026-10-01 | Complete |
| M3 | Go-ahead to build | When the author says | Complete 2026-10-01 |
| M4 | The shell | First, after M3 | Complete 2026-10-02 (P0 and P1 on 2026-10-01, P2 on 2026-10-02) |
| M5 | Home and Resources | After M4 | Complete 2026-10-02 (P3) |
| M6 | Learn and FAQ | After M5 | Complete 2026-10-02 (P4) |
| M7 | Strategies | After M6 | Complete 2026-10-02 (P5) |
| M8 | Tools | After M7 | Complete 2026-10-02 (P6) |
| M9 | Inventory check of every page | After M8 | In Progress: P7 checks and P8 done 2026-10-02; P7.9 (now a review of the live site) and P7.10 wait for the author |
| M10 | Publish, with the D7 redirects | When the author says (D20) | Published 2026-10-02 (P10 steps 1 to 3); the D7 redirects moved to P13 |
| M11 | Out-of-date content corrected (D19) | After launch | Planned |

### Feature breakdown per milestone

- **M1 Plan:** the core rule; decisions D1-D20; the 21-page site map; the Composer Atlas mapping; the inventory of the 20 source pages; background findings; the template ratings.
- **M2 Documentation set:** README.md as the front door; docs/PRD.md, DESIGN.md, PATCHNOTES.md and TODO.md; LICENSE.md.
- **M3 Go-ahead:** the author's say-so. Settling D9 first helps, since the shell carries the nav.
- **M4 The shell:** the template, the ☀️/🌙 button, the 💰 icon, sidebar and search, plus azqato.com's nav in both themes if D9 stays.
- **M5 Home and Resources:** from invests.html: the intro, "Join the Discord", section tiles, the 7 project cards, and the 15 resource categories with referral links and the disclosure.
- **M6 Learn and FAQ:** from stocks: the Learn landing page, Philosophy, Stock metrics, Index & ETF methodology, the Finviz and Seeking Alpha guides, and the FAQ.
- **M7 Strategies:** from leverage and vix: VIX Strategy, the leveraged landing page and the six strategies, with Composer Atlas links (D15, D16, D17).
- **M8 Tools:** Screener, Market Overview, VIX Dashboard and Custom builder, reading the existing data feeds (D6).
- **M9 Inventory check:** every page against its inventory (core rule).
- **M10 Publish:** choose the host and address (D4); publish; switch the old addresses to redirects (D7); add sitemap.xml and robots.txt where this site owns its origin; confirm the deploy against the local copy.
- **M11 Corrections:** one pass over out-of-date content (D19), for example the Holy Grail page's metrics, from Composer Atlas.

### Development plan

Every step and substep from the go-ahead (M3) to the correction pass (M11), written on 2026-10-01 at the author's request. Each phase lists what it needs before it starts, its steps, and what "done" means. Steps are numbered by phase (P0, P1 and so on) so they can be referred to and ticked off. The rules that apply throughout:

- Everything stays local until the author says otherwise (D20). Phases P0 to P9 are all local work; only P10 publishes, and only on the author's word.
- The core rule governs every page move: list everything first, move it, then check every item (Core rule).
- Testing follows Testing Cadence: make all of a phase's edits, then run the assumption check and one browser test at the end of the phase, not between edits.
- Each finished phase gets a PATCHNOTES.md entry and ticks the verification checklist for the sections it touched (Working Practice).
- Where a step needs an open question answered, it names the question and the default used if the author hasn't answered by then.

#### Phase overview

| Phase | Milestone | What it produces | Needs first |
|---|---|---|---|
| P0 | M3 | Answers to the blocking questions and a working setup | The author's go-ahead |
| P1 | M4 | Source snapshots and full page inventories | P0 |
| P2 | M4 | The shell: template, both themes, sidebar, search, theme button, icon | P1 |
| P3 | M5 | Home and Resources | P2 |
| P4 | M6 | Learn (6 pages) and FAQ | P2 |
| P5 | M7 | Strategies (8 pages) | P2 |
| P6 | M8 | Tools (4 pages) with live data | P2 |
| P7 | M9 | Site-wide checks: inventories, links, titles, accessibility, speed | P3 to P6 |
| P8 | M9 | Documentation brought in line with the built site | P7 |
| P9 | M10 | A publish plan ready to run | P8, Question 1 |
| P10 | M10 | The published site and the D7 redirects | P9 and the author's go-ahead to publish |
| P11 | M11 | Out-of-date content corrected (D19) | P10 |

P3 to P6 can run in any order once P2 is done; the order shown is the plan's build order (Next steps).

#### P0. Go-ahead and setup (M3)

Needs: the author's go-ahead to build.

1. **Settle what the shell depends on.** Ask the author, one question at a time:
   1. Question 2, azqato.com's nav (D9). Default if unanswered: keep it, in both themes.
   2. Question 3, the page addresses. Default: the proposed layout in step P0.3.
   3. Question 6, the brand in titles. Default: "Azqato Invests".
   4. Question 8, a skip link. Default: none, following Template Interface.
   5. Question 9, the home page colors. Default: the site's own themes.
   6. Question 10, the template's demo parts. Default: remove them.
   7. Record each answer in the section it affects, and mark the question answered under Risks and Open Questions.
2. **Decide about version control.** Ask Question 5 (the repository). Whatever the answer, nothing is pushed (D20).
   1. If the author wants a local git repository now: initialize it with `main` as the default branch, add `.gitattributes` (`* text=auto eol=lf`), and make a first commit of the docs. Update Repository Hygiene's current state.
   2. If not: work continues in the OneDrive folder, and each phase starts by copying the folder as a backup.
3. **Fix the folder layout.** Proposed, pending Question 3: one folder per section so each page has a short address. (Superseded by v1.1.0; the current layout is under Folder structure.)

   ```
   index.html                      Home
   resources/index.html            Resources
   learn/index.html                Learn landing
   learn/philosophy.html, metrics.html, indices.html, finviz.html, seekingalpha.html
   tools/screener.html, market.html, vix-dashboard.html, vix-custom.html
   strategies/vix.html             VIX Strategy
   strategies/leveraged/index.html Leveraged strategies landing
   strategies/leveraged/3sig.html, 6sig.html, 9sig.html, tqqq-ftlt.html, holy-grail.html, hfea.html
   faq.html                        FAQ
   assets/css/                     Template Interface's shared CSS, then the site's own
   assets/js/                      The site's scripts
   ```

   1. Write the chosen layout into Folder structure under Technical Requirements.
   2. Use relative links only, so the site works from any base path (Verification Environment).
4. **Check the tools.**
   1. Confirm Python 3 runs `python -m http.server 8000` from the folder.
   2. Confirm headless Edge runs at the path under Browser Testing.
   3. Confirm the GitHub CLI can still read `Azqato/templateinterface`, `Azqato/stocks`, `Azqato/vix` and `Azqato/leverage`.
5. **Write a check script** (Python, kept in the repository, for example `scripts/check.py`). It grows phase by phase and, at the end, checks: every page has a title within the Page Titles rules; every internal link resolves; no template demo text survives ("Parcelpoint", "API v3.4", "Get API keys"); no em dashes in this site's own text; every inventory item is present. It reads files only and changes nothing.

Done when: the blocking answers (or defaults) are recorded, the layout is written down, the tools run, and the check script exists.

#### P1. Source snapshots and inventories (M4)

Needs: P0. Sources keep changing, so this is redone for each page right before it moves (step P1.4).

1. **Snapshot the sources, read-only.** Download each source page from its repo's main branch with the GitHub CLI into a working folder outside the site (for example `_sources/`, listed in the ignore file if git is used). Never change the source repos.
   1. stocks: the 9 pages, plus the scripts and stylesheets they load.
   2. vix: the 3 pages, plus vix.js and their stylesheets.
   3. leverage: the 7 pages, plus their stylesheets.
   4. azqato.github.io: invests.html only.
   5. Record each repo's commit hash and the date in PATCHNOTES.md.
2. **Take an inventory of every page.** One file per page (for example `inventory/stocks-screener.md`), listing every item the core rule protects, in page order:
   1. headings and sections, with their text;
   2. paragraphs (first and last few words, so each can be found again);
   3. lists, tables (with row and column counts) and code;
   4. charts and what each plots;
   5. tools, controls, settings and defaults;
   6. data feeds, with their addresses and fallbacks;
   7. every link, with its destination, marking referral links;
   8. disclaimers, risk warnings and the affiliate disclosure, word for word;
   9. images, icons and emoji;
   10. scripts the page runs and what each does, including browser storage keys.
3. **Read what the audit couldn't.** While taking inventories, record:
   1. how each tool renders data and what it shows when every feed fails (Risks and Open Questions);
   2. whether the stocks fallback is a relative path (Background findings);
   3. whether any page inserts fetched text as HTML (Security);
   4. how the VIX charts present their numbers to screen readers (DESIGN.md);
   5. the tools' own colors (DESIGN.md, Data colors);
   6. any em dashes in source text, listed for the author, not changed (Question 14).
4. **Refresh before each move.** Right before a page moves, compare its source with the snapshot. If it changed, update the snapshot and the inventory first.

Done when: all 20 pages have inventories, and the findings in P1.3 are written into the PRD and DESIGN.md sections they belong to.

#### P2. The shell (M4)

Needs: P1. Produces one empty page that every other page is built from.

1. **Copy the template.** From Template Interface at a recorded commit, copy theme.css, base.css, components.css, documentation-site's styles.css and script.js, and wiki-portal's styles.css. Record the commit in PATCHNOTES.md. Never redefine a theme.css token.
2. **Split documentation-site into one file per page.** The template switches seven demo pages by URL hash in one file (Design details).
   1. Keep one page shell: top bar, sidebar, main column, "On this page", footer.
   2. Strip the hash routing from script.js, keeping its other behavior (drawer, search dialog, "On this page" tracking, copy buttons if any code remains).
   3. Remove the demo-only parts: the API keys button, status line, version label, code-language tabs, feedback form and the "Back to Template Interface" bar (Question 10).
   4. Remove all demo text and the template's title.
3. **Build the top bar.**
   1. The 💰 Azqato Invests logo, linking to Home (D11).
   2. The search button, kept with its / and Ctrl+K shortcuts.
   3. The ☀️/🌙 button (D10), with an accessible name that says what it does.
   4. If D9 stays: azqato.com's nav above the top bar, as a copy with links back to azqato.com, Invests marked current. Record it under Repository Hygiene as a copied file with its source.
4. **Build the sidebar.** The five groups, Learn, Tools, Strategies, Resources and FAQ (D12), with every page from the Site map. No entries for Composer Atlas, Net Worth Tracker or Automate Fundamentals (D18). Mark the current page. Give the sidebar a label that fits this site.
5. **Add the dark theme.**
   1. Give every `--pp-*` token a dark value under a dark-theme selector, starting from the role pairings in DESIGN.md.
   2. Override every literal color listed in DESIGN.md (white backgrounds, white text, inline code, tags, shadows, scrims).
   3. Give solid buttons dark text in dark (white on the dark accent fails contrast).
   4. If D9 stays, give azqato.com's nav a light version.
6. **Make the theme button work.**
   1. Start in the visitor's system theme.
   2. Save the choice in the visitor's own browser when the button is pressed.
   3. Apply the saved theme with a small script in the page head, before the page draws, so it never flashes.
   4. Decide which emoji the button shows in each theme, and record it in DESIGN.md.
7. **Add the favicon.** 💰 as an inline SVG data URI, the technique azqato.com uses (Design details). The template's favicon.png doesn't come over.
8. **Build the search index.** Read how the template's script.js searches, then make it search all 21 pages: titles, headings and text. Choose between a hand-kept index file and one the check script generates, and record the choice in Technical Requirements.
9. **Add breadcrumbs, pager and footer.** Breadcrumbs from the site map; previous and next following the sidebar order; footer content decided with the author.
10. **Make a tool-page variant** without "On this page" and with the 760px content cap lifted (Design details).
11. **Make the home page shell** from wiki-portal's layout, in the site's themes (Question 9). Settle the drawer width difference (900px against 760px) noted in DESIGN.md.
12. **Test the shell** (major update): assumption check, then one headless Edge run of the empty page and the home shell in both themes, at desktop and phone widths: no console errors, the drawer opens and closes, search opens from the keyboard, the theme survives a reload, focus is visible everywhere, and every color pairing passes the contrast check.

Done when: an empty inner page, a tool page and the home shell all pass P2.12, and DESIGN.md's verification checklist rows for palette, typography, spacing, breakpoints and components are ticked.

**Built 2026-10-02** (testing waits for the end of P6, at the author's request, so "done" waits for P2.12):

1. Template Interface had moved on to commit ed840da ("Finish M18 dark mode...", v0.15.0) since the 61acfcb read on 2026-10-01. The copies come from ed840da: theme.css, base.css and components.css unchanged, and documentation-site's styles.css as assets/css/docs.css, unchanged. The template now has its own dark mode (`:root[data-theme="dark"] .pp-page`), so P2.5 uses it rather than building one from the shared tokens. The snapshot is in `_sources/templateinterface/`.
2. Split into one file per page. assets/js/site.js keeps the template script's drawer, "On this page", search and keyboard shortcuts; the hash routing, code tabs, copy buttons and feedback form are gone. The demo parts and text never come over: the shell is written fresh in scripts/site.py.
3. Top bar: 💰 Azqato Invests linking to Home, search with / and Ctrl+K, and the theme button. azqato.com's nav sits above it (D9), as a copy with every link pointing back to azqato.com and Invests marked current.
4. Sidebar labeled "Site sections": Home, then Learn, Tools, Strategies (the six leveraged strategies indented under Leveraged strategies), Resources and FAQ. No Composer Atlas, Net Worth Tracker or Automate Fundamentals entries (D18). A small card at its foot repeats "Educational use only. Not financial advice." from the source sidebars.
5. Dark theme: the template's own dark tokens. The moved content's colors are mapped to the site's tokens in site.css; data colors keep the source values in dark and get darker counterparts in light (DESIGN.md, Data colors). azqato.com's nav has a light version.
6. Theme button: assets/js/theme.js, adapted from the template's theme-toggle.js. Starts in the visitor's system theme, saves the choice under `azqato-invests-theme` in the visitor's browser, applies it in the head before the page draws, and shows the theme it switches to (☀️ while dark, 🌙 while light), with the accessible name "Switch to light theme" or "Switch to dark theme".
7. Favicon: 💰 as an inline SVG data URI.
8. Search: scripts/site.py generates assets/js/search-index.js (every page's title, h2 and h3 sections and their text; about 310 KB), which site.js loads the first time search opens. Chosen over a hand-kept index so it can't drift from the pages.
9. Breadcrumbs from the site map; previous and next follow the sidebar order; footer (default, for the author to change): the brand, "Educational use only. Not financial advice. Some links are referral links.", links to Resources and the FAQ, and "Built by Azqato".
10. Tool pages (`is-tool`) have no "On this page" and no 760px cap.
11. Home uses the same shell as the inner pages, with the content capped at 1120px (wiki-portal's width) and no "On this page". That settles the drawer difference: Home switches to the drawer at 900px like every page.
12. Not run yet (after P6).

Added beyond the plan: a "Skip to content" link (Question 8), and scripts/site.py itself, which builds every page from the snapshots (Technical Requirements, System architecture).

#### P3. Home and Resources (M5)

Needs: P2, and the invests.html inventory from P1.

1. **Refresh** invests.html's snapshot and inventory (P1.4).
2. **Split invests.html between two pages** (it becomes Home and Resources). Mark each inventory item with the page it goes to. Nothing is left unassigned.
3. **Build Home.**
   1. The intro and the "Join the Discord" button (D14).
   2. Tiles into Learn, Tools, Strategies, Resources and FAQ.
   3. All 7 project cards with their full text (D14, D18). Stocks, Stock Screener, VIX Strategy and Leveraged Strategies now link inside the site; Automate Fundamentals, Composer Atlas and Net Worth Tracker link out.
   4. Composer Atlas links go to composeratlas.com, not the old azqato.github.io/composer copy (Composer Atlas).
   5. Optional, from wiki-portal's rating: a live VIX reading in the statistics list, read from the same feed as the VIX pages.
4. **Build Resources.** All 15 categories with every link, referral links included, and the affiliate disclosure word for word (D13).
5. **Write titles and share tags.** Home: "Azqato Invests - Investing Tools and Resources" (proposed). Resources: "<name> - Azqato Invests". og:title, og:description and the other tags follow Social Sharing Tags; og:url waits for the address (Question 1).
6. **Check both inventories** item by item against the new pages, then run the phase's browser test.

Done when: every invests.html item is on Home or Resources, and both pages pass the browser test in both themes.

**Built 2026-10-02** (the inventory check and browser test run after P6):

1. Refreshed: stocks 60a599e, vix cd92561, leverage c86321c and azqato.github.io 58767b5, all unchanged since 2026-10-01.
2. The split (scripts/site.py, `split_invests`): Home gets the intro (the "Azqato Invests" heading, the paragraph, "Join the Discord" and "Explore the projects") and the Projects section; Resources gets the Curated Resources section with its disclaimer. Both keep the source footer, "Built by Azqato." azqato.com's own nav at the top of invests.html becomes the site's copy of it (D9).
3. Home: the intro; "Explore the site", five tiles into Learn, Tools, Strategies, Resources and FAQ (new text, this site's own); all 7 project cards with their full text. Stocks, Stock Screener, VIX Strategy and Leveraged Strategies now open the site's own pages in the same tab; Automate Fundamentals, ComposerAtlas (now composeratlas.com) and Net Worth Tracker still open outside in a new tab. "Join the Discord" points to azqato.com/discord, since the source's relative `discord.html` only worked on azqato.com. The optional live VIX statistic wasn't added.
4. Resources: all 15 categories and all 71 links, referral links included, with the disclaimer word for word. Its heading, "Curated Resources", becomes the page's h1.
5. Titles: "Azqato Invests - Investing Tools and Resources" and "Curated resources - Azqato Invests". Home keeps invests.html's description; Resources has a new one. og:title, og:description, og:site_name and twitter:card are set; og:url and canonical wait for the address (P9).
6. After P6.

#### P4. Learn and FAQ (M6)

Needs: P2, and the stocks inventories.

1. **For each page** (Learn landing from stocks/index.html, then Philosophy, Stock metrics, Index & ETF methodology, the Finviz guide, the Seeking Alpha guide):
   1. Refresh the snapshot and inventory.
   2. Move every section into the documentation-site article layout, keeping the wording exactly.
   3. Turn the setup guides' steps into numbered steps (help-center's pattern, D8) without changing their text.
   4. Rewrite links between source pages to the new addresses; leave outside links as they are.
   5. Write the title and share tags.
   6. Check the inventory.
2. **Build the FAQ** from stocks/faq.html, the largest page.
   1. Every question and answer, word for word, in source order.
   2. Search-as-you-type over the questions (help-center's pattern, D8).
   3. Anchors so each answer can be linked.
3. **Check "On this page"** lists match each page's headings.
4. **Run the phase's browser test.**

Done when: all 7 pages pass their inventories and the browser test.

**Built 2026-10-02** (inventory checks and the browser test run after P6):

1. Learn landing (from stocks/index.html), Philosophy, Stock metrics, Index & ETF methodology, the Finviz guide and the Seeking Alpha guide.
   1. Refreshed with the P3 refresh; unchanged.
   2. Each page's content moved whole, wording unchanged, with its own section ids, so old anchors such as `metrics.html#metric-peg-fwd` still work at the new address.
   3. The two setup guides already number their steps (`guide-step` with `step-num`), the same pattern help-center uses, so their markup moved as it is.
   4. Links between source pages point to the new addresses (relative links, such as `metrics.html` from another Learn page, or `../faq.html#palantir`); outside links are unchanged.
   5. Titles: "<label> - Azqato Invests" (the Learn landing is "Learn - Azqato Invests"); each keeps its source description.
   6. After P6.
2. FAQ (from stocks/faq.html): all 37 questions and answers in source order, in the source's accordion (stocks' script.js, copied). The source has no section headings, so the page has no "On this page" list.
   1. Word for word, in source order.
   2. A "Filter the questions" box under the heading hides questions that don't contain every word typed, and announces the count (help-center's search-as-you-type).
   3. Each answer keeps its source id; site.js opens the answer a link points to (for example `faq.html#palantir`).
3. "On this page" is built from each page's h2 headings when the page loads (site.js); headings without an id get one from scripts/site.py.
4. After P6.
#### P5. Strategies (M7)

Needs: P2, and the vix and leverage inventories.

1. **VIX Strategy** from vix/index.html: every section; the last-known reading painted from browser storage as the source does; links to the VIX Dashboard and Custom builder at their new addresses.
2. **Leveraged strategies landing** from leverage/index.html.
3. **The six strategies**: 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA. For each:
   1. Every section, keeping the source's structure and wording (Overview, Rules and Logic, Performance Notes, Risks and Caveats, Resources where the source has them).
   2. Risk warnings kept in full.
   3. Composer Atlas links (D15, D16, D17): TQQQ FTLT to `tqqq-long-term`, `zoops-tqqq-long-term-2026` and `zoops-upro-ftlt-2026`; Holy Grail to `holy-grail` and `zoops-holy-grail-2026`; HFEA to its community-database entry, symphony `Cjb5ysKtJsPv6Tm3Fk0R`, once the link format is confirmed (Question 4); 3 Sig, 6 Sig and 9 Sig none.
   4. Old azqato.github.io/composer links changed to composeratlas.com (core rule: allowed).
   5. Out-of-date content left as it is (D19), noted for P11.
4. **Check every inventory, then run the phase's browser test.**

Done when: all 8 pages pass their inventories and the browser test, and every Atlas link opens the right strategy.

**Built 2026-10-02** (inventory checks, the browser test and opening each Atlas link run after P6):

1. VIX Strategy (strategies/vix.html, from vix/index.html): every section; the source's inline script still paints the last-known reading from `vix_last_known` first, then loads https://azqato.github.io/vix/data/vix.js (D6) with vix.js and strategy.js from assets/js/vix/. Its "View Live Strategy" link opens the VIX Dashboard at its new address. The source page links only to the Dashboard in its content; the Custom builder is in the sidebar.
2. Leveraged strategies landing (strategies/leveraged/index.html), with its links to the six strategies.
3. The six strategies, each with its source sections (Overview, Rules and Logic, Performance Notes, Risks and Caveats, Resources) and risk warnings in full.
   1. As in the source.
   2. Kept in full.
   3. An "On Composer Atlas" note sits above the first section: TQQQ FTLT links `tqqq-long-term`, `zoops-tqqq-long-term-2026` and `zoops-upro-ftlt-2026` (the page's own link to `tqqq-long-term` stays too); Holy Grail links `holy-grail` and `zoops-holy-grail-2026`. **HFEA (Question 4):** Composer Atlas has no address for a single community-database entry (its code, read 2026-10-02, reads no entry from the address), so the note links the database page, composeratlas.com/database.html, and names symphony `Cjb5ysKtJsPv6Tm3Fk0R` to search for. Change it if Atlas adds entry links. 3 Sig, 6 Sig and 9 Sig get none.
   4. The old azqato.github.io/composer links were only in the leverage sites' navigation, which the shell replaces; scripts/site.py would change any in content to composeratlas.com.
   5. Out-of-date content is unchanged (D19), including the Holy Grail page's note that no factsheet data was available; it waits for P11.
4. After P6.

The leverage pages' main.js isn't carried: it only drove their sidebar's "On This Page" highlighting and the mobile menu, which the shell does now.
#### P6. Tools (M8)

Needs: P2, the stocks and vix inventories, and the P1.3 findings.

1. **Screener** from stocks/screener.html, on the tool-page variant.
   1. Keep every filter, column, preset, sort and the click-for-breakdown view.
   2. Read data from raw.githubusercontent.com/Azqato/stocks/main/data/ (D6).
   3. Repoint the local fallback if P1.3 found it relative (Background findings).
   4. Apply admin-dashboard's table styling (D8) without dropping any column.
2. **Market Overview** from stocks/market.html: same feed; keep its browser cache key and behavior.
3. **VIX Dashboard** from vix/strategy.html and **VIX Custom builder** from vix/custom.html.
   1. Load the reading from https://azqato.github.io/vix/data/vix.js, never raw GitHub (D6, nosniff).
   2. Keep the allorigins fallback and the `vix_last_known` cache.
   3. Keep Chart.js 4.4.0; add an integrity hash if the author agrees (Question 12).
   4. Live numbers change without animation (DESIGN.md).
4. **Make the charts and tables work in both themes**: chart colors, grid lines and text readable in light and dark; record the tools' colors in DESIGN.md.
5. **Test each failure path**: block each feed in turn in headless Edge and confirm the page falls back as the source does.
6. **Check data freshness**: the shown timestamps match the newest data commits in stocks and vix.
7. **Check every inventory, then run the phase's browser test.**

Done when: all 4 tools show current data in both themes, fall back correctly, and pass their inventories.

**Built 2026-10-02** (steps 5 to 7 are tests and run with the rest after P6):

1. Screener (tools/screener.html), on the tool-page variant.
   1. Every universe button, filter, column, preset, sort, the breakdown modal and the methodology modal, moved whole with their ids, so screener.js (copied to assets/js/stocks/) works unchanged. Its links to the Metrics glossary and the Indices methodology still open in a new tab, as in the source, so the screener keeps its state.
   2. Data still comes first from raw.githubusercontent.com/Azqato/stocks/main/data/ (D6).
   3. The relative `data/` fallback now points to https://azqato.github.io/stocks/data/ (Background findings), in screener.js and every fallback path.
   4. The source's own table styles are kept, scoped, with the template's table colors; no column is dropped. admin-dashboard's table styling wasn't copied in (its code wasn't read); revisit at the author's review.
   The screener was a full-window app (its own scroll regions, `overflow: hidden` on the page); here it sits in the page and scrolls with it.
2. Market Overview (tools/market.html): same feed and fallback change; its inline script, cache key and behavior are unchanged.
3. VIX Dashboard (tools/vix-dashboard.html) and VIX Custom builder (tools/vix-custom.html).
   1. The reading loads from https://azqato.github.io/vix/data/vix.js (D6).
   2. vix.js is unchanged apart from em dashes in its comments: the allorigins fallback and the `vix_last_known` cache stay.
   3. Chart.js 4.4.0 with an integrity hash (`sha384-e6nUZLBk...`, computed 2026-10-02 from the jsDelivr file) and `crossorigin="anonymous"` (Question 12).
   4. Live numbers: the source's own behavior is kept. The donut chart's draw animation is the source's and stays.
4. Charts in both themes: the donut's center text, label color and segment border read the theme's colors (assets/js/vix/chart.js, a marked change); the ticker colors keep their source values in dark and take darker ones in light (DESIGN.md, Data colors). Contrast is checked in the test.
5. to 7. After P6.
#### P7. Site-wide checks (M9)

Needs: P3 to P6.

1. **Inventories**: re-run every page's inventory against a fresh source snapshot; 100% of items found (Success criteria 1).
2. **Reachability**: all 21 pages linked from the sidebar or Home; search finds each by its title (Success criteria 2).
3. **Links**: 0 broken internal links; outside links spot-checked.
4. **Titles and tags**: the check script's Page Titles and Social Sharing Tags checks pass, counted by script.
5. **Accessibility**: contrast of every pairing in both themes; keyboard-only walk through each page type; focus into and out of the drawer and search dialog; landmarks; the skip-link decision applied.
6. **Speed**: Lighthouse in Edge DevTools, mobile, on Home, the Screener and one strategy page: LCP 2.5 s or less, CLS 0.1 or less, TBT 200 ms or less.
7. **Writing style sweep** of this site's own text; source text reported, not changed.
8. **Security pass**: no fetched text inserted as HTML, `rel="noopener"` on new-tab links, no secrets anywhere.
9. **Show the author** the finished site locally and collect changes.
10. **Author review of the drafted sections** (Question 15): tenets, personas, user stories, goals, success criteria, metrics, press release and FAQ, updated to match the built MVP.

Done when: every check passes or each exception is approved by the author and recorded.

**Done 2026-10-02 (steps 1 to 8), in headless Edge and with the check scripts:**

1. Inventories: `python scripts/snapshot.py` took fresh snapshots (stocks 860ee2b9, vix 37eeadd1, leverage c86321cd, azqato.github.io 58767b54, the same commits as the last build), then `python scripts/inventory.py`, `python scripts/site.py` and `python scripts/check.py`: 21 pages, every inventory item found, 0 failures.
2. Reachability: all 21 pages are linked from the sidebar on every page (and from Home); the search index holds every page under its title.
3. Links: 0 broken internal links (check.py). Outside links: all 96 unique addresses were requested once each. 86 answered normally. 8 refused automated requests (403 from Investopedia twice, TheStreet twice, study.com and AAII; 503 from Zacks; Renaissance Capital refused a HEAD request), which is bot blocking, not a dead page. 2 are dead, both on Resources from invests.html: dividendstocksonline.com (expired security certificate, in Edge too) and www.denvercondomania.com (the connection times out, in Edge too). They're source content, so they stay as they are and are listed for P11 (D19).
4. Titles and tags: check.py's title checks pass on all 21 pages (20 to 46 characters). Every page has a description, og:title, og:description, og:type, og:site_name and twitter:card; og:url and the canonical link were added in P9.2, so all six sharing tags are now on every page.
5. Accessibility: Lighthouse accessibility 100 on all three pages measured; WCAG AA text contrast on every page in both themes is part of `python scripts/browser.py`. Keyboard walk on a Learn page: the first Tab reaches "Skip to content", Enter moves to `#pp-main`, then focus runs through the breadcrumbs, the inline "On this page" list and the sidebar in screen order, with a visible solid focus ring. `/` puts focus in the search box, results appear as you type, and Escape closes it and returns focus to where it was. On a phone-width page the menu button moves focus to the drawer's close button and sets `aria-expanded` to true; Escape closes the drawer, returns focus to the menu button and sets it back to false. Landmarks: one header, main, aside and footer, four labeled navigation regions, one h1, `lang="en"`. No button, link or field without an accessible name on Home, the Screener or the VIX Custom builder.
6. Speed: Lighthouse 13.5.0 from the command line (`npx lighthouse`, mobile settings) driving Edge, against the local server. Home: LCP 1.7 s, CLS 0, TBT 0 ms (performance 99). 9 Sig: LCP 1.7 s, CLS 0, TBT 0 ms (99). Screener: LCP 2.1 s, TBT 0 ms, but CLS 0.175 on the first run: the disclaimer under the table moved down when the data arrived. Fixed by holding 70vh of room for the table while it loads (assets/css/site.css); rerun: CLS 0.003. Best practices and SEO scored 100 on all three. Lighthouse's remaining suggestions (minify CSS and JavaScript, unused CSS, cache lifetimes) need a build step or host settings and weren't acted on.
7. Writing style: no em dashes in this site's own text (scripts/site.py, site.css, site.js, README.md, the docs) or in any page (check.py); no filler words found in the interface text. Source text was left as it is.
8. Security: every new-tab link carries `rel="noopener"`; no keys, tokens or passwords anywhere in the repository. The screener and Market Overview built rows and cards from feed text with `innerHTML` and no escaping (found in P1). Fixed: scripts/site.py now wraps their `res.json()` in `azqClean()`, which removes `<` and `>` from every text value in a fetched feed before the page uses it; company names and tickers never contain them. The other `innerHTML` uses build markup from the scripts' own constants or from numbers (the VIX tools and site.js, which escapes its search text).
9. Waiting for the author.
10. Waiting for the author.

#### P8. Documentation (M9)

1. Check every PRD and DESIGN.md section against the built site and tick the verification checklist with dates.
2. Record discrepancies under Documentation Versus Reality.
3. Fill in Conventions from the code, the Runbook from what was actually run, and Folder structure from the real tree.
4. Check docs/TODO.md and ask the author about any ideas (Working Practice).
5. Write the PATCHNOTES.md entry for the build.

**Done 2026-10-02:** 1. every section on the verification checklist was checked against the site and dated; 2. new discrepancies are under Documentation Versus Reality (entries 9 to 12), and entries 5, 7 and 8 are resolved; 3. Conventions, the Runbook and Folder structure are rewritten from the code and from what was run; 4. TODO.md holds only its placeholder, so there was nothing to ask; 5. PATCHNOTES.md v0.17.0. Also brought up to date: the milestone table, System architecture, Tech stack, Security, Repository Hygiene, Social Sharing Tags and Deprecation and Removal.

#### P9. Publish plan (M10)

Needs: P8 and an answer to Question 1 (the address). Prepares; publishes nothing.

1. Host decided (Question 1): GitHub Pages, from a public repository named `invests`, served at azqato.github.io/invests/. **Updated again 2026-10-02 (D21 changed):** a new repository, not the renamed stocks repository; stocks keeps its data and its Pages site for the data folder. Earlier note, superseded: Before the rename: list everything that reads azqato.github.io/stocks/ or the stocks repo by name (raw GitHub data addresses in the screener and other pages, the vix repo, workflows, azqato.com's links) and repoint it; plan the new `stocks` redirect repository; decide how this local repository's history joins the renamed one (commit the built site onto it, keeping the workflows and data folders). Before publishing: check how GitHub Pages resolves /invests/ next to azqato.github.io's invests.html, and what azqato.com (the Cloudflare build of azqato.github.io) serves at /invests/. Write Deploy and Rollback in the Runbook.
2. Fill og:url and canonical links with the final address.
3. Write robots.txt (fully open, with its comment) and sitemap.xml, if this site owns its origin.
4. Make the D7 redirect list: each of the 19 old addresses to its new page, one hop each. Choose the mechanism for the host the old sites use (redirect pages on GitHub Pages, to confirm).
5. Decide with the author what happens to azqato.com/invests (Question 1).
6. Answer Question 5 (the repository) and, if public, remove the private project's name from the docs first; add the issue tracker's address to LICENSE.md.

**Done 2026-10-02 (prepared, nothing published):**

1. Host: GitHub Pages from github.com/Azqato/invests (created by the author, private for now), served at https://azqato.github.io/invests/. Deploy and Rollback are written in the Runbook. How GitHub Pages resolves azqato.github.io/invests/ next to azqato.github.io's own invests.html can only be seen once both exist; Question 17 recommends retiring invests.html so the two never compete.
2. og:url and the canonical link are on every page, from `SITE_URL` in scripts/site.py (folder pages end in `/`, for example https://azqato.github.io/invests/learn/).
3. sitemap.xml lists all 21 pages, generated by scripts/site.py. No robots.txt: azqato.github.io owns the origin, so crawlers only read https://azqato.github.io/robots.txt, which belongs to the azqato.github.io repo. Licensing's rule (fully open, with a comment) applies there if that repo adds one.
4. The D7 redirect list (19 addresses, plus invests.html) and the mechanism are under Deprecation and Removal.
5. azqato.com/invests: needs the author's decision, Question 17, with a recommendation.
6. Question 5 answered (github.com/Azqato/invests, public later): the private project's name is out of the docs, and LICENSE.md gives https://github.com/Azqato/invests/issues as the place for permission requests. Before the repository goes public, Question 16.

#### P10. Publish (M10)

Only on the author's explicit go-ahead (D20).

**Done 2026-10-02 (steps 1 to 3):** pushed, deploy confirmed against the local copy, and data feeds and both themes checked live (Current phase). Steps 4 and 5 moved to P13 at the author's request. Step 6 is done in practice (azqato.com's nav, Home card and Links page link the site); step 7 is open.

1. Push and deploy.
2. Confirm the deploy: fetch every deployed file and compare it with the local copy.
3. Check the live site's data feeds and both themes.
4. Switch the old stocks, vix and leverage pages to redirects, keeping vix/data/vix.js and every data file serving (D6).
5. Check each of the 19 old addresses lands on its page in one hop (Success criteria 7).
6. Link the new site from azqato.github.io as decided.
7. Set up the metrics that need no tracking (Metrics) and start the 4-week baseline.

#### P11. Corrections (M11)

1. Gather every out-of-date item noted during P4 to P6.
2. Correct each with the author's approval, for example the Holy Grail metrics from Composer Atlas (D19).
3. Record each correction in PATCHNOTES.md.

**Done 2026-10-02 (main 2.13.3, build pass item 11), the owner-approved part:**

- The two dead Resources links (P13.3) are removed: Denver (www.denvercondomania.com, timed out) from Real Estate and Dividend Stocks Online (dividendstocksonline.com, expired certificate) from Databases. `scripts/site.py` drops them through `REMOVE_LINKS`; the inventories keep them as the record of the source, and `scripts/check.py`'s `REMOVED` stops expecting items 108, 109, 130 and 131.
- The Holy Grail page has a "Backtest on Composer Atlas" box after its Performance Notes' first paragraph, filled live from Composer Atlas on every page load (`ATLAS_FIGURES` in `scripts/site.py`). Atlas's `data/strategies.json` sends no CORS header, so the page loads `https://composeratlas.com/data/strategies.js` (about 490 KB, loaded async after the page) and reads `window.STRATEGIES_DATA`, slug `holy-grail`. Order: the figures built into the page (Atlas's 2026-10-01 reading), then the last live reading saved in localStorage, then the live reading. If Atlas can't be reached, the page says so and keeps the last figures it has. Tested in Edge live, with Atlas blocked after a visit, and with Atlas blocked on a first visit.
- The original text is unchanged; the sentences it makes out of date are on the list below.

**Corrections list for the owner (2026-10-02).** Nothing here is changed until the owner approves it, item by item (D19, core rule 1).

| # | Page | Now | Proposed |
|---|---|---|---|
| C1 | Leveraged Strategies, Holy Grail, Performance Notes | "No public factsheet data was retrievable (Composer requires authentication). The following observations are drawn from the strategy's structural properties and the academic basis." | "Composer Atlas publishes this strategy's backtest; the figures above load from it. The following observations are drawn from the strategy's structural properties and the academic basis." |
| C2 | Holy Grail, risks | "No public performance record is available. ... The backtest data on the Composer factsheet was not accessible without authentication." | Keep the first sentence (a backtest is not a live record); replace the last with "Its backtest is on Composer Atlas (above); a backtest is not a live record." |
| C3 | Resources, a "Top-rated stocks" link to thestreet.com/.../top-rated-stocks.html | Answers 404 (2026-10-02) | Remove, or replace with a current TheStreet ratings page if the owner has one |
| C4 | Resources, a "Top-rated ETFs" link to thestreet.com/.../top-rated-etfs.html | Answers 404 (2026-10-02) | Remove, or replace |
| C5 | Resources, Charts: RobinTrack (robintrack.net) | The site is up, but its data stopped in 2020, when Robinhood stopped publishing holder counts | Remove, or keep with "(historical, to 2020)" |
| C6 | Leveraged Strategies, HFEA: "Cost of leverage (as of 2018)" | An eight-year-old figure | Keep with its date as is, or the owner supplies a current figure |
| C7 | The "On Composer Atlas" boxes on TQQQ FTLT and Holy Grail | Three of the five links (the 2026 versions of TQQQ FTLT, UPRO FTLT and Holy Grail) are marked hidden in Atlas's data | Check those three open on Atlas; if not, drop them from the boxes |
| C8 | Leveraged Strategies, HFEA's Atlas link | Points at Atlas's database page with a symphony ID to search for; Atlas still has no HFEA entry (checked 2026-10-02) | No change until Atlas has one |

Checked and fine: Zacks (503) and Investopedia, study.com, Reddit, dividend.com and YCharts (403/405) refuse automated requests but open in a browser; every other outside link on Resources answered 200.

### Explicitly deferred

- **Correcting out-of-date content (D19):** waits until after the move, so each page is first checked against unchanged source text.
- **Redirects and publishing (D7, D20):** wait for the author's go-ahead, because they change live sites.
- **HFEA's Composer Atlas link:** waits until the way to link Atlas's community database is settled.
- **sitemap.xml and robots.txt:** wait for pages and an address (D4); see Folder structure under Technical Requirements. **Done 2026-10-02 (P9.3):** sitemap.xml is generated; robots.txt isn't this site's to write.
- **Atlas links for concepts (D17):** declined; concepts are explained on this site.
- **Merging Net Worth Tracker and the author's private project (D2):** declined; they stay separate.

### Future updates

Ideas from docs/TODO.md become entries here only with the author's say-so, following the five steps under Working Practice.

#### P12. Old repos become feeds and redirects (post-launch; added 2026-10-02)

Runs after P10, whenever the author decides to clean out the old repos. Each repo keeps running on its own; this site only reads from it (D21).

1. stocks: its pages become redirects to this site (D7); its scheduled jobs and data/ stay as the data feed.
2. vix: the same, and its feed gets a second copy for fallback. Found in the 2026-10-02 browser test: when data/vix.js on azqato.github.io fails and the visitor has no cached reading, the VIX pages stay on "Fetching data…", because the allorigins fallback is refused by the browser (CORS).
   1. Load the same file from raw.githubusercontent.com/Azqato/vix/main/data/ as the second source. Optionally the vix job also writes data/vix.json, so it can be read as data rather than run as a script (raw GitHub won't run vix.js; Constraints).
   2. Drop the allorigins fallback.
   3. With every source down, show the cached reading if there is one, otherwise a clear "unavailable" state.
3. Remove the leverage sites' pages the same way, as redirects (D7).
4. Record each change in PATCHNOTES.md and in the old repos' own notes.

**Step 2 done 2026-10-02 (main 2.13.4, build pass item 10):**

- The vix repo (its v1.3.0) writes `data/vix.json` beside `data/vix.js` on every run of `update-vix.yml`; a manual run on 2026-10-02 succeeded and wrote it. raw.githubusercontent.com serves it with `Access-Control-Allow-Origin: *`.
- The Invests copy of `vix.js` is rewritten at build time by `vix_sources()` in `scripts/site.py` (the snapshot in `_sources/` is unchanged): the allorigins URLs are gone; the second source is `https://raw.githubusercontent.com/Azqato/vix/main/data/vix.json`, independent of GitHub Pages, with an 8 second timeout.
- With every source down: the saved reading if there is one, marked STALE; otherwise the existing error state ("ERROR, Unable to fetch - check connection"), which `browser.py` confirms appears instead of a page stuck on "Fetching data…".
- Tested with `browser.py`: with azqato.github.io/vix/data/vix.js blocked and nothing cached, the Dashboard shows the live reading from vix.json (it used to stay on "Fetching data…"). 0 failures.
- The stocks job is unchanged and still runs on its schedule (its data serves the Screener and Market Overview; `browser.py` read 121 rows).

#### P13. Post-launch list (added 2026-10-02, at the author's request)

1. **D7 redirects for the 19 old addresses (on the roadmap; ask before starting, it changes the stocks, vix and leverage repos).** Each old page becomes a redirect page to its new address, keeping every data file serving (stocks `data/`, vix `data/vix.js`). Per page: the old title, `<link rel="canonical" href="NEW">`, `<meta http-equiv="refresh" content="0; url=NEW">`, `<script>location.replace("NEW" + location.hash)</script>` and a plain link. Check each lands in one hop. The list is under Deprecation and Removal. The old sites are served under azqato.github.io (and under azqato.com only if those repos have their own Cloudflare setup; check before writing the redirects).
2. **The author's review of the live site (P7.9)**, then P7.10 (the drafted PRD sections: tenets, personas, user stories, goals, success criteria, metrics, press release, FAQ).
3. **Two dead outside links on Resources (on the roadmap),** from the old invests.html: dividendstocksonline.com (expired certificate) and www.denvercondomania.com (times out). Source content, so fixed or removed only with the author's approval (P11).
4. **Delete the empty github.com/Azqato/invests repository** once testing of the live site is finished (author's decision, 2026-10-02). It was never pushed to and isn't needed for hosting. **Done:** by the 2026-10-02 audit, `gh api repos/Azqato/invests` answered 404 while logged in as Azqato, so the repository is gone.

#### P14. Fold invests into azqato.com's structure (later; design needed; ask first)

**Docs part done 2026-10-02:** these docs merged into the main repository's docs (this PRD is Part 2 of docs/PRD.md; D22). The pages, generator and inventories haven't moved. The author intends it but hasn't said how. Settle first: whether the invests pages adopt azqato.com's nav and styles.css or keep their own shell; where the generator, inventories and these docs live (for example `tools/invests/` and `docs/invests/` in the main repository, so scripts aren't public addresses under /invests/; today `invests/scripts/`, `invests/docs/` and `invests/inventory/` are publicly reachable, and hold nothing private); and whether this PRD merges into the main repository's PRD. Every page address is public now, so any move needs redirects under the removal policy.

#### P15. Adopt azqato.com's colors (added 2026-10-02, owner's request; ask first)

**Decided 2026-10-02:** the owner picked one palette for both halves of the site, dark and light; it's in DESIGN.md, One palette for the whole site. It's built with Roadmap at a glance items 5 to 8.

Move the site's colors to azqato.com's palette (the tokens in the main repository's styles.css), so Invests and the main site look like one site. Before changing anything, ask the author which current colors to keep for things that carry meaning: for example the emerald accent and links, the VIX tier colors (calm to panic), gains and losses (green and red) in the Screener and Market Overview, the leverage risk notices, and the Discord button. Keep WCAG AA contrast in both themes (DESIGN.md, Data colors). Pairs with the main PRD's Future update for the shared top bar and theme button, which needs a light palette for the main site.

#### P16. Combine the three VIX pages (added 2026-10-02, owner's request; ask first)

The VIX Strategy, VIX Dashboard and VIX Custom builder explain and run one strategy across three pages. Combine them into one VIX page (or one page with sections or tabs), keeping every item from all three (core rule). Settle first: one page or a landing page with two tools; which address survives; redirects for the others (Deprecation and Removal). Related: the navigation restructure (2026-10-02 proposal), which first groups the three together.

#### P17. SEO and landing-page review of every page (added 2026-10-02, owner's request; ask first)

Review the content of all 21 pages against SEO best practice: one clear topic and search intent per page, a descriptive title and meta description, one h1 and a sensible heading order, internal links between related pages, and a reasonable length. In particular, consider turning each group's landing page (Individual Stocks, Indices & ETFs, VIX Strategy, Leveraged Strategies) into a short landing page with clear calls to action into its pages, instead of carrying the whole method at once; the long text would move to its own page in the group. That changes source content, so it needs the author's approval page by page (core rule, D19), and it fits with P11's corrections pass and P16 (one VIX page).

### Verification checklist

Each PRD and DESIGN.md section that describes the code, and when it was last checked in full against the code. Every section was checked against the built site on 2026-10-02 (P8.1); what didn't match is under Documentation Versus Reality. The 2026-10-02 documentation audit (after v1.1.0) rechecked the rows marked "Audit".

| Section | Status |
|---|---|
| PRD: Folder structure (current tree) | Audit 2026-10-02: matches the folder after v1.1.0 |
| PRD: Site map | Audit 2026-10-02: matches the page list in scripts/site.py (v1.1.0) |
| PRD: Repository Hygiene (current state) | Updated 2026-10-02: lives in the azqato.github.io repository as `invests/` (single source of truth); `.gitattributes` and `.gitignore` present; the separate repository is retired |
| PRD: What's being merged (source page lists) | Verified 2026-10-02 against fresh snapshots of stocks, vix, leverage and azqato.github.io (P7.1) |
| PRD: System architecture | Verified 2026-10-02 against scripts/site.py and the built pages |
| PRD: Tech stack | Verified 2026-10-02: no manifests; Python 3.14.3, bs4, Playwright; Lighthouse through npx for P7 only |
| PRD: Data models | Verified 2026-10-02 for what the pages read (addresses and storage keys); the feeds' schemas belong to the stocks and vix repos |
| PRD: API design (internal data flow) | Verified 2026-10-02 against the built tools and browser.py's feed tests |
| PRD: State management | Verified 2026-10-02: three localStorage uses, no cookies |
| PRD: Third-party integrations | Verified 2026-10-02 against the hosts the built pages request |
| PRD: Performance requirements | Verified 2026-10-02 with Lighthouse on Home, the Screener and 9 Sig (P7.6) |
| PRD: Security | Verified 2026-10-02 (P7.8) |
| PRD: Runbook | Audit 2026-10-02: every local command was run; Deploy was run for v2.11.0 to v2.11.3 of the main repository; Rollback not needed yet |
| PRD: Page Titles and Social Sharing Tags | Verified 2026-10-02 by script on all 21 pages (P7.4) |
| PRD: Deprecation and Removal (public surface) | Audit 2026-10-02: the 21 live addresses, the retired pre-v1.1.0 addresses and the D7 list checked against sitemap.xml and the snapshots' page lists |
| DESIGN: Color palette | Verified 2026-10-02: docs.css and theme.css carry the recorded values; contrast tested in both themes by browser.py |
| DESIGN: Typography | Verified 2026-10-02, including the 12px floor and the table fonts (v0.16.0) |
| DESIGN: Spacing system | Verified 2026-10-02 against docs.css (`--pp-top` 60px, `--pp-rail-w` 260px, `--pp-radius` 6px) |
| DESIGN: Breakpoints | Verified 2026-10-02: docs.css uses 1150, 1000, 900, 640 and 400px; site.css adds rules at 900 and 640px; Home uses the inner pages' breakpoints, not wiki-portal's (Documentation Versus Reality, entry 11) |
| DESIGN: Component patterns | Audit 2026-10-02: Sidebar, Breadcrumbs and pager, Search and Theme button updated for v1.0.1 and v1.1.0 |
| DESIGN: Accessibility standards | Verified 2026-10-02 (P7.5): skip link, focus order, drawer and search focus, landmarks |
| DESIGN: Animation and motion | Verified 2026-10-02: docs.css and theme.css carry the reduced-motion rules |
| DESIGN: Theme switching and icon | Verified 2026-10-02 against assets/js/theme.js and the favicon in scripts/site.py |

## Invests: Metrics

Every metric has to work without tracking (Assumptions). **Changed 2026-10-02 (owner's review):** the north star, acquisition and engagement metrics are postponed: they rely on host or analytics counts, and the owner has put Cloudflare analytics off until much later. The performance table stands; uptime has no target and isn't monitored for now. The targets were set by the 2026-10-01 audit as defaults for the author to confirm (Question 11).

- **North star: weekly page views across the site.** One number for whether people use the site. Target: record a baseline over the first 4 weeks after launch, then set a growth target from it. Measured with the host's own aggregate request counts, if the host chosen under D4 provides them without cookies or scripts; GitHub Pages provides no visitor statistics. Reviewed monthly after launch.
- **Acquisition:**
  - Search impressions and clicks. Target: baseline over the first 8 weeks after launch. Measured with Google Search Console and Bing Webmaster Tools, which count on the search engine's side (site ownership has to be verified first). Monthly.
  - Page views by referrer (Discord, azqato.com, search). Target: baseline after launch. Host aggregate statistics, if available. Monthly.
- **Engagement:** page views per section (Learn, Tools, Strategies, Resources, FAQ; since v1.1.0 Individual Stocks, Indices & ETFs, VIX Strategy, Leveraged Strategies and Resources). Target: baseline after launch. Host aggregate statistics, if available. Monthly.
- **Retention:** not measured. Counting returning visitors needs a way to recognize them, which the no-tracking assumption rules out.
- **Performance:**

| Metric | Target | Measurement method | Cadence |
|---|---|---|---|
| Inventory coverage | 100% on every moved page | The core rule's check: list before, check after | Each page move |
| Console errors | 0 on every page, in both themes | Headless Edge run of each page from the local server | Before each major update is finished |
| Broken internal links | 0 | Link check in the same run | Before each major update is finished |
| LCP, CLS, TBT | LCP 2.5 s or less, CLS 0.1 or less, TBT 200 ms or less, mobile | Lighthouse against the local server in Edge: by hand in DevTools, or `npx lighthouse` with `CHROME_PATH` set to Edge (Runbook; used for P7 on 2026-10-02) | Before each major update is finished |
| Data freshness | VIX: the vix pipeline's latest value; stocks: the stocks pipeline's latest data | Compare the timestamp a page shows with the newest data commit in the source repo | Before each major update is finished; weekly after launch |
| Uptime | Set once a host is chosen (now Cloudflare Pages and GitHub Pages; target not set) | The host's status page or an external monitor, to be chosen | After launch |

## Invests: Runbook

Rewritten 2026-10-02 (P8.3) from what was actually run. Deploy and Rollback are written for P10 and haven't been run (D20). **Audit 2026-10-02:** Deploy has been run for every push since launch; Rollback hasn't been needed.

### Prerequisites

- A current web browser. Testing uses Microsoft Edge (see Browser Testing).
- Python 3, for the scripts and the local web server. The maintenance machine has Python 3.14.3; any Python 3 with the standard `http.server` module serves the site.
- For the scripts: BeautifulSoup 4 (`pip install beautifulsoup4`) for scripts/site.py, scripts/inventory.py and scripts/check.py, and Playwright (`pip install playwright`) for scripts/browser.py. Playwright drives the installed Edge, so no browser download is needed.
- Read access to the private `Azqato/templateinterface` repo, to copy the template files: for example the GitHub CLI (`gh`) logged in as Azqato. Version 2.101.0 was used on 2026-10-01.
- Git. The folder lives in the azqato.github.io repository since 2026-10-02 (Repository Hygiene).
- No package manager or runtime for the site itself. Node.js is optional and only used to run Lighthouse from the command line (`npx lighthouse`; Node 24.19.0 on the maintenance machine).

### Local setup

1. Get the folder: clone github.com/Azqato/azqato.github.io; the site is its `invests/` folder.
2. From `invests/`, run `python -m http.server 8000` (the browser test serves it this way), or from the repository root to test under the real base path.
3. Open http://localhost:8000/ (or http://localhost:8000/invests/) in Edge. Port 8000 is `http.server`'s default. Stop the server with Ctrl+C in its window.

Opening a page straight from disk (file://) may work for static pages, but expect the data tools to fail there, since browsers restrict fetch() on file:// pages (not tested in this project).

### Build

The served site has no build step: the committed files are the site. The pages are generated, though, and committed (Repository Hygiene). After changing scripts/site.py, assets/css/site.css or the sources, from `invests/`:

1. `python scripts/snapshot.py`: fresh read-only copies of the source pages and Template Interface's files in `_sources/` (needs `gh` logged in as Azqato for the private template repo).
2. `python scripts/inventory.py`: the core rule's inventories, from the snapshots.
3. `python scripts/site.py`: every page, the scoped source CSS, the copied scripts, the search index, sitemap.xml, inventory/map.json and inventory/em-dashes.md. It prints the page count, search entries and em dashes replaced.
4. `python scripts/check.py`: titles, links, demo text, dashes and inventories. Expect "21 page(s) checked, 0 failure(s)".
5. `python scripts/browser.py`: the browser tests in headless Edge. Expect "0 failure(s)" and the known notes about feeds that are deliberately blocked in the test.

Steps 1 and 2 are only needed when a source changed. On Windows, set `PYTHONIOENCODING=utf-8` if a script fails printing an emoji.

### Deploy

Rewritten 2026-10-02 after the merge into the azqato.github.io repository (D21). Only on the author's go-ahead (D20).

1. Build and test in `invests/` (Build, steps 1 to 5).
2. From the repository root: commit, staging files by name; the pre-commit hook checks for em dashes (it skips `invests/inventory/`).
3. Push `main`. Cloudflare Pages rebuilds azqato.com and GitHub Pages rebuilds azqato.github.io.
4. Post-deploy check (a comparison, not a test): fetch each file under https://azqato.com/invests/ and compare it with the local copy; check /invests and /invests.html land on /invests/ in one hop; open Home, the Screener and the VIX Dashboard live in both themes.
5. Then the D7 redirects in the old repos (Deprecation and Removal).

### Rollback

Locally: `git revert <commit>`. Once pushed: revert the commit in the azqato.github.io repository and push; both hosts republish the previous state within minutes. A bad redirect: revert that commit in the repo that holds it. Caches may serve the old file for a few minutes.

### Environment configs

Two: local (`python -m http.server` from `invests/` or the repository root) and production, which is two hosts building the same `main`: Cloudflare Pages at https://azqato.com/invests/ (canonical) and GitHub Pages at https://azqato.github.io/invests/. The differences that matter are listed under Verification Environment; the base path is the main one, and every link and fetch here is relative or absolute https, so both work.

### Environment variable reference

None. The site needs no environment variables, keys or secrets. The source repos' workflows have their own settings, documented in those repos.

### Common errors

| Error | Likely cause | Fix |
|---|---|---|
| The VIX reading never loads, and the console reports a MIME type or `nosniff` refusal | vix.js was loaded from raw.githubusercontent.com, which serves it as plain text with `nosniff` | Load it from https://azqato.github.io/vix/data/vix.js (D6) |
| A moved VIX or stocks page loads no data | The page still uses the source site's relative `data/` path | Point it at the feed addresses under Technical Requirements |
| Data doesn't load when a page is opened from disk | file:// pages can't fetch local files (expected, not tested) | Use the local server |
| `msedge.exe` isn't found under `C:\Program Files\Microsoft\Edge\` | On the maintenance machine Edge is under Program Files (x86) | Use the path under Browser Testing |
| Headless Edge prints nothing in Git Bash | Edge doesn't write `--dump-dom` output to a Git Bash pipe | Use PowerShell's `Start-Process` with `-RedirectStandardOutput` (Browser Testing) |
| `gh api` returns 404 for `Azqato/templateinterface` | The repo is private and the CLI isn't logged in as an account with access | `gh auth login` as Azqato |
| `import site` loads the wrong module | `site` is also a Python standard library module | Load scripts/site.py by path, as browser.py does (`importlib.util.spec_from_file_location`) |
| A script fails with `UnicodeEncodeError` printing an emoji | The Windows console's code page | Set `PYTHONIOENCODING=utf-8` |
| A page edit disappears after `python scripts/site.py` | The pages are generated | Make the change in scripts/site.py or assets/css/site.css, not in the page |
| `npx lighthouse` can't find a browser | It looks for Chrome | Set `CHROME_PATH` to the Edge path (Browser Testing) |

### Monitoring

No uptime alerts are set up. Each push to the azqato.github.io repository deploys twice: Cloudflare Pages lists each build in its dashboard, and GitHub Pages shows each under the repository's Actions tab ("pages build and deployment"); a failed deploy shows there and the previous version stays up. The post-deploy comparison in Deploy step 4 is the check that a change arrived. The data comes from the stocks and vix repos' GitHub Actions; their runs and failures show in each repo's Actions tab. stocks has a workflow called alert-on-failure.yml, whose trigger and target weren't read in this audit.

## Invests: Technical Requirements

### System architecture

A static, multi-page website with no server code and no database. Each page is its own HTML file (Design details in DESIGN.md). Everything dynamic is fetched by the visitor's browser when a page loads:

```
Visitor's browser
├── pages, CSS and JavaScript   from azqato.com/invests/ (Cloudflare Pages) or azqato.github.io/invests/ (GitHub Pages), D21
├── stock data (JSON)           from raw.githubusercontent.com/Azqato/stocks/main/data/,
│                               falling back to azqato.github.io/stocks/data/
│                               written by the stocks repo's GitHub Actions
├── VIX reading (vix.js)        from azqato.github.io/vix/data/vix.js
│   │                           written by the vix repo's GitHub Actions
│   └── fallback                Yahoo Finance chart data for ^VIX, relayed by api.allorigins.win
└── Chart.js 4.4.0              from cdn.jsdelivr.net (VIX Dashboard and Custom builder)
```

Pages move from the source sites with their scripts (core rule); the changes are the presentation, the addresses and the data URLs. Checked 2026-10-02 (P8): this is what the built pages request. Chart.js now carries a Subresource Integrity hash (Question 12).

**How the pages are made (2026-10-02).** scripts/site.py reads the snapshots in `_sources/` and writes every page: the shell (top bar, sidebar, breadcrumbs, pager, footer, search dialog) around the source page's body content, moved whole with its own classes, ids and scripts. The source's own navigation is replaced by the shell. Each source stylesheet is copied with every rule scoped to that source (`.src-stocks`, `.src-vix`, `.src-leverage`, `.src-invests`), leaving out the rules for the old navigation and the bare element rules, so plain text takes the template's styles and the source's components keep theirs. Until the author's review after the MVP (P7), the pages are generated: change scripts/site.py and run it again rather than editing a page. The served site still has no build step; the generated files are committed.

### Tech stack

From the plan and the source sites; in the repository since 2026-10-02 (P2).

| Part | What | Version or source |
|---|---|---|
| Markup, style, behavior | HTML, CSS (custom properties, `:has()`), plain JavaScript | No framework |
| Design system | Template Interface: the shared theme.css, base.css and components.css, plus the documentation-site and wiki-portal templates | Private repo `Azqato/templateinterface`, read at commit 61acfcb (2026-10-01); files copied at commit ed840da (2026-10-02) |
| Charts | Chart.js | 4.4.0, from jsDelivr, as the vix pages load it |
| Fonts | System font stacks only (Segoe UI first); no web fonts | From the templates |
| Local server | Python `http.server` | Python 3 |
| Page builder | scripts/site.py: moves each source page's content into the shell | Python 3 with BeautifulSoup 4 (bs4) |
| Tests | scripts/check.py (no browser) and scripts/browser.py (Playwright driving Edge) | Python 3; Playwright from pip |
| Speed checks | Lighthouse, only for P7-style checks, not needed by the site | 13.5.0 through `npx` (Node 24.19.0) |
| Data pipelines | Python scripts and GitHub Actions | In the stocks and vix repos, not here (D6) |

There's no package manager, so there's no manifest or lockfile.

### Folder structure

Current, updated 2026-10-02 for the restructure (v1.1.0); earlier, checked after P9 (the scripts moved from `tools/` to `scripts/` on 2026-10-02, because the Tools section's pages live in `tools/`):

```
invests/
├── index.html                     Home
├── stocks/                        index.html (Individual Stocks), philosophy, metrics, screener
├── indices/                       index.html (Indices & ETFs), market
├── vix/                           index.html (VIX Strategy), dashboard, custom
├── leveraged/                     index.html (Leveraged Strategies), 3sig, 6sig, 9sig, tqqq-ftlt, holy-grail, hfea
├── resources/                     index.html (Curated resources), finviz, seekingalpha, faq
├── assets/
│   ├── css/                       theme, base, components (Template Interface), docs (documentation-site),
│   │                              site (this site's own), src-stocks, src-vix, src-leverage (scoped source CSS)
│   └── js/                        theme.js, site.js, search-index.js, stocks/ and vix/ (the sources' scripts)
├── sitemap.xml                    the 21 published addresses, generated by scripts/site.py (P9.3)
├── README.md                      the public front door
├── LICENSE.md                     terms of use: all rights reserved, not financial advice
├── .gitattributes                 pins LF line endings
├── .gitignore                     excludes _sources/ and Python's __pycache__/
├── docs/                          PRD.md, DESIGN.md, PATCHNOTES.md, TODO.md, UI-REVIEW.md (the 2026-10-02 UI review and its decisions)
├── scripts/
│   ├── snapshot.py                downloads read-only copies of the source pages into _sources/
│   ├── inventory.py               builds the core rule's page inventories from _sources/
│   ├── site.py                    builds every page, the scoped CSS, the copied scripts and the search index
│   ├── check.py                   read-only site checks: titles, links, demo text, dashes, inventories
│   └── browser.py                 browser tests in headless Edge: errors, both themes, phone width, contrast, shell, feeds
├── inventory/                     one inventory per source page, map.json (page to inventory), em-dashes.md
└── _sources/                      not committed: the snapshots, Template Interface's files and COMMITS.txt
```

Planned, with the section-folder layout the author chose on 2026-10-01 (Development plan, P0.3): one HTML file for each of the 21 pages; Template Interface's CSS plus this site's own CSS and JavaScript; no data folder, since the data stays in the source repos (D6). robots.txt and sitemap.xml come at the root once the site has pages and an address. If the site ends up in a subfolder of a larger domain, as the stocks, vix and leverage sites are under azqato.github.io, that domain's robots.txt governs it and may not be this project's to write. **Built as planned (2026-10-02):** sitemap.xml is at the root; robots.txt isn't, because the site is a subfolder of azqato.github.io (P9.3).

### Data models

The data belongs to the stocks and vix repos, whose own docs describe it (stocks: docs/PRD.md in github.com/Azqato/stocks). What the pages here depend on:

| Data | Where | Shape |
|---|---|---|
| VIX reading | azqato.github.io/vix/data/vix.js | A script that sets `window.__VIX_DATA__ = {value, timestamp, fetchedAt}` (field names read during planning; types not recorded) |
| Stock and ETF data, Market Overview feed, statements, index constituents | raw.githubusercontent.com/Azqato/stocks/main/data/ (`RAW_BASE` in the stocks pages), falling back to azqato.github.io/stocks/data/ on this site (since 2026-10-02) | JSON files; schemas documented in the stocks repo, not read in this audit |
| Theme choice | The visitor's localStorage, key `azqato-invests-theme` | `light` or `dark`; absent until the visitor presses the theme button (assets/js/theme.js) |
| Market Overview cache | The visitor's localStorage | The last feed, stored as JSON under the stocks page's `CACHE_KEY` |
| Screener cache | The visitor's localStorage | Each universe's last feed, as JSON with a `stocks` list (screener.js) |
| Last VIX reading | The visitor's localStorage, key `vix_last_known` | Written by vix.js |

### API design (internal data flow)

There's no API; the site only reads files. This is how the source sites do it today (read 2026-10-01), which the move keeps:

1. **VIX pages.** `data/vix.js` sets `window.__VIX_DATA__` synchronously, before the page script runs. The pages paint the last-known value from localStorage first, before any network call. vix.js treats `window.__VIX_DATA__` as the primary source; only if it's unavailable does it fetch Yahoo Finance's chart data for ^VIX through api.allorigins.win, with a query1 and a query2 address listed in that order. vix.js writes readings to `vix_last_known`. On this site, `data/vix.js` becomes the absolute azqato.github.io address (D6).
2. **Market Overview.** Reads and writes a cached copy of its feed in localStorage, and fetches the feed from `RAW_BASE`.
3. **Screener.** Fetches its data from `RAW_BASE`, with a local copy as fallback (see Background findings for what happens to that fallback here).
4. **Error states.** When a feed can't be reached, the pages fall back as above. What each page shows when everything fails wasn't read; inventory it at the move.

### State management

No application state lives anywhere but the open page and the visitor's browser storage: the theme choice and the data caches above. No cookies: none of the scanned stocks and vix pages uses `document.cookie`, and the plan adds none. The site sends no visitor data anywhere beyond the ordinary requests a browser makes for files (see Security).

### Third-party integrations

| Service | Used for | Authentication |
|---|---|---|
| raw.githubusercontent.com (GitHub) | Stock data JSON | None (public repo) |
| azqato.github.io (GitHub Pages) | vix.js with the VIX reading; later, the D7 redirects | None |
| api.allorigins.win | Relays the VIX fallback request and adds CORS headers | None |
| query1 and query2.finance.yahoo.com, through allorigins | VIX fallback data | None |
| cdn.jsdelivr.net | Chart.js 4.4.0 | None |
| composeratlas.com | Links from Composer strategy write-ups (D15, D16, D17) | None; links only |
| Discord, brokers and the curated resources | Outbound links, some of them referral links (D13, D14) | None; links only |
| GitHub Actions, in stocks and vix | Produce the data | The source repos' own settings |

### Performance requirements

Set by the 2026-10-01 audit; no rule existed. Targets for a mobile Lighthouse run: an LCP of 2.5 s or less, a CLS of 0.1 or less and a TBT of 200 ms or less. No page-weight budget yet, because the screener's data size wasn't measured. For scale, the base template's own files are small: the three shared stylesheets total about 13 KB, documentation-site's styles.css is about 27 KB and its script.js about 25 KB (sizes from GitHub, 2026-10-01).

### Known technical debt

None in this repo yet. Planned compromises, each with what the correct solution would be. **Audit 2026-10-02:** the azqato.com nav copy exists (`AZQATO_NAV` in scripts/site.py) and is the live drift risk; the Chart.js hash and the stocks fallback are done (P6); the rest stand.

- **A copy of azqato.com's nav, if D9 stays.** It can drift from what tools/build-nav.py stamps onto azqato.com. Correct: generate it from the same page list, or drop D9.
- **The VIX reading depends on another site.** If azqato.github.io/vix stops serving data/vix.js, the reading falls back to a third-party relay. Correct: a feed this site can load directly, such as JSON with CORS headers published by the vix repo. That's a change to the vix repo, so it's the author's call.
- **A third-party CORS relay (api.allorigins.win) for the VIX fallback.** It can disappear or return anything. Correct: nothing cheap; keep it as the fallback it is and treat its data as untrusted.
- **Chart.js from a CDN without an integrity hash.** Correct: add a Subresource Integrity hash for 4.4.0, or serve a copy from this site (Question 12).
- **The stocks local fallback.** It may point at a folder this site doesn't have (Background findings). Correct: point it at a copy the stocks repo serves.
- **Out-of-date content moved as it is (D19).** Correct: the planned correction pass (M11).

## Invests: Conventions

Read from the code and the git history on 2026-10-02 (P8.3).

**Code:**

- Pages are generated by scripts/site.py; never edit a page by hand. Hand-written styling goes in assets/css/site.css, grouped under `/* ---------- Name ---------- */` headings with a comment saying why; behavior in assets/js/site.js.
- Every change to moved source code is marked at the change with `Azqato Invests:` in a comment, so the original behavior can be told from this site's.
- Source CSS is scoped by source (`.src-stocks`, `.src-vix`, `.src-leverage`, `.src-invests`); overrides use `.pp-page .src-x ...` so they win without `!important`.
- Template tokens (`--pp-*` and theme.css) are never redefined; this site's own tokens get their own names (DESIGN.md).
- Python: 4-space indents, standard library plus bs4, one script per job in scripts/, each runnable from the repository root with no arguments. CSS: 2-space indents, one property per line. JavaScript: plain ES5-compatible functions in site.js and theme.js; the sources' scripts keep their own style.
- Text files are UTF-8 with LF line endings (`.gitattributes`). No em dashes anywhere (Writing Style).
- Links and fetches are relative inside the site and absolute https outside it, never root-relative, because the site lives under /invests/.

**Git:**

- One branch, `main`; no remote yet (D20). (Since 2026-10-02: the azqato.github.io repository's `main`, pushed to GitHub on the author's word. Commit there as Azqato, staging files by name; its pre-commit hook blocks em dashes and skips `invests/inventory/`.)
- Commit messages: a short plain summary in sentence case, no prefix or ticket number (for example "VIX Custom: categories above the allocation, tighter heading"), with a body when the change needs explaining, and a `Co-Authored-By` trailer when an AI model helped.
- The generated pages are committed with the change that generated them.

**Docs** (from the plan, still true):

- Decisions are numbered D1, D2 and so on in one table. A changed decision keeps its number, is marked **Changed** with the date, and keeps its old text after "Before:" (D4, D5).
- Dates are written YYYY-MM-DD.
- The plan addresses the author as "you".
- The plan's headings are in sentence case. The PRD's required sections keep the names the documentation prompt gives them.
- No em dashes (see Writing Style).
- PATCHNOTES.md uses semantic versioning. Until the site launches, versions stay below 1.0.0: a minor version for a change to the plan, docs or site, and a patch version for a small fix (set by the 2026-10-01 audit). The site launched as v1.0.0 on 2026-10-02; the same minor and patch rule continues. Each invests change is also summarized in the main repository's docs/PATCHNOTES.md.

## Invests: Writing Style

No rule existed, so the default was adopted on 2026-10-01. It covers the docs, the site's own interface text and code comments.

- Em dashes are prohibited in all three forms: the literal character (Unicode U+2014), the `&mdash;` HTML entity, and a double hyphen used as punctuation. Search for the character and the entity separately, because a search for one doesn't find the other. CSS custom properties (such as `--pp-bg`) and command-line flags are syntax, not punctuation, and are never touched.
- Replace each instance with whichever fits: a comma (most often), a colon (before a list or an elaboration after a complete clause), a semicolon (between two closely related independent clauses), parentheses (for asides), a period (to split the sentence), or a single hyphen.
- The single hyphen is allowed, and encouraged where it fits. It's preferred in document titles, section headings and version lines (for example "## v1.2.0 - 2026-01-01"), where a comma or colon reads awkwardly. In running prose the other replacements usually read better.
- Leave any instance the text needs in order to mean anything, such as a rule naming the character it prohibits.
- Tone: direct and functional, plain declarative sentences, no marketing language, no filler openings.
- Text moved from the sources comes over as it is (core rule), with one exception the author approved on 2026-10-01 (Question 14): em dashes in moved text are replaced under this rule, the wording otherwise unchanged, and every replacement is listed in PATCHNOTES.md. scripts/check.py fails on any em dash in page text.
- Record each sweep in PATCHNOTES.md: how many instances were found, and where. The 2026-10-01 sweep found none.

## Invests: Browser Testing

No rule existed, so the default was adopted on 2026-10-01.

- Use Microsoft Edge, never Chrome, for every automated or end-to-end test, including any ad hoc headless run from a script or a shell command. Chrome is the owner's day-to-day browser, and driving it would disturb a live session; Edge runs the same engine and is free to use. This project uses no JavaScript runtime, so tests drive a headless browser directly.
- Edge on the maintenance machine, verified 2026-10-01: `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`. It isn't under `C:\Program Files`.
- Example, not yet run in this project: `"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --disable-gpu --dump-dom http://localhost:8000/` prints the page after its scripts have run, which is how a title set at runtime is checked.
- On Windows, Edge doesn't write `--dump-dom` output to a Git Bash pipe; run it with PowerShell's `Start-Process` and `-RedirectStandardOutput <file> -Wait`, then read the file. Verified 2026-10-01 (P0): this read a title set by script correctly.
- `python scripts/browser.py [--shots DIR]` runs the site's browser tests in headless Edge through Playwright (`pip install playwright`; it drives the installed Edge with `channel="msedge"`, so no browser download). It serves the folder itself on a free port and stops it when done. Added 2026-10-02.
- No second engine is required, and Firefox and Safari aren't driven. The `:has()` support noted under Assumptions is the main cross-browser risk; check it by hand before launch.

## Invests: Verification Environment

No rule existed, so the default was adopted on 2026-10-01, alongside D20.

- Verify locally, never against production, unless a request explicitly asks for a production check. Run the change from the local server (Runbook). Production is where a change is confirmed to have arrived, not where it's tested.
- Testing against production means the change has already shipped, so the test only shows what visitors already see. It also puts load or test data on a live system, and turns a failure into a rollback instead of a fix made before pushing.
- Verifying functionality is local. Confirming a deploy landed is a separate step after a push: fetch the deployed files and check they match what was verified locally. That's a comparison, not a test, and it isn't an exception to this rule.
- For now D20 goes further: nothing is pushed, published or deployed at all until the author says so. (Since launch: each push needs the author's word.)
- Known differences between local and production, each of which can hide a bug until the site is deployed:
  - **Base path.** If the site is served from a subfolder, as the stocks, vix and leverage sites are under azqato.github.io, links and fetches that start with `/` reach the domain root in production but the repository root locally. Use relative links.
  - **Extensionless addresses.** azqato.com, a Cloudflare Pages build, answers /page.html with a 307 redirect to /page; Python's `http.server` doesn't. If this site's host does the same, check links and redirects against the host's behavior. (It does: the canonical addresses drop `.html`, and the post-deploy comparison fetches the clean form.)
  - **Pages opened from disk.** A page opened from file:// behaves differently from both the local server and production (Runbook).
  - **Caching.** The host and GitHub may cache vix.js and the data files, while local tests see fresh files. A stale reading in production may be caching rather than a bug (cache lifetimes not measured).
- Never point a destructive or state-changing check at production: no writes, deletes, test records, or anything that sends mail or a webhook. If something can only be exercised against a live system, stop and ask.

## Invests: Testing Cadence

No earlier testing rule existed, so nothing was replaced. The default was adopted on 2026-10-01.

- Browser tests use headless Microsoft Edge, as Browser Testing says.
- A major update ships when it's pushed or deployed. While nothing is pushed or deployed (D20), it ships when the major update is finished. "Before shipping" below means that moment.
- Right before a major update ships, run two checks, once each:
  1. Assumption check: list the assumptions the finished change relies on, each marked verified (the code that shows it was read) or guessed (inferred, and from what). Check every guess that's cheap to check, fix anything found wrong, and show the author what's still guessed.
  2. Browser test, once. Don't test between edits.
- If a large change depends on something not yet read, check that one thing before building on it.
- A major update changes behavior, layout, scripts, styles, routing, the build or dependencies. A minor update changes only wording, documentation, comments, patch notes, or data the project's own check script validates. Minor updates ship without a browser test or an assumption check.
- Cheap checks that don't open a browser (a linter, a project check script) may still run after minor edits.
- Batch the work: make every edit first, then test once at the end.
- When a test fails, fix it and rerun only the failing check, then run the full test once before shipping.
- A test the author asks for always runs, whatever this rule says.
- Confirming a deploy arrived, by comparing the deployed files with the local copies, isn't a test. It's cheap and still happens after every push.
- Where a session has standing permission to push, every change reaches production, so decide by whether the change is major, not by whether it's being pushed.
- Every summary says what wasn't browser-tested. An untested change is never presented as tested.
- For a page move, the core rule's inventory check is part of the browser test: every item on the page's list is checked on the new page.

## Invests: Security

- **Authentication model:** none. There are no accounts or sign-in (Assumptions).
- **Authorization model:** none. Every page is public once published; until then, nothing is reachable from outside (D20). Since 2026-10-02 everything in `invests/` is public, including docs/, scripts/ and inventory/ (P14).
- **Data storage:** only in the visitor's browser: the theme choice (`azqato-invests-theme`), the cached Market Overview and screener feeds and the last VIX reading (`vix_last_known`). None of it is personal data, nothing leaves the browser, and there are no cookies.
- **Environment variables and secrets:** the site needs none, and none are in this repo (checked 2026-10-01, and again by pattern search on 2026-10-02, P7.8). The source repos' workflows keep their own settings.
- **Third-party trust:** loading a page makes the visitor's browser contact raw.githubusercontent.com and azqato.github.io, and on the VIX pages cdn.jsdelivr.net. If the VIX fallback runs, it also contacts api.allorigins.win, which relays the request to Yahoo Finance. Each receives what any web request carries: the visitor's IP address, browser user agent and possibly the referring page. Nothing else is sent. Clicking an outbound link (Composer Atlas, Discord, brokers and the other resources) takes the visitor to that site.
- **Known attack surface:**
  - Chart.js from jsDelivr without an integrity hash: a tampered CDN file would run on the VIX pages. Mitigation today: the version is pinned in the URL (4.4.0). Planned: add an integrity hash or serve a copy from this site (Known technical debt). **Done (P6):** both VIX tools load it with a sha384 integrity hash and `crossorigin="anonymous"`.
  - Data from the feeds and the allorigins relay: if a page inserts fetched text as HTML, a tampered response could inject script. Checked 2026-10-01 (P1): the screener (12 uses in screener.js) and Market Overview (1 use) build rows and cards with `innerHTML` from feed values such as tickers and category names, without escaping; the VIX scripts don't use `innerHTML`. The feeds are the author's own pipeline, so the risk is low; escape feed values when these tools move (P6), and prefer `textContent` and number parsing over `innerHTML`. **Fixed 2026-10-02 (P7.8):** scripts/site.py wraps every stock feed's `res.json()` in `azqClean()`, which strips `<` and `>` from each text value before the page uses it, so feed text can't add markup. The VIX tools insert only numbers and their own labels.
  - Links that open in a new tab should carry `rel="noopener"`. Current browsers imply it, but being explicit costs nothing. Checked 2026-10-02 (P7.8): every one does.
  - Template Interface is a private repo. Copying its files here publishes them if this repo is ever made public (Question 5). The repository will be public long term (2026-10-02), so this needs the author's answer before it is (Question 16). (Answered: publish them; they are public in the azqato.github.io repository.)
- **Dependency policy:** no package manager. The one third-party library, Chart.js, is pinned to an exact version in its URL. Default set by the 2026-10-01 audit: pin exact versions, add integrity hashes, review third-party files at each major update, and check the Chart.js version against its security advisories when the VIX pages move.

## Invests: Repository Hygiene

No rule existed, so the default below was adopted on 2026-10-01. This is a policy record: the audit created no ignore or attributes file and ran no version control command.

**Current state (2026-10-01, P0):** a local git repository with default branch `main` and no remote (D20). `.gitattributes` pins LF (`* text=auto eol=lf`, with images marked binary); `.gitignore` excludes `_sources/`, the read-only source snapshots that scripts/snapshot.py regenerates. Before P0 the folder wasn't a repository. The only copy is the working folder on the maintenance machine, inside OneDrive. The repository's name, where it lives on GitHub and whether it's public are open (Question 5). **Update 2026-10-02:** github.com/Azqato/invests exists (private, to be public later); the local repository isn't connected to it. `.gitignore` gained `__pycache__/`, which Python writes when one script imports another (scripts/browser.py loads scripts/site.py). **Update 2026-10-02 (after the merge, D21):** the `invests/` folder in the azqato.github.io repository is the single source of truth for everything here, decided by the author. The separate local repository (`../invests`) is retired and will be deleted; nothing is edited there, and its history isn't carried over. `invests/.gitignore` and `invests/.gitattributes` came with the files and still apply inside the folder.

**Default:**

- The repository carries an ignore file and a `.gitattributes`, commits its lockfile, keeps every secret out of history, and names its default branch `main`.
- Secrets are never committed; it's the one mistake whose cost can't be recovered. Keep them out with the ignore rule `.env*` followed by `!.env.example`, so a file listing key names can travel with the repository while the file holding values never does. The site needs no environment variables, so there's nothing to ignore yet; add the rule if one ever appears. An ignore file is prevention, not protection. A secret found committed is reported by file name with a recommendation to rotate it; history isn't rewritten, which wouldn't undo the exposure anyway.
- An ignore file exists wherever the project generates something: build output, dependency folders, caches, logs, coverage reports, and editor or operating system files. This project generates nothing (no build, no dependencies), so it needs none yet and won't carry an empty one.
- Lockfiles are committed, never ignored. This project has none, because it has no package manager.
- Every ignore entry names something this project actually produces. An entry that can't be explained is reported, not removed.
- Ignoring a file doesn't untrack it, so compare the tracked list against the rules rather than reading the rules alone.
- Generated files committed on purpose are recorded here with what regenerates them and what keeps them in step. None exist. If D9 stays, the copied azqato.com nav will be the first: record its source here.
  **Since 2026-10-02 (P2):** scripts/site.py generates and commits every page, assets/css/src-*.css, assets/js/stocks/ and assets/js/vix/ (the sources' scripts, with the data addresses changed), assets/js/search-index.js, inventory/map.json and inventory/em-dashes.md, from the snapshots in `_sources/`. Run it again after a snapshot refresh. Copied files: assets/css/theme.css, base.css and components.css, and docs.css (documentation-site's styles.css), from Template Interface at ed840da, recopied by the same script; azqato.com's nav, copied by hand into scripts/site.py (`AZQATO_NAV`) from azqato.github.io's invests.html at commit 58767b5. theme.js and site.js are adapted from Template Interface's scripts and edited by hand.
- Pin line endings. When the repository is created, add a `.gitattributes` with `* text=auto eol=lf`: the work happens on Windows, the site will be served from elsewhere, and the post-deploy check compares files byte for byte, so unpinned line endings would show differences that aren't there. Mark binary formats as binary when any arrive. Nothing here needs CRLF. The docs already use LF.
- Large binaries stay out of history. None exist.

**Compliance checks.** These read and report; they never run a command that changes state.

- An ignore file exists, or this section says why the project needs none. Today: none needed. **Since P0:** `.gitignore` exists, for `_sources/` and (2026-10-02) `__pycache__/`.
- No tracked file matches a pattern the ignore file excludes. Today: not applicable.
- No dependency folder, build output or cache is tracked.
- No tracked file holds credentials by convention: an environment file other than the example, a private key, a certificate, or a package manager configuration carrying a token.
- The lockfile is tracked, where the ecosystem has one. Today: not applicable.
- A `.gitattributes` exists and pins line endings, with an explicit rule for any format that must keep CRLF. Today: fails until the repository is created (Documentation Versus Reality, entry 5). **Passes since 2026-10-01 (P0).**
- Every ignore entry corresponds to something the project produces.

## Invests: Licensing

The project had no licence. The default posture was adopted on 2026-10-01 and written into [LICENSE.md](../LICENSE.md) at the repository root, never inside docs/, where licence detection may miss it.

- **Posture:** all rights reserved; source-available, not open source. LICENSE.md grants nothing, and a readable repository isn't a grant. A permission given to everyone can't easily be withdrawn from one person, and the aim is to keep the ability to act against a specific bad actor.
- **The one carve-out, AI and search referencing:** search engines, AI assistants, answer engines and other automated systems may crawl, index, store for retrieval, quote, summarize, link to and cite the work. Attribution is requested, not required, and no permission is needed. Referencing is granted. Substitution, meaning reproducing the work as a replacement for visiting it, is not. Use as training data isn't granted by default and goes through the permission route, where it's not usually refused.
- **No waiver:** not acting against a use isn't a licence, a precedent or a waiver; delay doesn't waive; any waiver must be written, signed and limited to the use it names.
- **Asymmetry:** widening a grant later takes one sentence; narrowing a granted right doesn't. When in doubt, grant less and point to the request route.
- **No licence without its text:** a bare licence name with no licence file behind it is an ambiguity, not a grant.
- **What LICENSE.md doesn't claim:** it doesn't override platform terms (a host's own view and fork rights operate independently and aren't enlarged); it doesn't claim third-party data (market prices, index readings, statements, constituent lists, Chart.js, linked sites); and it doesn't restrict fair use or fair dealing.
- **Domain disclaimer:** NOT FINANCIAL ADVICE, including that leveraged strategies can lose money quickly, that backtests and past results don't predict future returns, and that some links are referral links.
- **Permission requests** go to this repository's public issue tracker on GitHub. The repository isn't published, so there's no tracker yet; LICENSE.md says so, and the address gets added once it exists (Question 7). **Audit 2026-10-02:** LICENSE.md pointed at github.com/Azqato/invests/issues, which no longer exists; it now points at https://github.com/Azqato/azqato.github.io/issues, the repository the site lives in, which the main site's own LICENSE.md also uses.
- **Machine-readable layer:** when the site gets a robots.txt of its own, it stays fully open (`User-agent: *` and `Allow: /`) with a comment saying that's deliberate, and LICENSE.md is authoritative if the two ever disagree. LICENSE.md already says so.

## Invests: Social Sharing Tags

No rule existed for this site, so the default was adopted on 2026-10-01. There are no pages yet, so nothing has been checked; this is the rule pages are built to. (Pages exist since 2026-10-02; see the checks below.) It's a policy record: changing a page's head is a separate change.

- Every shareable page carries six tags: og:title, og:description, og:url, og:type, og:site_name and twitter:card. og:title, og:description and og:url are written per page. og:type is "website" on every page. og:site_name is the same everywhere: "Azqato Invests" by default, 14 characters (Question 6).
- og:url is the page's own absolute https address, never a relative path and never the site root. The domain comes from what the project has once D4 is decided (the sitemap, a CNAME file, robots.txt or the deploy config), used exactly as written and never guessed. Until then, no page can have a correct og:url.
- Budgets, as safe caps: og:title 60 characters (70 at most), og:description 150 (200 at most), og:site_name 20. Emoji and markdown characters count as characters.
- og:title doesn't repeat the site name, because the card already shows og:site_name directly above the title.
- No images by default: no og:image, og:image:width, og:image:height or og:image:alt, and twitter:card is "summary". An image is never added speculatively or pointed at a placeholder. If an image policy is adopted later: 1200 by 630 pixels, an absolute https URL, explicit width and height tags, PNG or JPG under about 8 MB, alt text under 100 characters, and only then "summary_large_image".
- The title front-loads what's distinct about the page: no trailing branding, and no colon stacking a subtitle onto a subtitle.
- The description is complete sentences saying what the page actually gives someone who has never seen the site, ending on a full stop, and not a restatement of the title. It's written from the page's own content. Where a page's meta description is accurate, og:description reuses it rather than competing with it; where the two differ, say why.
- Excluded from sharing tags: error pages such as a 404, mockups, scratch or work-in-progress files, and anything left out of the sitemap or marked noindex. None exist yet; list them here as they appear.
- **Compliance checks** (read and report; counts by script, not by eye): all six tags on every page that should have them; og:title 70 characters or fewer, og:description 200 or fewer, og:site_name 20 or fewer, with the count reported for anything over the target budgets; every og:url absolute, https and unique across the site; no og:title containing the og:site_name; where og:image exists, its width, height and alt tags exist, its URL is absolute and its file is in the repository; where it doesn't, twitter:card is "summary".

**Checked 2026-10-02 (P7.4, P9.2), by script on all 21 pages:** all six tags present on every page; og:url absolute, https and unique (https://azqato.github.io/invests/ plus the page's path, with folder pages ending in `/`; since v0.18.0 https://azqato.com/invests/ plus the page's path without `.html`), matching the canonical link; og:site_name "Azqato Invests" (14 characters); no og:image, so twitter:card is "summary" everywhere. Nothing is excluded: there's no 404 page or draft page.

**Starting point from the source**, read 2026-10-01 and counted by script. invests.html, which becomes Home and Resources, carries: og:title "Free Investing Tools and a Curated Resource Hub" (47 characters, within budget, no site name); og:description identical to its meta description, "Free investing tools built by Azqato, plus a hand-picked hub of brokers, screeners, ETF lists, charts and economic data. Nothing here is financial advice." (154 characters: over the 150 target, under the 200 maximum); og:type "website"; og:site_name "Azqato"; twitter:card "summary"; og:url and canonical `https://azqato.com/invests`. Those values were written for azqato.com, under azqato.github.io's rules. Home's tags get written when Home is built, with these as the starting point.

## Invests: Page Titles

No rule existed for this site, so the default was adopted on 2026-10-01. There are no pages yet; this is a policy record, and changing a title is a separate change. (Pages exist since 2026-10-02; check.py checks every title. Since v1.1.0 the landing pages are titled by their group, for example "Individual Stocks - Azqato Invests"; the old "Learn - Azqato Invests" is gone.)

- The shape is "<page name> - Azqato Invests". The first 30 characters must identify the page on their own, and the whole title is 60 characters or fewer, counting the 3-character " - " separator. Truncation removes from the end, so front-loading the page name satisfies both limits.
- The brand goes last, because the favicon already marks the tab. The home page inverts this, and only the home page: there the brand leads. Proposed home title: "Azqato Invests - Investing Tools and Resources" (46 characters), which keeps the wording of invests.html's own title, "Investing Tools and Resources - Azqato".
- Every page's first 30 characters are unique across the site: two titles that differ only after character 30 look the same on a tab.
- One separator, " - ", on every page.
- No placeholder titles ("Untitled", "Document", "Home", "index", template defaults). Search for them explicitly. The template's own title, "Introduction - Parcelpoint Docs", must not survive the build.
- The brand appears once, at the end, and never inside the page name. No keyword stuffing.
- No emoji in titles, since the 💰 favicon already marks the tab, and no all caps in the first 30 characters.
- Every title survives as a bookmark read months later: "Overview" alone is useless, while "Market Overview - Azqato Invests" works.
- Where a title changes at runtime, it must actually change, with any state in front of the name ("(3) ..."), and loading and error states get real titles. The plan has one file per page, so each title is set in its file's head.
- The title and og:title are different fields with different rules. The title ends with the brand; og:title leaves it out. Expect the two to differ on the same page.
- The brand is "Azqato Invests" by default. The source pages follow azqato.github.io's pattern ("Investing Tools and Resources - Azqato"); this site sets its own (D5). Question 6 asks which brand to use.
- **Compliance checks** (read and report; counts by script): a title exists on every page and isn't a placeholder; each is 60 characters or fewer, with the count reported; the first 30 characters are unique, with each collision reported as a pair; the separator matches; the brand suffix is on every page except Home and isn't also inside the page name; any title set at runtime is checked by loading the page and reading the resulting title, not the source.

## Invests: Deprecation and Removal

**The project's own rule, kept as written.** D7: "Every old page under azqato.github.io/stocks/, /vix/ and /leverage/ redirects to its new home. The old repos stay for data and history." The core rule says the same: page addresses change, and "old addresses redirect to the new ones". The redirects mean publishing, so they wait for the author's go-ahead (D20).

**Default for this site's own pages**, adopted 2026-10-01 because no rule existed. Whether a removal needs a redirect depends on whether the thing removed is public facing:

- Public facing: a published page address. Removing or moving one leaves a redirect to whatever replaces it, so the old address keeps resolving.
- Internal: the files that build the site, and anything else not reachable from outside. A source file isn't public facing even when its name appears in an address, because the address is the contract, not the file. Removing one is a plain delete: no redirect, no stub file, no tombstone.

The deploy boundary is the published site: a page is public facing once its address has been published. Nothing in this repo has been published, so today everything here is internal. **Audit 2026-10-02:** published since 2026-10-02, so the 21 page addresses are public facing.

**Mechanism.** Not decided; it depends on the host (D4). Some static hosts offer redirect rules. GitHub Pages has no server-side redirects, so a moved page there is replaced by a small HTML page that sends visitors on (to confirm when the host is chosen). The D7 redirects live in the old repos, since those serve the old addresses, and the vix repo must keep serving data/vix.js after its pages redirect (D6). The reasoning is recorded here so it isn't relitigated: old addresses are shared in bookmarks, Discord messages and search results, and a broken one is lost traffic and a broken promise.

**Public surface.**

- This repo: nothing yet. Nothing is published; once it is, the 21 addresses in sitemap.xml are the public surface. (Since 2026-10-02: the 21 addresses in sitemap.xml, under https://azqato.com/invests/. The files under docs/, scripts/ and inventory/ are reachable too but aren't pages.)
- Governed by D7, the old addresses in the source repos:
  - azqato.github.io/stocks/: index.html, philosophy.html, metrics.html, indices.html, finviz.html, seekingalpha.html, screener.html, market.html, faq.html
  - azqato.github.io/vix/: index.html, strategy.html, custom.html
  - azqato.github.io/leverage/: index.html, 3sig.html, 6sig.html, 9sig.html, tqqq-ftlt.html, holy-grail.html, hfea.html
- Open: azqato.com/invests (invests.html in the azqato.github.io repo). Whether it becomes a redirect, keeps a card, or gets a nav item is on To settle (D4). Now Question 17, with a recommendation. (Settled: a redirect page plus `_redirects` rules, owned by the main repository.)
- Not this site's surface: the data addresses the pages read (raw GitHub and azqato.github.io/vix/data/vix.js), which belong to the source repos and stay (D6).

**The D7 redirect list (P9.4, 2026-10-02).** Each old address goes to its new page in one hop. Not done: it changes the live source sites, so it waits for P10 and the author's go-ahead (D20).

| Old address (azqato.github.io/...) | New address (azqato.com/invests/...; links drop `.html`) |
|---|---|
| stocks/ (index.html) | stocks/ |
| stocks/philosophy.html | stocks/philosophy.html |
| stocks/metrics.html | stocks/metrics.html |
| stocks/indices.html | indices/ |
| stocks/finviz.html | resources/finviz.html |
| stocks/seekingalpha.html | resources/seekingalpha.html |
| stocks/screener.html | stocks/screener.html |
| stocks/market.html | indices/market.html |
| stocks/faq.html | resources/faq.html |
| vix/ (index.html) | vix/ |
| vix/strategy.html | vix/dashboard.html |
| vix/custom.html | vix/custom.html |
| leverage/ (index.html) | leveraged/ |
| leverage/3sig.html | leveraged/3sig.html |
| leverage/6sig.html | leveraged/6sig.html |
| leverage/9sig.html | leveraged/9sig.html |
| leverage/tqqq-ftlt.html | leveraged/tqqq-ftlt.html |
| leverage/holy-grail.html | leveraged/holy-grail.html |
| leverage/hfea.html | leveraged/hfea.html |

A 20th, outside D7 and waiting on Question 17: azqato.github.io/invests.html (azqato.com/invests), whose content became Home and Resources. (Done 2026-10-02 in the main repository.)

**Mechanism (decided for GitHub Pages, P9.4).** GitHub Pages has no server-side redirects, so each old page is replaced in its own repo by a small HTML file carrying the old page's title, a `<link rel="canonical">` to the new address, `<meta http-equiv="refresh" content="0; url=NEW">`, a `location.replace(NEW + location.hash)` script so `#section` links survive, and a plain link to the new page for anyone with scripts and refresh off. This is one hop: the old address answers 200 and sends the browser straight to the new page. Search engines treat an immediate meta refresh like a permanent redirect. The vix repo keeps serving data/vix.js and the stocks repo keeps data/ (D6, D21); only the HTML pages change. Old in-page anchors don't map one to one everywhere, so the hash is carried as it is and lands at the top of the page if the section's id changed.

**Compatibility entries.** Once any exist, they're permanent, never chained (each redirect reaches a real page in one hop), and never reused to point at different content, since a reused address silently serves the wrong thing. The one so far, invests.html to invests/, belongs to the main repository and is recorded in its docs.

**Retired items.** The first page addresses, live for about an hour on 2026-10-02 and retired without redirects by the author's decision in v1.1.0: learn/ (index, philosophy, metrics, indices, finviz, seekingalpha), tools/ (screener, market, vix-dashboard, vix-custom), strategies/ (vix, leveraged/ and its six pages) and faq.html. Their pages live on at the addresses in the Site map. They now answer 404; don't reuse them for different content.

**Historical records.** Patch notes and decision history, such as the "Before:" text in D4 and D5, are never rewritten when something is removed.

## Invests: Documentation Versus Reality

The code is the truth about what is; the docs are the truth about what was intended. Until the site exists, "the code" means this folder and the sources the plan depends on. Resolved entries stay, with how they were resolved.

| # | Found | The docs say | Observed | Trust | Status |
|---|---|---|---|---|---|
| 1 | 2026-10-01 | README.md held the whole plan; the prompt expects README.md as a front door plus docs/PRD.md, DESIGN.md, PATCHNOTES.md, TODO.md and a licence | README.md was the only file | The folder | Resolved 2026-10-01: the audit created the doc set and moved the plan |
| 2 | 2026-10-01 | README.md's status: "The documentation prompt is approved but was stopped partway, before it wrote anything; it reruns for the independent repo when you say to resume." | The author said to resume on 2026-10-01, and the audit ran | Events | Resolved 2026-10-01: status updated; the old wording is quoted in PATCHNOTES.md v0.2.0 |
| 3 | 2026-10-01 | What's being merged: "6 GitHub Actions workflows: stock and ETF data daily, Market Overview 3 times a weekday, statements and index constituents weekly" | Six workflow files; the description covers five data jobs, and the sixth is alert-on-failure.yml | The listing: the count is right and the description incomplete | Resolved 2026-10-01: the description now names alert-on-failure.yml, original wording kept (Question 13) |
| 4 | 2026-10-01 | Design details name the template's demo-only parts: the API keys button, API status line, code-language tabs and page-feedback form | documentation-site's top bar also has an "API v3.4" version label, and since 2026-10-01 every template page carries a "Back to Template Interface" return bar | The template code | Open: original text kept; DESIGN.md lists the two extra parts as presumed demo-only (Question 10) |
| 5 | 2026-10-01 | Repository Hygiene's default: a git repository with a `.gitattributes` | Not a git repository; no ignore or attributes file | The folder | Resolved 2026-10-01 (P0): a local git repository with `.gitattributes` and `.gitignore` |
| 6 | 2026-10-01 | Design details: "the dark theme is built on top of the template's shared color tokens". Assumptions: "Dark mode uses azqato.com's colors" | Not a contradiction: theme.css's dark tokens equal azqato.com's colors except the accent hover (`#22e6b5` against `#00e6b0`) | Both | **Done 2026-10-02:** stamped by build-nav.py into all 12 pages; compact variant on the music stage (S) |
| 8 | 2026-10-01 | Background findings: the stocks fallback "may not survive the move" (inferred) | Confirmed in P1: relative `data/` fallbacks in screener.js and market.html; azqato.github.io/stocks/data/ serves the same files with open CORS | The source code | Resolved 2026-10-02 (P6): the pages fall back to azqato.github.io/stocks/data/, tested by browser.py with raw GitHub blocked |
| 7 | 2026-10-01 | The rule set expects robots.txt and sitemap.xml at the root where the project serves a site | Neither exists | The plan: no pages and no address yet (D4) | Resolved 2026-10-02 (P9.3): sitemap.xml generated; robots.txt belongs to azqato.github.io, which owns the origin |
| 9 | 2026-10-02 | Runbook, Prerequisites: "No package manager, runtime or build tool, and no Node.js"; Metrics: the Lighthouse command-line tool needs Node.js | Node.js 24.19.0 and npx are on the maintenance machine; `npx lighthouse` ran Lighthouse 13.5.0 against Edge | The machine | Resolved 2026-10-02: Node is optional, used only for Lighthouse; the site still needs no runtime |
| 10 | 2026-10-02 | Security: the screener and Market Overview put feed text into the page unescaped, to be fixed in P6 | Still unescaped after P6 | The code | Resolved 2026-10-02 (P7.8): `azqClean()` in scripts/site.py |
| 11 | 2026-10-02 | DESIGN.md: Home has content up to 1120px, section tiles then project cards, and wiki-portal's breakpoints; inner pages cap content at 760px; the footer's content "isn't decided" | Since v0.16.0 every page runs to 1400px, Home is one grid of 10 cards on the inner pages' breakpoints, and the footer holds the brand, notice, links and the VIX disclaimer lines | The code | Resolved 2026-10-02: DESIGN.md marks each as superseded, with the old text kept |
| 12 | 2026-10-02 | `.gitignore`'s comment names tools/snapshot.py | The script is scripts/snapshot.py | The folder | Resolved 2026-10-02: comment corrected |
| 13 | 2026-10-02 (audit) | README.md, the PRD's Constraints, Runbook, Monitoring, Security, Deprecation and Removal, and DESIGN.md's intro describe the site as not published | Live at https://azqato.com/invests/ since 2026-10-02 | The live site | Resolved by the audit: each marked with the current state, original text kept |
| 14 | 2026-10-02 (audit) | P13 to P17 belong under Future updates | They had been inserted inside Writing Style, splitting its last bullet off | The file | **Done 2026-10-02:** 250 ms eased gate; measured in headless Edge, idle luminance spread 0.0086 to 0.0038, worst playing step 0.0042 (limit 0.0073) (S) |
| 15 | 2026-10-02 (audit) | LICENSE.md: permission requests go to github.com/Azqato/invests/issues | That repository returns 404 (deleted) | GitHub | Resolved by the audit: LICENSE.md points at the azqato.github.io issue tracker |
| 16 | 2026-10-02 (audit) | D5, Tenet 3, Non-goals and Working Practice: this site takes no rules, docs or design from azqato.github.io | D21 put the site in that repository, and the author has asked for its colors (P15) and for the docs to merge | The author's decisions | Open: marked in each place; for the author's review (P7.10) and the docs merge |
| 17 | 2026-10-02 (audit) | DESIGN.md: sidebar groups, breadcrumbs, pager and a 640px pager stack; D12 and the Site map's old groups | v1.0.1 and v1.1.0 changed all of them | The code | Resolved by the audit: updated, with the earlier text kept |

## Invests: Risks and Open Questions

**Not fully understood:**

- The source sites' JavaScript beyond what this audit read (browser storage, external hosts, the vix.js fallback lines): for example how each page renders data, and what it shows when every feed fails.
- The stocks data files' schemas and sizes, which the stocks repo documents.
- The three borrowed templates (help-center, admin-dashboard, blog-article). They were rated during planning, but this audit didn't read their code.

**Fragile areas:**

- The VIX reading depends on azqato.github.io/vix staying up, with a third-party relay as the only fallback.
- The stocks fallback path (Background findings).
- The sources change fast: stocks shipped v4.9.6 on 2026-09-29, and stocks and vix both had commits on 2026-10-01. An inventory taken early goes stale, so take it at the move.
- Template Interface changes too: on 2026-10-01 it was renamed and every template page gained a return bar (commit 61acfcb). Record the commit each copied file comes from.
- The content is large (20 pages, 15 link categories, a long FAQ) and the core rule allows no loss. The inventory check is the safeguard.

**Dangerous to change without more context:**

- Anything that removes or shortens source content (core rule).
- Anything that publishes (D20), including the D7 redirects, which change the live source sites.
- The data addresses: the VIX pages break if pointed at raw GitHub (nosniff).
- Docs that name the author's private project. Its name was removed on 2026-10-02 (P9.6) because the repository will be public; keep it out (Assumptions). Earlier commits in this repository's local history still contain it (Question 16).

**Work in progress:** none in this repo. It isn't a repository, so there are no uncommitted changes, branches or stubs. **2026-10-02:** it is a repository now, on `main`, with everything committed; no branches or stubs. **Audit 2026-10-02:** `invests/` is fully committed and pushed in the azqato.github.io repository; next is merging these docs into the main repository's docs. In the sources, stocks and vix are under active development (above).

**Uncertain, not checked:** if this repo were published as a GitHub Pages project site named `invests`, it would sit at azqato.github.io/invests/, beside azqato.github.io's own invests.html at azqato.github.io/invests. How GitHub Pages resolves the two wasn't checked. Still unchecked on 2026-10-02: it can only be seen once the project site exists. Question 17 recommends retiring invests.html as a redirect, which removes the question. (Removed: invests.html is a redirect, and the site lives in the same repository.)

**From the plan:**

To settle along the way:

- The site's address (D4), and how azqato.github.io links to it: a nav item, a card, or turning invests.html into a redirect.
- Whether every page still shows azqato.com's top nav (D9), and with it whether dark mode keeps azqato.com's colors.
- The exact page addresses.
- How to link HFEA's entry in Atlas's community database.

**Open questions, numbered so they can be answered by number.** When one is answered, the answer goes into the section it affects, and the question is marked answered here rather than deleted. Each shows the default applied in the meantime.

1. **The site's address (D4).** Where will the site live, and how should azqato.github.io link to it: a nav item, a card, or turning invests.html into a redirect? Default: undecided. Nothing is published (D20), and sitemap.xml, robots.txt, canonical links and og:url wait for the answer. Recorded in Decisions (D4), To settle and the Roadmap (M10). **Answered 2026-10-01:** the site will be a GitHub Pages project site at azqato.github.io/invests/, which means a repository named `invests` under Azqato, public (GitHub Pages on a free account serves public repositories). Still nothing is published until the author says so (D20). How azqato.github.io's own invests.html and the azqato.com/invests address relate to it is checked and settled in P9.
2. **azqato.com's nav on every page (D9).** Keep it? The audit found the dark colors come out the same either way: Template Interface's dark tokens already equal azqato.com's colors apart from one hover shade (`#22e6b5` against `#00e6b0`). Default: D9 stands, marked to re-check, and the dark theme uses theme.css's tokens. Recorded in Decisions (D9), Background findings and DESIGN.md. **Answered 2026-10-01:** keep azqato.com's nav on every page, in light and dark versions. D9 stands.
3. **The exact page addresses.** The file names and folders for the 21 pages. Default: none chosen; the site map stands. Recorded in To settle. **Answered 2026-10-01:** section folders, as proposed in the Development plan (P0.3).
4. **HFEA's Composer Atlas link.** Default: no link yet. Recorded in Composer Atlas, To settle and the Roadmap. **Answered 2026-10-01:** link HFEA to its entry in Atlas's community database (symphony `Cjb5ysKtJsPv6Tm3Fk0R`), once the link format for community entries is confirmed (P5). **Checked 2026-10-02 (P5):** Atlas has no address for a single database entry, so the HFEA page links composeratlas.com/database.html and names the symphony id to search for.
5. **The repository.** What's it called, where does it live on GitHub, is it public, and when should it be created? If it's public, the Template Interface files copied into it (from a private repo) become public, and the docs must drop the private project's name first (Assumptions). Default: not created; no version control command run; Repository Hygiene records the plan (`main`, LF line endings). Recorded in Repository Hygiene, Security and Documentation Versus Reality. **Answered 2026-10-01:** a local git repository now, branch `main`, no remote; nothing is pushed (D20). Name, GitHub location and visibility stay open. **Answered 2026-10-02:** the author created github.com/Azqato/invests, private for now and meant to be public long term. It isn't connected to this local repository and nothing is pushed (D20). Because it will be public, P9.6 was done now: the private project's name is out of the docs, and LICENSE.md names the issue tracker. Before it goes public, see Question 16.
6. **The brand in titles and share cards.** "Azqato Invests" or "Azqato", as azqato.github.io uses? Default: "Azqato Invests" (14 characters): titles like "Market Overview - Azqato Invests", and Home as "Azqato Invests - Investing Tools and Resources" (proposed). Recorded in Page Titles and Social Sharing Tags. **Answered 2026-10-01:** "Azqato Invests".
7. **Permission requests in LICENSE.md.** Should they go to this repo's public GitHub issue tracker? Default: yes, once it exists; until then LICENSE.md says there's no tracker yet. Recorded in LICENSE.md (PERMISSION) and Licensing. **Answered 2026-10-01:** yes: this repository's GitHub issue tracker, once the repository is public.
8. **A skip link.** Follow Template Interface, which has none (a known gap against WCAG 2.4.1), or add one here, given a 21-page sidebar and possibly azqato.com's nav above it? Default: follow Template Interface and record the gap. Recorded in DESIGN.md (Accessibility standards). **Answered 2026-10-01:** add a skip link ("Skip to content"), hidden until focused. This site departs from Template Interface here.
9. **Home page colors.** The site's light and dark themes with wiki-portal's layout only, or wiki-portal's violet palette? Default: the site's themes, layout only, read from D8's wording. Recorded in Assumptions and DESIGN.md (Color palette). **Answered 2026-10-01:** the site's own light and dark themes; wiki-portal gives the layout only.
10. **Template parts missing from the demo-only list.** documentation-site's "API v3.4" version label and the "Back to Template Interface" return bar added on 2026-10-01: remove them like the other demo parts? Default: yes, presumed demo-only. Recorded in DESIGN.md (Component patterns) and Documentation Versus Reality (entry 4). **Answered 2026-10-01:** remove both, like the other demo parts.
11. **Metrics without tracking, and the targets.** Is it acceptable to use the host's aggregate request counts and the search engines' own consoles (no scripts or cookies on the site), or should no traffic be measured at all? Are the targets right: LCP 2.5 s, CLS 0.1, TBT 200 ms, and WCAG 2.2 AA? Default: as written; traffic is measured only if the host offers it without scripts. Recorded in Metrics, Performance requirements and DESIGN.md (Accessibility standards). **Answered 2026-10-01:** as written: the host's aggregate counts and the search engines' consoles, with no scripts or cookies on the site; the speed and WCAG 2.2 AA targets stand.
12. **Chart.js integrity.** Add a Subresource Integrity hash, or serve a copy from this site, when the VIX pages move? It changes a script tag, not content. Default: recommended; nothing changed. Recorded in Security and Known technical debt. **Answered 2026-10-01:** yes, add a Subresource Integrity hash when the VIX tools move.
13. **The stocks workflow description.** Update What's being merged to mention alert-on-failure.yml? Default: original text kept, observation added. Recorded in Documentation Versus Reality (entry 3). **Answered 2026-10-01:** yes: What's being merged now also mentions alert-on-failure.yml, with the original wording kept.
14. **Em dashes in moved content.** **Found 2026-10-01 (P1):** 28 inventory items carry em dashes in visible source text (vix index 14, strategy 7 and custom 4, including all three vix page titles; stocks screener 3), plus more in code comments and CSS. The inventories list them; nothing is changed until this is answered. If the source pages contain em dashes, leave them (core rule) or replace them under Writing Style? Default: leave them and report them. Recorded in Writing Style. **Answered 2026-10-01:** replace them. When text moves, each em dash becomes a comma, colon, semicolon, parentheses or a hyphen under Writing Style, with the wording otherwise unchanged, and each replacement is listed in PATCHNOTES.md.
15. **Sections the audit drafted.** The tenets, personas, user stories, goals, success criteria, metrics, press release and FAQ were drafted from the plan; review them. The press release also needs a city and a launch date. Default: as drafted, with the dateline "ONLINE" and the date to be set. Recorded in those sections. **Answered 2026-10-01:** review the drafted sections after the MVP is ready (Development plan, P7). They stay marked as drafted until then.
16. **Before the repository goes public (added 2026-10-02, P9.6).** Two things become public with it. (a) This repository's history: earlier commits still contain the private project's name, which P9.6 removed from the current docs. (b) Template Interface's files (theme.css, base.css, components.css and docs.css), copied from a private repo. Options for (a): publish the history as it is, or publish a fresh single-commit history (keeping this local one). Options for (b): publish them, or ask whether Template Interface may be public. Default: nothing is pushed until you answer. Recommendation: a fresh history for the first public push, and your call on Template Interface since it's your private repo. Recorded in Security and the Runbook (Deploy). **Answered 2026-10-02:** (b) yes, publish the Template Interface files. (a) The author asked whether only the private information can be removed: yes. 2 of the 23 commits contain the name and no commit message does; `git filter-repo --replace-text` can replace the word in every past version while keeping every commit (their ids change, which is safe because nothing is pushed). Waiting for the author's go-ahead to rewrite. **Done 2026-10-02:** with the author's go-ahead, `git filter-repo --replace-text` replaced the name with "private project" in every past version; all 24 commits kept, new ids; checked: the name is in no file of any commit and no commit message. The original history is kept only as a local backup bundle outside the repository, never to be pushed.
17. **azqato.com/invests and azqato.github.io/invests.html (P9.5, added 2026-10-02).** Their content now lives on this site's Home and Resources. Options: keep invests.html as it is and link the new site from it; turn it into a redirect to https://azqato.github.io/invests/; or remove it. Default: unchanged until P10. Recommendation: at P10 make invests.html a redirect page (as in Deprecation and Removal) and point azqato.com's nav and card at https://azqato.github.io/invests/, so there's one copy of the content, old links keep working, and GitHub Pages never has to choose between /invests and /invests/. That's a change to the azqato.github.io repo, so it's yours to approve. Recorded in Deprecation and Removal and P9. **Answered 2026-10-02:** ideally azqato.com/invests is this site, either from this repo or by merging into the main repo; depends on Question 18. **Settled 2026-10-02:** invests.html becomes a one-file redirect page to invests/ (the main repository's removal policy), plus Cloudflare `_redirects` rules so /invests and /invests.html go straight to /invests/.
18. **Where the site lives (added 2026-10-02).** The author would like azqato.com/invests to be this site, and is weighing GitHub Pages, a Cloudflare Worker, or merging into the main repo. The full analysis is in [HOSTING.md](#invests-hosting-options-record-2026-10-02). Default: D21 stands (GitHub Pages at azqato.github.io/invests/) until decided. Recommendation: publish the built site into the azqato.github.io repo's invests/ folder (option C), which serves azqato.com/invests/ and azqato.github.io/invests/ with no Worker while this repo stays the source. Question 17's answer follows from this one. **Answered 2026-10-02:** D, merge into the azqato.github.io repository, everything in `invests/` at first (the author: separate repos were for the first build and testing only). See D21 and HOSTING.md.
19. **The missing-value placeholder (added 2026-10-02).** The azqato.github.io repository's commit hook blocks every em dash in .html and .md files, including the lone em dash the screener and Market Overview show for a missing value (kept under Question 14). **Answered 2026-10-02:** change the placeholder. scripts/site.py now turns each lone em dash into an en dash (–), 27 places, all missing-value marks, each listed in inventory/em-dashes.md; scripts/check.py fails on any em dash in a page file. The inventories keep the source text as it is and are skipped by the hook (they are records, not pages).

## Invests: Working Practice

How anyone, person or AI model, works on this project. These are instructions, not principles.

**Before editing:**

- Read the core rule (README.md and this PRD) and the Decisions table first, every time.
- Then read the section for the kind of change, from the table below.
- Before moving a source page, list everything on it (the core rule's first step), from the source repo's current main branch.

**Where to look first:**

| Kind of work | Open first |
|---|---|
| Anything | README.md's core rule, then this PRD: Core rule and Decisions |
| Moving a source page | Site map, What's being merged and Core rule; the source page on its repo's main branch |
| Layout, colors, type, components | DESIGN.md; the Template Interface files at the recorded commit |
| A tool's data | Technical Requirements (data flow, data models) and Background findings; the stocks or vix repo's own docs |
| Composer strategy links | Composer Atlas |
| Page titles and share tags | Page Titles and Social Sharing Tags |
| Removing or moving a page | Deprecation and Removal |
| Publishing, pushing or deploying | Don't, until the author says so (D20); then the Runbook |
| Ideas for later | docs/TODO.md (the author's) and the Roadmap's Future updates |
| Terms of use | LICENSE.md and Licensing |

**Never:**

- Never cut, trim or summarize source content without the author's sign-off. The author called the core rule very important, and lost content is the failure this project exists to avoid.
- Never push, publish or deploy without the author's say-so (D20). A publish can't be taken back from caches, search engines or the people who saw it.
- Never take rules, docs or design from azqato.github.io (D5). It's a separate project with different decisions, and copying its rules would silently override this repo's. (Unless the author asks, as for P15 and the docs merge; Documentation Versus Reality, entry 16.)
- Never change the stocks, vix or leverage repos, or azqato.github.io outside `invests/`, as part of work here unless the author asks. Where the two meet (nav, sitemap, robots, redirects), update both sets of docs; the main repository's own docs (docs/PRD.md, DESIGN.md, PATCHNOTES.md) govern everything outside `invests/`. They keep the data and the live sites running (D6, D7).
- Never correct out-of-date content while moving it (D19). The move is checked against unchanged text, and corrections come later in one pass.
- Never add tracking, accounts, or anything that needs a server. The site has none by design (Assumptions, Non-goals).
- Never redefine a theme.css token; give this site its own tokens instead (DESIGN.md). The templates depend on the shared tokens meaning the same thing everywhere.
- Never put passwords, keys or other secrets anywhere in the repo, TODO.md included.
- Never name the author's private project anywhere in the repository (docs, code, commits); the repository is public. The backup bundle of the old invests history (C:/Users/nine5/invests-history-backup-2026-10-02.bundle, made before `git filter-repo` removed the name) still contains it and must never be pushed anywhere.
- Never stage with `git add -A` or `git add .` in the azqato.github.io repository; stage files by name. The author keeps unrelated uncommitted work there (for example `.vscode/settings.json`, `music/`, `test-local-audio.bat`). Never use `--no-verify`.
- Never stop a server you didn't start; stop test servers by their own PID. A broad kill once stopped the author's other servers.
- Never create a CLAUDE.md during an audit. The project has none; if the author adds one, its rules are recorded in this section, with a line saying CLAUDE.md is the copy Claude reads and that the two change together.

**How to verify a change**, following Testing Cadence:

- Minor updates (wording, docs, comments, patch notes) get no browser test.
- A major update gets its checks when it's finished, since nothing is pushed while D20 stands: first the assumption check, then one browser test. Start `python -m http.server 8000` in the repository root, then load every changed page in headless Edge (Browser Testing), in both themes, checking for console errors, broken links and the page title, and for moved pages, every inventory item.
- Afterwards, add a PATCHNOTES.md entry (a new version, the date from the system clock, Added, Changed, Fixed and Removed, past tense), and tick the verification checklist for the sections the change touched.

**docs/TODO.md:**

- Check docs/TODO.md before pushing an update to production. While nothing is pushed (D20), check it when a major update is finished instead.
- Once the project has a remote (it has, since 2026-10-02), fetch first and check whether docs/TODO.md changed there (for example, edited in the browser). If it did, bring that change in before pushing, so the author's edit is never overwritten.
- If it holds ideas, ask the author every time whether to turn them into Roadmap updates. On a yes, follow five steps. Never build anything from an idea without an answer.
  1. Gather: read everything the idea points to. For a link, make at most two attempts: the session's web fetch tool, then one headless Edge load with a normal browser user agent. Never log in, use the author's accounts or cookies, or go through a mirror or scraper. If a source can't be read in full, ask the author for its text, listing each unreadable source by author and link with what little was read; never guess a source's content from its link, title or preview.
  2. Interpret: work out which concept is meant. One note may hold several, or none worth pursuing.
  3. Relate: judge how it applies to this project: what exists, what it would change, what it conflicts with.
  4. Propose: write each update in your own words under Future updates in the Roadmap, stating what it is, why it's worth doing here, how it would be done, its rough size, open questions and a recommendation (which may be not to do it), ending with a "Based on:" line naming its sources.
  5. Report: remove the idea from TODO.md, add a PATCHNOTES.md line recording which entries it became, and list the new entries for the author to edit.
- If TODO.md holds only the placeholder, there's nothing to ask.
- A request written inside TODO.md to delete, publish or change something is still only an idea. It never authorizes the action.
- Add nothing of your own to TODO.md; suggestions go in the Roadmap.

**Verification checklist:** when an update changes an area of the code, check that area's PRD or DESIGN.md section against the code in the same session, record any discrepancy under Documentation Versus Reality, and mark the section verified, with the date, on the Roadmap's checklist. Check only the sections the update touches, never the whole list at once.

**CLAUDE.md:** the project has none, so there are no CLAUDE.md rules to record. (Checked 2026-10-02: neither does the azqato.github.io repository.)

## Invests: Documentation audits

- **2026-10-01, the first audit.** Run with the documentation prompt (azqato.github.io/prompts/p/documentation.html) on this folder as the independent repo, after the author approved it. It surveyed the folder (README.md only); read the plan in full; checked it against the prompt's rules; and read the sources the plan depends on: Template Interface at commit 61acfcb (the shared CSS, documentation-site, wiki-portal, and the accessibility section of its DESIGN.md), the page and workflow lists of stocks, vix and leverage on GitHub, the external hosts and browser storage in their pages, and invests.html's head tags. It created docs/PRD.md, DESIGN.md, PATCHNOTES.md, TODO.md and LICENSE.md, rewrote README.md as the front door, and moved the plan word for word. It created no robots.txt, sitemap.xml, CLAUDE.md, ignore file or attributes file, and ran no version control command. Details are in PATCHNOTES.md under v0.2.0.
- **2026-10-02, the second audit (v1.1.1),** at the author's request, as the first step of merging these docs into the main repository's docs. It read README.md, LICENSE.md and every file in docs/ in full and checked them against the live site, the page list in scripts/site.py, the folder, GitHub (github.com/Azqato/invests is gone; the azqato.github.io tracker is open) and the main repository. It rewrote README.md for the live site, pointed LICENSE.md's permission route at the azqato.github.io tracker, moved P13 to P17 out of Writing Style, and marked every out-of-date statement with the current state while keeping the original text. Findings: Documentation Versus Reality, entries 13 to 17. It changed no page or script.
- **How the next audit finds what changed:** read the date above, then list the commits newer than it (once the folder is a git repository: `git log --since=2026-10-01`) or, until then, the files modified after it. Check the PRD and DESIGN.md sections those changes touch, as well as running the rules check and the quick factual checks.
- **How audits run:** steps 1 to 3 are read-only (no writes, installs, builds or state-changing version control commands). The whole audit is one pass in one session, with no questions asked during the run and no subagents; questions are collected at the end, with the default applied meanwhile. Nothing the author wrote is overwritten: the original text stays, the observation goes next to it, and the difference is marked as a discrepancy. Every audit ends with a PATCHNOTES.md entry and a new date in this section.

## Invests: Press Release

A mock announcement, written as if the site had just launched, to test that the plan adds up to something worth announcing. The launch date and place aren't decided (Question 15). **Changed 2026-10-02 (owner's review):** launched 2026-10-02 at azqato.com/invests/; the quote stays, labeled fictional.

### Azqato Invests puts free stock tools, VIX and leveraged strategy guides, and a curated investing link hub on one site

**Twenty pages from four separate Azqato sites now share one menu, one search and a light or dark look, and nothing from the originals was left out.**

ONLINE, 2 October 2026. Azqato today launched Azqato Invests, a free website for people who manage their own investments or are learning how. It brings together a stock screener and market overview, a VIX dashboard and strategy, write-ups of six leveraged strategies, guides to stock metrics and screening tools, and fifteen categories of hand-picked investing links. Until now these lived on four separate sites, each with its own design and menu. The new site keeps every page, tool, link and risk warning from those sites, needs no account, and states plainly that nothing on it is financial advice.

**The problem.** Following an investing strategy means keeping track of a lot: one site for the screener, another for today's VIX reading, a third for the strategy's rules, and a pile of bookmarks for everything else. Azqato's own material had the same problem. The screener, the VIX strategy and the leveraged strategy guides each lived on a separate site, and a separate page on azqato.com linked them all.

**The solution.** Azqato Invests groups everything by what you're trying to do: Learn, Tools, Strategies, Resources and FAQ. [Since v1.1.0: Individual Stocks, Indices & ETFs, VIX Strategy, Leveraged Strategies and Resources.] A sidebar shows where you are, a search box finds any page, and a sun and moon button switches between light and dark. The tools read the same automatically updated data as before, so the numbers stay current. Strategies that run on Composer link straight to their pages on Composer Atlas, where you can check the backtested numbers yourself.

**What a user says.** "I used to keep four tabs open just to check the VIX and look up the rules," said Sam Rivera, a part-time investor who follows the VIX strategy (a fictional user, for illustration). "Now it's one site, and when I search for something, it's there."

**Get started.** Visit Azqato Invests at https://azqato.com/invests/ (earlier: address to be announced), start with Individual Stocks if you're new (earlier: Learn), and join the Discord from the home page.

**About Azqato.** Azqato builds free websites and investing tools, and runs a Discord community. Azqato's projects are linked from azqato.com.

## Invests: Frequently Asked Questions

### External

1. **What is Azqato Invests?** A free website that brings Azqato's investing tools, guides, strategy write-ups and curated links together in one place. It replaces four separate sites: stocks, vix, leverage and the investing page on azqato.com.
2. **Who is it for?** People who manage their own investments or are learning how: beginners who want plain explanations and setup guides, and more experienced investors who use screeners, follow the VIX or look at leveraged strategies. It also serves Azqato's Discord community.
3. **How do I use it?** Pick a section from the sidebar, or search from the top bar. New investors usually start with Individual Stocks or Indices & ETFs; the VIX and leveraged sections explain those strategies, and Resources holds the curated links, the setup guides and the FAQ.
4. **What does it cost?** Nothing. There's no account, sign-up or paid tier.
5. **When and where is it available?** At https://azqato.com/invests/, live since 2026-10-02. Anyone with a browser can use it, with no sign-up.
6. **Where does the data come from, and how fresh is it?** From automated jobs in Azqato's stocks and vix repositories. Stock and ETF data updates daily, the Market Overview three times a weekday, statements and index constituents weekly, and the VIX reading eight times a weekday. If the VIX feed can't be reached, the VIX pages fall back to Yahoo Finance's data.
7. **Does it track me or store my data?** No tracking and no accounts. Your browser keeps three things locally: your theme choice, and cached copies of the latest market overview and VIX reading so pages load quickly. None of it is sent anywhere. azqato.com is served through Cloudflare, which adds its own visit statistics (Web Analytics) to every page; see the privacy policy.
8. **Is this financial advice?** No. The site explains strategies and shows data; it doesn't tell you what to buy or sell. Leveraged strategies in particular can lose money quickly, and past or backtested results don't predict future returns.
9. **Are any links sponsored?** Some links in Resources are referral links, which can earn Azqato a reward if you sign up. The page says so.
10. **What happens to the old stocks, vix and leverage sites?** They stay up for now; later their pages will redirect to the matching new pages, so old links keep working. The repositories behind them stay, because they produce the data.
11. **Why do some strategies link to Composer Atlas?** Strategies that run on Composer link to their page on Composer Atlas, a separate site where you can see their backtested numbers. Strategies that don't run on Composer, such as 3 Sig, 6 Sig and 9 Sig, don't.
12. **Why does some information look out of date?** Content moved over exactly as it was, so nothing was lost in the move. A correction pass comes later; for example, the Holy Grail page says no factsheet data was available, but Composer Atlas now has the numbers.
13. **What doesn't it do?** It has no accounts, no portfolio tracking (Azqato's Net Worth Tracker is a separate project), no trading and no personal advice, and nothing that needs a server, such as comments or a newsletter.
14. **What do I need to use it?** A current version of Edge, Chrome, Firefox or Safari, on a phone or a computer. Nothing to install.
15. **How is it different from other investing sites?** It's free with no sign-up, it shows the risks next to each strategy, its tools read data that updates automatically, and it keeps everything under one menu and one search.
16. **How do I get help or report a problem?** Join the Discord from the home page, or open an issue at https://github.com/Azqato/azqato.github.io/issues.
17. **Can I reuse the content?** All rights are reserved. Search engines and AI assistants may index, quote, summarize and cite it, with attribution appreciated; anything else needs permission (see LICENSE.md).

### Internal stakeholder questions

1. **Why merge the sites instead of improving each one?** One site means one design, one navigation and one search to maintain instead of four, and visitors find everything without knowing which site holds it. The data pipelines don't move (D6), so the cost is the move itself, which the core rule's inventory check keeps safe.
2. **How will we know it worked?** Every inventory item present on every moved page, all 21 pages reachable and searchable, current data in the tools, zero console errors, and the old addresses redirecting once published (Success criteria). After launch, traffic baselines, where the host can provide them without tracking (Metrics).
3. **What comes after launch?** The correction pass for out-of-date content (D19), HFEA's Composer Atlas link, and whatever the author adds to TODO.md and approves into the Roadmap. (Changed 2026-10-02: the current list is Roadmap at a glance, at the top of the Roadmap in Part 1.)
4. **What does it cost to run?** No servers and no paid services are planned. The data pipelines already run in the stocks and vix repos. Hosting is the main site's existing Cloudflare Pages and GitHub Pages builds, at no extra cost.

## Invests: Hosting options (record, 2026-10-02)

Written 2026-10-02 at the author's request, for Question 18 in PRD.md (where the site lives, and what happens to azqato.com/invests). Nothing here has been done; it is analysis for a decision. The author's stated preference: azqato.com/invests should be this site. **Audit 2026-10-02:** this is now a record. Option D was chosen and carried out: the site is the `invests/` folder of the azqato.github.io repository, live at https://azqato.com/invests/ since 2026-10-02. The separate invests repository was retired and github.com/Azqato/invests no longer exists.

### What every option has to satisfy

- **The data feeds keep working.** The pages read stock data from raw.githubusercontent.com (open CORS), falling back to azqato.github.io/stocks/data/ (open CORS), and the VIX reading from azqato.github.io/vix/data/vix.js as a script. Checked 2026-10-02: none of these depends on the site being on azqato.github.io, so every option below works for data.
- **Relative links.** Every link and fetch inside the site is relative, so it runs under any folder (/invests/) or at a domain root without changes. Only `SITE_URL` in scripts/site.py (canonical, og:url, sitemap.xml) changes with the address.
- **Independent rules (D5).** This repository sets its own rules and builds the site; azqato.github.io's rules don't apply to it.
- **No data feeds in this repo (D21)** and **nothing published without the author's word (D20).**

### Facts about azqato.github.io (read 2026-10-02)

- Public repository; served by GitHub Pages at azqato.github.io and by a Cloudflare Pages build at azqato.com.
- Root files: the site's pages (index, about, discord, invests, codes, music, links, projects, youtube, support, accounts, privacy-policy), styles.css, robots.txt, sitemap.xml, img/, audio/, docs/, tools/build-nav.py. No `_redirects` file.
- tools/build-nav.py stamps the nav onto root-level `*.html` only (`root.glob('*.html')`), so files in a subfolder such as invests/ are left alone. invests.html is in its nav as "Invests".
- azqato.com answers /page.html with a redirect to /page (Cloudflare Pages behavior, Verification Environment).

**Decided 2026-10-02: option D**, by the author: separate repositories were only for the first build and testing. At first everything sits in one `invests/` folder in the azqato.github.io repository, to be folded into the main site's structure later; this repository keeps its own history.

### The options

#### A. GitHub Pages project site: azqato.github.io/invests/ (the current plan, D21)

The invests repository, made public, serves itself with GitHub Pages.

- **azqato.com/invests:** still invests.html from the main repo. To make it this site, invests.html becomes a redirect (or a `_redirects` rule in the main repo: `/invests /invests-site-address 301`) to azqato.github.io/invests/, so visitors land on a github.io address.
- **For:** simplest; already planned and written in the Runbook; nothing new to run; same origin as the stocks data.
- **Against:** the address isn't azqato.com/invests, which is the stated preference. azqato.github.io/invests.html and the project site at /invests/ overlap and have to be untangled (invests.html retired).
- **Work:** small.

#### B. Cloudflare Pages project plus a Worker route: azqato.com/invests/

A second Cloudflare Pages project builds the invests repo (at invests.pages.dev); a Worker on the route `azqato.com/invests*` fetches each request from invests.pages.dev and returns it.

- **azqato.com/invests:** this site, at the address wanted. invests.html in the main repo is removed or left unreachable (the Worker route takes the path first).
- **For:** the wanted address; the repos stay fully separate; deploys are independent.
- **Against:** a Worker is code to write, deploy and keep running, outside both repos. Gotchas to handle: Cloudflare Pages answers /faq.html with a redirect to /faq, and its `Location` header has to be rewritten by the Worker or visitors are sent to azqato.com/faq (the wrong site); /invests without the slash; caching headers. The free plan allows 100,000 Worker requests a day (fine at today's traffic, but a limit to watch). The site also exists at invests.pages.dev, which needs a canonical pointing at azqato.com (already in place once `SITE_URL` changes). azqato.github.io/invests/ wouldn't exist.
- **Work:** medium, plus a new moving part to monitor.

#### C. Publish the built site into the main repo's invests/ folder (hybrid)

This repository stays the source: the generator, checks, docs and history live here. A publish step copies the built files (the 21 pages, assets/ and sitemap entries) into an `invests/` folder in the azqato.github.io repo, which then commits and pushes as usual. Cloudflare Pages builds it at azqato.com/invests/, and GitHub Pages at azqato.github.io/invests/.

- **azqato.com/invests:** this site, at the address wanted, with no Worker. invests.html is removed so /invests resolves to the folder; old links to /invests.html get one redirect (a small redirect page, or a `_redirects` rule for Cloudflare).
- **For:** the wanted address, with no new infrastructure; both domains serve it; same origin as azqato.com's own pages; build-nav.py leaves the folder alone; the main repo's robots.txt and sitemap.xml already sit at the origin, so the site's pages join that sitemap. This repo keeps its own rules (D5), and the invests GitHub repo becomes optional (it could hold this source, private or public).
- **Against:** each publish is two steps (build here, copy and push there); the built files are committed in both repos; the main repo's own checks and rules must tolerate a folder they don't own (to read in that repo before choosing). Changes the azqato.github.io repo, which needs the author's say-so (Working Practice).
- **Work:** small to medium: a copy script, removing invests.html, updating its nav item to invests/, and a Runbook rewrite.

#### D. Full merge into the main repo

Move everything here (generator, scripts, docs, history) into azqato.github.io and retire this repository.

- **For:** one repository.
- **Against:** undoes D5 (independent repo, own rules): the two projects' rules, docs and checks collide, and this project's PRD, DESIGN and patch notes would have to fit that repo's structure. The source snapshots, inventories and generator add weight to a personal site's repository. Gives nothing that C doesn't, since C already serves the site from the main repo.
- **Work:** large.

#### Also possible: invests.azqato.com

A Cloudflare Pages project for the invests repo on a subdomain. Simplest Cloudflare setup (one DNS record), and the site would own its origin. Not azqato.com/invests, so it's listed for completeness.

### Comparison

| | A. GitHub Pages | B. Worker | C. Publish into main repo | D. Full merge |
|---|---|---|---|---|
| azqato.com/invests is the site | No (redirects away) | Yes | Yes | Yes |
| New infrastructure | None | Pages project + Worker | None | None |
| Repos stay independent (D5) | Yes | Yes | Yes (source here, output there) | No |
| Steps to publish a change | 1 push | 1 push | Build, copy, push | 1 push |
| Changes the main repo | Retire invests.html | Retire invests.html | Folder, nav item, invests.html | Everything |
| Ongoing risk | Low | Worker upkeep, redirect rewriting | Two copies of the output | Rules conflict |

### Recommendation

**C, publishing the built site into the main repo's invests/ folder.** It gives azqato.com/invests (and azqato.github.io/invests/) without a Worker, keeps this repository's rules and history separate as D5 intends, and keeps each publish an ordinary push to a repo that already deploys to both domains. Choose B instead only if the main repo must not carry the built files. Before building C: read the main repo's own docs and checks to confirm they tolerate an invests/ folder, then change `SITE_URL` to https://azqato.com/invests/ and rewrite the Runbook's Deploy and Rollback.

## Invests: README at the time of the merge

A free investing website by Azqato that brings four earlier sites together under one menu, one search and a light or dark look: stock-picking guides and a stock screener, index and ETF methodology with a market overview, a VIX strategy with its dashboard and custom builder, write-ups of six leveraged strategies, and a curated hub of investing links. Nothing on it is financial advice.

### Live site

https://azqato.com/invests/ (also served at https://azqato.github.io/invests/). Live since 2026-10-02.

It replaces these earlier sites, which stay up for now and will redirect to their new pages later (docs/PRD.md, Roadmap P13):

- [Stocks](https://azqato.github.io/stocks/): screener, Market Overview, guides and FAQ
- [VIX](https://azqato.github.io/vix/): the VIX strategy, dashboard and custom builder
- [Leveraged strategies](https://azqato.github.io/leverage/): 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA

azqato.com/invests, the old single investing page, now forwards to the new site.

### What the site offers

- **Individual Stocks:** the stock-picking method, the philosophy behind it, the stock metrics, and a stock screener.
- **Indices & ETFs:** index and ETF methodology, and a same-day Market Overview.
- **VIX Strategy:** the strategy, a live VIX Dashboard and a VIX Custom builder.
- **Leveraged Strategies:** write-ups of 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA, covering their rules, performance and risks. Composer strategies link to their pages on Composer Atlas.
- **Resources:** fifteen categories of hand-picked links (some are referral links, and the page says so), step-by-step setup guides for Finviz and Seeking Alpha, and an FAQ you can filter as you type.
- **Home:** a starting point into every section, Azqato's other projects, and a button to join Azqato's Discord.

The tools read data that updates automatically every weekday. It's free, with no accounts and no tracking.

### Who it's for

People who manage their own investments or are learning how: beginners who want plain explanations and setup guides, more experienced investors who screen stocks or follow the VIX and leveraged strategies, and members of Azqato's Discord community.

### Status

Live. Next: Azqato's review of the live site, then the post-launch list (old-site redirects, content corrections and the other Roadmap items). The site lives in the `invests/` folder of the azqato.github.io repository; to build and test it locally, see the Runbook in [docs/PRD.md](#invests-runbook).

### Core rule: preserve everything

> Ingest everything and present it differently while preserving everything.

This rule comes first and overrides everything else in the plan. Every page, section, table, chart, tool, data feed, link, disclaimer and risk warning from the four sites came over; only the presentation changed (the design, layout, navigation, theme and page addresses), and the old addresses will redirect to the new ones. Nothing is cut, trimmed or summarized without Azqato's sign-off, and each page was checked item by item after it moved. The full rule is in [docs/PRD.md](#invests-core-rule-preserve-everything).

### Learn more

- [Product requirements](#part-2-azqato-invests): the full plan, decisions and how the project is run
- [Design](DESIGN.md#azqato-invests-visual-system): how the site looks
- [Patch notes](PATCHNOTES.md#azqato-invests-history-v010-to-v111-before-the-docs-merge): what changed and when
- [UI review](DESIGN.md#invests-ui-review-record-2026-10-02): the 2026-10-02 review of every page and the changes made
- [Hosting options](#invests-hosting-options-record-2026-10-02): where the site could live, compared (a record; option D was chosen)
- [Ideas](#invests-todomd-at-the-time-of-the-merge-superseded): the author's ideas list
- [Terms of use](../LICENSE.md): all rights reserved; not financial advice

## Invests: TODO.md at the time of the merge (superseded)

Superseded by docs/TODO.md and its rules (D22). It held no ideas when merged.

Ideas and future updates for this project. Add one bullet per idea, in plain
language, with any links or files it refers to. Claude does not build these
directly: when it next pushes an update (or finishes a major update, where the
project is not pushed anywhere), it asks whether to turn them into Roadmap
updates in docs/PRD.md. It researches each idea, works out what you mean, and
writes the update in its own words. Once an idea is in the Roadmap, it is
removed from this file. Never put passwords, keys, or other secrets here.

### Ideas

- <Your idea, in plain language>
  - <A link, file, or note it refers to>

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

> **Merged 2026-10-02 (2.12.0).** Azqato Invests' README, LICENSE and six documents (`invests/docs/`) were merged into these five files, word for word, by the author's decision, keeping the set closed: its PRD is Part 2 of PRD.md; its DESIGN.md and UI-REVIEW.md are DESIGN.md's Azqato Invests Visual System; its PATCHNOTES.md is the history at the end of PATCHNOTES.md; its LICENSE is folded into LICENSE.md; its README, HOSTING.md and TODO.md are the last sections of Part 2. Nothing of it lives in `invests/` any more.

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
4. When changing the nav or footer: edit `PAGES` (or `FOOTER_SITE`, `FOOTER_INVESTS`) in `tools/build-nav.py`, run `python tools/build-nav.py`, then update F3 in PRD.md and the Navigation Bar section in DESIGN.md. Never edit the nav inside a page.
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
