# Patch Notes

All notable changes to the Azqato Portfolio are documented here.
Format: `[version] — YYYY-MM-DD`

---

## [1.0.0] — 2026-06-06

### Added
- Initial release of the portfolio site.
- Self-contained `index.html` with zero external dependencies.
- Project card grid with icon, name, description, tags, GitHub link, optional demo link, star count, and last-updated fields.
- Tag filter bar — auto-generated from the `PROJECTS` array; filters the grid in real time.
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

## [1.1.0] — 2026-06-06

### Added
- Three live projects populated from their READMEs: Net Worth Tracker, VIX Strategy, and Lantern.

### Changed
- Project card title now links to the live GitHub Pages site (`demo` URL) instead of the GitHub repository, making the primary action open the running app.
- GitHub repository link retained as a separate icon button on each card alongside the live-site (↗) button.

---

## [1.2.0] — 2026-06-06

### Changed
- Project tags simplified to category-only labels: Net Worth Tracker and VIX Strategy tagged `Finance`; Lantern tagged `Social`. Removed tech-stack tags (JavaScript, Chart.js, Dashboard, Privacy, Tailwind CSS) from the filter bar.
- Nav "Projects" link replaced with "Index", pointing to `https://azqato.github.io/`.
- Removed "Browse Projects" secondary CTA button from the hero section.

---

## [1.2.1] — 2026-06-06

### Changed
- README title updated from "Azqato Portfolio" to "Azqato's Portfolio".
- Added live site link (`https://azqato.github.io/`) directly below the README title.

---

## [1.2.2] — 2026-06-06

### Added
- ⚡ emoji favicon added to all pages via inline SVG data URI — no external image file required.

---

## [1.3.0] — 2026-06-07

### Added
- `support.html` — dedicated support page with a personal pitch, Buy Me a Coffee CTA (buymeacoffee.com/azqato), and an affiliate partners grid (6 placeholder cards: Tesla, Robinhood, M1 Finance, Webull, Coinbase, Public).
- "Support" nav link added to `index.html` pointing to `support.html`.
- "Support" nav link on `support.html` highlights as active to signal current page.
- Affiliate card design: square logo area, promo badge, description, and CTA button.
- Pitch card on support page with gradient top border, avatar, bio, and signature pulled from the buymeacoffee About section.

---

## [1.3.1] — 2026-06-07

### Changed
- Buy Me a Coffee CTA section moved above the About Azqato pitch card so the support ask is the first thing visitors see after the hero.
- CTA paragraph replaced with the full buymeacoffee disclaimer: investment intent statement and fund-use caveat.
- Removed the "Opens buymeacoffee.com/azqato, One-time or monthly, 100% goes to the journey" sub-line from the CTA.
- Removed duplicate investment paragraph from the pitch card body since it now lives in the CTA above.
- All em dashes replaced with commas across `support.html` for improved readability.

---

## [1.3.2] — 2026-06-07

### Changed
- CTA disclaimer paragraph left-aligned for improved readability, while the emoji, heading, and button remain centered.

---

## [1.4.0] — 2026-06-07

### Added
- `about.html` — dedicated About page with hero section and the Azqato pitch card (bio, role line, signature).
- "About" nav link added to all pages pointing to `about.html`, with active state highlighted on `about.html`.
- `.nav-links a.active` CSS rule added to `index.html` to support active nav highlighting.

### Changed
- Nav standardised across all pages: Portfolio, About, GitHub, Support. "Index" (external azqato.github.io link) replaced with "Portfolio" (relative `index.html` link) on all pages.
- About Azqato pitch card moved from `support.html` to `about.html`. `support.html` now focuses solely on the Buy Me a Coffee CTA and affiliate partners.
- Footer simplified to "Built by Azqato" across all pages, removing the redundant GitHub link from footer text.

---

## [1.4.1] — 2026-06-07

### Changed
- About page bio expanded with full background story: gaming origins, Twitch and YouTube content creation, B5TA community on RuneScape and Discord, web development work, and closing call to join the journey.
- Role line updated from "Investor, Developer, Community Builder" to "Content Creator, Web Developer, Community Leader" to better reflect the full bio.
- Em dash removed from closing paragraph ("adventure, one built on...").

---

## [1.5.0] — 2026-06-07

### Added
- Clan B5TA project card: community website for the RuneScape clan founded in 2014, tagged `Social` and `Gaming`, linking to the live GitHub Pages site and repo.
- `Gaming` added as a new filter tag category.

---

## [1.5.1] — 2026-06-07

### Changed
- Clan B5TA tag simplified from `Social, Gaming` to `Social` only. `Gaming` filter category removed; current categories are `Finance` and `Social`.

---

## [1.6.0] — 2026-06-07

### Added
- Cat Food Center project card: mobile-first PWA for evaluating cat food via barcode scan or search, tagged `Tools`, linking to the live GitHub Pages site and repo.
- `Tools` added as a new filter tag category.

### Changed
- Net Worth Tracker tagged with `Tools` in addition to `Finance`.

---

## [1.6.1] — 2026-06-07

### Changed
- Cat Food Center icon updated from 🐱 emoji to the project's own `favicon.svg` via the new `iconUrl` field.

### Added
- `iconUrl` optional field on project entries: accepts a URL to an image or SVG and takes precedence over `icon` when set.

---

## [1.7.0] — 2026-06-07

### Changed
- Public affiliate card: real referral link added (`share.public.com/azqato`), promo updated to "Free $20", description updated to match.
- Robinhood affiliate card: real referral link added (`join.robinhood.com/robertg273/`), promo updated to "Free $5–$200 Stock", description updated to match.
- M1 Finance affiliate card: real referral link added (`m1.finance/BVZBG3OqOfMj`), promo updated to "Free $75 Bonus", description updated to reflect $10,000 funding requirement and M1 Premium benefit.
- Affiliate section note updated from "Placeholder links" to "Some links are live, others are coming soon."

---

## [1.7.1] — 2026-06-07

### Changed
- Tesla affiliate card: real referral link added (`ts.la/robert459550`), promo updated to "Free 3 Months FSD", description updated to reflect 3 months of Full Self-Driving or $400 off Solar or Powerwall.

---

## [1.7.2] — 2026-06-07

### Changed
- M1 Finance affiliate card description updated to exact wording specified.

---

## [1.7.3] — 2026-06-07

### Changed
- Affiliate section note replaced with a plain-English disclaimer explaining how referral links work.

### Removed
- Webull and Coinbase placeholder cards removed from the affiliate grid.

---

## [1.7.4] — 2026-06-07

### Added
- Lyft affiliate card: 50% off first ride up to $10 (`lyft.com/invite/ROBGOLDY630855`).

---

## [1.8.0] — 2026-06-08

### Added
- `/docs/` directory created to house all project documentation.
- `docs/TRD.md` — Technical Reference Document covering system architecture, tech stack, data models, internal data flow, state management, third-party integrations, performance requirements, and known technical debt.
- `docs/DESIGN.md` — Design system document covering color palette (all CSS custom properties), typography, spacing, breakpoints, component patterns, accessibility standards, and motion rules.
- `docs/PRFAQ.md` — Press release and FAQ (internal and external).
- `docs/TENETS.md` — Product principles with 5 prioritized tenets.
- `docs/METRICS.md` — Success metrics, targets, measurement methods, and reporting cadence.
- `docs/ROADMAP.md` — Milestone table with current phase, planned features, and deferred items.
- `docs/SECURITY.md` — Security model covering auth, data storage, third-party trust, attack surface, and dependency policy.
- `docs/RUNBOOK.md` — Operational runbook with local setup, build, deploy, rollback, environment configs, common errors, and monitoring.

### Changed
- `PRD.md` moved from project root to `docs/PRD.md` and expanded with problem statement, target user personas, assumptions, and measurable success criteria.
- `PATCHNOTES.md` moved from project root to `docs/PATCHNOTES.md`.
- `README.md` updated with tech stack table, prerequisites section, environment variable reference (none), expanded deploy instructions, link to `/docs/`, and updated file overview reflecting the new `docs/` structure.

### Removed
- `PRD.md` from project root (moved to `docs/PRD.md`).
- `PATCHNOTES.md` from project root (moved to `docs/PATCHNOTES.md`).

## [1.9.0] — 2026-06-08

### Added
- ComposerAtlas project card: curated strategy library and education hub for Composer.trade investing, featuring strategy pages with plain-English logic breakdowns, risk profiles, metrics tables, and a glossary of systematic investing concepts. Tagged `Finance` and `Tools`.

## [1.9.1] — 2026-06-08

### Changed
- ComposerAtlas and Cat Food Center tagged with `Education` to reflect their educational content.
- `Education` added as a new filter tag category.

---

## [1.9.2] — 2026-06-09

### Changed
- Buy Me a Coffee CTA paragraph split: main text ends with `*` asterisk; disclaimer moved below the button in smaller italic text.

---

## [1.9.3] — 2026-06-09

### Added
- Boaty McBoatface Ventures project card: humorous marketing site for a fictional New England canvas exo-skeleton water displacement company, tagged `Meme`.
- `Meme` added as a new filter tag category.

---

## [2.0.0] — 2026-06-09

### Added
- `links.html` — Social and platform links hub, organized into sections: Community & Streaming, YouTube, Music, Social, Investing, and More. All external links from the old website consolidated here.
- `youtube.html` — YouTube channels page showcasing all four channels (Azqato, Azqato Streams, Azqato Mixes, Azqato Chills) as cards with thumbnail photos, channel descriptions, and subscribe buttons.
- `invests.html` — Azqato Invests resource hub with 14 curated sections: Platforms, Careers, ETFs, Companies, Ratings, Screeners, Real Estate, Charts, Databases, Economic Indicators, Education, Guides, Indices, Information, and News.
- `music.html` — Music page featuring the two Spotify playlists (BANGERS, ADDICTIONS) with cover art, plus links to Last.fm, Mixcloud, and YouTube Mixes.
- `accounts.html` — Gaming accounts page listing Azqato's profiles across Steam, League of Legends, Teamfight Tactics, and RuneScape.
- `privacy-policy.html` — Full privacy policy page covering Consent, Information Collection, Log Files, Cookies, DART Cookies, CCPA, GDPR, Children's Information, Affiliate Links, Financial Disclaimer, and Entertainment Purposes.
- `img/` directory with 14 image assets migrated from the old website: profile photos (`home-hero-profile.jpg`, `about-profile.jpg`, `logo-cat-avatar.jpg`), YouTube channel thumbnails (`yt-thumb-azqato.jpg`, `yt-thumb-streams.jpg`, `yt-thumb-mixes.jpg`, `yt-thumb-chills.jpg`), larger channel images (`yt-channel-*.jpg`), Spotify playlist covers (`music-playlist-bangers.jpg`, `music-playlist-addictions.jpg`), and music logo (`music-logo-small.jpg`).
- Profile photo (`home-hero-profile.jpg`) added to the `index.html` hero section as an 80px circular avatar.
- "All Links →" secondary CTA button added to the `index.html` hero actions, pointing to `links.html`.
- Profile photo (`about-profile.jpg`) added to the `about.html` pitch card avatar, replacing the ⚡ emoji.
- `Links`, `YouTube`, and `Invests` nav links added to all pages.
- Privacy Policy footer link added to all pages.

### Changed
- `index.html` hero description expanded to mention content creation, gaming, investing, music production, and streaming — preserving the intro text from the old website's landing page.
- Nav expanded from 4 links (Portfolio, About, GitHub, Support) to 7 links (Portfolio, About, Links, YouTube, Invests, GitHub, Support) across all pages.
- Footer on all pages updated from "Built by Azqato" to include a "Privacy Policy" link.
- `about.html` pitch avatar size increased from 60px to 72px to better display the profile photo.

### Removed
- `oldwebsite/` directory and all its contents deleted after full content migration.

---

## [2.0.1] — 2026-06-09

### Changed
- League of Legends accounts on `accounts.html` updated to Riot ID format: `Chief Rocka` → `서주프#zoop` and `Azqato` → `Azqato#zoop`.
- Both LoL op.gg links updated to the new URL format (`op.gg/lol/summoners/na/`).

---

## [2.0.2] — 2026-06-09

### Changed
- TFT accounts on `accounts.html` updated to metatft.com with Riot ID format: `서주프#zoop` and `Azqato#zoop`. Links updated from lolchess.gg to `metatft.com/player/na/`.
- RuneScape accounts updated: `Hctibaru` replaced with `ironqato`; both links updated from runeclan.com to runepixels.com (`/players/<name>/skills`).

---

## [2.0.3] — 2026-06-09

### Changed
- Privacy Policy link moved from all page footers to the More section on `links.html` as a button.
- Footers across all 9 pages simplified back to "Built by Azqato" only.

---

## [2.0.4] — 2026-06-09

### Changed
- Footer byline updated to "Built by Azqato." on all pages — period is outside the link element so it renders in `--text-muted` rather than the accent green.

---

## [2.1.0] — 2026-06-10

### Added
- Stock Methodology project card: educational site documenting a fundamentals-driven individual stock and ETF investing methodology, covering 10 evaluation metrics (PEG, P/E FWD, RSI, revenue/EPS growth, cash/debt, 52W range), a Finviz screener guide, Seeking Alpha watchlist setup, and VIX-based index investing strategies. Tagged `Finance` and `Education`.

---

## [2.1.1] — 2026-06-10

### Changed
- All links to the GitHub profile (`github.com/Azqato`) now open in the same tab. Removed `target="_blank" rel="noopener"` from all 20 occurrences across 9 pages (nav links, footer bylines, hero CTA, and links page button).

---

<!-- Template for future entries:

## [x.y.z] — YYYY-MM-DD

### Added
-

### Changed
-

### Fixed
-

### Removed
-

-->
