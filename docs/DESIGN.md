# Design Document: Azqato Portfolio

## Design Philosophy

The portfolio uses a GitHub Dark-inspired aesthetic to signal developer credibility without requiring any explanation. The visual language is intentional: if it looks at home on github.com, it belongs here. Motion is used only to confirm interactivity, never for decoration, and every element defaults to the minimum necessary complexity.

The accent color follows the same brand green used across Azqato's projects (see [Net Worth Tracker design system](https://github.com/Azqato/net-worth-tracker/blob/main/docs/DESIGN.md)): a teal-green (`#00d4a0`) that replaces the previous GitHub blue. Green is used for all primary interactive elements: links, active nav states, CTA buttons, card hover borders, and tag highlights.

---

## Color Palette

All colors are defined as CSS custom properties in the `:root` block of each page's `<style>` tag.

| Token            | Hex Value   | Intended Use                                      |
|------------------|-------------|---------------------------------------------------|
| `--bg`           | `#0d1117`   | Page background                                   |
| `--surface`      | `#161b22`   | Card background, nav bar, pitch card              |
| `--border`       | `#30363d`   | All borders and dividers                          |
| `--accent`       | `#00d4a0`   | Primary interactive color (links, active states)  |
| `--accent-hover` | `#00e6b0`   | Hover state for accent-colored elements           |
| `--green`        | `#3fb950`   | "Available" status badge, success states          |
| `--purple`       | `#bc8cff`   | Secondary accent (role badge on About page)       |
| `--orange`       | `#ffa657`   | Tertiary accent (used sparingly)                  |
| `--text`         | `#e6edf3`   | Primary body text                                 |
| `--text-muted`   | `#8b949e`   | Secondary text (descriptions, labels, captions)   |
| `--card-hover`   | `#1c2128`   | Card background on hover                          |
| `--tag-bg`       | `#21262d`   | Tag pill background                               |
| `--coffee`       | `#FFDD00`   | Buy Me a Coffee button background                 |
| `--coffee-hover` | `#FFE84D`   | Buy Me a Coffee button hover background           |
| `--discord`      | `#5865f2`   | Discord button background (landing page CTA)      |
| `--discord-hover`| `#6b76f5`   | Discord button hover background                   |

The `--discord` and `--discord-hover` tokens are defined only on the landing page (`index.html`), where the Discord join is the primary call to action.

### Language Tag Colors

Language tags use inline color values, not CSS custom properties:

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

The site uses the system font stack with no external font loading.

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
```

| Role              | Size       | Weight  | Color           | Notes                          |
|-------------------|------------|---------|-----------------|--------------------------------|
| Page heading (h1) | `2.5rem`   | `700`   | `--text`        | Hero headline                  |
| Section heading   | `1.5rem`   | `600`   | `--text`        | Section titles                 |
| Card title        | `1.1rem`   | `600`   | `--accent`      | Links to demo or GitHub        |
| Body text         | `1rem`     | `400`   | `--text`        | Paragraphs and card descriptions |
| Muted / caption   | `0.875rem` | `400`   | `--text-muted`  | Tags, labels, meta info        |
| Nav links         | `0.9rem`   | `400`   | `--text-muted`  | Active state: `--accent`       |
| Button text       | `0.9rem`   | `500`   | contextual      | Varies by button type          |
| Code / tag        | `0.75rem`  | `500`   | language color  | Language tag pills             |

Line height defaults to `1.6` for body text, `1.3` for headings.

---

## Spacing System

The site does not use a strict spacing scale library. Spacing values used in practice:

| Use case                   | Value     |
|----------------------------|-----------|
| Section padding (vertical) | `3rem`    |
| Card padding               | `1.5rem`  |
| Card gap in grid           | `1.5rem`  |
| Nav padding                | `1rem 2rem` |
| Inline element gap (small) | `0.5rem`  |
| Inline element gap (large) | `1rem`    |
| Tag/badge padding          | `0.25rem 0.6rem` |
| Border radius (cards)      | `12px`    |
| Border radius (tags/badges) | `20px`   |
| Border radius (buttons)    | `6px–8px` |

---

## Breakpoints

| Breakpoint     | Width     | Changes                                                        |
|----------------|-----------|----------------------------------------------------------------|
| Mobile         | `< 600px` | Nav links hidden (logo and GitHub button only visible in nav)  |
| Tablet / Desktop | `≥ 600px` | Full nav links visible; project grid switches to multi-column  |

The project grid uses `CSS Grid` with `auto-fill` and `minmax(300px, 1fr)`, so column count adjusts automatically based on viewport width without discrete breakpoints for the grid itself.

The affiliate card grid on `support.html` uses `minmax(250px, 1fr)`, following the same pattern.

---

## Component Patterns

### Project Card

- Background: `--surface`; hover background: `--card-hover`
- Border: `1px solid --border`; hover border: `1px solid --accent` with `opacity: 0.5`
- Border radius: `12px`
- Hover: `transform: translateY(-3px)` + `box-shadow` with accent tint + a 3px top-edge gradient using `--accent`
- Transition: `all 0.2s ease`
- Icon area: `48px × 48px`, rounded (`12px`), background `--tag-bg`
- Title: accent color, `text-decoration: none`; hover: underline
- Tags: pill shape, `--tag-bg` background, `--text-muted` text, `0.75rem`
- Language tag: pill with language-specific color
- Action buttons: `--surface` background, `--border` border; hover: `--accent` border + text

### Navigation Bar

- Background: `--surface`; border-bottom: `1px solid --border`
- Sticky (`position: sticky; top: 0; z-index: 100`)
- Logo: `--text` color, `font-size: 1.1rem`, `font-weight: 600`
- Nav links: `--text-muted`; hover: `--text`; active: `--accent`
- Hidden on `< 600px` via `display: none` on `.nav-links`
- Max content width: `1200px`, centered with `margin: 0 auto`

### Hero Section

- Status badge: small pill with colored dot (green for "available", purple for role)
- Headline: `2.5rem`, `700` weight, `--text`
- Bio text: `1.1rem`, `--text-muted`
- CTAs: primary button (`--accent` background, white text) + secondary button (outlined, `--accent` border)

### Buttons

| Variant     | Background   | Border        | Text          | Use case                    |
|-------------|--------------|---------------|---------------|-----------------------------|
| Primary     | `--accent`   | none          | `#0d1117`     | Main CTAs                   |
| Outlined    | transparent  | `--accent`    | `--accent`    | Secondary actions            |
| Coffee      | `--coffee`   | none          | `#1a1a1a`     | Buy Me a Coffee only         |
| Discord     | `--discord`  | none          | `#ffffff`     | Join the Discord CTA (landing page hero and closing band) |
| Affiliate   | `--accent`   | none          | `#0d1117`     | Affiliate card CTA buttons   |
| Icon button | `--surface`  | `--border`    | `--text-muted` | Card action icons (GitHub, ↗) |

All buttons: `border-radius: 6px–8px`, `padding: 0.6rem 1.2rem`, `cursor: pointer`, `transition: all 0.2s`.

### Affiliate Card

- Same card base as project cards (surface background, border, border-radius, hover lift)
- Logo area: `100px × 100px`, centered, with brand-specific background color and large emoji/text logo
- Promo badge: accent-colored pill at top of card
- Description: `--text-muted`, `0.9rem`
- CTA button: primary style

---

## Image Assets

Image assets live in `img/` at the project root. All images were migrated from the old azqato.com website.

| File                            | Use                                              |
|---------------------------------|--------------------------------------------------|
| `home-hero-profile.jpg`         | Hero avatar on `projects.html`                   |
| `about-profile.jpg`             | Pitch card avatar on `about.html`                |
| `logo-cat-avatar.jpg`           | Original site logo (available for reuse)         |
| `yt-thumb-azqato.jpg`           | YouTube channel thumbnail for Azqato             |
| `yt-thumb-streams.jpg`          | YouTube channel thumbnail for Azqato Streams     |
| `yt-thumb-mixes.jpg`            | YouTube channel thumbnail for Azqato Mixes       |
| `yt-thumb-chills.jpg`           | YouTube channel thumbnail for Azqato Chills      |
| `yt-channel-azqato.jpg`         | Larger YouTube channel image for Azqato          |
| `yt-channel-streams.jpg`        | Larger YouTube channel image for Azqato Streams  |
| `yt-channel-mixes.jpg`          | Larger YouTube channel image for Azqato Mixes    |
| `yt-channel-chills.jpg`         | Larger YouTube channel image for Azqato Chills   |
| `music-playlist-bangers.jpg`    | Spotify playlist cover for BANGERS               |
| `music-playlist-addictions.jpg` | Spotify playlist cover for ADDICTIONS            |
| `music-logo-small.jpg`          | Small music logo (available for reuse)           |

Profile photos and thumbnails are rendered as circles via `border-radius: 50%` and `object-fit: cover`.

---

## Accessibility Standards

**Target:** WCAG 2.1 Level AA where achievable within a no-dependency constraint.

| Requirement               | Implementation                                                     |
|---------------------------|---------------------------------------------------------------------|
| Color contrast            | `--text` (`#e6edf3`) on `--bg` (`#0d1117`) = ~15:1 ratio          |
| `--text-muted` contrast   | `#8b949e` on `#0d1117` = ~4.8:1 (meets AA for normal text)        |
| Semantic markup           | `<nav>`, `<main>`, `<section>`, `<footer>`, `<h1>`/`<h2>` hierarchy |
| Link clarity              | All links are visually distinct (accent color + hover underline)   |
| Button labels             | All buttons have visible text labels                               |
| Keyboard navigation       | Standard browser tab order; no custom focus traps                  |
| Focus indicators          | Browser default focus ring (not removed)                           |
| Alt text                  | Avatar image on About page has alt text                            |
| Viewport meta             | `<meta name="viewport" content="width=device-width, initial-scale=1">` |

No ARIA roles are used beyond what is implicit in semantic HTML.

---

## Animation and Motion

All motion is functional: it confirms interactivity and directs attention. No decorative animations.

| Element          | Animation                                          | Duration   | Easing    |
|------------------|----------------------------------------------------|------------|-----------|
| Project card     | `translateY(-3px)` + box-shadow on hover           | `0.2s`     | `ease`    |
| Affiliate card   | `translateY(-3px)` + box-shadow on hover           | `0.2s`     | `ease`    |
| Filter buttons   | Background/border color transition on hover/active | `0.2s`     | `ease`    |
| Nav links        | Color transition on hover                          | `0.2s`     | `ease`    |
| All buttons      | Background/border color transition on hover        | `0.2s`     | `ease`    |

Motion is not reduced for `prefers-reduced-motion` currently. This is a known gap. The animations are subtle enough (3px translate, color transitions) that they are unlikely to cause issues, but a `@media (prefers-reduced-motion: reduce)` rule disabling transforms would be the correct fix.
