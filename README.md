# Azqato Portfolio

Personal site for Azqato. Eleven self-contained HTML pages, zero dependencies, deployed via GitHub Pages.

**Live site:** https://azqato.github.io/

---

## Tech Stack

| Layer           | Technology      | Version / Notes                          |
|-----------------|-----------------|------------------------------------------|
| Markup          | HTML5           | Semantic elements throughout             |
| Styling         | CSS3            | Custom properties, Grid, Flexbox         |
| Scripting       | JavaScript      | ES6+ (vanilla, no framework)             |
| Hosting         | GitHub Pages    | Deployed from `main` branch root         |

---

## Prerequisites

- Git
- A modern browser (Chrome, Firefox, Edge, or Safari, latest)
- A text editor

No Node.js, no npm, no build tools required.

---

## Installation

```bash
git clone https://github.com/Azqato/Azqato.git
cd Azqato
git config core.hooksPath .githooks   # enable the writing-style pre-commit guard
```

No `npm install`. No compilation step.

The `core.hooksPath` step enables a `pre-commit` hook that blocks commits containing em dashes in HTML or docs, per the no-em-dash policy in [`docs/PRD.md`](docs/PRD.md). Bypass in an emergency with `git commit --no-verify`.

---

## Running Locally

```bash
# Option 1: open index.html directly in any browser (works as a file:// URL)
# Option 2: local server (avoids file:// edge cases on some browsers)
npx serve .            # http://localhost:3000
python -m http.server  # http://localhost:8000
```

No required port. All pages work as file:// URLs with no server.

---

## Environment Variables

None. No server, no build step, no secrets. Affiliate links and Buy Me a Coffee URLs are hardcoded directly in `support.html`.

---

## Build

No build step. Source files are the deployed files.

---

## Deploy

### GitHub Pages (current)

1. Push to `main`.
2. In repository Settings → Pages, set source to `main` branch / `root`.
3. Live at `https://<username>.github.io/` within ~60 seconds.

Routine deploy:

```bash
git add <changed files>
git commit -m "Description of change"
git push origin main
```

### Alternative static hosts

| Host             | Steps                                                       |
|------------------|-------------------------------------------------------------|
| Vercel           | Drag and drop the project folder at vercel.com/new; no build command |
| Netlify          | Drag and drop at app.netlify.com/drop                       |
| Cloudflare Pages | Connect repo; leave build command blank                     |

---

## Adding a Project

Edit the `PROJECTS` array near the bottom of `projects.html`:

```js
{
  name: "My Project",
  desc: "One-sentence description.",
  github: "https://github.com/Azqato/my-project",
  demo: "https://azqato.github.io/my-project/",
  tags: ["Finance"],
  langClass: "lang-js",
  icon: "⚡",
  updated: "2026",
}
```

The card title and ↗ button link to `demo`. The GitHub icon button links to `github`. If no `demo` is set, the title falls back to `github`.

### `langClass` options

| Class       | Language   | Color     |
|-------------|------------|-----------|
| `lang-js`   | JavaScript | `#e8c840` |
| `lang-ts`   | TypeScript | `#3178c6` |
| `lang-py`   | Python     | `#3572a5` |
| `lang-cs`   | C#         | `#178600` |
| `lang-html` | HTML       | `#e34c26` |
| `lang-css`  | CSS        | `#563d7c` |
| `lang-go`   | Go         | `#00add8` |
| `lang-rust` | Rust       | `#dea584` |
| `lang-java` | Java       | `#b07219` |

---

## Adding a Discord Server

Edit `discord.html` directly. Each server is a static `.server-card` block. Copy an existing card, update the icon, name, description, and `href` on the `.btn-join` anchor.

---

## File Overview

```
.
├── index.html           - landing page: intro, Discord CTA, explore grid
├── projects.html        - project grid: cards, tag filter, hero
├── about.html           - bio and personal pitch
├── discord.html         - Discord server directory: four community servers
├── support.html         - Buy Me a Coffee CTA + affiliate partners grid
├── links.html           - all social/platform links by category
├── youtube.html         - four YouTube channels
├── invests.html         - investing projects showcase + curated resource hub
├── music.html           - Spotify playlists + music platform links
├── accounts.html        - gaming accounts (Steam, LoL, TFT, RuneScape)
├── privacy-policy.html  - full privacy policy
├── img/                 - image assets (profile photos, YT thumbnails, covers)
├── .githooks/           - pre-commit writing-style guard (enable via core.hooksPath)
├── README.md            - this file
└── docs/
    ├── PRD.md           - product requirements and all project documentation
    ├── DESIGN.md        - design system and visual tokens
    └── PATCHNOTES.md    - versioned changelog
```

---

## Navigation

All 11 pages share the same sticky nav: **Home, About, Discord, Invests, Links, Projects, Tools, YouTube, GitHub, Support**. The Discord nav link points to `discord.html`. The Tools nav link points to `https://azqato.github.io/tools/`. The GitHub nav link opens `github.com/Azqato` in the same tab. Nav collapses on viewports under 600 px. The active page link has `class="active"` set directly in the HTML; there is no JS routing.

When updating the nav, edit it consistently across all 11 HTML files. There is no shared include yet; see the Roadmap in `docs/PRD.md` for the planned shared-asset extraction milestone.

---

## Documentation

See [/docs/](docs/) for full documentation: PRD (requirements + architecture + runbook + all reference material), design system, and patch notes.
