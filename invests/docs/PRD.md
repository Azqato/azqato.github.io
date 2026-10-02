# PRD - Azqato Invests

This is the product requirements document for Azqato Invests: one site, in its own repo, that merges the stocks, vix and leverage sites with the current invests.html page, built on the documentation-site template. It's the main reference for anyone working on the project, person or AI model. It holds the whole plan, the technical setup, the standing rules and how work is done here, so the project can be understood without reading any code.

- **Stage:** planning is done apart from a few open points (see Risks and Open Questions). No site files exist yet. Where this document describes the site, it describes the plan, not code; the verification checklist in the Roadmap shows which sections have been checked, and against what.
- **Last documentation audit:** 2026-10-01 (see Documentation audits). The next audit starts from this date.
- **Other documents:** [README.md](../README.md) is the short public front door. [DESIGN.md](DESIGN.md) covers how the site looks. [PATCHNOTES.md](PATCHNOTES.md) logs every change. [TODO.md](TODO.md) is the author's ideas list. [LICENSE.md](../LICENSE.md) sets the terms of use.
- **Where the plan came from:** until 2026-10-01 the whole plan lived in README.md. The documentation audit on that date moved it here and into DESIGN.md word for word. Text marked "Added by the 2026-10-01 audit" is new.

## Core rule: preserve everything

> Ingest everything and present it differently while preserving everything.

It's the same approach the stocks, vix and leverage sites were built on. It covers all four sources (stocks, vix, leverage and invests.html), applies to every part of the build, and overrides anything else in this plan.

- **Kept:** every page, section, paragraph, table, chart, tool, setting, data feed, link (referral links included), disclaimer and risk warning.
- **Changed:** only the presentation: the template, layout, navigation, theme and page addresses (old addresses redirect to the new ones).
- **Allowed:** correcting a link that points to an old address, such as the old Composer Atlas link. The link stays; only its destination changes.
- **Never without your sign-off:** cutting, trimming or summarizing away any content.

How it's checked:

1. Before a page moves, everything on it gets listed.
2. After it moves, every item on that list is checked against the new page.
3. A page isn't done until every item is accounted for.

The author's words when setting the rule (2026-10-01): "ingest everything and present it differently while preserving everything, just like the other websites we are consolidating into this. everythign should follow this rule and core ideology please make sure to document it in readme.md this is very important". As asked, README.md carries a short version of the rule; this section is the full one. Decision D3 applies it to everything.

## Problem statement

Azqato's investing material is split across four places, each a separate site with its own pages, styles and navigation:

- the stocks site: 9 pages of guides, a screener, Market Overview and an FAQ;
- the vix site: 3 pages, the VIX strategy, its dashboard and a custom builder;
- the leverage site: 7 pages, a landing page and six leveraged strategies;
- invests.html on azqato.com: one page of project cards and 15 categories of curated links.

A visitor has to know which site holds what, and the sites link to one another rather than sharing one menu or one search. Some links point to an old GitHub Pages copy of Composer Atlas instead of the live site (see Composer Atlas).

Azqato Invests merges all four into one site with one navigation, one search and one design, while keeping every page, tool, link, disclaimer and risk warning (core rule). It's for people learning about investing or managing their own investments, for Azqato's Discord community, and for Azqato as the site's one maintainer.

## Target users

Personas drafted by the 2026-10-01 audit from the plan; the descriptions are illustrative.

1. **The learner.** New to investing, or to picking individual stocks. Reads the Learn pages (philosophy, stock metrics, index and ETF methodology), the setup guides and the FAQ. Needs plain explanations, numbered steps and risk warnings that are hard to miss. The template ratings describe the reading pages as being for "beginner-to-intermediate investors".
2. **The stock picker.** Manages their own portfolio and screens for ideas. Uses the Screener, Market Overview and the Metrics page. Needs a full-width, dense table, quick filters and current data.
3. **The strategy follower.** Runs, or is weighing, a rules-based strategy: the VIX strategy or one of the leveraged ones (3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail, HFEA). Checks the VIX Dashboard, reads the rules and risks, and compares with Composer Atlas. Needs today's reading, the exact rules and a direct link to the Atlas page.
4. **The Discord member.** Arrives from a link shared in Azqato's Discord. Needs to land on the right page and find related pages through the sidebar and search. Visitors arriving from elsewhere use the "Join the Discord" button to join.
5. **The maintainer (Azqato).** Keeps the site and the data pipelines running alone. Needs plain files with no build step, the pipelines left where they are (D6), and one place to change shared things.

## Goals

1. Everything from the four sources is on the new site: every inventory item accounted for on every page (core rule, D3).
2. One navigation, one search and one design across all 21 pages (D8, D12).
3. The tools keep working from the existing data feeds, with no pipeline moved (D6).
4. Light and dark themes, switched with one button (D10).
5. Composer strategies link to their Composer Atlas pages (D15, D16, D17).
6. Every old stocks, vix and leverage address keeps working by redirecting to its new page, once publishing is approved (D7, D20).

## Non-goals

- No accounts, sign-in or saved user data (Assumptions).
- No tracking or analytics scripts (Assumptions).
- No financial advice or personal recommendations. The site explains and shows data; invests.html already says "Nothing here is financial advice."
- No moving, copying or rebuilding the data pipelines; they stay in the stocks and vix repos (D6).
- No Net Worth Tracker pages, and none from the author's private project. Net Worth Tracker keeps only its home page card (D2).
- No sidebar entries for Composer Atlas, Net Worth Tracker or Automate Fundamentals (D18).
- No Composer Atlas links for concepts, only for Composer strategies (D17).
- No correcting out-of-date content during the move; a later roadmap item does that (D19).
- No cutting, trimming or summarizing content without the author's sign-off (core rule).
- No build step and no Node.js (Assumptions).
- No features that need a server, such as the template's page-feedback form, comments or a mailing list (Design details in DESIGN.md; template ratings).
- No rules, docs or design taken from azqato.github.io (D5).
- Nothing pushed, published or deployed until the author says so (D20).

## User stories

- As a learner, I want the stock metrics, methodology pages and FAQ in one place so that I can learn the basics without working out which site holds what.
- As a learner, I want the Finviz and Seeking Alpha setup guides as numbered steps so that I can follow them while setting up my own account.
- As a stock picker, I want the screener's table to use the full page width so that I can compare many columns at once.
- As a stock picker, I want the Market Overview to show the latest scheduled data so that I can see where the market stands today.
- As a strategy follower, I want today's VIX reading and what it means for the strategy so that I can follow the rules without doing the arithmetic myself.
- As a strategy follower, I want each Composer strategy write-up to link to its Composer Atlas page so that I can check its backtested numbers.
- As any visitor, I want to search every page from the top bar so that I can find a topic without knowing which section holds it.
- As any visitor, I want a button that switches between light and dark and remembers my choice so that the site is comfortable to read.
- As a visitor with an old bookmark, I want old stocks, vix and leverage addresses to land on the matching new page so that my links still work.
- As a visitor, I want referral links disclosed so that I know when a link can earn Azqato a reward.
- As a Discord member, I want the home page's "Join the Discord" button so that I can join the community.
- As the maintainer, I want every source page checked against an inventory after it moves so that I know nothing was lost.
- As the maintainer, I want the new pages to read the data the existing pipelines already publish so that I don't have to move or rebuild them.

## Feature list

### MVP (must ship)

Everything in the Site map, with the core rule's inventory check passed for each page:

- **Shell, on every page:** the top bar with the 💰 Azqato Invests name, search across every page and the ☀️/🌙 theme button (D10, D11); the sidebar with Learn, Tools, Strategies, Resources and FAQ (D12); breadcrumbs and previous/next links; an "On this page" list on reading pages but not on tool pages. azqato.com's top nav above it all, if D9 stays.
- **Home** (wiki-portal layout): the intro and "Join the Discord" button from invests.html, tiles into each section, and all 7 project cards with their text (D14, D18).
- **Resources:** all 15 curated categories with every link, referral links included, and the affiliate disclosure (D13).
- **Learn:** the landing page plus Philosophy, Stock metrics, Index & ETF methodology, the Finviz setup guide and the Seeking Alpha setup guide, from stocks.
- **FAQ:** from stocks, searchable as you type (D8, borrowed from help-center).
- **Strategies:** VIX Strategy (from vix), and the leveraged strategies landing page with 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA (from leverage). TQQQ FTLT, Holy Grail and HFEA keep their full write-ups, with Composer Atlas links (D15, D16).
- **Tools:** Screener and Market Overview (from stocks), VIX Dashboard and VIX Custom builder (from vix), reading the existing data feeds (D6).
- **Themes:** light and dark, starting from the visitor's system theme, with the choice saved in their browser (D10, Assumptions).
- **Redirects:** every old page under azqato.github.io/stocks/, /vix/ and /leverage/ redirects to its new home (D7). This means publishing, so it waits for the author's go-ahead (D20).

### Future (post-launch)

- Correct out-of-date content across the site, for example the Holy Grail page's missing factsheet numbers, which Composer Atlas now has (D19).
- Link HFEA to its entry in Atlas's community database once the way to link it is settled (To settle).
- sitemap.xml and robots.txt, once the site has pages and an address (D4).
- Retire the old repos (added 2026-10-02, at the author's request; much later, when the author decides to clean them out): the stocks and vix repos become redirects to this site plus data feeds only (P12).
- Ideas from docs/TODO.md, turned into Roadmap entries only with the author's say-so (Working Practice).

## Constraints

- **Static files only.** Plain HTML, CSS and JavaScript, with no build step, no Node.js, and Python only for scripts (Assumptions). There's no server, so nothing that needs one (forms that submit, accounts, comments) is possible.
- **No data feeds in this repo (author's rule, 2026-10-02; D21).** This repo only displays the site. It holds no data files, no scheduled jobs or GitHub Actions that fetch or generate data, and no scripts that pull market data into it. All data is read at page load from the feed repos (stocks and vix), which run on their own. The only automation allowed here is the GitHub Pages or Cloudflare Pages build that publishes the site. A new data need goes into a feed repo, never here.
- **The data stays where it is.** Stock data is read from raw.githubusercontent.com/Azqato/stocks/main/data/ and the VIX reading from azqato.github.io/vix/data/vix.js (D6). The VIX file can't come from raw GitHub, which serves it as plain text with `X-Content-Type-Options: nosniff`, so browsers won't run it (Background findings).
- **Hosting.** azqato.com serves only the azqato.github.io repo, as a Cloudflare Pages build, so this repo needs its own hosting or extra Cloudflare setup (Background findings). The address isn't decided (D4).
- **Local only.** Nothing is pushed, published or deployed until the author says so (D20). That includes the D7 redirects, which change the live source sites.
- **Content.** The core rule overrides everything: nothing from the sources is cut, trimmed or summarized without sign-off. The author's private project stays out of any public docs (D2, Assumptions).
- **Templates.** The design comes from Template Interface, the author's private template repo. Its documentation-site template keeps all its demo pages in one file switched by URL hash, so it has to be split into one file per page (Design details in DESIGN.md). Its shared tokens in theme.css are never redefined (DESIGN.md).
- **People and time.** One maintainer. The plan sets no deadline or budget.

## Assumptions

Correct any that are wrong.

- Same stack as your other sites: plain HTML, CSS and JavaScript, no build step, no Node.js, Python for data scripts.
- No accounts and no tracking. The theme choice is saved only in the visitor's own browser.
- The site starts in the visitor's system theme until they press ☀️/🌙.
- Dark mode uses azqato.com's colors so it matches the shared nav; light mode uses the template's. To re-check along with D9.
- When the documentation prompt reruns, this plan becomes the PRD, DESIGN and PATCHNOTES docs in this repo's own `docs/` folder. If the repo is ever made public, the docs leave out the author's private project. Done 2026-10-02 (P9.6): its name was removed from every doc.

Added by the 2026-10-01 audit:

- The home page uses the site's own light and dark themes; wiki-portal contributes its layout only, not its violet palette. This is read from D8's wording ("wiki-portal's directory layout") and is Question 9.
- Visitors use a current version of Edge, Chrome, Firefox or Safari. documentation-site's CSS uses the `:has()` selector (for smooth scrolling and for locking the page while the menu is open), which older browsers ignore.
- The source sites' browser caches move over with their tools: the Market Overview keeps a cached copy of its feed in localStorage, and the VIX pages keep the last reading under the key `vix_last_known` (read from the source code on 2026-10-01).

## Success criteria

1. **Nothing lost:** for each of the 20 source pages, 100% of the items on its inventory are found on the new site (the core rule's check, done page by page).
2. **Everything reachable:** all 21 pages are linked from the sidebar or the home page, and site search returns each page for its own title.
3. **Data current:** on a weekday, the VIX reading shown is the one the vix pipeline last committed, and the Screener and Market Overview show the stocks pipeline's latest data.
4. **No errors:** every page loads in headless Edge with 0 console errors and 0 broken internal links, in both themes.
5. **Readable:** every text and UI color pairing in both themes meets WCAG AA contrast: 4.5:1 for body text, 3:1 for large text.
6. **Fast:** in a mobile Lighthouse run, Home, the Screener and one strategy page reach an LCP of 2.5 s or less, a CLS of 0.1 or less and a TBT of 200 ms or less (targets set by the 2026-10-01 audit; see Metrics).
7. **Old links work:** once publishing is approved, each of the 19 old stocks, vix and leverage page addresses reaches its new page in one hop (D7).

## Tenets

Drafted by the 2026-10-01 audit from the core rule and the decisions, in priority order: when two conflict, the higher one wins. The author may reorder or reword them (Question 15).

1. **Preserve before polish.** Nothing from the four sources is cut, trimmed or summarized without the author's sign-off, even when it's repetitive, out of date (D19) or awkward to fit the template. When content and layout disagree, the layout changes. A cleaner page that lost a paragraph is a failed move.
2. **Local until told otherwise.** Nothing is pushed, published or deployed until the author says so (D20), not even a fix for something broken on a live site. Work is finished and verified locally, then waits. A ready change that sits unpublished costs nothing that can't be recovered; a publish can't be taken back.
3. **This repo sets its own rules.** Azqato Invests is independent (D5). Where azqato.github.io's docs, rules or design say something different, this repo's docs win. azqato.github.io is a source of facts, such as where a feed lives, never of rules.
4. **Reuse the feeds, don't move the pipelines.** Pages read the data the stocks and vix repos already publish, even when that's awkward, like loading the VIX reading from another site (D6). A second copy of a pipeline is a second thing to keep running.
5. **Template structure, source content.** Layout, navigation and styling come from the chosen Template Interface templates (D8); words, numbers, links and warnings come from the sources. Template demo content always comes out, and source content never does.
6. **No accounts, no tracking.** If a feature needs sign-in, a server or a way to follow visitors, it's out, even when it would make success easier to measure. Anything the site keeps stays in the visitor's own browser.

## Decisions

| # | Area | Decision |
|---|---|---|
| D1 | Scope | Merge [stocks](https://github.com/Azqato/stocks), [vix](https://github.com/Azqato/vix), [leverage](https://github.com/Azqato/leverage) and the current [invests.html](https://github.com/Azqato/azqato.github.io/blob/main/invests.html) into one site, Azqato Invests |
| D2 | Scope | Net Worth Tracker and the author's private project stay separate. Net Worth Tracker keeps its card on the home page; the private project stays private, as its own README requires. **Changed 2026-10-02 (P9.6):** the private project's name was taken out, because this repository will be public; the decision itself is unchanged, and the earlier wording isn't repeated here for the same reason |
| D3 | Scope | Everything follows the core rule above |
| D4 | Hosting | **Changed 2026-10-01.** The site's address isn't decided yet (see To settle); azqato.github.io links to it. **Decided 2026-10-01:** azqato.github.io/invests/, a GitHub Pages project site from a public repository named `invests` (Question 1). Before: the home address was azqato.github.io/invests.html, served as azqato.com/invests |
| D5 | Hosting | **Changed 2026-10-01.** Azqato Invests is its own independent repo, and this folder becomes it. azqato.github.io only links here; its rules, docs and design don't apply to this site. Before: the code lived in the azqato.github.io repo, with invests.html as the home page and the other pages in an `invests/` folder |
| D6 | Hosting | The data pipelines stay in the stocks and vix repos. The new pages read the stock data from GitHub, as the screener already does, and the VIX reading from the vix site (see Background findings) |
| D7 | Hosting | Every old page under azqato.github.io/stocks/, /vix/ and /leverage/ redirects to its new home. The old repos stay for data and history |
| D8 | Design | `documentation-site` for every inner page and `wiki-portal`'s directory layout for the home page, borrowing `help-center`'s searchable FAQ and step-by-step guides, `admin-dashboard`'s summary tiles and table styling for the tools, and `blog-article`'s reading-progress bar. The design comes from these Template Interface templates, not from azqato.github.io |
| D9 | Design | Every page shows azqato.com's top nav (Home, About, Discord, Invests, Codes, Music, Links, Projects, YouTube, Support) above the site's own top bar and sidebar. **To re-check:** this was decided when the site was going to live in the azqato.github.io repo (see To settle). **Confirmed 2026-10-01:** keep it |
| D10 | Design | Light and dark themes, switched with a ☀️/🌙 button |
| D11 | Design | The site's icon is 💰 |
| D12 | Content | Pages are grouped by topic: Learn, Tools, Strategies, Resources and FAQ (see Site map) |
| D13 | Content | All 15 curated resource categories come over with every link, referral links included, and the affiliate disclosure |
| D14 | Content | The home page keeps the "Join the Discord" button and all 7 project cards |
| D15 | Composer Atlas | When the site refers to a Composer.trade strategy, it links to [Composer Atlas](https://composeratlas.com) |
| D16 | Composer Atlas | TQQQ FTLT, Holy Grail and HFEA keep their full write-ups, each with a clear link to its match on Composer Atlas (listed under Composer Atlas below) |
| D17 | Composer Atlas | Only Composer strategies link to Atlas. Concepts are explained on this site, without Atlas links |
| D18 | Other projects | Composer Atlas, Net Worth Tracker and Automate Fundamentals appear as home page cards and in-page links, never in the sidebar |
| D19 | Content | Out-of-date content moves over as it is, and a roadmap item added later corrects all of it. For example, the Holy Grail page says no factsheet data was available, but Composer Atlas now has the numbers |
| D20 | Working practice | Once development starts, everything stays local until you say otherwise: nothing is pushed, published or deployed (decided 2026-10-01) |
| D21 | Hosting | **Changed again 2026-10-02 (Question 18, option D):** the site moves into the azqato.github.io repository, for now as one self-contained `invests/` folder (pages, assets, scripts, inventories and docs), served at https://azqato.com/invests/ by that repository's Cloudflare Pages build (and at azqato.github.io/invests/ by GitHub Pages). Separate repositories were only for the first build and testing. This local repository keeps its own history; the main repository gets the files as a new commit. Folding the files into the main site's own structure is a later step. The stocks and vix repositories still hold the data. Before: **Changed 2026-10-02:** the stocks repository stays the data source and is not the host. The site lives in its own new public repository named `invests` (D4, D5) with no data feeds in it; the stock data workflows and files stay in stocks (D6), and the site reads them from azqato.github.io/stocks/data/, which is the same origin as azqato.github.io/invests/. The stocks repository keeps GitHub Pages on for its data folder while its old pages become D7 redirects. Before: at publish time the author renames the [stocks](https://github.com/Azqato/stocks) repository to `invests`, and it becomes Azqato Invests: the new site replaces its pages, while its data workflows, data files and history stay. This serves the site at azqato.github.io/invests/ (D4) without a new repository, and the stock data becomes same-repo files (updates D6 for stock data; the VIX reading still comes from the vix site). GitHub Pages doesn't redirect after a rename, so a new, small `stocks` repository holds the D7 redirect pages for the old azqato.github.io/stocks/ addresses. Nothing is renamed until the author's go-ahead (D20) |

## Site map

21 pages from the 20 source pages (invests.html splits into Home and Resources).

```
Home                                from invests.html, address not decided (D4)
│
├── Learn                           landing, from stocks/index.html
│   ├── Philosophy                  stocks/philosophy.html
│   ├── Stock metrics               stocks/metrics.html
│   ├── Index & ETF methodology     stocks/indices.html
│   ├── Finviz setup guide          stocks/finviz.html
│   └── Seeking Alpha setup guide   stocks/seekingalpha.html
│
├── Tools
│   ├── Screener                    stocks/screener.html
│   ├── Market Overview             stocks/market.html
│   ├── VIX Dashboard               vix/strategy.html
│   └── VIX Custom builder          vix/custom.html
│
├── Strategies
│   ├── VIX Strategy                vix/index.html
│   └── Leveraged strategies        landing, from leverage/index.html
│       └── 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail, HFEA
│
├── Resources                       curated links, from invests.html
└── FAQ                             stocks/faq.html
```

**On every page:** the site's top bar with 💰 Azqato Invests, search across every page and the ☀️/🌙 button, under azqato.com's top nav if D9 stays.

**Home** (wiki-portal layout): the intro and "Join the Discord" button from invests.html, tiles into each section, and all 7 project cards with their text. The four cards that pointed to the old sites (Stocks, Stock Screener, VIX Strategy, Leveraged Strategies) now link inside the site; Automate Fundamentals, Composer Atlas and Net Worth Tracker link out.

**Inner pages** (documentation-site layout): the sidebar with the five sections, and the page itself with breadcrumbs, an "On this page" list and previous/next links.

DESIGN.md describes each layout in detail.

## What's being merged

| Source | Live now | Pages | Data |
|---|---|---|---|
| stocks | [azqato.github.io/stocks](https://azqato.github.io/stocks/) | 9: home, Philosophy, Metrics, Index & ETF methodology, Screener, Market Overview, FAQ, Finviz guide, Seeking Alpha guide | 6 GitHub Actions workflows: stock and ETF data daily, Market Overview 3 times a weekday, statements and index constituents weekly. The sixth, alert-on-failure.yml, is the failure alert (added 2026-10-01, Question 13; its trigger is read in P1 refreshes) |
| vix | [azqato.github.io/vix](https://azqato.github.io/vix/) | 3: About, Dashboard, Custom | 1 workflow updates the VIX reading 8 times a weekday |
| leverage | [azqato.github.io/leverage](https://azqato.github.io/leverage/) | 7: home, 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail, HFEA | None |
| invests.html | [azqato.com/invests](https://azqato.com/invests) | 1: intro with a Discord button, 7 project cards, 15 categories of curated links (some are referral links) | None |

20 pages in total. All four are plain HTML, CSS and JavaScript with no build step.

Added by the 2026-10-01 audit, read from GitHub that day:

- The files on each repo's main branch match the table. stocks: faq, finviz, index, indices, market, metrics, philosophy, screener and seekingalpha (.html). vix: custom, index and strategy. leverage: 3sig, 6sig, 9sig, hfea, holy-grail, index and tqqq-ftlt.
- stocks has six workflow files: alert-on-failure.yml, constituents.yml, market-overview.yml, screener-data-etfs.yml, statements.yml and stock-data.yml. The table's description covers the five data jobs; the sixth is alert-on-failure.yml, whose trigger wasn't read (Documentation Versus Reality, entry 3). vix has one, update-vix.yml. leverage has none.
- The sources are still changing. On 2026-10-01 the newest entry in stocks' patch notes was v4.9.6 (2026-09-29), and the main branches of stocks and vix both had commits from that day. Take each page's inventory when it moves, not from this table.

## Composer Atlas

Strategy link format: `https://composeratlas.com/strategies?slug=<slug>` (checked and live).

| Strategy here | On Composer Atlas |
|---|---|
| TQQQ For The Long Term | `tqqq-long-term` (original) and `zoops-tqqq-long-term-2026`, plus `zoops-upro-ftlt-2026`, its S&P 500 counterpart. The page already links the original. |
| Holy Grail | `holy-grail` (original) and `zoops-holy-grail-2026`. The page says no factsheet data was available; Atlas has the backtested metrics. |
| HFEA | No curated page. The Composer version the page cites (symphony `Cjb5ysKtJsPv6Tm3Fk0R`) is in Atlas's community database. |

3 Sig, 6 Sig and 9 Sig aren't Composer strategies, so they get no Atlas link.

invests.html and the leverage pages link to azqato.github.io/composer, a GitHub Pages copy. Those links change to composeratlas.com, the live site.

## Background findings

- **azqato.com only serves the azqato.github.io repo (affects D4).** azqato.com/invests is byte-for-byte the repo's invests.html, but azqato.com/stocks/, /vix/ and /leverage/ return 404. That repo's own docs say azqato.com is a Cloudflare Pages build of it, separate from GitHub Pages. A site in its own repo won't appear on azqato.com unless Cloudflare is set up to serve it too.
- **Moot since the D5 change: a page and a folder can share the name `invests`.** This was checked for the old D5. In the azqato.github.io repo, music.html sits next to a music/ folder, and both azqato.com/music and azqato.github.io/music serve the page.
- **The screener and Market Overview already load their data from GitHub (behind D6)** (raw.githubusercontent.com/Azqato/stocks/main/data/), with a local copy as fallback. Pages elsewhere can read the same feeds without moving any pipelines.
- **The VIX reading can't come from raw GitHub (affects D6).** The VIX pages load it as a script, `data/vix.js`. raw.githubusercontent.com serves files as plain text with `X-Content-Type-Options: nosniff`, so browsers refuse to run them as scripts. azqato.github.io/vix/data/vix.js serves the same file as JavaScript, and the vix site stays up anyway to hold the D7 redirects.
- **The data bots are busy (behind D6).** Stocks and vix schedule about 68 data runs a week (28 for stocks, 40 for vix). Each run that produces new data commits it to its repo, and each commit redeploys that repo's site.
- **The name is already in use.** The stocks sidebar reads "Azqato Invests / Individual Stocks" and links to azqato.com/invests; the vix nav links there too.

Added by the 2026-10-01 audit:

- **Template Interface's shared colors are azqato.com's dark colors (affects D9 and the dark theme).** Template Interface's theme.css defines a dark palette: canvas `#0d1117`, surface `#161b22`, border `#30363d`, text `#e6edf3` and `#8b949e`, accent `#00d4a0`, success `#3fb950`. These match azqato.com's dark colors except the accent's hover shade (`#22e6b5` in theme.css, `#00e6b0` on azqato.com). A dark theme built on the shared tokens and one built on azqato.com's colors therefore come out the same apart from that shade, whichever way D9 goes. documentation-site's own palette is light (a white page with emerald `#0b7a52`) and wiki-portal's is a dark violet. Details are in DESIGN.md.
- **The vix pages load Chart.js 4.4.0 from jsDelivr without an integrity hash** (strategy.html and custom.html). See Security.
- **The source sites keep only market data in the browser.** The Market Overview caches its feed in localStorage, and the VIX pages cache the last reading under `vix_last_known`. None of the scanned stocks and vix pages uses cookies.
- **The stocks fallback may not survive the move (affects D6).** The Screener and Market Overview fall back to a local copy of the data when raw GitHub fails. If that fallback is a relative path (not read in this audit), it finds nothing on this site, which has no data folder. To keep the feed's behavior (core rule), it would need a new target, such as the copy the stocks site serves under azqato.github.io/stocks/ (not checked). **Checked 2026-10-01 (P1):** the fallbacks are relative: screener.js and market.html list each feed as raw GitHub first, then `data/<file>`. https://azqato.github.io/stocks/data/ serves the same files as JSON with `Access-Control-Allow-Origin: *`, so it can replace the relative path (P6).

## Roadmap

### Current phase

**Update 2026-10-02, hosting decided (v0.18.0):** Question 18 answered with option D: the site merges into the azqato.github.io repository as an `invests/` folder, at https://azqato.com/invests/ (D21). Canonical links, og:url and sitemap.xml now use azqato.com's clean addresses (no .html). This repository's history was rewritten to remove the private project's name (Question 16). The files are committed to the main repository locally; nothing is pushed.

**Update 2026-10-02, P7 to P9 done (v0.17.0):** the site-wide checks, the documentation pass and the publish plan, at the author's request ("do everything up to finishing P9"). Nothing was pushed or published (D20). What each step found is under its phase in the Development plan. In short:
- P7: the inventories pass against a fresh snapshot; all 21 pages are reachable from the sidebar and found by title in search; 0 broken internal links, and 2 of the 96 outside links are dead (source content, listed for P11); every page carries all the sharing tags; Lighthouse (mobile, in Edge) passes on Home, the Screener and 9 Sig after one fix to the Screener's layout shift; the keyboard walk, drawer and search focus, landmarks and skip link work; no em dashes or secrets; feed text is now cleaned before it is shown as HTML. Steps 9 and 10 (showing the author the site, and the author's review of the drafted sections) wait for the author.
- P8: every PRD and DESIGN.md section was checked against the site and the verification checklist is dated; Conventions, the Runbook and Folder structure are filled in from the code; TODO.md holds only its placeholder.
- P9: canonical links, og:url and sitemap.xml use https://azqato.github.io/invests/; the redirect list for the 19 old addresses is under Deprecation and Removal; Deploy and Rollback are written in the Runbook; the private project's name is out of the docs and LICENSE.md names the issue tracker. Waiting on the author: Question 16 (the repository's history and the template files before it goes public) and Question 17 (azqato.com/invests and azqato.github.io/invests.html).
- Next: P7.9 and P7.10 with the author, then P10 only on the author's go-ahead.

**Update 2026-10-02, UI review fixes built and tested (v0.16.0):** every decision in docs/UI-REVIEW.md is built (its "Done" section lists each change and where it lives). Page width: option C, everything full width, chosen from three previews, which were then removed. Tested once everything was built: `python scripts/check.py` 21 pages, 0 failures; `python scripts/browser.py` 0 failures (the same 9 notes as before: the stocks feed's 2026-09-30 data and the VIX fallback findings). A probe found no text under 12px on any page at 1600px or 390px. Behavior checks in headless Edge: both VIX tools show LIVE with the same tier wording; the Custom builder shows the result first; the sidebar opens only the current group; the source footers are hidden and the VIX disclaimer sits in the site footer; the VIX table cells carry their labels on phones; the azqato.com bar is hidden on phones and its links are in the menu. Every page was scrolled through again in light and dark at 1440px and in light at 390px.

**Update 2026-10-02, UI review:** every page was scrolled through in headless Edge (light and dark at 1440px, light at 390px). The findings and suggested fixes are in docs/UI-REVIEW.md and wait for the author's decisions; nothing was changed.

**Update 2026-10-02, P2 to P6 tested; paused for the author:** the deferred tests ran after P6.
- `python scripts/check.py`: 21 pages, 0 failures (titles, links, demo text, dashes, inventories).
- `python scripts/browser.py` (new; headless Edge): 0 failures. Every page loads with no script errors or failed requests in light and dark, at 1280px and 390px, with no sideways scroll, and passes WCAG AA text contrast at 1280px. The skip link, drawer, search (`/`, Ctrl+K, results for every section), theme button and its saved choice, FAQ filter and FAQ answer links work. The tools load live data, and the screener falls back to azqato.github.io/stocks/data/ with raw GitHub blocked.
- Fixed on the way: the leverage risk notices laid out as a row (the template's `.callout` is flex), which pushed TQQQ FTLT and Holy Grail sideways on phones; light-theme data colors below AA, including the VIX ticker colors, which were hard-coded in the scripts and didn't follow the theme (DESIGN.md, Data colors); a dark-theme red badge at 4.1:1, already in the source.
- Findings for the author, not changed (source behavior):
  - The stocks feed's newest data was from 2026-09-30 5:48 PM when tested on 2026-10-02, so the 2026-10-01 runs hadn't landed; that's the stocks repo's job.
  - With only vix.js blocked and no cached reading, the VIX Dashboard stays on "Fetching data…": its allorigins fallback is refused by the browser (CORS). With every feed blocked it shows its error state, and with a cached reading it shows that.
- Next: the author's review, then P7.

**Update 2026-10-02, P6 built:** the four tools: Screener, Market Overview, VIX Dashboard and VIX Custom builder. P2 to P6 are all built; the testing deferred from each phase runs next.

**Update 2026-10-02, P5 built:** Strategies: the VIX Strategy, the leveraged strategies landing and the six strategies, with Composer Atlas links.

**Update 2026-10-02, P4 built:** Learn (6 pages) and the FAQ.

**Update 2026-10-02, P3 built:** Home and Resources, split from invests.html. The source snapshots were refreshed first (P1.4); no source had changed since 2026-10-01.

**Update 2026-10-02, P2 built:** the shell is built: every page shares one top bar, sidebar, breadcrumbs, pager, footer and search, in light and dark, generated by scripts/site.py from the source snapshots. Testing waits until P6 is built, at the author's request (P2.12). The Python scripts moved from `tools/` to `scripts/`, because the Tools section's pages live in `tools/`.

**Update 2026-10-02:** D21 added: the stocks repository will be renamed to `invests` and host the site at publish time (P9). Nothing changes until then. **Changed the same day:** stocks stays the data source only; the site gets its own `invests` repository with no data feeds (D21).

**Update 2026-10-01:** building started. P0 (setup) and P1 (source snapshots and inventories) are done; P2, the shell, is next.

**Paused 2026-10-01 (usage limits), where work stopped:** every open question (1 to 15) is answered and recorded under Risks and Open Questions. P0 and P1 are complete and committed to the local git repository (`main`, no remote). scripts/check.py now fails on em dashes in page text (Question 14). Nothing is in progress and there are no uncommitted changes. To resume: start Development plan P2 (the shell), first refreshing the source snapshots with `python scripts/snapshot.py` and `python scripts/inventory.py` if the sources have changed. The drafted sections stay marked as drafted until the author's review after the MVP (P7.10).

**Planning, with the docs set up.** The plan is complete apart from the open points under Risks and Open Questions. The first documentation audit ran on 2026-10-01 and moved the plan into these docs. Building starts when the author gives the go-ahead, and everything stays local until the author says otherwise (D20).

### Next steps (from the plan)

1. You say when to resume.
2. The documentation prompt reruns for this independent repo, and this plan moves into its docs.
3. You give the go-ahead to start building. Everything stays local until you say otherwise (D20).
4. Proposed build order:
   1. The shell: template, the ☀️/🌙 button, the 💰 icon, sidebar and search, plus azqato.com's nav in both themes if D9 stays.
   2. Home and Resources, from invests.html.
   3. Learn and FAQ, from stocks.
   4. Strategies, from leverage and vix.
   5. Tools: screener, Market Overview, VIX Dashboard and Custom builder, reading the existing data feeds.
   6. Check every page against its inventory (core rule). Switching the old addresses to redirects means publishing, so it waits for your go-ahead (D20).

Steps 1 and 2 were completed on 2026-10-01: the author said to resume, and the documentation audit moved the plan into these docs.

### Milestones

| # | Milestone | Target | Status |
|---|---|---|---|
| M1 | Plan: core rule, decisions D1-D20, site map, sources, template choice | 2026-10-01 | Complete |
| M2 | Documentation set (first audit) | 2026-10-01 | Complete |
| M3 | Go-ahead to build | When the author says | Complete 2026-10-01 |
| M4 | The shell | First, after M3 | Complete 2026-10-02 (P0 and P1 on 2026-10-01, P2 on 2026-10-02) |
| M5 | Home and Resources | After M4 | Complete 2026-10-02 (P3) |
| M6 | Learn and FAQ | After M5 | Complete 2026-10-02 (P4) |
| M7 | Strategies | After M6 | Complete 2026-10-02 (P5) |
| M8 | Tools | After M7 | Complete 2026-10-02 (P6) |
| M9 | Inventory check of every page | After M8 | In Progress: P7 checks and P8 done 2026-10-02; P7.9 and P7.10 wait for the author |
| M10 | Publish, with the D7 redirects | When the author says (D20) | In Progress: P9 (the publish plan) done 2026-10-02; P10 waits for the author's go-ahead and Questions 16 and 17 |
| M11 | Out-of-date content corrected (D19) | After launch | Planned |

### Feature breakdown per milestone

- **M1 Plan:** the core rule; decisions D1-D20; the 21-page site map; the Composer Atlas mapping; the inventory of the 20 source pages; background findings; the template ratings.
- **M2 Documentation set:** README.md as the front door; docs/PRD.md, DESIGN.md, PATCHNOTES.md and TODO.md; LICENSE.md.
- **M3 Go-ahead:** the author's say-so. Settling D9 first helps, since the shell carries the nav.
- **M4 The shell:** the template, the ☀️/🌙 button, the 💰 icon, sidebar and search, plus azqato.com's nav in both themes if D9 stays.
- **M5 Home and Resources:** from invests.html: the intro, "Join the Discord", section tiles, the 7 project cards, and the 15 resource categories with referral links and the disclosure.
- **M6 Learn and FAQ:** from stocks: the Learn landing page, Philosophy, Stock metrics, Index & ETF methodology, the Finviz and Seeking Alpha guides, and the FAQ.
- **M7 Strategies:** from leverage and vix: VIX Strategy, the leveraged landing page and the six strategies, with Composer Atlas links (D15, D16, D17).
- **M8 Tools:** Screener, Market Overview, VIX Dashboard and Custom builder, reading the existing data feeds (D6).
- **M9 Inventory check:** every page against its inventory (core rule).
- **M10 Publish:** choose the host and address (D4); publish; switch the old addresses to redirects (D7); add sitemap.xml and robots.txt where this site owns its origin; confirm the deploy against the local copy.
- **M11 Corrections:** one pass over out-of-date content (D19), for example the Holy Grail page's metrics, from Composer Atlas.

### Development plan

Every step and substep from the go-ahead (M3) to the correction pass (M11), written on 2026-10-01 at the author's request. Each phase lists what it needs before it starts, its steps, and what "done" means. Steps are numbered by phase (P0, P1 and so on) so they can be referred to and ticked off. The rules that apply throughout:

- Everything stays local until the author says otherwise (D20). Phases P0 to P9 are all local work; only P10 publishes, and only on the author's word.
- The core rule governs every page move: list everything first, move it, then check every item (Core rule).
- Testing follows Testing Cadence: make all of a phase's edits, then run the assumption check and one browser test at the end of the phase, not between edits.
- Each finished phase gets a PATCHNOTES.md entry and ticks the verification checklist for the sections it touched (Working Practice).
- Where a step needs an open question answered, it names the question and the default used if the author hasn't answered by then.

#### Phase overview

| Phase | Milestone | What it produces | Needs first |
|---|---|---|---|
| P0 | M3 | Answers to the blocking questions and a working setup | The author's go-ahead |
| P1 | M4 | Source snapshots and full page inventories | P0 |
| P2 | M4 | The shell: template, both themes, sidebar, search, theme button, icon | P1 |
| P3 | M5 | Home and Resources | P2 |
| P4 | M6 | Learn (6 pages) and FAQ | P2 |
| P5 | M7 | Strategies (8 pages) | P2 |
| P6 | M8 | Tools (4 pages) with live data | P2 |
| P7 | M9 | Site-wide checks: inventories, links, titles, accessibility, speed | P3 to P6 |
| P8 | M9 | Documentation brought in line with the built site | P7 |
| P9 | M10 | A publish plan ready to run | P8, Question 1 |
| P10 | M10 | The published site and the D7 redirects | P9 and the author's go-ahead to publish |
| P11 | M11 | Out-of-date content corrected (D19) | P10 |

P3 to P6 can run in any order once P2 is done; the order shown is the plan's build order (Next steps).

#### P0. Go-ahead and setup (M3)

Needs: the author's go-ahead to build.

1. **Settle what the shell depends on.** Ask the author, one question at a time:
   1. Question 2, azqato.com's nav (D9). Default if unanswered: keep it, in both themes.
   2. Question 3, the page addresses. Default: the proposed layout in step P0.3.
   3. Question 6, the brand in titles. Default: "Azqato Invests".
   4. Question 8, a skip link. Default: none, following Template Interface.
   5. Question 9, the home page colors. Default: the site's own themes.
   6. Question 10, the template's demo parts. Default: remove them.
   7. Record each answer in the section it affects, and mark the question answered under Risks and Open Questions.
2. **Decide about version control.** Ask Question 5 (the repository). Whatever the answer, nothing is pushed (D20).
   1. If the author wants a local git repository now: initialize it with `main` as the default branch, add `.gitattributes` (`* text=auto eol=lf`), and make a first commit of the docs. Update Repository Hygiene's current state.
   2. If not: work continues in the OneDrive folder, and each phase starts by copying the folder as a backup.
3. **Fix the folder layout.** Proposed, pending Question 3: one folder per section so each page has a short address.

   ```
   index.html                      Home
   resources/index.html            Resources
   learn/index.html                Learn landing
   learn/philosophy.html, metrics.html, indices.html, finviz.html, seekingalpha.html
   tools/screener.html, market.html, vix-dashboard.html, vix-custom.html
   strategies/vix.html             VIX Strategy
   strategies/leveraged/index.html Leveraged strategies landing
   strategies/leveraged/3sig.html, 6sig.html, 9sig.html, tqqq-ftlt.html, holy-grail.html, hfea.html
   faq.html                        FAQ
   assets/css/                     Template Interface's shared CSS, then the site's own
   assets/js/                      The site's scripts
   ```

   1. Write the chosen layout into Folder structure under Technical Requirements.
   2. Use relative links only, so the site works from any base path (Verification Environment).
4. **Check the tools.**
   1. Confirm Python 3 runs `python -m http.server 8000` from the folder.
   2. Confirm headless Edge runs at the path under Browser Testing.
   3. Confirm the GitHub CLI can still read `Azqato/templateinterface`, `Azqato/stocks`, `Azqato/vix` and `Azqato/leverage`.
5. **Write a check script** (Python, kept in the repository, for example `scripts/check.py`). It grows phase by phase and, at the end, checks: every page has a title within the Page Titles rules; every internal link resolves; no template demo text survives ("Parcelpoint", "API v3.4", "Get API keys"); no em dashes in this site's own text; every inventory item is present. It reads files only and changes nothing.

Done when: the blocking answers (or defaults) are recorded, the layout is written down, the tools run, and the check script exists.

#### P1. Source snapshots and inventories (M4)

Needs: P0. Sources keep changing, so this is redone for each page right before it moves (step P1.4).

1. **Snapshot the sources, read-only.** Download each source page from its repo's main branch with the GitHub CLI into a working folder outside the site (for example `_sources/`, listed in the ignore file if git is used). Never change the source repos.
   1. stocks: the 9 pages, plus the scripts and stylesheets they load.
   2. vix: the 3 pages, plus vix.js and their stylesheets.
   3. leverage: the 7 pages, plus their stylesheets.
   4. azqato.github.io: invests.html only.
   5. Record each repo's commit hash and the date in PATCHNOTES.md.
2. **Take an inventory of every page.** One file per page (for example `inventory/stocks-screener.md`), listing every item the core rule protects, in page order:
   1. headings and sections, with their text;
   2. paragraphs (first and last few words, so each can be found again);
   3. lists, tables (with row and column counts) and code;
   4. charts and what each plots;
   5. tools, controls, settings and defaults;
   6. data feeds, with their addresses and fallbacks;
   7. every link, with its destination, marking referral links;
   8. disclaimers, risk warnings and the affiliate disclosure, word for word;
   9. images, icons and emoji;
   10. scripts the page runs and what each does, including browser storage keys.
3. **Read what the audit couldn't.** While taking inventories, record:
   1. how each tool renders data and what it shows when every feed fails (Risks and Open Questions);
   2. whether the stocks fallback is a relative path (Background findings);
   3. whether any page inserts fetched text as HTML (Security);
   4. how the VIX charts present their numbers to screen readers (DESIGN.md);
   5. the tools' own colors (DESIGN.md, Data colors);
   6. any em dashes in source text, listed for the author, not changed (Question 14).
4. **Refresh before each move.** Right before a page moves, compare its source with the snapshot. If it changed, update the snapshot and the inventory first.

Done when: all 20 pages have inventories, and the findings in P1.3 are written into the PRD and DESIGN.md sections they belong to.

#### P2. The shell (M4)

Needs: P1. Produces one empty page that every other page is built from.

1. **Copy the template.** From Template Interface at a recorded commit, copy theme.css, base.css, components.css, documentation-site's styles.css and script.js, and wiki-portal's styles.css. Record the commit in PATCHNOTES.md. Never redefine a theme.css token.
2. **Split documentation-site into one file per page.** The template switches seven demo pages by URL hash in one file (Design details).
   1. Keep one page shell: top bar, sidebar, main column, "On this page", footer.
   2. Strip the hash routing from script.js, keeping its other behavior (drawer, search dialog, "On this page" tracking, copy buttons if any code remains).
   3. Remove the demo-only parts: the API keys button, status line, version label, code-language tabs, feedback form and the "Back to Template Interface" bar (Question 10).
   4. Remove all demo text and the template's title.
3. **Build the top bar.**
   1. The 💰 Azqato Invests logo, linking to Home (D11).
   2. The search button, kept with its / and Ctrl+K shortcuts.
   3. The ☀️/🌙 button (D10), with an accessible name that says what it does.
   4. If D9 stays: azqato.com's nav above the top bar, as a copy with links back to azqato.com, Invests marked current. Record it under Repository Hygiene as a copied file with its source.
4. **Build the sidebar.** The five groups, Learn, Tools, Strategies, Resources and FAQ (D12), with every page from the Site map. No entries for Composer Atlas, Net Worth Tracker or Automate Fundamentals (D18). Mark the current page. Give the sidebar a label that fits this site.
5. **Add the dark theme.**
   1. Give every `--pp-*` token a dark value under a dark-theme selector, starting from the role pairings in DESIGN.md.
   2. Override every literal color listed in DESIGN.md (white backgrounds, white text, inline code, tags, shadows, scrims).
   3. Give solid buttons dark text in dark (white on the dark accent fails contrast).
   4. If D9 stays, give azqato.com's nav a light version.
6. **Make the theme button work.**
   1. Start in the visitor's system theme.
   2. Save the choice in the visitor's own browser when the button is pressed.
   3. Apply the saved theme with a small script in the page head, before the page draws, so it never flashes.
   4. Decide which emoji the button shows in each theme, and record it in DESIGN.md.
7. **Add the favicon.** 💰 as an inline SVG data URI, the technique azqato.com uses (Design details). The template's favicon.png doesn't come over.
8. **Build the search index.** Read how the template's script.js searches, then make it search all 21 pages: titles, headings and text. Choose between a hand-kept index file and one the check script generates, and record the choice in Technical Requirements.
9. **Add breadcrumbs, pager and footer.** Breadcrumbs from the site map; previous and next following the sidebar order; footer content decided with the author.
10. **Make a tool-page variant** without "On this page" and with the 760px content cap lifted (Design details).
11. **Make the home page shell** from wiki-portal's layout, in the site's themes (Question 9). Settle the drawer width difference (900px against 760px) noted in DESIGN.md.
12. **Test the shell** (major update): assumption check, then one headless Edge run of the empty page and the home shell in both themes, at desktop and phone widths: no console errors, the drawer opens and closes, search opens from the keyboard, the theme survives a reload, focus is visible everywhere, and every color pairing passes the contrast check.

Done when: an empty inner page, a tool page and the home shell all pass P2.12, and DESIGN.md's verification checklist rows for palette, typography, spacing, breakpoints and components are ticked.

**Built 2026-10-02** (testing waits for the end of P6, at the author's request, so "done" waits for P2.12):

1. Template Interface had moved on to commit ed840da ("Finish M18 dark mode...", v0.15.0) since the 61acfcb read on 2026-10-01. The copies come from ed840da: theme.css, base.css and components.css unchanged, and documentation-site's styles.css as assets/css/docs.css, unchanged. The template now has its own dark mode (`:root[data-theme="dark"] .pp-page`), so P2.5 uses it rather than building one from the shared tokens. The snapshot is in `_sources/templateinterface/`.
2. Split into one file per page. assets/js/site.js keeps the template script's drawer, "On this page", search and keyboard shortcuts; the hash routing, code tabs, copy buttons and feedback form are gone. The demo parts and text never come over: the shell is written fresh in scripts/site.py.
3. Top bar: 💰 Azqato Invests linking to Home, search with / and Ctrl+K, and the theme button. azqato.com's nav sits above it (D9), as a copy with every link pointing back to azqato.com and Invests marked current.
4. Sidebar labeled "Site sections": Home, then Learn, Tools, Strategies (the six leveraged strategies indented under Leveraged strategies), Resources and FAQ. No Composer Atlas, Net Worth Tracker or Automate Fundamentals entries (D18). A small card at its foot repeats "Educational use only. Not financial advice." from the source sidebars.
5. Dark theme: the template's own dark tokens. The moved content's colors are mapped to the site's tokens in site.css; data colors keep the source values in dark and get darker counterparts in light (DESIGN.md, Data colors). azqato.com's nav has a light version.
6. Theme button: assets/js/theme.js, adapted from the template's theme-toggle.js. Starts in the visitor's system theme, saves the choice under `azqato-invests-theme` in the visitor's browser, applies it in the head before the page draws, and shows the theme it switches to (☀️ while dark, 🌙 while light), with the accessible name "Switch to light theme" or "Switch to dark theme".
7. Favicon: 💰 as an inline SVG data URI.
8. Search: scripts/site.py generates assets/js/search-index.js (every page's title, h2 and h3 sections and their text; about 310 KB), which site.js loads the first time search opens. Chosen over a hand-kept index so it can't drift from the pages.
9. Breadcrumbs from the site map; previous and next follow the sidebar order; footer (default, for the author to change): the brand, "Educational use only. Not financial advice. Some links are referral links.", links to Resources and the FAQ, and "Built by Azqato".
10. Tool pages (`is-tool`) have no "On this page" and no 760px cap.
11. Home uses the same shell as the inner pages, with the content capped at 1120px (wiki-portal's width) and no "On this page". That settles the drawer difference: Home switches to the drawer at 900px like every page.
12. Not run yet (after P6).

Added beyond the plan: a "Skip to content" link (Question 8), and scripts/site.py itself, which builds every page from the snapshots (Technical Requirements, System architecture).

#### P3. Home and Resources (M5)

Needs: P2, and the invests.html inventory from P1.

1. **Refresh** invests.html's snapshot and inventory (P1.4).
2. **Split invests.html between two pages** (it becomes Home and Resources). Mark each inventory item with the page it goes to. Nothing is left unassigned.
3. **Build Home.**
   1. The intro and the "Join the Discord" button (D14).
   2. Tiles into Learn, Tools, Strategies, Resources and FAQ.
   3. All 7 project cards with their full text (D14, D18). Stocks, Stock Screener, VIX Strategy and Leveraged Strategies now link inside the site; Automate Fundamentals, Composer Atlas and Net Worth Tracker link out.
   4. Composer Atlas links go to composeratlas.com, not the old azqato.github.io/composer copy (Composer Atlas).
   5. Optional, from wiki-portal's rating: a live VIX reading in the statistics list, read from the same feed as the VIX pages.
4. **Build Resources.** All 15 categories with every link, referral links included, and the affiliate disclosure word for word (D13).
5. **Write titles and share tags.** Home: "Azqato Invests - Investing Tools and Resources" (proposed). Resources: "<name> - Azqato Invests". og:title, og:description and the other tags follow Social Sharing Tags; og:url waits for the address (Question 1).
6. **Check both inventories** item by item against the new pages, then run the phase's browser test.

Done when: every invests.html item is on Home or Resources, and both pages pass the browser test in both themes.

**Built 2026-10-02** (the inventory check and browser test run after P6):

1. Refreshed: stocks 60a599e, vix cd92561, leverage c86321c and azqato.github.io 58767b5, all unchanged since 2026-10-01.
2. The split (scripts/site.py, `split_invests`): Home gets the intro (the "Azqato Invests" heading, the paragraph, "Join the Discord" and "Explore the projects") and the Projects section; Resources gets the Curated Resources section with its disclaimer. Both keep the source footer, "Built by Azqato." azqato.com's own nav at the top of invests.html becomes the site's copy of it (D9).
3. Home: the intro; "Explore the site", five tiles into Learn, Tools, Strategies, Resources and FAQ (new text, this site's own); all 7 project cards with their full text. Stocks, Stock Screener, VIX Strategy and Leveraged Strategies now open the site's own pages in the same tab; Automate Fundamentals, ComposerAtlas (now composeratlas.com) and Net Worth Tracker still open outside in a new tab. "Join the Discord" points to azqato.com/discord, since the source's relative `discord.html` only worked on azqato.com. The optional live VIX statistic wasn't added.
4. Resources: all 15 categories and all 71 links, referral links included, with the disclaimer word for word. Its heading, "Curated Resources", becomes the page's h1.
5. Titles: "Azqato Invests - Investing Tools and Resources" and "Curated resources - Azqato Invests". Home keeps invests.html's description; Resources has a new one. og:title, og:description, og:site_name and twitter:card are set; og:url and canonical wait for the address (P9).
6. After P6.

#### P4. Learn and FAQ (M6)

Needs: P2, and the stocks inventories.

1. **For each page** (Learn landing from stocks/index.html, then Philosophy, Stock metrics, Index & ETF methodology, the Finviz guide, the Seeking Alpha guide):
   1. Refresh the snapshot and inventory.
   2. Move every section into the documentation-site article layout, keeping the wording exactly.
   3. Turn the setup guides' steps into numbered steps (help-center's pattern, D8) without changing their text.
   4. Rewrite links between source pages to the new addresses; leave outside links as they are.
   5. Write the title and share tags.
   6. Check the inventory.
2. **Build the FAQ** from stocks/faq.html, the largest page.
   1. Every question and answer, word for word, in source order.
   2. Search-as-you-type over the questions (help-center's pattern, D8).
   3. Anchors so each answer can be linked.
3. **Check "On this page"** lists match each page's headings.
4. **Run the phase's browser test.**

Done when: all 7 pages pass their inventories and the browser test.

**Built 2026-10-02** (inventory checks and the browser test run after P6):

1. Learn landing (from stocks/index.html), Philosophy, Stock metrics, Index & ETF methodology, the Finviz guide and the Seeking Alpha guide.
   1. Refreshed with the P3 refresh; unchanged.
   2. Each page's content moved whole, wording unchanged, with its own section ids, so old anchors such as `metrics.html#metric-peg-fwd` still work at the new address.
   3. The two setup guides already number their steps (`guide-step` with `step-num`), the same pattern help-center uses, so their markup moved as it is.
   4. Links between source pages point to the new addresses (relative links, such as `metrics.html` from another Learn page, or `../faq.html#palantir`); outside links are unchanged.
   5. Titles: "<label> - Azqato Invests" (the Learn landing is "Learn - Azqato Invests"); each keeps its source description.
   6. After P6.
2. FAQ (from stocks/faq.html): all 37 questions and answers in source order, in the source's accordion (stocks' script.js, copied). The source has no section headings, so the page has no "On this page" list.
   1. Word for word, in source order.
   2. A "Filter the questions" box under the heading hides questions that don't contain every word typed, and announces the count (help-center's search-as-you-type).
   3. Each answer keeps its source id; site.js opens the answer a link points to (for example `faq.html#palantir`).
3. "On this page" is built from each page's h2 headings when the page loads (site.js); headings without an id get one from scripts/site.py.
4. After P6.
#### P5. Strategies (M7)

Needs: P2, and the vix and leverage inventories.

1. **VIX Strategy** from vix/index.html: every section; the last-known reading painted from browser storage as the source does; links to the VIX Dashboard and Custom builder at their new addresses.
2. **Leveraged strategies landing** from leverage/index.html.
3. **The six strategies**: 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA. For each:
   1. Every section, keeping the source's structure and wording (Overview, Rules and Logic, Performance Notes, Risks and Caveats, Resources where the source has them).
   2. Risk warnings kept in full.
   3. Composer Atlas links (D15, D16, D17): TQQQ FTLT to `tqqq-long-term`, `zoops-tqqq-long-term-2026` and `zoops-upro-ftlt-2026`; Holy Grail to `holy-grail` and `zoops-holy-grail-2026`; HFEA to its community-database entry, symphony `Cjb5ysKtJsPv6Tm3Fk0R`, once the link format is confirmed (Question 4); 3 Sig, 6 Sig and 9 Sig none.
   4. Old azqato.github.io/composer links changed to composeratlas.com (core rule: allowed).
   5. Out-of-date content left as it is (D19), noted for P11.
4. **Check every inventory, then run the phase's browser test.**

Done when: all 8 pages pass their inventories and the browser test, and every Atlas link opens the right strategy.

**Built 2026-10-02** (inventory checks, the browser test and opening each Atlas link run after P6):

1. VIX Strategy (strategies/vix.html, from vix/index.html): every section; the source's inline script still paints the last-known reading from `vix_last_known` first, then loads https://azqato.github.io/vix/data/vix.js (D6) with vix.js and strategy.js from assets/js/vix/. Its "View Live Strategy" link opens the VIX Dashboard at its new address. The source page links only to the Dashboard in its content; the Custom builder is in the sidebar.
2. Leveraged strategies landing (strategies/leveraged/index.html), with its links to the six strategies.
3. The six strategies, each with its source sections (Overview, Rules and Logic, Performance Notes, Risks and Caveats, Resources) and risk warnings in full.
   1. As in the source.
   2. Kept in full.
   3. An "On Composer Atlas" note sits above the first section: TQQQ FTLT links `tqqq-long-term`, `zoops-tqqq-long-term-2026` and `zoops-upro-ftlt-2026` (the page's own link to `tqqq-long-term` stays too); Holy Grail links `holy-grail` and `zoops-holy-grail-2026`. **HFEA (Question 4):** Composer Atlas has no address for a single community-database entry (its code, read 2026-10-02, reads no entry from the address), so the note links the database page, composeratlas.com/database.html, and names symphony `Cjb5ysKtJsPv6Tm3Fk0R` to search for. Change it if Atlas adds entry links. 3 Sig, 6 Sig and 9 Sig get none.
   4. The old azqato.github.io/composer links were only in the leverage sites' navigation, which the shell replaces; scripts/site.py would change any in content to composeratlas.com.
   5. Out-of-date content is unchanged (D19), including the Holy Grail page's note that no factsheet data was available; it waits for P11.
4. After P6.

The leverage pages' main.js isn't carried: it only drove their sidebar's "On This Page" highlighting and the mobile menu, which the shell does now.
#### P6. Tools (M8)

Needs: P2, the stocks and vix inventories, and the P1.3 findings.

1. **Screener** from stocks/screener.html, on the tool-page variant.
   1. Keep every filter, column, preset, sort and the click-for-breakdown view.
   2. Read data from raw.githubusercontent.com/Azqato/stocks/main/data/ (D6).
   3. Repoint the local fallback if P1.3 found it relative (Background findings).
   4. Apply admin-dashboard's table styling (D8) without dropping any column.
2. **Market Overview** from stocks/market.html: same feed; keep its browser cache key and behavior.
3. **VIX Dashboard** from vix/strategy.html and **VIX Custom builder** from vix/custom.html.
   1. Load the reading from https://azqato.github.io/vix/data/vix.js, never raw GitHub (D6, nosniff).
   2. Keep the allorigins fallback and the `vix_last_known` cache.
   3. Keep Chart.js 4.4.0; add an integrity hash if the author agrees (Question 12).
   4. Live numbers change without animation (DESIGN.md).
4. **Make the charts and tables work in both themes**: chart colors, grid lines and text readable in light and dark; record the tools' colors in DESIGN.md.
5. **Test each failure path**: block each feed in turn in headless Edge and confirm the page falls back as the source does.
6. **Check data freshness**: the shown timestamps match the newest data commits in stocks and vix.
7. **Check every inventory, then run the phase's browser test.**

Done when: all 4 tools show current data in both themes, fall back correctly, and pass their inventories.

**Built 2026-10-02** (steps 5 to 7 are tests and run with the rest after P6):

1. Screener (tools/screener.html), on the tool-page variant.
   1. Every universe button, filter, column, preset, sort, the breakdown modal and the methodology modal, moved whole with their ids, so screener.js (copied to assets/js/stocks/) works unchanged. Its links to the Metrics glossary and the Indices methodology still open in a new tab, as in the source, so the screener keeps its state.
   2. Data still comes first from raw.githubusercontent.com/Azqato/stocks/main/data/ (D6).
   3. The relative `data/` fallback now points to https://azqato.github.io/stocks/data/ (Background findings), in screener.js and every fallback path.
   4. The source's own table styles are kept, scoped, with the template's table colors; no column is dropped. admin-dashboard's table styling wasn't copied in (its code wasn't read); revisit at the author's review.
   The screener was a full-window app (its own scroll regions, `overflow: hidden` on the page); here it sits in the page and scrolls with it.
2. Market Overview (tools/market.html): same feed and fallback change; its inline script, cache key and behavior are unchanged.
3. VIX Dashboard (tools/vix-dashboard.html) and VIX Custom builder (tools/vix-custom.html).
   1. The reading loads from https://azqato.github.io/vix/data/vix.js (D6).
   2. vix.js is unchanged apart from em dashes in its comments: the allorigins fallback and the `vix_last_known` cache stay.
   3. Chart.js 4.4.0 with an integrity hash (`sha384-e6nUZLBk...`, computed 2026-10-02 from the jsDelivr file) and `crossorigin="anonymous"` (Question 12).
   4. Live numbers: the source's own behavior is kept. The donut chart's draw animation is the source's and stays.
4. Charts in both themes: the donut's center text, label color and segment border read the theme's colors (assets/js/vix/chart.js, a marked change); the ticker colors keep their source values in dark and take darker ones in light (DESIGN.md, Data colors). Contrast is checked in the test.
5. to 7. After P6.
#### P7. Site-wide checks (M9)

Needs: P3 to P6.

1. **Inventories**: re-run every page's inventory against a fresh source snapshot; 100% of items found (Success criteria 1).
2. **Reachability**: all 21 pages linked from the sidebar or Home; search finds each by its title (Success criteria 2).
3. **Links**: 0 broken internal links; outside links spot-checked.
4. **Titles and tags**: the check script's Page Titles and Social Sharing Tags checks pass, counted by script.
5. **Accessibility**: contrast of every pairing in both themes; keyboard-only walk through each page type; focus into and out of the drawer and search dialog; landmarks; the skip-link decision applied.
6. **Speed**: Lighthouse in Edge DevTools, mobile, on Home, the Screener and one strategy page: LCP 2.5 s or less, CLS 0.1 or less, TBT 200 ms or less.
7. **Writing style sweep** of this site's own text; source text reported, not changed.
8. **Security pass**: no fetched text inserted as HTML, `rel="noopener"` on new-tab links, no secrets anywhere.
9. **Show the author** the finished site locally and collect changes.
10. **Author review of the drafted sections** (Question 15): tenets, personas, user stories, goals, success criteria, metrics, press release and FAQ, updated to match the built MVP.

Done when: every check passes or each exception is approved by the author and recorded.

**Done 2026-10-02 (steps 1 to 8), in headless Edge and with the check scripts:**

1. Inventories: `python scripts/snapshot.py` took fresh snapshots (stocks 860ee2b9, vix 37eeadd1, leverage c86321cd, azqato.github.io 58767b54, the same commits as the last build), then `python scripts/inventory.py`, `python scripts/site.py` and `python scripts/check.py`: 21 pages, every inventory item found, 0 failures.
2. Reachability: all 21 pages are linked from the sidebar on every page (and from Home); the search index holds every page under its title.
3. Links: 0 broken internal links (check.py). Outside links: all 96 unique addresses were requested once each. 86 answered normally. 8 refused automated requests (403 from Investopedia twice, TheStreet twice, study.com and AAII; 503 from Zacks; Renaissance Capital refused a HEAD request), which is bot blocking, not a dead page. 2 are dead, both on Resources from invests.html: dividendstocksonline.com (expired security certificate, in Edge too) and www.denvercondomania.com (the connection times out, in Edge too). They're source content, so they stay as they are and are listed for P11 (D19).
4. Titles and tags: check.py's title checks pass on all 21 pages (20 to 46 characters). Every page has a description, og:title, og:description, og:type, og:site_name and twitter:card; og:url and the canonical link were added in P9.2, so all six sharing tags are now on every page.
5. Accessibility: Lighthouse accessibility 100 on all three pages measured; WCAG AA text contrast on every page in both themes is part of `python scripts/browser.py`. Keyboard walk on a Learn page: the first Tab reaches "Skip to content", Enter moves to `#pp-main`, then focus runs through the breadcrumbs, the inline "On this page" list and the sidebar in screen order, with a visible solid focus ring. `/` puts focus in the search box, results appear as you type, and Escape closes it and returns focus to where it was. On a phone-width page the menu button moves focus to the drawer's close button and sets `aria-expanded` to true; Escape closes the drawer, returns focus to the menu button and sets it back to false. Landmarks: one header, main, aside and footer, four labeled navigation regions, one h1, `lang="en"`. No button, link or field without an accessible name on Home, the Screener or the VIX Custom builder.
6. Speed: Lighthouse 13.5.0 from the command line (`npx lighthouse`, mobile settings) driving Edge, against the local server. Home: LCP 1.7 s, CLS 0, TBT 0 ms (performance 99). 9 Sig: LCP 1.7 s, CLS 0, TBT 0 ms (99). Screener: LCP 2.1 s, TBT 0 ms, but CLS 0.175 on the first run: the disclaimer under the table moved down when the data arrived. Fixed by holding 70vh of room for the table while it loads (assets/css/site.css); rerun: CLS 0.003. Best practices and SEO scored 100 on all three. Lighthouse's remaining suggestions (minify CSS and JavaScript, unused CSS, cache lifetimes) need a build step or host settings and weren't acted on.
7. Writing style: no em dashes in this site's own text (scripts/site.py, site.css, site.js, README.md, the docs) or in any page (check.py); no filler words found in the interface text. Source text was left as it is.
8. Security: every new-tab link carries `rel="noopener"`; no keys, tokens or passwords anywhere in the repository. The screener and Market Overview built rows and cards from feed text with `innerHTML` and no escaping (found in P1). Fixed: scripts/site.py now wraps their `res.json()` in `azqClean()`, which removes `<` and `>` from every text value in a fetched feed before the page uses it; company names and tickers never contain them. The other `innerHTML` uses build markup from the scripts' own constants or from numbers (the VIX tools and site.js, which escapes its search text).
9. Waiting for the author.
10. Waiting for the author.

#### P8. Documentation (M9)

1. Check every PRD and DESIGN.md section against the built site and tick the verification checklist with dates.
2. Record discrepancies under Documentation Versus Reality.
3. Fill in Conventions from the code, the Runbook from what was actually run, and Folder structure from the real tree.
4. Check docs/TODO.md and ask the author about any ideas (Working Practice).
5. Write the PATCHNOTES.md entry for the build.

**Done 2026-10-02:** 1. every section on the verification checklist was checked against the site and dated; 2. new discrepancies are under Documentation Versus Reality (entries 9 to 12), and entries 5, 7 and 8 are resolved; 3. Conventions, the Runbook and Folder structure are rewritten from the code and from what was run; 4. TODO.md holds only its placeholder, so there was nothing to ask; 5. PATCHNOTES.md v0.17.0. Also brought up to date: the milestone table, System architecture, Tech stack, Security, Repository Hygiene, Social Sharing Tags and Deprecation and Removal.

#### P9. Publish plan (M10)

Needs: P8 and an answer to Question 1 (the address). Prepares; publishes nothing.

1. Host decided (Question 1): GitHub Pages, from a public repository named `invests`, served at azqato.github.io/invests/. **Updated again 2026-10-02 (D21 changed):** a new repository, not the renamed stocks repository; stocks keeps its data and its Pages site for the data folder. Earlier note, superseded: Before the rename: list everything that reads azqato.github.io/stocks/ or the stocks repo by name (raw GitHub data addresses in the screener and other pages, the vix repo, workflows, azqato.com's links) and repoint it; plan the new `stocks` redirect repository; decide how this local repository's history joins the renamed one (commit the built site onto it, keeping the workflows and data folders). Before publishing: check how GitHub Pages resolves /invests/ next to azqato.github.io's invests.html, and what azqato.com (the Cloudflare build of azqato.github.io) serves at /invests/. Write Deploy and Rollback in the Runbook.
2. Fill og:url and canonical links with the final address.
3. Write robots.txt (fully open, with its comment) and sitemap.xml, if this site owns its origin.
4. Make the D7 redirect list: each of the 19 old addresses to its new page, one hop each. Choose the mechanism for the host the old sites use (redirect pages on GitHub Pages, to confirm).
5. Decide with the author what happens to azqato.com/invests (Question 1).
6. Answer Question 5 (the repository) and, if public, remove the private project's name from the docs first; add the issue tracker's address to LICENSE.md.

**Done 2026-10-02 (prepared, nothing published):**

1. Host: GitHub Pages from github.com/Azqato/invests (created by the author, private for now), served at https://azqato.github.io/invests/. Deploy and Rollback are written in the Runbook. How GitHub Pages resolves azqato.github.io/invests/ next to azqato.github.io's own invests.html can only be seen once both exist; Question 17 recommends retiring invests.html so the two never compete.
2. og:url and the canonical link are on every page, from `SITE_URL` in scripts/site.py (folder pages end in `/`, for example https://azqato.github.io/invests/learn/).
3. sitemap.xml lists all 21 pages, generated by scripts/site.py. No robots.txt: azqato.github.io owns the origin, so crawlers only read https://azqato.github.io/robots.txt, which belongs to the azqato.github.io repo. Licensing's rule (fully open, with a comment) applies there if that repo adds one.
4. The D7 redirect list (19 addresses, plus invests.html) and the mechanism are under Deprecation and Removal.
5. azqato.com/invests: needs the author's decision, Question 17, with a recommendation.
6. Question 5 answered (github.com/Azqato/invests, public later): the private project's name is out of the docs, and LICENSE.md gives https://github.com/Azqato/invests/issues as the place for permission requests. Before the repository goes public, Question 16.

#### P10. Publish (M10)

Only on the author's explicit go-ahead (D20).

1. Push and deploy.
2. Confirm the deploy: fetch every deployed file and compare it with the local copy.
3. Check the live site's data feeds and both themes.
4. Switch the old stocks, vix and leverage pages to redirects, keeping vix/data/vix.js and every data file serving (D6).
5. Check each of the 19 old addresses lands on its page in one hop (Success criteria 7).
6. Link the new site from azqato.github.io as decided.
7. Set up the metrics that need no tracking (Metrics) and start the 4-week baseline.

#### P11. Corrections (M11)

1. Gather every out-of-date item noted during P4 to P6.
2. Correct each with the author's approval, for example the Holy Grail metrics from Composer Atlas (D19).
3. Record each correction in PATCHNOTES.md.

### Explicitly deferred

- **Correcting out-of-date content (D19):** waits until after the move, so each page is first checked against unchanged source text.
- **Redirects and publishing (D7, D20):** wait for the author's go-ahead, because they change live sites.
- **HFEA's Composer Atlas link:** waits until the way to link Atlas's community database is settled.
- **sitemap.xml and robots.txt:** wait for pages and an address (D4); see Folder structure under Technical Requirements. **Done 2026-10-02 (P9.3):** sitemap.xml is generated; robots.txt isn't this site's to write.
- **Atlas links for concepts (D17):** declined; concepts are explained on this site.
- **Merging Net Worth Tracker and the author's private project (D2):** declined; they stay separate.

### Future updates

Ideas from docs/TODO.md become entries here only with the author's say-so, following the five steps under Working Practice.

#### P12. Old repos become feeds and redirects (post-launch; added 2026-10-02)

Runs after P10, whenever the author decides to clean out the old repos. Each repo keeps running on its own; this site only reads from it (D21).

1. stocks: its pages become redirects to this site (D7); its scheduled jobs and data/ stay as the data feed.
2. vix: the same, and its feed gets a second copy for fallback. Found in the 2026-10-02 browser test: when data/vix.js on azqato.github.io fails and the visitor has no cached reading, the VIX pages stay on "Fetching data…", because the allorigins fallback is refused by the browser (CORS).
   1. Load the same file from raw.githubusercontent.com/Azqato/vix/main/data/ as the second source. Optionally the vix job also writes data/vix.json, so it can be read as data rather than run as a script (raw GitHub won't run vix.js; Constraints).
   2. Drop the allorigins fallback.
   3. With every source down, show the cached reading if there is one, otherwise a clear "unavailable" state.
3. Remove the leverage sites' pages the same way, as redirects (D7).
4. Record each change in PATCHNOTES.md and in the old repos' own notes.

### Verification checklist

Each PRD and DESIGN.md section that describes the code, and when it was last checked in full against the code. Every section was checked against the built site on 2026-10-02 (P8.1); what didn't match is under Documentation Versus Reality.

| Section | Status |
|---|---|
| PRD: Folder structure (current tree) | Verified 2026-10-02 against the folder listing (P8) |
| PRD: Repository Hygiene (current state) | Verified 2026-10-02: local git repository on `main`, no remote; `.gitattributes` and `.gitignore` present; github.com/Azqato/invests exists but isn't connected |
| PRD: What's being merged (source page lists) | Verified 2026-10-02 against fresh snapshots of stocks, vix, leverage and azqato.github.io (P7.1) |
| PRD: System architecture | Verified 2026-10-02 against scripts/site.py and the built pages |
| PRD: Tech stack | Verified 2026-10-02: no manifests; Python 3.14.3, bs4, Playwright; Lighthouse through npx for P7 only |
| PRD: Data models | Verified 2026-10-02 for what the pages read (addresses and storage keys); the feeds' schemas belong to the stocks and vix repos |
| PRD: API design (internal data flow) | Verified 2026-10-02 against the built tools and browser.py's feed tests |
| PRD: State management | Verified 2026-10-02: three localStorage uses, no cookies |
| PRD: Third-party integrations | Verified 2026-10-02 against the hosts the built pages request |
| PRD: Performance requirements | Verified 2026-10-02 with Lighthouse on Home, the Screener and 9 Sig (P7.6) |
| PRD: Security | Verified 2026-10-02 (P7.8) |
| PRD: Runbook | Verified 2026-10-02: every local command was run; Deploy and Rollback are written but not run (D20) |
| PRD: Page Titles and Social Sharing Tags | Verified 2026-10-02 by script on all 21 pages (P7.4) |
| PRD: Deprecation and Removal (public surface) | Verified 2026-10-02 against the snapshots' page lists; nothing published |
| DESIGN: Color palette | Verified 2026-10-02: docs.css and theme.css carry the recorded values; contrast tested in both themes by browser.py |
| DESIGN: Typography | Verified 2026-10-02, including the 12px floor and the table fonts (v0.16.0) |
| DESIGN: Spacing system | Verified 2026-10-02 against docs.css (`--pp-top` 60px, `--pp-rail-w` 260px, `--pp-radius` 6px) |
| DESIGN: Breakpoints | Verified 2026-10-02: docs.css uses 1150, 1000, 900, 640 and 400px; site.css adds rules at 900 and 640px; Home uses the inner pages' breakpoints, not wiki-portal's (Documentation Versus Reality, entry 11) |
| DESIGN: Component patterns | Verified 2026-10-02; the Home, Footer and Sidebar notes were out of date and are marked there (entry 11) |
| DESIGN: Accessibility standards | Verified 2026-10-02 (P7.5): skip link, focus order, drawer and search focus, landmarks |
| DESIGN: Animation and motion | Verified 2026-10-02: docs.css and theme.css carry the reduced-motion rules |
| DESIGN: Theme switching and icon | Verified 2026-10-02 against assets/js/theme.js and the favicon in scripts/site.py |

## Metrics

Every metric has to work without tracking (Assumptions). The targets were set by the 2026-10-01 audit as defaults for the author to confirm (Question 11).

- **North star: weekly page views across the site.** One number for whether people use the site. Target: record a baseline over the first 4 weeks after launch, then set a growth target from it. Measured with the host's own aggregate request counts, if the host chosen under D4 provides them without cookies or scripts; GitHub Pages provides no visitor statistics. Reviewed monthly after launch.
- **Acquisition:**
  - Search impressions and clicks. Target: baseline over the first 8 weeks after launch. Measured with Google Search Console and Bing Webmaster Tools, which count on the search engine's side (site ownership has to be verified first). Monthly.
  - Page views by referrer (Discord, azqato.com, search). Target: baseline after launch. Host aggregate statistics, if available. Monthly.
- **Engagement:** page views per section (Learn, Tools, Strategies, Resources, FAQ). Target: baseline after launch. Host aggregate statistics, if available. Monthly.
- **Retention:** not measured. Counting returning visitors needs a way to recognize them, which the no-tracking assumption rules out.
- **Performance:**

| Metric | Target | Measurement method | Cadence |
|---|---|---|---|
| Inventory coverage | 100% on every moved page | The core rule's check: list before, check after | Each page move |
| Console errors | 0 on every page, in both themes | Headless Edge run of each page from the local server | Before each major update is finished |
| Broken internal links | 0 | Link check in the same run | Before each major update is finished |
| LCP, CLS, TBT | LCP 2.5 s or less, CLS 0.1 or less, TBT 200 ms or less, mobile | Lighthouse against the local server in Edge: by hand in DevTools, or `npx lighthouse` with `CHROME_PATH` set to Edge (Runbook; used for P7 on 2026-10-02) | Before each major update is finished |
| Data freshness | VIX: the vix pipeline's latest value; stocks: the stocks pipeline's latest data | Compare the timestamp a page shows with the newest data commit in the source repo | Before each major update is finished; weekly after launch |
| Uptime | Set once a host is chosen | The host's status page or an external monitor, to be chosen | After launch |

## Runbook

Rewritten 2026-10-02 (P8.3) from what was actually run. Deploy and Rollback are written for P10 and haven't been run (D20).

### Prerequisites

- A current web browser. Testing uses Microsoft Edge (see Browser Testing).
- Python 3, for the scripts and the local web server. The maintenance machine has Python 3.14.3; any Python 3 with the standard `http.server` module serves the site.
- For the scripts: BeautifulSoup 4 (`pip install beautifulsoup4`) for scripts/site.py, scripts/inventory.py and scripts/check.py, and Playwright (`pip install playwright`) for scripts/browser.py. Playwright drives the installed Edge, so no browser download is needed.
- Read access to the private `Azqato/templateinterface` repo, to copy the template files: for example the GitHub CLI (`gh`) logged in as Azqato. Version 2.101.0 was used on 2026-10-01.
- Git. The folder has been a repository since 2026-10-01 (Repository Hygiene).
- No package manager or runtime for the site itself. Node.js is optional and only used to run Lighthouse from the command line (`npx lighthouse`; Node 24.19.0 on the maintenance machine).

### Local setup

1. Get the folder. It's a local git repository with no remote; the only copy is the working folder on the maintenance machine, inside OneDrive. github.com/Azqato/invests exists but isn't connected (D20).
2. From the repository root, run `python -m http.server 8000`.
3. Open http://localhost:8000/ in Edge. Port 8000 is `http.server`'s default. Stop the server with Ctrl+C in its window.

Opening a page straight from disk (file://) may work for static pages, but expect the data tools to fail there, since browsers restrict fetch() on file:// pages (not tested in this project).

### Build

The served site has no build step: the committed files are the site. The pages are generated, though, and committed (Repository Hygiene). After changing scripts/site.py, assets/css/site.css or the sources, from the repository root:

1. `python scripts/snapshot.py`: fresh read-only copies of the source pages and Template Interface's files in `_sources/` (needs `gh` logged in as Azqato for the private template repo).
2. `python scripts/inventory.py`: the core rule's inventories, from the snapshots.
3. `python scripts/site.py`: every page, the scoped source CSS, the copied scripts, the search index, sitemap.xml, inventory/map.json and inventory/em-dashes.md. It prints the page count, search entries and em dashes replaced.
4. `python scripts/check.py`: titles, links, demo text, dashes and inventories. Expect "21 page(s) checked, 0 failure(s)".
5. `python scripts/browser.py`: the browser tests in headless Edge. Expect "0 failure(s)" and the known notes about feeds that are deliberately blocked in the test.

Steps 1 and 2 are only needed when a source changed. On Windows, set `PYTHONIOENCODING=utf-8` if a script fails printing an emoji.

### Deploy

Rewritten 2026-10-02 for D21's latest form (Question 18); not run. Only on the author's go-ahead (D20).

1. Build and test here (Build, steps 1 to 5) and commit in this repository.
2. Copy the tracked files into the azqato.github.io repository's `invests/` folder (`git ls-files` here, copied with the same paths); `_sources/` stays out (ignored there as `invests/_sources/`).
3. In that repository: check the em-dash hook passes, run `python invests/scripts/check.py`, commit, and push `main`. Cloudflare Pages rebuilds azqato.com and GitHub Pages rebuilds azqato.github.io.
4. Post-deploy check (a comparison, not a test): fetch each file under https://azqato.com/invests/ and compare it with the local copy; check /invests and /invests.html land on /invests/ in one hop; open Home, the Screener and the VIX Dashboard live in both themes.
5. Then the D7 redirects in the old repos (Deprecation and Removal).

### Rollback

Locally: `git revert <commit>`. Once pushed: revert the invests commit in the azqato.github.io repository and push; both hosts republish the previous state within minutes. A bad redirect: revert that commit in the repo that holds it. Caches may serve the old file for a few minutes.

### Environment configs

Two, once published: local (`python -m http.server` from the repository root) and production (GitHub Pages at https://azqato.github.io/invests/, not deployed). The differences that matter are listed under Verification Environment; the base path is the main one, and every link and fetch here is relative or absolute https, so both work.

### Environment variable reference

None. The site needs no environment variables, keys or secrets. The source repos' workflows have their own settings, documented in those repos.

### Common errors

| Error | Likely cause | Fix |
|---|---|---|
| The VIX reading never loads, and the console reports a MIME type or `nosniff` refusal | vix.js was loaded from raw.githubusercontent.com, which serves it as plain text with `nosniff` | Load it from https://azqato.github.io/vix/data/vix.js (D6) |
| A moved VIX or stocks page loads no data | The page still uses the source site's relative `data/` path | Point it at the feed addresses under Technical Requirements |
| Data doesn't load when a page is opened from disk | file:// pages can't fetch local files (expected, not tested) | Use the local server |
| `msedge.exe` isn't found under `C:\Program Files\Microsoft\Edge\` | On the maintenance machine Edge is under Program Files (x86) | Use the path under Browser Testing |
| Headless Edge prints nothing in Git Bash | Edge doesn't write `--dump-dom` output to a Git Bash pipe | Use PowerShell's `Start-Process` with `-RedirectStandardOutput` (Browser Testing) |
| `gh api` returns 404 for `Azqato/templateinterface` | The repo is private and the CLI isn't logged in as an account with access | `gh auth login` as Azqato |
| `import site` loads the wrong module | `site` is also a Python standard library module | Load scripts/site.py by path, as browser.py does (`importlib.util.spec_from_file_location`) |
| A script fails with `UnicodeEncodeError` printing an emoji | The Windows console's code page | Set `PYTHONIOENCODING=utf-8` |
| A page edit disappears after `python scripts/site.py` | The pages are generated | Make the change in scripts/site.py or assets/css/site.css, not in the page |
| `npx lighthouse` can't find a browser | It looks for Chrome | Set `CHROME_PATH` to the Edge path (Browser Testing) |

### Monitoring

Nothing is live, so there are no logs or uptime alerts yet. Once published, GitHub Pages shows each deploy under the repository's Actions tab ("pages build and deployment"); a failed deploy shows there and the previous version stays up. The data comes from the stocks and vix repos' GitHub Actions; their runs and failures show in each repo's Actions tab. stocks has a workflow called alert-on-failure.yml, whose trigger and target weren't read in this audit.

## Technical Requirements

### System architecture

A static, multi-page website with no server code and no database. Each page is its own HTML file (Design details in DESIGN.md). Everything dynamic is fetched by the visitor's browser when a page loads:

```
Visitor's browser
├── pages, CSS and JavaScript   from azqato.github.io/invests/ (GitHub Pages, D21; not published yet)
├── stock data (JSON)           from raw.githubusercontent.com/Azqato/stocks/main/data/,
│                               falling back to azqato.github.io/stocks/data/
│                               written by the stocks repo's GitHub Actions
├── VIX reading (vix.js)        from azqato.github.io/vix/data/vix.js
│   │                           written by the vix repo's GitHub Actions
│   └── fallback                Yahoo Finance chart data for ^VIX, relayed by api.allorigins.win
└── Chart.js 4.4.0              from cdn.jsdelivr.net (VIX Dashboard and Custom builder)
```

Pages move from the source sites with their scripts (core rule); the changes are the presentation, the addresses and the data URLs. Checked 2026-10-02 (P8): this is what the built pages request. Chart.js now carries a Subresource Integrity hash (Question 12).

**How the pages are made (2026-10-02).** scripts/site.py reads the snapshots in `_sources/` and writes every page: the shell (top bar, sidebar, breadcrumbs, pager, footer, search dialog) around the source page's body content, moved whole with its own classes, ids and scripts. The source's own navigation is replaced by the shell. Each source stylesheet is copied with every rule scoped to that source (`.src-stocks`, `.src-vix`, `.src-leverage`, `.src-invests`), leaving out the rules for the old navigation and the bare element rules, so plain text takes the template's styles and the source's components keep theirs. Until the author's review after the MVP (P7), the pages are generated: change scripts/site.py and run it again rather than editing a page. The served site still has no build step; the generated files are committed.

### Tech stack

From the plan and the source sites; in the repository since 2026-10-02 (P2).

| Part | What | Version or source |
|---|---|---|
| Markup, style, behavior | HTML, CSS (custom properties, `:has()`), plain JavaScript | No framework |
| Design system | Template Interface: the shared theme.css, base.css and components.css, plus the documentation-site and wiki-portal templates | Private repo `Azqato/templateinterface`, read at commit 61acfcb (2026-10-01); files copied at commit ed840da (2026-10-02) |
| Charts | Chart.js | 4.4.0, from jsDelivr, as the vix pages load it |
| Fonts | System font stacks only (Segoe UI first); no web fonts | From the templates |
| Local server | Python `http.server` | Python 3 |
| Page builder | scripts/site.py: moves each source page's content into the shell | Python 3 with BeautifulSoup 4 (bs4) |
| Tests | scripts/check.py (no browser) and scripts/browser.py (Playwright driving Edge) | Python 3; Playwright from pip |
| Speed checks | Lighthouse, only for P7-style checks, not needed by the site | 13.5.0 through `npx` (Node 24.19.0) |
| Data pipelines | Python scripts and GitHub Actions | In the stocks and vix repos, not here (D6) |

There's no package manager, so there's no manifest or lockfile.

### Folder structure

Current, checked 2026-10-02 after P9 (the scripts moved from `tools/` to `scripts/` on 2026-10-02, because the Tools section's pages live in `tools/`):

```
invests/
├── index.html                     Home
├── faq.html                       FAQ
├── learn/                         index.html (Learn), philosophy, metrics, indices, finviz, seekingalpha
├── tools/                         screener, market, vix-dashboard, vix-custom
├── strategies/                    vix.html, and leveraged/: index.html, 3sig, 6sig, 9sig, tqqq-ftlt, holy-grail, hfea
├── resources/index.html           Resources
├── assets/
│   ├── css/                       theme, base, components (Template Interface), docs (documentation-site),
│   │                              site (this site's own), src-stocks, src-vix, src-leverage (scoped source CSS)
│   └── js/                        theme.js, site.js, search-index.js, stocks/ and vix/ (the sources' scripts)
├── sitemap.xml                    the 21 published addresses, generated by scripts/site.py (P9.3)
├── README.md                      the public front door
├── LICENSE.md                     terms of use: all rights reserved, not financial advice
├── .gitattributes                 pins LF line endings
├── .gitignore                     excludes _sources/ and Python's __pycache__/
├── docs/                          PRD.md, DESIGN.md, PATCHNOTES.md, TODO.md, UI-REVIEW.md (the 2026-10-02 UI review and its decisions)
├── scripts/
│   ├── snapshot.py                downloads read-only copies of the source pages into _sources/
│   ├── inventory.py               builds the core rule's page inventories from _sources/
│   ├── site.py                    builds every page, the scoped CSS, the copied scripts and the search index
│   ├── check.py                   read-only site checks: titles, links, demo text, dashes, inventories
│   └── browser.py                 browser tests in headless Edge: errors, both themes, phone width, contrast, shell, feeds
├── inventory/                     one inventory per source page, map.json (page to inventory), em-dashes.md
└── _sources/                      not committed: the snapshots, Template Interface's files and COMMITS.txt
```

Planned, with the section-folder layout the author chose on 2026-10-01 (Development plan, P0.3): one HTML file for each of the 21 pages; Template Interface's CSS plus this site's own CSS and JavaScript; no data folder, since the data stays in the source repos (D6). robots.txt and sitemap.xml come at the root once the site has pages and an address. If the site ends up in a subfolder of a larger domain, as the stocks, vix and leverage sites are under azqato.github.io, that domain's robots.txt governs it and may not be this project's to write. **Built as planned (2026-10-02):** sitemap.xml is at the root; robots.txt isn't, because the site is a subfolder of azqato.github.io (P9.3).

### Data models

The data belongs to the stocks and vix repos, whose own docs describe it (stocks: docs/PRD.md in github.com/Azqato/stocks). What the pages here depend on:

| Data | Where | Shape |
|---|---|---|
| VIX reading | azqato.github.io/vix/data/vix.js | A script that sets `window.__VIX_DATA__ = {value, timestamp, fetchedAt}` (field names read during planning; types not recorded) |
| Stock and ETF data, Market Overview feed, statements, index constituents | raw.githubusercontent.com/Azqato/stocks/main/data/ (`RAW_BASE` in the stocks pages), falling back to azqato.github.io/stocks/data/ on this site (since 2026-10-02) | JSON files; schemas documented in the stocks repo, not read in this audit |
| Theme choice | The visitor's localStorage, key `azqato-invests-theme` | `light` or `dark`; absent until the visitor presses the theme button (assets/js/theme.js) |
| Market Overview cache | The visitor's localStorage | The last feed, stored as JSON under the stocks page's `CACHE_KEY` |
| Screener cache | The visitor's localStorage | Each universe's last feed, as JSON with a `stocks` list (screener.js) |
| Last VIX reading | The visitor's localStorage, key `vix_last_known` | Written by vix.js |

### API design (internal data flow)

There's no API; the site only reads files. This is how the source sites do it today (read 2026-10-01), which the move keeps:

1. **VIX pages.** `data/vix.js` sets `window.__VIX_DATA__` synchronously, before the page script runs. The pages paint the last-known value from localStorage first, before any network call. vix.js treats `window.__VIX_DATA__` as the primary source; only if it's unavailable does it fetch Yahoo Finance's chart data for ^VIX through api.allorigins.win, with a query1 and a query2 address listed in that order. vix.js writes readings to `vix_last_known`. On this site, `data/vix.js` becomes the absolute azqato.github.io address (D6).
2. **Market Overview.** Reads and writes a cached copy of its feed in localStorage, and fetches the feed from `RAW_BASE`.
3. **Screener.** Fetches its data from `RAW_BASE`, with a local copy as fallback (see Background findings for what happens to that fallback here).
4. **Error states.** When a feed can't be reached, the pages fall back as above. What each page shows when everything fails wasn't read; inventory it at the move.

### State management

No application state lives anywhere but the open page and the visitor's browser storage: the theme choice (planned) and the two data caches above. No cookies: none of the scanned stocks and vix pages uses `document.cookie`, and the plan adds none. The site sends no visitor data anywhere beyond the ordinary requests a browser makes for files (see Security).

### Third-party integrations

| Service | Used for | Authentication |
|---|---|---|
| raw.githubusercontent.com (GitHub) | Stock data JSON | None (public repo) |
| azqato.github.io (GitHub Pages) | vix.js with the VIX reading; later, the D7 redirects | None |
| api.allorigins.win | Relays the VIX fallback request and adds CORS headers | None |
| query1 and query2.finance.yahoo.com, through allorigins | VIX fallback data | None |
| cdn.jsdelivr.net | Chart.js 4.4.0 | None |
| composeratlas.com | Links from Composer strategy write-ups (D15, D16, D17) | None; links only |
| Discord, brokers and the curated resources | Outbound links, some of them referral links (D13, D14) | None; links only |
| GitHub Actions, in stocks and vix | Produce the data | The source repos' own settings |

### Performance requirements

Set by the 2026-10-01 audit; no rule existed. Targets for a mobile Lighthouse run: an LCP of 2.5 s or less, a CLS of 0.1 or less and a TBT of 200 ms or less. No page-weight budget yet, because the screener's data size wasn't measured. For scale, the base template's own files are small: the three shared stylesheets total about 13 KB, documentation-site's styles.css is about 27 KB and its script.js about 25 KB (sizes from GitHub, 2026-10-01).

### Known technical debt

None in this repo yet. Planned compromises, each with what the correct solution would be:

- **A copy of azqato.com's nav, if D9 stays.** It can drift from what tools/build-nav.py stamps onto azqato.com. Correct: generate it from the same page list, or drop D9.
- **The VIX reading depends on another site.** If azqato.github.io/vix stops serving data/vix.js, the reading falls back to a third-party relay. Correct: a feed this site can load directly, such as JSON with CORS headers published by the vix repo. That's a change to the vix repo, so it's the author's call.
- **A third-party CORS relay (api.allorigins.win) for the VIX fallback.** It can disappear or return anything. Correct: nothing cheap; keep it as the fallback it is and treat its data as untrusted.
- **Chart.js from a CDN without an integrity hash.** Correct: add a Subresource Integrity hash for 4.4.0, or serve a copy from this site (Question 12).
- **The stocks local fallback.** It may point at a folder this site doesn't have (Background findings). Correct: point it at a copy the stocks repo serves.
- **Out-of-date content moved as it is (D19).** Correct: the planned correction pass (M11).

## Conventions

Read from the code and the git history on 2026-10-02 (P8.3).

**Code:**

- Pages are generated by scripts/site.py; never edit a page by hand. Hand-written styling goes in assets/css/site.css, grouped under `/* ---------- Name ---------- */` headings with a comment saying why; behavior in assets/js/site.js.
- Every change to moved source code is marked at the change with `Azqato Invests:` in a comment, so the original behavior can be told from this site's.
- Source CSS is scoped by source (`.src-stocks`, `.src-vix`, `.src-leverage`, `.src-invests`); overrides use `.pp-page .src-x ...` so they win without `!important`.
- Template tokens (`--pp-*` and theme.css) are never redefined; this site's own tokens get their own names (DESIGN.md).
- Python: 4-space indents, standard library plus bs4, one script per job in scripts/, each runnable from the repository root with no arguments. CSS: 2-space indents, one property per line. JavaScript: plain ES5-compatible functions in site.js and theme.js; the sources' scripts keep their own style.
- Text files are UTF-8 with LF line endings (`.gitattributes`). No em dashes anywhere (Writing Style).
- Links and fetches are relative inside the site and absolute https outside it, never root-relative, because the site lives under /invests/.

**Git:**

- One branch, `main`; no remote yet (D20).
- Commit messages: a short plain summary in sentence case, no prefix or ticket number (for example "VIX Custom: categories above the allocation, tighter heading"), with a body when the change needs explaining, and a `Co-Authored-By` trailer when an AI model helped.
- The generated pages are committed with the change that generated them.

**Docs** (from the plan, still true):

- Decisions are numbered D1, D2 and so on in one table. A changed decision keeps its number, is marked **Changed** with the date, and keeps its old text after "Before:" (D4, D5).
- Dates are written YYYY-MM-DD.
- The plan addresses the author as "you".
- The plan's headings are in sentence case. The PRD's required sections keep the names the documentation prompt gives them.
- No em dashes (see Writing Style).
- PATCHNOTES.md uses semantic versioning. Until the site launches, versions stay below 1.0.0: a minor version for a change to the plan, docs or site, and a patch version for a small fix (set by the 2026-10-01 audit).

## Writing Style

No rule existed, so the default was adopted on 2026-10-01. It covers the docs, the site's own interface text and code comments.

- Em dashes are prohibited in all three forms: the literal character (Unicode U+2014), the `&mdash;` HTML entity, and a double hyphen used as punctuation. Search for the character and the entity separately, because a search for one doesn't find the other. CSS custom properties (such as `--pp-bg`) and command-line flags are syntax, not punctuation, and are never touched.
- Replace each instance with whichever fits: a comma (most often), a colon (before a list or an elaboration after a complete clause), a semicolon (between two closely related independent clauses), parentheses (for asides), a period (to split the sentence), or a single hyphen.
- The single hyphen is allowed, and encouraged where it fits. It's preferred in document titles, section headings and version lines (for example "## v1.2.0 - 2026-01-01"), where a comma or colon reads awkwardly. In running prose the other replacements usually read better.
- Leave any instance the text needs in order to mean anything, such as a rule naming the character it prohibits.
- Tone: direct and functional, plain declarative sentences, no marketing language, no filler openings.
- Text moved from the sources comes over as it is (core rule), with one exception the author approved on 2026-10-01 (Question 14): em dashes in moved text are replaced under this rule, the wording otherwise unchanged, and every replacement is listed in PATCHNOTES.md. scripts/check.py fails on any em dash in page text.
- Record each sweep in PATCHNOTES.md: how many instances were found, and where. The 2026-10-01 sweep found none.

## Browser Testing

No rule existed, so the default was adopted on 2026-10-01.

- Use Microsoft Edge, never Chrome, for every automated or end-to-end test, including any ad hoc headless run from a script or a shell command. Chrome is the owner's day-to-day browser, and driving it would disturb a live session; Edge runs the same engine and is free to use. This project uses no JavaScript runtime, so tests drive a headless browser directly.
- Edge on the maintenance machine, verified 2026-10-01: `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`. It isn't under `C:\Program Files`.
- Example, not yet run in this project: `"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --disable-gpu --dump-dom http://localhost:8000/` prints the page after its scripts have run, which is how a title set at runtime is checked.
- On Windows, Edge doesn't write `--dump-dom` output to a Git Bash pipe; run it with PowerShell's `Start-Process` and `-RedirectStandardOutput <file> -Wait`, then read the file. Verified 2026-10-01 (P0): this read a title set by script correctly.
- `python scripts/browser.py [--shots DIR]` runs the site's browser tests in headless Edge through Playwright (`pip install playwright`; it drives the installed Edge with `channel="msedge"`, so no browser download). It serves the folder itself on a free port and stops it when done. Added 2026-10-02.
- No second engine is required, and Firefox and Safari aren't driven. The `:has()` support noted under Assumptions is the main cross-browser risk; check it by hand before launch.

## Verification Environment

No rule existed, so the default was adopted on 2026-10-01, alongside D20.

- Verify locally, never against production, unless a request explicitly asks for a production check. Run the change from the local server (Runbook). Production is where a change is confirmed to have arrived, not where it's tested.
- Testing against production means the change has already shipped, so the test only shows what visitors already see. It also puts load or test data on a live system, and turns a failure into a rollback instead of a fix made before pushing.
- Verifying functionality is local. Confirming a deploy landed is a separate step after a push: fetch the deployed files and check they match what was verified locally. That's a comparison, not a test, and it isn't an exception to this rule.
- For now D20 goes further: nothing is pushed, published or deployed at all until the author says so.
- Known differences between local and production, each of which can hide a bug until the site is deployed:
  - **Base path.** If the site is served from a subfolder, as the stocks, vix and leverage sites are under azqato.github.io, links and fetches that start with `/` reach the domain root in production but the repository root locally. Use relative links.
  - **Extensionless addresses.** azqato.com, a Cloudflare Pages build, answers /page.html with a 307 redirect to /page; Python's `http.server` doesn't. If this site's host does the same, check links and redirects against the host's behavior.
  - **Pages opened from disk.** A page opened from file:// behaves differently from both the local server and production (Runbook).
  - **Caching.** The host and GitHub may cache vix.js and the data files, while local tests see fresh files. A stale reading in production may be caching rather than a bug (cache lifetimes not measured).
- Never point a destructive or state-changing check at production: no writes, deletes, test records, or anything that sends mail or a webhook. If something can only be exercised against a live system, stop and ask.

## Testing Cadence

No earlier testing rule existed, so nothing was replaced. The default was adopted on 2026-10-01.

- Browser tests use headless Microsoft Edge, as Browser Testing says.
- A major update ships when it's pushed or deployed. While nothing is pushed or deployed (D20), it ships when the major update is finished. "Before shipping" below means that moment.
- Right before a major update ships, run two checks, once each:
  1. Assumption check: list the assumptions the finished change relies on, each marked verified (the code that shows it was read) or guessed (inferred, and from what). Check every guess that's cheap to check, fix anything found wrong, and show the author what's still guessed.
  2. Browser test, once. Don't test between edits.
- If a large change depends on something not yet read, check that one thing before building on it.
- A major update changes behavior, layout, scripts, styles, routing, the build or dependencies. A minor update changes only wording, documentation, comments, patch notes, or data the project's own check script validates. Minor updates ship without a browser test or an assumption check.
- Cheap checks that don't open a browser (a linter, a project check script) may still run after minor edits.
- Batch the work: make every edit first, then test once at the end.
- When a test fails, fix it and rerun only the failing check, then run the full test once before shipping.
- A test the author asks for always runs, whatever this rule says.
- Confirming a deploy arrived, by comparing the deployed files with the local copies, isn't a test. It's cheap and still happens after every push.
- Where a session has standing permission to push, every change reaches production, so decide by whether the change is major, not by whether it's being pushed.
- Every summary says what wasn't browser-tested. An untested change is never presented as tested.
- For a page move, the core rule's inventory check is part of the browser test: every item on the page's list is checked on the new page.

## Security

- **Authentication model:** none. There are no accounts or sign-in (Assumptions).
- **Authorization model:** none. Every page is public once published; until then, nothing is reachable from outside (D20).
- **Data storage:** only in the visitor's browser: the theme choice (planned), the cached Market Overview feed and the last VIX reading (`vix_last_known`). None of it is personal data, nothing leaves the browser, and there are no cookies.
- **Environment variables and secrets:** the site needs none, and none are in this repo (checked 2026-10-01, and again by pattern search on 2026-10-02, P7.8). The source repos' workflows keep their own settings.
- **Third-party trust:** loading a page makes the visitor's browser contact raw.githubusercontent.com and azqato.github.io, and on the VIX pages cdn.jsdelivr.net. If the VIX fallback runs, it also contacts api.allorigins.win, which relays the request to Yahoo Finance. Each receives what any web request carries: the visitor's IP address, browser user agent and possibly the referring page. Nothing else is sent. Clicking an outbound link (Composer Atlas, Discord, brokers and the other resources) takes the visitor to that site.
- **Known attack surface:**
  - Chart.js from jsDelivr without an integrity hash: a tampered CDN file would run on the VIX pages. Mitigation today: the version is pinned in the URL (4.4.0). Planned: add an integrity hash or serve a copy from this site (Known technical debt). **Done (P6):** both VIX tools load it with a sha384 integrity hash and `crossorigin="anonymous"`.
  - Data from the feeds and the allorigins relay: if a page inserts fetched text as HTML, a tampered response could inject script. Checked 2026-10-01 (P1): the screener (12 uses in screener.js) and Market Overview (1 use) build rows and cards with `innerHTML` from feed values such as tickers and category names, without escaping; the VIX scripts don't use `innerHTML`. The feeds are the author's own pipeline, so the risk is low; escape feed values when these tools move (P6), and prefer `textContent` and number parsing over `innerHTML`. **Fixed 2026-10-02 (P7.8):** scripts/site.py wraps every stock feed's `res.json()` in `azqClean()`, which strips `<` and `>` from each text value before the page uses it, so feed text can't add markup. The VIX tools insert only numbers and their own labels.
  - Links that open in a new tab should carry `rel="noopener"`. Current browsers imply it, but being explicit costs nothing. Checked 2026-10-02 (P7.8): every one does.
  - Template Interface is a private repo. Copying its files here publishes them if this repo is ever made public (Question 5). The repository will be public long term (2026-10-02), so this needs the author's answer before it is (Question 16).
- **Dependency policy:** no package manager. The one third-party library, Chart.js, is pinned to an exact version in its URL. Default set by the 2026-10-01 audit: pin exact versions, add integrity hashes, review third-party files at each major update, and check the Chart.js version against its security advisories when the VIX pages move.

## Repository Hygiene

No rule existed, so the default below was adopted on 2026-10-01. This is a policy record: the audit created no ignore or attributes file and ran no version control command.

**Current state (2026-10-01, P0):** a local git repository with default branch `main` and no remote (D20). `.gitattributes` pins LF (`* text=auto eol=lf`, with images marked binary); `.gitignore` excludes `_sources/`, the read-only source snapshots that scripts/snapshot.py regenerates. Before P0 the folder wasn't a repository. The only copy is the working folder on the maintenance machine, inside OneDrive. The repository's name, where it lives on GitHub and whether it's public are open (Question 5). **Update 2026-10-02:** github.com/Azqato/invests exists (private, to be public later); the local repository isn't connected to it. `.gitignore` gained `__pycache__/`, which Python writes when one script imports another (scripts/browser.py loads scripts/site.py).

**Default:**

- The repository carries an ignore file and a `.gitattributes`, commits its lockfile, keeps every secret out of history, and names its default branch `main`.
- Secrets are never committed; it's the one mistake whose cost can't be recovered. Keep them out with the ignore rule `.env*` followed by `!.env.example`, so a file listing key names can travel with the repository while the file holding values never does. The site needs no environment variables, so there's nothing to ignore yet; add the rule if one ever appears. An ignore file is prevention, not protection. A secret found committed is reported by file name with a recommendation to rotate it; history isn't rewritten, which wouldn't undo the exposure anyway.
- An ignore file exists wherever the project generates something: build output, dependency folders, caches, logs, coverage reports, and editor or operating system files. This project generates nothing (no build, no dependencies), so it needs none yet and won't carry an empty one.
- Lockfiles are committed, never ignored. This project has none, because it has no package manager.
- Every ignore entry names something this project actually produces. An entry that can't be explained is reported, not removed.
- Ignoring a file doesn't untrack it, so compare the tracked list against the rules rather than reading the rules alone.
- Generated files committed on purpose are recorded here with what regenerates them and what keeps them in step. None exist. If D9 stays, the copied azqato.com nav will be the first: record its source here.
  **Since 2026-10-02 (P2):** scripts/site.py generates and commits every page, assets/css/src-*.css, assets/js/stocks/ and assets/js/vix/ (the sources' scripts, with the data addresses changed), assets/js/search-index.js, inventory/map.json and inventory/em-dashes.md, from the snapshots in `_sources/`. Run it again after a snapshot refresh. Copied files: assets/css/theme.css, base.css and components.css, and docs.css (documentation-site's styles.css), from Template Interface at ed840da, recopied by the same script; azqato.com's nav, copied by hand into scripts/site.py (`AZQATO_NAV`) from azqato.github.io's invests.html at commit 58767b5. theme.js and site.js are adapted from Template Interface's scripts and edited by hand.
- Pin line endings. When the repository is created, add a `.gitattributes` with `* text=auto eol=lf`: the work happens on Windows, the site will be served from elsewhere, and the post-deploy check compares files byte for byte, so unpinned line endings would show differences that aren't there. Mark binary formats as binary when any arrive. Nothing here needs CRLF. The docs already use LF.
- Large binaries stay out of history. None exist.

**Compliance checks.** These read and report; they never run a command that changes state.

- An ignore file exists, or this section says why the project needs none. Today: none needed. **Since P0:** `.gitignore` exists, for `_sources/` and (2026-10-02) `__pycache__/`.
- No tracked file matches a pattern the ignore file excludes. Today: not applicable.
- No dependency folder, build output or cache is tracked.
- No tracked file holds credentials by convention: an environment file other than the example, a private key, a certificate, or a package manager configuration carrying a token.
- The lockfile is tracked, where the ecosystem has one. Today: not applicable.
- A `.gitattributes` exists and pins line endings, with an explicit rule for any format that must keep CRLF. Today: fails until the repository is created (Documentation Versus Reality, entry 5). **Passes since 2026-10-01 (P0).**
- Every ignore entry corresponds to something the project produces.

## Licensing

The project had no licence. The default posture was adopted on 2026-10-01 and written into [LICENSE.md](../LICENSE.md) at the repository root, never inside docs/, where licence detection may miss it.

- **Posture:** all rights reserved; source-available, not open source. LICENSE.md grants nothing, and a readable repository isn't a grant. A permission given to everyone can't easily be withdrawn from one person, and the aim is to keep the ability to act against a specific bad actor.
- **The one carve-out, AI and search referencing:** search engines, AI assistants, answer engines and other automated systems may crawl, index, store for retrieval, quote, summarize, link to and cite the work. Attribution is requested, not required, and no permission is needed. Referencing is granted. Substitution, meaning reproducing the work as a replacement for visiting it, is not. Use as training data isn't granted by default and goes through the permission route, where it's not usually refused.
- **No waiver:** not acting against a use isn't a licence, a precedent or a waiver; delay doesn't waive; any waiver must be written, signed and limited to the use it names.
- **Asymmetry:** widening a grant later takes one sentence; narrowing a granted right doesn't. When in doubt, grant less and point to the request route.
- **No licence without its text:** a bare licence name with no licence file behind it is an ambiguity, not a grant.
- **What LICENSE.md doesn't claim:** it doesn't override platform terms (a host's own view and fork rights operate independently and aren't enlarged); it doesn't claim third-party data (market prices, index readings, statements, constituent lists, Chart.js, linked sites); and it doesn't restrict fair use or fair dealing.
- **Domain disclaimer:** NOT FINANCIAL ADVICE, including that leveraged strategies can lose money quickly, that backtests and past results don't predict future returns, and that some links are referral links.
- **Permission requests** go to this repository's public issue tracker on GitHub. The repository isn't published, so there's no tracker yet; LICENSE.md says so, and the address gets added once it exists (Question 7).
- **Machine-readable layer:** when the site gets a robots.txt of its own, it stays fully open (`User-agent: *` and `Allow: /`) with a comment saying that's deliberate, and LICENSE.md is authoritative if the two ever disagree. LICENSE.md already says so.

## Social Sharing Tags

No rule existed for this site, so the default was adopted on 2026-10-01. There are no pages yet, so nothing has been checked; this is the rule pages are built to. It's a policy record: changing a page's head is a separate change.

- Every shareable page carries six tags: og:title, og:description, og:url, og:type, og:site_name and twitter:card. og:title, og:description and og:url are written per page. og:type is "website" on every page. og:site_name is the same everywhere: "Azqato Invests" by default, 14 characters (Question 6).
- og:url is the page's own absolute https address, never a relative path and never the site root. The domain comes from what the project has once D4 is decided (the sitemap, a CNAME file, robots.txt or the deploy config), used exactly as written and never guessed. Until then, no page can have a correct og:url.
- Budgets, as safe caps: og:title 60 characters (70 at most), og:description 150 (200 at most), og:site_name 20. Emoji and markdown characters count as characters.
- og:title doesn't repeat the site name, because the card already shows og:site_name directly above the title.
- No images by default: no og:image, og:image:width, og:image:height or og:image:alt, and twitter:card is "summary". An image is never added speculatively or pointed at a placeholder. If an image policy is adopted later: 1200 by 630 pixels, an absolute https URL, explicit width and height tags, PNG or JPG under about 8 MB, alt text under 100 characters, and only then "summary_large_image".
- The title front-loads what's distinct about the page: no trailing branding, and no colon stacking a subtitle onto a subtitle.
- The description is complete sentences saying what the page actually gives someone who has never seen the site, ending on a full stop, and not a restatement of the title. It's written from the page's own content. Where a page's meta description is accurate, og:description reuses it rather than competing with it; where the two differ, say why.
- Excluded from sharing tags: error pages such as a 404, mockups, scratch or work-in-progress files, and anything left out of the sitemap or marked noindex. None exist yet; list them here as they appear.
- **Compliance checks** (read and report; counts by script, not by eye): all six tags on every page that should have them; og:title 70 characters or fewer, og:description 200 or fewer, og:site_name 20 or fewer, with the count reported for anything over the target budgets; every og:url absolute, https and unique across the site; no og:title containing the og:site_name; where og:image exists, its width, height and alt tags exist, its URL is absolute and its file is in the repository; where it doesn't, twitter:card is "summary".

**Checked 2026-10-02 (P7.4, P9.2), by script on all 21 pages:** all six tags present on every page; og:url absolute, https and unique (https://azqato.github.io/invests/ plus the page's path, with folder pages ending in `/`), matching the canonical link; og:site_name "Azqato Invests" (14 characters); no og:image, so twitter:card is "summary" everywhere. Nothing is excluded: there's no 404 page or draft page.

**Starting point from the source**, read 2026-10-01 and counted by script. invests.html, which becomes Home and Resources, carries: og:title "Free Investing Tools and a Curated Resource Hub" (47 characters, within budget, no site name); og:description identical to its meta description, "Free investing tools built by Azqato, plus a hand-picked hub of brokers, screeners, ETF lists, charts and economic data. Nothing here is financial advice." (154 characters: over the 150 target, under the 200 maximum); og:type "website"; og:site_name "Azqato"; twitter:card "summary"; og:url and canonical `https://azqato.com/invests`. Those values were written for azqato.com, under azqato.github.io's rules. Home's tags get written when Home is built, with these as the starting point.

## Page Titles

No rule existed for this site, so the default was adopted on 2026-10-01. There are no pages yet; this is a policy record, and changing a title is a separate change.

- The shape is "<page name> - Azqato Invests". The first 30 characters must identify the page on their own, and the whole title is 60 characters or fewer, counting the 3-character " - " separator. Truncation removes from the end, so front-loading the page name satisfies both limits.
- The brand goes last, because the favicon already marks the tab. The home page inverts this, and only the home page: there the brand leads. Proposed home title: "Azqato Invests - Investing Tools and Resources" (46 characters), which keeps the wording of invests.html's own title, "Investing Tools and Resources - Azqato".
- Every page's first 30 characters are unique across the site: two titles that differ only after character 30 look the same on a tab.
- One separator, " - ", on every page.
- No placeholder titles ("Untitled", "Document", "Home", "index", template defaults). Search for them explicitly. The template's own title, "Introduction - Parcelpoint Docs", must not survive the build.
- The brand appears once, at the end, and never inside the page name. No keyword stuffing.
- No emoji in titles, since the 💰 favicon already marks the tab, and no all caps in the first 30 characters.
- Every title survives as a bookmark read months later: "Overview" alone is useless, while "Market Overview - Azqato Invests" works.
- Where a title changes at runtime, it must actually change, with any state in front of the name ("(3) ..."), and loading and error states get real titles. The plan has one file per page, so each title is set in its file's head.
- The title and og:title are different fields with different rules. The title ends with the brand; og:title leaves it out. Expect the two to differ on the same page.
- The brand is "Azqato Invests" by default. The source pages follow azqato.github.io's pattern ("Investing Tools and Resources - Azqato"); this site sets its own (D5). Question 6 asks which brand to use.
- **Compliance checks** (read and report; counts by script): a title exists on every page and isn't a placeholder; each is 60 characters or fewer, with the count reported; the first 30 characters are unique, with each collision reported as a pair; the separator matches; the brand suffix is on every page except Home and isn't also inside the page name; any title set at runtime is checked by loading the page and reading the resulting title, not the source.

## Deprecation and Removal

**The project's own rule, kept as written.** D7: "Every old page under azqato.github.io/stocks/, /vix/ and /leverage/ redirects to its new home. The old repos stay for data and history." The core rule says the same: page addresses change, and "old addresses redirect to the new ones". The redirects mean publishing, so they wait for the author's go-ahead (D20).

**Default for this site's own pages**, adopted 2026-10-01 because no rule existed. Whether a removal needs a redirect depends on whether the thing removed is public facing:

- Public facing: a published page address. Removing or moving one leaves a redirect to whatever replaces it, so the old address keeps resolving.
- Internal: the files that build the site, and anything else not reachable from outside. A source file isn't public facing even when its name appears in an address, because the address is the contract, not the file. Removing one is a plain delete: no redirect, no stub file, no tombstone.

The deploy boundary is the published site: a page is public facing once its address has been published. Nothing in this repo has been published, so today everything here is internal.

**Mechanism.** Not decided; it depends on the host (D4). Some static hosts offer redirect rules. GitHub Pages has no server-side redirects, so a moved page there is replaced by a small HTML page that sends visitors on (to confirm when the host is chosen). The D7 redirects live in the old repos, since those serve the old addresses, and the vix repo must keep serving data/vix.js after its pages redirect (D6). The reasoning is recorded here so it isn't relitigated: old addresses are shared in bookmarks, Discord messages and search results, and a broken one is lost traffic and a broken promise.

**Public surface.**

- This repo: nothing yet. Nothing is published; once it is, the 21 addresses in sitemap.xml are the public surface.
- Governed by D7, the old addresses in the source repos:
  - azqato.github.io/stocks/: index.html, philosophy.html, metrics.html, indices.html, finviz.html, seekingalpha.html, screener.html, market.html, faq.html
  - azqato.github.io/vix/: index.html, strategy.html, custom.html
  - azqato.github.io/leverage/: index.html, 3sig.html, 6sig.html, 9sig.html, tqqq-ftlt.html, holy-grail.html, hfea.html
- Open: azqato.com/invests (invests.html in the azqato.github.io repo). Whether it becomes a redirect, keeps a card, or gets a nav item is on To settle (D4). Now Question 17, with a recommendation.
- Not this site's surface: the data addresses the pages read (raw GitHub and azqato.github.io/vix/data/vix.js), which belong to the source repos and stay (D6).

**The D7 redirect list (P9.4, 2026-10-02).** Each old address goes to its new page in one hop. Not done: it changes the live source sites, so it waits for P10 and the author's go-ahead (D20).

| Old address (azqato.github.io/...) | New address (azqato.github.io/invests/...) |
|---|---|
| stocks/ (index.html) | learn/ |
| stocks/philosophy.html | learn/philosophy.html |
| stocks/metrics.html | learn/metrics.html |
| stocks/indices.html | learn/indices.html |
| stocks/finviz.html | learn/finviz.html |
| stocks/seekingalpha.html | learn/seekingalpha.html |
| stocks/screener.html | tools/screener.html |
| stocks/market.html | tools/market.html |
| stocks/faq.html | faq.html |
| vix/ (index.html) | strategies/vix.html |
| vix/strategy.html | tools/vix-dashboard.html |
| vix/custom.html | tools/vix-custom.html |
| leverage/ (index.html) | strategies/leveraged/ |
| leverage/3sig.html | strategies/leveraged/3sig.html |
| leverage/6sig.html | strategies/leveraged/6sig.html |
| leverage/9sig.html | strategies/leveraged/9sig.html |
| leverage/tqqq-ftlt.html | strategies/leveraged/tqqq-ftlt.html |
| leverage/holy-grail.html | strategies/leveraged/holy-grail.html |
| leverage/hfea.html | strategies/leveraged/hfea.html |

A 20th, outside D7 and waiting on Question 17: azqato.github.io/invests.html (azqato.com/invests), whose content became Home and Resources.

**Mechanism (decided for GitHub Pages, P9.4).** GitHub Pages has no server-side redirects, so each old page is replaced in its own repo by a small HTML file carrying the old page's title, a `<link rel="canonical">` to the new address, `<meta http-equiv="refresh" content="0; url=NEW">`, a `location.replace(NEW + location.hash)` script so `#section` links survive, and a plain link to the new page for anyone with scripts and refresh off. This is one hop: the old address answers 200 and sends the browser straight to the new page. Search engines treat an immediate meta refresh like a permanent redirect. The vix repo keeps serving data/vix.js and the stocks repo keeps data/ (D6, D21); only the HTML pages change. Old in-page anchors don't map one to one everywhere, so the hash is carried as it is and lands at the top of the page if the section's id changed.

**Compatibility entries.** Once any exist, they're permanent, never chained (each redirect reaches a real page in one hop), and never reused to point at different content, since a reused address silently serves the wrong thing.

**Retired items.** None yet.

**Historical records.** Patch notes and decision history, such as the "Before:" text in D4 and D5, are never rewritten when something is removed.

## Documentation Versus Reality

The code is the truth about what is; the docs are the truth about what was intended. Until the site exists, "the code" means this folder and the sources the plan depends on. Resolved entries stay, with how they were resolved.

| # | Found | The docs say | Observed | Trust | Status |
|---|---|---|---|---|---|
| 1 | 2026-10-01 | README.md held the whole plan; the prompt expects README.md as a front door plus docs/PRD.md, DESIGN.md, PATCHNOTES.md, TODO.md and a licence | README.md was the only file | The folder | Resolved 2026-10-01: the audit created the doc set and moved the plan |
| 2 | 2026-10-01 | README.md's status: "The documentation prompt is approved but was stopped partway, before it wrote anything; it reruns for the independent repo when you say to resume." | The author said to resume on 2026-10-01, and the audit ran | Events | Resolved 2026-10-01: status updated; the old wording is quoted in PATCHNOTES.md v0.2.0 |
| 3 | 2026-10-01 | What's being merged: "6 GitHub Actions workflows: stock and ETF data daily, Market Overview 3 times a weekday, statements and index constituents weekly" | Six workflow files; the description covers five data jobs, and the sixth is alert-on-failure.yml | The listing: the count is right and the description incomplete | Resolved 2026-10-01: the description now names alert-on-failure.yml, original wording kept (Question 13) |
| 4 | 2026-10-01 | Design details name the template's demo-only parts: the API keys button, API status line, code-language tabs and page-feedback form | documentation-site's top bar also has an "API v3.4" version label, and since 2026-10-01 every template page carries a "Back to Template Interface" return bar | The template code | Open: original text kept; DESIGN.md lists the two extra parts as presumed demo-only (Question 10) |
| 5 | 2026-10-01 | Repository Hygiene's default: a git repository with a `.gitattributes` | Not a git repository; no ignore or attributes file | The folder | Resolved 2026-10-01 (P0): a local git repository with `.gitattributes` and `.gitignore` |
| 6 | 2026-10-01 | Design details: "the dark theme is built on top of the template's shared color tokens". Assumptions: "Dark mode uses azqato.com's colors" | Not a contradiction: theme.css's dark tokens equal azqato.com's colors except the accent hover (`#22e6b5` against `#00e6b0`) | Both | Resolved 2026-10-01: consistent; noted in Background findings and DESIGN.md |
| 8 | 2026-10-01 | Background findings: the stocks fallback "may not survive the move" (inferred) | Confirmed in P1: relative `data/` fallbacks in screener.js and market.html; azqato.github.io/stocks/data/ serves the same files with open CORS | The source code | Resolved 2026-10-02 (P6): the pages fall back to azqato.github.io/stocks/data/, tested by browser.py with raw GitHub blocked |
| 7 | 2026-10-01 | The rule set expects robots.txt and sitemap.xml at the root where the project serves a site | Neither exists | The plan: no pages and no address yet (D4) | Resolved 2026-10-02 (P9.3): sitemap.xml generated; robots.txt belongs to azqato.github.io, which owns the origin |
| 9 | 2026-10-02 | Runbook, Prerequisites: "No package manager, runtime or build tool, and no Node.js"; Metrics: the Lighthouse command-line tool needs Node.js | Node.js 24.19.0 and npx are on the maintenance machine; `npx lighthouse` ran Lighthouse 13.5.0 against Edge | The machine | Resolved 2026-10-02: Node is optional, used only for Lighthouse; the site still needs no runtime |
| 10 | 2026-10-02 | Security: the screener and Market Overview put feed text into the page unescaped, to be fixed in P6 | Still unescaped after P6 | The code | Resolved 2026-10-02 (P7.8): `azqClean()` in scripts/site.py |
| 11 | 2026-10-02 | DESIGN.md: Home has content up to 1120px, section tiles then project cards, and wiki-portal's breakpoints; inner pages cap content at 760px; the footer's content "isn't decided" | Since v0.16.0 every page runs to 1400px, Home is one grid of 10 cards on the inner pages' breakpoints, and the footer holds the brand, notice, links and the VIX disclaimer lines | The code | Resolved 2026-10-02: DESIGN.md marks each as superseded, with the old text kept |
| 12 | 2026-10-02 | `.gitignore`'s comment names tools/snapshot.py | The script is scripts/snapshot.py | The folder | Resolved 2026-10-02: comment corrected |

## Risks and Open Questions

**Not fully understood:**

- The source sites' JavaScript beyond what this audit read (browser storage, external hosts, the vix.js fallback lines): for example how each page renders data, and what it shows when every feed fails.
- The stocks data files' schemas and sizes, which the stocks repo documents.
- The three borrowed templates (help-center, admin-dashboard, blog-article). They were rated during planning, but this audit didn't read their code.

**Fragile areas:**

- The VIX reading depends on azqato.github.io/vix staying up, with a third-party relay as the only fallback.
- The stocks fallback path (Background findings).
- The sources change fast: stocks shipped v4.9.6 on 2026-09-29, and stocks and vix both had commits on 2026-10-01. An inventory taken early goes stale, so take it at the move.
- Template Interface changes too: on 2026-10-01 it was renamed and every template page gained a return bar (commit 61acfcb). Record the commit each copied file comes from.
- The content is large (20 pages, 15 link categories, a long FAQ) and the core rule allows no loss. The inventory check is the safeguard.

**Dangerous to change without more context:**

- Anything that removes or shortens source content (core rule).
- Anything that publishes (D20), including the D7 redirects, which change the live source sites.
- The data addresses: the VIX pages break if pointed at raw GitHub (nosniff).
- Docs that name the author's private project. Its name was removed on 2026-10-02 (P9.6) because the repository will be public; keep it out (Assumptions). Earlier commits in this repository's local history still contain it (Question 16).

**Work in progress:** none in this repo. It isn't a repository, so there are no uncommitted changes, branches or stubs. **2026-10-02:** it is a repository now, on `main`, with everything committed; no branches or stubs. In the sources, stocks and vix are under active development (above).

**Uncertain, not checked:** if this repo were published as a GitHub Pages project site named `invests`, it would sit at azqato.github.io/invests/, beside azqato.github.io's own invests.html at azqato.github.io/invests. How GitHub Pages resolves the two wasn't checked. Still unchecked on 2026-10-02: it can only be seen once the project site exists. Question 17 recommends retiring invests.html as a redirect, which removes the question.

**From the plan:**

To settle along the way:

- The site's address (D4), and how azqato.github.io links to it: a nav item, a card, or turning invests.html into a redirect.
- Whether every page still shows azqato.com's top nav (D9), and with it whether dark mode keeps azqato.com's colors.
- The exact page addresses.
- How to link HFEA's entry in Atlas's community database.

**Open questions, numbered so they can be answered by number.** When one is answered, the answer goes into the section it affects, and the question is marked answered here rather than deleted. Each shows the default applied in the meantime.

1. **The site's address (D4).** Where will the site live, and how should azqato.github.io link to it: a nav item, a card, or turning invests.html into a redirect? Default: undecided. Nothing is published (D20), and sitemap.xml, robots.txt, canonical links and og:url wait for the answer. Recorded in Decisions (D4), To settle and the Roadmap (M10). **Answered 2026-10-01:** the site will be a GitHub Pages project site at azqato.github.io/invests/, which means a repository named `invests` under Azqato, public (GitHub Pages on a free account serves public repositories). Still nothing is published until the author says so (D20). How azqato.github.io's own invests.html and the azqato.com/invests address relate to it is checked and settled in P9.
2. **azqato.com's nav on every page (D9).** Keep it? The audit found the dark colors come out the same either way: Template Interface's dark tokens already equal azqato.com's colors apart from one hover shade (`#22e6b5` against `#00e6b0`). Default: D9 stands, marked to re-check, and the dark theme uses theme.css's tokens. Recorded in Decisions (D9), Background findings and DESIGN.md. **Answered 2026-10-01:** keep azqato.com's nav on every page, in light and dark versions. D9 stands.
3. **The exact page addresses.** The file names and folders for the 21 pages. Default: none chosen; the site map stands. Recorded in To settle. **Answered 2026-10-01:** section folders, as proposed in the Development plan (P0.3).
4. **HFEA's Composer Atlas link.** Default: no link yet. Recorded in Composer Atlas, To settle and the Roadmap. **Answered 2026-10-01:** link HFEA to its entry in Atlas's community database (symphony `Cjb5ysKtJsPv6Tm3Fk0R`), once the link format for community entries is confirmed (P5). **Checked 2026-10-02 (P5):** Atlas has no address for a single database entry, so the HFEA page links composeratlas.com/database.html and names the symphony id to search for.
5. **The repository.** What's it called, where does it live on GitHub, is it public, and when should it be created? If it's public, the Template Interface files copied into it (from a private repo) become public, and the docs must drop the private project's name first (Assumptions). Default: not created; no version control command run; Repository Hygiene records the plan (`main`, LF line endings). Recorded in Repository Hygiene, Security and Documentation Versus Reality. **Answered 2026-10-01:** a local git repository now, branch `main`, no remote; nothing is pushed (D20). Name, GitHub location and visibility stay open. **Answered 2026-10-02:** the author created github.com/Azqato/invests, private for now and meant to be public long term. It isn't connected to this local repository and nothing is pushed (D20). Because it will be public, P9.6 was done now: the private project's name is out of the docs, and LICENSE.md names the issue tracker. Before it goes public, see Question 16.
6. **The brand in titles and share cards.** "Azqato Invests" or "Azqato", as azqato.github.io uses? Default: "Azqato Invests" (14 characters): titles like "Market Overview - Azqato Invests", and Home as "Azqato Invests - Investing Tools and Resources" (proposed). Recorded in Page Titles and Social Sharing Tags. **Answered 2026-10-01:** "Azqato Invests".
7. **Permission requests in LICENSE.md.** Should they go to this repo's public GitHub issue tracker? Default: yes, once it exists; until then LICENSE.md says there's no tracker yet. Recorded in LICENSE.md (PERMISSION) and Licensing. **Answered 2026-10-01:** yes: this repository's GitHub issue tracker, once the repository is public.
8. **A skip link.** Follow Template Interface, which has none (a known gap against WCAG 2.4.1), or add one here, given a 21-page sidebar and possibly azqato.com's nav above it? Default: follow Template Interface and record the gap. Recorded in DESIGN.md (Accessibility standards). **Answered 2026-10-01:** add a skip link ("Skip to content"), hidden until focused. This site departs from Template Interface here.
9. **Home page colors.** The site's light and dark themes with wiki-portal's layout only, or wiki-portal's violet palette? Default: the site's themes, layout only, read from D8's wording. Recorded in Assumptions and DESIGN.md (Color palette). **Answered 2026-10-01:** the site's own light and dark themes; wiki-portal gives the layout only.
10. **Template parts missing from the demo-only list.** documentation-site's "API v3.4" version label and the "Back to Template Interface" return bar added on 2026-10-01: remove them like the other demo parts? Default: yes, presumed demo-only. Recorded in DESIGN.md (Component patterns) and Documentation Versus Reality (entry 4). **Answered 2026-10-01:** remove both, like the other demo parts.
11. **Metrics without tracking, and the targets.** Is it acceptable to use the host's aggregate request counts and the search engines' own consoles (no scripts or cookies on the site), or should no traffic be measured at all? Are the targets right: LCP 2.5 s, CLS 0.1, TBT 200 ms, and WCAG 2.2 AA? Default: as written; traffic is measured only if the host offers it without scripts. Recorded in Metrics, Performance requirements and DESIGN.md (Accessibility standards). **Answered 2026-10-01:** as written: the host's aggregate counts and the search engines' consoles, with no scripts or cookies on the site; the speed and WCAG 2.2 AA targets stand.
12. **Chart.js integrity.** Add a Subresource Integrity hash, or serve a copy from this site, when the VIX pages move? It changes a script tag, not content. Default: recommended; nothing changed. Recorded in Security and Known technical debt. **Answered 2026-10-01:** yes, add a Subresource Integrity hash when the VIX tools move.
13. **The stocks workflow description.** Update What's being merged to mention alert-on-failure.yml? Default: original text kept, observation added. Recorded in Documentation Versus Reality (entry 3). **Answered 2026-10-01:** yes: What's being merged now also mentions alert-on-failure.yml, with the original wording kept.
14. **Em dashes in moved content.** **Found 2026-10-01 (P1):** 28 inventory items carry em dashes in visible source text (vix index 14, strategy 7 and custom 4, including all three vix page titles; stocks screener 3), plus more in code comments and CSS. The inventories list them; nothing is changed until this is answered. If the source pages contain em dashes, leave them (core rule) or replace them under Writing Style? Default: leave them and report them. Recorded in Writing Style. **Answered 2026-10-01:** replace them. When text moves, each em dash becomes a comma, colon, semicolon, parentheses or a hyphen under Writing Style, with the wording otherwise unchanged, and each replacement is listed in PATCHNOTES.md.
15. **Sections the audit drafted.** The tenets, personas, user stories, goals, success criteria, metrics, press release and FAQ were drafted from the plan; review them. The press release also needs a city and a launch date. Default: as drafted, with the dateline "ONLINE" and the date to be set. Recorded in those sections. **Answered 2026-10-01:** review the drafted sections after the MVP is ready (Development plan, P7). They stay marked as drafted until then.
16. **Before the repository goes public (added 2026-10-02, P9.6).** Two things become public with it. (a) This repository's history: earlier commits still contain the private project's name, which P9.6 removed from the current docs. (b) Template Interface's files (theme.css, base.css, components.css and docs.css), copied from a private repo. Options for (a): publish the history as it is, or publish a fresh single-commit history (keeping this local one). Options for (b): publish them, or ask whether Template Interface may be public. Default: nothing is pushed until you answer. Recommendation: a fresh history for the first public push, and your call on Template Interface since it's your private repo. Recorded in Security and the Runbook (Deploy). **Answered 2026-10-02:** (b) yes, publish the Template Interface files. (a) The author asked whether only the private information can be removed: yes. 2 of the 23 commits contain the name and no commit message does; `git filter-repo --replace-text` can replace the word in every past version while keeping every commit (their ids change, which is safe because nothing is pushed). Waiting for the author's go-ahead to rewrite. **Done 2026-10-02:** with the author's go-ahead, `git filter-repo --replace-text` replaced the name with "private project" in every past version; all 24 commits kept, new ids; checked: the name is in no file of any commit and no commit message. The original history is kept only as a local backup bundle outside the repository, never to be pushed.
17. **azqato.com/invests and azqato.github.io/invests.html (P9.5, added 2026-10-02).** Their content now lives on this site's Home and Resources. Options: keep invests.html as it is and link the new site from it; turn it into a redirect to https://azqato.github.io/invests/; or remove it. Default: unchanged until P10. Recommendation: at P10 make invests.html a redirect page (as in Deprecation and Removal) and point azqato.com's nav and card at https://azqato.github.io/invests/, so there's one copy of the content, old links keep working, and GitHub Pages never has to choose between /invests and /invests/. That's a change to the azqato.github.io repo, so it's yours to approve. Recorded in Deprecation and Removal and P9. **Answered 2026-10-02:** ideally azqato.com/invests is this site, either from this repo or by merging into the main repo; depends on Question 18. **Settled 2026-10-02:** invests.html becomes a one-file redirect page to invests/ (the main repository's removal policy), plus Cloudflare `_redirects` rules so /invests and /invests.html go straight to /invests/.
18. **Where the site lives (added 2026-10-02).** The author would like azqato.com/invests to be this site, and is weighing GitHub Pages, a Cloudflare Worker, or merging into the main repo. The full analysis is in [HOSTING.md](HOSTING.md). Default: D21 stands (GitHub Pages at azqato.github.io/invests/) until decided. Recommendation: publish the built site into the azqato.github.io repo's invests/ folder (option C), which serves azqato.com/invests/ and azqato.github.io/invests/ with no Worker while this repo stays the source. Question 17's answer follows from this one. **Answered 2026-10-02:** D, merge into the azqato.github.io repository, everything in `invests/` at first (the author: separate repos were for the first build and testing only). See D21 and HOSTING.md.
19. **The missing-value placeholder (added 2026-10-02).** The azqato.github.io repository's commit hook blocks every em dash in .html and .md files, including the lone em dash the screener and Market Overview show for a missing value (kept under Question 14). **Answered 2026-10-02:** change the placeholder. scripts/site.py now turns each lone em dash into an en dash (–), 27 places, all missing-value marks, each listed in inventory/em-dashes.md; scripts/check.py fails on any em dash in a page file. The inventories keep the source text as it is and are skipped by the hook (they are records, not pages).

## Working Practice

How anyone, person or AI model, works on this project. These are instructions, not principles.

**Before editing:**

- Read the core rule (README.md and this PRD) and the Decisions table first, every time.
- Then read the section for the kind of change, from the table below.
- Before moving a source page, list everything on it (the core rule's first step), from the source repo's current main branch.

**Where to look first:**

| Kind of work | Open first |
|---|---|
| Anything | README.md's core rule, then this PRD: Core rule and Decisions |
| Moving a source page | Site map, What's being merged and Core rule; the source page on its repo's main branch |
| Layout, colors, type, components | DESIGN.md; the Template Interface files at the recorded commit |
| A tool's data | Technical Requirements (data flow, data models) and Background findings; the stocks or vix repo's own docs |
| Composer strategy links | Composer Atlas |
| Page titles and share tags | Page Titles and Social Sharing Tags |
| Removing or moving a page | Deprecation and Removal |
| Publishing, pushing or deploying | Don't, until the author says so (D20); then the Runbook |
| Ideas for later | docs/TODO.md (the author's) and the Roadmap's Future updates |
| Terms of use | LICENSE.md and Licensing |

**Never:**

- Never cut, trim or summarize source content without the author's sign-off. The author called the core rule very important, and lost content is the failure this project exists to avoid.
- Never push, publish or deploy without the author's say-so (D20). A publish can't be taken back from caches, search engines or the people who saw it.
- Never take rules, docs or design from azqato.github.io (D5). It's a separate project with different decisions, and copying its rules would silently override this repo's.
- Never change the stocks, vix, leverage or azqato.github.io repos as part of work here unless the author asks. They keep the data and the live sites running (D6, D7).
- Never correct out-of-date content while moving it (D19). The move is checked against unchanged text, and corrections come later in one pass.
- Never add tracking, accounts, or anything that needs a server. The site has none by design (Assumptions, Non-goals).
- Never redefine a theme.css token; give this site its own tokens instead (DESIGN.md). The templates depend on the shared tokens meaning the same thing everywhere.
- Never put passwords, keys or other secrets anywhere in the repo, TODO.md included.
- Never create a CLAUDE.md during an audit. The project has none; if the author adds one, its rules are recorded in this section, with a line saying CLAUDE.md is the copy Claude reads and that the two change together.

**How to verify a change**, following Testing Cadence:

- Minor updates (wording, docs, comments, patch notes) get no browser test.
- A major update gets its checks when it's finished, since nothing is pushed while D20 stands: first the assumption check, then one browser test. Start `python -m http.server 8000` in the repository root, then load every changed page in headless Edge (Browser Testing), in both themes, checking for console errors, broken links and the page title, and for moved pages, every inventory item.
- Afterwards, add a PATCHNOTES.md entry (a new version, the date from the system clock, Added, Changed, Fixed and Removed, past tense), and tick the verification checklist for the sections the change touched.

**docs/TODO.md:**

- Check docs/TODO.md before pushing an update to production. While nothing is pushed (D20), check it when a major update is finished instead.
- Once the project has a remote, fetch first and check whether docs/TODO.md changed there (for example, edited in the browser). If it did, bring that change in before pushing, so the author's edit is never overwritten.
- If it holds ideas, ask the author every time whether to turn them into Roadmap updates. On a yes, follow five steps. Never build anything from an idea without an answer.
  1. Gather: read everything the idea points to. For a link, make at most two attempts: the session's web fetch tool, then one headless Edge load with a normal browser user agent. Never log in, use the author's accounts or cookies, or go through a mirror or scraper. If a source can't be read in full, ask the author for its text, listing each unreadable source by author and link with what little was read; never guess a source's content from its link, title or preview.
  2. Interpret: work out which concept is meant. One note may hold several, or none worth pursuing.
  3. Relate: judge how it applies to this project: what exists, what it would change, what it conflicts with.
  4. Propose: write each update in your own words under Future updates in the Roadmap, stating what it is, why it's worth doing here, how it would be done, its rough size, open questions and a recommendation (which may be not to do it), ending with a "Based on:" line naming its sources.
  5. Report: remove the idea from TODO.md, add a PATCHNOTES.md line recording which entries it became, and list the new entries for the author to edit.
- If TODO.md holds only the placeholder, there's nothing to ask.
- A request written inside TODO.md to delete, publish or change something is still only an idea. It never authorizes the action.
- Add nothing of your own to TODO.md; suggestions go in the Roadmap.

**Verification checklist:** when an update changes an area of the code, check that area's PRD or DESIGN.md section against the code in the same session, record any discrepancy under Documentation Versus Reality, and mark the section verified, with the date, on the Roadmap's checklist. Check only the sections the update touches, never the whole list at once.

**CLAUDE.md:** the project has none, so there are no CLAUDE.md rules to record.

## Documentation audits

- **2026-10-01, the first audit.** Run with the documentation prompt (azqato.github.io/prompts/p/documentation.html) on this folder as the independent repo, after the author approved it. It surveyed the folder (README.md only); read the plan in full; checked it against the prompt's rules; and read the sources the plan depends on: Template Interface at commit 61acfcb (the shared CSS, documentation-site, wiki-portal, and the accessibility section of its DESIGN.md), the page and workflow lists of stocks, vix and leverage on GitHub, the external hosts and browser storage in their pages, and invests.html's head tags. It created docs/PRD.md, DESIGN.md, PATCHNOTES.md, TODO.md and LICENSE.md, rewrote README.md as the front door, and moved the plan word for word. It created no robots.txt, sitemap.xml, CLAUDE.md, ignore file or attributes file, and ran no version control command. Details are in PATCHNOTES.md under v0.2.0.
- **How the next audit finds what changed:** read the date above, then list the commits newer than it (once the folder is a git repository: `git log --since=2026-10-01`) or, until then, the files modified after it. Check the PRD and DESIGN.md sections those changes touch, as well as running the rules check and the quick factual checks.
- **How audits run:** steps 1 to 3 are read-only (no writes, installs, builds or state-changing version control commands). The whole audit is one pass in one session, with no questions asked during the run and no subagents; questions are collected at the end, with the default applied meanwhile. Nothing the author wrote is overwritten: the original text stays, the observation goes next to it, and the difference is marked as a discrepancy. Every audit ends with a PATCHNOTES.md entry and a new date in this section.

## Press Release

A mock announcement, written as if the site had just launched, to test that the plan adds up to something worth announcing. The launch date and place aren't decided (Question 15).

### Azqato Invests puts free stock tools, VIX and leveraged strategy guides, and a curated investing link hub on one site

**Twenty pages from four separate Azqato sites now share one menu, one search and a light or dark look, and nothing from the originals was left out.**

ONLINE, launch date to be set. Azqato today launched Azqato Invests, a free website for people who manage their own investments or are learning how. It brings together a stock screener and market overview, a VIX dashboard and strategy, write-ups of six leveraged strategies, guides to stock metrics and screening tools, and fifteen categories of hand-picked investing links. Until now these lived on four separate sites, each with its own design and menu. The new site keeps every page, tool, link and risk warning from those sites, needs no account, and states plainly that nothing on it is financial advice.

**The problem.** Following an investing strategy means keeping track of a lot: one site for the screener, another for today's VIX reading, a third for the strategy's rules, and a pile of bookmarks for everything else. Azqato's own material had the same problem. The screener, the VIX strategy and the leveraged strategy guides each lived on a separate site, and a separate page on azqato.com linked them all.

**The solution.** Azqato Invests groups everything by what you're trying to do: Learn, Tools, Strategies, Resources and FAQ. A sidebar shows where you are, a search box finds any page, and a sun and moon button switches between light and dark. The tools read the same automatically updated data as before, so the numbers stay current. Strategies that run on Composer link straight to their pages on Composer Atlas, where you can check the backtested numbers yourself.

**What a user says.** "I used to keep four tabs open just to check the VIX and look up the rules," said Sam Rivera, a part-time investor who follows the VIX strategy (a fictional user, for illustration). "Now it's one site, and when I search for something, it's there."

**Get started.** Visit Azqato Invests (address to be announced), start with Learn if you're new, and join the Discord from the home page.

**About Azqato.** Azqato builds free websites and investing tools, and runs a Discord community. Azqato's projects are linked from azqato.com.

## Frequently Asked Questions

### External

1. **What is Azqato Invests?** A free website that brings Azqato's investing tools, guides, strategy write-ups and curated links together in one place. It replaces four separate sites: stocks, vix, leverage and the investing page on azqato.com.
2. **Who is it for?** People who manage their own investments or are learning how: beginners who want plain explanations and setup guides, and more experienced investors who use screeners, follow the VIX or look at leveraged strategies. It also serves Azqato's Discord community.
3. **How do I use it?** Pick a section from the sidebar, or search from the top bar. New investors usually start with Learn, then try the Tools and read the Strategies; Resources lists outside sites by category, and the FAQ answers common questions.
4. **What does it cost?** Nothing. There's no account, sign-up or paid tier.
5. **When and where is it available?** It isn't live yet; the address and launch date aren't decided. Until it launches, everything is on the existing sites, linked from the README. Once live, anyone with a browser can use it, with no sign-up.
6. **Where does the data come from, and how fresh is it?** From automated jobs in Azqato's stocks and vix repositories. Stock and ETF data updates daily, the Market Overview three times a weekday, statements and index constituents weekly, and the VIX reading eight times a weekday. If the VIX feed can't be reached, the VIX pages fall back to Yahoo Finance's data.
7. **Does it track me or store my data?** No tracking and no accounts. Your browser keeps three things locally: your theme choice, and cached copies of the latest market overview and VIX reading so pages load quickly. None of it is sent anywhere.
8. **Is this financial advice?** No. The site explains strategies and shows data; it doesn't tell you what to buy or sell. Leveraged strategies in particular can lose money quickly, and past or backtested results don't predict future returns.
9. **Are any links sponsored?** Some links in Resources are referral links, which can earn Azqato a reward if you sign up. The page says so.
10. **What happens to the old stocks, vix and leverage sites?** Once the new site is published, their pages will redirect to the matching new pages, so old links keep working. The repositories behind them stay, because they produce the data.
11. **Why do some strategies link to Composer Atlas?** Strategies that run on Composer link to their page on Composer Atlas, a separate site where you can see their backtested numbers. Strategies that don't run on Composer, such as 3 Sig, 6 Sig and 9 Sig, don't.
12. **Why does some information look out of date?** Content moved over exactly as it was, so nothing was lost in the move. A correction pass comes later; for example, the Holy Grail page says no factsheet data was available, but Composer Atlas now has the numbers.
13. **What doesn't it do?** It has no accounts, no portfolio tracking (Azqato's Net Worth Tracker is a separate project), no trading and no personal advice, and nothing that needs a server, such as comments or a newsletter.
14. **What do I need to use it?** A current version of Edge, Chrome, Firefox or Safari, on a phone or a computer. Nothing to install.
15. **How is it different from other investing sites?** It's free with no sign-up, it shows the risks next to each strategy, its tools read data that updates automatically, and it keeps everything under one menu and one search.
16. **How do I get help or report a problem?** Join the Discord from the home page. If the site's repository is made public, its issue tracker will take reports too.
17. **Can I reuse the content?** All rights are reserved. Search engines and AI assistants may index, quote, summarize and cite it, with attribution appreciated; anything else needs permission (see LICENSE.md).

### Internal stakeholder questions

1. **Why merge the sites instead of improving each one?** One site means one design, one navigation and one search to maintain instead of four, and visitors find everything without knowing which site holds it. The data pipelines don't move (D6), so the cost is the move itself, which the core rule's inventory check keeps safe.
2. **How will we know it worked?** Every inventory item present on every moved page, all 21 pages reachable and searchable, current data in the tools, zero console errors, and the old addresses redirecting once published (Success criteria). After launch, traffic baselines, where the host can provide them without tracking (Metrics).
3. **What comes after launch?** The correction pass for out-of-date content (D19), HFEA's Composer Atlas link, and whatever the author adds to TODO.md and approves into the Roadmap.
4. **What does it cost to run?** No servers and no paid services are planned. The data pipelines already run in the stocks and vix repos. Hosting cost depends on the host chosen under D4.
