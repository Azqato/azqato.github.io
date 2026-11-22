---
title: Website Setup
description: Build a website from the ground up by running eight of this site's prompts in order, tracked as a roadmap in the README, without repeating work.
meta: Claude Code Prompt
---

Builds a website from the ground up by running eight prompts from this site in a fixed order: Project Defaults, Documentation, Assumption Check, URL Structure, Landing Page, Design Review, Mobile Audit, and finally App Performance or Animation Performance, whichever fits the site. It reads the project first, then sets up the README with a Roadmap section that lists the steps as a checklist, each linked to its prompt, and waits for your go-ahead.

For each step it downloads the full prompt from this site and reads it before acting, rather than working from memory. Several prompts ask for the same groundwork, such as reading the docs or asking about the project, so it checks what the session has already done and skips repeats, saying what it skipped, unless a file has changed since. It follows each prompt's own checkpoints, asks you when two steps disagree, ticks each step in the roadmap once its checks pass, and asks before moving to the next. It never commits, pushes, or publishes anything.

## Prompt

```
Set up this website from the ground up by running a series of prompts from azqato.com, one at a time, in a fixed order. Track the work as a roadmap in README.md, and never repeat a task this session has already done.

The steps, in this order (each prompt's full text is at https://azqato.com/codes/prompts/md/<slug>.md):
1. Project Defaults (project-defaults)
2. Documentation (documentation)
3. Assumption Check (assumption-check)
4. URL Structure (url-structure)
5. Landing Page (landing-page)
6. Design Review (design-review)
7. Mobile Audit (mobile-responsive-audit)
8. App Performance (app-performance) or Animation Performance (animation-performance): App Performance for a site with app-like screens, data loading, or long lists; Animation Performance for a site whose animations matter; both if both apply. When you reach this step, recommend one, say why, and ask me.

Start
- Read the project first: README.md, CLAUDE.md, docs/, and the main files, if they exist. An empty folder is fine; say so.
- Create README.md if it does not exist, or add to it if it does, keeping everything already in it. Add a "Roadmap" section that lists the steps above in order as a checklist, each with its prompt's page address, in this shape:
  - [ ] 1. Project Defaults: house rules and a docs folder. https://azqato.com/codes/prompts/project-defaults/
  If the README already has a roadmap, keep its items and their ticks, and add these steps to it rather than replacing it.
- Show me the roadmap and wait for my go-ahead before step 1.

Running each step
- Download the step's Markdown file with curl (a web fetch tool may return only a summary) and read the whole prompt before acting. If it cannot be downloaded, stop and tell me; never run a step from memory.
- Before acting, list the tasks the prompt asks for and check each one against what this session has already done. Skip a task that an earlier step in this session already did (for example, reading the docs, mapping the project, or asking me something I already answered), unless a file it depended on has changed since; then redo only what the change affects. Say which tasks you skipped and which earlier step did them. Only work done in this session counts: in a new session, read the docs and the roadmap again before continuing.
- Follow the prompt's own checkpoints and questions. Where it asks something an earlier step already settled, show the earlier answer and ask only what is new.
- Where a step conflicts with a decision made in an earlier step or recorded in the docs, quote both and ask me which wins. Do not settle it yourself.
- When the step's own checks pass, tick it in the roadmap with today's date (from the system clock) and a one-line result. If a step stops early or fails its checks, leave it unticked and add a note saying why.
- Then report in a few lines: what was done, what was skipped as already done, and what is left. Ask before starting the next step.

Ground rules
- Do not commit, push, deploy, or publish anything.
- Do not skip, reorder, or merge steps unless I say so.

Finish
When the last step is done, check the roadmap: every step is ticked or carries a note saying why not, and every tick is backed by that step's passing checks. Report which steps passed, which were skipped or left unfinished and why, and anything you could not verify.
```
