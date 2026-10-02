# Hosting options - Azqato Invests

Written 2026-10-02 at the author's request, for Question 18 in PRD.md (where the site lives, and what happens to azqato.com/invests). Nothing here has been done; it is analysis for a decision. The author's stated preference: azqato.com/invests should be this site.

## What every option has to satisfy

- **The data feeds keep working.** The pages read stock data from raw.githubusercontent.com (open CORS), falling back to azqato.github.io/stocks/data/ (open CORS), and the VIX reading from azqato.github.io/vix/data/vix.js as a script. Checked 2026-10-02: none of these depends on the site being on azqato.github.io, so every option below works for data.
- **Relative links.** Every link and fetch inside the site is relative, so it runs under any folder (/invests/) or at a domain root without changes. Only `SITE_URL` in scripts/site.py (canonical, og:url, sitemap.xml) changes with the address.
- **Independent rules (D5).** This repository sets its own rules and builds the site; azqato.github.io's rules don't apply to it.
- **No data feeds in this repo (D21)** and **nothing published without the author's word (D20).**

## Facts about azqato.github.io (read 2026-10-02)

- Public repository; served by GitHub Pages at azqato.github.io and by a Cloudflare Pages build at azqato.com.
- Root files: the site's pages (index, about, discord, invests, codes, music, links, projects, youtube, support, accounts, privacy-policy), styles.css, robots.txt, sitemap.xml, img/, audio/, docs/, tools/build-nav.py. No `_redirects` file.
- tools/build-nav.py stamps the nav onto root-level `*.html` only (`root.glob('*.html')`), so files in a subfolder such as invests/ are left alone. invests.html is in its nav as "Invests".
- azqato.com answers /page.html with a redirect to /page (Cloudflare Pages behavior, Verification Environment).

**Decided 2026-10-02: option D**, by the author: separate repositories were only for the first build and testing. At first everything sits in one `invests/` folder in the azqato.github.io repository, to be folded into the main site's structure later; this repository keeps its own history.

## The options

### A. GitHub Pages project site: azqato.github.io/invests/ (the current plan, D21)

The invests repository, made public, serves itself with GitHub Pages.

- **azqato.com/invests:** still invests.html from the main repo. To make it this site, invests.html becomes a redirect (or a `_redirects` rule in the main repo: `/invests /invests-site-address 301`) to azqato.github.io/invests/, so visitors land on a github.io address.
- **For:** simplest; already planned and written in the Runbook; nothing new to run; same origin as the stocks data.
- **Against:** the address isn't azqato.com/invests, which is the stated preference. azqato.github.io/invests.html and the project site at /invests/ overlap and have to be untangled (invests.html retired).
- **Work:** small.

### B. Cloudflare Pages project plus a Worker route: azqato.com/invests/

A second Cloudflare Pages project builds the invests repo (at invests.pages.dev); a Worker on the route `azqato.com/invests*` fetches each request from invests.pages.dev and returns it.

- **azqato.com/invests:** this site, at the address wanted. invests.html in the main repo is removed or left unreachable (the Worker route takes the path first).
- **For:** the wanted address; the repos stay fully separate; deploys are independent.
- **Against:** a Worker is code to write, deploy and keep running, outside both repos. Gotchas to handle: Cloudflare Pages answers /faq.html with a redirect to /faq, and its `Location` header has to be rewritten by the Worker or visitors are sent to azqato.com/faq (the wrong site); /invests without the slash; caching headers. The free plan allows 100,000 Worker requests a day (fine at today's traffic, but a limit to watch). The site also exists at invests.pages.dev, which needs a canonical pointing at azqato.com (already in place once `SITE_URL` changes). azqato.github.io/invests/ wouldn't exist.
- **Work:** medium, plus a new moving part to monitor.

### C. Publish the built site into the main repo's invests/ folder (hybrid)

This repository stays the source: the generator, checks, docs and history live here. A publish step copies the built files (the 21 pages, assets/ and sitemap entries) into an `invests/` folder in the azqato.github.io repo, which then commits and pushes as usual. Cloudflare Pages builds it at azqato.com/invests/, and GitHub Pages at azqato.github.io/invests/.

- **azqato.com/invests:** this site, at the address wanted, with no Worker. invests.html is removed so /invests resolves to the folder; old links to /invests.html get one redirect (a small redirect page, or a `_redirects` rule for Cloudflare).
- **For:** the wanted address, with no new infrastructure; both domains serve it; same origin as azqato.com's own pages; build-nav.py leaves the folder alone; the main repo's robots.txt and sitemap.xml already sit at the origin, so the site's pages join that sitemap. This repo keeps its own rules (D5), and the invests GitHub repo becomes optional (it could hold this source, private or public).
- **Against:** each publish is two steps (build here, copy and push there); the built files are committed in both repos; the main repo's own checks and rules must tolerate a folder they don't own (to read in that repo before choosing). Changes the azqato.github.io repo, which needs the author's say-so (Working Practice).
- **Work:** small to medium: a copy script, removing invests.html, updating its nav item to invests/, and a Runbook rewrite.

### D. Full merge into the main repo

Move everything here (generator, scripts, docs, history) into azqato.github.io and retire this repository.

- **For:** one repository.
- **Against:** undoes D5 (independent repo, own rules): the two projects' rules, docs and checks collide, and this project's PRD, DESIGN and patch notes would have to fit that repo's structure. The source snapshots, inventories and generator add weight to a personal site's repository. Gives nothing that C doesn't, since C already serves the site from the main repo.
- **Work:** large.

### Also possible: invests.azqato.com

A Cloudflare Pages project for the invests repo on a subdomain. Simplest Cloudflare setup (one DNS record), and the site would own its origin. Not azqato.com/invests, so it's listed for completeness.

## Comparison

| | A. GitHub Pages | B. Worker | C. Publish into main repo | D. Full merge |
|---|---|---|---|---|
| azqato.com/invests is the site | No (redirects away) | Yes | Yes | Yes |
| New infrastructure | None | Pages project + Worker | None | None |
| Repos stay independent (D5) | Yes | Yes | Yes (source here, output there) | No |
| Steps to publish a change | 1 push | 1 push | Build, copy, push | 1 push |
| Changes the main repo | Retire invests.html | Retire invests.html | Folder, nav item, invests.html | Everything |
| Ongoing risk | Low | Worker upkeep, redirect rewriting | Two copies of the output | Rules conflict |

## Recommendation

**C, publishing the built site into the main repo's invests/ folder.** It gives azqato.com/invests (and azqato.github.io/invests/) without a Worker, keeps this repository's rules and history separate as D5 intends, and keeps each publish an ordinary push to a repo that already deploys to both domains. Choose B instead only if the main repo must not carry the built files. Before building C: read the main repo's own docs and checks to confirm they tolerate an invests/ folder, then change `SITE_URL` to https://azqato.com/invests/ and rewrite the Runbook's Deploy and Rollback.
