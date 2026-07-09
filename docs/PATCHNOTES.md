# Patch Notes

All notable changes to the Azqato Portfolio are documented here.
Format: `[version] - YYYY-MM-DD`

---

## [1.0.0] - 2026-06-06

### Added
- Initial release of the portfolio site.
- Self-contained `index.html` with zero external dependencies.
- Project card grid with icon, name, description, tags, GitHub link, optional demo link, star count, and last-updated fields.
- Tag filter bar, auto-generated from the `PROJECTS` array; filters the grid in real time.
- Project count label that updates to reflect the active filter.
- Sticky nav bar with logo and GitHub profile link; collapses nav links on mobile.
- Hero section with status badge, headline, bio, and two CTA buttons.
- Language-specific tag colour classes: `lang-js`, `lang-ts`, `lang-py`, `lang-cs`, `lang-html`, `lang-css`, `lang-go`, `lang-rust`, `lang-java`.
- Hover animations on cards: lift, border highlight, top-edge gradient.
- Fully responsive layout (320 px → 2560 px).
- CSS custom properties for easy retheme via `:root` variables.
- `README.md` with setup and deployment instructions.
- `PRD.md` documenting requirements, user stories, and design tokens.
- `PATCHNOTES.md` (this file).

---

## [1.1.0] - 2026-06-06

### Added
- Three live projects populated from their READMEs: Net Worth Tracker, VIX Strategy, and Lantern.

### Changed
- Project card title now links to the live GitHub Pages site (`demo` URL) instead of the GitHub repository, making the primary action open the running app.
- GitHub repository link retained as a separate icon button on each card alongside the live-site (↗) button.

---

## [1.2.0] - 2026-06-06

### Changed
- Project tags simplified to category-only labels: Net Worth Tracker and VIX Strategy tagged `Finance`; Lantern tagged `Social`. Removed tech-stack tags (JavaScript, Chart.js, Dashboard, Privacy, Tailwind CSS) from the filter bar.
- Nav "Projects" link replaced with "Index", pointing to `https://azqato.github.io/`.
- Removed "Browse Projects" secondary CTA button from the hero section.

---

## [1.2.1] - 2026-06-06

### Changed
- README title updated from "Azqato Portfolio" to "Azqato's Portfolio".
- Added live site link (`https://azqato.github.io/`) directly below the README title.

---

## [1.2.2] - 2026-06-06

### Added
- ⚡ emoji favicon added to all pages via inline SVG data URI with no external image file required.

---

## [1.3.0] - 2026-06-07

### Added
- `support.html`: dedicated support page with a personal pitch, Buy Me a Coffee CTA (buymeacoffee.com/azqato), and an affiliate partners grid (6 placeholder cards: Tesla, Robinhood, M1 Finance, Webull, Coinbase, Public).
- "Support" nav link added to `index.html` pointing to `support.html`.
- "Support" nav link on `support.html` highlights as active to signal current page.
- Affiliate card design: square logo area, promo badge, description, and CTA button.
- Pitch card on support page with gradient top border, avatar, bio, and signature pulled from the buymeacoffee About section.

---

## [1.3.1] - 2026-06-07

### Changed
- Buy Me a Coffee CTA section moved above the About Azqato pitch card so the support ask is the first thing visitors see after the hero.
- CTA paragraph replaced with the full buymeacoffee disclaimer: investment intent statement and fund-use caveat.
- Removed the "Opens buymeacoffee.com/azqato, One-time or monthly, 100% goes to the journey" sub-line from the CTA.
- Removed duplicate investment paragraph from the pitch card body since it now lives in the CTA above.
- All em dashes replaced with commas across `support.html` for improved readability.

---

## [1.3.2] - 2026-06-07

### Changed
- CTA disclaimer paragraph left-aligned for improved readability, while the emoji, heading, and button remain centered.

---

## [1.4.0] - 2026-06-07

### Added
- `about.html`: dedicated About page with hero section and the Azqato pitch card (bio, role line, signature).
- "About" nav link added to all pages pointing to `about.html`, with active state highlighted on `about.html`.
- `.nav-links a.active` CSS rule added to `index.html` to support active nav highlighting.

### Changed
- Nav standardised across all pages: Portfolio, About, GitHub, Support. "Index" (external azqato.github.io link) replaced with "Portfolio" (relative `index.html` link) on all pages.
- About Azqato pitch card moved from `support.html` to `about.html`. `support.html` now focuses solely on the Buy Me a Coffee CTA and affiliate partners.
- Footer simplified to "Built by Azqato" across all pages, removing the redundant GitHub link from footer text.

---

## [1.4.1] - 2026-06-07

### Changed
- About page bio expanded with full background story: gaming origins, Twitch and YouTube content creation, B5TA community on RuneScape and Discord, web development work, and closing call to join the journey.
- Role line updated from "Investor, Developer, Community Builder" to "Content Creator, Web Developer, Community Leader" to better reflect the full bio.
- Em dash removed from closing paragraph ("adventure, one built on...").

---

## [1.5.0] - 2026-06-07

### Added
- Clan B5TA project card: community website for the RuneScape clan founded in 2014, tagged `Social` and `Gaming`, linking to the live GitHub Pages site and repo.
- `Gaming` added as a new filter tag category.

---

## [1.5.1] - 2026-06-07

### Changed
- Clan B5TA tag simplified from `Social, Gaming` to `Social` only. `Gaming` filter category removed; current categories are `Finance` and `Social`.

---

## [1.6.0] - 2026-06-07

### Added
- Cat Food Center project card: mobile-first PWA for evaluating cat food via barcode scan or search, tagged `Tools`, linking to the live GitHub Pages site and repo.
- `Tools` added as a new filter tag category.

### Changed
- Net Worth Tracker tagged with `Tools` in addition to `Finance`.

---

## [1.6.1] - 2026-06-07

### Changed
- Cat Food Center icon updated from 🐱 emoji to the project's own `favicon.svg` via the new `iconUrl` field.

### Added
- `iconUrl` optional field on project entries: accepts a URL to an image or SVG and takes precedence over `icon` when set.

---

## [1.7.0] - 2026-06-07

### Changed
- Public affiliate card: real referral link added (`share.public.com/azqato`), promo updated to "Free $20", description updated to match.
- Robinhood affiliate card: real referral link added (`join.robinhood.com/robertg273/`), promo updated to "Free $5–$200 Stock", description updated to match.
- M1 Finance affiliate card: real referral link added (`m1.finance/BVZBG3OqOfMj`), promo updated to "Free $75 Bonus", description updated to reflect $10,000 funding requirement and M1 Premium benefit.
- Affiliate section note updated from "Placeholder links" to "Some links are live, others are coming soon."

---

## [1.7.1] - 2026-06-07

### Changed
- Tesla affiliate card: real referral link added (`ts.la/robert459550`), promo updated to "Free 3 Months FSD", description updated to reflect 3 months of Full Self-Driving or $400 off Solar or Powerwall.

---

## [1.7.2] - 2026-06-07

### Changed
- M1 Finance affiliate card description updated to exact wording specified.

---

## [1.7.3] - 2026-06-07

### Changed
- Affiliate section note replaced with a plain-English disclaimer explaining how referral links work.

### Removed
- Webull and Coinbase placeholder cards removed from the affiliate grid.

---

## [1.7.4] - 2026-06-07

### Added
- Lyft affiliate card: 50% off first ride up to $10 (`lyft.com/invite/ROBGOLDY630855`).

---

## [1.8.0] - 2026-06-08

### Added
- `/docs/` directory created to house all project documentation.
- `docs/TRD.md`: Technical Reference Document covering system architecture, tech stack, data models, internal data flow, state management, third-party integrations, performance requirements, and known technical debt.
- `docs/DESIGN.md`: Design system document covering color palette (all CSS custom properties), typography, spacing, breakpoints, component patterns, accessibility standards, and motion rules.
- `docs/PRFAQ.md`: Press release and FAQ (internal and external).
- `docs/TENETS.md`: Product principles with 5 prioritized tenets.
- `docs/METRICS.md`: Success metrics, targets, measurement methods, and reporting cadence.
- `docs/ROADMAP.md`: Milestone table with current phase, planned features, and deferred items.
- `docs/SECURITY.md`: Security model covering auth, data storage, third-party trust, attack surface, and dependency policy.
- `docs/RUNBOOK.md`: Operational runbook with local setup, build, deploy, rollback, environment configs, common errors, and monitoring.

### Changed
- `PRD.md` moved from project root to `docs/PRD.md` and expanded with problem statement, target user personas, assumptions, and measurable success criteria.
- `PATCHNOTES.md` moved from project root to `docs/PATCHNOTES.md`.
- `README.md` updated with tech stack table, prerequisites section, environment variable reference (none), expanded deploy instructions, link to `/docs/`, and updated file overview reflecting the new `docs/` structure.

### Removed
- `PRD.md` from project root (moved to `docs/PRD.md`).
- `PATCHNOTES.md` from project root (moved to `docs/PATCHNOTES.md`).

## [1.9.0] - 2026-06-08

### Added
- ComposerAtlas project card: curated strategy library and education hub for Composer.trade investing, featuring strategy pages with plain-English logic breakdowns, risk profiles, metrics tables, and a glossary of systematic investing concepts. Tagged `Finance` and `Tools`.

## [1.9.1] - 2026-06-08

### Changed
- ComposerAtlas and Cat Food Center tagged with `Education` to reflect their educational content.
- `Education` added as a new filter tag category.

---

## [1.9.2] - 2026-06-09

### Changed
- Buy Me a Coffee CTA paragraph split: main text ends with `*` asterisk; disclaimer moved below the button in smaller italic text.

---

## [1.9.3] - 2026-06-09

### Added
- Boaty McBoatface Ventures project card: humorous marketing site for a fictional New England canvas exo-skeleton water displacement company, tagged `Meme`.
- `Meme` added as a new filter tag category.

---

## [2.0.0] - 2026-06-09

### Added
- `links.html`: Social and platform links hub, organized into sections: Community and Streaming, YouTube, Music, Social, Investing, and More. All external links from the old website consolidated here.
- `youtube.html`: YouTube channels page showcasing all four channels (Azqato, Azqato Streams, Azqato Mixes, Azqato Chills) as cards with thumbnail photos, channel descriptions, and subscribe buttons.
- `invests.html`: Azqato Invests resource hub with 14 curated sections: Platforms, Careers, ETFs, Companies, Ratings, Screeners, Real Estate, Charts, Databases, Economic Indicators, Education, Guides, Indices, Information, and News.
- `music.html`: Music page featuring the two Spotify playlists (BANGERS, ADDICTIONS) with cover art, plus links to Last.fm, Mixcloud, and YouTube Mixes.
- `accounts.html`: Gaming accounts page listing Azqato's profiles across Steam, League of Legends, Teamfight Tactics, and RuneScape.
- `privacy-policy.html`: Full privacy policy page covering Consent, Information Collection, Log Files, Cookies, DART Cookies, CCPA, GDPR, Children's Information, Affiliate Links, Financial Disclaimer, and Entertainment Purposes.
- `img/` directory with 14 image assets migrated from the old website: profile photos (`home-hero-profile.jpg`, `about-profile.jpg`, `logo-cat-avatar.jpg`), YouTube channel thumbnails (`yt-thumb-azqato.jpg`, `yt-thumb-streams.jpg`, `yt-thumb-mixes.jpg`, `yt-thumb-chills.jpg`), larger channel images (`yt-channel-*.jpg`), Spotify playlist covers (`music-playlist-bangers.jpg`, `music-playlist-addictions.jpg`), and music logo (`music-logo-small.jpg`).
- Profile photo (`home-hero-profile.jpg`) added to the `index.html` hero section as an 80px circular avatar.
- "All Links →" secondary CTA button added to the `index.html` hero actions, pointing to `links.html`.
- Profile photo (`about-profile.jpg`) added to the `about.html` pitch card avatar, replacing the ⚡ emoji.
- `Links`, `YouTube`, and `Invests` nav links added to all pages.
- Privacy Policy footer link added to all pages.

### Changed
- `index.html` hero description expanded to mention content creation, gaming, investing, music production, and streaming, preserving the intro text from the old website's landing page.
- Nav expanded from 4 links (Portfolio, About, GitHub, Support) to 7 links (Portfolio, About, Links, YouTube, Invests, GitHub, Support) across all pages.
- Footer on all pages updated from "Built by Azqato" to include a "Privacy Policy" link.
- `about.html` pitch avatar size increased from 60px to 72px to better display the profile photo.

### Removed
- `oldwebsite/` directory and all its contents deleted after full content migration.

---

## [2.0.1] - 2026-06-09

### Changed
- League of Legends accounts on `accounts.html` updated to Riot ID format: `Chief Rocka` → `서주프#zoop` and `Azqato` → `Azqato#zoop`.
- Both LoL op.gg links updated to the new URL format (`op.gg/lol/summoners/na/`).

---

## [2.0.2] - 2026-06-09

### Changed
- TFT accounts on `accounts.html` updated to metatft.com with Riot ID format: `서주프#zoop` and `Azqato#zoop`. Links updated from lolchess.gg to `metatft.com/player/na/`.
- RuneScape accounts updated: `Hctibaru` replaced with `ironqato`; both links updated from runeclan.com to runepixels.com (`/players/<name>/skills`).

---

## [2.0.3] - 2026-06-09

### Changed
- Privacy Policy link moved from all page footers to the More section on `links.html` as a button.
- Footers across all 9 pages simplified back to "Built by Azqato" only.

---

## [2.0.4] - 2026-06-09

### Changed
- Footer byline updated to "Built by Azqato." on all pages. The period is outside the link element so it renders in `--text-muted` rather than the accent green.

---

## [2.1.0] - 2026-06-10

### Added
- Stock Methodology project card: educational site documenting a fundamentals-driven individual stock and ETF investing methodology, covering 10 evaluation metrics (PEG, P/E FWD, RSI, revenue/EPS growth, cash/debt, 52W range), a Finviz screener guide, Seeking Alpha watchlist setup, and VIX-based index investing strategies. Tagged `Finance` and `Education`.

---

## [2.1.1] - 2026-06-10

### Changed
- All links to the GitHub profile (`github.com/Azqato`) now open in the same tab. Removed `target="_blank" rel="noopener"` from all 20 occurrences across 9 pages (nav links, footer bylines, hero CTA, and links page button).

---

## [2.2.0] - 2026-06-10

### Added
- TQQQ Strategies project card: educational wiki-style site documenting six leveraged ETF strategies side by side: 3 Sig, 6 Sig, 9 Sig, TQQQ For The Long Term, Holy Grail, and HFEA. Each strategy has a dedicated page covering rules and logic, performance notes, risks, and sources. Tagged `Finance` and `Education`. Live at `https://azqato.github.io/leveraged-strategies/`.

---

## [2.2.1] - 2026-06-10

### Changed
- TQQQ Strategies card icon updated from ⚡ to 🚀 to match the site's favicon.

---

## [2.2.2] - 2026-06-10

### Changed
- TQQQ Strategies project card renamed to "Leveraged Strategies" ahead of a planned site rename.

---

## [2.2.4] - 2026-06-11

### Changed
- Fixed HTML-encoded em dash (`&mdash;`) in `index.html` hero bio paragraph. Previous audit only searched for the literal `—` character and missed the entity form.
- `docs/PRD.md` Writing Style section updated to note that em dashes appear in two forms in HTML (`—` and `&mdash;`) and both are prohibited. Audits must search for each form independently.

---

## [2.2.3] - 2026-06-11

### Changed
- Em dashes removed from all HTML pages (accounts.html, index.html, invests.html, youtube.html) and all documentation files (PRD.md, PATCHNOTES.md, ROADMAP.md, DESIGN.md, TRD.md, METRICS.md, SECURITY.md, TENETS.md, PRFAQ.md, RUNBOOK.md) and README.md. Replaced with comma, colon, semicolon, parentheses, or period based on context.
- Version headers in PATCHNOTES.md updated from `[x.y.z] — YYYY-MM-DD` format to `[x.y.z] - YYYY-MM-DD` for consistency.
- `docs/PRD.md` updated with a Writing Style section documenting the no-em-dash methodology and preferred punctuation alternatives.

---

## [2.3.0] - 2026-06-13

### Added
- New introductory landing page at `index.html`, designed as the front door for first-time visitors. It introduces who Azqato is across gaming, content creation, investing, music, and community, then routes visitors onward rather than opening straight into the project grid.
- Discord join as the primary call to action, featured both in the hero and in a dedicated closing CTA band (`discord.gg/39JrFNY7qS`), styled with the official Discord brand color (`#5865f2`) and logo.
- "Explore the site" card grid linking to all eight key destinations: Projects, About, YouTube, Music, Invests, Gaming Accounts, Links, and Support, each with an icon and one-line description.
- Hero with an easygoing introduction and a secondary "Explore the site" anchor button, plus an intro blurb with a short bio and category pills (Gaming, Investing, Music, Web Dev, Community).
- `--discord` and `--discord-hover` CSS custom properties on the landing page.

### Changed
- Site structure reworked so the landing page is the default entry point. The project grid (cards, tag filter, hero) moved from `index.html` to `projects.html`; the new introductory landing page now occupies `index.html`.
- Navigation label renamed from "Portfolio" to "Projects" across all pages, and the link now points to `projects.html`.
- Nav logo on every page links home to `index.html` (the new landing page). The project grid page's logo, previously `href="#"`, now also points to `index.html`.
- `projects.html` page title updated from "Azqato | Portfolio" to "Azqato | Projects".

### Notes
- The landing page follows the existing design system (GitHub dark theme, `#00d4a0` accent, system font stack, zero dependencies) and is self-contained with inline CSS.
- The site now comprises 10 pages.

---

## [2.3.1] - 2026-06-13

### Added
- "Home" and "Discord" links added to the global navigation. Home points to the landing page (`index.html`); Discord points to the community invite (`discord.gg/39JrFNY7qS`) and opens in the same tab, matching the GitHub link convention.

### Changed
- Navigation reordered across all 10 pages to: Home, About, Discord, Invests, Links, Projects, YouTube, GitHub, Support.
- Landing page hero introduction reworded for a more confident, knowledgeable first impression (removed the "music nerd" phrasing and the "front door / come hang out" close).
- Landing page intro blurb refined for tone: now notes B5TA has thrived on RuneScape and Discord for over a decade, and splits "music production" and "DJ mixes" into separate highlighted lanes.
- Highlighted the connecting "and" before "web development" in the intro lanes so it carries the same accent styling as the other lanes.

---

## [2.3.2] - 2026-06-13

### Added
- No Fee Apartments project card: curated directory of no-broker-fee apartment buildings across New York City, Boston, and San Francisco. Tagged `Tools` and `Real Estate`. Links to `nofeeapartments.net`.
- LV Guest List project card: free guest list access for Las Vegas's top nightclubs and dayclubs. Tagged `Social`. Links to `lvguestlist.com`.
- `Real Estate` added as a new filter tag category.

### Changed
- `projects.html` hero stripped down to title and description only: removed the avatar image, "Available for collaboration" badge, and CTA buttons.
- `projects.html` hero description rewritten as a concise rocket pitch: "Finance dashboards, social platforms, educational tools, and a few projects that refuse to take themselves seriously. Every one is live and built to actually be used. Pick a tag and dig in."
- Spacing between the hero description and the Projects section header tightened: hero bottom padding reduced from `3rem` to `1.5rem`; section top padding reduced from `3rem` to `1.5rem`.

---

## [2.4.0] - 2026-06-13

### Added
- `discord.html`: dedicated Discord page listing all four community servers (Azqato, Azqato Invests, B5TA, League of Azqato) as cards with permanent invite links, descriptions, and Discord-blue Join Server buttons.
- `--discord` and `--discord-hover` CSS custom properties on `discord.html`.

### Changed
- Nav Discord link updated from the external `discord.gg` invite URL to `discord.html` across all 11 pages, so visitors browse all servers before choosing one to join.
- Azqato main Discord invite updated from the temporary link (`discord.gg/39JrFNY7qS`) to the permanent invite (`discord.gg/sKGKC3JFSE`) in `index.html` and `links.html`.
- `docs/PRD.md` site structure table updated to include `discord.html`.
- The site now comprises 11 pages.

---

## [2.4.1] - 2026-06-13

### Changed
- Discord server card icons updated: Azqato 🐱, Azqato Invests 💸, B5TA ⚔️ (unchanged), League of Azqato 🖥️.
- `discord.html` hero description rewritten as a general community pitch, removing per-server references in favour of a broader invitation.

---

## [2.5.0] - 2026-06-13

### Changed
- Documentation consolidated from 10 files to 4: `README.md` (root), `docs/PRD.md`, `docs/DESIGN.md`, `docs/PATCHNOTES.md`.
- `docs/TRD.md`, `docs/TENETS.md`, `docs/PRFAQ.md`, `docs/SECURITY.md`, `docs/RUNBOOK.md`, `docs/METRICS.md`, and `docs/ROADMAP.md` removed; all content absorbed into `docs/PRD.md` under dedicated sections.
- `README.md` rewritten as a developer-only reference: removed marketing language, updated file overview to 11 pages, updated nav description to reflect `discord.html` and the `class="active"` pattern, added "Adding a Discord Server" instructions.
- `docs/DESIGN.md` updated: fixed card border-radius to `10px`, hover transform to `translateY(-2px)`, and card gap to `1rem` to match actual implementation; updated `--discord` and `--discord-hover` note to reflect both `index.html` and `discord.html`; added Discord server card component pattern; updated all typography and spacing values to current code.
- `docs/PRD.md` expanded with consolidated Architecture, Tenets, FAQ, Security, Runbook, Metrics, Roadmap, and Documentation Process sections; added F8 (Discord Page) and F10 (Landing Page) to Feature List; updated site structure table to 11 pages; updated Discord server data model with all four permanent invite links; updated project list to 11 current projects.
- Roadmap in `docs/PRD.md` updated: v2.4.0 milestone renamed to "discord.html: four server cards, sitewide nav update" to match what actually shipped; planned code-extraction milestone renumbered to v2.6.0.

### Removed
- `docs/TRD.md`
- `docs/TENETS.md`
- `docs/PRFAQ.md`
- `docs/SECURITY.md`
- `docs/RUNBOOK.md`
- `docs/METRICS.md`
- `docs/ROADMAP.md`

---

## [2.6.0] - 2026-06-14

### Added
- Prompts project card: personal reference library of reusable Claude Code prompts for recurring development, documentation, and maintenance tasks. Zero-dependency, hash-based routing, one-click copy; works offline from any browser. Tagged `Tools` and `Education`. Live at `https://azqato.github.io/prompts/`.

---

## [2.6.1] - 2026-06-15

### Changed
- ComposerAtlas demo link updated from `https://azqato.github.io/ComposerAtlas/` to `https://azqato.github.io/composer` to match the new deployment directory.

---

## [2.6.2] - 2026-06-15

### Added
- "Azqato Projects" resource card added as the first card on `invests.html`, listing all five finance-related projects: Net Worth Tracker, VIX Strategy, ComposerAtlas, Stock Methodology, and Leveraged Strategies.

---

## [2.6.3] - 2026-06-15

### Fixed
- "Azqato's Projects" card title in `invests.html` corrected from "⚡ Azqato Projects".

---

## [2.6.4] - 2026-06-15

### Fixed
- Discord link in the `invests.html` hero paragraph updated from the direct `discord.gg` invite URL to `discord.html`, consistent with the rest of the site.

---

## [2.6.5] - 2026-06-27

### Added
- Azqato's Tools project card: collection of free, browser-based utilities including a Markdown editor with live preview and HTML export, a Favicon Downloader, a Link Cleaner that strips tracking parameters, and a Nasdaq 100 Screener. Tagged `Tools`. Live at `https://azqato.github.io/tools/`.

---

## [2.6.6] - 2026-06-27

### Changed
- "Tools" nav link added to all 11 pages after "Projects", pointing to `https://azqato.github.io/tools/` and opening in the same tab. Nav order is now: Home, About, Discord, Invests, Links, Projects, Tools, YouTube, GitHub, Support.

---

## [2.5.1] - 2026-07-02

### Added
- Twitch Prime affiliate card on `support.html`: explains that Amazon Prime members can use their one free monthly Twitch channel subscription on Azqato's channel at no extra cost. Links to `twitch.tv/azqato`.

---

## [2.5.2] - 2026-07-05

### Fixed
- **Nav bar horizontal overflow between 601px and ~754px on all 11 pages.** The desktop nav (10 links, `gap: 1.5rem`, no wrap) only had a single `display: none` breakpoint at `max-width: 600px`; above that width the full-width link row didn't fit until the viewport reached ~754px, forcing the whole page to overflow horizontally by 51-55px on every page in that range (confirmed via headless Chrome DOM measurement, not screenshots, since `document.documentElement.scrollWidth > clientWidth` in that window). Replaced the abrupt hide-at-600px behavior with a hamburger menu: nav links collapse behind a `.nav-toggle` button below 860px (safe margin above the ~754px content width) and open as a dropdown panel, restoring mobile/tablet navigation that was previously just missing below 600px with no fallback. Implemented identically across all 11 pages (markup, CSS, and a small inline toggle script per page, consistent with the site's no-shared-file architecture).
- **CSS Grid bare `1fr` tracks reverting to unclamped columns on mobile.** `.platform-grid` (`accounts.html`), `.resource-grid` (`invests.html`), `.link-grid` (`links.html`), and `.channel-grid` (`youtube.html`) used `minmax(Npx, 1fr)` at desktop width but their `@media (max-width: 600px)` overrides reverted to a bare `1fr` (or `1fr 1fr`), which has an implicit `min-width: auto` rather than `0`; a card with long unbreakable content could force the grid, and the page, wider than the viewport. Changed the mobile overrides to `minmax(0, 1fr)` (and `repeat(2, minmax(0, 1fr))` for the two-column cases) to match the desktop guard.
- **Redundant spacing from `margin-top` stacked on top of a flex `gap`.** Six elements (`.hero-actions` in `index.html`/`projects.html`, `.pitch-signature` in `about.html`/`support.html`, `.playlist-btn` in `music.html`, `.affiliate-link-btn` in `support.html`) carried their own `margin-top` despite already being spaced by their flex-column parent's `gap`, doubling the intended gap. Removed the redundant margins; parent `gap` now provides the sole spacing.

---

## [2.7.3] - 2026-07-08

### Changed
- Merged two adjacent `html { }` rules in `invests.html` into a single block (`overflow-y: scroll` + `scroll-behavior: smooth`). Cosmetic cleanup only; no behavior change.

---

## [2.7.2] - 2026-07-08

### Changed
- Updated the Leveraged Strategies featured card link on `invests.html` from `https://azqato.github.io/leveraged-strategies/` to `https://azqato.github.io/leverage/`.

---

## [2.7.1] - 2026-07-08

### Fixed
- **Nav logo position shifted slightly between pages.** `.nav-inner` centers itself with `margin: 0 auto` inside a `max-width: 1100px` wrapper, and Windows Chrome/Edge reserve real horizontal space for a vertical scrollbar only when a page's content is tall enough to scroll. Pages that fit within the viewport (`accounts.html`, `codes.html`, `youtube.html`) had no scrollbar and therefore a few pixels more usable width than longer pages, so the centered nav-inner (and the "Azqato" logo inside it) landed at a slightly different horizontal position depending on page length. Added `html { overflow-y: scroll; }` to every page so the scrollbar gutter is always reserved, whether or not the page actually needs to scroll; confirmed via headless Chrome measurement that `.nav-logo`'s `getBoundingClientRect().left` is now identical across all 12 pages at every tested width.

---

## [2.7.0] - 2026-07-08

### Changed
- Site favicon changed from the ⚡ emoji to 🦁 across all 12 pages (inline SVG data-URI favicon, unchanged everywhere else).
- The "About" card icon in the homepage explore grid (`index.html`) changed from 👋 to 🦁 to match the new favicon.

---

## [2.6.10] - 2026-07-08

### Fixed
- Corrected the Azqato Mixes channel link on `youtube.html` to `https://www.youtube.com/@AzqatoMixes` (previously pointed to the wrong channel).

---

## [2.6.9] - 2026-07-08

### Changed
- Reordered the `invests.html` featured project cards so the strategy projects lead: Stocks, Leveraged Strategies, ComposerAtlas, Net Worth Tracker, VIX Strategy, Stock Screener.
- Renamed the "Stock Methodology" featured card to "Stocks" on `invests.html` (link target unchanged: `https://azqato.github.io/stocks/`). The `projects.html` card retains its original name.

---

## [2.6.8] - 2026-07-08

### Added
- `invests.html` redesigned to lead with Azqato's own investing projects. New hero with a primary "Join the Discord" CTA and a secondary "Explore the projects" CTA that smooth-scrolls to the project showcase.
- Featured project showcase: six large clickable cards (Net Worth Tracker, VIX Strategy, ComposerAtlas, Stock Methodology, Stock Screener, Leveraged Strategies), each with a description, hover lift, gradient top-bar, and sliding arrow. Card icons mirror each project's own favicon emoji.
- Stock Screener link (`https://azqato.github.io/stocks/screener.html`) added to the projects list.
- Writing-style guard: a `.githooks/pre-commit` hook that blocks any commit introducing an em dash into an HTML or documentation file, enforcing the no-em-dash policy in the Writing Style section of `docs/PRD.md`. Enabled per clone with `git config core.hooksPath .githooks`.

### Changed
- Curated resource grid moved below the project showcase under a new "Curated Resources" heading; the old text-only "Azqato's Projects" resource card was replaced by the featured cards.

### Fixed
- Removed a stray em dash from a historical patch note entry in `docs/PATCHNOTES.md` (grid-collapse fix description), bringing all documentation into compliance with the no-em-dash policy.

---

## [2.6.7] - 2026-07-05

### Added
- ProteinPulse project card: browser-based calorie and protein tracker with daily logging, customizable goals, a carry-forward model, and weekly and monthly graphs. Fully client-side with Excel import and export. Tagged `Tools` and `Health`. Live at `https://azqato.github.io/protein/`.
- `Health` added as a new filter tag category.

---

<!-- Template for future entries:

## [x.y.z] - YYYY-MM-DD

### Added
-

### Changed
-

### Fixed
-

### Removed
-

-->
