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

There is no CSS build step, no preprocessor, and no minification. `styles.css` is 2,282 bytes and is the only external stylesheet on any page.

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

Only `lang-js` and `lang-html` are currently in use by the `PROJECTS` array. The rest are defined ahead of need.

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

`music.html` is the only page with a non-trivial rendering layer, and it is large enough (91 KB, roughly 2,175 lines) that its visual rules belong here rather than being reverse-engineered from the source each time.

### Structure

- A single full-viewport `<canvas id="viz">` is `position: fixed`, `z-index: 0`, `pointer-events: none`, and painted every frame via `requestAnimationFrame`.
- `nav`, `.hero`, `.section`, and `footer` are lifted to `z-index: 1` so page chrome sits above the canvas.
- `.stage-console` is a `position: fixed` glass panel centered at `top: 13vh`, sized `clamp(280px, 38vw, 560px)` by `clamp(220px, 36vh, 460px)`, holding the two Mixcloud iframes and three platform links. It scrolls independently (`overflow-y: auto`) with a purple-tinted thin scrollbar. It is designed to read as content displayed on the stage's center screen.
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

### The visualizer is not audio-reactive

This is the single most important thing to know about the page, and it was previously documented nowhere. `music.html` declares `var analyser = null, freqData = null;` and never assigns either. The `freq(i)` helper therefore always takes its synthetic branch, generating a per-band value from three summed sine waves with per-band random phases, smoothed over time. Every "beat", laser burst, fire column, and screen pulse is procedural animation on a frame counter, not a response to the Mixcloud audio.

This is by design and should not be treated as a bug to fix. A browser cannot read audio out of a third-party iframe, and capturing system or other-tab audio was considered and declined. The paused `feature/native-audio-player` branch is the only path to genuine reactivity, because it plays the audio from the page itself.

### Dynamic favicon

Every third frame, `music.html` redraws a 32x32 canvas of twelve radial spokes colored `hsl(195 + f*65, 100%, 70%)` and assigns it to the page's `<link rel="icon">` as a data URL. The shared lion favicon is therefore only visible on this page for the first few frames. Every other page keeps the lion.

---

## Image Assets

All images live in `img/` at the project root. Profile and thumbnail images render with `object-fit: cover`; the About avatar is a circle (`border-radius: 50%`).

| File | Size | Referenced by |
|------|------|---------------|
| `about-profile.jpg` | 198 KB | `about.html` pitch card avatar |
| `yt-thumb-azqato.jpg` | 333 KB | `youtube.html` |
| `yt-thumb-streams.jpg` | 469 KB | `youtube.html` |
| `yt-thumb-mixes.jpg` | 854 KB | `youtube.html` |
| `yt-thumb-chills.jpg` | 659 KB | `youtube.html` |
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

The four `yt-thumb-*.jpg` files are the site's real performance outlier: `youtube.html` is 7.8 KB of HTML that pulls 2.3 MB of images. No lazy-loading attribute is set on them.

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
2. **The beat flash rate on `music.html` has never been measured** against WCAG 2.3.1, which allows no more than three flashes per second. The pause control added in v2.8.7 gives a visitor a way out, but it does not excuse the page from the criterion for anyone who has not pressed it.
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
4. Any new page copies the nav block verbatim from an existing page and moves the `class="active"` to its own link. There is no shared nav include yet.
5. When a CSS value changes in the source, update the matching row in this document in the same commit. That rule predates this audit and is the reason the design system is still legible.
6. Match the existing dark palette. There is no light theme and none is planned; do not add `prefers-color-scheme` handling.
