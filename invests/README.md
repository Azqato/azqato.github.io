# Azqato Invests

A free investing website, being built by Azqato, that brings four existing sites together under one menu, one search and a light or dark look: a stock screener with stock-picking guides, a VIX strategy and dashboard, write-ups of leveraged strategies, and a curated hub of investing links. Nothing on it is financial advice.

## Live site

There's no hosted instance yet. The site is built and tested locally and will be published at https://azqato.github.io/invests/ when Azqato decides. Until then, everything it holds is on the existing sites:

- [Stocks](https://azqato.github.io/stocks/): screener, Market Overview, guides and FAQ
- [VIX](https://azqato.github.io/vix/): the VIX strategy, dashboard and custom builder
- [Leveraged strategies](https://azqato.github.io/leverage/): 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA
- [Investing tools and resources](https://azqato.com/invests): project cards and curated links

## What the site will offer

- **Learn:** plain-language guides to investing philosophy, stock metrics and index and ETF methodology, plus step-by-step setup guides for Finviz and Seeking Alpha.
- **Tools:** a stock screener, a market overview, and a VIX dashboard with a custom builder. Their data updates automatically every weekday.
- **Strategies:** the VIX strategy, and write-ups of six leveraged strategies (3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA) covering their rules, performance and risks. Composer strategies link to their pages on Composer Atlas.
- **Resources:** fifteen categories of hand-picked links to brokers, screeners, ETF lists, charts and economic data. Some are referral links, and the page says so.
- **FAQ:** answers to common questions, searchable as you type.
- **Home:** a starting point into every section, Azqato's other projects, and a button to join Azqato's Discord.

It's free, with no accounts and no tracking.

## Who it's for

People who manage their own investments or are learning how: beginners who want plain explanations and setup guides, more experienced investors who screen stocks or follow the VIX and leveraged strategies, and members of Azqato's Discord community.

## Status

Built and tested locally, not yet published. All 21 pages are built, the site-wide checks have passed (links, accessibility, speed, security), and the publish plan is ready. Next: Azqato's review, then publishing, which happens only when Azqato decides. To run it locally, see the Runbook in [docs/PRD.md](docs/PRD.md#runbook).

## Core rule: preserve everything

> Ingest everything and present it differently while preserving everything.

This rule comes first and overrides everything else in the plan. Every page, section, table, chart, tool, data feed, link, disclaimer and risk warning from the four sites comes over; only the presentation changes (the design, layout, navigation, theme and page addresses), and old addresses will redirect to the new ones. Nothing is cut, trimmed or summarized without Azqato's sign-off, and each page is checked item by item after it moves. The full rule is in [docs/PRD.md](docs/PRD.md#core-rule-preserve-everything).

## Learn more

- [Product requirements](docs/PRD.md): the full plan, decisions and how the project is run
- [Design](docs/DESIGN.md): how the site looks
- [Hosting options](docs/HOSTING.md): where the site could live, compared
- [UI review](docs/UI-REVIEW.md): the 2026-10-02 review of every page and the changes made
- [Patch notes](docs/PATCHNOTES.md): what changed and when
- [Ideas](docs/TODO.md): the author's ideas list
- [Terms of use](LICENSE.md): all rights reserved; not financial advice
