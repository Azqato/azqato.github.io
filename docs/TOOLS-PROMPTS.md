# Tools and Prompts: interpretation and plan (roadmap item 22)

Written 2026-10-08. This covers phase 1 (interpretation, read only) and a draft of phase 2 (the plan). Nothing in either repo was changed. Phase 3, the build, starts on the owner's answers to the questions at the end.

**Sources.** Local clones of https://github.com/Azqato/tools (branch `master`, v1.4.2, commit 23a4f2f) and https://github.com/Azqato/prompts (branch `main`, v1.112.0, commit e697a88). Both are clean and match GitHub.

---

## Phase 1: interpretation

### Tools (azqato.github.io/tools)

- **What it is:** ten small utilities that run entirely in the browser: Markdown Editor, Favicon Downloader, Link Cleaner, Character Counter, Wash Sale Tracker, Bookmark Manager, Base64 Encoder, JSON Formatter, Password Generator and Timestamp Converter. A landing page lists them with a search box, along with four "external" links to Azqato projects hosted elsewhere: Nasdaq 100 Screener, Net Worth Tracker, VIX Strategy and Protein Tracker.
- **How it's built:** plain HTML, CSS and JS with no build step. There is one HTML page per tool (8 to 19 KB each), one script per tool plus `js/common.js` (theme, nav), and one stylesheet (`css/style.css`, 34 KB, about 1,300 lines). The total is about 210 KB.
- **Its own design:** it has its own palette (`--bg #f6f7f9`, a purple gradient on the logo and hero) and its own theme switch (`data-theme` set in JS, with no `prefers-color-scheme` in the CSS). This is not the Template Interface Color Standard.
- **Data:** the Markdown draft, Wash Sale log and bookmarks are saved in `localStorage` under the `azqato.github.io` origin. **On azqato.com that is a different origin, so saved data does not carry over.** Users would start empty.
- **Docs:** README, PRD, DESIGN and PATCHNOTES. It has had a full accessibility pass. Friend Finder is on its roadmap.

### Prompts (azqato.github.io/prompts)

- **What it is:** a library of 24 Claude Code prompts. It is a single-page app: `index.html` with hash routes (`#/slug`) and a search box. Each prompt's description shows first, and the full text sits behind Expand.
- **How it's built:**
  - The source of truth is `prompts/*.md`, 24 files (288 KB) with frontmatter.
  - `js/prompts-data.js` is a verbatim copy so the site works from `file://`.
  - `p/<slug>.html` are 25 generated share pages, which carry the link-preview tags and a meta refresh to the prompt.
  - `tools/prompts-mirror.py` syncs and checks all of that and writes `sitemap.xml`.
  - `dashboard/` is a generated progress page, marked noindex.
- **The Copy button is the critical part.** It does not copy the prompt. It copies a one-line pointer: *"Review the full prompt on this website, provide a summary of what it does and then ask if I would like to run it: https://azqato.github.io/prompts/p/<slug>.html"*. Claude then fetches that page, which names the raw Markdown on `raw.githubusercontent.com/Azqato/prompts/main/prompts/<slug>.md`. **Every pointer anyone has already copied, saved or shared depends on those addresses still working and still serving the prompt text.**
- **Its own design and rules:** its own `css/style.css`, a strict writing style (no em dashes, the same rule this site has), a `CLAUDE.md` with a dashboard workflow, and a PRD with 27 sections.

### How these differ from Invests

Invests was mostly **content pages** (articles, tables, charts) that `tools/invests/site.py` moved whole out of source snapshots and rewrapped in this site's chrome. Both new sources are **apps**:

- Tools is ten interactive pages whose behavior lives in JS.
- Prompts is one JS app plus generated pages, and its addresses are effectively a public API.

Their content moves the same way, but the scripts must keep working, and both have to keep their old addresses alive.

### Constraints that carry over from Invests

- Source text is kept word for word.
- The pages get the shared top bars, footer and `colors.css`.
- Each page gets a clean address and a search entry.
- The old addresses redirect.
- **GitHub Pages cannot send a real 301.** The old repos can only redirect with a meta refresh plus a canonical link, as Invests' old repos do.

---

## Phase 2: the plan (draft, for the owner's review)

1. **Tools first; it is the simpler of the two.**
   - Snapshot it into `tools/tools-site/_sources/` and write a generator `tools/tools-site/site.py` modeled on the Invests one. It moves each tool's `<main>` and script into `/tools/<name>/`, gives it the shared chrome and maps its colors onto `--ti-color-*` roles.
   - Add a `/tools/` index (the landing list and its search), a nav entry, search-index entries and a check script (links, no leftover old palette, every tool loads with no console errors). Add a browser test per tool for its main action.
   - For the four "external" entries, VIX Strategy should point to `/invests/vix/`; the other three keep their links.
   - **Tracker data:** add a one-time import notice, or accept that it starts empty (see question 2).
2. **Then Prompts.**
   - Keep `Azqato/prompts` as the place prompts are written (its `.md` files, mirror script and `CLAUDE.md` workflow stay). This site's generator reads its `prompts/*.md` and builds `/prompts/` and one real page per prompt at `/prompts/<slug>/`, with the full text in the HTML. That page replaces both the hash route and the share page.
   - The Copy pointer on azqato.com names the new address.
   - **Old pointers:** the old `p/<slug>.html` pages must keep serving the prompt itself, not only a redirect, because Claude's fetch tool may not follow a meta refresh (question 3).
3. **Redirects and links (old repos, after the owner says yes).**
   - Change the old landing pages and tool pages to a meta refresh plus canonical pointing to azqato.com.
   - Update the Codes and Projects cards here to the new internal addresses.
   - Add `_redirects` for the no-slash forms.
4. **Docs:** PRD decision entries, PATCHNOTES, Runbook steps for "a prompt was added in the prompts repo, rebuild here", and DESIGN notes for the two new sections.

Rough size: Tools is one or two sessions. Prompts is one or two, and most of its risk is in the old-address handling.

---

## Questions for the owner

1. **Order:** Tools first, then Prompts? (Recommended.)
2. **Saved data in Tools:** the Markdown draft, Wash Sale log and bookmarks don't carry over to azqato.com. Is starting empty fine, or should the old site show a notice for a while ("Moved; export first")? The recommendation is a notice on the three affected old tool pages, linking to the new page.
3. **Old prompt pointers:** keep the old `azqato.github.io/prompts/p/<slug>.html` pages serving the full prompt text, with a "moved" line and a canonical link to azqato.com, so pointers already pasted keep working? (Recommended.) The alternative is a bare redirect, which may break them.
4. **Where new prompts get written:** keep writing them in the prompts repo, with this site rebuilding from it (recommended, since its `CLAUDE.md` workflow and mirror script stay useful), or move the authoring here and retire that repo?
5. **Tools' look:** drop its purple gradient logo and hero for azqato.com's emerald and the color standard? The recommendation is yes, matching how Invests was handled.
6. **Dashboard:** the prompts repo's `dashboard/` is a build-progress page, not product. Should it be left out of azqato.com? (Recommended.)
