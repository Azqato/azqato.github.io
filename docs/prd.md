# PRD.md — TQQQ Strategies Site

**Version:** 1.4
**Status:** Active
**Author:** Azqato

---

## 1. Overview

### Problem

Information about leveraged ETF strategies is scattered across forum threads, videos, and paywalled newsletters. There is no single, clean, readable reference that documents the well-known TQQQ strategy frameworks side by side in a consistent format.

### Solution

A static, wiki-style educational site that documents three TQQQ strategies, each on its own dedicated page with an identical structure. Readers can learn each framework, compare them, and dig into resources, all in one place.

### Goals

1. Document six strategies (3 Sig, 6 Sig, 9 Sig, TQQQ For The Long Term, Holy Grail, HFEA) in a consistent, readable format
2. Ship a working multi-page site skeleton with placeholder strategy content that can be filled in iteratively
3. Maintain visual and structural consistency with other Azqato properties
4. Stay fully static and dependency-free so it deploys to GitHub Pages with zero configuration

### Non-Goals

- No live market data, charts, or price feeds
- No backtesting tools or calculators (possible future roadmap item)
- No user accounts, comments, or community features
- No recommendations or signals. The site documents methodologies, it does not tell anyone what to do

---

## 2. Audience

**Primary:** Self-directed retail investors who already know what TQQQ is and want a structured reference for the major strategy frameworks built around it.

**Secondary:** Newer investors researching leveraged ETFs who need an honest, hype-free introduction including the risks.

**Reading mode:** Deliberate and slow. Visitors come to study, not skim. Long-form content with strong hierarchy and in-page navigation.

---

## 3. Scope

### Pages

| Page | File | Purpose |
|------|------|---------|
| Home | `index.html` | Introduce leveraged ETFs and TQQQ, present all strategies as cards, set the educational tone, link out to each strategy page |
| 3 Sig | `3sig.html` | Dedicated page for the 3 Sig strategy |
| 6 Sig | `6sig.html` | Dedicated page for the 6 Sig strategy |
| 9 Sig | `9sig.html` | Dedicated page for the 9 Sig strategy |
| TQQQ For The Long Term | `tqqq-ftlt.html` | Dedicated page for the FTLT strategy |
| Holy Grail | `holy-grail.html` | Dedicated page for the Holy Grail strategy |
| HFEA | `hfea.html` | Dedicated page for Hedgefundie's Excellent Adventure |

### /strategies Convention

Every `.md` file in `/strategies` maps to exactly one page, one nav entry, and one index card. Adding a new strategy means:

1. Create `/strategies/<name>.md` as the content source
2. Create `<name>.html` at the repo root using the strategy page template
3. Add a nav link to every page (sidebar and top-bar) after existing strategy links, before Support
4. Add a strategy card to `index.html` in the same order as the nav

The Support link (`https://azqato.github.io/support.html`) is always the last nav item and is never replaced by a strategy link.

### Strategy Page Template

Every strategy page uses the same section skeleton so readers can compare frameworks easily:

1. **Hero**: strategy name, one-line summary, origin attribution
2. **Overview**: what the strategy is and the core thesis
3. **Rules and Logic**: the mechanical rules, rebalancing cadence, allocation targets
4. **Performance Notes**: historical behavior, drawdown character, known weaknesses
5. **Risks and Caveats**: leveraged ETF specific risks as they apply to this strategy
6. **Resources**: books, threads, and source material

Initial build ships these sections as labeled placeholders. Content is authored in `/strategies/*.md` first, then ported into the HTML.

### Content Source Files

Each strategy has a matching markdown file in `/strategies` that serves as the source of truth for that strategy's content. HTML pages are updated from these files manually. No client-side markdown rendering in v1.

### Research Sources Convention

When a strategy page requires external research, the URLs used must be stored inside the strategy's `.md` file using an HTML comment block. This block is for the content author's reference only and must never be ported to the HTML page.

**Format:**

```markdown
<!-- RESEARCH SOURCES — internal reference only, do not port to HTML -->
- https://example.com/article (description of what this source covers)
<!-- END RESEARCH SOURCES -->
```

**Rules:**

1. The block is placed at the top of the file, immediately after the frontmatter metadata fields
2. Each line inside the block is one URL with a parenthetical note on what that source contributed
3. When porting content from `.md` to `.html`, the `<!-- RESEARCH SOURCES -->` block and everything inside it is omitted entirely — it never appears in any HTML file
4. If additional sources are discovered later, they are added to the block in the `.md` file

This convention ensures research sources are preserved with the content without being exposed in the public-facing website.

---

## 4. Requirements

### Functional

- F1: Multi-page static site, seven HTML pages, shared stylesheet and script
- F2: Persistent wiki-style sidebar navigation on desktop, collapsing to a sticky top bar on mobile
- F3: In-page anchor navigation on strategy pages with scroll-based active state highlighting
- F4: Strategy cards on the index page linking to each strategy page
- F5: Consistent footer with educational disclaimer on every page
- F6: Placeholder content blocks on all six strategy pages, clearly labeled

### Technical

- T1: HTML, CSS, and vanilla JavaScript only. No frameworks, no build tools, no package manager
- T2: Deployable to GitHub Pages from the repo root with no configuration
- T3: No external dependencies of any kind (fonts, CDNs, libraries)
- T4: Single shared `css/style.css` and `js/main.js` across all pages
- T5: Works with JavaScript disabled (JS is enhancement only: scroll highlighting, mobile nav)

### Content

- C1: No real-time data references. All content must remain accurate regardless of market conditions
- C2: Educational tone, no hype, no calls to action to buy or sell
- C3: Every page carries the disclaimer: educational use only, not financial advice
- C4: Strategy attribution must credit original authors and sources where applicable

---

## 5. Success Criteria

- Site is live at https://azqato.github.io/leveraged-strategies/ with all seven pages navigable
- All six strategy pages share an identical section skeleton
- Lighthouse accessibility score of 95+ on every page
- Total page weight under 100KB per page (no images required in v1)
- Strategy content can be updated by editing one HTML file per strategy without touching layout code

---

## 6. Milestones

| Milestone | Status | Deliverable |
|-----------|--------|-------------|
| M1: Skeleton | Complete | Seven pages, shared nav, placeholder strategy sections |
| M2: Content drafts | Complete | All six `/strategies/*.md` files researched and fully written |
| M3: Content port | Complete | All seven HTML pages rewritten with full strategy content. All placeholders replaced. Four badge/lead corrections applied. Site live at https://azqato.github.io/leveraged-strategies/ |
| M4: Polish | Pending | Accessibility pass, responsive QA, Lighthouse audit |

---

## 7. Open Questions

- Should a comparison page (all three strategies side by side in a table) be added in a future version?
- Is a glossary page for leveraged ETF terms (volatility decay, daily reset, beta slippage) worth adding?
- Should `/strategies` markdown eventually be rendered client-side, or remain reference-only?

---

## 8. Version History

| Version | Date | Summary |
|---------|------|---------|
| 1.4 | June 2026 | Marked M3 milestone complete. Added live site URL. Updated success criteria with live URL |
| 1.3 | June 2026 | Updated scope to reflect six strategies and seven pages. Marked M1 and M2 milestones complete. Updated F1, F6, and success criteria counts |
| 1.2 | June 2026 | Added HFEA to pages table. Documented Research Sources Convention: URLs stored in `<!-- RESEARCH SOURCES -->` comment blocks in .md files, never ported to HTML |
| 1.1 | June 2026 | Added 3 Sig and 6 Sig pages. Documented /strategies convention: each .md file drives a page, nav entry, and index card. Support link added as permanent last nav item |
| 1.0 | June 2026 | Initial PRD. Four-page scope, placeholder-first build, content philosophy and technical constraints defined |
