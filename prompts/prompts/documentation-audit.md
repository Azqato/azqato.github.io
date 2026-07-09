---
title: Documentation Audit
description: Read all project source files, then create or update the full set of documentation in the correct folder structure.
meta: Claude Code Prompt
hidden: true
---

Reads every source file, config, and existing doc in a project, then writes or rewrites the complete documentation suite. Covers ten documents: README, PRD, TRD, DESIGN, PATCHNOTES, PRFAQ, TENETS, METRICS, ROADMAP, SECURITY, and RUNBOOK. Each document is written to a required spec with the sections listed in the prompt.

Use it when starting a new project, when documentation has drifted from the current codebase, or when a project needs to go from scattered notes to a full structured doc set in one pass. The prompt also enforces the correct folder structure, moving any misplaced files into `/docs`.

## Prompt

```
Perform a full documentation audit on this project. Read all existing source files,
configs, and any current documentation to understand what is being built. Then do
the following:

1. Update every existing documentation file to reflect the actual current state of
   the project: do not leave placeholder text if the real information is available
   in the codebase.

2. Create any missing documentation files from the list below.

3. Enforce the following folder structure:

   /project-root
   ├── README.md          ← Important: README.MD is always root only, never inside /docs
   └── /docs
       ├── PRD.md
       ├── TRD.md
       ├── DESIGN.md
       ├── PATCHNOTES.md
       ├── PRFAQ.md
       ├── TENETS.md
       ├── METRICS.md
       ├── ROADMAP.md
       ├── SECURITY.md
       └── RUNBOOK.md

   If any of these files exist outside of /docs (except README.md), move them into
   /docs. If /docs does not exist, create it.

---
README.md - The front door. First thing anyone sees. Explains what the project is and how to use it.
PRD.md - What you're building and who it's for. Written before any code starts.
TRD.md - How you're building it. Languages, frameworks, and technical decisions.
DESIGN.md - How it looks. Colors, fonts, spacing, and UI rules to stay consistent.
PATCHNOTES.md - A running log of every change made, with dates and reasons why.
PRFAQ.md - A fake launch announcement written before you build anything. Forces clarity on the value upfront.
TENETS.md - Short guiding principles that help you make decisions when options feel equal.
METRICS.md - Defines what success looks like in numbers before you launch.
ROADMAP.md - What gets built and in what order. Keeps you focused and on track.
SECURITY.md - How the app protects users and their data. Documents access rules and known risks.
RUNBOOK.md - Step-by-step instructions for deploying, rolling back, or fixing common problems.
---

## Document Specifications

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

---

### /docs/TRD.md
Required sections:
- System architecture: describe how the system is structured at a high level
  (client/server, serverless, static, etc.)
- Tech stack: every language, framework, library, and tool used with versions
- Folder structure: annotated tree of the project directory
- Data models: every major data type, its fields, types, and relationships
- API design: all endpoints or functions, their inputs, outputs, and error states.
  If browser-only, document the internal data flow instead.
- State management: how application state is managed and where it lives
- Third-party integrations: every external API or service used, what it does,
  and how it is authenticated
- Performance requirements: target load times, bundle size limits, rendering targets
- Known technical debt: any shortcuts taken with a note on what the correct
  solution would be

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

### /docs/PRFAQ.md
Required sections:
- Press release: written as if the product has just launched publicly. Include
  product name, what it does, who it is for, the key benefit, and a mock quote
  from a fictional user. Written for a general audience, no jargon.
- Internal FAQ: 5-10 questions a team member or stakeholder would ask.
  Cover scope, tradeoffs, risks, and what assumptions must be true for this
  to succeed.
- External FAQ: 5-10 questions a real user would ask. Cover how it works,
  what it costs, what data it uses, and what it does not do.

---

### /docs/TENETS.md
Required format:
- 3-7 tenets maximum. More than 7 dilutes the value.
- Each tenet has a short title (3-5 words) and a 2-4 sentence explanation.
- Tenets must be opinionated enough to resolve a real product tradeoff.
  A tenet that everyone agrees with without hesitation is not useful.
- Order them by priority. When two tenets conflict, the higher one wins.

---

### /docs/METRICS.md
Required sections:
- North star metric: the single number that best represents if the product
  is delivering value
- Acquisition metrics: how users find and start using the product
- Engagement metrics: how users interact with the product over time
- Retention metrics: whether users come back
- Performance metrics: technical health indicators (load time, error rate,
  uptime)
- Targets: a specific goal value for each metric and a timeframe
- Measurement method: what tool or method captures each metric
- Reporting cadence: how often each metric is reviewed

---

### /docs/ROADMAP.md
Required sections:
- Current phase: name and brief description of where the product is now
- Milestone table: each milestone has a name, target date or relative
  timeframe, and a status (Planned, In Progress, Complete, Blocked)
- Feature breakdown per milestone: bullet list of what ships in each phase
- Explicitly deferred items: features considered but intentionally pushed
  out with a short reason why

---

### /docs/SECURITY.md
Required sections:
- Authentication model: how users are identified and sessions are managed
- Authorization model: what different user roles can and cannot do
- Data storage: what user data is stored, where, and how it is protected
- Environment variables: confirm no secrets are hardcoded; list all
  variables that must be set in the environment and never committed
- Third-party trust: list every third-party service that receives user
  data and what data it receives
- Known attack surface: any areas of the app with elevated risk and
  what mitigations are in place
- Dependency policy: how dependencies are monitored for vulnerabilities

---

### /docs/RUNBOOK.md
Required sections:
- Local setup: complete steps to get the project running from a fresh
  machine, including all prerequisites
- Build: exact command to produce a production build and where the
  output goes
- Deploy: step-by-step deploy process for each environment (staging,
  production). Include any manual steps that are not automated.
- Rollback: how to revert to the previous working version
- Environment configs: list of environments and what differs between them
- Common errors: a table of known errors, their likely cause, and the
  fix
- Monitoring: where to check logs, errors, and uptime alerts
```
