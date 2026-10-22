# Prompts: Operating Notes

How the Prompts section of azqato.com (`/codes/prompts/`) is run: where things live, the rules every prompt follows,
and the steps for adding, changing and retiring prompts. Site-wide rules (deploy, design, the em dash hook, versioning)
live in the site's own [docs/PRD.md](../../../docs/PRD.md); this file covers only what is specific to prompts and
points there for the rest.

Last updated 2026-10-12, site version 2.19.1.

---

## 1. What the section is

A public collection of prompts for Claude Code. Each prompt has its own page with a short description and the full
prompt text, a Copy button and an Expand toggle. The list page carries every visible prompt in a set order, with search.

The section moved here from its own repository (Azqato/prompts, served at azqato.github.io/prompts/) under item 22 of
the site plan. That repository is archived. Its share pages in `p/` stay published and forward to the matching page
here, so old links keep working. Its version line ended at v1.112.0; from 2.19.0 prompts changes are ordinary site
versions, and the old history sits at the end of [docs/PATCHNOTES.md](../../../docs/PATCHNOTES.md).

## 2. Where things live

| Path | What it is |
|---|---|
| `codes/prompts/md/<slug>.md` | The source of each prompt. The only file edited by hand to change a prompt. Also served publicly as is. |
| `scripts/prompts/build.py` | Turns the sources into pages. Holds `CATEGORIES` (the category headings and the list order within each; `ORDER` is derived from it) and `RETIRED` (old slugs and where they now point). |
| `codes/prompts/index.html` | The list page. Generated. |
| `codes/prompts/<slug>/index.html` | One page per prompt. Generated. |
| `codes/prompts/assets/` | `prompts.js` (search, Expand, Copy) and the section's styles. Edited by hand. |
| `sitemap.xml`, `_redirects` | Each has a prompts block the build rewrites. The rest of each file is untouched. |
| `scripts/prompts/browser.py` | The browser test for the section. |
| `codes/prompts/docs/PRD.md` | This file. |

Generated pages are committed like any other file, and the site works if the build script is deleted. Never hand-edit a
generated page: the next build overwrites it, and `--check` reports the drift.

### Source file format

```
---
title: Short Title
description: One sentence for the list, search results and link previews.
meta: Claude Code Prompt
hidden: true            (optional)
---

A paragraph or two saying what the prompt does and when to use it.

## Prompt

    (the prompt, in one fenced code block)
```

The slug is the filename. The description body is shown above the prompt; the fenced block is the prompt itself and is
what Copy, Expand and the agent note refer to.

## 3. Rules for every prompt

Prompts are public and get reused by people who have never seen this site, often arriving at one page from a shared
link. These rules keep a prompt safe to hand to a stranger and keep it working when it runs.

### Content

- **No push, commit or publish instructions.** The person running a prompt decides when anything goes to a remote.
  Search new text for "push", "commit", "publish to GitHub" and their variants before it goes live.
- **Nothing tied to the author.** No accounts, credentials, private services or personal paths. A prompt must run the
  same in anyone's project.
- **Third-party sites are allowed when the prompt itself uses them**, for example a public tool or reference the prompt
  sends Claude to. Check that the site is live and that its terms allow the use, note the date checked in the patch
  notes, and have the prompt ask before installing anything.

### Writing

Every new or edited prompt is checked against these, where they apply. A one-line prompt has little to measure; a review
prompt has little to write.

1. **Read, don't recall.** Tell Claude to read the files, page or text it needs before acting. A fact that can be read
   is never taken from memory.
2. **Look before judging.** Order the steps so reading and checking come first and conclusions last. Never ask for a
   verdict followed by reasons.
3. **Give exact work to tools.** Counts, lengths, sizes, dates, sums, exact matches and comparisons are done with a
   command or script, not by eye.
4. **Allow "unknown".** Say what to do when something cannot be found or checked: stop and ask, or mark it unknown.
   Never fill a gap with a guess.
5. **Show the output's shape.** Where format matters, name the columns, sections or fields, or give a one-line example.
6. **Finish on a pass or fail.** End with a check that can be verified (tests pass, every file exists, every item meets
   the bar) and ask for a report of what was and was not checked.
7. **Scores that can't be gamed.** Fix the rubric before scoring, judge from the real work, and forbid raising one
   number by lowering another.
8. **Stay focused.** The main instruction comes first. Link or fetch long reference material instead of pasting it, and
   cut filler.
9. **Supply what the model can't know.** Its own name and version and today's date come from the session or the system
   clock, or the prompt asks.

### Style

- Plain words, short sentences, written for a general reader.
- No em dashes in this file, the page text or the patch notes; the site hook enforces it. The prompt sources in `md/`
  are exempt from the hook so imported prompts can be kept word for word, but new prompt text should avoid them too.
- **Title:** aim for 60 characters, 70 at most, without the site name (the build adds it).
- **Description:** one sentence ending in a full stop, aim for 150 characters, 200 at most.
- Count lengths with a script, not by eye.

## 4. Page behaviour worth knowing before changing it

- **Copy** does not copy the prompt. It copies a short pointer to the prompt's page:
  `Review the full prompt on this website, provide a summary of what it does and then ask if I would like to run it: `
  followed by the page address. This lets the person see what a prompt does before it runs. The wording changes only at
  the author's request, and the browser test checks it character for character.
- On failure Copy shows "Copy failed" for two seconds. Nothing is stored in the browser.
- The prompt starts collapsed. The whole bar toggles Expand and Hide, except Copy, which never toggles it.
- Search matches every typed word in any order. Enter opens the first match; Escape clears.
- Each page links its source with `rel="alternate"` to `md/<slug>.md` and carries a hidden note telling AI agents that
  the code block is the full prompt. Both exist so an agent given the page address can read the prompt reliably.
- Each page has its own canonical address, `https://azqato.com/codes/prompts/<slug>/`, and the usual Open Graph tags.

## 5. Adding a prompt

1. Pick a slug: lowercase, hyphenated, short, and never one that is or was in use (check `RETIRED`).
2. Write `codes/prompts/md/<slug>.md` in the format above.
3. Check the text against section 3. Count the title and description lengths with a script.
4. Add the slug to the right category in `CATEGORIES` in `scripts/prompts/build.py`, where it should appear in that
   category's list. The Prompts page and the Codes sidebar both show it under that heading.
5. Run the build and checks (section 8).
6. Add a site patch-notes entry (section 9).

The Add Prompt prompt (`md/add-prompt.md`) walks Claude through these steps from raw prompt text.

## 6. Changing, renaming, hiding and removing

- **Editing** a prompt: change its `.md` file, rerun the build and checks, and add a patch-notes entry.
- **Hiding:** add `hidden: true`. The page stays live at its address but leaves the list, search and the sitemap. Use it
  for a prompt that is still linked from somewhere but should no longer be offered.
- **Renaming:** `git mv` the source to the new slug, update `CATEGORIES`, and add `'<old>': '<new>'` to `RETIRED`. The build
  writes a 301 from the old address. Search the site for the old slug and title and fix anything that describes the
  present.
- **Removing:** delete the source, take it out of `CATEGORIES`, and add it to `RETIRED` pointing at the list page or the
  nearest replacement. Its address is public, so it is retired, never just dropped.
- `RETIRED` entries are permanent, never chain (point at the final page directly) and are never reused.
- Past patch notes keep the names a prompt had at the time. They are a record, not a description of now.

## 7. Public addresses

- `https://azqato.com/codes/prompts/` and `https://azqato.com/codes/prompts/<slug>/` are the live pages. The build adds
  a 301 for each address without its trailing slash.
- `https://azqato.com/codes/prompts/md/<slug>.md` serves each source as is. Treat these as public too.
- Retired slugs: `iphone-ipad-simulator` now points to `ios-simulator`.
- The archived repo's share pages (`azqato.github.io/prompts/p/<slug>.html`) forward to the pages here. The repo is
  archived, so a prompt added here has no old share page and needs none. If a prompt that had one is renamed or
  removed, its old share page still forwards to the old address here, which the `RETIRED` redirect then carries on.
- Some prompt texts may still cite old addresses under `azqato.github.io/prompts/`. Replace them with the address here
  when that prompt is next edited.

## 8. Build and checks

Run from the site root:

```bash
python scripts/prompts/build.py           # pages, sitemap block, redirects block, then the Contents sidebar
python scripts/build-nav.py               # always last: nav, footer, search
python scripts/prompts/build.py --check   # exits 1 if any generated page or block is out of date
python scripts/build-nav.py --check       # nav and footer match everywhere
python scripts/prompts/browser.py         # every page, both themes, desktop and phone
```

When the build writes a page it reruns `scripts/codes/shell.py` itself, so the Contents sidebar, crumbs and byline are
never lost. `--check` ignores what `shell.py` and `build-nav.py` add, so it passes on a clean tree.

The build stops if `CATEGORIES` and the files in `md/` disagree. The browser test runs headless Edge and covers each page in
both themes at both widths with contrast checks, search, the Contents sidebar and Previous / Next, the collapsed start,
Expand, the exact Copy pointer, that Copy never collapses the prompt, that the page text matches its source, and that a
source file is served unchanged. A change is ready when all three checks pass.

## 9. Versions and patch notes

Prompts changes are site versions and go in [docs/PATCHNOTES.md](../../../docs/PATCHNOTES.md) under the site's rules:
a minor version for a new or reworked prompt or a docs change, a patch version for a small fix. Name the prompt in the
entry. Committing and pushing are the author's call, never something a prompt asks for.

## 10. Ideas

Candidate prompts, not yet written. Before adding one, check it against section 3 and confirm any third-party claim
from a primary source.

- **Legal Audit.** From a post listing six legal traps common in quickly built apps, with a suggested one-paragraph fix
  prompt:
  1. Signup with no age question (COPPA, children under 13).
  2. Google Fonts loaded from Google's servers, leaking visitor IP addresses (a Munich court awarded damages under GDPR).
  3. Session replay on by default, recording keystrokes (can count as wiretapping under California's CIPA).
  4. Marketing email with no unsubscribe link or postal address (CAN-SPAM).
  5. Subscription checkout without renewal terms beside the button (California automatic renewal law).
  6. No registered DMCA agent, losing safe harbor for user uploads.

  The post's own prompt fixes all six in one go. A site version should audit first and report, then ask before each
  fix, say it is not legal advice, and have Claude confirm current penalty figures and rules from official sources
  rather than repeat the post's numbers.
