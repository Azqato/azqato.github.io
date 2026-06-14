# Design Document: Azqato Portfolio

## Design Philosophy

The portfolio uses a GitHub Dark-inspired aesthetic to signal developer credibility without requiring any explanation. The visual language is intentional: if it looks at home on github.com, it belongs here. Motion is used only to confirm interactivity, never for decoration. Every element defaults to the minimum necessary complexity.

The accent color is a teal-green (`#00d4a0`) that replaces the default GitHub blue and is used consistently across all primary interactive elements: links, active nav states, CTA buttons, card hover borders, and tag highlights.

---

## Color Palette

All colors are defined as CSS custom properties in the `:root` block of each page's `<style>` tag.

| Token             | Hex Value   | Intended Use                                                          |
|-------------------|-------------|-----------------------------------------------------------------------|
| `--bg`            | `#0d1117`   | Page background                                                       |
| `--surface`       | `#161b22`   | Card background, nav bar, pitch card                                  |
| `--border`        | `#30363d`   | All borders and dividers                                              |
| `--accent`        | `#00d4a0`   | Primary interactive color: links, active states, hover borders        |
| `--accent-hover`  | `#00e6b0`   | Hover state for accent-colored elements                               |
| `--green`         | `#3fb950`   | Status badge dot, success indicators                                  |
| `--purple`        | `#bc8cff`   | Secondary accent (role badge on About page, gradient pair)            |
| `--orange`        | `#ffa657`   | Tertiary accent, used sparingly                                       |
| `--text`          | `#e6edf3`   | Primary body text                                                     |
| `--text-muted`    | `#8b949e`   | Secondary text: descriptions, labels, captions, nav links             |
| `--card-hover`    | `#1c2128`   | Card background on hover                                              |
| `--tag-bg`        | `#21262d`   | Tag pill background                                                   |
| `--coffee`        | `#FFDD00`   | Buy Me a Coffee button background (`support.html` only)               |
| `--coffee-hover`  | `#FFE84D`   | Buy Me a Coffee button hover background (`support.html` only)         |
| `--discord`       | `#5865f2`   | Discord button background (`index.html` and `discord.html`)           |
| `--discord-hover` | `#4752c4`   | Discord button hover background (`index.html` and `discord.html`)     |

`--discord` and `--discord-hover` are defined on `index.html` (landing page Discord CTA) and `discord.html` (server card join buttons). They are not part of the global token set applied to all pages.

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

---

## Typography

The site uses the system font stack with no external font loading:

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
```

| Role              | Size                        | Weight | Color          | Notes                                |
|-------------------|-----------------------------|--------|----------------|--------------------------------------|
| Page heading (h1) | `clamp(2rem, 5vw, 3.5rem)`  | `800`  | `--text`       | Hero headline; fluid between viewports |
| Section heading   | `1.4rem`                    | `700`  | `--text`       | Section titles with left accent bar  |
| Card title        | `1rem`                      | `700`  | `--text`       | Links to demo or GitHub; hover: `--accent` |
| Body text         | `1rem`                      | `400`  | `--text`       | Paragraphs                           |
| Card description  | `0.85rem`                   | `400`  | `--text-muted` | Card body copy                       |
| Muted / caption   | `0.78rem`–`0.82rem`         | `400`  | `--text-muted` | Tags, labels, meta info, section meta |
| Nav links         | `0.9rem`                    | `400`  | `--text-muted` | Active state: `--accent`, weight `600` |
| Button text       | `0.9rem`                    | `600`  | contextual     | Varies by button type                |
| Tag pills         | `0.72rem`                   | `600`  | language color | Language and category tag pills      |

Line height: `1.6` for body text, `1.15` for hero headings.

---

## Spacing System

Spacing values used across the site:

| Use case                       | Value              |
|--------------------------------|--------------------|
| Hero padding (top)             | `5rem` (desktop), `3rem` (mobile) |
| Section padding (vertical)     | `1.5rem 2rem 3rem` |
| Card padding                   | `1.25rem`–`1.5rem` |
| Card gap in grid               | `1rem`             |
| Nav height                     | `60px`             |
| Nav padding                    | `0 2rem`           |
| Inline element gap (small)     | `0.35rem`–`0.5rem` |
| Inline element gap (medium)    | `0.75rem`          |
| Inline element gap (large)     | `1rem`             |
| Tag / badge padding            | `0.18rem 0.6rem`–`0.25rem 0.75rem` |
| Border radius (cards)          | `10px`             |
| Border radius (tags / badges)  | `999px`            |
| Border radius (buttons)        | `6px`              |

Max content width: `1100px`, centered with `margin: 0 auto` on `.nav-inner`, `.hero`, and `.section`.

---

## Breakpoints

| Breakpoint        | Width      | Changes                                                           |
|-------------------|------------|-------------------------------------------------------------------|
| Mobile            | `< 600px`  | Nav links hidden (logo only visible); hero and section padding reduced; some grids collapse to one or two columns |
| Tablet / Desktop  | `>= 600px` | Full nav; multi-column grids                                      |

Project and server card grids use `CSS Grid` with `auto-fill` and `minmax(280px–300px, 1fr)`. Column count adjusts automatically; no discrete grid breakpoints beyond the global 600 px threshold.

---

## Component Patterns

### Project Card (`projects.html`)

- Background: `--surface`; hover background: `--card-hover`
- Border: `1px solid --border`; hover: `border-color: --accent`
- Border radius: `10px`
- Top-edge gradient on hover: `linear-gradient(90deg, --accent, --purple)`, `height: 2px`, `opacity: 0` default, `1` on hover
- Hover transform: `translateY(-2px)` + `box-shadow: 0 8px 24px rgba(0, 212, 160, 0.08)`
- Transition: `all 0.2s`
- Card padding: `1.25rem`; internal gap: `0.75rem`
- Hidden cards use `data-hidden="true"` to toggle display: none via CSS attribute selector

### Discord Server Card (`discord.html`)

- Same base as project cards but hover uses `--discord` border and shadow tint
- Top-edge gradient: `linear-gradient(90deg, --discord, --purple)`
- Hover box-shadow: `0 8px 24px rgba(88, 101, 242, 0.12)`
- Card padding: `1.5rem`; internal gap: `1rem`
- Icon: `2rem` emoji at the top left of the card header
- Join button: full-width, `--discord` background, white text, Discord SVG logo inline

### Navigation Bar

- Background: `rgba(13, 17, 23, 0.85)` with `backdrop-filter: blur(12px)`
- Border: `1px solid --border` (bottom)
- Sticky: `position: sticky; top: 0; z-index: 100`
- Height: `60px`
- Logo: `--text`, `1.15rem`, `700` weight; accent dot on trailing period
- Nav links: `--text-muted`; hover: `--text`; active: `--accent`, `600` weight
- Hidden on `< 600px` via `display: none` on `.nav-links`

### Hero Section

- Max width: `1100px`, centered
- Desktop padding: `5rem 2rem 1.5rem`
- Gap between hero elements: `1rem`
- Headline: `clamp(2rem, 5vw, 3.5rem)`, `800` weight, `letter-spacing: -0.5px`
- Description: `1.1rem`, `--text-muted`, `max-width: 560px`
- Status badge: pill with pulsing green dot, `--tag-bg` background, `--border` border

### Section Title

- Font size: `1.4rem`, weight `700`
- Left accent bar: `3px wide`, `1.2em tall`, `--accent` background, `2px border-radius`
- Rendered via `::before` pseudo-element with flexbox alignment

### Buttons

| Variant    | Background    | Border         | Text        | Use case                              |
|------------|---------------|----------------|-------------|---------------------------------------|
| Primary    | `--accent`    | `--accent`     | `#0d1117`   | Main CTAs                             |
| Secondary  | transparent   | `--border`     | `--text`    | Secondary actions; hover: `--accent` border |
| Coffee     | `--coffee`    | `--coffee`     | `#1a1a1a`   | Buy Me a Coffee only                  |
| Discord    | `--discord`   | `--discord`    | `#ffffff`   | Discord join buttons                  |
| Icon button | `--surface`  | `--border`     | `--text-muted` | Card action icons (GitHub, ↗)      |
| Join (full-width) | `--discord` | `--discord` | `#ffffff` | Discord server card join button      |

All buttons: `border-radius: 6px`, `padding: 0.55rem–0.6rem 1.2rem`, `font-size: 0.9rem`, `font-weight: 600`, `transition: all 0.2s`.

### Tag Pills

- Category tags: `--tag-bg` background, `--border` border, `--text-muted` text, `0.72rem`, `600` weight, `999px` border-radius
- Language tags: same shape with language-specific background, border, and text colors (see Language Tag Colors above)
- First tag on a card gets the `langClass` color if set

### Affiliate Card (`support.html`)

- Same base as project cards
- Logo area: fixed-size square, centered, brand-specific background color
- Promo badge: accent-colored pill
- Description: `--text-muted`, `0.9rem`
- CTA button: primary style

---

## Image Assets

All images live in `img/` at the project root.

| File                              | Use                                               |
|-----------------------------------|---------------------------------------------------|
| `home-hero-profile.jpg`           | Hero avatar on the landing page (`index.html`)    |
| `about-profile.jpg`               | Pitch card avatar on `about.html`                 |
| `logo-cat-avatar.jpg`             | Original site logo (available for reuse)          |
| `yt-thumb-azqato.jpg`             | YouTube thumbnail for Azqato channel              |
| `yt-thumb-streams.jpg`            | YouTube thumbnail for Azqato Streams              |
| `yt-thumb-mixes.jpg`              | YouTube thumbnail for Azqato Mixes                |
| `yt-thumb-chills.jpg`             | YouTube thumbnail for Azqato Chills               |
| `yt-channel-azqato.jpg`           | Larger YouTube channel image for Azqato           |
| `yt-channel-streams.jpg`          | Larger YouTube channel image for Azqato Streams   |
| `yt-channel-mixes.jpg`            | Larger YouTube channel image for Azqato Mixes     |
| `yt-channel-chills.jpg`           | Larger YouTube channel image for Azqato Chills    |
| `music-playlist-bangers.jpg`      | Spotify playlist cover for BANGERS                |
| `music-playlist-addictions.jpg`   | Spotify playlist cover for ADDICTIONS             |
| `music-logo-small.jpg`            | Small music logo (available for reuse)            |

Profile photos render as circles: `border-radius: 50%`, `object-fit: cover`.

---

## Accessibility Standards

Target: WCAG 2.1 Level AA where achievable within a zero-dependency constraint.

| Requirement             | Implementation                                                         |
|-------------------------|------------------------------------------------------------------------|
| Color contrast          | `--text` (`#e6edf3`) on `--bg` (`#0d1117`): ~15:1 ratio              |
| Muted text contrast     | `--text-muted` (`#8b949e`) on `--bg` (`#0d1117`): ~4.8:1 (AA normal text) |
| Semantic markup         | `<nav>`, `<section>`, `<footer>`, `<h1>`/`<h2>` hierarchy used throughout |
| Link clarity            | All links visually distinct (accent color + hover state)              |
| Button labels           | All buttons have visible text                                         |
| Keyboard navigation     | Standard browser tab order; no custom focus traps                     |
| Focus indicators        | Browser default focus ring preserved                                  |
| Alt text                | Avatar images have `alt` attributes; decorative icons have empty `alt=""` |
| Viewport meta           | `<meta name="viewport" content="width=device-width, initial-scale=1">` on all pages |

No ARIA roles are used beyond what is implicit in semantic HTML.

Known gap: `@media (prefers-reduced-motion: reduce)` is not currently implemented. The animations are subtle (2px translate, color transitions) and unlikely to cause issues, but adding a rule to disable transforms for users who prefer reduced motion would be the correct fix.

---

## Animation and Motion

All motion is functional: it confirms interactivity. No decorative animations.

| Element            | Animation                                                   | Duration | Easing |
|--------------------|-------------------------------------------------------------|----------|--------|
| Project card       | `translateY(-2px)` + box-shadow + top gradient on hover     | `0.2s`   | default |
| Discord server card | `translateY(-2px)` + box-shadow + top gradient on hover   | `0.2s`   | default |
| Affiliate card     | `translateY(-2px)` + box-shadow on hover                    | `0.2s`   | default |
| Filter buttons     | Background and border color on hover and active             | `0.2s`   | default |
| Nav links          | Color on hover                                              | `0.2s`   | default |
| All buttons        | Background and border color on hover                        | `0.2s`   | default |
| Status badge dot   | Opacity pulse (`1` to `0.3` and back), `@keyframes pulse`  | `2s`     | infinite |

All transitions use `transition: all 0.2s` shorthand. CSS `ease` is the browser default when no easing is specified.
