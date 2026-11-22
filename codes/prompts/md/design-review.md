---
title: Design Review
description: Review a site's design for defects and decoration with no job, citing each element, ranked by priority, and fixed by removing things first.
meta: Claude Code Prompt
---

Gives you a design review backed by evidence rather than taste. Claude looks at the rendered site, its states, and its code, and reports only what it can point to: every finding names the exact element, section, or line of copy, says what harm it does, and is either a quality defect (something broken, unreadable, or confusing) or decoration with no job (a glow, card, label, animation, or effect that adds nothing a visitor needs). Findings are ranked P0 to P3, with repeated instances grouped into one.

The fix it proposes is always removal first. For each suspect element it asks what job the element does, and whether the page is clearer without it; only when removing it would lose something does it suggest the smallest correction in the site's existing style. It never guesses whether AI made the design, never gives a numeric score, never treats a technique as bad in itself (a gradient or a dark theme can be exactly right), and never proposes a new font, palette, or layout unless you ask.

It follows the Template Interface Web Design Standard and Color Standard, which it reads in full first: it looks at eight widths from 320px to 1920px, in light and dark mode, and at a printed US Letter PDF, measures contrast against the Color Standard's required pairings, and checks each page for a hidden brief for AI agents.

It is read-only and stops with the report. Use it before a launch, after a redesign, or whenever a page feels generic and you cannot say why.

## Prompt

```
Review the design of this project's site or app. This is a review, not a redesign: do not edit any file, and stop with the report.

Standards
- Read both standards in full before reviewing, and review against them: the Template Interface Web Design Standard (https://templateinterface.com/standards/web-design/) and Color Standard (https://templateinterface.com/standards/color/). Download the raw HTML with curl; a fetch tool that summarizes drops their rules and tables. If either cannot be read, say so in Unknowns and review without it.

Evidence
- Look at the real thing: open the rendered pages from a local copy (not the live site, unless there is no local way to run it) at 320, 375, 700, 900, 1023, 1150, 1440 and 1920 px (set 320 and 375 with device emulation, since headless windows are clamped near 500px), in light and dark mode, and the states a visitor meets on the main flow: hover, focus, open menus, loading, empty, and error states where they exist. If this project states a browser testing rule, follow it.
- Print each page to a US Letter PDF with headless Edge (--print-to-pdf --no-pdf-header-footer, with a virtual time budget so scripts have run) and look at every sheet. Judge the PDF, not the print CSS.
- Every check is rendered and measured, never judged by reading the code. Contrast is measured by script with the WCAG 2.2 formula, from computed colors.
- Read the styles, tokens, components, copy, and any design document (such as docs/DESIGN.md) so you judge the site against its own system.
- Every finding must cite a concrete location: a page and section, a component, a selector or file and line, or a quoted line of copy. Do not report a general tendency you cannot point to. Anything you could not see or run is listed as unknown, never assumed.

Boundaries
- Do not guess whether AI made the design, and do not give a score.
- Do not call a technique bad in isolation. A gradient, serif, dark theme, glass effect, card, animation, or single typeface can be intentional and right.
- Do not propose a new font, palette, layout, design system, or art direction unless I ask for one. Keep the site's character, including density, edge, or humor that is unusual but works.

What to look for
- Quality defects: unclear or competing primary actions; low contrast or unreadable text; clipping, overflow, or overlap at either width; broken images, links, or controls; information only reachable on hover; missing states the flow needs; unclear labels or missing keyboard focus; accidental inconsistency in spacing, type, color, corner radius, or icons; hierarchy that contradicts what matters most.
- Stacked decoration: glows, gradient text, glass, borders, shadows, grids, particles, beams, noise, or floating shapes where several layers do the same decorative job or compete with the content.
- Repetition: a card around nearly every block, rows of icon-heading-text tiles with interchangeable content, nested rounded containers that express no hierarchy, a stock landing-page sequence unrelated to how this product is bought or used, labels and pills that restate what is next to them.
- Copy: empty superlatives, vague claims, filler, duplicated text, long centered paragraphs.
- Motion that delays reading, moves targets, blocks input, repeats mechanically, or ignores reduced-motion settings. Keep motion that explains state, cause, or place.
- Color: raw color values in component rules instead of roles (tokens); any text, control border, meaningful icon or focus ring below the Color Standard's minimum in either mode; any required pairing that fails in light or dark; status shown by color alone.
- Print: check the PDF against the Web Design Standard's print rules: dark ink on white whatever the screen theme, with a white background on @page as well as html; no controls, navigation, theme switch, live state or decorative art; all content kept, including what tabs or filters hide on screen; a header and footer on every sheet in @page margin boxes (the site name and a subtitle top left, a title for that sheet's section top center using CSS named pages and white-space: nowrap, contact details or a version and date top right, a short note bottom left, "Page " counter(page) " of " counter(pages) bottom right); no card, row or heading split or stranded across a page break; and no fixed paper size in the CSS. A near-empty sheet or a section printed twice is a finding.
- Brief for AI agents: each page should end with a brief for AI agents as the last thing in the body: what the page is and what a browser would show, what script draws or hides, which controls don't really work, and where the full text and data live, with complete links. It is written for an agent that can't run scripts or see the layout, hidden with a visually hidden clip (never hidden, display: none or aria-hidden, which text extractors drop), left out of print, and generated from the same data as the page. Check it exists, matches the page, and its links resolve.
- Unsupported proof: metrics, customers, logos, testimonials, ratings, or activity presented as evidence that the project does not show to be real.

The removal test, for every suspect element
1. Say what job it does: information, state, action, hierarchy, or brand meaning.
2. Ask whether removing it would make the page clearer without losing that job.
3. If yes, recommend removing or merging it.
4. If no, recommend the smallest correction using the site's existing system.
5. Suggest a replacement only when removal would lose something real.

Priorities
- P0: blocks the main task, a severe accessibility failure, or proof that misleads.
- P1: materially harms understanding, trust, navigation, or interaction.
- P2: repeated decoration or inconsistency that weakens hierarchy or identity.
- P3: minor polish.

Report
- Verdict: one short paragraph on the main problems and what to remove first.
- Checked: the pages, widths, modes, and states you actually looked at, and each PDF's page count.
- Findings: a table with priority, class (defect or decoration), pattern, evidence, harm, and the fix. Five to eight findings by default, the highest impact first, with repeated instances grouped into one.
- Unknowns: what you could not check.
- End with the single removal or correction that would improve the site most.
Then wait. If I ask you to apply fixes, apply only the ones I choose.
```
