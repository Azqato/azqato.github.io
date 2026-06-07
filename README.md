# Azqato Portfolio

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
  tags: ["JavaScript", "CLI"],
  langClass: "lang-js",   // drives the tag color
  icon: "⚡",             // optional emoji
  stars: "42",            // optional star count
  updated: "Jun 2025",    // optional last-updated label
}
```

**Card link behaviour:** the project title and ↗ button open the `demo` URL (the live GitHub Pages site). The GitHub icon button opens the `github` repo URL. If no `demo` is set, the title falls back to the `github` URL.

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
├── index.html       — the entire site (self-contained)
├── README.md        — this file
├── PRD.md           — product requirements document
└── PATCHNOTES.md    — version history / changelog
```
