---
title: Consolidate Documents
description: Read all project source files, then consolidate all documentation into four core files and enforce the correct folder structure.
meta: Claude Code Prompt
---

Reads every source file, config, and existing doc in a project, then consolidates all documentation into four core files: README.md at the root, and PRD.md, DESIGN.md, and PATCHNOTES.md inside `/docs`. Creates any missing files populated with the required sections. Moves misplaced files into the correct locations.

Use it when a project has scattered or excessive documentation and needs to be trimmed to a clean, maintainable core set. A leaner alternative to the Documentation Audit prompt, which targets an eleven-document suite.

## Prompt

```
Perform a full documentation audit for this project. Read all existing source files, configs, and any current documentation to understand what is being built. Then do the following:

1) Consolidate all of the files in docs into 4 main documents: README.md, /docs/PRD.md, /docs/DESIGN.md, /docs/PATCHNOTES.md

2) Create any missing documentation files and populate them accordingly.

3) Enforce the following folder structure:

   /project-root
   ├── README.md          ← Important: README.MD is always root only, never inside /docs
   └── /docs
       ├── PRD.md
       ├── DESIGN.md
       └── PATCHNOTES.md

   If any of these files exist outside of /docs (except README.md), move them into
   /docs. If /docs does not exist, create it.

---
README.md - The front door. First thing anyone sees. Explains what the project is and how to use it.
PRD.md - What you're building and who it's for. Written before any code starts. This file should contain sections consolidating all of the documentation files you are removing from this audit.
DESIGN.md - How it looks. Colors, fonts, spacing, and UI rules to stay consistent.
PATCHNOTES.md - A running log of every change made, with dates and reasons why.
---

### README.md (root)
Required sections:
- Project name and one-sentence description
- Link to the currently live site (ex: https://azqato.github.io/)
- Tech stack list with versions
- Prerequisites (Node version, package manager, environment requirements)
- Installation steps (exact commands, in order)
- How to run locally (dev server command, default port)
- Environment variable reference (key names, what each does, whether required or optional)
- Build and deploy instructions
- Link to /docs for full documentation

Do not include marketing language. README is for developers, not end users.

---

### /docs/PRD.md
Required sections:
- Problem statement: what problem does this product solve and for whom
- Target users: specific personas with context on their needs
- Goals: what success looks like for this product
- Non-goals: explicit list of what this product will not do
- User stories: written as "As a [user], I want to [action] so that [outcome]"
- Feature list: split into MVP (must ship) and Future (post-launch)
- Constraints: technical, time, budget, or platform limitations
- Assumptions: decisions made without full information that the team accepts as true
- Success criteria: measurable outcomes that confirm the product is working
In addition to all of the above, PRD.md should have a section detailing each of the consolidated documents and contain all of the information that was in them.

---

### /docs/DESIGN.md
Required sections:
- Design philosophy: 1-3 sentences on the visual and UX direction
- Color palette: every color token with hex value and intended use
- Typography: font families, sizes, weights, and line heights for each text role
  (heading 1-3, body, caption, label, code)
- Spacing system: the spacing scale used (e.g. 4px base unit)
- Breakpoints: every responsive breakpoint and what changes at each
- Component patterns: rules for how recurring UI elements (buttons, cards, forms,
  modals) should be built and styled
- Accessibility standards: WCAG level targeted, contrast requirements, keyboard
  navigation expectations
- Animation and motion: timing, easing, and rules for when motion is appropriate

---

### /docs/PATCHNOTES.md
Required format per entry:
- Version number using semantic versioning (MAJOR.MINOR.PATCH)
- Date in YYYY-MM-DD format
- Sections: Added, Changed, Fixed, Removed
- Each line item is one change, written in past tense

If no prior changelog exists, create an initial entry for the current state of
the project labeled as v0.1.0 or the nearest appropriate version.

---

After everything is updated, add these recent changes to PATCHNOTES.md and describe this process and how everything should be handled moving forward in PRD.md
```
