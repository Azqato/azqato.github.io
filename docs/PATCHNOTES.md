# Patch Notes

All notable changes to the Azqato Portfolio are documented here.
Format: `[version] - YYYY-MM-DD`

---

## [2.8.10] - 2026-08-29

### Added: the visualizer now reacts to real audio
- Added a native track player to the top of the `music.html` stage console: one same-origin file (`audio/womanchild-azqato-remix.mp3`, 6.1 MB, 4:46), with a play/pause button, title, elapsed and total time, and a draggable scrub bar. The two Mixcloud embeds and all three platform links are untouched and sit below it.
- Wired the track through a Web Audio `AnalyserNode` (fftSize 256, smoothing 0.8). While it plays, `freq()` reads real frequency data and the lasers, fire columns, screen pulses, crowd, and animated favicon follow the music. This is the first time anything on the site has responded to audio.
- Kept the synthetic three-sine signal as the fallback, and it is a fallback rather than a failure state. It runs when the track is paused, when it has never been started, and when a Mixcloud embed is playing. A paused element reads as silence, so falling through to the analyser would flatten the stage rather than idle it. Both branches share the same `0.72 / 0.28` smoothing, so the handover at play and pause is continuous rather than a jump.

### Technical notes
- Band `i` reads analyser bin `floor((i / 64) * bins * 0.8)`. The top fifth of the spectrum is skipped because it is nearly always empty and would otherwise waste a fifth of the bands on silence.
- Raw amplitudes are raised to the power 1.6 before smoothing. Without that curve most tracks sit inside a narrow loudness band and the stage reads as uniformly bright rather than dynamic. The exponent is ported from `feature/native-audio-player`, where it was tuned against a real track.
- The `AudioContext` is created lazily inside the play button's click handler, not at load. Browsers refuse to start one outside a user gesture, and creating it up front would leave a suspended context that never resumes.
- `createMediaElementSource` is called exactly once and guarded by an `audioWired` flag, because a second call on the same element throws. If it does throw, the error is logged and `analyser` is reset to null, which degrades the page to the synthetic signal instead of breaking playback.
- `preload="metadata"` rather than `none`. With `none` the duration stayed at `0:00` until first play, so the scrub bar had no range to show.
- Removed the `analyser` and `freqData` dead declarations, which had been declared and never assigned since the visualizer was written. They are now real. The Known Technical Debt row and the deferred cleanup item that tracked them are both gone.

### Known limitation
- **The stage is driven by the audio but does not yet read as reacting to it.** Confirmed on the first real listen: the kick does not land, and you cannot tell a drum hit from a pad by watching. Scoped as milestone v2.9.1 with six hypotheses to measure before changing anything, chief among them that the analyser's 0.8 smoothing and `freq()`'s own `0.72 / 0.28` are two low-pass filters in series and a kick is a transient. The onset-based kick detector already sitting on `feature/native-audio-player` exists because a raw analyser level does not give you a kick, and is pulled forward into that milestone.

### Fixed
- Skip Web Audio entirely when the page is opened over `file://`. The browser treats a same-folder mp3 as cross-origin there, so `createMediaElementSource` succeeds, reroutes the element, and outputs silence with no error thrown. The track appeared to play with the timer running and no sound. The page now checks `location.protocol` and leaves the element unrouted on a local file, so playback is audible and the stage runs synthetic. Serve over http to get the real path.

### Documentation
- Rewrote the "The visualizer is not audio-reactive" section of `docs/DESIGN.md` and the "signal driving the visualizer" section of `docs/PRD.md`. Both were correct when written and are now false. The replacement text is explicit about which of the three playback situations gets which signal, because the interesting case is the one that has not changed: a visitor playing a Mixcloud mix still sees choreography, not reaction, and no browser will ever let that page read cross-origin iframe audio.
- Added F19 (Native Track Player) to the feature list, updated F14 and F15, and added `audio/` to the folder tree and the public surface table.
- Marked steps 2 through 4 of milestone v2.9.0 as done and restated what the milestone is now: replacing the Mixcloud embeds, which is gated on the remaining audio files rather than on code. Five features are still unmerged on `feature/native-audio-player`: the `<video>` element, the onset-based kick detector, the beat-synced screen pulse, the loud-moment flash, and the Video screen mode. The beat flash needs measuring against WCAG 2.3.1 before it can ship.
- Recorded the sizing answer the milestone was waiting on: 6.1 MB for a 4:46 track at 192 kbps, so a handful of tracks fits in the repository and GitHub Pages serves them like any other asset. No object storage needed.
- Updated the `music.html` page weight from 91 KB to 99 KB everywhere it appears in the constraints, success criteria, technical debt, tenets, and working-practice sections. It remains the one acknowledged exception to the 50 KB budget.
- Noted that the zero-external-request caveat did **not** move. The player was added beside the embeds, not in place of them, so every "except `music.html`" qualifier still stands.

---


## [2.8.9] - 2026-08-29

### Fixed: dead demo link on the Leveraged Strategies card
- Fixed the Leveraged Strategies card in `projects.html`, which pointed its demo link at `azqato.github.io/leveraged-strategies/`. That URL returns a hard 404 and has since the project was renamed. Both the `demo` and `github` fields now point at `leverage`.
- Verified against the live web rather than assumed: `/leverage/` serves the page titled "Leveraged Strategies", `/leveraged-strategies/` returns 404, and the GitHub API resolves `Azqato/leveraged-strategies` to `Azqato/leverage`. GitHub redirects renamed repositories, which is why the `github` link still worked, but GitHub Pages does not redirect Pages URLs, which is why the demo link did not. Patch note 2.6.12 moved `invests.html` to the new URL and missed `projects.html`.
- No compatibility entry was added at the old path, because no repository serves it and there is nowhere to put one.

### Removed
- Removed `wrangler.jsonc`. It described a complete Cloudflare Workers deploy target, arrived on 2026-07-09 via the only pull request in this repository's history (a Cloudflare autoconfiguration integration), and was never used for a real deploy. An untested deploy path implies a safety net nobody has checked. The site is plain files and moves to any static host with no configuration, so nothing was lost.
- Removed the wrangler-specific patterns from `.gitignore` (`.wrangler`, `.dev.vars*`) along with the config they belonged to. The defensive `.env*` exclusion stays.
- Removed `.vscode/recentfedsummary.MD`, a personal summary of a finance video that was tracked in git, unrelated to the site, and the only remaining source of em-dash violations in the repository. Setting aside the exempt lines where a rule names the character it prohibits, the project is now fully compliant with its own writing policy.

### Changed
- Milestone v2.9.0 is no longer blocked. It was waiting on somewhere to host audio; the owner is supplying standalone audio files to be played directly on the page. The milestone grew in scope as a result: it now replaces the two Mixcloud iframes rather than adding a player beside them, and it is the next substantial piece of work on the site.
- Rewrote the Current Phase section of `docs/PRD.md`, which described the project as being in maintenance with a paused branch and a half-finished milestone. None of that is true any more. It now names v2.9.0 as next and lists the six remaining defect items with their sizes.

### Documentation
- Closed open questions 1 through 5 in `docs/PRD.md`. Each keeps its original text struck through with the answer beside it, per the documentation process, rather than being deleted. Questions 6, 7, and 8 remain, and question 8 is partly closed by v2.8.7.
- Recorded a standing rule in `docs/PRD.md` (Never Do These) and `docs/DESIGN.md` (Image Assets): **nothing in `img/` is ever deleted unless the owner asks for that file by name.** Unreferenced is the normal state of that folder, which is a working asset library rather than build output. The removal policy's plain internal delete does not apply there, and future audits should stop raising it. The corresponding Known Technical Debt row and deferred item were reworded from open questions into settled decisions.
- Updated the three Documentation Versus Reality rows that these answers resolve (15, 16, and 19) with what was decided and why.
- Removed every reference to Cloudflare Workers and `wrangler.jsonc` from the tech stack, folder tree, environments table, alternative hosts table, public surface table, security section, and internal FAQ. The Environments discrepancy note is now marked resolved instead of open: there is again exactly one environment, without qualification.
- Added v2.8.9 to the milestone table and updated the v2.9.0 row from blocked to ready.

---

## [2.8.8] - 2026-08-29

### Added: `tools/build-nav.py`, the nav now has one source
- Added `tools/build-nav.py`, which holds the navigation bar once and stamps it into every page. Running it rewrites the block between the `<!-- NAV -->` marker and the closing `</nav>` tag in all 12 HTML files and sets `class="active"` from each file's own name.
- Added a `--check` mode that reports any page whose nav has drifted, writes nothing, and exits non-zero. Running the script with no nav change prints "nav is up to date in every page", which doubles as a consistency check across all 12 pages.
- No markers were added to any page. Both `<!-- NAV -->` and `</nav>` already appeared exactly once per file, which is what makes the range unambiguous without extra scaffolding.
- The script preserves each file's own line endings. `music.html` is CRLF while every other page is LF, and rewriting that would have produced a whole-file diff instead of a nav diff.
- The two pages that are not in the nav (`accounts.html`, `privacy-policy.html`) need no special case: no entry matches their filename, so they receive the nav with no active item, which is what they had before.

### Changed
- **The deployed site is byte-for-byte unchanged by this release.** The script was verified against the existing pages before anything was committed: it reproduces all 12 navs exactly, producing an empty `git diff`. It was then verified to repair drift, by deliberately removing the Music link from `accounts.html` and corrupting a link label in `music.html`, running the script, and confirming both files returned to their committed state with line endings intact.
- Milestone v2.7.0 is complete. Both outstanding items (shared nav extraction and active-state detection) are closed by this change, roughly seven weeks after the CSS half shipped.

### Documentation
- Recorded in `docs/PRD.md` that the nav extraction shipped by a third method, not either of the two the milestone originally proposed. JS injection was rejected because it removes the nav entirely without JavaScript, trading away the site's graceful degradation to fix a maintenance problem that had never once produced a broken page. A real build step was rejected because it puts a toolchain between the source and the deployed artifact. A stamp script whose output is committed has neither property: the repository still contains complete deployable HTML, nothing runs at request time, and deleting the script would cost only the convenience.
- Rewrote the Build section of the Runbook to state that there is still no build step, and to explain why the stamp script is not one.
- Updated the Tenet 3 discussion, which previously used the nav duplication as its worked example of simplicity winning on merit. It now records what changed that verdict.
- Updated Known Technical Debt: the nav markup row is closed. What remains is the roughly 20 line toggle script, still duplicated verbatim in all 12 pages, and the fact that nothing runs `--check` automatically. Wiring it into the `pre-commit` hook alongside the em-dash guard is the obvious next step and is recorded as such.
- Updated the Working Practice never-do list, the common errors table, the fragile areas table, maintenance rule 4, the verification steps, the prerequisites table (Python 3 is now needed to change the nav, standard library only), the folder tree, the public surface table, and feature F3.
- Added a note to the Navigation Bar section of `docs/DESIGN.md` that the markup is generated and must not be hand-edited.
- Added v2.7.0, v2.8.7, and v2.8.8 rows to the milestone table.

---

## [2.8.7] - 2026-08-29

### Added: reduced motion support sitewide and a pause control on `music.html`
- Added a `@media (prefers-reduced-motion: reduce)` block to `styles.css` that collapses every animation and transition to `0.01ms` and forces `transform: none` on hover. The card hover lift is suppressed; the border and background color changes that carry the same affordance are untouched, so no interactive element loses its cue.
- Added a play/pause control to the mode-button row on `music.html` (`.motion-btn`, styled in `--accent` rather than the `--purple` used by the mode pills so it reads as a control over the whole scene). Every visitor can now stop the animation, which nothing on the page allowed before.
- The `music.html` visualizer now reads `prefers-reduced-motion` in JavaScript and decides whether to start its render loop. A CSS media query cannot stop a `requestAnimationFrame` loop, so this had to be handled in the script rather than the stylesheet.
- One frame is always painted before the loop is gated, so a paused stage shows the full scene rather than an empty canvas. Verified in Microsoft Edge with `--force-prefers-reduced-motion`: the button reads "Play" and the stage holds a complete still frame.

### Changed
- Refactored the `music.html` main loop: `draw()` no longer schedules itself. A new `loop()` drives the frames and a new `setPlaying()` starts and cancels it, updating the button label, `aria-pressed`, and `aria-label` together.
- Clicking a mode button while paused now redraws a single frame, so the picked mode is visible without starting the animation.
- The `resize` handler now redraws a single frame while paused, so the still frame stays correct after `build()` recomputes the stage layout.

### Documentation
- Resolved Open Question 8 in `docs/PRD.md`. Three candidates were built into a local harness and compared: freeze on first frame, start paused with a control, and a calm mode keeping slow motion without strobes or lasers. The control won because it is the only one of the three that also satisfies WCAG 2.2.2 (Pause Stop Hide, Level A) for the majority of visitors who never set a reduced-motion preference. The question is kept with its original text struck through rather than deleted, per the documentation process.
- Added feature F18 to `docs/PRD.md` and updated F14 to mention the control.
- Checked off the reduced-motion item in the v2.7.0 milestone in `docs/PRD.md`. That milestone now has only the nav extraction and its active-state detection outstanding.
- Replaced the `prefers-reduced-motion` row in Known Technical Debt with the tab-hidden render loop, which is the part that remains unsolved and is a battery concern rather than an accessibility one.
- Added a "Reduced motion" subsection to the Animation and Motion section of `docs/DESIGN.md` documenting both layers, the on-load behavior table, and the WCAG reasoning.
- Rewrote the accessibility gaps list in `docs/DESIGN.md`: the two items this release closed were removed and marked as closed, and two gaps that had been ranked below them (unmeasured beat flash rate against WCAG 2.3.1, and browser-default focus styles) are now named explicitly.

---

## [2.8.6] - 2026-08-29

### Changed: RouteNote referral code surfaced on the badge
- Changed the RouteNote promo badge on `support.html` from "Free Distribution" to "Referral Code: 2fcd201c", so the code is visible at a glance and visitors remember to enter it at sign-up. Referral credit is only granted when the code is entered.
- Moved the free-distribution message into the card description, which now reads "Free music distribution to Spotify, Apple Music, and every major platform. Enter referral code 2fcd201c when you sign up."
- Updated the RouteNote row of the active affiliate cards table in `docs/PRD.md` to match the new badge text.

---

## [2.8.5] - 2026-08-24

### Added
- Added a full "Documentation Versus Reality" table to `docs/PRD.md` recording all 20 discrepancies found between the documentation and the source, with the source trusted and the reasoning for each.
- Added a "Risks and Open Questions" section to `docs/PRD.md` covering what was not fully understood, fragile areas of the codebase, changes that are dangerous without more context, work in progress at audit time, and 8 numbered open questions for the author to resolve.
- Added a "Working Practice" section to `docs/PRD.md`: pre-edit checks, a "which document to read first" table, a never-do list, an 8-step verification procedure, and post-change documentation sync steps.
- Added a "Conventions" section to `docs/PRD.md` derived from the code itself, covering naming, formatting, organization, comments, error handling, and commit message and branching practice, naming the dominant form wherever the codebase is inconsistent.
- Added a "Browser Testing" section to `docs/PRD.md` adopting Microsoft Edge as the browser for any automated or headless testing, with resolved binary paths, and recording `test-local-audio.bat` as a pre-existing Chrome-driving deviation.
- Added a "Deprecation and Removal" section to `docs/PRD.md` defining the deploy boundary for this project, the HTML meta-refresh redirect mechanism, a full public surface table, and a retired items log.
- Added a "Press Release" section to `docs/PRD.md`, which the previous "Press Release and FAQ" block referenced but never actually contained.
- Added Retention metrics to `docs/PRD.md`, previously the one missing metrics category, together with an explicit statement that the site cannot measure retention and the three proxies available instead.
- Added a "How an audit is run" procedure to the Documentation Process section of `docs/PRD.md`.
- Added feature F13 (Codes page), F14 (music stage visualizer), F15 (stage console), F16 (shared stylesheet), and F17 (writing-style guard) to the `docs/PRD.md` feature list.
- Added a sixth product tenet, "Say What Is Actually True", covering site copy, promo badges, and documentation equally.
- Added a full `music.html` Visual System section to `docs/DESIGN.md`: scene structure, draw order, screen layout, DJ booth, reflection, bloom, scanlines, the 10-mode table with visible and hidden state, and the animated favicon.
- Added an image asset table to `docs/DESIGN.md` listing all 15 files in `img/` with sizes and referencing pages.
- Added six "Rules for Staying Consistent" to `docs/DESIGN.md`.
- Expanded the external FAQ in `docs/PRD.md` from 8 to 20 questions.

### Changed
- Rewrote `README.md` for a general reader: name, description, live link, a 12-row table of what each page offers in plain language, who it is for, current status, and links to `/docs`. Removed the clone and serve commands, the file overview, the tech stack table, the version number, and the "Adding a Project" and "Adding a Discord Server" instructions. All of that content was preserved in the `docs/PRD.md` Operational Runbook and Data Models sections rather than deleted.
- Rewrote `docs/DESIGN.md` around the two-layer CSS model (shared `styles.css` tokens versus page-scoped `:root` overrides), with separate token tables for each layer, the inline `rgba()` brand colors, and roughly 15 documented component patterns.
- Rewrote `docs/PRD.md` in full, merging every existing section rather than replacing it. Original intent, rationale, and wording were kept wherever the code agreed with them; where the code disagreed, both readings are recorded.
- Documented `wrangler.jsonc` as a configured but unused Cloudflare Workers deploy target in the tech stack and Environments sections, alongside the existing "only one environment" statement.
- Restated the under-50 KB page weight constraint as met on 11 of 12 pages, naming `music.html` at 91 KB as a deliberate and explained exception rather than quietly restating the target.
- Reprioritized the accessibility section of `docs/DESIGN.md`, promoting the absence of a reduced-motion path on `music.html` from a minor gap to a genuine problem.

### Fixed
- Corrected the navigation bar description in `README.md` and `docs/DESIGN.md` to the 10 current items (Home, About, Discord, Invests, Codes, Music, Links, Projects, YouTube, Support). Both had described a nav with external Tools and GitHub links that was removed in v2.6.x, and both omitted Music, added in v2.8.0.
- Added `codes.html`, which was live and in the nav of all 12 pages but appeared nowhere in `README.md` or `docs/PRD.md`, to the site structure table, folder tree, public surface list, and feature list.
- Corrected the page count from 11 to 12 in every location, and dropped the "self-contained" description of the pages, which stopped being accurate when `styles.css` was extracted in v2.7.0.
- Corrected the clone URL in the runbook from `github.com/Azqato/Azqato.git` to the actual remote, `github.com/Azqato/azqato.github.io.git`.
- Narrowed the "zero external requests" claim, which was true of 11 pages but not of `music.html` (two Mixcloud iframes on every load) or `projects.html` (one cross-site favicon), everywhere it appeared in the performance, privacy, and security sections.
- Corrected the affiliate card data model in `docs/PRD.md` and `docs/DESIGN.md` to the real class names (`.affiliate-logo`, `.affiliate-promo`, `.affiliate-link-btn`, on an anchor element). Three of the four previously documented class names did not exist in `support.html`.
- Removed the `activeTag` state variable from the `docs/PRD.md` state management table. No such variable exists; filter state lives in the DOM as `.active` and `data-hidden`.
- Corrected the mobile breakpoint in `docs/DESIGN.md` from "< 600px: nav links hidden" to the actual split: the nav collapses into a toggle at 860 px and content padding tightens at 600 px. The superseded claim is kept and marked rather than erased.
- Corrected the image usage claims in `docs/DESIGN.md`: `index.html` contains no image element at all, `music.html` lists no playlists, and 10 of the 15 files in `img/` are referenced by nothing, including a 1.9 MB GIF that appeared in no documentation.
- Corrected feature F4, which claimed the landing page hero includes a profile photo. It has interest pills and two CTA buttons.
- Corrected feature F11, which claimed the lion favicon is identical across all 12 pages. `music.html` replaces it at runtime every third frame.
- Documented that the `music.html` visualizer is not audio-reactive. `analyser` and `freqData` are declared and never assigned, so every visual is procedural. This was stated nowhere before and is now recorded in `docs/DESIGN.md`, the data flow section, F14, and Known Technical Debt.
- Corrected the Known Technical Debt entry describing the nav as duplicated across "all 11 HTML files" to 12.

### Removed
- Removed nothing from the codebase. This audit was documentation only; no HTML, CSS, JavaScript, or image file was edited, renamed, or deleted.

### Writing style sweep
- Swept every text file in the repository for both prohibited em-dash forms independently (the literal character and the HTML entity), including files inside dot-directories that a plain recursive glob skips.
- Found **zero violations** in any HTML file, in `styles.css`, and in all documentation prose.
- Found 4 occurrences in `docs/PRD.md` and `docs/PATCHNOTES.md`, all inside backtick code spans where the rule names or quotes the character it prohibits. All are exempt under the existing policy and were left in place.
- Found 2 occurrences in `.githooks/pre-commit`, where the guard defines the character it blocks. Exempt and left in place.
- Found 13 lines with real violations in `.vscode/recentfedsummary.MD`, a personal note unrelated to the site that is tracked in git. Left untouched: it is outside this audit's write scope and outside the project's own documentation. Recorded as Open Question 1 in `docs/PRD.md`.

---

## [2.8.4] - 2026-08-24

### Added: RouteNote affiliate card on `support.html`
- Added a RouteNote referral card to the affiliate partners grid on `support.html`, placed after Twitch Prime. Links to `routenote.com/rn/referral/2fcd201c` (referral code `2fcd201c`) with a "Free Distribution" promo badge and an orange-tinted logo tile.
- Updated the affiliate references in `docs/PRD.md`: feature F7, the assumptions list, the affiliate link accuracy criterion (now 7 links), the active affiliate cards line, and the third-party integrations table.

---

## [2.9.0] - 2026-07-16 (branch only, not deployed)

### Deferred: native track player, kick detection, and video screen mode
- Built and validated a native in-page audio player for `music.html`: a Web Audio-routed `<video>` element (two test tracks), a scrub-bar player UI, an onset-based kick detector tuned against a real track with `ffmpeg`, a beat-synced screen pulse, a rarity-gated loud-moment flash, audio-scaled laser beam counts, and a "Video" screen mode that draws the playing track's own frames onto the stage screens.
- Not merged to `main`: the player currently points at large local test files (multiple GB) that cannot be committed to this repo (GitHub rejects pushes over 100MB via normal git, and even Git LFS caps at 2GB/file on GitHub.com, well under these files' size). A live "Play" button pointing at nothing would be broken for real visitors.
- Full implementation kept on branch `feature/native-audio-player` (pushed to GitHub) so the work isn't lost. To resume: host a real track externally (object storage plus CDN, or a video host that serves a direct file URL) and point the `<video src>` at it, then merge the branch. See Known Technical Debt below.

---

## [2.8.3] - 2026-07-16

### Added: stage console panel on `music.html`
- Combined the two Mixcloud embeds and the three platform links (Last.fm, Mixcloud, YouTube) into a single `.stage-console` panel docked over the center visualizer screen. The panel is `position: fixed` and independently scrollable (`overflow-y: auto`), so it stays pinned in place and scrolls on its own without affecting the main page scroll. Styled with a dark glass background and a themed thin scrollbar to read as content displayed on the screen rather than a floating card.
- Removed the old in-flow `.section` block, `.mixcloud-embed`, and `.platform-grid` markup and styles that this replaces.

### Changed: visualizer mode buttons on `music.html`
- Hidden the Bars, Volumetric, Origami, Ghost, and Noise mode buttons; only Stars, Vortex, Squares, Tunnel, and Fence remain visible. The modes themselves are unchanged in code.
- The random mode auto-cycle now only picks from the five visible modes (Stars, Vortex, Squares, Tunnel, Fence), so the hidden modes no longer appear during automatic cycling either.

### Documentation
- Added a full mobile audit of `music.html` to `docs/PRD.md`'s Explicitly Deferred Items as a future action item, since the visualizer canvas and fixed stage console were tuned for desktop viewports first.

---

## [2.8.2] - 2026-07-11

### Fixed: Mixcloud embed width on `music.html`
- The two Mixcloud player iframes had a `width="660px"` HTML attribute that was silently overridden by `.mixcloud-embed iframe { width: 100% }`, so the embeds actually stretched to the full `.section` width (up to ~1036px) instead of the intended 660px.
- Gave `.mixcloud-embed` a `max-width` of `calc(3 * 220px + 2 * 1rem)` (692px) and centered it, so the embeds now match the width of the three-card platform-grid row (Last.fm, Mixcloud, YouTube) directly below them.

---

## [2.8.1] - 2026-07-11

### Fixed: floor reflection ghosting near the DJ booth
- The panoramic screens' bloom effect (an upscaled, offset redraw of already-rendered panel pixels) was being mirrored onto the glossy floor by `drawReflection()`, and that mirrored band overlapped the DJ booth's position, making the booth appear doubled and blurry. Clipped a hole in the reflection draw over the booth's footprint so the reflection no longer washes over it.

### Changed: DJ booth redesign
- Replaced the flat, single `fillRect` booth panel with an actual structure: a front fascia (angled toward the crowd), raked side cheeks, and a solid base, all merged into one continuous silhouette running from the top deck down to the floor. The old design ended in a thin, near-invisible riser that read as an abrupt cutoff; the new one is grounded.
- Moved the "AZQATO" wordmark off a fixed spot at the top of the stage truss (the old `drawULogo`, now removed) and onto the booth's fascia, keeping the same gold gradient and glow treatment. Sizing now accounts for `letterSpacing` and fits both the width and height of the fascia's text box, fixing an overflow bug where the letters bled past the panel's edges.
- Added a top deck with a back rail (visible thickness along the rear edge instead of a flat cutoff), two CDJ silhouettes with small static jog-wheel accents (previously oversized glowing circles), and a plain static mixer panel between them, replacing the animated audio-reactive LED grid that used to sit there.
- Removed the center laser-triangle overlay (`drawTriangle`) that floated above the booth.
- Enlarged the booth overall and added top margin above the wordmark so it isn't crowded by the deck.

---

## [2.8.0] - 2026-07-10

### Changed: `music.html` visualizer overhaul

**Screen layout**
- Replaced the 5-screen Brooklyn Mirage layout (center + 2 wings + 2 outer panels) with a cleaner 3-screen layout: one wide center screen (42% canvas width) and two independent side panels (22% each) with a visible gap between center and sides. Side panels are flat (no rotation).
- `drawOuterScreen` removed entirely; only `drawWingScreen` remains for the side panels.

**WebGL shader modes** (added 7 new GPU visualizers, modes 5-9 plus two added mid-session):
- **Origami** (mode 5, `@XorDev`): soft-shaded folded-paper layers with bounce lighting and palette color cycling.
- **Tunnel** (mode 6, CC0): star-shaped SDF tunnel with per-layer rotation, postprocess vignette and contrast.
- **Ghost** (mode 7, seb chevrel 2019): ray-marched ghost dancers scene with SDF bodies, AO, soft shadows, and palette coloring; reuses the volumetric noise texture as `iChannel0`.
- **Fence** (mode 8, CC0): layered hexagonal grid animation with animated palette and camera drift.
- **Noise** (mode 9, Inigo Quilez MIT): value noise with fractal octaves, alternates between Cartesian and polar projection every 3 seconds.
- Previously added: **Vortex** (mode 3, CC-BY-NC-SA-4.0 @WorkingClassHacker) and **Squares** (mode 4, CC0).

**Mode system**
- Mode count increased from 5 to 10 (modes 0–9); `% 10` cycling.
- Auto-advance now picks a **random** mode on each 30-second tick (no immediate repeat) instead of cycling sequentially.
- Default mode on page load changed from Bars (0) to **Squares** (4).
- Removed Julia, Plasma, Mandelbrot, Newton, and Burning Ship canvas fractal modes (and their dead `computeFractal_REMOVED` code block).

**UI / text**
- Hero badge changed from "🎵 Now playing" to "🎵 Azqato's Music".
- H1 heading ("Azqato's Music") made visually hidden (1×1 px clip) while remaining in the DOM for SEO and screen readers.
- Canvas logo text changed from "AZ" to "AZQATO"; vertical position tuned.
- Footer "Built by Azqato." background/blur pill now wraps tightly around the text instead of spanning the full footer width.
- Mode buttons updated to match new 10-mode list: Bars, Volumetric, Stars, Vortex, Squares, Origami, Tunnel, Ghost, Fence, Noise.

---

## [2.7.0] - 2026-07-09

### Changed
- **Roadmap milestone: Code Extraction + Shared Assets (first half).** Extracted the CSS that was byte-identical across all 12 pages into a single external `styles.css`: the 12 shared design tokens (`:root`), the universal reset, the scrollbar-gutter fix, `body`, the entire nav component (`nav`, `.nav-inner`, `.nav-logo`, `.nav-toggle`, `.nav-links` and its states), the nav's 860px collapse breakpoint, and `footer`. Every page now links `<link rel="stylesheet" href="styles.css" />` instead of repeating roughly 100 lines of identical CSS in its own inline `<style>` block.
- Page-specific `:root` overrides (`--discord`/`--discord-hover` on `discord.html`/`index.html`/`invests.html`, `--spotify` on `music.html`, `--coffee`/`--coffee-hover` on `support.html`) remain in each page's own inline `<style>` block, since CSS custom properties cascade additively across multiple `:root` rules; only the 12 common tokens moved to `styles.css`.
- Renumbered six patch-note entries that had drifted into the `2.7.x` range (favicon change, nav logo scrollbar-gutter fix, Leveraged Strategies URL update, `invests.html` `html{}` rule merge, `invests.html`/`codes.html`/`youtube.html`/`discord.html`/`about.html`/`links.html` layout pass, VIX Strategy URL casing) down to `2.6.11`-`2.6.16`, since none of them were the actual "Code Extraction + Shared Assets" roadmap milestone and the true `v2.7.0` needed to be free for this entry.

### Deferred
- Extracting the shared `<nav>` markup and its toggle `<script>` out of the 12 HTML files themselves is intentionally not done here: it requires deciding between a JS-injected nav (no build step, but the nav is briefly absent until JS runs) and a minimal build step (nav stays in static HTML, but the project currently has none). The `styles.css` extraction above has no such trade-off and was safe to do immediately.
- Auto-detecting the active nav link via `window.location.pathname` and adding `@media (prefers-reduced-motion: reduce)` remain outstanding from the same roadmap milestone.

---

## [1.0.0] - 2026-06-06

### Added
- Initial release of the portfolio site.
- Self-contained `index.html` with zero external dependencies.
- Project card grid with icon, name, description, tags, GitHub link, optional demo link, star count, and last-updated fields.
- Tag filter bar, auto-generated from the `PROJECTS` array; filters the grid in real time.
- Project count label that updates to reflect the active filter.
- Sticky nav bar with logo and GitHub profile link; collapses nav links on mobile.
- Hero section with status badge, headline, bio, and two CTA buttons.
- Language-specific tag colour classes: `lang-js`, `lang-ts`, `lang-py`, `lang-cs`, `lang-html`, `lang-css`, `lang-go`, `lang-rust`, `lang-java`.
- Hover animations on cards: lift, border highlight, top-edge gradient.
- Fully responsive layout (320 px → 2560 px).
- CSS custom properties for easy retheme via `:root` variables.
- `README.md` with setup and deployment instructions.
- `PRD.md` documenting requirements, user stories, and design tokens.
- `PATCHNOTES.md` (this file).

---

## [1.1.0] - 2026-06-06

### Added
- Three live projects populated from their READMEs: Net Worth Tracker, VIX Strategy, and Lantern.

### Changed
- Project card title now links to the live GitHub Pages site (`demo` URL) instead of the GitHub repository, making the primary action open the running app.
- GitHub repository link retained as a separate icon button on each card alongside the live-site (↗) button.

---

## [1.2.0] - 2026-06-06

### Changed
- Project tags simplified to category-only labels: Net Worth Tracker and VIX Strategy tagged `Finance`; Lantern tagged `Social`. Removed tech-stack tags (JavaScript, Chart.js, Dashboard, Privacy, Tailwind CSS) from the filter bar.
- Nav "Projects" link replaced with "Index", pointing to `https://azqato.github.io/`.
- Removed "Browse Projects" secondary CTA button from the hero section.

---

## [1.2.1] - 2026-06-06

### Changed
- README title updated from "Azqato Portfolio" to "Azqato's Portfolio".
- Added live site link (`https://azqato.github.io/`) directly below the README title.

---

## [1.2.2] - 2026-06-06

### Added
- ⚡ emoji favicon added to all pages via inline SVG data URI with no external image file required.

---

## [1.3.0] - 2026-06-07

### Added
- `support.html`: dedicated support page with a personal pitch, Buy Me a Coffee CTA (buymeacoffee.com/azqato), and an affiliate partners grid (6 placeholder cards: Tesla, Robinhood, M1 Finance, Webull, Coinbase, Public).
- "Support" nav link added to `index.html` pointing to `support.html`.
- "Support" nav link on `support.html` highlights as active to signal current page.
- Affiliate card design: square logo area, promo badge, description, and CTA button.
- Pitch card on support page with gradient top border, avatar, bio, and signature pulled from the buymeacoffee About section.

---

## [1.3.1] - 2026-06-07

### Changed
- Buy Me a Coffee CTA section moved above the About Azqato pitch card so the support ask is the first thing visitors see after the hero.
- CTA paragraph replaced with the full buymeacoffee disclaimer: investment intent statement and fund-use caveat.
- Removed the "Opens buymeacoffee.com/azqato, One-time or monthly, 100% goes to the journey" sub-line from the CTA.
- Removed duplicate investment paragraph from the pitch card body since it now lives in the CTA above.
- All em dashes replaced with commas across `support.html` for improved readability.

---

## [1.3.2] - 2026-06-07

### Changed
- CTA disclaimer paragraph left-aligned for improved readability, while the emoji, heading, and button remain centered.

---

## [1.4.0] - 2026-06-07

### Added
- `about.html`: dedicated About page with hero section and the Azqato pitch card (bio, role line, signature).
- "About" nav link added to all pages pointing to `about.html`, with active state highlighted on `about.html`.
- `.nav-links a.active` CSS rule added to `index.html` to support active nav highlighting.

### Changed
- Nav standardised across all pages: Portfolio, About, GitHub, Support. "Index" (external azqato.github.io link) replaced with "Portfolio" (relative `index.html` link) on all pages.
- About Azqato pitch card moved from `support.html` to `about.html`. `support.html` now focuses solely on the Buy Me a Coffee CTA and affiliate partners.
- Footer simplified to "Built by Azqato" across all pages, removing the redundant GitHub link from footer text.

---

## [1.4.1] - 2026-06-07

### Changed
- About page bio expanded with full background story: gaming origins, Twitch and YouTube content creation, B5TA community on RuneScape and Discord, web development work, and closing call to join the journey.
- Role line updated from "Investor, Developer, Community Builder" to "Content Creator, Web Developer, Community Leader" to better reflect the full bio.
- Em dash removed from closing paragraph ("adventure, one built on...").

---

## [1.5.0] - 2026-06-07

### Added
- Clan B5TA project card: community website for the RuneScape clan founded in 2014, tagged `Social` and `Gaming`, linking to the live GitHub Pages site and repo.
- `Gaming` added as a new filter tag category.

---

## [1.5.1] - 2026-06-07

### Changed
- Clan B5TA tag simplified from `Social, Gaming` to `Social` only. `Gaming` filter category removed; current categories are `Finance` and `Social`.

---

## [1.6.0] - 2026-06-07

### Added
- Cat Food Center project card: mobile-first PWA for evaluating cat food via barcode scan or search, tagged `Tools`, linking to the live GitHub Pages site and repo.
- `Tools` added as a new filter tag category.

### Changed
- Net Worth Tracker tagged with `Tools` in addition to `Finance`.

---

## [1.6.1] - 2026-06-07

### Changed
- Cat Food Center icon updated from 🐱 emoji to the project's own `favicon.svg` via the new `iconUrl` field.

### Added
- `iconUrl` optional field on project entries: accepts a URL to an image or SVG and takes precedence over `icon` when set.

---

## [1.7.0] - 2026-06-07

### Changed
- Public affiliate card: real referral link added (`share.public.com/azqato`), promo updated to "Free $20", description updated to match.
- Robinhood affiliate card: real referral link added (`join.robinhood.com/robertg273/`), promo updated to "Free $5–$200 Stock", description updated to match.
- M1 Finance affiliate card: real referral link added (`m1.finance/BVZBG3OqOfMj`), promo updated to "Free $75 Bonus", description updated to reflect $10,000 funding requirement and M1 Premium benefit.
- Affiliate section note updated from "Placeholder links" to "Some links are live, others are coming soon."

---

## [1.7.1] - 2026-06-07

### Changed
- Tesla affiliate card: real referral link added (`ts.la/robert459550`), promo updated to "Free 3 Months FSD", description updated to reflect 3 months of Full Self-Driving or $400 off Solar or Powerwall.

---

## [1.7.2] - 2026-06-07

### Changed
- M1 Finance affiliate card description updated to exact wording specified.

---

## [1.7.3] - 2026-06-07

### Changed
- Affiliate section note replaced with a plain-English disclaimer explaining how referral links work.

### Removed
- Webull and Coinbase placeholder cards removed from the affiliate grid.

---

## [1.7.4] - 2026-06-07

### Added
- Lyft affiliate card: 50% off first ride up to $10 (`lyft.com/invite/ROBGOLDY630855`).

---

## [1.8.0] - 2026-06-08

### Added
- `/docs/` directory created to house all project documentation.
- `docs/TRD.md`: Technical Reference Document covering system architecture, tech stack, data models, internal data flow, state management, third-party integrations, performance requirements, and known technical debt.
- `docs/DESIGN.md`: Design system document covering color palette (all CSS custom properties), typography, spacing, breakpoints, component patterns, accessibility standards, and motion rules.
- `docs/PRFAQ.md`: Press release and FAQ (internal and external).
- `docs/TENETS.md`: Product principles with 5 prioritized tenets.
- `docs/METRICS.md`: Success metrics, targets, measurement methods, and reporting cadence.
- `docs/ROADMAP.md`: Milestone table with current phase, planned features, and deferred items.
- `docs/SECURITY.md`: Security model covering auth, data storage, third-party trust, attack surface, and dependency policy.
- `docs/RUNBOOK.md`: Operational runbook with local setup, build, deploy, rollback, environment configs, common errors, and monitoring.

### Changed
- `PRD.md` moved from project root to `docs/PRD.md` and expanded with problem statement, target user personas, assumptions, and measurable success criteria.
- `PATCHNOTES.md` moved from project root to `docs/PATCHNOTES.md`.
- `README.md` updated with tech stack table, prerequisites section, environment variable reference (none), expanded deploy instructions, link to `/docs/`, and updated file overview reflecting the new `docs/` structure.

### Removed
- `PRD.md` from project root (moved to `docs/PRD.md`).
- `PATCHNOTES.md` from project root (moved to `docs/PATCHNOTES.md`).

## [1.9.0] - 2026-06-08

### Added
- ComposerAtlas project card: curated strategy library and education hub for Composer.trade investing, featuring strategy pages with plain-English logic breakdowns, risk profiles, metrics tables, and a glossary of systematic investing concepts. Tagged `Finance` and `Tools`.

## [1.9.1] - 2026-06-08

### Changed
- ComposerAtlas and Cat Food Center tagged with `Education` to reflect their educational content.
- `Education` added as a new filter tag category.

---

## [1.9.2] - 2026-06-09

### Changed
- Buy Me a Coffee CTA paragraph split: main text ends with `*` asterisk; disclaimer moved below the button in smaller italic text.

---

## [1.9.3] - 2026-06-09

### Added
- Boaty McBoatface Ventures project card: humorous marketing site for a fictional New England canvas exo-skeleton water displacement company, tagged `Meme`.
- `Meme` added as a new filter tag category.

---

## [2.0.0] - 2026-06-09

### Added
- `links.html`: Social and platform links hub, organized into sections: Community and Streaming, YouTube, Music, Social, Investing, and More. All external links from the old website consolidated here.
- `youtube.html`: YouTube channels page showcasing all four channels (Azqato, Azqato Streams, Azqato Mixes, Azqato Chills) as cards with thumbnail photos, channel descriptions, and subscribe buttons.
- `invests.html`: Azqato Invests resource hub with 14 curated sections: Platforms, Careers, ETFs, Companies, Ratings, Screeners, Real Estate, Charts, Databases, Economic Indicators, Education, Guides, Indices, Information, and News.
- `music.html`: Music page featuring the two Spotify playlists (BANGERS, ADDICTIONS) with cover art, plus links to Last.fm, Mixcloud, and YouTube Mixes.
- `accounts.html`: Gaming accounts page listing Azqato's profiles across Steam, League of Legends, Teamfight Tactics, and RuneScape.
- `privacy-policy.html`: Full privacy policy page covering Consent, Information Collection, Log Files, Cookies, DART Cookies, CCPA, GDPR, Children's Information, Affiliate Links, Financial Disclaimer, and Entertainment Purposes.
- `img/` directory with 14 image assets migrated from the old website: profile photos (`home-hero-profile.jpg`, `about-profile.jpg`, `logo-cat-avatar.jpg`), YouTube channel thumbnails (`yt-thumb-azqato.jpg`, `yt-thumb-streams.jpg`, `yt-thumb-mixes.jpg`, `yt-thumb-chills.jpg`), larger channel images (`yt-channel-*.jpg`), Spotify playlist covers (`music-playlist-bangers.jpg`, `music-playlist-addictions.jpg`), and music logo (`music-logo-small.jpg`).
- Profile photo (`home-hero-profile.jpg`) added to the `index.html` hero section as an 80px circular avatar.
- "All Links →" secondary CTA button added to the `index.html` hero actions, pointing to `links.html`.
- Profile photo (`about-profile.jpg`) added to the `about.html` pitch card avatar, replacing the ⚡ emoji.
- `Links`, `YouTube`, and `Invests` nav links added to all pages.
- Privacy Policy footer link added to all pages.

### Changed
- `index.html` hero description expanded to mention content creation, gaming, investing, music production, and streaming, preserving the intro text from the old website's landing page.
- Nav expanded from 4 links (Portfolio, About, GitHub, Support) to 7 links (Portfolio, About, Links, YouTube, Invests, GitHub, Support) across all pages.
- Footer on all pages updated from "Built by Azqato" to include a "Privacy Policy" link.
- `about.html` pitch avatar size increased from 60px to 72px to better display the profile photo.

### Removed
- `oldwebsite/` directory and all its contents deleted after full content migration.

---

## [2.0.1] - 2026-06-09

### Changed
- League of Legends accounts on `accounts.html` updated to Riot ID format: `Chief Rocka` → `서주프#zoop` and `Azqato` → `Azqato#zoop`.
- Both LoL op.gg links updated to the new URL format (`op.gg/lol/summoners/na/`).

---

## [2.0.2] - 2026-06-09

### Changed
- TFT accounts on `accounts.html` updated to metatft.com with Riot ID format: `서주프#zoop` and `Azqato#zoop`. Links updated from lolchess.gg to `metatft.com/player/na/`.
- RuneScape accounts updated: `Hctibaru` replaced with `ironqato`; both links updated from runeclan.com to runepixels.com (`/players/<name>/skills`).

---

## [2.0.3] - 2026-06-09

### Changed
- Privacy Policy link moved from all page footers to the More section on `links.html` as a button.
- Footers across all 9 pages simplified back to "Built by Azqato" only.

---

## [2.0.4] - 2026-06-09

### Changed
- Footer byline updated to "Built by Azqato." on all pages. The period is outside the link element so it renders in `--text-muted` rather than the accent green.

---

## [2.1.0] - 2026-06-10

### Added
- Stock Methodology project card: educational site documenting a fundamentals-driven individual stock and ETF investing methodology, covering 10 evaluation metrics (PEG, P/E FWD, RSI, revenue/EPS growth, cash/debt, 52W range), a Finviz screener guide, Seeking Alpha watchlist setup, and VIX-based index investing strategies. Tagged `Finance` and `Education`.

---

## [2.1.1] - 2026-06-10

### Changed
- All links to the GitHub profile (`github.com/Azqato`) now open in the same tab. Removed `target="_blank" rel="noopener"` from all 20 occurrences across 9 pages (nav links, footer bylines, hero CTA, and links page button).

---

## [2.2.0] - 2026-06-10

### Added
- TQQQ Strategies project card: educational wiki-style site documenting six leveraged ETF strategies side by side: 3 Sig, 6 Sig, 9 Sig, TQQQ For The Long Term, Holy Grail, and HFEA. Each strategy has a dedicated page covering rules and logic, performance notes, risks, and sources. Tagged `Finance` and `Education`. Live at `https://azqato.github.io/leveraged-strategies/`.

---

## [2.2.1] - 2026-06-10

### Changed
- TQQQ Strategies card icon updated from ⚡ to 🚀 to match the site's favicon.

---

## [2.2.2] - 2026-06-10

### Changed
- TQQQ Strategies project card renamed to "Leveraged Strategies" ahead of a planned site rename.

---

## [2.2.4] - 2026-06-11

### Changed
- Fixed HTML-encoded em dash (`&mdash;`) in `index.html` hero bio paragraph. Previous audit only searched for the literal `—` character and missed the entity form.
- `docs/PRD.md` Writing Style section updated to note that em dashes appear in two forms in HTML (`—` and `&mdash;`) and both are prohibited. Audits must search for each form independently.

---

## [2.2.3] - 2026-06-11

### Changed
- Em dashes removed from all HTML pages (accounts.html, index.html, invests.html, youtube.html) and all documentation files (PRD.md, PATCHNOTES.md, ROADMAP.md, DESIGN.md, TRD.md, METRICS.md, SECURITY.md, TENETS.md, PRFAQ.md, RUNBOOK.md) and README.md. Replaced with comma, colon, semicolon, parentheses, or period based on context.
- Version headers in PATCHNOTES.md updated from `[x.y.z] — YYYY-MM-DD` format to `[x.y.z] - YYYY-MM-DD` for consistency.
- `docs/PRD.md` updated with a Writing Style section documenting the no-em-dash methodology and preferred punctuation alternatives.

---

## [2.3.0] - 2026-06-13

### Added
- New introductory landing page at `index.html`, designed as the front door for first-time visitors. It introduces who Azqato is across gaming, content creation, investing, music, and community, then routes visitors onward rather than opening straight into the project grid.
- Discord join as the primary call to action, featured both in the hero and in a dedicated closing CTA band (`discord.gg/39JrFNY7qS`), styled with the official Discord brand color (`#5865f2`) and logo.
- "Explore the site" card grid linking to all eight key destinations: Projects, About, YouTube, Music, Invests, Gaming Accounts, Links, and Support, each with an icon and one-line description.
- Hero with an easygoing introduction and a secondary "Explore the site" anchor button, plus an intro blurb with a short bio and category pills (Gaming, Investing, Music, Web Dev, Community).
- `--discord` and `--discord-hover` CSS custom properties on the landing page.

### Changed
- Site structure reworked so the landing page is the default entry point. The project grid (cards, tag filter, hero) moved from `index.html` to `projects.html`; the new introductory landing page now occupies `index.html`.
- Navigation label renamed from "Portfolio" to "Projects" across all pages, and the link now points to `projects.html`.
- Nav logo on every page links home to `index.html` (the new landing page). The project grid page's logo, previously `href="#"`, now also points to `index.html`.
- `projects.html` page title updated from "Azqato | Portfolio" to "Azqato | Projects".

### Notes
- The landing page follows the existing design system (GitHub dark theme, `#00d4a0` accent, system font stack, zero dependencies) and is self-contained with inline CSS.
- The site now comprises 10 pages.

---

## [2.3.1] - 2026-06-13

### Added
- "Home" and "Discord" links added to the global navigation. Home points to the landing page (`index.html`); Discord points to the community invite (`discord.gg/39JrFNY7qS`) and opens in the same tab, matching the GitHub link convention.

### Changed
- Navigation reordered across all 10 pages to: Home, About, Discord, Invests, Links, Projects, YouTube, GitHub, Support.
- Landing page hero introduction reworded for a more confident, knowledgeable first impression (removed the "music nerd" phrasing and the "front door / come hang out" close).
- Landing page intro blurb refined for tone: now notes B5TA has thrived on RuneScape and Discord for over a decade, and splits "music production" and "DJ mixes" into separate highlighted lanes.
- Highlighted the connecting "and" before "web development" in the intro lanes so it carries the same accent styling as the other lanes.

---

## [2.3.2] - 2026-06-13

### Added
- No Fee Apartments project card: curated directory of no-broker-fee apartment buildings across New York City, Boston, and San Francisco. Tagged `Tools` and `Real Estate`. Links to `nofeeapartments.net`.
- LV Guest List project card: free guest list access for Las Vegas's top nightclubs and dayclubs. Tagged `Social`. Links to `lvguestlist.com`.
- `Real Estate` added as a new filter tag category.

### Changed
- `projects.html` hero stripped down to title and description only: removed the avatar image, "Available for collaboration" badge, and CTA buttons.
- `projects.html` hero description rewritten as a concise rocket pitch: "Finance dashboards, social platforms, educational tools, and a few projects that refuse to take themselves seriously. Every one is live and built to actually be used. Pick a tag and dig in."
- Spacing between the hero description and the Projects section header tightened: hero bottom padding reduced from `3rem` to `1.5rem`; section top padding reduced from `3rem` to `1.5rem`.

---

## [2.4.0] - 2026-06-13

### Added
- `discord.html`: dedicated Discord page listing all four community servers (Azqato, Azqato Invests, B5TA, League of Azqato) as cards with permanent invite links, descriptions, and Discord-blue Join Server buttons.
- `--discord` and `--discord-hover` CSS custom properties on `discord.html`.

### Changed
- Nav Discord link updated from the external `discord.gg` invite URL to `discord.html` across all 11 pages, so visitors browse all servers before choosing one to join.
- Azqato main Discord invite updated from the temporary link (`discord.gg/39JrFNY7qS`) to the permanent invite (`discord.gg/sKGKC3JFSE`) in `index.html` and `links.html`.
- `docs/PRD.md` site structure table updated to include `discord.html`.
- The site now comprises 11 pages.

---

## [2.4.1] - 2026-06-13

### Changed
- Discord server card icons updated: Azqato 🐱, Azqato Invests 💸, B5TA ⚔️ (unchanged), League of Azqato 🖥️.
- `discord.html` hero description rewritten as a general community pitch, removing per-server references in favour of a broader invitation.

---

## [2.5.0] - 2026-06-13

### Changed
- Documentation consolidated from 10 files to 4: `README.md` (root), `docs/PRD.md`, `docs/DESIGN.md`, `docs/PATCHNOTES.md`.
- `docs/TRD.md`, `docs/TENETS.md`, `docs/PRFAQ.md`, `docs/SECURITY.md`, `docs/RUNBOOK.md`, `docs/METRICS.md`, and `docs/ROADMAP.md` removed; all content absorbed into `docs/PRD.md` under dedicated sections.
- `README.md` rewritten as a developer-only reference: removed marketing language, updated file overview to 11 pages, updated nav description to reflect `discord.html` and the `class="active"` pattern, added "Adding a Discord Server" instructions.
- `docs/DESIGN.md` updated: fixed card border-radius to `10px`, hover transform to `translateY(-2px)`, and card gap to `1rem` to match actual implementation; updated `--discord` and `--discord-hover` note to reflect both `index.html` and `discord.html`; added Discord server card component pattern; updated all typography and spacing values to current code.
- `docs/PRD.md` expanded with consolidated Architecture, Tenets, FAQ, Security, Runbook, Metrics, Roadmap, and Documentation Process sections; added F8 (Discord Page) and F10 (Landing Page) to Feature List; updated site structure table to 11 pages; updated Discord server data model with all four permanent invite links; updated project list to 11 current projects.
- Roadmap in `docs/PRD.md` updated: v2.4.0 milestone renamed to "discord.html: four server cards, sitewide nav update" to match what actually shipped; planned code-extraction milestone renumbered to v2.6.0.

### Removed
- `docs/TRD.md`
- `docs/TENETS.md`
- `docs/PRFAQ.md`
- `docs/SECURITY.md`
- `docs/RUNBOOK.md`
- `docs/METRICS.md`
- `docs/ROADMAP.md`

---

## [2.6.0] - 2026-06-14

### Added
- Prompts project card: personal reference library of reusable Claude Code prompts for recurring development, documentation, and maintenance tasks. Zero-dependency, hash-based routing, one-click copy; works offline from any browser. Tagged `Tools` and `Education`. Live at `https://azqato.github.io/prompts/`.

---

## [2.6.1] - 2026-06-15

### Changed
- ComposerAtlas demo link updated from `https://azqato.github.io/ComposerAtlas/` to `https://azqato.github.io/composer` to match the new deployment directory.

---

## [2.6.2] - 2026-06-15

### Added
- "Azqato Projects" resource card added as the first card on `invests.html`, listing all five finance-related projects: Net Worth Tracker, VIX Strategy, ComposerAtlas, Stock Methodology, and Leveraged Strategies.

---

## [2.6.3] - 2026-06-15

### Fixed
- "Azqato's Projects" card title in `invests.html` corrected from "⚡ Azqato Projects".

---

## [2.6.4] - 2026-06-15

### Fixed
- Discord link in the `invests.html` hero paragraph updated from the direct `discord.gg` invite URL to `discord.html`, consistent with the rest of the site.

---

## [2.6.5] - 2026-06-27

### Added
- Azqato's Tools project card: collection of free, browser-based utilities including a Markdown editor with live preview and HTML export, a Favicon Downloader, a Link Cleaner that strips tracking parameters, and a Nasdaq 100 Screener. Tagged `Tools`. Live at `https://azqato.github.io/tools/`.

---

## [2.6.6] - 2026-06-27

### Changed
- "Tools" nav link added to all 11 pages after "Projects", pointing to `https://azqato.github.io/tools/` and opening in the same tab. Nav order is now: Home, About, Discord, Invests, Links, Projects, Tools, YouTube, GitHub, Support.

---

## [2.5.1] - 2026-07-02

### Added
- Twitch Prime affiliate card on `support.html`: explains that Amazon Prime members can use their one free monthly Twitch channel subscription on Azqato's channel at no extra cost. Links to `twitch.tv/azqato`.

---

## [2.5.2] - 2026-07-05

### Fixed
- **Nav bar horizontal overflow between 601px and ~754px on all 11 pages.** The desktop nav (10 links, `gap: 1.5rem`, no wrap) only had a single `display: none` breakpoint at `max-width: 600px`; above that width the full-width link row didn't fit until the viewport reached ~754px, forcing the whole page to overflow horizontally by 51-55px on every page in that range (confirmed via headless Chrome DOM measurement, not screenshots, since `document.documentElement.scrollWidth > clientWidth` in that window). Replaced the abrupt hide-at-600px behavior with a hamburger menu: nav links collapse behind a `.nav-toggle` button below 860px (safe margin above the ~754px content width) and open as a dropdown panel, restoring mobile/tablet navigation that was previously just missing below 600px with no fallback. Implemented identically across all 11 pages (markup, CSS, and a small inline toggle script per page, consistent with the site's no-shared-file architecture).
- **CSS Grid bare `1fr` tracks reverting to unclamped columns on mobile.** `.platform-grid` (`accounts.html`), `.resource-grid` (`invests.html`), `.link-grid` (`links.html`), and `.channel-grid` (`youtube.html`) used `minmax(Npx, 1fr)` at desktop width but their `@media (max-width: 600px)` overrides reverted to a bare `1fr` (or `1fr 1fr`), which has an implicit `min-width: auto` rather than `0`; a card with long unbreakable content could force the grid, and the page, wider than the viewport. Changed the mobile overrides to `minmax(0, 1fr)` (and `repeat(2, minmax(0, 1fr))` for the two-column cases) to match the desktop guard.
- **Redundant spacing from `margin-top` stacked on top of a flex `gap`.** Six elements (`.hero-actions` in `index.html`/`projects.html`, `.pitch-signature` in `about.html`/`support.html`, `.playlist-btn` in `music.html`, `.affiliate-link-btn` in `support.html`) carried their own `margin-top` despite already being spaced by their flex-column parent's `gap`, doubling the intended gap. Removed the redundant margins; parent `gap` now provides the sole spacing.

---

## [2.6.16] - 2026-07-09

### Changed
- Updated all VIX Strategy references to the renamed lowercase URLs: live site `https://azqato.github.io/vix` (`invests.html` card and `projects.html` `demo`) and repo `https://github.com/Azqato/vix` (`projects.html` `github`).

---

## [2.6.15] - 2026-07-09

### Added
- `--discord` and `--discord-hover` color tokens on `invests.html` to support a Discord-branded hero button.

### Changed
- `invests.html` restructured to the `discord.html` layout pattern: removed the "Community investing resources" hero badge, replaced the large `.section-head` blocks with discord-style `.section-header` sections (accent-bar `.section-title` + `.section-desc` + bottom-border separator), and retitled the two sections "Projects" and "Curated Resources".
- `invests.html` hero "Join the Discord" button restyled to match the homepage `.btn-discord` (blue `--discord` background, white text, inline Discord SVG logo, lift-and-glow hover); the secondary "Explore the projects" button aligned to the homepage secondary style.
- `index.html` both "Join the Discord" buttons repointed from the external `discord.gg/sKGKC3JFSE` invite to the internal `discord.html` page (removed `target="_blank"`/`rel`, now same-site navigation).
- `codes.html` reformatted to the invests/discord layout: removed the "Developer tools & AI prompts" hero badge and both hero CTA buttons, replaced `.section-head` with the discord-style `.section-header` (Title/Description/separator), and merged its duplicate `html {}` rules.
- `youtube.html` reformatted the same way: removed the "▶ Subscribe & watch" hero badge and added a "Channels" `.section-header` (Title/Description/separator) above the channel grid.
- `discord.html` hero heading changed from "Join Azqato's Discord" to "Azqato's Discord".
- `about.html` removed the "Investor, Developer, Community Builder" hero badge.
- `links.html` removed the "Find me everywhere" hero badge and changed the hero description from "All my platforms, communities, and channels in one place." to "Find me everywhere."

### Removed
- Unused `.hero-badge` / `.hero-badge::before` / `@keyframes pulse` CSS from `invests.html`, `codes.html`, and `youtube.html` (badge markup removed on those pages). The same now-unused CSS remains in `about.html` and `links.html` and is flagged for later cleanup.

---

## [2.6.14] - 2026-07-08

### Changed
- Merged two adjacent `html { }` rules in `invests.html` into a single block (`overflow-y: scroll` + `scroll-behavior: smooth`). Cosmetic cleanup only; no behavior change.

---

## [2.6.13] - 2026-07-08

### Changed
- Updated the Leveraged Strategies featured card link on `invests.html` from `https://azqato.github.io/leveraged-strategies/` to `https://azqato.github.io/leverage/`.

---

## [2.6.12] - 2026-07-08

### Fixed
- **Nav logo position shifted slightly between pages.** `.nav-inner` centers itself with `margin: 0 auto` inside a `max-width: 1100px` wrapper, and Windows Chrome/Edge reserve real horizontal space for a vertical scrollbar only when a page's content is tall enough to scroll. Pages that fit within the viewport (`accounts.html`, `codes.html`, `youtube.html`) had no scrollbar and therefore a few pixels more usable width than longer pages, so the centered nav-inner (and the "Azqato" logo inside it) landed at a slightly different horizontal position depending on page length. Added `html { overflow-y: scroll; }` to every page so the scrollbar gutter is always reserved, whether or not the page actually needs to scroll; confirmed via headless Chrome measurement that `.nav-logo`'s `getBoundingClientRect().left` is now identical across all 12 pages at every tested width.

---

## [2.6.11] - 2026-07-08

### Changed
- Site favicon changed from the ⚡ emoji to 🦁 across all 12 pages (inline SVG data-URI favicon, unchanged everywhere else).
- The "About" card icon in the homepage explore grid (`index.html`) changed from 👋 to 🦁 to match the new favicon.

---

## [2.6.10] - 2026-07-08

### Fixed
- Corrected the Azqato Mixes channel link on `youtube.html` to `https://www.youtube.com/@AzqatoMixes` (previously pointed to the wrong channel).

---

## [2.6.9] - 2026-07-08

### Changed
- Reordered the `invests.html` featured project cards so the strategy projects lead: Stocks, Leveraged Strategies, ComposerAtlas, Net Worth Tracker, VIX Strategy, Stock Screener.
- Renamed the "Stock Methodology" featured card to "Stocks" on `invests.html` (link target unchanged: `https://azqato.github.io/stocks/`). The `projects.html` card retains its original name.

---

## [2.6.8] - 2026-07-08

### Added
- `invests.html` redesigned to lead with Azqato's own investing projects. New hero with a primary "Join the Discord" CTA and a secondary "Explore the projects" CTA that smooth-scrolls to the project showcase.
- Featured project showcase: six large clickable cards (Net Worth Tracker, VIX Strategy, ComposerAtlas, Stock Methodology, Stock Screener, Leveraged Strategies), each with a description, hover lift, gradient top-bar, and sliding arrow. Card icons mirror each project's own favicon emoji.
- Stock Screener link (`https://azqato.github.io/stocks/screener.html`) added to the projects list.
- Writing-style guard: a `.githooks/pre-commit` hook that blocks any commit introducing an em dash into an HTML or documentation file, enforcing the no-em-dash policy in the Writing Style section of `docs/PRD.md`. Enabled per clone with `git config core.hooksPath .githooks`.

### Changed
- Curated resource grid moved below the project showcase under a new "Curated Resources" heading; the old text-only "Azqato's Projects" resource card was replaced by the featured cards.

### Fixed
- Removed a stray em dash from a historical patch note entry in `docs/PATCHNOTES.md` (grid-collapse fix description), bringing all documentation into compliance with the no-em-dash policy.

---

## [2.6.7] - 2026-07-05

### Added
- ProteinPulse project card: browser-based calorie and protein tracker with daily logging, customizable goals, a carry-forward model, and weekly and monthly graphs. Fully client-side with Excel import and export. Tagged `Tools` and `Health`. Live at `https://azqato.github.io/protein/`.
- `Health` added as a new filter tag category.

---

<!-- Template for future entries:

## [x.y.z] - YYYY-MM-DD

### Added
-

### Changed
-

### Fixed
-

### Removed
-

-->
