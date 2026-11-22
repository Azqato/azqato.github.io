---
title: Mobile Audit
description: Check every page at eight screen widths and on Letter paper for overflow, color and print bugs, fix the root causes, and verify by measuring, not by eye.
meta: Claude Code Prompt
---

Runs a full mobile-friendliness and responsive-design pass across an entire site, following the Template Interface Web Design Standard and Color Standard, which it reads in full first. It checks three surfaces, mobile, desktop and print: every page at a fixed set of widths (320px through 1920px) for horizontal overflow, container overflow, unwrapped toolbars, modal sizing, and clipped text. It also targets four specific CSS bug patterns that are common and easy to miss: the `overflow` shorthand silently canceling an `overflow-x` setting, bare `1fr` grid tracks forcing page-level overflow from wide content, flexbox children ignoring their flex parent's width because of the default `min-width: auto`, and doubled spacing when `margin` stacks with a flex/grid `gap`.

It also measures color contrast in light and dark mode against the Color Standard's required pairings, prints every page to a US Letter PDF and reads each sheet (ink on white, no controls or stale live state, hidden tab content included, a header and footer on every page, nothing split across a break), and checks that each page ends with a hidden brief for AI agents.

Verification is done by injecting a debug script that reads `scrollWidth`/`clientWidth` and element bounding rectangles, not by eyeballing screenshots, since headless browsers enforce a minimum viewport width that makes narrow screenshots unreliable; the print check reads the PDF, not the print CSS. Any fix that changes how content is presented (not a pure CSS correctness fix) is flagged for a design decision before implementation. The prompt ends with updating the project's existing changelog and planning docs with the root cause and fix, following whatever documentation conventions the project already has.

## Prompt

```
Do a mobile-friendliness / responsive audit-and-fix pass across this entire site, following this process.

First read both standards in full and follow them: the Web Design Standard (https://templateinterface.com/standards/web-design/) and the Color Standard (https://templateinterface.com/standards/color/). Download the raw HTML with curl; a fetch tool that summarizes drops the rules and tables. If either cannot be read in full, stop and tell me. Where a standard and this project's own rules disagree, quote both and ask me which wins.

## 1. Audit scope
Mobile, desktop and print are three surfaces, and each one is checked. Every check is rendered and measured, never judged by reading the code.

Screens: check every page/view at these widths: 320px, 375px, 700px, 900px, 1023px (or your main sidebar/desktop breakpoint), 1150px, 1440px, 1920px. The widths are samples, so also step the width from 320px to 1920px in 20px steps, measuring overflow by script, to catch a bug that lives only between them. For each width, check for:
- Horizontal page overflow (the page itself becomes wider than the viewport)
- Elements that overflow their own container without an intended scroll affordance
- Any table, wide toolbar, or button row that doesn't wrap or reflow cleanly
- Modal/dialog sizing at narrow widths
- Text/labels getting clipped or overlapping

Color, in both light and dark mode:
- Colors are used through roles (custom properties such as a text, muted-text, accent or danger token), not raw hex values in component rules. List every raw value you find.
- Measure contrast with the WCAG 2.2 formula, by script, from computed colors: 4.5:1 for body text, 3:1 for large text, control borders, meaningful icons and the focus ring, each measured against what is directly behind it. Cover every pairing the Color Standard lists as required.
- No status is shown by color alone, and links inside running text are underlined.

Print, on US Letter paper (8.5 by 11 in):
- Dark ink on white whatever the screen theme, page margins included: the print styles set a white background on @page as well as on html.
- Left out: navigation, controls, the theme switch, live state that will be wrong tomorrow (an "Open now" badge, "Today", countdowns) and decorative illustrations.
- Kept: everything a reader wants on paper, including content hidden behind tabs, accordions or filters on screen, each part under its own heading.
- A header and footer on every sheet, drawn in @page margin boxes: the site name and a subtitle top left; a title naming that sheet's section top center, set with CSS named pages (@page menu { @top-center { content: "Menu"; } } with .menu { page: menu; }) and white-space: nowrap; contact details, or a version and date, top right; a short note bottom left; "Page " counter(page) " of " counter(pages) bottom right. A new named page starts a new sheet, so short sections should share one name. A CSS table header does not repeat on every printed page in Chromium, so it is no substitute for margin boxes.
- No card, row, figure or heading split or stranded across a page break (break-inside: avoid; break-after: avoid on headings), and no near-empty pages from forced breaks.
- No fixed paper size in the CSS: a page that fits A4 (8.27 in wide) also fits Letter.

Brief for AI agents:
- Each page should end its body with a section for AI agents that says what the page is and what a browser would show, what script draws or hides, which controls don't really work, and where the full text and data live, with complete links. It is written for an agent that can't run scripts or see the layout, hidden from sighted readers with a visually hidden clip (never hidden, display: none or aria-hidden, which text extractors drop), left out of print, and generated from the same data as the page. Check that it exists, is last in the body, reads correctly with scripts off, matches the page, and that its links resolve. Report gaps; don't add one without asking (section 4).

## 2. Specific bug patterns to check for (these are common, easy to introduce, and easy to miss)
- **CSS `overflow` shorthand resetting both axes**: if any element sets `overflow-x: auto` and elsewhere in the same rule (or a later rule) sets the bare `overflow: hidden`/`overflow: <value>` shorthand, it silently cancels the x-axis setting. Grep for elements with both an explicit `overflow-x`/`overflow-y` AND a bare `overflow` declaration.
- **CSS Grid implicit min-width on `1fr` tracks**: any `grid-template-columns` using a bare `1fr` has an implicit `min-width: auto`, which resolves to the intrinsic content width, not zero. If a grid cell contains something wide (a table, a long button row), it can force the whole grid, and the page, wider than the viewport. Fix is `minmax(0, 1fr)` instead of `1fr`. **Check this in EVERY media query that touches the same grid**, not just the desktop rule, since it's common to fix it in one breakpoint and have a separate mobile override silently reset it back to a bare `1fr`.
- **Flexbox children with default `min-width`/`min-height: auto`**: a flex item's default min-size is `auto`, which for a large-content child (e.g. a scrollable table wrapper inside a `flex: 1` column) resolves to "big enough to fit everything," not "shrink to the space given." This causes the child to overflow its flex parent instead of scrolling internally. Fix is `min-width: 0` / `min-height: 0` on the flex item.
- **Redundant spacing when adjacent elements are in a flex/grid container with `gap`**: if a container already has `gap`, don't also add `margin` on a child for spacing, since they stack and double that one gap. Check any element that was moved into a `gap`-based container after being styled for a different original position.
- **`display` beating `hidden`**: any rule that sets `display` overrides the `hidden` attribute. Check hidden things by their rendered box, not their markup.
- **Print bugs**: only the open tab panel printing; a dark theme on paper (backgrounds dropped, pale text left); frozen live state; hero art filling a sheet; a forced page break leaving a near-empty page; and a print rule that loses to a heavier screen selector (`.panel.panel` beats `.panel`) and so does nothing.

A search of the CSS finds suspects; only a rendered measurement confirms a bug.

## 3. Verification methodology, do NOT rely on screenshots alone
Drive Microsoft Edge rather than Chrome, unless the project states its own
browser testing rule. Chrome is typically the owner's day-to-day browser and
driving it disturbs a live session; Edge runs the same engine, so every
measurement below is identical.

Any headless Chromium browser enforces an effective minimum viewport (~485-500px) even when you request a smaller `--window-size`, and screenshot pixel dimensions don't always match the actual layout viewport. Screenshots below that width will look broken even when there's zero actual overflow, and can also miss real bugs that only show up in specific coordinate ranges. Instead:
- Inject a small debug `<script>` into a scratch copy of the page that prints `window.innerWidth`, `document.documentElement.scrollWidth`, `document.documentElement.clientWidth`, and `getBoundingClientRect()` for suspect elements.
- The reliable check for "is there page-level overflow" is `scrollWidth === clientWidth`, not a visual read of a screenshot.
- For subtler layout bugs (like uneven spacing between sibling buttons), measure `getBoundingClientRect().left`/`.right` for every sibling and diff the gaps programmatically rather than eyeballing a zoomed screenshot.
- Test against a local copy served via `python -m http.server`, not the live site, so fixes can be verified before shipping.
- For 320px and 375px, set the viewport with the DevTools Protocol's `Emulation.setDeviceMetricsOverride`, since `--window-size` is clamped. Use a scratch browser profile in the temp folder and a virtual time budget, so the page's scripts have run and extensions add no noise, and delete the profile afterwards.
- Print each page to PDF with headless Edge (`--headless=new --no-pdf-header-footer --virtual-time-budget=4000 --print-to-pdf=<file>`), once with the screen in light mode and once in dark. Check the PDF, not the CSS: count its pages with a script, extract its text to confirm nothing is missing, and render every page to an image and look at it.
- Screenshots still help me see a fix, as evidence alongside the measurements rather than instead of them. For each visual fix, take the before, the key moment, and the after in the same framing (same width, scroll position, and state). Look at every image before trusting it, and retake any that shows a half-loaded page, missing fonts, or the wrong state. Label them honestly: a narrow headless window is a phone-width browser check, not a test on a device.

## 4. Design decisions, ask, don't guess
If fixing overflow requires a real design choice (e.g., should a wide table hide columns responsively, switch to a card layout, or just gain a visible horizontal scrollbar; should hidden content be recoverable via a menu), stop and ask which approach to use before implementing. Don't silently pick an approach for anything that changes how content is presented, only for pure bug fixes (CSS correctness issues with one obviously correct fix). In print, the wording of the header and footer, which sections share a named page, and leaving out anything beyond controls, live state and decoration are design choices; so are adding a brief for AI agents and adding a color role. Propose them and ask.

## 5. Regression safety
Before and after each fix, verify no functional/data regression, whatever this site's zero-regression check is (a known-good rendering of key data, a specific test page's expected content, etc.), reconfirm it matches after the CSS/layout changes, since these are render-only changes that shouldn't touch logic.

## 6. Documentation
After the fixes are verified, update this project's changelog/patch-notes file with a dated entry describing what was found and fixed (root cause, not just "fixed mobile bugs"), and update any roadmap/PRD-style planning doc if this project has one. Follow whatever documentation conventions already exist in this repo (check for existing docs before creating new ones).

Work through this systematically: audit first and report what you find across all breakpoints, then ask about any open design questions, then implement and verify, then document. Finish with a report: each width and page checked, the scrollWidth and clientWidth measured at each, each contrast pairing measured in light and dark mode with its ratio, each page's PDF page count and the top-center title on every sheet, whether each page has a brief for AI agents, what was fixed, and anything you could not check. Then go through the Web Design Standard's checklist and mark each item pass, fail or not checked.
```
