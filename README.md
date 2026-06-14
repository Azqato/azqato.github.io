# Azqato's Prompts

A static personal library of reusable Claude Code prompts. Built as a personal reference tool and organized knowledge base for prompt patterns that solve recurring development, documentation, and maintenance tasks.

Live site: [azqato.github.io/prompts](https://azqato.github.io/prompts/)

---

## What This Is

This site collects prompts that can be dropped directly into Claude Code. Each prompt is written as its own markdown file in `prompts/`, with a title, a plain-language description of what it does, and the full prompt text. The site reads those markdown files and renders a dedicated page for each one with a one-click copy button.

No frameworks, no build tools, no dependencies. Pure HTML, CSS, and vanilla JavaScript. It runs by opening `index.html` directly in a browser (no server required).

---

## How It Works

Prompts live as markdown files, not as hand-written HTML pages. There is one shared `index.html` shell. It uses hash-based routing (`index.html#/em-dash-audit`) to show either the home list or a single prompt.

Browsers block `fetch()` of local files when a page is opened from disk (`file://`), so the prompt markdown is also embedded in `prompts-data.js`, which the browser loads with a normal `<script>` tag. This is what lets the site run with no server and no dependencies. The `.md` files in `prompts/` remain the readable, editable source; `prompts-data.js` mirrors them.

---

## Files

| File | Description |
| --- | --- |
| `index.html` | Single-page shell: sidebar, content area, footer. Renders all views. |
| `prompts-data.js` | Embedded copy of every prompt markdown file, loaded via `<script>` so the site works offline and on `file://`. |
| `script.js` | Parses the embedded markdown, builds the sidebar, handles routing and copy-to-clipboard. |
| `style.css` | Full design system stylesheet shared across all views. |
| `prompts/em-dash-audit.md` | Em dash audit prompt: find and replace em dashes in all forms across all project files. |
| `prompts/documentation-audit.md` | Documentation audit prompt: create or update the full documentation suite for any project. |

---

## Docs

| File | Description |
| --- | --- |
| `docs/PRD.md` | Product requirements, scope, writing style rules, and content philosophy |
| `docs/DESIGN.md` | Full design specification including color tokens, typography, layout, and components |
| `docs/PATCHNOTES.md` | Changelog updated after every meaningful change to the site |

---

## File Structure

```
prompts/
├── index.html
├── prompts-data.js
├── style.css
├── script.js
├── README.md
├── prompts/
│   ├── em-dash-audit.md
│   └── documentation-audit.md
└── docs/
    ├── PRD.md
    ├── DESIGN.md
    └── PATCHNOTES.md
```

---

## Prompt Markdown Format

Each file in `prompts/` follows this structure:

```markdown
---
title: Em Dash Audit
description: One-line summary shown in the home list.
meta: Claude Code Prompt
---

A paragraph (or more) describing what the prompt does and when to use it.

## Prompt

​```
The full prompt text goes here, inside a fenced code block.
​```
```

The frontmatter supplies the title, the home-list description, and the small meta label. Everything between the frontmatter and the `## Prompt` heading becomes the on-page description. The first fenced code block is the copyable prompt.

---

## Design

- GitHub Dark-inspired palette. Teal accent `#00d4a0`, background `#0d1117`, surface `#161b22`
- System fonts only, no external font loading
- CSS Grid sidebar layout with sticky positioning on desktop
- Responsive: sidebar collapses to sticky top nav below 1024px
- Full design specification in `docs/DESIGN.md`

---

## Running Locally

No build step and no server required. Open `index.html` directly in a browser. It also works unchanged when hosted on GitHub Pages.

---

## Adding a New Prompt

1. Create a new `.md` file in `prompts/` (e.g. `prompts/my-prompt.md`) using the markdown format above
2. Add its content to `prompts-data.js` so the browser can load it without a server, and add its slug to the display-order list in that file
3. Add a row to the Files table in this README if needed
4. Update `docs/PATCHNOTES.md` with a new version entry

---

## Content Philosophy

Every prompt page contains exactly three things: a title, a description of what the prompt does, and the prompt itself. Descriptions are written in plain language. No marketing copy, no filler. The goal is to find a prompt, understand it in one read, and copy it immediately.

---

## Author

**Azqato**, [azqato.github.io](https://azqato.github.io)
