# Azqato's Portfolio

**Live site:** https://azqato.github.io/

A self-contained, zero-dependency portfolio site for displaying GitHub projects. Built with plain HTML, CSS, and JavaScript — no build tools, no frameworks, no npm.

## Getting Started

Open `index.html` in any browser. That's it.

## Adding a Project

Edit the `PROJECTS` array near the bottom of `index.html`:

```js
{
  name: "My Project",
  desc: "A short description of what this project does.",
  github: "https://github.com/Azqato/my-project",  // repo link (GitHub icon button)
  demo: "https://azqato.github.io/my-project/",    // live site (card title + ↗ button)
  tags: ["Finance"],      // keep tags to high-level categories (e.g. Finance, Social)
  langClass: "lang-js",   // drives the tag color
  icon: "⚡",             // optional emoji
  stars: "42",            // optional star count
  updated: "Jun 2025",    // optional last-updated label
}
```

**Card link behaviour:** the project title and ↗ button open the `demo` URL (the live GitHub Pages site). The GitHub icon button opens the `github` repo URL. If no `demo` is set, the title falls back to the `github` URL.

**Tags:** use broad category labels rather than tech-stack specifics so the filter bar stays clean. Current categories: `Finance`, `Social`, `Tools`.

### `langClass` options

| Class       | Language   |
|-------------|------------|
| `lang-js`   | JavaScript |
| `lang-ts`   | TypeScript |
| `lang-py`   | Python     |
| `lang-cs`   | C#         |
| `lang-html` | HTML       |
| `lang-css`  | CSS        |
| `lang-go`   | Go         |
| `lang-rust` | Rust       |
| `lang-java` | Java       |

## Favicon

The site uses a ⚡ emoji favicon defined as an inline SVG data URI in the `<head>` — no image file needed. To change it, replace the emoji in this line in `index.html`:

```html
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚡</text></svg>" />
```

Add the same line to any future pages to keep the favicon consistent.

## Customizing

All design tokens live in `:root` at the top of the `<style>` block in `index.html`. Change `--accent`, `--bg`, `--surface`, etc. to retheme instantly.

To update the hero text, name, or GitHub profile link, edit the `<!-- HERO -->` section in `index.html` and the `<!-- NAV -->` links.

## Deployment

Drop `index.html` into any static host:

- **GitHub Pages** — push to a repo, enable Pages from Settings → Pages → `main` branch / `root`.
- **Vercel / Netlify** — drag-and-drop the folder.
- **Cloudflare Pages** — connect the repo, no build command needed.

## File Overview

```
.
├── index.html       — portfolio / project grid
├── about.html       — about page: bio, role, and personal pitch
├── support.html     — support page: Buy Me a Coffee CTA + affiliate partners grid
├── README.md        — this file
├── PRD.md           — product requirements document
└── PATCHNOTES.md    — version history / changelog
```
