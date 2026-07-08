---
title: Documentation
description: Scan the entire codebase, then consolidate all documentation into four core files, packing every supporting doc into a deeply sectioned PRD.
meta: Claude Code Prompt
---

Crawls the full codebase first, then audits and consolidates all documentation into four core files: README.md at the root, and PRD.md, DESIGN.md, and PATCHNOTES.md inside `/docs`. Missing files are created and the correct folder structure is enforced. The PRD absorbs everything else, with required sections for Tenets, Roadmap, Metrics, Runbook, Technical Requirements, Security, a Press Release, and an FAQ, so the entire project can be understood from `/docs` alone without reading any code.

Use it when a project needs one authoritative, exhaustive doc set in a single pass. The heaviest of the documentation prompts: where Consolidate Documents keeps four lean files and Documentation Audit spreads detail across eleven, this folds that full depth into a single comprehensive PRD.

## Prompt

```
Perform a full documentation audit of the /docs folder. Your goal is to ensure every document accurately reflects the current state of the codebase with no gaps, outdated information, or missing coverage.
Steps to follow:

Crawl the entire codebase and build a complete picture of what exists: all files, features, components, routes, configs, and logic.
Open every document in /docs one by one.
For each document, compare its content against the actual codebase and identify anything that is outdated, missing, inaccurate, or incomplete.
Rewrite or update each document so it is fully accurate and comprehensive based on the current version of the site.
Do not skip any document. Every single file in /docs must be reviewed and updated.
After all documents are updated, provide a summary of what changed in each file and why.

Standards to uphold:

Every document should be thorough enough that a new contributor or AI model can understand the project entirely from the /docs folder alone.
If a document is missing a section that the codebase clearly warrants, add it.

Make sure to perform a full codebase scan before touching any documentation.

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
PATCHNOTES.md - A running log of every change made, with dates and reasons why.
DESIGN.md - How it looks. Colors, fonts, spacing, and UI rules to stay consistent.
PRD.md - What you're building and who it's for. You should be so detailed that it is easy to understand everything about the entire project without having to review any code. This file should also contain additional sections consolidating all of the documentation files you are removing from this audit in order to keep track of the overall direction of the project accurately from all perspectives. 

---

### README.md (root)
Required sections:
- Project name and one-sentence description
- Link to the currently live site
- Tech stack list with versions
- Prerequisites (Node version, package manager, environment requirements)
- Installation steps (exact commands, in order)
- How to run locally (dev server command, default port)
- Environment variable reference (key names, what each does, whether required or optional)
- Build and deploy instructions
- Link to /docs for full documentation

Do not include marketing language. README is for developers, not end users.

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
- Any additional information an AI model would find relevant when it comes to understanding the design philosophy behind the website.

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
Additional sections:
Tenents
- 3-7 tenets maximum. More than 7 dilutes the value.
- Each tenet has a short title (3-5 words) and a 2-4 sentence explanation.
- Tenets must be opinionated enough to resolve a real product tradeoff.
  A tenet that everyone agrees with without hesitation is not useful.
- Order them by priority. When two tenets conflict, the higher one wins.
Roadmap
- Current phase: name and brief description of where the product is now
- Milestone table: each milestone has a name, target date or relative
  timeframe, and a status (Planned, In Progress, Complete, Blocked)
- Feature breakdown per milestone: bullet list of what ships in each phase
- Explicitly deferred items: features considered but intentionally pushed
  out with a short reason why
Metrics
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
Runbook
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
Technical Requirements
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
Security
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
Press Release
- Written as if the product has just launched publicly. Include
  product name, what it does, who it is for, the key benefit, and a mock quote
  from a fictional user. Written for a general audience, no jargon.
- Headline - one sentence naming the product and its core benefit, written as a live published announcement
- Subheadline - expands on the headline with one added detail or hook
- Dateline - city and release date
- Opening paragraph - covers who, what, when, where, and why in 3 to 5 sentences
- Problem statement - the specific pain point being solved, written from the customer perspective
- Solution description - how the product solves it, in plain non-technical language
- Customer quote - fictional but realistic quote from a named target persona
- Call to action - what the reader should do next (sign up, visit, download)
- Company boilerplate - one short paragraph describing the organization
Frequently Asked Questions
- External FAQ: 10-25 questions a real user would ask. Cover how it works,
  what it costs, what data it uses, and what it does not do.
- Core definition and target audience
- Step by step usage summary
- Pricing and availability - cost, tiers, launch date, and regions
- Technical requirements - integrations, compatibility, and dependencies
- Competitive differentiation - how it differs from existing alternatives
- Known limitations - what the product does not do in v1
- Support and onboarding - how users get help and ramp up
- Internal stakeholder questions - ROI rationale, success metrics, and roadmap direction

---

After everything is updated, add these recent changes to PATCHNOTES.md and describe this process and how everything should be handled moving forward in PRD.md.
```
