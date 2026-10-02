# DESIGN - Azqato Invests

How Azqato Invests looks and behaves: the visual rules, the components and the reasons behind them. There's no site code yet, so this describes the planned design. Its values were read from the Template Interface templates chosen in D8, at commit 61acfcb, on 2026-10-01. The PRD's verification checklist shows what has been checked against site code (nothing yet).

The Design details and Template ratings sections moved here from README.md word for word on 2026-10-01. Everything else was written by that day's documentation audit from the template code; text that sets something new, rather than recording what the templates do, says so.

## Design philosophy

A calm, readable reference: documentation-site's sidebar, breadcrumbs and single accent color carry every inner page, so the content, risk warnings included, is what stands out. The template supplies structure and styling, and the sources supply every word, number and link (core rule). Light and dark are the same site in two palettes, and motion only ever helps someone keep their place. (Drafted by the 2026-10-01 audit from D8 and the core rule.)

## Where the design comes from

- **D8:** `documentation-site` for every inner page and `wiki-portal`'s directory layout for the home page, borrowing `help-center`'s searchable FAQ and step-by-step guides, `admin-dashboard`'s summary tiles and table styling, and `blog-article`'s reading-progress bar. Template ratings, below, records why.
- **Template Interface** is the author's private template repo, `Azqato/templateinterface`. This document records it at commit 61acfcb (2026-10-01, "Rename to Template Interface; add return bar to every template page"). Record the commit each copied file comes from, since the templates are still changing.
- **The template contract.** Every template loads three shared stylesheets (theme.css for tokens, base.css for element defaults, components.css for shared patterns) and then its own styles.css. A template adds local tokens (documentation-site's `--pp-*` on `.pp-page`, wiki-portal's `--wiki-*` on `.wiki-page`) and never redefines a token from theme.css. This site follows the same rule.
- **Template Interface's own docs/DESIGN.md** is the reference for anything this document doesn't cover. Where the two differ, this document wins for this site.

## Color palette

Two themes, light and dark (D10), switched with the ☀️/🌙 button. Uses below come from the rules that reference each token in the template's stylesheet. Parts that are marked as demo-only (see Component patterns) still use some tokens, and those uses are listed so nothing is missed when the parts come out.

### Light theme: documentation-site's palette

Declared on `.pp-page` in documentation-site's styles.css.

| Token | Hex | Used for |
|---|---|---|
| `--pp-bg` | `#ffffff` | Page, top bar, main column and "On this page" column backgrounds |
| `--pp-rail` | `#f4f6f7` | Sidebar, table header, footer and search button backgrounds |
| `--pp-hover` | `#e9edef` | Sidebar link hover background |
| `--pp-line` | `#e0e5e8` | Dividers and card borders: top bar, cards, tables, pager, footer, search panel |
| `--pp-line-strong` | `#c3ccd1` | Borders on controls (inputs, the menu and close buttons, search button, keyboard hints) and breadcrumb separators |
| `--pp-ink` | `#13201b` | Headings, bold text, inline code, table headers, labels, input text, the logo |
| `--pp-text` | `#2b3833` | Body text, sidebar links, the lede, cards, table cells, search |
| `--pp-muted` | `#55625c` | Secondary text: breadcrumbs, meta line, group labels, "On this page" links, help text, footer, search results |
| `--pp-emerald` | `#0b7a52` | The one accent: links, the focus ring, solid buttons, the logo mark, step numbers, hover borders, the current-item marker in the sidebar and "On this page" |
| `--pp-emerald-deep` | `#075c3d` | Accent text and hover: solid button hover, the current sidebar link, link hover, note callouts, pager titles |
| `--pp-emerald-pale` | `#e2f3eb` | Accent backgrounds: the current sidebar link, note callouts, card kickers, the selected search result |
| `--pp-emerald-line` | `#b5dfcb` | Note callout border |
| `--pp-mint` | `#6ee7b7` | Accent inside dark code blocks: the selected code tab, copy button hover, focus inside code |
| `--pp-code-bg` | `#0d1714` | Code block background |
| `--pp-code-bar` | `#14221d` | Code block title bar |
| `--pp-code-line` | `#22342d` | Code block borders |
| `--pp-code-text` | `#e3ede8` | Code text |
| `--pp-code-dim` | `#b3c3bc` | Code tab and label text |
| `--pp-amber-bg` | `#fff6e1` | Warning callout background |
| `--pp-amber-line` | `#efd395` | Warning callout border |
| `--pp-amber` | `#a35d00` | Warning callout text |
| `--pp-amber-ink` | `#653a00` | The "required" marker and the "fix" tag |
| `--pp-blue` | `#1c5cb8` | The GET method badge (demo content) |
| `--pp-red` | `#b3261e` | Invalid input border and field error text |
| `--pp-mark` | `#fbeeb0` | Search match highlight |

documentation-site also uses colors written directly in its rules rather than as tokens. A dark theme has to override these too:

- White backgrounds (`#fff`): keyboard hints, the menu's close button, the sidebar card, table row headers, inputs, the search dialog, and the icon-only search button at 640px and below.
- White text (`#fff`): solid buttons and their hover, step numbers, the logo mark's stroke, method badges, and the code tabs and copy button on hover.
- Inline code: border `#d9e4de`, background `#eef4f1`.
- Code syntax colors: `#8fa39a`, `#9be9b9`, `#8cc8ff`, `#f7c873`, `#d4b1ff`, `#ffb68a` and `#7fe0de`; copy button border `#33483f` and text `#d5e2dc`.
- Tags: "change" `#e6eefa` with `#1a4a91` text; "fix" background `#fff0dc`.
- Shadows and overlays, tinted green-black: the card hover shadow, the search dialog shadow and backdrop, the open drawer's shadow, and the scrim behind it (`rgba(13, 23, 20, 0.45)`).
- Print styles: black on white.

### Dark theme: the shared tokens

Declared on `:root` in Template Interface's theme.css. None of the templates has a dark mode of its own (Design details), so the dark theme is built on these. They are azqato.com's dark colors apart from one hover shade.

| Token | Hex | Used for in the shared CSS | azqato.com's matching token |
|---|---|---|---|
| `--color-canvas` | `#0d1117` | Page background | `--bg`, same |
| `--color-surface` | `#161b22` | Sidebar, cards, callouts, table headers | `--surface`, same |
| `--color-surface-inset` | `#010409` | Code blocks, inline code, inputs, sidebar link hover | None |
| `--color-border-default` | `#30363d` | Sidebar edge, cards, inputs | `--border`, same |
| `--color-border-muted` | `#21262d` | Code block borders, table rows | None; azqato.com's `--tag-bg` has the same hex |
| `--color-text-primary` | `#e6edf3` | Body text, headings, table headers | `--text`, same |
| `--color-text-secondary` | `#8b949e` | Sidebar links, captions, table cells | `--text-muted`, same |
| `--color-text-tertiary` | `#7c8487` | Not used in the shared CSS | None |
| `--color-accent` | `#00d4a0` | Links, primary buttons, the active nav item, the focus ring | `--accent`, same |
| `--color-accent-emphasis` | `#22e6b5` | Link and primary button hover | `--accent-hover` is `#00e6b0`, the one difference |
| `--color-accent-muted` | `#0d3d31` | Active sidebar link and tab backgrounds, secondary button hover | None |
| `--color-danger` | `#f85149` | Caution callout | None |
| `--color-warning` | `#d29922` | Warning callout | None |
| `--color-success` | `#3fb950` | Not used in the shared CSS | `--green`, same |

azqato.com's other tokens have no shared counterpart: `--purple` `#bc8cff`, `--orange` `#ffa657` and `--card-hover` `#1c2128`.

### How the two themes fit together

**Built 2026-10-02 (P2).** Template Interface added a dark mode to documentation-site after this document was written (commit ed840da, v0.15.0): its own `--pp-*` tokens get dark values under `:root[data-theme="dark"] .pp-page`, screen only, so print stays light. This site uses that dark palette as it is: page `#0e1513`, rail `#121b18`, text `#cbd8d1`, headings `#e6efe9`, accent `#3ccf93`. The plan below, written before the template had a dark mode, is kept as the record.

- The moved content's own colors are mapped to the site's tokens in site.css, so a source's surfaces, borders, text and accent follow the theme. The sources' data colors keep their source values in dark and take darker counterparts in light (Data colors, below).
- azqato.com's nav takes the shared dark tokens in dark and the site's light palette in light.

Planned; not decided in detail.

- The dark theme gives documentation-site's own tokens dark values under a dark-theme selector, taken from the shared tokens, and overrides the literal colors listed above. It never redefines a theme.css token (the template contract). Which shared value each `--pp-*` token takes isn't decided. The obvious starting point pairs them by role: page with canvas, sidebar with surface, text with text, accent with accent.
- In dark, solid buttons need dark text: white on `#00d4a0` measures 1.92:1, while `#0d1117` on it measures 9.85:1 (Accessibility standards). components.css's primary button already uses `#0d1117`.
- Every new pairing is checked for contrast in both themes before it ships.
- **azqato.com's nav (only if D9 stays).** azqato.com is dark-only, so its nav needs a light version for this site's light theme (Design details). Its dark colors are the shared tokens above.
- **The home page** uses the site's light and dark themes; wiki-portal's violet palette (`--wiki-*`: canvas `#241f3f`, accent `#7d5fe6` and 12 more) isn't used. This is the PRD's assumption, read from D8's wording, and Question 9; the author confirmed it on 2026-10-01.
- **Data colors.** The tools' own colors (chart lines, up and down values, VIX levels) were read on 2026-10-01 (P1). stocks: positive `#3fb950`, negative `#f85149`, warning `#ffa657`, and screener tiers S+ `#bc8cff`, S `#2ea043`, A `#7ee787`, B `#e3b341`, C `#ffa198`. vix: BIL `#3b82f6`, SPY `#00ff88`, QQQ `#f59e0b`, TQQQ `#ef4444`, on its own dark palette (`#0a0e1a` page). All were chosen for dark backgrounds, so each needs a light-theme counterpart with its contrast checked. They come over with the tools (core rule) and get recorded here when the tools move, with their contrast checked in both themes.
  **Light-theme counterparts, chosen 2026-10-02 (P2; contrast checked in the P6 browser test):** stocks and leverage positive `#1a7f37`, negative `#cf222e`, warning `#9a6700`, purple `#8250df`; leverage strategy colors 3 Sig `#0969da`, 6 Sig `#9a6700`, 9 Sig `#0550ae`, HFEA `#bc4c00`, FTLT `#1a7f37`, Holy Grail `#8250df`; vix green `#047857`, amber `#b45309`, blue `#1d4ed8`, red `#b91c1c`, orange `#c2410c`, with the same values for its five tiers. **Changed 2026-10-02 after the contrast test (scripts/browser.py):** light positive `#116329`, negative `#a40e26`, warning `#7d4e00` (the first choices were 4.0 to 4.3:1 on their badge tints); vix amber `#92400e`; screener tiers in light S+ `#6639ba`, S `#116329`, A `#1a7f37`, B `#7d4e00`, C `#a40e26` (their text is colored, not only the fill); VIX tickers in light BIL `#1d4ed8`, SPY `#047857`, QQQ `#92400e`, TQQQ `#b91c1c` (strategy.js and custom.js now give them as CSS variables with the source hex as fallback, so they follow the theme); white text on the light green VIX button; and in dark, the stocks red badge text `#ff7b72` (the source's `#f85149` was 4.1:1 on its tint). The VIX donut's center text, border and label read the theme's colors (assets/js/vix/chart.js, a marked change).

## Typography

**Minimum size (UI review, 2026-10-02):** no text under 12px. scripts/site.py raises source `font-size` values under 12px or 0.75rem (`min_font`), and site.css sets the template's and this site's small text (table headers, labels, badges, the sidebar card) to 12px or more. Figures in the stocks tables use the site font with tabular digits instead of a mono font. The VIX pages keep their mono font for data, as SF Mono, Consolas or Liberation Mono (Courier New last, since its Q reads as underlined).

No web fonts: every face is a system font stack.

- documentation-site, used for every inner page: text `"Segoe UI", system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif` (`--pp-sans`); code `Consolas, "SF Mono", Menlo, "Liberation Mono", monospace` (`--pp-mono`). The base is 16px with a line height of 1.6, and 1.7 inside articles.
- The shared stack, used by base.css, components.css and wiki-portal: text `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` (`--font-body`); code `ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace` (`--font-mono`).

### Roles (documentation-site)

| Role | Size | Weight | Line height | Notes |
|---|---|---|---|---|
| h1 | 2.5rem (2rem at 640px and below) | 700 | 1.15 | Letter spacing -0.02em |
| Lede (the paragraph under h1) | 1.2rem (1.08rem at 640px and below) | 400 | 1.55 | |
| h2 | 1.5rem (1.3rem at 640px and below) | 650 | 1.25 | Letter spacing -0.01em |
| h3 | 1.15rem | 650 | 1.3 | |
| Body | 1rem | 400 | 1.7 | |
| Caption: meta line, breadcrumbs, footer, "On this page" links | 0.875rem | 400 | "On this page" links 1.45 | |
| Label: sidebar group names, the "On this page" title, the search results heading | 0.75rem | 700 | | Uppercase, letter spacing 0.06em |
| Form label | Inherited | 600 | | |
| Sidebar link | 0.95rem | 600 for the current page | | |
| Table | 0.9rem; header 0.8rem | Header 700 | 1.5 | Header letter spacing 0.02em |
| Button | 0.9rem | 600 | | |
| Code, inline | 0.875em | | | |
| Code, block | 0.875rem (0.8125rem at 640px and below) | | 1.65 | |
| Help text under fields | 0.85rem | | | |
| Tag | 0.75rem | 700 | | |
| Logo | Name 1.1rem; tag 0.75rem | Name 700; tag 600 | | |

### The shared scale (theme.css)

Sizes: xs 0.75rem, sm 0.875rem, base 1rem, md 1.125rem, lg 1.25rem, xl 1.5rem, 2xl 1.875rem, 3xl 2.25rem, 4xl 3rem. Line heights: tight 1.25, normal 1.5, relaxed 1.7. Weights: 400, 500, 600, 700.

base.css applies them to plain elements: body at base size with relaxed line height; headings semibold with tight line height (h1 3xl, h2 xl, h3 lg, h4 md); small text and `.caption` at xs in the secondary text color.

## Spacing system

- **The shared scale, on a 4px base:** `--space-1` 0.25rem (4px), `--space-2` 0.5rem (8px), `--space-3` 0.75rem (12px), `--space-4` 1rem (16px), `--space-5` 1.25rem (20px), `--space-6` 1.5rem (24px), `--space-8` 2rem (32px), `--space-10` 2.5rem (40px), `--space-12` 3rem (48px), `--space-16` 4rem (64px), `--space-20` 5rem (80px). base.css spaces headings with it (h2 starts `--space-10` below the text above it, h3 `--space-8`, h4 `--space-6`; every heading leaves `--space-4` below) and leaves `--space-6` after paragraphs and lists.
- **documentation-site uses pixel values rather than the scale.** The main column is padded 32px 48px 72px (top, sides, bottom), then 32px 40px 64px at 1150px and below, 28px 24px 56px at 900px and below, and 20px 16px 48px at 640px and below. The sidebar is padded 24px 16px 32px.
- **Corner radius:** documentation-site uses 6px everywhere (`--pp-radius`); the shared scale is 4px, 6px, 12px and fully round.
- **Shadows (shared):** small `0 1px 2px rgba(0, 0, 0, 0.4)`, medium `0 4px 12px rgba(0, 0, 0, 0.5)`, large `0 8px 24px rgba(0, 0, 0, 0.6)`.
- **Layout sizes:** documentation-site's top bar is 60px tall (`--pp-top`), the sidebar 260px wide (`--pp-rail-w`) and the "On this page" column 240px, and article content is capped at 760px. wiki-portal's rail is 168px, its content is capped at 1120px (1440px on a page marked `is-wide`), with a `--space-8` gutter under a 132px masthead (190px at 760px and below). The shared layout tokens (`--sidebar-width` 280px, `--content-max-width` 780px, `--portfolio-max-width` 1200px) belong to Template Interface's own pages.

## Breakpoints

All are maximum widths, so each applies at that width and below.

### Inner pages (documentation-site)

| Width | What changes |
|---|---|
| Above 1150px | Three columns: sidebar, page, "On this page" |
| 1150px | The "On this page" column hides and an inline list appears at the top of the article; two columns |
| 1000px | The top bar's status line hides (a demo part) |
| 900px | One column. The sidebar becomes a drawer, `min(320px, 86vw)` wide, that slides in from the left over a scrim when the menu button is pressed; the menu and close buttons appear |
| 640px | The top bar's right-hand group hides; search becomes a 40px icon button; headings and code shrink (see Typography); cards and the pager stack into one column; the search dialog goes full width |
| 400px | The logo's tag hides; step numbers shrink to 26px |

### Home (wiki-portal)

| Width | What changes |
|---|---|
| 1280px | The search box narrows to 200px |
| 1200px | Section tiles drop to 3 columns |
| 1080px | Split sections stack; the right rail goes to 2 columns |
| 900px | Feature, welcome and banner blocks go to 1 column; the skill grid goes to 2 |
| 760px | The 168px rail becomes a 240px drawer; the top bar stacks and search goes full width; the masthead grows to 190px; tiles go to 2 columns |
| 520px | Tiles and the skill grid go to 1 column; the welcome heading shrinks to 2xl |

Inner pages switch to a drawer at 900px and the home page at 760px. Whether the home page keeps its own rail or uses the site's sidebar isn't decided; settle the difference when the home page is built. **Settled (P2):** Home uses the site's sidebar and the inner pages' breakpoints; the wiki-portal table above is kept for reference. site.css adds its own rules at 900px (the azqato.com bar folds into the menu; larger tap targets) and 640px (phone layouts).

### Print

documentation-site hides the top bar, sidebar, "On this page", the feedback form, the pager, copy buttons and heading anchors, and prints code black on white.

## Component patterns

### Page structure

documentation-site's page, as read: a skip-free run of landmarks, in this order.

1. `nav.sr-bar`: Template Interface's "Back to Template Interface" bar. It comes out (Removed template parts).
2. `header.pp-top`: the top bar.
3. `nav.pp-sidebar`, labeled "Documentation": the sidebar.
4. `main.pp-main`: the page, with labeled breadcrumbs ("Breadcrumb") at the top and labeled previous/next links ("Previous and next page") at the bottom.
5. `aside.pp-toc`: "On this page".
6. `footer.pp-footer`.

The template keeps its demo pages in one file and switches between them by URL hash; this site gives every page its own file (Design details).

### Top bar

- **In the template:** a menu button (narrow screens only), the "Parcelpoint" logo with a "Docs" tag, a search button, and on the right the status line, the "API v3.4" version label and a "Get API keys" button.
- **On this site:** the logo becomes 💰 Azqato Invests (D11); the search button stays and searches every page; the ☀️/🌙 button is added (D10); the status line, version label and API keys button come out. If D9 stays, azqato.com's nav sits above the top bar.

### Sidebar

**Built 2026-10-02 (P2):** labeled "Site sections"; Home first, then the five groups, with the six leveraged strategies indented under Leveraged strategies; a card at the foot says "Educational use only. Not financial advice.", carried from the source sidebars.


The five sections, Learn, Tools, Strategies, Resources and FAQ, as groups (D12). The current page is marked with the pale accent background, deep accent text, weight 600 and an accent edge. Composer Atlas, Net Worth Tracker and Automate Fundamentals never appear here (D18). At 900px and below the sidebar becomes a drawer. Its label, "Documentation" in the template, needs a name that fits this site (not decided).

### Breadcrumbs and pager

Breadcrumbs show where the page sits (for example Strategies, then Leveraged strategies, then 3 Sig). The pager links to the previous and next pages; planned to follow the sidebar's order.

### Article content

- A lede under the h1, then h2 and h3 sections. Headings carry anchors.
- **Numbered steps** for the Finviz and Seeking Alpha setup guides (D8 borrows help-center's step-by-step guides for these).
- **Callouts:** a note style (emerald) and a warning style (amber), each with an icon column.
- **Tables:** in a bordered, scrollable wrapper, with a tinted header row.
- **Cards:** a three-column grid that stacks below 640px, with a border and shadow on hover.
- The template's strategy-friendly structure suits the write-ups (Overview, Rules and Logic, Performance Notes, Risks and Caveats, Resources: see Template ratings). Each page keeps its source's own sections and wording (core rule).

### "On this page"

The right-hand column on reading pages, marking the section in view. At 1150px and below it becomes an inline list at the top of the article. Tool pages drop it so the screener's table gets the full width (Design details); they also need the 760px article cap lifted.

### Search

The search button opens a dialog, also opened with / or Ctrl+K. Results show a title, a breadcrumb and a snippet, with matches highlighted. Here it searches all 21 pages. How the template builds its search index wasn't read (its script.js); decide how this site builds one when the shell is built.

### Buttons

documentation-site's `.pp-btn`: 0.9rem, weight 600, 6px corners; the solid style is emerald with white text and turns deep emerald on hover. The shared `.button` is 40px tall in primary (accent fill, `#0d1117` text), secondary (accent outline) and ghost styles.

### Footer

**Built 2026-10-02 (P2), a default for the author to change:** the brand, "Educational use only. Not financial advice. Some links are referral links.", links to Resources and the FAQ, and "Built by Azqato". Each moved page also keeps its source's own footer text at the end of the article.


The template's footer has a brand line and links on the rail background. This site's footer content isn't decided.

**Updated 2026-10-02 (v0.16.0):** one footer per page. The source footers that repeat it are hidden (kept in the page); the VIX pages' disclaimer and copyright lines sit in the site footer as notes.

### Removed template parts

The demo-only parts named in Design details come out: the API keys button, API status line, code-language tabs and the page-feedback form. The audit found two more parts that look demo-only, which come out too (Question 10, confirmed 2026-10-01):

- the top bar's "API v3.4" version label;
- the "Back to Template Interface" return bar, added to every template page on 2026-10-01, which links back to the template gallery.

The template's own text must not survive anywhere: before finishing a page, search it for "Parcelpoint", "API" and the template's title, "Introduction - Parcelpoint Docs".

### Home page (wiki-portal layout)

**Superseded 2026-10-02 (v0.16.0, UI review):** Home is one grid of 10 project cards in the source's card style (no separate section tiles), up to 1400px wide like every page, on the inner pages' breakpoints; the wiki-portal breakpoints under Breakpoints don't apply to it. The text below is kept as it was.

**Built 2026-10-02 (P2, P3):** Home uses the inner pages' shell (top bar, sidebar, drawer at 900px) with no "On this page" and content up to 1120px, wiki-portal's width. Its body follows wiki-portal's directory idea: the intro, tiles into the five sections, then the project cards. wiki-portal's violet palette, masthead art, rail and statistics list aren't used; the live VIX statistic is left for later.


From the plan: the intro and "Join the Discord" button from invests.html, tiles into each section, and all 7 project cards with their text (D14, D18). From wiki-portal's rating: portal tiles for the sections, the statistics list for live numbers like the VIX, update panels for what's new, and dense panels for the curated links, with the masthead artwork and talk-page tab toned down for a finance site.

### Borrowed parts

D8 borrows help-center's searchable FAQ and step-by-step guides, admin-dashboard's summary tiles and table styling (for the tools), and blog-article's reading-progress bar (for long pages). These templates were rated in planning but their code wasn't read in this audit. Record each part's markup, tokens and behavior here when it's borrowed.

### Theme button

**Built 2026-10-02 (P2):** assets/js/theme.js. It starts in the visitor's system theme, saves the choice in the visitor's browser, sets the theme in the head before the page draws, and shows the theme it switches to: ☀️ while dark, 🌙 while light, which is Template Interface's convention. Its accessible name says the action ("Switch to light theme").

- ☀️/🌙 in the top bar (D10).
- The site starts in the visitor's system theme and switches when the button is pressed; the choice is saved in the visitor's own browser (PRD Assumptions).
- Planned by the 2026-10-01 audit: apply the saved theme with a small script in the page head, before the page is drawn, so it never flashes the wrong theme first.
- Not decided: whether the button shows the current theme's emoji or the one it switches to.
- It needs an accessible name that says what it does, such as "Switch to dark theme", because an emoji alone isn't a clear name.

### Icons

- **Favicon:** 💰 (D11), as an inline SVG data URI, the technique azqato.com uses for its 🦁 (Design details); invests.html's own favicon is a `data:image/svg+xml` with a 100 by 100 viewBox. The template's favicon.png doesn't come over.
- **Interface icons:** Template Interface's rules: inline SVG on a 24 by 24 viewBox, 2px stroke, round caps. Its reference is assets/svg/icon-reference.md in that repo.

## Accessibility standards

- **Level:** WCAG AA, the level Template Interface targets on every page and template. Assumed to mean WCAG 2.2 (Question 11).
- **Contrast:** 4.5:1 for body text; 3:1 for large text (1.5rem and up, or bold at 1.25rem and up); 3:1 for focus rings and for the edges of controls against what's behind them.

**Measured pairings.** Computed on 2026-10-01 with the WCAG formula, from the token values. All the text pairings pass AA except white on the dark accent, which the dark theme must not use.

| Theme | Pairing | Ratio |
|---|---|---|
| Light | Body text `#2b3833` on `#ffffff` | 12.24:1 |
| Light | Headings `#13201b` on `#ffffff` | 16.80:1 |
| Light | Secondary text `#55625c` on `#ffffff` | 6.39:1 |
| Light | Secondary text `#55625c` on the sidebar `#f4f6f7` | 5.89:1 |
| Light | Links `#0b7a52` on `#ffffff` (also the focus ring) | 5.36:1 |
| Light | White on solid buttons `#0b7a52` | 5.36:1 |
| Light | Current sidebar link `#075c3d` on `#e2f3eb` | 7.00:1 |
| Light | Warning callout text `#a35d00` on `#fff6e1` | 4.73:1 |
| Light | Code text `#e3ede8` on `#0d1714` | 15.26:1 |
| Dark | Body text `#e6edf3` on `#0d1117` | 16.02:1 |
| Dark | Secondary text `#8b949e` on `#0d1117` | 6.15:1 |
| Dark | Secondary text `#8b949e` on surface `#161b22` | 5.62:1 |
| Dark | Tertiary text `#7c8487` on surface `#161b22` | 4.54:1 |
| Dark | Links `#00d4a0` on `#0d1117` (also the focus ring) | 9.85:1 |
| Dark | Accent `#00d4a0` on the active item `#0d3d31` | 6.32:1 |
| Dark | `#0d1117` on the primary button `#00d4a0` | 9.85:1 |
| Dark | White on `#00d4a0` | 1.92:1, fails |
| Dark | Warning `#d29922` and danger `#f85149` on `#0d1117` | 7.50:1 and 5.65:1 |

Input borders measure 1.63:1 in light (`#c3ccd1` on white) and 1.55:1 in dark (`#30363d` on `#0d1117`). WCAG asks for 3:1 where a border is the only thing showing where a field is. Check each form control when the tools move.

- **Keyboard and focus:** everything works from the keyboard, in the same order it appears on screen. Focus shows as a ring: documentation-site's is 3px solid emerald with a 2px gap, and base.css's is 2px solid accent with a 2px gap, both on `:focus-visible`. Search opens with / or Ctrl+K. The menu button reports whether the drawer is open (`aria-expanded`) and which element it controls. How focus moves into and out of the drawer and the search dialog wasn't read; check both when the shell is built. **Checked 2026-10-02 (P7.5):** opening the drawer moves focus to its close button and Escape returns it to the menu button; `/` focuses the search box and Escape returns focus to where it was.
- **Landmarks:** header, navigation (the sidebar, breadcrumbs and pager each labeled), main, aside and footer.
- **Skip link:** none. Template Interface shipped one until its v0.6.0, then removed it in v0.6.2 at its maintainer's request, a known exception to WCAG 2.4.1 (Bypass Blocks). Keyboard users have to tab past the top bar and sidebar (and azqato.com's nav, if D9 stays) to reach the content. **Decided 2026-10-01 (Question 8):** this site adds a "Skip to content" link, hidden until focused, closing the gap. The leverage source pages already have one.
- **Icons:** decorative SVGs are hidden from screen readers (`aria-hidden`); meaningful ones get a title or label. The ☀️/🌙 button needs an accessible name (Theme button).
- **Data:** tables keep real header cells. The VIX pages draw charts with Chart.js; read 2026-10-01 (P1): each donut chart's canvas has an `aria-label` describing the chart (for example "Donut chart showing current ETF allocation percentages"). Check when they move that the percentages are also readable as text.
- **Motion:** reduced motion is respected (Animation and motion).

## Animation and motion

- **Shared timing (theme.css):** fast 100ms, base 150ms and slow 250ms, all eased. Under `prefers-reduced-motion: reduce`, all three become 0ms, which switches off every shared transition at once.
- **documentation-site:** smooth scrolling to anchors; the drawer slides in over 0.2s; cards change border and shadow over 0.15s on hover. Under reduced motion, scrolling jumps and the drawer and cards don't animate.
- **Shared components:** cards lift 2px with a larger shadow on hover. A fade-in-up effect (12px rise, slow timing) is applied by Template Interface's motion-utils.js; its reduced-motion handling comes from the theme timings.
- **wiki-portal:** a pulse animation, off under reduced motion; its drawer uses the slow timing.
- **Added by the 2026-10-01 audit:** live numbers, such as the VIX reading and market data, change without animation, so a value is never shown partway through a transition.

## Page layouts

**Width (UI review, option C, 2026-10-02):** content runs from the sidebar to the 1400px limit on every page, prose included; the sources' own caps (stocks 820px, VIX 1100px) are lifted. A page whose "On this page" list is empty gives that column back. Card grids add columns as space allows (Market Overview 200px minimum, Home 200px, Resources masonry columns of 260px). On phones (640px and below) the VIX tables become stacked cards, and the sidebar holds the azqato.com links (900px and below). Sidebar groups collapse except the one holding the current page. Each page has one footer; the VIX pages' disclaimer lines sit in it.

The site map in the PRD lists every page and its source.

- **Inner pages:** documentation-site's grid of sidebar (260px), page (content capped at 760px) and "On this page" (240px), under a 60px top bar. (Since v0.16.0 the content cap is 1400px; see Width above.)
- **Tool pages:** the same without "On this page", and with the content cap lifted, so the screener's table can use the full width.
- **Home:** wiki-portal's layout: a masthead band, then a narrow rail beside a wide content column (up to 1120px) of tiles and panels. (As built: the inner pages' shell with one card grid; see Home page under Component patterns.)

## Design details

- `documentation-site` keeps its seven demo pages in one HTML file and switches between them by URL hash. This site gets one file per page, so every page has its own address and the redirects in D7 have somewhere to land.
- Tool pages drop the "On this page" column so the screener's table gets the full width.
- The template's demo-only parts come out: the API keys button, API status line, code-language tabs and the page-feedback form, which needs a server. They belong to the template, not the sources, so the core rule doesn't cover them.
- None of the 21 templates has a dark mode, so the dark theme is built on top of the template's shared color tokens.
- If D9 stays: azqato.com is dark-only today (background `#0d1117`, accent `#00d4a0`), so its nav needs a light version for this site's light mode. azqato.com's pages get the nav from `tools/build-nav.py`, which only reaches pages in the azqato.github.io repo, so this site would carry its own copy of the nav, with links pointing back to azqato.com.
- The 💰 favicon uses the same inline-SVG emoji technique azqato.com uses for its 🦁.

## Template ratings

**Chosen (D8): `documentation-site` for every inner page, with `wiki-portal`'s directory layout for the home page.** Both use Template Interface's shared stylesheets, which makes them easier to combine, and `help-center` and `admin-dashboard` have patterns worth borrowing for the FAQ and the tools.

Each template is rated from 1.0 to 10.0 on how well it fits this plan: 15 reading pages (methodology, setup guides, strategy write-ups, FAQ), 4 data tools (screener, Market Overview, VIX dashboard and custom builder), a hub home page with curated links, and a free, no-signup tone.

**documentation-site (9.0).** Its sidebar groups, breadcrumbs, previous/next pager, "On this page" list and search across every page are exactly what 15 reading pages across Learn, Strategies and the FAQ need, and its fixed page structure matches the strategy write-ups (Overview, Rules and Logic, Performance Notes, Risks and Caveats, Resources). It misses a 10 only because it has no hub-style home page or data-tool patterns, and its API-specific parts (the API keys button, status line, code-language tabs and a feedback form that needs a server) have to come out.

**wiki-portal (7.5).** It is built for this site's home page job, a directory into many pages, and its blocks map cleanly: portal tiles for the sections, the statistics list for live numbers like the VIX, update panels for what's new, and dense panels for the curated links. It only builds the home page, though, and its game-wiki touches (masthead artwork, a talk-page tab) would need toning down for a finance site.

**help-center (6.5).** Its search-as-you-type, topic cards and library of numbered-step articles suit the FAQ, the largest page being merged, and the Finviz and Seeking Alpha setup guides. It is a single support page with no place for the tools or the strategies, and its chat, phone and contact form would all have to go.

**blog-article (6.0).** Its article page reads well for long methodology pages like Philosophy and Metrics, with a reading-progress bar and a contents list that marks where you are. But it is framed as a journal of dated essays with a subscribe form, and it has neither sidebar navigation for a 20-page reference nor any pattern for the tools.

**admin-dashboard (5.5).** Its KPI tiles, chart and searchable, sortable, filterable table are the library's closest match for the screener, Market Overview and VIX dashboard. It is built for an internal team where density beats explanation, so the 15 reading pages for beginner-to-intermediate investors would feel like a control panel.

**course-landing (4.0).** Its sections answer a learner's questions in order (is this for me, what will I learn), which could present the Learn pages as a free course. But the page exists to sell a paid cohort and ends in an application form with payment plans, which works against a free, no-signup site.

**ecommerce-storefront (3.5).** Filtering on several criteria, searching, sorting and opening a quick view is the same narrow-and-compare loop the screener runs, and its card grid could suit Market Overview. Everything else is shopping (bag drawer, size guide, delivery), and the screener needs a dense table rather than product cards.

**portfolio-site (3.5).** The current invests.html already works like a portfolio of projects, and the case-study format (problem, approach, measurable result) could frame a strategy's results. But it is a single scrolling page about one person's work for hire, not a multi-section reference.

**pricing-page (3.0).** Its side-by-side tier cards and full comparison table could compare 3 Sig, 6 Sig and 9 Sig, and its live calculator echoes how the VIX dashboard turns one reading into an allocation. Everything else is built to sell a subscription, and this site sells nothing.

**real-estate-listing (3.0).** Its filter, sort and open-a-detail-view flow echoes the screener's click-for-breakdown popup, and the calculator inside that view echoes the VIX custom builder. The synced map is a large part of the template and has no use here, and listings and viewing requests have no counterpart.

**community-forum (2.5).** Category navigation, search and a side column with house rules could organize content, and you do run a Discord community. But threads, replies and posting need accounts and a server, which this site doesn't have, and the Discord already does that job.

**landing-page (2.5).** Its hero with one clear action could carry the home page's "Join the Discord" button. Its own README says a site people browse needs a multi-page template, and this one is a pitch for a single product's free trial.

**careers-page (2.0).** A filterable list whose items open in place could hold the six leveraged strategies. The rest (values, benefits, hiring process, application form) is recruiting copy with nothing to map onto.

**nonprofit-site (2.0).** Its show-the-numbers-before-the-ask approach suits a site that puts risk warnings next to every strategy. But the whole page builds toward a donation form, which this site doesn't need.

**ecommerce-product (1.5).** Option pickers that redraw a preview loosely resemble the VIX custom builder swapping tickers. Otherwise it sells one physical product through a cart, which has no counterpart here.

**event-site (1.5).** It promotes one dated event on one page, answering when, who and how much. Only its stats strip might carry over.

**onboarding-flow (1.5).** It is a stepped signup for an app with accounts, and this site has none. Its step-by-step form would only matter if the site gained something like a strategy-picker quiz, which isn't in the plan.

**small-business (1.5).** It answers a local customer's "can you come, when, and what will it cost" and then takes a booking. Beyond a services grid, nothing maps onto an investing reference.

**waitlist-signup (1.5).** The whole page has one job, collecting an email address, and this site has no newsletter or launch list. It would only matter if you later wanted an Azqato Invests mailing list.

**restaurant-site (1.0).** It answers opening hours, menu, directions and table bookings for someone on a phone. None of that has a counterpart on an investing site.

**resume-site (1.0).** It is one person's printable CV on a single sheet. Neither its content nor its one-sheet layout fits a 20-page reference site.

### Summary

| Template | Rating | Role on this site |
|---|---|---|
| documentation-site | 9.0 | Base for every inner page |
| wiki-portal | 7.5 | Home page layout |
| help-center | 6.5 | Borrow: searchable FAQ, step-by-step guides |
| blog-article | 6.0 | Borrow: reading-progress bar for long pages |
| admin-dashboard | 5.5 | Borrow: summary tiles and table styling for the tools |
| course-landing | 4.0 | Skip |
| ecommerce-storefront | 3.5 | Skip |
| portfolio-site | 3.5 | Skip |
| pricing-page | 3.0 | Skip |
| real-estate-listing | 3.0 | Skip |
| community-forum | 2.5 | Skip |
| landing-page | 2.5 | Skip |
| careers-page | 2.0 | Skip |
| nonprofit-site | 2.0 | Skip |
| ecommerce-product | 1.5 | Skip |
| event-site | 1.5 | Skip |
| onboarding-flow | 1.5 | Skip |
| small-business | 1.5 | Skip |
| waitlist-signup | 1.5 | Skip |
| restaurant-site | 1.0 | Skip |
| resume-site | 1.0 | Skip |

## Notes for contributors and AI models

- Read the PRD's core rule and Decisions before changing anything here. The design serves the content: when a layout can't hold some source content, the layout changes.
- Copy template files from Template Interface at a recorded commit and note the commit in PATCHNOTES.md.
- Never redefine a theme.css token. Give this site's values to its own tokens.
- Build each part in both themes, and measure the contrast of every new pairing in both.
- The literal colors in documentation-site's stylesheet need dark counterparts; they're listed under the light palette.
- No template demo text may survive: search for "Parcelpoint" and "API" before finishing a page.
- No web fonts; keep the system stacks.
- When the design is built, check this document against the code and mark each section on the PRD's verification checklist.
