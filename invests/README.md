# Azqato Invests

A free investing website by Azqato that brings four earlier sites together under one menu, one search and a light or dark look: stock-picking guides and a stock screener, index and ETF methodology with a market overview, a VIX strategy with its dashboard and custom builder, write-ups of six leveraged strategies, and a curated hub of investing links. Nothing on it is financial advice.

## Live site

https://azqato.com/invests/ (also served at https://azqato.github.io/invests/). Live since 2026-10-02.

It replaces these earlier sites, which stay up for now and will redirect to their new pages later (docs/PRD.md, Roadmap P13):

- [Stocks](https://azqato.github.io/stocks/): screener, Market Overview, guides and FAQ
- [VIX](https://azqato.github.io/vix/): the VIX strategy, dashboard and custom builder
- [Leveraged strategies](https://azqato.github.io/leverage/): 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA

azqato.com/invests, the old single investing page, now forwards to the new site.

## What the site offers

- **Individual Stocks:** the stock-picking method, the philosophy behind it, the stock metrics, and a stock screener.
- **Indices & ETFs:** index and ETF methodology, and a same-day Market Overview.
- **VIX Strategy:** the strategy, a live VIX Dashboard and a VIX Custom builder.
- **Leveraged Strategies:** write-ups of 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA, covering their rules, performance and risks. Composer strategies link to their pages on Composer Atlas.
- **Resources:** fifteen categories of hand-picked links (some are referral links, and the page says so), step-by-step setup guides for Finviz and Seeking Alpha, and an FAQ you can filter as you type.
- **Home:** a starting point into every section, Azqato's other projects, and a button to join Azqato's Discord.

The tools read data that updates automatically every weekday. It's free, with no accounts and no tracking.

## Who it's for

People who manage their own investments or are learning how: beginners who want plain explanations and setup guides, more experienced investors who screen stocks or follow the VIX and leveraged strategies, and members of Azqato's Discord community.

## Status

Live. Next: Azqato's review of the live site, then the post-launch list (old-site redirects, content corrections and the other Roadmap items). The site lives in the `invests/` folder of the azqato.github.io repository; to build and test it locally, see the Runbook in [docs/PRD.md](docs/PRD.md#runbook).

## Core rule: preserve everything

> Ingest everything and present it differently while preserving everything.

This rule comes first and overrides everything else in the plan. Every page, section, table, chart, tool, data feed, link, disclaimer and risk warning from the four sites came over; only the presentation changed (the design, layout, navigation, theme and page addresses), and the old addresses will redirect to the new ones. Nothing is cut, trimmed or summarized without Azqato's sign-off, and each page was checked item by item after it moved. The full rule is in [docs/PRD.md](docs/PRD.md#core-rule-preserve-everything).

## Learn more

- [Product requirements](docs/PRD.md): the full plan, decisions and how the project is run
- [Design](docs/DESIGN.md): how the site looks
- [Patch notes](docs/PATCHNOTES.md): what changed and when
- [UI review](docs/UI-REVIEW.md): the 2026-10-02 review of every page and the changes made
- [Hosting options](docs/HOSTING.md): where the site could live, compared (a record; option D was chosen)
- [Ideas](docs/TODO.md): the author's ideas list
- [Terms of use](LICENSE.md): all rights reserved; not financial advice
