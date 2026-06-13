# Azqato's Portfolio

A self-contained, zero-dependency personal site for Azqato. It opens with an introductory landing page and routes visitors to a project showcase plus hubs for content, music, investing, and community. Built with plain HTML, CSS, and vanilla JavaScript. No build tools, no frameworks, no npm.

**Live site:** https://azqato.github.io/

---

## Tech Stack

| Layer      | Technology          | Version / Notes              |
|------------|---------------------|------------------------------|
| Markup     | HTML5               | Semantic elements throughout |
| Styling    | CSS3                | Custom properties, Grid, Flexbox |
| Scripting  | JavaScript          | ES6+ (vanilla, no framework) |
| Hosting    | GitHub Pages        | Deployed from `main` branch root |

---

## Prerequisites

No build tools, package managers, or runtimes required. All you need is:

- A modern browser (Chrome, Firefox, Edge, or Safari, latest version)
- A text editor to modify project data

---

## Installation

```bash
git clone https://github.com/Azqato/Azqato.git
cd Azqato
```

That's it. No `npm install`, no compilation step.

---

## Running Locally

Open `index.html` directly in a browser:

```
# Option 1: double-click index.html in your file manager
# Option 2: drag index.html into a browser window
# Option 3: use a local server (any will work)
npx serve .          # serves at http://localhost:3000
python -m http.server # serves at http://localhost:8000
```

Default port depends on which local server you choose (see above). No port is required; the files work as file:// URLs.

---

## Adding a Project

Edit the `PROJECTS` array near the bottom of `projects.html`:

```js
{
  name: "My Project",
  desc: "A short description of what this project does.",
  github: "https://github.com/Azqato/my-project",  // repo link (GitHub icon button)
  demo: "https://azqato.github.io/my-project/",    // live site (card title + ↗ button)
  tags: ["Finance"],      // keep tags to high-level categories (Finance, Social, Tools)
  langClass: "lang-js",   // drives the language tag color
  icon: "⚡",             // optional emoji
  iconUrl: "https://…/favicon.svg", // optional image/SVG URL; overrides icon when set
  stars: "42",            // optional star count
  updated: "Jun 2025",    // optional last-updated label
}
```

**Card link behavior:** the project title and ↗ button open the `demo` URL. The GitHub icon button opens the `github` repo URL. If no `demo` is set, the title falls back to the `github` URL.

### `langClass` options

| Class       | Language   | Color    |
|-------------|------------|----------|
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

## Environment Variables

None. This project has no server, no build step, and no secrets. There are no `.env` files and nothing to configure.

Affiliate links and Buy Me a Coffee URLs are hardcoded directly in `support.html`.

---

## Favicon

The ⚡ emoji favicon is defined as an inline SVG data URI in the `<head>`. No image file required. To change it, replace the emoji in this line in each HTML file:

```html
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚡</text></svg>" />
```

---

## Customizing the Theme

All design tokens are CSS custom properties in `:root` at the top of each file's `<style>` block. Change `--accent`, `--bg`, `--surface`, etc. to retheme instantly. See [/docs/DESIGN.md](docs/DESIGN.md) for the full token reference.

---

## Build

There is no build step. The source files are the deployed files.

---

## Deploy

### GitHub Pages (current)
1. Push to the `main` branch.
2. In repository Settings → Pages, set source to `main` branch / `root`.
3. The site is live at `https://<username>.github.io/` within ~60 seconds.

### Other static hosts
- **Vercel / Netlify:** drag and drop the project folder; no build command needed.
- **Cloudflare Pages:** connect the repo; leave build command blank.
- **Any static host:** upload all `.html` files and the `docs/` folder.

---

## File Overview

```
.
├── index.html          - introductory landing page: intro, Discord CTA, explore grid
├── projects.html       - project grid: cards, tag filter, hero
├── about.html          - about page: bio, role, and personal pitch
├── support.html        - support page: Buy Me a Coffee CTA + affiliate partners grid
├── links.html          - links hub: all social/platform links by category
├── youtube.html        - YouTube channels page
├── invests.html        - curated investing resource hub
├── music.html          - Spotify playlists + music platform links
├── accounts.html       - gaming accounts (Steam, LoL, TFT, RuneScape)
├── privacy-policy.html - full privacy policy
├── img/                - image assets (profile photos, YT thumbnails, playlist covers)
├── README.md           - this file
└── docs/
    ├── PRD.md       - product requirements document
    ├── TRD.md       - technical reference document
    ├── DESIGN.md    - design system and visual tokens
    ├── PATCHNOTES.md - version history / changelog
    ├── PRFAQ.md     - press release and FAQ
    ├── TENETS.md    - product principles
    ├── METRICS.md   - success metrics and targets
    ├── ROADMAP.md   - milestones and planned features
    ├── SECURITY.md  - security model and considerations
    └── RUNBOOK.md   - operational runbook
```

---

## Navigation

Every page shares the same sticky nav, in this order: **Home, About, Discord, Invests, Links, Projects, YouTube, GitHub, Support**. The logo links to the landing page (`index.html`). The Discord link (`discord.gg/39JrFNY7qS`) and the GitHub link both open in the same tab. The nav collapses on viewports under 600 px. When updating the nav, edit it consistently across all 10 HTML pages (there is no shared include yet; see the code-extraction milestone in [ROADMAP.md](docs/ROADMAP.md)).

---

## Full Documentation

See [/docs/](docs/) for the complete documentation set.
