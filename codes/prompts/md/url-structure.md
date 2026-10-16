---
title: URL Structure
description: Audit a website's URLs against one clean standard, then, once approved, move pages area by area with tested redirects and navigation to match.
meta: Claude Code Prompt
---

Gives a website one URL standard that every page follows: lowercase hyphenated paths, plural collections, one folder per area with an overview page at its root, and one canonical address per page. Every old address is redirected, and the navigation is rebuilt from the same structure.

Claude audits first and changes nothing until you approve. It lists every route with a script, marks each one that breaks the standard and why, proposes the new address and navigation, and lists every redirect needed, along with chains, broken internal links and canonicals that point elsewhere. It works out what the host can actually do: a server or a host with a redirects file gets permanent 301s, while a host that cannot redirect gets redirect pages instead.

After approval it moves one area at a time, updating routes, internal links, navigation, overview pages, the sitemap and canonical tags together, and tests every redirect pair. It ends with a table of every URL change and the checks it ran.

## Prompt

```
Give this website a clean, consistent URL structure: one standard that every page follows, every old URL redirected, and navigation built from the same structure. Audit first, get my approval, then move pages in small, tested steps.

Read first
- Read the project's own instructions, README and routing setup before acting, and follow any rules they set.
- Work out the framework and how routes are declared (file-based, attributes, a router config), where redirects can live, how the sitemap and canonical tags are made, and how navigation is built.
- Work out what the host can do: send real 301 redirects (a server, middleware, or a redirects file the host reads), or only serve static files. Check which form the host serves a folder at, /x or /x/.
- If you cannot tell how routing or hosting works, stop and ask me. If the site has no tests, say so and offer to add a small script that checks redirects; ask before adding it.

The standard
- Paths are lowercase, with words separated by hyphens: /tools/compound-calculator, never /Tools/CompoundCalculator or /tools/compound_calculator.
- Paths name things; query strings only filter, sort, page or call a handler: /strategies/42 and /strategies?sort=new, never /strategy?id=42.
- Collections are plural nouns. Items sit under their collection by a stable id: /strategies, /strategies/42, /strategies/42/edit, /strategies/new.
- Each area of the site is one folder. The folder's root is an overview page, and every page in that area lives under it: /community, /community/strategies, /community/pies.
- No file extensions, and no dates or version numbers unless the content really is dated.
- One trailing-slash form for the whole site. Use the form the host serves natively (static hosts often serve folders as /x/), and redirect the other form to it.
- Signed-in or app areas get one clear prefix (such as /app or /account), so public and private pages never mix.
- Every page has one canonical URL: its canonical tag points to itself, and every other form of it (capitals, the other slash form, old name, http, www or non-www) redirects to it in one hop.
- Public, indexable pages are in the sitemap. Redirecting, private or noindex pages are not.

Navigation follows the URLs
- Each multi-page area has an overview page at its folder root, with a card or link for every page in the area.
- In the main nav, an area with several pages is a dropdown. Clicking its label opens the overview; the caret opens a menu of the area's pages. Leave out an "Overview" item, since the label already goes there.
- A new page is added in three places at once: its URL under the folder, a card on the overview, and a menu item.

Audit (change nothing yet)
- With a script, list every route: path, page or handler, public or private, in the sitemap or not, and how many internal links point to it.
- Mark each one that breaks the standard and say why.
- Propose the new URL for each, grouped by area, with the new nav and overview structure.
- List every redirect needed (old → new), plus redirect chains (including existing redirects that would now point at a moved page), 404s from internal links, and any canonical that does not point to itself.
- Note risks: links in emails, docs or external sites (mark these unknown if you cannot check them, never guess); URLs that carry tokens or return addresses (keep their query string through the redirect); SEO for pages that rank.
- Propose the short "URL standard" section for the project's instructions file (see "From now on").
- Then stop and show me the audit. Do not move any URL until I approve it.

Move, after approval
- Work one area at a time. For each area: change the routes, redirect every old URL straight to the new one (query string kept where it matters), and update every internal link, the nav, the overview, the sitemap and the canonical tags.
- Use permanent 301 redirects wherever the host supports them. Where it cannot redirect, leave a small page at the old address with a canonical tag to the new URL, an immediate meta refresh, a script redirect that keeps the #fragment, and a plain link, and say which addresses rely on this.
- Add a catch-all that sends any path with capital letters to its lowercase form, leaving static files alone. If the host cannot do this, say so.
- Keep the redirects in one place (a single map, middleware, or redirects file), with a comment on why each exists. Redirects are permanent; never remove one, and never chain one redirect into another.
- Add a test for every redirect pair (old path and query in, expected new path out) and for the lowercase rule.
- After each area: build, run the tests, request each old and new URL locally and confirm one redirect then 200, and crawl the internal links with a script for 404s and chains. Never run checks that change data against production.

From now on
- Once I approve it, add the short "URL standard" section to the project's instructions file, so every future page follows it: the rules above, the three-places rule for new pages, and a tested redirect whenever a URL changes.

Report, in this order
1. The audit summary: routes found, how many broke the standard, and why.
2. A table of every URL change: old, new, redirect type (301 or redirect page), redirect tested (yes or no).
3. The new navigation: each area, its overview, its menu items.
4. Checks run (build, tests, local redirect checks, link crawl) and whether each passed.
5. What is left or unknown, and why.

Do not commit anything.
```
