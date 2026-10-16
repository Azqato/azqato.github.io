---
title: URL Structure
description: Audit a website's URLs against one clean standard, then, once approved, move pages area by area with tested links, redirects and navigation to match.
meta: Claude Code Prompt
---

Gives a website one URL standard that every page follows: lowercase hyphenated paths, plural collections, every page except the home page in its own folder, each area with an overview page at its root, a clean project root, and all navigation generated from one source.

Claude first works out how the site runs, since that changes the rules. A hosted site with redirects gets permanent 301s, canonical tags and a sitemap. A static host that cannot redirect gets redirect pages. A site only ever opened from disk gets relative links that name the file, and old files are deleted once nothing points at them.

It audits first and changes nothing until you approve: every route listed with a script, each break from the standard and why, the proposed addresses and navigation, the redirects or link updates needed, files to tidy or delete, and any exceptions to the standard, such as case-sensitive IDs, for you to approve once. After approval it moves one area at a time and tests every link and redirect. It ends with a table of every URL change and the checks it ran.

## Prompt

```
Give this website a clean, consistent URL structure: one standard that every page follows, every old URL handled, and navigation built from the same structure. Audit first, get my approval, then move pages in small, tested steps.

Read first
- Read the project's own instructions, README and routing setup before acting, and follow any rules they set, including any URL standard and its approved exceptions.
- Work out the framework and how routes are declared (file-based, attributes, a router config), how pages are generated, how the sitemap and canonical tags are made, and how navigation is built.
- Work out how the site runs, since the rules below depend on it:
  - Hosted with redirects: a server, middleware, or a redirects file the host reads, so it can send real 301s.
  - Hosted, static files only: no way to send a 301. Check which form the host serves a folder at, /x or /x/.
  - Local only: opened from disk and never hosted.
- If you cannot tell how routing or hosting works, stop and ask me. If the site has no tests, say so and offer to add a small script that checks links (and redirects, if hosted); ask before adding it.

The standard
- Paths are lowercase, with words separated by hyphens: /tools/compound-calculator, never /Tools/CompoundCalculator or /tools/compound_calculator.
- Paths name things; query strings only filter, sort, page or call a handler: /strategies/42 and /strategies?sort=new, never /strategy?id=42.
- Collections are plural nouns. Items sit under their collection by a stable id: /strategies, /strategies/42, /strategies/42/edit, /strategies/new.
- Every page except the home page lives in a folder named for it, even a single page: /search, not a search file at the root. Each area of the site is one folder whose root is an overview page, with every page in that area under it: /community, /community/strategies, /community/pies.
- No file extensions in URLs, and no dates or version numbers unless the content really is dated.
- Signed-in or app areas get one clear prefix (such as /app or /account), so public and private pages never mix.
- A clean root: it holds only the home page, project files (README, config, the instructions file, and anything the host reads there, such as a redirects file, robots.txt or the 404 page) and folders. Stylesheets, scripts, images and fonts live under one assets folder.

How the standard applies, by how the site runs
- Hosted with redirects: every page has one canonical URL whose canonical tag points to itself; every other form of it (capitals, the other slash form, old name, http, www or non-www) sends a 301 to it in one hop. Use one trailing-slash form site-wide, the one the host serves natively. Public, indexable pages are in the sitemap; redirecting, private or noindex pages are not.
- Hosted, static files only: the same, except an old address keeps a small redirect page (a canonical tag to the new URL, an immediate meta refresh, a script redirect that keeps the #fragment, and a plain link) in place of a 301.
- Local only: there are no redirects, canonical tags, sitemap or lowercase catch-all. Every link is relative and names the actual file, so the example /tools/compound-calculator becomes tools/compound-calculator/index.html. A link starting with / points at the root of the drive, and a folder link opens a directory listing, so neither may be used. When a page moves, update every link to it and delete the old file, once I confirm nothing outside the project links in.

Navigation follows the URLs
- Each multi-page area has an overview page at its folder root, with a card or link for every page in the area.
- In the main nav, an area with several pages is a dropdown. Clicking its label opens the overview; the caret opens a menu of the area's pages. Leave out an "Overview" item, since the label already goes there.
- Every page's navigation is generated from one source. A menu written by hand on any page, while others are generated, is a finding.
- A new page is added in three places at once: its URL in its folder, a card on the overview, and a menu item.

Audit (change nothing yet)
- State how the site runs, and how you know.
- With a script, list every route: path, page or handler, public or private, in the sitemap or not (if hosted), and how many internal links point to it.
- Mark each one that breaks the standard and say why.
- Propose the new URL for each, grouped by area, with the new nav and overview structure, and where navigation is not yet generated from one source.
- List every redirect or link update needed (old → new), plus redirect chains (including existing redirects that would now point at a moved page), broken internal links, and, if hosted, any canonical that does not point to itself.
- List the root cleanup: files to move under assets, and files nothing loads (checked with a script, since some files are only loaded by scripts), proposed for deletion.
- List exceptions: anything that cannot follow the standard, the reason, and the pages it covers, named as a narrow pattern (for example, "summary filenames are case-sensitive YouTube video IDs"), never a blanket rule.
- Note risks: links in emails, docs or external sites (mark these unknown if you cannot check them, never guess); URLs that carry tokens or return addresses (keep their query string through the redirect); SEO for pages that rank.
- Propose the short "URL standard" section for the project's instructions file (see "From now on").
- Then stop and show me the audit. Do not move, delete or redirect anything until I approve it, including each exception and each deletion.

Move, after approval
- Work one area at a time. For each area: move the pages, handle every old URL as its mode requires (301, redirect page, or update every link and delete the old file), and update every internal link, the generated navigation, the overview, and, if hosted, the sitemap and canonical tags.
- If hosted with redirects, add a catch-all that sends any path with capital letters to its lowercase form, leaving static files and approved exceptions alone. If the host cannot do this, say so.
- Keep redirects in one place (a single map, middleware, or redirects file), with a comment on why each exists. Redirects are permanent; never remove one, and never chain one redirect into another.
- Add a test for every redirect pair (old path and query in, expected new path out) and for the lowercase rule, where they apply.
- After each area, build, run the tests, then check with a script:
  - Hosted: request each old and new URL locally and confirm one redirect then 200, and crawl the internal links for 404s and chains.
  - Local only: resolve every link the way a browser does from disk, relative to the page's own file, and confirm each one names a file that exists.
  - Every page's navigation matches its one source.
- Never run checks that change data against production.

From now on
- Once I approve it, add the short "URL standard" section to the project's instructions file, so every future page follows it: the rules above for this site's mode, the approved exceptions, the three-places rule for new pages, and a tested redirect or link update whenever a URL changes.

Report, in this order
1. The audit summary: how the site runs, routes found, how many broke the standard and why, and the approved exceptions.
2. A table of every URL change: old, new, how the old URL is handled (301, redirect page, or links updated and old file deleted), and tested (yes or no).
3. The new navigation: each area, its overview, its menu items, and its one source.
4. The root cleanup: files moved and files deleted, each with its approval.
5. Checks run (build, tests, redirect or link checks, navigation check) and whether each passed.
6. What is left or unknown, and why.

Do not commit anything.
```
