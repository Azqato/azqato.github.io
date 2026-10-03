# Design Document: Azqato Portfolio

This document describes how the site looks and the rules for keeping it consistent. It is written against the source as it exists today. Where a documented rule and the code disagree, both are recorded and the disagreement is marked as a discrepancy for the author to resolve, rather than one being silently overwritten by the other.

---

## Design Philosophy

The portfolio uses a GitHub Dark-inspired aesthetic to signal developer credibility without requiring any explanation. The visual language is intentional: if it looks at home on github.com, it belongs here. Motion is used only to confirm interactivity, never for decoration. Every element defaults to the minimum necessary complexity.

The accent color is a teal-green (`#00d4a0`) that replaces the default GitHub blue and is used consistently across all primary interactive elements: links, active nav states, CTA buttons, card hover borders, and tag highlights.

One page deliberately breaks this philosophy. `music.html` is a full-screen concert-stage visualizer rendered on a canvas behind the page content, with lasers, haze, fire columns, a crowd, and a DJ booth. It is loud on purpose: the page is about DJ mixes, and the rest of the site stays quiet so this page can be the exception. Every other page follows the rules above without exception.

---

## Where the CSS Lives

Since `v2.7.0` the site has two layers of styling:

| Layer | File | Contents |
|-------|------|----------|
| Shared | `styles.css` (linked by all 12 pages) | The 12 common design tokens on `:root`, the universal reset, the `html { overflow-y: scroll }` scrollbar-gutter fix, `body` typography, the entire nav component, the nav's 860 px collapse breakpoint, and `footer` |
| Page-specific | inline `<style>` in each `.html` file | Extra `:root` tokens for that page, hero, sections, grids, cards, and that page's own responsive rules |

There is no CSS build step, no preprocessor, and no minification. `styles.css` is 2,887 bytes and is the only external stylesheet on any page.

A page that needs an extra token (for example `--discord`, `--spotify`, `--coffee`) declares its own small additional `:root` block in that page's inline `<style>` tag. CSS custom properties cascade additively across multiple `:root` rules, so this adds tokens without overriding the shared ones.

---

## Color Palette

### Shared tokens (defined once in `styles.css`)

| Token             | Hex Value   | Intended Use                                                          |
|-------------------|-------------|-----------------------------------------------------------------------|
| `--bg`            | `#0d1117`   | Page background                                                       |
| `--surface`       | `#161b22`   | Card background, nav bar, pitch card                                  |
| `--border`        | `#30363d`   | All borders and dividers                                              |
| `--accent`        | `#00d4a0`   | Primary interactive color: links, active states, hover borders        |
| `--accent-hover`  | `#00e6b0`   | Hover state for accent-colored elements                               |
| `--green`         | `#3fb950`   | Status badge dot, success indicators                                  |
| `--purple`        | `#bc8cff`   | Secondary accent (role badge on About page, gradient pair, music.html chrome) |
| `--orange`        | `#ffa657`   | Tertiary accent, used sparingly                                       |
| `--text`          | `#e6edf3`   | Primary body text                                                     |
| `--text-muted`    | `#8b949e`   | Secondary text: descriptions, labels, captions, nav links             |
| `--card-hover`    | `#1c2128`   | Card background on hover                                              |
| `--tag-bg`        | `#21262d`   | Tag pill background                                                   |

### One palette for the whole site (decided 2026-10-02)

The owner picked these on 2026-10-02 (PRD Part 2, P15; Roadmap at a glance, item 4), one color per role, from a side-by-side comparison of azqato.com's and Invests' colors. They become the tokens for both halves of the site when items 5 to 8 are built; until then the tables above and Azqato Invests Visual System describe what is live. Contrast is measured against the page background with the WCAG formula.

**Live 2026-10-02 (2.13.7, build pass item 5).** styles.css carries these as tokens: dark on `:root`, light on `:root[data-theme="light"]` and, for visitors without scripts, under `prefers-color-scheme: light`. New tokens: `--on-accent` (text on an accent fill), `--amber`, `--red`, `--blue`, `--nav-bg`, `--nav-menu-bg`. Changes from the table, made after the contrast audit: light `--green` `#116329` (`#1a7f37` was 4.36:1); dark `--border` `#3a4a43` and `--text-muted` `#9fb1a8`. Invests maps documentation-site's `--pp-*` tokens to these in invests/assets/css/site.css. One shared script, `/theme.js`, sets the theme before the first paint for every page (Theme button). music.html stays dark and has no button (`data-theme-lock="dark"`): the owner's "the visualizer stays dark". Known before this pass and unchanged: the Projects page's dark C# and HTML tags measure 3.42 and 4.09:1 (owner review).

| Role | Dark | Source | Light | Source |
|---|---|---|---|---|
| Page background | `#0d1117` | azqato.com | `#f6f8fa` | New (GitHub-style) |
| Cards, top bar, sidebar | `#161b22` | azqato.com | `#f6f8fa` | New (GitHub-style); same as the background, so panels are set off by their borders |
| Hover on cards and rows | `#1c2128` | azqato.com | `#eaeef2` | New (GitHub-style) |
| Borders and dividers | `#3a4a43` | Invests | `#d0d7de` | New (GitHub-style) |
| Main text and headings | `#e6edf3` | azqato.com | `#1f2328` (14.8:1) | New |
| Secondary text | `#9fb1a8` | Invests | `#59636e` (5.7:1) | New |
| Accent: links, active page, buttons | `#00d4a0` | azqato.com | `#007a5e` (5.0:1) | New, a deeper azqato.com mint |
| Warnings and risk notices | `#f0b45a` | Invests | `#9a6700` (4.6:1) | New (GitHub-style) |
| Losses and errors | `#f85149` | New (GitHub-style) | `#cf222e` (5.0:1) | New (GitHub-style) |
| Information notes | `#58a6ff` | New (GitHub-style) | `#0969da` (4.9:1) | New (GitHub-style) |
| Second accent | `#bc8cff` | azqato.com | `#8250df` (4.7:1) | New (GitHub-style) |

Every text color passes AA (4.5:1) on its background in both themes. On the light hover color, warning, info and second-accent text fall to 4.2 to 4.45:1, so colored text inside a hovered row needs a check when it's built.

### Page-scoped tokens (declared inline on the pages that need them)

| Token             | Hex Value   | Declared on                                          | Use                                        |
|-------------------|-------------|------------------------------------------------------|--------------------------------------------|
| `--coffee`        | `#FFDD00`   | `support.html`                                       | Buy Me a Coffee button background          |
| `--coffee-hover`  | `#FFE84D`   | `support.html`                                       | Buy Me a Coffee button hover background    |
| `--discord`       | `#5865f2`   | `index.html`, `discord.html`, `invests.html`         | Discord button background                  |
| `--discord-hover` | `#4752c4` on `discord.html`; `#6b76f5` on `index.html` and `invests.html` | same three pages | Discord button hover background |
| `--spotify`       | `#1db954`   | `music.html`                                         | Declared but not referenced by any rule in the current `music.html`. Left in place; harmless. Discrepancy: the token survives from the era when the page listed Spotify playlists. |

`--discord-hover` having two different values is a real inconsistency in the source, not a documentation error. It is recorded here rather than corrected, since which value is intended is the author's call.

### Colors written inline rather than tokenized

Several brand and accent colors are written as literal `rgba()` values in inline `style` attributes rather than as tokens. This is the dominant pattern for one-off brand colors and is not treated as a defect:

- Affiliate logo tiles on `support.html`: Tesla `rgba(204,17,17,...)`, Twitch `rgba(145,70,255,...)`, RouteNote `rgba(255,107,0,...)`, Robinhood `rgba(0,200,5,...)`, M1 Finance `rgba(27,63,106,...)`, Public `rgba(61,82,213,...)`, Lyft `rgba(255,0,191,...)`.
- The entire `music.html` visualizer palette, which is computed per frame in JavaScript and in GLSL shader source rather than declared in CSS.

### Language Tag Colors

Language tags use inline color values rather than CSS custom properties:

| Class        | Language   | Color     |
|--------------|------------|-----------|
| `lang-js`    | JavaScript | `#e8c840` |
| `lang-ts`    | TypeScript | `#3178c6` |
| `lang-py`    | Python     | `#3572a5` |
| `lang-cs`    | C#         | `#178600` |
| `lang-html`  | HTML       | `#e34c26` |
| `lang-css`   | CSS        | `#563d7c` |
| `lang-go`    | Go         | `#00add8` |
| `lang-rust`  | Rust       | `#dea584` |
| `lang-java`  | Java       | `#b07219` |

In use by the `PROJECTS` array: `lang-js` on eight entries, `lang-html` on six, and `lang-cs` on one (Automate Fundamentals, added in v2.9.8). The rest are defined ahead of need.

---

## Typography

The site uses the system font stack with no external font loading:

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
```

There is no monospace face anywhere on the site. The "code-adjacent" feel comes from color and density, not from a typeface.

| Role              | Size                        | Weight | Color          | Notes                                |
|-------------------|-----------------------------|--------|----------------|--------------------------------------|
| Page heading (h1) | `clamp(2rem, 5vw, 3.5rem)`  | `800`  | `--text`       | Hero headline; fluid between viewports |
| Section heading (h2) | `1.4rem`                 | `700`  | `--text`       | Section titles with left accent bar  |
| Sub-heading (h3)  | `1rem`-`1.15rem`            | `700`  | `--text`       | Card names, pitch identity, resource card headers |
| Card title        | `1rem`                      | `700`  | `--text`       | Links to demo or GitHub; hover: `--accent` |
| Body text         | `1rem`                      | `400`  | `--text`       | Paragraphs                           |
| Lead paragraph    | `1.1rem`                    | `400`  | `--text-muted` | Hero description under the h1        |
| Card description  | `0.78rem`-`0.85rem`         | `400`  | `--text-muted` | Card body copy                       |
| Muted / caption   | `0.78rem`-`0.82rem`         | `400`  | `--text-muted` | Tags, labels, meta info, section meta |
| Nav links         | `0.9rem`                    | `400`  | `--text-muted` | Active state: `--accent`, weight `600` |
| Button text       | `0.9rem`                    | `600`  | contextual     | Varies by button type                |
| Tag pills         | `0.72rem`                   | `600`  | language color | Language and category tag pills      |
| Footer            | `0.8rem`                    | `400`  | `--text-muted` | Single line, centered                |

Line height: `1.6` for body text (set on `body`), `1.15` for hero headings, `1.55`-`1.8` for card and pitch copy.

Letter spacing: `-0.5px` on hero headings, `0.5px` on the nav logo, `0.2px` on the Buy Me a Coffee button. Everything else uses the default.

---

## Spacing System

There is no numeric spacing scale (no 4 px or 8 px base unit) and no spacing tokens. Values are written directly in `rem` at each use site, drawn from a small set of conventional values. Recording that absence is deliberate: a contributor looking for a scale will not find one, and should match the table below instead of inventing one.

| Use case                       | Value              |
|--------------------------------|--------------------|
| Hero padding (top)             | `5rem` (desktop), `3rem` (mobile) |
| Hero horizontal padding        | `2rem` (desktop), `1.25rem` (mobile) |
| Section padding (vertical)     | `2rem`-`3rem`, page-dependent |
| Card padding                   | `1.25rem`-`2.5rem` |
| Card gap in grid               | `1rem`-`1.25rem`   |
| Nav height                     | `60px`             |
| Nav padding                    | `0 2rem`           |
| Inline element gap (small)     | `0.35rem`-`0.5rem` |
| Inline element gap (medium)    | `0.75rem`          |
| Inline element gap (large)     | `1rem`             |
| Tag / badge padding            | `0.18rem 0.6rem`-`0.25rem 0.75rem` |
| Border radius (cards)          | `10px`-`12px`      |
| Border radius (large panels)   | `16px`             |
| Border radius (tags / badges)  | `999px`            |
| Border radius (buttons)        | `6px`-`10px`       |
| Footer padding                 | `2rem`             |

Max content width: `1100px`, centered with `margin: 0 auto` on `.nav-inner`, `.hero`, `.section`, and `.cta-section`.

---

## Breakpoints

The site has two real breakpoints, and they are at different widths for different concerns. This is the most commonly misremembered fact in the design system, so it is stated explicitly:

| Breakpoint | Width | What changes |
|------------|-------|--------------|
| Nav collapse | `max-width: 860px` (in `styles.css`) | `.nav-toggle` hamburger becomes visible; `.nav-links` switches to a hidden absolutely-positioned dropdown panel below the bar, opened by adding `.open`. Links become full-width block rows with `0.6rem` vertical padding. |
| Content reflow | `max-width: 600px` (in each page's inline `<style>`) | Hero, section, and CTA horizontal padding drops from `2rem` to `1.25rem`; vertical padding tightens; some grid `minmax` floors drop (for example the affiliate grid goes from `200px` to `160px`). |

Between 601 px and 860 px the page keeps its desktop padding but the nav is already collapsed. That gap is intentional in effect but was never a stated decision; treat it as observed behavior.

Grids are otherwise fluid rather than breakpoint-driven. They use `repeat(auto-fill, minmax(Npx, 1fr))` and reflow continuously:

| Grid | `minmax` floor |
|------|----------------|
| Explore cards (`index.html`) | `260px` |
| Project cards (`projects.html`) | `280px` |
| Featured project cards (`invests.html`, `codes.html`) | `300px` |
| Discord server cards | `280px` |
| Affiliate cards (`support.html`) | `200px`, `160px` under 600 px |

> **Discrepancy (open).** Earlier versions of this document stated the mobile breakpoint as "`< 600px`: nav links hidden (logo only visible)". That describes the pre-`v2.6.x` nav, which had no hamburger. The current source collapses the nav at 860 px into a toggle-driven dropdown. The 860 px figure above is what the code does; `docs/PRD.md` feature F3 already agrees with the code. The old 600 px nav claim is recorded here only so a reader who saw it knows it was superseded, not lost.

---

## Component Patterns

### Navigation Bar

- Background: `rgba(13, 17, 23, 0.85)` with `backdrop-filter: blur(12px)`
- Border: `1px solid --border` (bottom)
- Sticky: `position: sticky; top: 0; z-index: 100`
- Height: `60px`; inner max width `1100px`
- Logo: `--text`, `1.15rem`, `700` weight, accent-colored trailing period; always links to `index.html`
- Nav links: `--text-muted`; hover: `--text`; active: `--accent`, `600` weight
- Collapses at 860 px behind `.nav-toggle` (a `☰` button carrying `aria-label` and `aria-expanded`)
- **No external links in the top-level nav.** Every item in `.nav-links` must resolve to a page on azqato.github.io (or a relative link on the current page). Links to other properties (GitHub, sibling project sites not hosted in this repo) belong on the page itself (a card, a footer credit, a button) rather than in the persistent top-level nav.
- Current nav order, identical in all 12 pages: **Home, About, Discord, Invests, Codes, Music, Links, Projects, YouTube, Support** (10 items).
- `accounts.html` and `privacy-policy.html` carry the same nav but are not themselves in it. They are reached from `index.html`'s explore grid and from `links.html`.
- **The nav markup is generated. Do not hand-edit it.** As of v2.8.8 the block between `<!-- NAV -->` and `</nav>` in every page is stamped by `tools/build-nav.py`. To change the nav, edit the `PAGES` list in that script and run it, then update this section and F3 in PRD.md. A hand edit inside a page survives only until the next run. The active state is applied by the script from each file's own name, so `class="active"` is no longer maintained by hand either.

### Footer

- `border-top: 1px solid --border`, `padding: 2rem`, centered, `0.8rem`, `--text-muted`
- Content is one line on every page: `Built by <a href="https://azqato.com/">Azqato</a>.`
- `music.html` is the exception: its footer is nested inside `.mode-controls`, has a transparent background, and wraps its text in a blurred dark pill so it stays readable over the visualizer.

**Replaced in 2.13.0 (build pass, item 6).** The footer is now `.site-footer`, stamped into all 12 pages by `tools/build-nav.py` between `<!-- FOOTER -->` and `</footer>`, styled after the Azqato Invests footer:
- A `--surface` panel with a `--border` top line, `0.875rem`, `--text-muted`; inner width `1100px` like the nav.
- The `Azqato.` brand, then a `<nav aria-label="Footer">` with two rows of plain links: every site page (the ten nav pages plus Gaming Accounts and Privacy Policy) and Azqato Invests' five sections. The current page's link is marked `aria-current="page"` and shown in `--accent`.
- `© 2026 Azqato` on its own line. The financial-advice line stays on Invests' own footer.
- Links are at least 24px tall for tapping. `.site-footer-nav` resets the top bar's `nav` rule, which matches every `<nav>`.
- `music.html` uses `.site-footer--stage`: the same block, compact and translucent inside the stage console, without the Invests row so the console stays short.

### Hero Section

- Max width: `1100px`, centered; flex column with `1rem` gap
- Desktop padding: `5rem 2rem 3rem` on most pages (`projects.html` and the discord-style pages trim the bottom)
- Headline: `clamp(2rem, 5vw, 3.5rem)`, `800` weight, `letter-spacing: -0.5px`, with a `.highlight` span in `--accent`
- Description: `1.1rem`, `--text-muted`, `max-width: 560px`-`600px`
- Optional status badge (`.hero-badge`): pill with a pulsing green dot, `--tag-bg` background, `--border` border. Used on `support.html`, `accounts.html`, and `music.html`.
- Optional `.hero-cta` / `.hero-actions` row: flex, wraps, `0.75rem` gap

### Section Title

- Font size: `1.4rem`, weight `700`, flex with `0.5rem` gap
- Left accent bar rendered via `::before`: `3px` wide, `1.2em` tall, `--accent`, `2px` radius

### Section Header (`.section-header`)

The block introducing a page section, used on `discord.html`, `invests.html`, `codes.html`, `youtube.html`, and `projects.html`. Contains a `.section-title` plus either a `.section-desc` or a `.section-meta`.

- `margin-bottom: 1.5rem`; on `invests`/`codes`/`youtube` also `padding-bottom: 1rem` and `border-bottom: 1px solid --border`
- `.section-desc`: `0.95rem`, `--text-muted`, `margin-top: 0.5rem`, `max-width: 620px`
- `.section-meta`: right-aligned count text on `projects.html`, written by JS

### Project Card (`projects.html`)

Built entirely by `buildCard()` in JS from the `PROJECTS` array; never written by hand.

- Background: `--surface`; hover background: `--card-hover`
- Border: `1px solid --border`; hover: `border-color: --accent`
- Border radius: `10px`; padding `1.25rem`; internal gap `0.75rem`
- Top-edge gradient on hover: `linear-gradient(90deg, --accent, --purple)`, `2px` tall, `opacity 0` to `1`
- Hover: `translateY(-2px)` plus `box-shadow: 0 8px 24px rgba(0, 212, 160, 0.08)`
- Card icon is an emoji, or an `<img>` at 22x22 when `iconUrl` is set
- Two icon buttons top-right: live demo (`↗`, only when `demo` is set) and GitHub (inline SVG)
- Hidden cards carry `data-hidden="true"`, toggled by the filter, and are hidden by an attribute selector

### Featured Project Card (`invests.html`, `codes.html`)

(Since v2.11.0 `invests.html` is a redirect page, so this card is on `codes.html` only; Azqato Invests' Home has its own cards, under Azqato Invests Visual System.)

A larger, fully clickable variant written as static HTML. The entire card is an `<a>`.

- Background: `--surface`; border `1px solid --border`; hover `border-color: --accent`
- Border radius: `12px`; padding `1.5rem`; internal gap `0.6rem`
- Top-edge gradient on hover: `linear-gradient(90deg, --accent, --purple)`, `3px`, `opacity 0` to `1`
- Hover: `translateY(-4px)` plus `box-shadow: 0 12px 28px rgba(0, 0, 0, 0.35)`
- Icon: `1.6rem` emoji; each card's icon mirrors that project's own favicon emoji
- Title (`1.05rem`, `700`) with a trailing `→` that slides `translateX(4px)` and turns `--accent` on hover

### Explore Card (`index.html`)

The landing page's destination grid. Same shape as the featured project card, with its own class names.

- `.explore-card`: `--surface`, `1px solid --border`, `12px` radius, `1.4rem` padding, flex column, `0.5rem` gap
- Hover: `--card-hover` background, `--accent` border, `translateY(-3px)`, teal glow, top gradient fades in
- `.explore-icon` `1.6rem` emoji, `.explore-name` `1.05rem`/`700` with a sliding arrow, `.explore-desc` `0.85rem` muted

### Discord Server Card (`discord.html`)

- Same base as project cards but hover uses `--discord` border and shadow tint
- Top-edge gradient: `linear-gradient(90deg, --discord, --purple)`
- Hover box-shadow: `0 8px 24px rgba(88, 101, 242, 0.12)`
- Card padding `1.5rem`; internal gap `1rem`; icon `2rem` emoji at the top left
- Join button: full-width, `--discord` background, white text, inline Discord SVG

### Affiliate Card (`support.html`)

The entire card is an `<a>` to the referral URL. Actual class names, which differ from what older documentation recorded:

| Element | Class | Styling |
|---------|-------|---------|
| Card | `.affiliate-card` | `--surface`, `1px solid --border`, `12px` radius, `1.5rem 1.25rem` padding, centered flex column, `0.65rem` gap |
| Logo tile | `.affiliate-logo` | `72x72`, `18px` radius, `2rem` emoji, brand-tinted `rgba()` background and border written inline |
| Name | `.affiliate-name` | `0.95rem`, `700`, `--text` |
| Promo badge | `.affiliate-promo` | `0.75rem`, `600`, `--green` text on `rgba(63,185,80,0.1)` with a matching border, `999px` radius |
| Description | `.affiliate-desc` | `0.78rem`, `--text-muted`, `line-height 1.55`, `flex: 1` so buttons bottom-align |
| CTA | `.affiliate-link-btn` | full width, `6px` radius, transparent, `--accent` text; on card hover gains an `--accent` border and a faint teal fill |

Hover on the card: `--card-hover` background, `--accent` border, `translateY(-3px)`, teal glow, and the logo tile scales to `1.05`.

> **Discrepancy (resolved in favor of the code).** Earlier documentation described this card as `.logo-area`, `.promo-badge`, `.affiliate-btn` wrapped in a `<div>`. No such classes exist in `support.html`. The table above is read directly from the source. The same stale names still appear in the Affiliate Card data model in `docs/PRD.md`, which has been updated in the same pass.

### Buy Me a Coffee CTA (`support.html`)

- `.cta-inner`: `--surface` panel, `12px` radius, `3rem 2rem` padding, with a `3px` top gradient `linear-gradient(90deg, --coffee, --orange)`
- `.cta-btn`: `--coffee` background, `#1a1a1a` text, `0.9rem 2.5rem` padding, `10px` radius, `800` weight; hover lifts `2px` and adds a yellow glow
- The disclaimer under the button is `0.78rem` italic muted text

### Discord CTA Band (`index.html`)

- `.cta-inner`: `--surface`, `16px` radius, `3rem 2rem`, centered, with a `3px` top gradient `linear-gradient(90deg, --discord, --purple)`
- Contains a `2.75rem` emoji, an `1.7rem`/`800` heading, a `540px` muted paragraph, and the Discord button

### Link Button (`links.html`)

- `.link-btn`: `--surface` pill-ish button in a fluid grid, emoji icon plus label, `--border` border, hover to `--accent`
- Grouped under section titles: Community and Streaming, YouTube, Music, Social, Investing, More

### Platform Card (`accounts.html`)

- `.platform-card`: `--surface` panel with a `.platform-header` (emoji icon plus name) and a `.account-list` of linked account names

### Channel Card (`youtube.html`)

- `.channel-card`: full-card `<a>` containing a `.channel-thumb` image, `.channel-name`, `.channel-sub`, and a `.channel-btn` "Subscribe →"
- The four thumbnails are the only content images on the site besides the About avatar

### Resource Card (`invests.html`)

(Since v2.11.0 `invests.html` is a redirect page, so this card is no longer in use; the links live on in Azqato Invests' Resources page.)

- `.resource-card`: `--surface` panel with an emoji-prefixed `h3` and a `<ul>` of external links
- Sixteen categories: Platforms, Careers, ETFs, Companies, Ratings, Screeners, Real Estate, Charts, Databases, Economic Indicators, Education, Guides, Indices, Information, News, and the disclaimer block above them
- `.disclaimer`: bordered notice with an `&#9432;` glyph, shown above the grid, stating that Azqato is not a licensed financial advisor and that some links are referral links

### Policy Block (`privacy-policy.html`)

- `.policy-block` wrapping repeated `.policy-section` elements, each an `h2` plus prose or a list. No cards, no grid.

### Pitch Card (`about.html`)

- `.pitch-card`: `--surface`, `12px` radius, `2.5rem` padding, with a `3px` top gradient `linear-gradient(90deg, --accent, --purple, --orange)`
- `.pitch-avatar`: `60px` circle holding `img/about-profile.jpg`, `object-fit: cover`
- `.pitch-body`: `0.95rem`, `line-height 1.8`, muted, with `<strong>` promoted to `--text`
- `.pitch-signature`: `--accent`, `700`

### Buttons

| Variant    | Background    | Border         | Text        | Use case                              |
|------------|---------------|----------------|-------------|---------------------------------------|
| Primary    | `--accent`    | `--accent`     | `#0d1117`   | Main CTAs                             |
| Secondary  | transparent   | `--border`     | `--text`    | Secondary actions; hover: `--accent` border |
| Coffee     | `--coffee`    | `--coffee`     | `#1a1a1a`   | Buy Me a Coffee only                  |
| Discord    | `--discord`   | `--discord`    | `#ffffff`   | Discord join and CTA buttons          |
| Icon button | `--surface`  | `--border`     | `--text-muted` | Card action icons (GitHub, ↗)      |
| Join (full-width) | `--discord` | `--discord` | `#ffffff` | Discord server card join button      |
| Viz button | `rgba(22,27,34,0.88)` | `--border` | `--text-muted` | `music.html` mode controls; hover and active use `--purple` |

Most buttons use `border-radius: 6px`, `font-size: 0.9rem`, `font-weight: 600`, `transition: all 0.2s`. The hero and coffee buttons are larger (`8px`-`10px` radius, `0.95rem`-`1.05rem`).

### Tag Pills

- Category tags: `--tag-bg` background, `--border` border, `--text-muted` text, `0.72rem`, `600` weight, `999px` radius
- Language tags: same shape with language-specific background, border, and text colors
- The first tag on a card gets the `langClass` color when one is set
- `.pill` on `index.html` is the same shape at `0.82rem` with `--text` text, used for the interest row

---

## `music.html` Visual System

`music.html` is the only page with a non-trivial rendering layer, and it is large enough (112 KB, roughly 2,660 lines) that its visual rules belong here rather than being reverse-engineered from the source each time.

### Structure

- A single full-viewport `<canvas id="viz">` is `position: fixed`, `z-index: 0`, `pointer-events: none`, and painted every frame via `requestAnimationFrame`.
- `nav`, `.hero`, `.section`, and `footer` are lifted to `z-index: 1` so page chrome sits above the canvas.
- `.stage-console` is a `position: fixed` glass panel centered at `top: 13vh`, sized `clamp(280px, 38vw, 560px)` by `clamp(220px, 36vh, 460px)`, holding, in order, the native track player, the two Mixcloud iframes, and three platform links. It scrolls independently (`overflow-y: auto`) with a purple-tinted thin scrollbar. It is designed to read as content displayed on the stage's center screen.
- `.console-player` sits at the top of that panel: a two-row block on the same glass, separated from the embeds below by a hairline border. The top row is a 34px circular `.track-playbtn` in accent purple beside a `.track-meta` column holding the `.track-title` and a small uppercase `.track-tag` carrying the track credit, currently "EOB, Azqato". The bottom row is the scrub: elapsed time, a full-width `.track-seek` range input, total time, with `.track-time` in a tabular-figure monospace so the digits do not jitter as they count.
- `.track-seek` is a styled `input[type=range]`. Both `::-webkit-slider-thumb` and `::-moz-range-thumb` are set, because the two engines share nothing here; omitting either gives one browser the platform default thumb against a custom track. The input carries `disabled` in the markup and is enabled by JavaScript on `loadedmetadata`, so it can never be dragged before a duration exists.
- The player is placed above the embeds rather than below because it is the only thing on the panel that drives the stage. Its position is the page's way of saying which control does something the others do not.
- `.mode-controls` is a fixed centered row at `bottom: 1.5rem` holding the visible mode buttons and the page's footer pill.

### The rendered scene

Drawn per frame in this order: background, beat flash, three trusses and their lights, the center screen (either a CSS-drawn LED grid or an upscaled WebGL texture), the two wing screens, the stage floor, the floor reflection, the DJ booth, fire columns, lasers, dust, haze, the crowd, and finally a prerendered vignette and letterbox grade.

- **Screen layout**: one wide center screen (42% of canvas width) and two flat side panels (22% each), all sharing a top edge at `10%` of viewport height and a height of `42%`.
- **DJ booth**: a front fascia flared wider at the bottom, raked side cheeks, a solid base running to the floor, a top deck with a back rail, two CDJ silhouettes, and a static mixer panel. The "AZQATO" wordmark sits on the fascia with a gold gradient and glow, sized to fit both the width and height of its text box.
- **Reflection**: rendered into a half-device-resolution buffer and mirrored onto the glossy floor, with a hole clipped over the booth footprint so the screens' bloom does not ghost the booth.
- **Bloom**: a deliberately cheap trick, drawing panel pixels into a 64x40 buffer and upscaling.
- **LED scanlines**: a 1x3 pixel repeating pattern at `rgba(0,0,0,0.55)` overlaid on screen panels.

### Screen modes

Ten modes exist in code (0-9). Modes 1 through 9 are WebGL2 fragment shaders rendered into an offscreen 640x400 canvas and drawn onto the center screen as an image; mode 0 is a plain canvas LED grid.

| Mode | Name | Visible in UI |
|------|------|---------------|
| 0 | Bars | Hidden |
| 1 | Volumetric | Hidden |
| 2 | Stars | Visible |
| 3 | Vortex | Visible |
| 4 | Squares | Visible, default on load |
| 5 | Origami | Hidden |
| 6 | Tunnel | Visible |
| 7 | Ghost | Hidden |
| 8 | Fence | Visible |
| 9 | Noise | Hidden |

Hidden modes keep their buttons in the DOM with `style="display:none;"` and are excluded from the auto-cycle. Every 1,800 frames (roughly 30 seconds at 60 fps) the page picks a random mode from the visible five, never repeating the current one.

### The visualizer reacts to the native track only

`music.html` carries one same-origin track (`audio/womanchild-azqato-remix.mp3`) alongside the two Mixcloud embeds. When that track is playing, its audio is routed through a Web Audio `AnalyserNode` and `freq(i)` reads real frequency data, so the lasers, fire, screen pulses, and crowd genuinely follow the music.

At every other moment the page falls back to a synthetic signal: three summed sine waves per band with fixed random phases, smoothed over time. That covers three cases, and they are all normal rather than error states:

| Situation | Signal |
|-----------|--------|
| Native track playing | Real analyser data, dynamic range widened by `Math.pow(raw, 1.6)` |
| Native track paused or never started | Synthetic. A paused track reads as silence, which would flatten the stage rather than idle it. |
| A Mixcloud embed playing | Synthetic. The iframes are cross-origin and their audio is unreadable by this page under any browser's security model, so the stage cannot follow them. |

That last row is the one to keep in mind when writing copy about the page. A visitor playing a Mixcloud mix sees choreography, not reaction. Only the native track drives the visuals.

**How a hit is made visible.** A detected kick raises `beatPulse` to 1, which decays at 0.86 per frame. It drives four things at once, and the multiplicity is the point: one element changing reads as an effect, four changing together reads as a response.

| Element | Response to `beatPulse` |
|---------|------------------------|
| Center screen | Zoom to 1.08, clipped to the bezel |
| Crowd | Front row bounce plus 5, back row plus 2.5 |
| Lasers | Mid-band intensity plus 0.22, clamped |
| WebGL clock | Jumps forward 0.05 s |
| Full-width light pump | Scaled to 0.26, capped on purpose, and only while the pyro is firing |

That last row is an accessibility constraint, not a taste decision, and in v2.9.3 it stopped being a theoretical one.

**Everything on this page used to be timed in frames, and `requestAnimationFrame` runs at the display's refresh rate.** The refractory was written as 26 frames, described everywhere as 433 ms, and that description was only ever true on a 60 Hz panel. Measured with a worst-case synthetic signal that clears the detector's threshold on every frame:

| Display | Before v2.9.3 | After | WCAG 2.3.1 limit |
|---|---|---|---|
| 60 Hz | 2.40 /s | **1.70 /s** | 3 /s |
| 120 Hz | **4.70 /s** | **1.70 /s** | 3 /s |
| 144 Hz | **5.60 /s** | **1.70 /s** | 3 /s |

On any high-refresh display the page was running at nearly twice the limit. Every rate is now wall-clock milliseconds, so the rig behaves identically on a phone, a TV and a 144 Hz gaming monitor, and the refractory is 600 ms rather than 433, which sits under the limit instead of on it.

**Rate is only half of photosensitivity.** The size of the luminance step matters as much as its frequency, so the light pump is halved to 0.26, the white wash over the main panel is roughly a third of what it was, and the laser response is softened. Impact is carried by motion (zoom, bounce, beam count) rather than by luminance. Do not raise the light pump.

**Motion reads from the fast signal, light reads from a slow one.** `sampleAudio()` smooths asymmetrically so a kick jumps 75 percent of the way to its peak in one frame. That is what makes a hit land in the bars and the beat detector, and it is exactly wrong for brightness: the same step across a large area is seen as the whole picture pulsing rather than as a hit. Panel bloom, the white panel wash, the background gradient and the floor grid therefore read from `envBroad` and `envLow`, the same signal symmetrically smoothed at roughly a 300 ms time constant. When adding anything new, ask whether it moves or whether it glows, and pick the signal accordingly.

**Nothing counted in frames.** `requestAnimationFrame` runs at the viewer's refresh rate, so a frame count is a rate that changes with their monitor. Both bugs of this class found so far (the beat refractory in v2.9.3, the `t` counter in v2.9.4) shipped looking correct because they were tuned on a 60 Hz panel. `t` now advances in 60 fps-equivalent units so its fourteen hand-tuned coefficients stay valid, and every other rate is wall-clock milliseconds.

**Nothing flashes without a visible cause.** Both the light pump and the white wash over the main panel are gated on `fireActive`, true while any of the four pyro jets is burning. This is a legibility rule before it is an accessibility one: a flash with nothing making it reads as a glitch, while the same flash with fire behind it reads as the blast throwing light across the room. It narrows the photosensitivity exposure as a side effect, since the flash cannot fire during quiet passages when the jets are down. The flag is set in `drawFire()`, which runs after the flashes in the frame order, so the gate reads the previous frame. 16 ms at 60 fps, not perceivable.

One consequence for local work: opening the page over `file://` makes the browser treat the same-folder mp3 as cross-origin, so the page deliberately skips Web Audio and runs synthetic. The audio is audible but the reaction is not real. Never judge the visualizer's reactivity from a local file load.

This is by design and should not be treated as a bug to fix. A browser cannot read audio out of a third-party iframe, and capturing system or other-tab audio was considered and declined. The paused `feature/native-audio-player` branch is the only path to genuine reactivity, because it plays the audio from the page itself.

### Dynamic favicon

Every third frame, `music.html` redraws a 32x32 canvas of twelve radial spokes colored `hsl(195 + f*65, 100%, 70%)` and assigns it to the page's `<link rel="icon">` as a data URL. The shared lion favicon is therefore only visible on this page for the first few frames. Every other page keeps the lion. **Updated 2026-10-02 (2.13.1):** the static icon on this page is now 🎧, not the lion; the spokes still replace it after the first few frames.

### Music page on phones

Tested 2026-10-02 (2.13.2, build pass item 15e) in Edge at 320, 375, 414 and 480 px wide, with touch on. No sideways scroll and no script errors at any width. Fixed at 600 px and below:

- The stage console now spans the screen less a 1rem gutter (up to 560px). Its old 280px floor left it narrower than the screen at 414 to 480px, half covering the badge.
- The "🎵 Azqato's Music" badge is hidden, since the top bar already reads "🎧 Azqato Music".
- The footer is one flowing block of 0.7rem links with the brand and copyright inline, and the mode row it sits in spans the screen. It went from about seven lines at 320px to three.
- On touch screens (`pointer: coarse`, any width) the seek bar is a 24px tall input with the 4px track drawn through its middle, and an 18px thumb.

Tap targets: the mode buttons and the console links are at least 32px tall; footer links are 24px, the WCAG 2.2 AA minimum. Desktop is unchanged (footer 87px, badge shown).

### Composer Atlas figures (Invests)

Added 2026-10-02 (2.13.3). A note-style callout (`pp-callout--note site-atlas site-atlas-figures`) holding a two-column table (`.site-atlas-table` in `invests/assets/css/site.css`): label left, figure right in tabular numerals, a 1px border between rows. Below it a `role="status"` line says where the figures came from (built in, saved from the last visit, or live, with Atlas's update date), then "A backtest, not a live record, and not financial advice" and a link to the strategy on Atlas. Percentages to one decimal place, ratios to two. Used on the Holy Grail page; `ATLAS_FIGURES` in `invests/scripts/site.py` can add it to other strategies.

### Page emoji and section brands

Added 2026-10-02 (2.13.1, build pass item 21), from the owner's answers. Each page has its own emoji favicon; the home page and any page without one use 🦁.

| Page | Emoji | Page | Emoji |
|---|---|---|---|
| Home | 🦁 | Links | 🔗 |
| About | 🙋 | Projects | 🛠️ |
| Discord | 💬 | YouTube | 📺 |
| Invests (Home) | 💰 | Support | ☕ |
| Codes | 💻 | Gaming Accounts | 🎮 |
| Music | 🎧 | Privacy | 🔒 |

The Invests sections take their section's emoji: Individual Stocks 📈, Indices & ETFs 📊, VIX Strategy ⚡, Leveraged Strategies 🚀, Resources 📚.

The top bar shows a section brand on that section's pages: "🎧 Azqato Music" on `music.html`, "💻 Azqato Codes" on `codes.html` and "💰 Azqato Invests" on the Invests pages. Every other page shows "Azqato.". Page titles are unchanged. The root pages' icons and brands are stamped by `tools/build-nav.py` (`ICONS`, `BRANDS`); the Invests icons come from `invests/scripts/site.py` (`GROUP_ICONS`). Never edit either by hand.

---

## Azqato Invests Visual System

The 21 pages in `invests/` have their own visual system, built on Template Interface's documentation-site and wiki-portal templates, with a light and a dark theme. This section is Azqato Invests' DESIGN.md and UI-REVIEW.md, merged word for word (Merged 2026-10-02, 2.12.0); headings moved down a level. Where this section and the rest of this document differ, the rest of this document is the most up to date rule (PRD Part 2, D22), and Roadmap P15 (adopt azqato.com's colors) will bring the two closer.

How Azqato Invests looks and behaves: the visual rules, the components and the reasons behind them. **Audit 2026-10-02:** the site is built and live; sections marked Built, Updated or Superseded describe it as it is, and the rest records the plan. Original text: There's no site code yet, so this describes the planned design. Its values were read from the Template Interface templates chosen in D8, at commit 61acfcb, on 2026-10-01. The PRD's verification checklist shows what has been checked against site code (nothing yet).

The Design details and Template ratings sections moved here from README.md word for word on 2026-10-01. Everything else was written by that day's documentation audit from the template code; text that sets something new, rather than recording what the templates do, says so.

### Design philosophy

A calm, readable reference: documentation-site's sidebar, breadcrumbs and single accent color carry every inner page, so the content, risk warnings included, is what stands out. The template supplies structure and styling, and the sources supply every word, number and link (core rule). Light and dark are the same site in two palettes, and motion only ever helps someone keep their place. (Drafted by the 2026-10-01 audit from D8 and the core rule.)

### Where the design comes from

- **D8:** `documentation-site` for every inner page and `wiki-portal`'s directory layout for the home page, borrowing `help-center`'s searchable FAQ and step-by-step guides, `admin-dashboard`'s summary tiles and table styling, and `blog-article`'s reading-progress bar. Template ratings, below, records why.
- **Template Interface** is the author's private template repo, `Azqato/templateinterface`. This document records it at commit 61acfcb (2026-10-01, "Rename to Template Interface; add return bar to every template page"). Record the commit each copied file comes from, since the templates are still changing.
- **The template contract.** Every template loads three shared stylesheets (theme.css for tokens, base.css for element defaults, components.css for shared patterns) and then its own styles.css. A template adds local tokens (documentation-site's `--pp-*` on `.pp-page`, wiki-portal's `--wiki-*` on `.wiki-page`) and never redefines a token from theme.css. This site follows the same rule.
- **Template Interface's own docs/DESIGN.md** is the reference for anything this document doesn't cover. Where the two differ, this document wins for this site.

### Color palette

Two themes, light and dark (D10), switched with the ☀️/🌙 button. Uses below come from the rules that reference each token in the template's stylesheet. Parts that are marked as demo-only (see Component patterns) still use some tokens, and those uses are listed so nothing is missed when the parts come out.

#### Light theme: documentation-site's palette

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

#### Dark theme: the shared tokens

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

#### How the two themes fit together

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

### Typography

**Minimum size (UI review, 2026-10-02):** no text under 12px. scripts/site.py raises source `font-size` values under 12px or 0.75rem (`min_font`), and site.css sets the template's and this site's small text (table headers, labels, badges, the sidebar card) to 12px or more. Figures in the stocks tables use the site font with tabular digits instead of a mono font. The VIX pages keep their mono font for data, as SF Mono, Consolas or Liberation Mono (Courier New last, since its Q reads as underlined).

No web fonts: every face is a system font stack.

- documentation-site, used for every inner page: text `"Segoe UI", system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif` (`--pp-sans`); code `Consolas, "SF Mono", Menlo, "Liberation Mono", monospace` (`--pp-mono`). The base is 16px with a line height of 1.6, and 1.7 inside articles.
- The shared stack, used by base.css, components.css and wiki-portal: text `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` (`--font-body`); code `ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace` (`--font-mono`).

#### Roles (documentation-site)

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

#### The shared scale (theme.css)

Sizes: xs 0.75rem, sm 0.875rem, base 1rem, md 1.125rem, lg 1.25rem, xl 1.5rem, 2xl 1.875rem, 3xl 2.25rem, 4xl 3rem. Line heights: tight 1.25, normal 1.5, relaxed 1.7. Weights: 400, 500, 600, 700.

base.css applies them to plain elements: body at base size with relaxed line height; headings semibold with tight line height (h1 3xl, h2 xl, h3 lg, h4 md); small text and `.caption` at xs in the secondary text color.

### Spacing system

- **The shared scale, on a 4px base:** `--space-1` 0.25rem (4px), `--space-2` 0.5rem (8px), `--space-3` 0.75rem (12px), `--space-4` 1rem (16px), `--space-5` 1.25rem (20px), `--space-6` 1.5rem (24px), `--space-8` 2rem (32px), `--space-10` 2.5rem (40px), `--space-12` 3rem (48px), `--space-16` 4rem (64px), `--space-20` 5rem (80px). base.css spaces headings with it (h2 starts `--space-10` below the text above it, h3 `--space-8`, h4 `--space-6`; every heading leaves `--space-4` below) and leaves `--space-6` after paragraphs and lists.
- **documentation-site uses pixel values rather than the scale.** The main column is padded 32px 48px 72px (top, sides, bottom), then 32px 40px 64px at 1150px and below, 28px 24px 56px at 900px and below, and 20px 16px 48px at 640px and below. The sidebar is padded 24px 16px 32px.
- **Corner radius:** documentation-site uses 6px everywhere (`--pp-radius`); the shared scale is 4px, 6px, 12px and fully round.
- **Shadows (shared):** small `0 1px 2px rgba(0, 0, 0, 0.4)`, medium `0 4px 12px rgba(0, 0, 0, 0.5)`, large `0 8px 24px rgba(0, 0, 0, 0.6)`.
- **Layout sizes:** documentation-site's top bar is 60px tall (`--pp-top`), the sidebar 260px wide (`--pp-rail-w`) and the "On this page" column 240px, and article content is capped at 760px. wiki-portal's rail is 168px, its content is capped at 1120px (1440px on a page marked `is-wide`), with a `--space-8` gutter under a 132px masthead (190px at 760px and below). The shared layout tokens (`--sidebar-width` 280px, `--content-max-width` 780px, `--portfolio-max-width` 1200px) belong to Template Interface's own pages.

### Breakpoints

All are maximum widths, so each applies at that width and below.

#### Inner pages (documentation-site)

| Width | What changes |
|---|---|
| Above 1150px | Three columns: sidebar, page, "On this page" |
| 1150px | The "On this page" column hides and an inline list appears at the top of the article; two columns |
| 1000px | The top bar's status line hides (a demo part) |
| 900px | One column. The sidebar becomes a drawer, `min(320px, 86vw)` wide, that slides in from the left over a scrim when the menu button is pressed; the menu and close buttons appear |
| 640px | The top bar's right-hand group hides; search becomes a 40px icon button; headings and code shrink (see Typography); cards and the pager stack into one column; the search dialog goes full width. (Since v1.0.1 the pager wraps rather than stacking; see Breadcrumbs and pager.) |
| 400px | The logo's tag hides; step numbers shrink to 26px |

#### Home (wiki-portal)

| Width | What changes |
|---|---|
| 1280px | The search box narrows to 200px |
| 1200px | Section tiles drop to 3 columns |
| 1080px | Split sections stack; the right rail goes to 2 columns |
| 900px | Feature, welcome and banner blocks go to 1 column; the skill grid goes to 2 |
| 760px | The 168px rail becomes a 240px drawer; the top bar stacks and search goes full width; the masthead grows to 190px; tiles go to 2 columns |
| 520px | Tiles and the skill grid go to 1 column; the welcome heading shrinks to 2xl |

Inner pages switch to a drawer at 900px and the home page at 760px. Whether the home page keeps its own rail or uses the site's sidebar isn't decided; settle the difference when the home page is built. **Settled (P2):** Home uses the site's sidebar and the inner pages' breakpoints; the wiki-portal table above is kept for reference. site.css adds its own rules at 900px (the azqato.com bar folds into the menu; larger tap targets) and 640px (phone layouts).

#### Print

documentation-site hides the top bar, sidebar, "On this page", the feedback form, the pager, copy buttons and heading anchors, and prints code black on white.

### Component patterns

#### Page structure

documentation-site's page, as read: a skip-free run of landmarks, in this order.

1. `nav.sr-bar`: Template Interface's "Back to Template Interface" bar. It comes out (Removed template parts).
2. `header.pp-top`: the top bar.
3. `nav.pp-sidebar`, labeled "Documentation": the sidebar.
4. `main.pp-main`: the page, with labeled breadcrumbs ("Breadcrumb") at the top and labeled previous/next links ("Previous and next page") at the bottom.
5. `aside.pp-toc`: "On this page".
6. `footer.pp-footer`.

The template keeps its demo pages in one file and switches between them by URL hash; this site gives every page its own file (Design details).

#### Top bar

- **In the template:** a menu button (narrow screens only), the "Parcelpoint" logo with a "Docs" tag, a search button, and on the right the status line, the "API v3.4" version label and a "Get API keys" button.
- **On this site:** the logo becomes 💰 Azqato Invests (D11); the search button stays and searches every page; the ☀️/🌙 button is added (D10); the status line, version label and API keys button come out. If D9 stays, azqato.com's nav sits above the top bar.

#### Sidebar

**Built 2026-10-02 (P2):** labeled "Site sections"; Home first, then the five groups, with the six leveraged strategies indented under Leveraged strategies; a card at the foot says "Educational use only. Not financial advice.", carried from the source sidebars.

**Updated 2026-10-02 (v1.0.1, v1.1.0):** the groups are Individual Stocks, Indices & ETFs, VIX Strategy, Leveraged Strategies and Resources, each a collapsible `<details>` that starts open only when it holds the current page. In the four topic groups the first entry is the landing page, listed as "Overview"; nothing is indented. The sidebar is a full-height flex column and the note sits at its foot (`.site-sidebar-foot`), on two lines: "Educational use only." and "Not financial advice." When open groups fill the sidebar, the note follows them, 32px below. At 900px and below an "Azqato.com" group holds azqato.com's links.


The five sections, Learn, Tools, Strategies, Resources and FAQ, as groups (D12). The current page is marked with the pale accent background, deep accent text, weight 600 and an accent edge. Composer Atlas, Net Worth Tracker and Automate Fundamentals never appear here (D18). At 900px and below the sidebar becomes a drawer. Its label, "Documentation" in the template, needs a name that fits this site (not decided).

#### Breadcrumbs and pager

Breadcrumbs show where the page sits (for example Strategies, then Leveraged strategies, then 3 Sig). The pager links to the previous and next pages; planned to follow the sidebar's order.

**Updated 2026-10-02 (v1.0.1, v1.1.0):** breadcrumbs read Home, then the group (linked to its landing page), then the page; a landing page shows Home, then its own name. The pager follows the sidebar order. Each pager button fits its text (at least 200px): Previous sits at the left edge and Next at the right, also when either is alone (Home has only Next, the FAQ only Previous); they wrap onto two lines on phones instead of stacking into one column. Home and Resources keep the same 32px gap above the pager as every other page.

#### Article content

- A lede under the h1, then h2 and h3 sections. Headings carry anchors.
- **Numbered steps** for the Finviz and Seeking Alpha setup guides (D8 borrows help-center's step-by-step guides for these).
- **Callouts:** a note style (emerald) and a warning style (amber), each with an icon column.
- **Tables:** in a bordered, scrollable wrapper, with a tinted header row.
- **Cards:** a three-column grid that stacks below 640px, with a border and shadow on hover.
- The template's strategy-friendly structure suits the write-ups (Overview, Rules and Logic, Performance Notes, Risks and Caveats, Resources: see Template ratings). Each page keeps its source's own sections and wording (core rule).

#### "On this page"

The right-hand column on reading pages, marking the section in view. At 1150px and below it becomes an inline list at the top of the article. Tool pages drop it so the screener's table gets the full width (Design details); they also need the 760px article cap lifted.

#### Search

The search button opens a dialog, also opened with / or Ctrl+K. Results show a title, a breadcrumb and a snippet, with matches highlighted. Here it searches all 21 pages. How the template builds its search index wasn't read (its script.js); decide how this site builds one when the shell is built. **Built 2026-10-02 (P2):** scripts/site.py generates assets/js/search-index.js from every page, loaded the first time search opens; before typing, the dialog suggests four pages (the Screener, VIX Strategy, Stock metrics and the FAQ).

#### Buttons

documentation-site's `.pp-btn`: 0.9rem, weight 600, 6px corners; the solid style is emerald with white text and turns deep emerald on hover. The shared `.button` is 40px tall in primary (accent fill, `#0d1117` text), secondary (accent outline) and ghost styles.

#### Footer

**Built 2026-10-02 (P2), a default for the author to change:** the brand, "Educational use only. Not financial advice. Some links are referral links.", links to Resources and the FAQ, and "Built by Azqato". Each moved page also keeps its source's own footer text at the end of the article.


The template's footer has a brand line and links on the rail background. This site's footer content isn't decided.

**Updated 2026-10-02 (v0.16.0):** one footer per page. The source footers that repeat it are hidden (kept in the page); the VIX pages' disclaimer and copyright lines sit in the site footer as notes.

#### Removed template parts

The demo-only parts named in Design details come out: the API keys button, API status line, code-language tabs and the page-feedback form. The audit found two more parts that look demo-only, which come out too (Question 10, confirmed 2026-10-01):

- the top bar's "API v3.4" version label;
- the "Back to Template Interface" return bar, added to every template page on 2026-10-01, which links back to the template gallery.

The template's own text must not survive anywhere: before finishing a page, search it for "Parcelpoint", "API" and the template's title, "Introduction - Parcelpoint Docs".

#### Home page (wiki-portal layout)

**Superseded 2026-10-02 (v0.16.0, UI review):** Home is one grid of 10 project cards in the source's card style (no separate section tiles), up to 1400px wide like every page, on the inner pages' breakpoints; the wiki-portal breakpoints under Breakpoints don't apply to it. The text below is kept as it was.

**Built 2026-10-02 (P2, P3):** Home uses the inner pages' shell (top bar, sidebar, drawer at 900px) with no "On this page" and content up to 1120px, wiki-portal's width. Its body follows wiki-portal's directory idea: the intro, tiles into the five sections, then the project cards. wiki-portal's violet palette, masthead art, rail and statistics list aren't used; the live VIX statistic is left for later.


From the plan: the intro and "Join the Discord" button from invests.html, tiles into each section, and all 7 project cards with their text (D14, D18). From wiki-portal's rating: portal tiles for the sections, the statistics list for live numbers like the VIX, update panels for what's new, and dense panels for the curated links, with the masthead artwork and talk-page tab toned down for a finance site.

#### Borrowed parts

D8 borrows help-center's searchable FAQ and step-by-step guides, admin-dashboard's summary tiles and table styling (for the tools), and blog-article's reading-progress bar (for long pages). These templates were rated in planning but their code wasn't read in this audit. Record each part's markup, tokens and behavior here when it's borrowed.

#### Theme button

**Moved 2026-10-03 (2.14.2, owner's request):** on every page except the home page, the theme button sits in the second bar, which matches Invests: the page's emoji and name (for example "💻 Azqato Codes"), "Search the site" (`/search.js`, which searches every root page and every Invests section through `/search-index.js`; both are written by `tools/build-nav.py`) and the theme button. The top bar shows only "Azqato." and the links, and scrolls away while the second bar stays. The home page keeps one bar, with the theme button at its end. The music page's second bar has no button (it stays dark).

**Moved 2026-10-02 (2.13.7):** the script is now `/theme.js`, shared by every page on azqato.com and Invests. The saved choice is under `azqato-theme` (Invests' old `azqato-invests-theme` still counts). On the root pages the button sits at the end of the slim top bar, beside ☰ on phones.

**Built 2026-10-02 (P2):** assets/js/theme.js. It starts in the visitor's system theme, saves the choice in the visitor's browser, sets the theme in the head before the page draws, and shows the theme it switches to: ☀️ while dark, 🌙 while light, which is Template Interface's convention. Its accessible name says the action ("Switch to light theme").

- ☀️/🌙 in the top bar (D10).
- The site starts in the visitor's system theme and switches when the button is pressed; the choice is saved in the visitor's own browser (PRD Assumptions).
- Planned by the 2026-10-01 audit: apply the saved theme with a small script in the page head, before the page is drawn, so it never flashes the wrong theme first.
- Not decided: whether the button shows the current theme's emoji or the one it switches to. **Decided (P2):** the one it switches to, as built above.
- It needs an accessible name that says what it does, such as "Switch to dark theme", because an emoji alone isn't a clear name.

#### Icons

- **Favicon:** 💰 (D11), as an inline SVG data URI, the technique azqato.com uses for its 🦁 (Design details); invests.html's own favicon is a `data:image/svg+xml` with a 100 by 100 viewBox. The template's favicon.png doesn't come over.
- **Interface icons:** Template Interface's rules: inline SVG on a 24 by 24 viewBox, 2px stroke, round caps. Its reference is assets/svg/icon-reference.md in that repo.

### Accessibility standards

- **Level:** WCAG AA, the level Template Interface targets on every page and template. Assumed to mean WCAG 2.2 (Question 11).
- **Contrast:** 4.5:1 for body text; 3:1 for large text (1.5rem and up, or bold at 1.25rem and up); 3:1 for focus rings and for the edges of controls against what's behind them.

**Measured pairings.** Computed on 2026-10-01 with the WCAG formula, from the token values. All the text pairings pass AA except white on the dark accent, which the dark theme must not use. **Audit 2026-10-02:** the dark rows below measure the shared theme.css tokens; the built dark theme uses documentation-site's own dark palette instead (How the two themes fit together), whose contrast scripts/browser.py checks on every page in both themes.

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

### Animation and motion

- **Shared timing (theme.css):** fast 100ms, base 150ms and slow 250ms, all eased. Under `prefers-reduced-motion: reduce`, all three become 0ms, which switches off every shared transition at once.
- **documentation-site:** smooth scrolling to anchors; the drawer slides in over 0.2s; cards change border and shadow over 0.15s on hover. Under reduced motion, scrolling jumps and the drawer and cards don't animate.
- **Shared components:** cards lift 2px with a larger shadow on hover. A fade-in-up effect (12px rise, slow timing) is applied by Template Interface's motion-utils.js; its reduced-motion handling comes from the theme timings.
- **wiki-portal:** a pulse animation, off under reduced motion; its drawer uses the slow timing.
- **Added by the 2026-10-01 audit:** live numbers, such as the VIX reading and market data, change without animation, so a value is never shown partway through a transition.

### Page layouts

**Width (UI review, option C, 2026-10-02):** content runs from the sidebar to the 1400px limit on every page, prose included; the sources' own caps (stocks 820px, VIX 1100px) are lifted. A page whose "On this page" list is empty gives that column back. Card grids add columns as space allows (Market Overview 200px minimum, Home 200px, Resources masonry columns of 260px). On phones (640px and below) the VIX tables become stacked cards, and the sidebar holds the azqato.com links (900px and below). Sidebar groups collapse except the one holding the current page. Each page has one footer; the VIX pages' disclaimer lines sit in it.

The site map in the PRD lists every page and its source.

- **Inner pages:** documentation-site's grid of sidebar (260px), page (content capped at 760px) and "On this page" (240px), under a 60px top bar. (Since v0.16.0 the content cap is 1400px; see Width above.)
- **Tool pages:** the same without "On this page", and with the content cap lifted, so the screener's table can use the full width.
- **Home:** wiki-portal's layout: a masthead band, then a narrow rail beside a wide content column (up to 1120px) of tiles and panels. (As built: the inner pages' shell with one card grid; see Home page under Component patterns.)

### Design details

- `documentation-site` keeps its seven demo pages in one HTML file and switches between them by URL hash. This site gets one file per page, so every page has its own address and the redirects in D7 have somewhere to land.
- Tool pages drop the "On this page" column so the screener's table gets the full width.
- The template's demo-only parts come out: the API keys button, API status line, code-language tabs and the page-feedback form, which needs a server. They belong to the template, not the sources, so the core rule doesn't cover them.
- None of the 21 templates has a dark mode, so the dark theme is built on top of the template's shared color tokens. (Superseded: documentation-site gained its own dark mode at commit ed840da, which this site uses; see How the two themes fit together.)
- If D9 stays: azqato.com is dark-only today (background `#0d1117`, accent `#00d4a0`), so its nav needs a light version for this site's light mode. azqato.com's pages get the nav from `tools/build-nav.py`, which only reaches pages in the azqato.github.io repo, so this site would carry its own copy of the nav, with links pointing back to azqato.com.
- The 💰 favicon uses the same inline-SVG emoji technique azqato.com uses for its 🦁.

### Template ratings

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

#### Summary

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

### Notes for contributors and AI models

- Read the PRD's core rule and Decisions before changing anything here. The design serves the content: when a layout can't hold some source content, the layout changes.
- Copy template files from Template Interface at a recorded commit and note the commit in PATCHNOTES.md.
- Never redefine a theme.css token. Give this site's values to its own tokens.
- Build each part in both themes, and measure the contrast of every new pairing in both.
- The literal colors in documentation-site's stylesheet need dark counterparts; they're listed under the light palette.
- No template demo text may survive: search for "Parcelpoint" and "API" before finishing a page.
- No web fonts; keep the system stacks.
- When the design is built, check this document against the code and mark each section on the PRD's verification checklist.

### Invests UI review (record, 2026-10-02)

A review of the user interface, the author's decisions on it, and what was built (v0.16.0, 2026-10-02). The findings below are kept as they were found; the "Done" section says what changed for each. **Audit 2026-10-02:** a record. Later changes: the pager buttons fit their text and the sidebar note sits at the sidebar's foot (v1.0.1), and the sidebar groups became Individual Stocks, Indices & ETFs, VIX Strategy, Leveraged Strategies and Resources (v1.1.0); see PATCHNOTES.md.

#### How the review was done

- **Date:** 2026-10-02, on the v0.14.3 build.
- **Method:** every page was scrolled top to bottom in headless Edge (Playwright, `channel="msedge"`), at:
  - 1440px wide, in light and dark;
  - 390px wide (a phone), in light.

  Each viewport was captured, and a probe measured small text, tap targets and line lengths.
- **Overall:** dark mode holds up well everywhere. Nearly every issue below shows up in light mode, on the phone, or in both.
- **Content rule:** every fix suggested here changes presentation only. None cuts or rewords source content (core rule).

#### Author's decisions (2026-10-02)

Decided in the brainstorming session; all built in v0.16.0 (Done, below).

| Topic | Decision |
|---|---|
| Footers | Merge into the site footer: one footer per page, carrying any wording only the source footers had (for example the VIX "Past performance is not indicative of future results"). |
| Home | Merge "Explore the site" and "Projects" into one grid. |
| Page width | **C, everything full width to 1400px** (chosen 2026-10-02 from three previews: A, grids wide with prose capped at about 75 characters; B, one column of about 1100px; C, everything full width). |
| Phone | VIX tables stack as cards; the screener gets a pinned ticker column and a scroll shadow. |
| Small text | 12px floor; table headers about 11.5px uppercase. |
| Sidebar | Collapse the groups that don't hold the current page. |
| VIX pages | Same status wording on the Dashboard and Custom; result (reading and donut) first on Custom; VIX Strategy uses the site's headings and boxes. |
| LIVE vs CACHED | Investigate as a bug and fix it in this site's copy. |
| Resources | Masonry columns. |
| Icons | Keep emoji, but pick a matching style and size. |
| FAQ chip | Restyle "Strategy Q&A" as a plain label, not a button. |
| Table fonts | Figures use the site's sans font with tabular (aligned) digits. |
| Azqato nav on phones | Fold its links into the menu drawer. |
| Tap targets | At least 24px on phones, by padding; text size unchanged. |
| Width examples | Build the three example pages together with the other fixes, as previews that don't change the real site. **Built 2026-10-02:** previews/index.html (made by scripts/previews.py), with Market Overview, Stock metrics and Resources in each option. All three lift the stocks pages' 820px cap and give back the empty "On this page" column on Resources and the FAQ. **Removed 2026-10-02** once C was chosen. |

Still open: the metric heading subtitles on Stock metrics, and the Market Overview card names and column count (these follow the width decision).

#### Done (v0.16.0, 2026-10-02)

Every decision above is built, and the findings below are fixed except where noted. Each change is presentation only: no source wording was cut or rewritten, and scripts/check.py still finds every inventoried item on its page.

| Item | What changed | Where |
|---|---|---|
| Page width (C) | The stocks pages' 820px cap (`.content-inner`) and the VIX pages' 1100px cap (`.container`, 720px `.section-lead`) are lifted, so content runs to the site's 1400px limit. Market Overview's grid fills the width (5 cards across at 1440px instead of 3). Pages whose "On this page" list is empty (Resources, FAQ) give its 240px column back to the content. | site.css, "Full-width content" |
| Footers | One footer per page. Source footers that only repeat the site footer ("Built by Azqato.", "Educational use only. Not financial advice.") stay in the page with class `site-dup`, hidden, so nothing is deleted. The VIX pages' disclaimer ("This is not financial advice... Past performance is not indicative of future results.", and on Custom "Tickers you enter here are not verified against a live quote.") and "© 2026 VIX Strategy. Built with no backend. Powered by VIX." move into the site footer as `site-footer-note`; their call-to-action ("View Live Strategy", "Read the Full Pitch", "View Core Strategy") stays in the page. | site.py `merge_footers`, `footer(page, notes)` |
| Home | "Explore the site" is gone; Home has one grid in the source's project-card style: Stocks, Stock Screener, Market Overview & VIX tools, VIX Strategy, Leveraged Strategies, Curated Resources, FAQ, then the outside projects (Automate Fundamentals, ComposerAtlas, Net Worth Tracker). Three cards are added (Market Overview & VIX tools, Curated Resources, FAQ) for the sections no source card covered; all seven source cards are kept. 10 cards make two full rows of 5 at 1440px. | site.py `split_invests`, `home_cards` |
| Icons | The emoji stay; each sits in the same 44px rounded tile at the same size. On phones the icon sits beside the title, so the cards are no longer tall and mostly empty. | site.css, "Home: one grid" |
| Small text | No source text is under 12px: scripts/site.py raises any `font-size` under 12px or 0.75rem in the source stylesheets and inline page styles (`min_font`). Table headers, labels, badges, chip counts and the sidebar card are set to 12px or more in site.css. The probe found 0 text under 12px on all 21 pages at 1600px and 390px. | site.py `min_font`; site.css, "Text size floor" |
| Sidebar | Each group is a `<details>`: it opens when it holds the current page and the rest open on click, with a chevron. On Home every group starts closed. | site.py `sidebar`; site.css, "Sidebar" |
| Azqato nav on phones | At 900px and below the azqato.com bar is hidden, and its links appear as an "Azqato.com" group in the menu drawer. | site.py `sidebar`; site.css |
| Tap targets | On phones, breadcrumb, "On this page", footer and sidebar links are at least 24px tall (sidebar 32px), and the FAQ toggles are 48px with a larger +. Links inside paragraphs stay as they are (the 24px rule exempts inline links); the probe's remaining small targets are all of that kind. | site.css, "Tap targets" |
| Table fonts | Figures in the stocks tables use the site font with tabular digits (`font-variant-numeric: tabular-nums`) instead of SF Mono/Consolas. The guides' `.ui-text` (on-screen labels) keeps its mono font. | site.css, "Tables" |
| Metric subtitles | The subtitle under each Stock metrics heading lines up with the heading (the source's 11px indent and -4px margin removed). | site.css |
| FAQ chip | The stocks pages' tag ("Strategy Q&A", "The 12 Signals" and the others) is a plain uppercase label with no border or background. | site.css, `.hero-badge` |
| Screener | The disclaimer under the table is a normal left-aligned paragraph at 14px. The pinned ticker column casts a shadow. On phones the tier chips wrap, the filter box is full width, the ticker column is narrower, and a "Swipe sideways for more columns →" line sits above the table. | site.css, "Screener" |
| Market Overview | Card names wrap instead of being cut off. | site.css |
| Resources | Masonry columns (CSS `columns: 260px`), so cards of different lengths stack without tall empty boxes. Cards read down each column, then across. | site.css, "Resources" |
| Card headings | The article's 32px heading margin no longer pushes Home and Resources card titles away from their icons. | site.css |
| VIX: tables on phones | The VIX tables become stacked cards at 640px and below; site.js gives each cell its column heading as `data-label`, including rows the tools add after loading (a MutationObserver). | site.js; site.css, "VIX pages" |
| VIX: status wording | The Custom builder's tier line reads like the Dashboard's ("VIX 15.45 → VIX 15–25 - Moderate Fear" instead of "Tier: 2"). | site.py `vix_inline` |
| VIX: LIVE vs CACHED | **Cause:** vix.js saves each reading for 30 minutes (`REFRESH_TTL`). The first VIX page fetched the feed and showed LIVE; the next page within 30 minutes read the same saved reading and showed CACHED, though it was the same live number. **Fix:** a saved reading under 30 minutes old now shows LIVE; one older than that, used because the feed failed, still shows STALE. Checked: Dashboard then Custom both show LIVE. | site.py `vix_inline` |
| VIX: Custom result first | The Custom builder shows the reading and the tier line first. **Changed v0.16.1 at the author's request:** "Your Categories" (the ticker inputs) then sits above "Your Custom Allocation" (the chart) and the breakdown, so the inputs come before the results they drive. | site.py `build_page` |
| VIX: Strategy Summary | The tool sections' padding drops from 48px to 32px, so the single accordion item doesn't sit in a large empty box. | site.css |
| VIX: QQQ looked underlined | Courier New's Q has a tail that reads as an underline. The VIX pages' mono font is now SF Mono, Consolas or Liberation Mono, with Courier New last. | site.css |
| VIX Strategy page style | Section headings use the site's heading font and size with no green underline; the alternating section backgrounds become a thin line between sections; cards, stat boxes and the table use the site's border, radius and background. The hero is unchanged. | site.css |
| Leverage callouts | Callout text is 15px (was 14.4px). | site.css |

Not changed: the leveraged pages' tables keep their layout; with the wider column they no longer wrap badly at 1440px. The items hidden on phones on the strategy pages stay as they are (no change needed).

#### Site-wide

1. **Two or three footers on one page.**
   - The pages that came from the stocks repo end with:
     - the source's centered "Built by Azqato.";
     - a tiny, left-aligned "Educational use only. Not financial advice." block;
     - the site footer, which says the same thing.
   - The VIX pages also carry their own footer: the disclaimer, a copyright line, "Built with no backend. Powered by VIX." and "Built by Azqato".
   - *Suggested fix:* hide the source footers and keep the site footer. The wording is only hidden, not removed, so no content is lost. The VIX disclaimer could move into the page as a notice if its extra wording ("Past performance is not indicative of future results") should stay visible.
2. **Some text is very small.**
   - Table headers in the stocks pages are 9.6 to 10.4px (metrics, example-label, metric-label).
   - Badges are 11.5px, and callout text is small.
   - The screener's group headers are about 9.9px.
   - The VIX gauge labels are 9.9 to 10.4px, and the VIX disclaimers are also tiny.
   - The sidebar footer text is 11.5px.
   - *Suggested fix:* nothing under 12px, and table headers at about 11.5px.
3. **Pages use the width unevenly.**
   - Market Overview, the FAQ, Resources and the VIX Strategy page stop at about 780px, leaving empty space to the right.
   - The paragraphs on VIX Custom (about 1052px) and the leveraged strategy pages (about 1004px) run long enough to be hard to read.
   - On pages with "On this page", the prose sits at about 570 to 780px with a gap before that list. Wide tables, such as the action levels on Index & ETF methodology, are cramped there.
   - *Suggested fix:* let cards and grids fill the width, and cap paragraphs at about 75 characters.
4. **The sidebar is long.**
   - Resources and FAQ only appear after you scroll the sidebar.
   - *Suggested fix:* collapse the groups that don't hold the current page, or give the sidebar its own scroll.
5. **Small tap targets on the phone.**
   - Breadcrumb links, inline links, "On this page" links and the top bar's "Azqato" link are 13 to 19px tall.
   - *Suggested fix:* at least 24px.
6. **The Azqato nav bar is cut off on the phone.**
   - It ends mid-word ("Co...") with no sign that it scrolls sideways.
   - *Suggested fix:* a fade at its right edge, or fold it into the menu.
7. **Fonts are mixed in the stocks tables.**
   - Mono and sans fonts sit side by side in the same tables.
   - *Suggested fix:* pick one for the figures.
8. **Subtitles under the metric headings are indented oddly** on Stock metrics.

#### Home

1. **"Explore the site" and "Projects" overlap.**
   - The Learn, Tools and Strategies tiles show up again as the Stocks, Leveraged Strategies, VIX Strategy and Stock Screener cards.
   - *Suggested fix:* merge them, or make Projects only the outside projects.
2. **The last card sits alone.**
   - The Projects grid leaves Stock Screener by itself in its row.
3. **The icons and the phone cards.**
   - The project icons are a mix of emoji and look inconsistent.
   - On the phone the cards are tall and mostly empty, with the icon floating on top.

#### Screener

1. **Only two columns show on the phone.**
   - At 390px the table shows Ticker and Tier only. The other ~15 columns are off to the side, with nothing showing that the table scrolls.
   - *Suggested fix:* a scroll shadow or hint, a pinned ticker column, or a compact phone view.
2. **The tier chips** (All, S+, S, A...) are cut off on the right on the phone.
3. **The "Filter by symbol" box** is clipped on the phone.
4. **The disclaimer under the table** is centered small print.
   - *Suggested fix:* a normal left-aligned paragraph.

#### Market Overview

1. **Only three columns at any width.**
   - The grid stays at 3 columns, about 780px wide, even at 1440px.
   - *Suggested fix:* 4 to 6 columns on wide screens.
2. **The card names (`.market-card-name`)** are clipped at 390px.
3. **Hard to scan.**
   - The colored bar on top of each card (green or red, for up or down) is the clearest signal. The name and ticker labels above it are tiny.

#### VIX Dashboard and VIX Custom builder

1. **The phone layout is the weakest on the site.**
   - The Allocation Breakdown table squeezes its description column into one-word lines and cuts text off on the right.
   - The Tier Reference table is clipped on the right.
   - *Suggested fix:* stack both tables as cards on the phone.
2. **The two pages word the same reading differently.**
   - The Dashboard's status line reads "VIX 16.39 → VIX 15-25 - Moderate Fear". Custom's reads "VIX 16.39 → Tier: 2".
   - *Suggested fix:* use the same wording on both.
3. **LIVE and CACHED disagree.**
   - Loaded at the same moment with the same reading, the Dashboard showed LIVE (green) and Custom showed CACHED (amber).
4. **An oversized box for one item.**
   - "Strategy Summary" holds a single accordion item in a large empty box, with too much space around it.
5. **The result is far down the page on Custom.**
   - The reading and the donut sit below the inputs, so the result you came for is a long way down.
6. **Ticker labels look like links.**
   - In light mode the QQQ and TQQQ labels are underlined.

#### Strategies

1. **Cramped tables.**
   - Tables in the narrow column next to "On this page" are cramped, and some cells wrap badly.
2. **Small callout text.**
   - Callouts such as "Composer symphony ID" and the formula box on HFEA are fine, but their text is small.
3. **Two styles on one site.**
   - The VIX Strategy page uses the VIX source's headings and boxes, so it doesn't match the leveraged pages.
4. **Hidden text on phones is harmless.**
   - The items that are visually hidden on phones on the strategy pages do no harm. No change needed.

#### Resources

1. **Narrow grid.**
   - The 3-column cards stop at about 800px.
2. **Uneven card heights.**
   - Category sizes vary a lot (Real Estate has 9 links and Charts has 2), so cards in the same row leave tall empty boxes.
   - *Suggested fix:* a masonry or column layout.
3. **Mixed icons.**
   - The category icons are small emoji next to uppercase titles, the same mix as on Home.

#### FAQ

1. **It stops at about 780px.**
   - The question list is clean, but it stops at that width.
2. **A chip that looks clickable.**
   - The "Strategy Q&A" chip looks like a button but does nothing.
3. **Small toggles on the phone.**
   - The + toggles work but are small.

#### Top 5, if only a few get done

1. One footer on every page.
2. Phone views for the VIX tables (stacked cards) and the screener (at least show that it scrolls sideways).
3. Nothing under 12px.
4. Let the grids (Market Overview, Resources, FAQ) fill the width, and cap paragraph length.
5. Merge "Explore the site" and "Projects" on Home.

---

## Image Assets

All images live in `img/` at the project root. Profile and thumbnail images render with `object-fit: cover`; the About avatar is a circle (`border-radius: 50%`).

| File | Size | Referenced by |
|------|------|---------------|
| `about-profile.jpg` | 198 KB | `about.html` pitch card avatar |
| `yt-thumb-azqato.jpg` | 333 KB | Kept, no longer referenced (since 2.12.6) |
| `yt-thumb-azqato-160.webp` | 7.1 KB | `youtube.html` (since 2.12.6) |
| `yt-thumb-streams.jpg` | 469 KB | Kept, no longer referenced (since 2.12.6) |
| `yt-thumb-streams-160.webp` | 6.1 KB | `youtube.html` (since 2.12.6) |
| `yt-thumb-mixes.jpg` | 854 KB | Kept, no longer referenced (since 2.12.6) |
| `yt-thumb-mixes-160.webp` | 8.9 KB | `youtube.html` (since 2.12.6) |
| `yt-thumb-chills.jpg` | 659 KB | Kept, no longer referenced (since 2.12.6) |
| `yt-thumb-chills-160.webp` | 7.3 KB | `youtube.html` (since 2.12.6) |
| `home-hero-profile.jpg` | 445 KB | Nothing |
| `logo-cat-avatar.jpg` | 335 KB | Nothing |
| `music-logo-small.jpg` | 45 KB | Nothing |
| `music-playlist-bangers.jpg` | 246 KB | Nothing |
| `music-playlist-addictions.jpg` | 237 KB | Nothing |
| `yt-channel-azqato.jpg` | 108 KB | Nothing |
| `yt-channel-streams.jpg` | 159 KB | Nothing |
| `yt-channel-mixes.jpg` | 182 KB | Nothing |
| `yt-channel-chills.jpg` | 138 KB | Nothing |
| `20260711-0151-37.7601512.gif` | 1.9 MB | Nothing |

> **Resolved 2026-08-29.** Earlier documentation described `home-hero-profile.jpg` as "Hero avatar on the landing page (`index.html`)" and the two `music-playlist-*.jpg` files as Spotify playlist covers on `music.html`. Neither was true: `index.html` contains no `<img>` at all, and `music.html` no longer lists Spotify playlists. The table above records actual usage instead.
>
> **The ten unreferenced files stay, and this is now a standing rule.** Nothing in `img/` is deleted unless the owner asks for that specific file by name. Unreferenced is the normal state of that folder: it is the owner's working library, not a set of build outputs, and a file being unlinked says nothing about whether it is wanted. Do not raise it as dead weight in a future audit, do not propose a cleanup, and do not delete one while doing unrelated work. The "Referenced by: Nothing" column above is a factual note about the current pages, not a to-do list.

The four `yt-thumb-*.jpg` files are the site's real performance outlier: `youtube.html` is 7.8 KB of HTML that pulls 2.3 MB of images. No lazy-loading attribute is set on them. **Fixed in 2.12.6:** the page now loads 160 px WebP copies (30 KB for all four, from 2.37 MB) with `loading="lazy"`, width and height; the originals stay in `img/`.

---

## Accessibility Standards

Target: WCAG 2.1 Level AA where achievable within a zero-dependency constraint.

| Requirement             | Implementation                                                         |
|-------------------------|------------------------------------------------------------------------|
| Color contrast          | `--text` (`#e6edf3`) on `--bg` (`#0d1117`): roughly 15:1               |
| Muted text contrast     | `--text-muted` (`#8b949e`) on `--bg` (`#0d1117`): roughly 4.8:1 (AA normal text) |
| Semantic markup         | `<nav>`, `<section>`, `<footer>`, `<h1>`/`<h2>` hierarchy used throughout |
| Link clarity            | All links visually distinct (accent color plus hover state)            |
| Button labels           | All buttons have visible text; the nav toggle has `aria-label` and a live `aria-expanded` |
| Keyboard navigation     | Standard browser tab order; no custom focus traps                      |
| Focus indicators        | Browser default focus ring preserved                                   |
| Alt text                | Content images have `alt`; the `iconUrl` project image uses `alt=""` as decorative |
| Viewport meta           | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` on all 12 pages |
| Hidden headings         | `music.html` keeps its `<h1>` in the DOM, visually hidden with a 1x1 clip, so the page has a heading for screen readers and search engines |

No ARIA roles are used beyond what is implicit in semantic HTML.

Known gaps, in the order they are worth fixing:

1. **No skip-to-content link** on any page.
2. ~~**The beat flash rate on `music.html` has never been measured** against WCAG 2.3.1.~~ **Measured in v2.9.3, and it failed.** The rate was frame-counted, so it scaled with refresh rate: 2.40 events per second at 60 Hz but **4.70 at 120 Hz and 5.60 at 144 Hz**, against a limit of three. Now 1.70 at every refresh rate. See Animation and Motion.
3. **`music.html` has not had a mobile audit.** The fixed console and fixed mode-control row were tuned for desktop viewports; behavior between 320 px and 480 px is unverified. This is tracked in the PRD's deferred list.
4. **Focus styles are browser defaults everywhere.** No custom `:focus-visible` ring is defined, so the outline on the accent-colored buttons is whatever the browser draws over a dark surface.

> **Closed in v2.8.7.** Earlier versions of this document listed the absence of any `@media (prefers-reduced-motion: reduce)` rule as the most serious accessibility gap on the site, and the absence of a pause control on `music.html` as the second. Both are fixed. See Animation and Motion below.

---

## Animation and Motion

All motion outside `music.html` is functional: it confirms interactivity. No decorative animation is used on any other page.

| Element            | Animation                                                   | Duration | Easing |
|--------------------|-------------------------------------------------------------|----------|--------|
| Project card       | `translateY(-2px)` plus box-shadow plus top gradient on hover | `0.2s` | default |
| Featured project card | `translateY(-4px)` plus box-shadow plus top gradient plus arrow slide on hover | `0.18s` | default |
| Explore card       | `translateY(-3px)` plus box-shadow plus top gradient plus arrow slide on hover | `0.2s` | default |
| Discord server card | `translateY(-2px)` plus box-shadow plus top gradient on hover | `0.2s` | default |
| Affiliate card     | `translateY(-3px)` plus box-shadow plus logo scale on hover  | `0.2s`   | default |
| Coffee button      | `translateY(-2px)` plus yellow glow on hover                 | `0.2s`   | default |
| Filter buttons     | Background and border color on hover and active              | `0.2s`   | default |
| Nav links          | Color on hover                                               | `0.2s`   | default |
| Status badge dot   | Opacity pulse (`1` to `0.3` and back), `@keyframes pulse`    | `2s`     | infinite |
| `music.html` canvas | Continuous scene render                                     | every frame | `requestAnimationFrame` |
| `music.html` favicon | Spoke redraw                                               | every 3rd frame | n/a |
| `music.html` screen mode | Random switch among the five visible modes             | every 1,800 frames | n/a |

Most transitions use the `transition: all 0.2s` shorthand. CSS `ease` is the browser default when no easing is named. Nothing on the site uses a custom cubic-bezier.

### Reduced motion

Added in v2.8.7. Two layers, because the two problems are different.

**Sitewide, in `styles.css`.** A `@media (prefers-reduced-motion: reduce)` block collapses every animation and transition to `0.01ms` and forces `transform: none` on hover. The hover lift disappears; the border and background color changes that carry the same affordance stay. Nothing in the table above communicates anything through movement alone, so nothing is lost.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    transition-delay: 0ms !important;
    scroll-behavior: auto !important;
  }
  *:hover { transform: none !important; }
}
```

**`music.html`, in the visualizer script.** A CSS media query cannot stop a `requestAnimationFrame` loop, so the page reads the same preference in JavaScript and gates the loop on it. A `.motion-btn` play/pause control sits at the left of the mode-button row, styled in `--accent` rather than the `--purple` used by the mode pills so it reads as a control over the whole scene rather than another mode.

The behavior:

| Visitor's preference | On load | Button reads |
|----------------------|---------|--------------|
| No preference | One frame painted, then the loop runs | Pause |
| `reduce` | One frame painted, then it holds still | Play |

The single frame is drawn before the loop is gated, so a paused stage shows the full scene (screens, booth, lasers, crowd) rather than an empty canvas. Pressing a mode button while paused redraws one frame so the change is visible without starting the animation, and a resize does the same. The preference is read once on load; a visitor who presses Play is not overridden if the OS setting changes mid-session.

Why a control rather than a hard freeze: WCAG 2.2.2 (Pause Stop Hide, Level A) requires a way to stop automatic motion that runs more than five seconds alongside other content, and the stage console sits directly over the visualizer. Freezing only for people who set the preference would have left that criterion unmet for everyone else. The control satisfies both at once.

**Rule for new motion:** if a movement does not tell the user that something is interactive or that state changed, it does not ship. `music.html` is the single, deliberate exception, and no second exception should be granted without a decision recorded in the PRD.

---

## Rules for Staying Consistent

1. Reuse an existing component pattern before inventing a new one. Most new sections are a grid of one of the six card types already documented above.
2. New shared colors go in `styles.css` as a token. A color used by exactly one page goes in that page's inline `:root`. A one-off brand tint may stay an inline `rgba()`.
3. Keep the `1100px` max width and the `2rem` / `1.25rem` horizontal padding pair. A section that sets its own width will visibly fail to line up with the nav.
4. Never hand-edit the nav in a page. Since v2.8.8 it is generated: add the page to `PAGES` in `tools/build-nav.py`, run the script, and commit the result. The script stamps the block between the `<!-- NAV -->` marker and `</nav>` in every root-level page and sets `class="active"` itself. A hand edit survives until the next run and then vanishes without warning. Verify with `python tools/build-nav.py --check`.
5. When a CSS value changes in the source, update the matching row in this document in the same commit. That rule predates this audit and is the reason the design system is still legible.
6. Match the existing dark palette. ~~There is no light theme and none is planned.~~ **Replaced 2026-10-02 (2.13.7):** every page has a light and a dark theme from one palette (One palette for the whole site); build new parts in both and check their contrast in both. (**2026-10-02:** true for the 12 root pages. Azqato Invests has both themes, and the PRD's Future updates bring its theme button to the whole site; PRD Documentation Versus Reality 39.)
