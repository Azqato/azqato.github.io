# Design System — azqato.com Old Website

Documented from screenshots (4 pages) and live page analysis. This is the source of truth for recreating the original visual design in vanilla HTML/CSS/JS.

---

## Color Palette

| Token | Value | Usage |
|---|---|---|
| `--bg` | `#000000` | Page background (pure black) |
| `--nav-bg` | `#000000` | Navigation bar background |
| `--text` | `#ffffff` | Primary text, headings, nav links |
| `--text-muted` | `#cccccc` | Secondary / body paragraph text |
| `--btn-bg` | `#6666cc` | Button fill (purple-blue, approx.) |
| `--btn-text` | `#ffffff` | Button label text |
| `--link` | `#7777dd` | Inline hyperlinks (blue-purple) |
| `--link-visited` | `#9966cc` | Visited links |
| `--footer-text` | `#888888` | Footer disclaimer text |
| `--footer-bg` | `#000000` | Footer background |
| `--nav-active` | `#ffffff` | Active nav item (bold white) |
| `--nav-inactive` | `#cccccc` | Inactive nav items |
| `--channel-border` | `#00ff00` | Green ring on active YouTube channel thumbnail |

> Note: Button and link colors are approximated from screenshots. Exact hex values should be verified with a color picker against the live site before the domain migrates.

---

## Typography

| Context | Properties |
|---|---|
| Body font | Sans-serif (Google Sites default — likely Roboto or system sans-serif) |
| Page heading (h1) | Large, bold, white, centered (e.g. "Welcome to Azqato.com!") |
| Section heading (h2) | Medium, bold, white (e.g. "About Azqato", "Azqato's Links") |
| Pronunciation subheading | Italic, medium weight (e.g. "Azz - Kah - Toe") |
| Body paragraphs | ~16px, normal weight, muted white |
| Button labels | ~14–15px, bold, white, uppercase or title case |
| Footer text | ~12px, gray, normal weight, bulleted list |
| Nav links | ~14px, normal weight; bold when active |
| Channel names (YouTube page) | ~14px, blue link color, underlined |

---

## Layout

### Global Shell

```
┌─────────────────────────────────────────┐
│  [cat icon] Azqato   Home About Links YouTube [🔍] │  ← sticky nav
├─────────────────────────────────────────┤
│                                         │
│            [page content]               │
│                                         │
├─────────────────────────────────────────┤
│  • Privacy Policy                       │  ← footer
│  • Disclaimer — affiliate disclosure    │
│  • Not a financial advisor              │
│  • Entertainment purposes only          │
└─────────────────────────────────────────┘
```

- Max content width: ~1100–1200px, centered
- Page background: pure black full bleed

---

### Nav Bar

```
[cat icon] Azqato          Home   About   Links   YouTube   🔍
```

- Full-width black bar
- Logo on far left: small circular cat avatar + "Azqato" wordmark
- Nav links on far right, horizontally spaced
- Active page: bold white text
- Inactive pages: lighter gray text
- Search icon (🔍) on far right
- No visible border or divider line between nav and content

---

### Home Page Layout

```
┌──────────────────────────────────────────────┐
│           Welcome to Azqato.com!             │  ← centered h1
│                                              │
│  [profile image]    About Azqato             │
│                     [bio text with links]    │  ← 2-col hero
│                                              │
│  [Discord] [Twitch] [Patreon] [Subscribe] [B5TA] [Support]   │  ← button row
│  [YouTube] [Azqato] [Mixes]   [Streams]  [Chills]  [Twitter] │
│  [Music]   [Last.fm][Mixcloud][Reddit]   [Accounts][Facebook] │
│  [Invests] [M1 Finance][Public.com][Instagram][Tumblr][Medium]│
└──────────────────────────────────────────────┘
```

- H1 centered at top
- Hero: two-column row — image left, text right; roughly equal width columns
- Button grid: 6 columns × 4 rows
- Buttons have consistent size and spacing
- Grid is centered on page

---

### About Page Layout

```
┌──────────────────────────────────────────────┐
│               About Azqato                  │  ← centered h1
│                                              │
│  [profile image]    Azz - Kah - Toe         │
│                     [paragraph 1]           │  ← 2-col hero
│                                              │
│  [paragraph 2 — full width]                 │
│  [paragraph 3 — full width, with links]     │
│  [paragraph 4 — full width]                 │
└──────────────────────────────────────────────┘
```

- H1 centered
- Hero two-column: image left, pronunciation + first paragraph right
- Remaining paragraphs below in full-width single column

---

### Links Page Layout

```
┌──────────────────────────────────────────────┐
│             Azqato's Links                  │  ← centered h1
│                                              │
│  [Discord]  [Patreon]  [Twitch]  [Subscribe]  [B5TA]  [Last.fm]  │
│  [YouTube]  [Azqato]   [Mixes]   [Streams]  [Chills]  [Mixcloud] │
│  [Instagram][Music]    [Twitter] [Reddit]  [Accounts][Facebook]  │
│  [Invests]  [M1 Finance][Public.com][Discord][Tumblr][Medium]    │
└──────────────────────────────────────────────┘
```

- No hero section — heading directly followed by button grid
- Same 6-column × 4-row grid as home page
- Grid is centered on page

---

### YouTube Page Layout

```
┌──────────────────────────────────────────────┐
│         Azqato's Youtube Channels           │  ← centered h1
│                                              │
│  [thumb]   [thumb]   [thumb]   [thumb]      │  ← 4 channel images
│  Azqato  AzqatoStreams AzqatoMixes AzqatoChills │  ← links below each
└──────────────────────────────────────────────┘
```

- 4 equal-width cards in a single row
- Each card: square thumbnail image + channel name as a hyperlink below
- First channel (Azqato) has a bright green circular border ring on the thumbnail image
- Thumbnails appear to be YouTube channel art / banner crops (square-ish)

---

### Invests Page Layout

- Heading "Azqato Invests"
- Intro paragraph + Discord community description
- Sections with headings (Platforms, Careers, ETFs, Companies, Ratings, Screeners, Real Estate, Charts, Databases, Economic Indicators, Education, Guides, Indices, Information, News)
- Each section contains a list of hyperlinks
- Standard inline link styling (blue-purple, underlined)

---

### Music Page Layout

- Heading "Music"
- Short intro text
- Two playlist cards (BANGERS, ADDICTIONS) — each with name, subtitle, and Spotify link
- Possibly embedded Spotify widgets (Google Sites supports iframes)

---

## Components

### Navigation Bar

- Black background, full width
- Logo: circular cat avatar image + "Azqato" text beside it
- Nav links: right-aligned, horizontal list
- Active state: `font-weight: bold; color: #fff`
- Inactive state: `color: #cccccc`
- Search icon: far right, clickable

### Button

```css
.btn {
  background: #6666cc;        /* approx — verify */
  color: #ffffff;
  border: none;
  border-radius: 4–6px;       /* slightly rounded */
  padding: 10px 16px;
  font-weight: bold;
  font-size: 14–15px;
  cursor: pointer;
  text-decoration: none;
  display: inline-block;
  min-width: ~130px;
  text-align: center;
}

.btn:hover {
  /* slight brightness increase or slight darken — not confirmed */
}
```

- Buttons are anchor tags styled as buttons (links that look like buttons)
- Consistent height and width across grid
- All caps or title case labels

### Hero Two-Column Section

```css
.hero {
  display: flex;
  align-items: flex-start;
  gap: 2–3rem;
  max-width: 900px;
  margin: 0 auto;
}

.hero img {
  width: ~300px;
  height: ~300px;
  object-fit: cover;
}
```

### Button Grid

```css
.btn-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 8–12px;
  max-width: ~900px;
  margin: 2rem auto;
}
```

### YouTube Channel Card

```css
.channel-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.channel-thumb {
  width: ~180px;
  height: ~180px;
  object-fit: cover;
}

/* First card only */
.channel-thumb--active {
  border: 3px solid #00ff00;
  border-radius: 50%;
}
```

### Footer

```css
footer {
  background: #000;
  padding: 1.5rem 2rem;
  color: #888888;
  font-size: 12px;
}

footer ul {
  list-style: disc;
  padding-left: 1.5rem;
}

footer a {
  color: #7777dd;
  text-decoration: underline;
}
```

---

## Spacing & Sizing

| Element | Value |
|---|---|
| Page max-width | ~1100–1200px |
| Hero image size | ~280–320px square |
| Button grid gap | ~8–12px |
| Button min-width | ~120–140px |
| Section padding (vertical) | ~2–3rem |
| Nav height | ~50–60px |
| Footer padding | ~1.5rem 2rem |
| YouTube channel thumbnail | ~180px square |

---

## Responsive Behavior

The original Google Sites site has limited responsive behavior. On mobile:
- Nav collapses (Google Sites handles this natively via its mobile menu)
- Button grid likely stacks or reduces columns
- Hero two-column drops to single column

For the vanilla rebuild, target desktop-first with a basic mobile breakpoint at ~600px.

---

## Assets Needed

| Asset | Source | Notes |
|---|---|---|
| Cat avatar / logo | Google Sites CDN | Need to re-host or replace |
| Home hero profile image | Google Sites CDN | Need to re-host or replace |
| About profile image | Google Sites CDN | Different image from home |
| YouTube channel thumbnails (4) | YouTube API or screenshot | Can fetch from YouTube directly |
| Favicon | Same cat avatar | Circular crop |

> All original images are hosted on `lh3.googleusercontent.com/sitesv/` and will break once the domain migrates away from Google Sites. Images must be saved and self-hosted.
