# Patch Notes

All notable changes to the Azqato Portfolio are documented here.
Format: `[version] - YYYY-MM-DD`

---

## [2.12.5] - 2026-10-02

### Changed
- `music.html`: the render loop pauses while the tab is hidden and resumes when it comes back; a
visitor who pressed Pause stays paused (build pass, item 15c).

---

## [2.9.5] - 2026-10-02

### Changed
- `music.html`: no pulsing unless the fire is firing. The background, horizon, floor grid and panel
brightness envelopes are multiplied by `fireGate`, which eases in and out over 250 ms so the gate
itself makes no hard step. Measured in headless Edge: idle luminance spread 0.0086 to 0.0038; worst
playing step 0.0042 (reserved version, Roadmap v2.9.5).

---

## [2.12.4] - 2026-10-02

### Changed
- `.githooks/pre-commit`: a commit that stages a root page is blocked when `tools/build-nav.py
--check` finds any page's nav out of date (build pass, item 15b).
- `docs/PRD.md`: the build pass approved; the owner's answers recorded; the build pass table.

---

## [2.12.3] - 2026-10-02

### Added
- `docs/DESIGN.md`: One palette for the whole site, the owner's picks for every color role in dark
and light (Roadmap at a glance, item 4; Invests P15), with contrast figures.

### Changed
- `docs/PRD.md`: P15 and Roadmap at a glance item 4 marked decided.

---

## [2.12.2] - 2026-10-02

### Changed
- `docs/PRD.md` Part 2, the owner's review of Invests' drafted sections, all suggestions accepted:
Tenet 3 and the "nothing from azqato.com" and "nothing pushed" non-goals removed (D22); Tenet 2 is
now "push only on the owner's word"; Tenet 5 softened for the shared look; a seventh goal (one look
with azqato.com); goals, user stories and success criteria marked met or open; analytics-based
metrics postponed; the press release dated; FAQ 7 mentions Cloudflare's beacon. Earlier text kept.
- `docs/PRD.md` Roadmap at a glance: the full review moves after item 15; the Discord card check is
done; new item 21 (a brand per section, an emoji per page). `docs/TODO.md`: the brand, mascot and
analytics questions answered.

---

## [2.12.1] - 2026-10-02

### Changed
- `docs/PRD.md`: new Roadmap at a glance at the top of the Roadmap, listing every open item from both
halves of the site in one suggested order (now, one site and one look, Invests content, the main
site, later), each pointing at its detail. Part 2's Current phase now leads with what's next and
lists its updates newest first; its Future updates run P12 to P17 in order. The deferred "no
light/dark toggle" row and the "SKIP cleanup" row are marked as reversed and done. No item was
removed.

---

## [2.12.0] - 2026-10-02

### Changed
- Docs merged: Azqato Invests' README, LICENSE and six documents (`invests/docs/`) merged word for
word into the main README, LICENSE and docs, by the owner's decision, keeping the five-document set
closed. `docs/PRD.md` gained Part 2: Azqato Invests (its PRD, HOSTING.md, README and TODO.md);
`docs/DESIGN.md` gained Azqato Invests Visual System (its DESIGN.md and UI-REVIEW.md); its patch
notes are the Azqato Invests history at the end of this file; `LICENSE.md` carries its terms.
- New decision, PRD Part 2, D22: the main site's rules, docs and design win. Supersedes its D5 and
Tenet 3.
- Version numbers combined: Invests changes are main 2.x entries from now on (its own line ended at
v1.1.1).
- `docs/PRD.md`: Part 1 places that still described `invests.html` as the investing hub marked with
the current state; Documentation Versus Reality rows 37 to 39; Current phase and the Which document
table point at Part 2. `docs/DESIGN.md`: rule 6 (no light theme) and the two `invests.html` cards
marked. `README.md`: the Invests row and the investor line describe the 21-page site.
- `invests/scripts/check.py`, `browser.py`: docstrings point at the PRD's Part 2.

### Removed
- `invests/README.md`, `invests/LICENSE.md` and `invests/docs/` (PRD, DESIGN, PATCHNOTES, HOSTING,
TODO, UI-REVIEW), after a script confirmed every paragraph and table row is in the merged docs.

---

## [2.11.3] - 2026-10-02

### Changed
- Azqato Invests v1.1.0: its sections are grouped by topic (Individual Stocks, Indices & ETFs, VIX
Strategy, Leveraged Strategies, Resources) at new addresses; the old ones were live about an hour
and get no redirects (owner's decision). See invests/docs/PATCHNOTES.md.
- Roadmap (Future updates): the Invests top bar and theme button across the whole site, clean
addresses for every page (`/discord` instead of `discord.html`), and the Invests footer across the
whole site.

---

## [2.11.2] - 2026-10-02

### Changed
- Azqato Invests v1.0.1: the pager buttons fit their text, with Next at the right edge; the gap above
the pager on Home and Resources matches the other pages; the sidebar's "Educational use only. / Not
financial advice." note sits at the bottom of the sidebar on two lines.
- The working notes from the merge (HANDOVER.md, never committed) moved into invests/docs/PRD.md
and were deleted. The post-launch list (old-site redirects, the two dead Resources links, deleting
the empty Azqato/invests repository after testing) is on the invests roadmap (P13).

---

## [2.11.1] - 2026-10-02

### Changed
- `invests/` in this repository is now the single source of truth for Azqato Invests. The separate
local repository it was built in is retired and will be deleted; nothing is edited there.
- invests/docs/PRD.md: Repository Hygiene, the Runbook's Local setup, Build and Deploy, and Rollback
describe working in `invests/` here instead of copying from the separate repository.

### Deployed
- Pushed 2026-10-02 (v2.11.0 and v2.11.1); Azqato Invests is live at https://azqato.com/invests/.
Post-deploy check: all 43 served files under invests/ match the local copies byte for byte;
https://azqato.com/invests and /invests.html answer 301 to /invests/ in one hop (`_redirects` works);
https://azqato.github.io/invests.html redirects to invests/index.html. In headless Edge, light and
dark: Home, the Screener (data loaded) and the VIX Dashboard (LIVE) show no script errors.

---

## [2.11.0] - 2026-10-02

Azqato Invests moves in. The investing site built in its own repository (stocks, vix and leverage
merged with this site's invests.html, 21 pages) now lives in `invests/`, served at
https://azqato.com/invests/. It is self-contained for now: its pages, assets, generator, checks and
docs are all inside the folder, and its own docs (invests/docs/PRD.md) govern it. Folding it into
this site's structure is planned for later. Its history stays in its own repository.

### Added
- `invests/`: the 21 pages, assets, sitemap.xml, scripts and docs of Azqato Invests.
- `_redirects`: Cloudflare Pages rules sending `/invests` and `/invests.html` to `/invests/` in one hop,
so the old page and the new folder never compete for the address.
- robots.txt: a second Sitemap line for https://azqato.com/invests/sitemap.xml.

### Changed
- `invests.html` is now a one-file redirect page to `invests/` (the first compatibility entry under the
removal policy). Its content lives on in the new Home and Resources pages, word for word.
- The nav's Invests item, the Home explore card and the Links page button point at `invests/`
(tools/build-nav.py updated and rerun).
- sitemap.xml: the Invests entry is https://azqato.com/invests/.
- Links to the new site use `invests/index.html`, so they also work when a page is opened from disk
(a folder link there shows a file listing); Cloudflare Pages serves it as /invests/.
- .githooks/pre-commit skips `invests/inventory/`: word-for-word records of the source pages, not pages.
Azqato Invests' pages are checked as usual (their missing-value mark is now an en dash).
- docs/PRD.md: site structure, folder structure, public surface and compatibility entries.

### Verified
- Served from this repository's root in headless Edge: all 21 pages under /invests/ in light and dark,
no script errors, no failed requests, no links leaving the folder; the screener loads its data and the
VIX tools read LIVE; invests.html lands on /invests/. `python invests/scripts/check.py`: 0 failures.
- Not verified: the `_redirects` rules (Cloudflare only) and the live deploy; nothing is pushed.

---

## [2.10.7] - 2026-09-29

The canonical domain is a **Cloudflare Pages** deployment, not GitHub Pages behind a proxy. Every
document in this project had the hosting wrong, and the v2.9.9 audit had confidently refined it to a
different wrong answer. The owner corrected it in one sentence: "I use Cloudflare Pages instead of
GitHub."

### What is actually true
`azqato.com` and `azqato.github.io` are **two independent deployments of the same commit**, not a
proxy and an origin. Each builds from a push to `main`. Neither knows about the other. That explains
several things this project had recorded as unexplained or had explained wrongly:

- The `.html` to extensionless 307 found during the v2.10.6 deploy check is Cloudflare Pages' default
  URL handling, not a mystery rule somebody added.
- `cfOrigin;dur=0` on every request was not aggressive caching in front of an origin. There is no
  other origin to contact.
- The empty 404 on `azqato.com` against GitHub's styled 404 on `azqato.github.io` is two different
  products, not one product behaving inconsistently.

Corroborated before changing anything: Cloudflare nameservers, Cloudflare IPs on both apex and `www`,
no GitHub headers anywhere in the `azqato.com` response.

### Fixed, and one of these was a real problem
- **`privacy-policy.html` named the wrong data controller.** It said "The site is hosted on GitHub
  Pages" and told readers their server-log data sits with GitHub. For the canonical domain, where
  essentially all traffic goes, it sits with **Cloudflare**. The page now describes both hosts, says
  which serves which address, and says plainly that in practice it means Cloudflare. This shipped
  yesterday in v2.10.5, so it was wrong for one day. It is the one item here with consequences beyond
  tidiness, which is why it was fixed first.
- **The deploy-verification step was checking the wrong host, for a reason that no longer exists.**
  v2.10.3 had deliberately kept the check on `azqato.github.io`, reasoning it was "the origin" and that
  `azqato.com` was a cache that might lie. With two independent deployments, **a green GitHub Pages
  build is not evidence that Cloudflare Pages built anything at all**. The check could have passed
  while the canonical domain sat on a failed build. It now checks `azqato.com` with a cache-buster, and
  says explicitly that each host reports only on itself.
- Architecture diagram, hosting table, third-party data tables, Security Model, and the environments
  note all corrected.

### The CNAME milestone is closed as moot, not deferred
A `CNAME` file is a **GitHub Pages** mechanism. `azqato.com` does not run on GitHub Pages, so the file
would have done nothing for it. Everything the milestone worried about dissolves with the premise: the
DNS never needed confirming for this purpose, the Pages custom-domain field was never going to be
involved, and the redirect-loop risk that justified holding it back could not occur, because there is
no proxy relationship to loop through. The milestone's real goal, making `azqato.com` canonical, was
already met by what shipped on 2026-09-28.

The caution cost nothing and was reasonable given what was believed. But the entire analysis, several
hundred words across three documents, rested on an assumption about infrastructure that is described
nowhere in this repository and was never flagged as an assumption. **When a plan depends on how
something outside the repository is wired, ask before writing the plan.**

### A constraint that turned out to be false
Both the Security Model and the constraints table said no CSP was possible because GitHub Pages cannot
send custom response headers. True of `azqato.github.io`. **False of `azqato.com`**, which runs on
Cloudflare Pages and supports a `_headers` file. Nothing was added, and going without a CSP is still
defensible on a static site with no user input. The change is that it is now a decision rather than a
limitation, and the documents say so.

### Changed
- **Music page sharing copy**, at the owner's request, reframed around why the page exists rather than
  what it does. `og:title` is now "A Concert Stage Built to Showcase the Music"; the description leads
  with Azqato building the page to showcase his music. Re-ran the v2.10.4 compliance gate: 43 and 172
  characters, no site name in `og:title`.

### Decided
- **Internal links keep their `.html`.** Each internal click on `azqato.com` therefore takes a 307 to
  the extensionless form. It costs a few milliseconds. Dropping the extensions would mean changing the
  nav generator and every page body, and would stop the site working when a page is opened straight
  from disk, which is how it has always been developed. Canonical and `og:url` already point at the
  extensionless destination, so shared links and crawlers are unaffected. Not revisited unless the
  development workflow changes.

---

## [2.10.6] - 2026-09-28

Canonical and `og:url` repointed at the URLs `azqato.com` actually serves. A same-day fix to a defect
introduced by v2.10.4, found by verifying the deploy rather than assuming it.

### The defect
v2.10.4 wrote `https://azqato.com/projects.html` into every canonical and `og:url` tag. Checking the
live site afterwards showed that `azqato.com` **307-redirects `/projects.html` to `/projects`**. There
is a Cloudflare rule stripping the extension, which nobody had recorded anywhere, and the audit never
saw it because it was reading the repository rather than the responses.

So all 11 non-index pages were declaring a canonical URL that immediately redirects. That is a
self-defeating signal: the tag says "the authoritative address is X", and X replies "no, it is Y". A
crawler will usually follow it and land in the right place, but a canonical is a statement about the
preferred address, and pointing it at a redirect weakens the one thing it exists to assert. The
sitemap had the same 11 URLs and the same problem.

### Changed
- All 11 non-index pages: `rel="canonical"` and `og:url` drop the `.html`.
- `sitemap.xml`: the same 11 `<loc>` values, with a comment recording why the URLs are extensionless
  so the next person does not "fix" them back.
- `index.html` was already correct. It declared `https://azqato.com/`, which returns 200 directly.

Verified on both hosts before changing anything: the extensionless form returns 200 on `azqato.com`
and on `azqato.github.io`, because GitHub Pages serves `/projects` for `projects.html` natively. The
declared URLs are therefore correct on the origin as well, which matters while the `CNAME` is still
outstanding.

### Not changed
Internal nav and body links still use `.html`. On `azqato.com` every internal click therefore takes a
307 before landing. That is a pre-existing condition of the Cloudflare rule rather than anything this
batch introduced, and changing it means touching the nav generator and every page body, which is a
separate decision. Recorded in `docs/TODO.md`.

### Also verified, and one trap recorded
Every declared canonical URL and every `sitemap.xml` entry was resolved against both hosts after the
deploy: 12 of 12 return 200 directly, with no redirect, on `azqato.com` and on `azqato.github.io`.

The Cloudflare analytics beacon was re-checked at the same time and **nearly produced a false
correction.** A plain `curl https://azqato.com/` returns a page with no beacon in it, which looks like
proof the analytics had been switched off and the privacy policy shipped hours earlier was wrong. It
is not. Cloudflare injects the beacon only when the request carries an `Accept: text/html` header,
which every real browser sends and `curl` does not. With the header it appears deterministically, on
`azqato.com` and never on `azqato.github.io`. The privacy policy is accurate as written. The check is
recorded in the PRD Security Model so the next person does not "fix" a correct page on the strength of
a bare `curl`.

### Worth keeping
The deploy check is what caught this. Confirming that a page went live is a weaker check than asking
whether the thing shipped is actually correct against the live site, and the second one is what found
a redirect rule that exists in nobody's documentation. The gap was not in the code; it was that the
head tags were written from the repository's filenames without ever asking what the canonical host
does with them.

---

## [2.10.5] - 2026-09-28

`privacy-policy.html` rewritten to describe this site rather than a generic one. The page was the last
piece of the analytics decision: v2.10.0 fixed the copy that claimed the site had no analytics, but the
privacy policy is the page a reader actually goes to when they want to know, and it was still generated
boilerplate from 2024 describing a site with ads, accounts and cookies. 14,212 bytes down to 13,381,
which is the right direction, because the old page was longer for being generic rather than for saying
more.

### Removed
- **Consent**, which described a log-in flow that does not exist.
- **Google DoubleClick DART Cookie**, **Advertising Partners** and **Third Party Privacy Policies**,
  all of which described ad networks this site has never carried.
- **Cookies and Web Beacons**, which explained cookie handling for a site that sets none.
- **How We Use Your Information**, a list of uses for information that is never collected.

A policy that describes the wrong site is worse than a short one. It is confidently wrong about exactly
the thing the reader came to check, and every false protection in it makes the true statements next to
it harder to believe.

### Added
- **The short version**, at the top, stating plainly that there are no accounts, forms, comments,
  newsletters or ads, no cookies set by the site, and no marketing trackers, then naming the three
  things that do see a visitor: the host, the analytics on the main domain, and the embedded players.
- **Web server logs.** GitHub Pages records requests as any web server does, including IP address,
  user agent, page and referrer. That is hosting infrastructure rather than a choice made here, and
  GitHub controls that data under its own policy.
- **Analytics on azqato.com.** The real disclosure, and the reason this milestone existed. It names
  Cloudflare, says the script is injected at the edge before the page reaches the visitor, and is
  specific about what kind of analytics it is, because "analytics" covers very different things: it is
  cookieless, does not fingerprint, does not build a profile, does not follow anyone between sites and
  is not shared with advertisers. It then says any blocker stops it and nothing on the site breaks,
  which is true and is the part most policies leave out.
- **Embedded players on the Music page.** Mixcloud and YouTube are loaded directly by the browser, so
  they see the visitor's IP and may set their own cookies, and this happens on page load rather than on
  play. No other page loads anything third party, and the one locally served track involves nobody.
- **Your rights over your data.** States the GDPR and CCPA rights, then refuses the usual dodge: this
  site holds no personal data to hand over or delete because it collects none, and the data that does
  exist sits with GitHub, Cloudflare, Mixcloud and YouTube as separate controllers, so a request is
  best made to them directly.
- **Copyright**, pointing at `LICENSE.md`, closing the last place the site implied its source was free
  to reuse.
- **Changes and contact**, noting that the revision history is public so any change to this page can be
  read in the repository, and ending by saying the page has not been reviewed by a lawyer and is not
  legal advice.

### Kept
- Children's Information, Affiliate Links, Financial Disclaimer and Entertainment Purposes, which were
  the four sections that were already accurate. The affiliate section gained a sentence naming where
  the links actually appear, which is the Support page and parts of Invests.

### Changed
- Hero: "Last updated: 2024. Accessible from azqato.github.io" became "Last updated: 28 September 2026.
  Applies to azqato.com and azqato.github.io, which serve the same site."

---

## [2.10.4] - 2026-09-28

Page heads: titles, social sharing tags, meta descriptions and canonical URLs, on all 12 pages. The
item with the actual payoff in this batch. Before this, every link shared to Discord rendered as a bare
URL with no title card, on a site whose primary call to action is its Discord page, and all 12 browser
tabs truncated to the same word.

### Added
Nine tags in every head, verified by count on each page rather than by spot-check: `<title>`,
`<meta name="description">`, `<link rel="canonical">`, `og:title`, `og:description`, `og:url`,
`og:type`, `og:site_name`, `twitter:card`.

- All `og:url` and `canonical` values are absolute on `https://azqato.com/`, the canonical domain
  decided at the audit. They are correct today: that domain already serves this site through
  Cloudflare, and the `CNAME` decision that is still outstanding changes which host is formally
  authoritative, not whether the address works.
- **No `og:image`, which is the specification rather than an omission.** The documentation spec puts
  images off by default, so `twitter:card` is `summary` rather than `summary_large_image`. Cards render
  as text. Adding an image later changes both settings together and needs a real per-page image or one
  credible default, not a logo stretched to fit.

### Changed
All 12 titles, from brand-first with a pipe (`Azqato | Projects`) to page-first with a suffix:

| Page | Was | Now |
|------|-----|-----|
| `index.html` | Azqato \| Welcome | Azqato - Communities, Projects, Music |
| `about.html` | Azqato \| About | About - Azqato |
| `discord.html` | Azqato \| Discord | Discord Communities - Azqato |
| `invests.html` | Azqato \| Invests | Investing Tools and Resources - Azqato |
| `codes.html` | Azqato \| Codes | AI Prompts and Coding Tools - Azqato |
| `music.html` | Azqato \| Music | Music and DJ Mixes - Azqato |
| `links.html` | Azqato \| Links | All Links - Azqato |
| `projects.html` | Azqato \| Projects | Projects - Azqato |
| `youtube.html` | Azqato \| YouTube | YouTube Channels - Azqato |
| `support.html` | Azqato \| Support | Support the Work - Azqato |
| `accounts.html` | Azqato \| Accounts | Gaming Accounts - Azqato |
| `privacy-policy.html` | Azqato \| Privacy Policy | Privacy Policy - Azqato |

The two that identified nothing to a stranger, "Welcome" and "Codes", now say what the page is. The
longest title is 38 characters against a 60 character budget, and no two pages share their first 30
characters, which is roughly what a tab shows.

### How it was applied
By script, with a compliance gate that ran to completion before a single file was written. The gate
failed the entire run on any title over 60 characters, any `og:title` over 70, any description over
200, an `og:title` containing the site name, a non-index title missing the suffix, two pages sharing
their first 30 characters, or a placeholder title. It passed on the first complete run. The ordering is
the part worth repeating: a script that validates all of its input before touching any of 12 files
cannot leave the repository half-edited.

### Verified
- `python tools/build-nav.py --check` clean, which matters because the nav block sits in all 12 heads.
- Browser test in headless Edge against a local server on `index`, `projects`, `music` and
  `privacy-policy`. All render correctly, with the music page's stage, lasers, local track, both
  Mixcloud embeds and the visualizer mode buttons intact.
- Still outstanding, because it cannot be done before deploying: paste two or three live URLs into
  Discord and look at the cards. That is the only check that tests what this milestone is for.

---

## [2.10.3] - 2026-09-28

Canonical domain, repository side. **Partial by design: the `CNAME` file was deliberately not created.**

### Changed
- `sitemap.xml`: all 12 `<loc>` values repointed from `azqato.github.io` to `azqato.com`, with a
  comment recording that the canonical domain was decided on 2026-09-28.
- `robots.txt`: the `Sitemap:` line and the header comment repointed.
- `README.md`: the live link is now `https://azqato.com/`.
- `docs/PRD.md`: the public-surface definition, the compatibility-entry example, the deploy step, the
  Environments table, Monitoring, the north-star metric, the press release dateline and its call to
  action. The unresolved note asking whether `azqato.com` was related to this repository was marked
  resolved: it is this repository, served through Cloudflare. The absence of a `CNAME` had been read as
  evidence the domain was unrelated, which was wrong.

### Not changed, on purpose
The `CNAME` file. It is the one change on the roadmap that can take the site down, and it depends on
the DNS records and the GitHub Pages custom-domain setting, both of which live outside this repository
and neither of which could be confirmed. Everything above is a text edit one revert undoes.

This split is why the batch is coherent rather than contradictory. The owner had excluded v2.10.3 from
the batch to avoid exactly this risk, which was sound, but v2.10.4 writes `azqato.com` into 12 page
heads, and shipping that while the sitemap still said `azqato.github.io` would have left the site
declaring one canonical address in its heads and another in its sitemap. That is worse than the
ambiguity it started with: two hosts merely competing is something a crawler resolves conservatively,
whereas an active contradiction invites it to pick, and it may not pick the intended one. Splitting on
the line of what needs DNS, rather than on the milestone boundary, let the risky part wait while the
rest shipped consistently.

### Deploy verification stays on the origin
The runbook still says to confirm a deploy by opening `azqato.github.io` rather than `azqato.com`, and
that is now a documented decision rather than a leftover. Cloudflare sits in front of the canonical
domain and caches, so a stale page there says nothing about whether GitHub Pages published, and a fresh
one might be a cache hit from before the push. The origin answers the question the check is asking.

---

## [2.10.2] - 2026-09-28

`.gitattributes` added at root, pinning `* text=auto eol=lf` with explicit `binary` lines for `*.mp3`,
`*.jpg`, `*.jpeg`, `*.png`, `*.gif` and `*.ico`.

### The finding that prompted this was wrong, and the correction is the useful part
The v2.9.9 audit recorded that `music.html` was committed with CRLF while every other text file was LF,
and scheduled a "deliberately noisy" commit that would rewrite all 12 pages. That was checked properly
before running, with `git ls-files --eol`, which is the authoritative test. **Every committed blob in
this repository was already LF, `music.html` included.** The CRLF existed only in the working tree, on
`music.html` and `.vscode/settings.json`.

What had been keeping the repository clean was `core.autocrlf=true` in the local git config, which
converted silently on the way in. That is not part of the repository. A second machine, a CI runner or
a fresh clone with a different setting would have committed CRLF, and nobody would have noticed until
the diff arrived.

So this file does not repair a broken repository. It moves a guarantee that was an accident of one
machine's configuration into the repository, where every clone gets it. That is a better reason than
the one the audit gave.

`git add --renormalize .` produced **zero changes**. The predicted 12-file diff never existed. The
sequencing advice that put this milestone first cost nothing and was sound reasoning, but it was
reasoning built on a premise that was cheap to check and had not been.

The lesson worth keeping: `git status` and editor line-ending indicators describe the working tree, not
the repository. Only `git ls-files --eol` answers what is actually committed.

### Note
`tools/build-nav.py` still contains its deliberate code to preserve whatever line ending each file
already uses. That note in the audit was accurate. It is belt-and-braces now rather than a workaround,
and it was left alone.

---

## [2.10.1] - 2026-09-28

`tools/build-nav.py`: the `SKIP` set listed `nav-extraction-test.html` and `reduced-motion-test.html`,
neither of which has existed for some time. Leaving them there implied a rule the project no longer
has, and the next reader would have had to check whether those files mattered.

`SKIP` is now an empty set with a comment naming what used to be in it and why it is gone. Emptying it
rather than deleting the mechanism costs one line and is the better shape: the loop that reads it is
untouched, so the next person who genuinely needs to exclude a page adds a filename instead of
rebuilding the feature. No behavioral change, since the script only ever iterated files that exist.
`python tools/build-nav.py --check` reports the nav is up to date in every page, which is the same
answer it gave before, and that is the point.

Offered at the v2.9.9 audit and deferred with "revisit this later", then pulled back into scope the
same day when the owner scheduled the batch.

---

## [2.10.0] - 2026-09-28

Copy alignment, applied immediately after the v2.9.9 audit closed. The audit put six questions to the
owner and all six were answered the same day. Five of the six became scheduled Roadmap milestones
(v2.10.2 through v2.10.5). This entry covers the one part that was pure documentation and so was
applied rather than scheduled: the sentences that had become false the moment a licence existed and
the moment the Cloudflare beacon was found.

### Changed
- **External FAQ, the open-source answer.** It read "Yes. The site and nearly every project on it are
  open source at github.com/Azqato." Now separates the two things it had run together: the individual
  projects are mostly public repositories carrying their own licences, while this site is
  source-available rather than open source, readable on purpose but reserved, with `LICENSE.md` setting
  out what is granted and an invitation to ask for anything else.
- **Press release boilerplate.** "Everything he builds is open source, runs entirely in the browser,
  and is free to use" became "Everything he builds runs entirely in the browser and is free to use, and
  most of the projects are public on GitHub."
- **Security Model, what the site collects.** It read "None. No analytics, no cookies set by the site,
  no tracking pixels, no forms, and no accounts." That was true of the source and false of what a
  visitor to the canonical domain receives. It now states both: nothing from the site's own code, plus
  GitHub's server-level request logging and the Cloudflare Web Analytics beacon injected into every
  page served from `azqato.com`.
- **External FAQ, "Why no analytics?" became "What analytics does the site use?"** The old answer
  defended a position the site no longer holds. The honest description is now "no tracking of its own,
  plus cookieless aggregate counts from the CDN", and the entry says so rather than defending the
  earlier absolute claim, because Tenet 6 does not leave room for a claim that is technically about the
  source while being false about what a visitor gets.
- **North star metric.** The paragraph explaining the metric's weakness assumed no analytics existed at
  all. Annotated: Cloudflare Web Analytics does hold real page-level visit counts that were never taken
  into account when the metric was designed. Whether to start reading them, and whether the metric
  should be redefined around them, is left unresolved rather than answered in passing.
- `docs/TODO.md`: the six decided items moved out of Decisions Waiting On The Owner and into a Decided
  section pointing at the Roadmap milestones, leaving three genuinely open items.

### Decisions recorded
All six are written up in full, with effort estimates, sequencing and open risks, under Decided At The
v2.9.9 Audit in the PRD Roadmap. In brief: keep all rights reserved; `azqato.com` is canonical; keep
the Cloudflare beacon and fix the copy; add the full sharing-tag set to all 12 pages; fix all 12 page
titles in the same pass; add `.gitattributes` and normalize everything. The smaller cleanups in
`docs/TODO.md` were offered and deferred.

### Not changed
- Nothing outside `/docs` and `README.md` was touched **in this version**. No page head, no title,
  no `CNAME`, no `.gitattributes`, and no `privacy-policy.html`. All of those except the `CNAME`
  shipped later the same day as v2.10.1 through v2.10.5. Those are the four scheduled milestones, and the
  recommended order puts the renormalization first so its whitespace-only diff across all 12 pages
  does not contaminate the head edits.
- No version control command that changes state was run.

---

## [2.9.9] - 2026-09-28

Full documentation audit, the first since v2.8.5 on 2026-08-24, covering the 17 commits since.
Read every document in `/docs` in full plus the README, then checked them against the code in
three passes. Four files created, 13 new discrepancies recorded, six questions left open for the
owner. No page was browser-tested, because a documentation-only change is a minor update under
the cadence policy this entry adopts.

### Added
- `LICENSE.md` at the repository root. The project had no licence text anywhere, while the README
  invited people to copy the source. Adopted the all rights reserved, source-available default,
  with sections covering no licence granted, AI search and automated access, no waiver, permission,
  platform terms, third-party content, no warranty, and the not-financial-advice disclaimer. AI
  referencing and quoting are granted; substitution is not; training data is routed to a request
  on the public issue tracker.
- `robots.txt` at the root. Confirmed missing by a live 404 on both hosts, not just absent from the
  repository. Fully open to every crawler with no exclusions, carrying a comment that says the
  openness is deliberate and that `LICENSE.md` wins if the two ever look like they disagree.
- `sitemap.xml` at the root, listing all 12 pages, which is every page: none sits behind a sign-in.
  Each `lastmod` is that page's last commit date read from git, not today's date. `robots.txt`
  names it on a `Sitemap:` line.
- `docs/TODO.md`. Seeded from open items already scattered through the other documents plus what
  this audit turned up. It is a holding place, explicitly not an instruction list, and it is never
  consolidated, merged, moved, or deleted.
- PRD: six new sections. **Verification Environment** (verify locally, never against production;
  `file://` does not count for `music.html` because it disables audio routing). **Testing Cadence**
  (see Changed). **Repository Hygiene** (a policy record, reported as a table of 10 rules against
  their actual state). **Licensing**. **Social Sharing Tags**. **Page Titles**, which this project had never recorded and   fails on all 12 pages, every one of them brand-first with a pipe separator so that every tab
  truncates to the same string.
- PRD Roadmap: a **Future updates** section, opening with a proposal for a progress dashboard built
  from the prompt at `https://azqato.github.io/prompts/p/progress-dashboard.html`. Added rather than
  adopted as a rule because this project has no `CLAUDE.md` and so no existing dashboard convention.
- PRD Roadmap: a **Verification checklist** naming the seven areas whose claims were not read in code
  at this audit and are carried forward on an earlier audit's authority.
- PRD: Open Questions 9 through 14, and Documentation Versus Reality rows 21 through 33.

### Changed
- **Testing Cadence replaced the project's rule of that kind.** The old rule required a browser check
  after every edit with no project-specific reason recorded for the frequency. The replaced wording
  was, in How to Verify a Change: "There is no test suite, so verification is manual and specific. Do
  all of these:", together with the Monitoring table row "Console errors | DevTools Console on the
  changed page | After each change". The default now applies: browser tests use headless Edge with a
  unique `--user-data-dir`; an assumption check and one browser test run immediately before a major
  update ships; minor updates (wording, docs, comments, patch notes) ship without either; batched
  edits are tested once; and confirming a deploy arrived is not a test. The verification steps
  themselves are unchanged, and the section now says the cadence governs when they run, not what
  they contain.
- **Never Do These: the visualizer rule had inverted and was rewritten.** It read "Never claim in copy
  that the music visualizer reacts to the audio. It does not." It does. `music.html` builds a real
  `AnalyserNode`, calls `createMediaElementSource` on the native player, and drives the lights from
  `getByteFrequencyData` every frame. The rule now draws the real line: true for the one same-origin
  track, false for the cross-origin Mixcloud and YouTube embeds, and false on `file://` where
  `canRouteAudio` is false and the page says so. The old wording is quoted in place. Following the old
  rule would have required deleting true sentences from the README and the FAQ.
- **README** made precise about analytics instead of left inaccurate. It claimed "no analytics, and no
  tracking" without qualification. `azqato.com` and `www.azqato.com` both serve a Cloudflare Web
  Analytics beacon, injected at the edge and not present in this repository's source;
  `azqato.github.io` is clean. The README now distinguishes what the site's own code does from what
  the `azqato.com` edge adds. Whether to keep the beacon is Open Question 12.
- **README**: "The source is open. Read it, copy it, or use it as a starting point for your own site"
  became a neutral pointer to `LICENSE.md`. A bare grant with no licence text behind it is an
  ambiguity, and leaving it beside a reserved-rights licence would mislead a reader in one direction
  or the other. The new wording asserts neither posture, pending Open Question 9.
- **Documentation Process: the document set is five, not four.** The old text read "Exactly four
  documents. No fifth file is created inside `/docs`", and maintenance rule 7 read "Never create a new
  `.md` file in `/docs`. Add a section to one of the three instead." Both contradicted the newly
  required `docs/TODO.md` and were updated to name it as the last addition.
- DESIGN.md: four stale claims corrected. `styles.css` given as 2,282 bytes, actually 2,887 since the
  v2.8.7 reduced-motion block. Only `lang-js` and `lang-html` described as in use; `lang-cs` joined
  them in v2.9.8. `.track-tag` described as reading "Drives the visualizer", text removed in v2.9.4;
  it carries the track credit now. Build rule 4 said "Any new page copies the nav block verbatim from
  an existing page... There is no shared nav include yet", false since v2.8.8 and contradicting
  DESIGN.md's own navigation section; replaced with the generator workflow, because as written it
  instructed the reader to do the one thing Never Do These forbids.
- PRD: `music.html` given as "roughly 91,000 bytes" in the Build section against 114 KB in nine other
  places. It is 117,417 bytes. Shared CSS given as 2.3 KB, now 2.8 KB.
- PRD: the Current Phase claim that "nothing is waiting on a decision any more" was true after v2.8.9
  and is not now.
- PRD: `2.9.5` added to the reserved version numbers, held for the visualizer brightness gate.
- PRD: the em-dash compliance paragraph still named `.vscode/recentfedsummary.MD` as out of
  compliance; that file was deleted in v2.8.9. Replaced with this audit's sweep result, which is zero
  violations across every tracked file and the four new ones, with six exempt occurrences inside
  backtick code spans where the rule names the character it prohibits.
- PRD: the Browser Testing section said the Edge binary path "has not been verified on this machine".
  It was verified at this audit.
- PRD: the press release said fourteen tools; it is fifteen as of v2.9.7.
- PRD: Working Practice gained a step to check `docs/TODO.md` before pushing, an explicit "ask before
  pushing" step, and a note that confirming the deploy afterwards is a comparison rather than a test.
- PRD: How An Audit Is Run gained five steps covering reading TODO.md, checking that required files
  are actually served rather than merely mentioned, keeping a policy record separate from an action,
  and naming what was not verified.

### Fixed
- The PRD's open question about whether `azqato.com` is related to this repository, which reasoned
  from the absence of a `CNAME` file that it was not. It is: the domain serves this exact site through
  Cloudflare, all 12 page footers link it, and git history shows a `CNAME` created and then deleted.
  Answering it opened a larger one, because the repository now demonstrably has two live hosts and no
  recorded canonical. See Open Question 10.

### Not changed, on purpose
- **No `CLAUDE.md` and no `/dashboard` were created.** An audit does not create a `CLAUDE.md` for a
  project that has none, and with no existing progress-dashboard convention the standing rule was not
  added either; a Future Updates roadmap entry proposes one instead.
- **No `.gitattributes` was created**, though its absence is a real gap: `music.html` is committed CRLF
  while everything else is LF, and `tools/build-nav.py` deliberately preserves per-file endings. A
  blanket `eol=lf` would rewrite all 12 pages in one diff. Repository Hygiene is a policy record, not
  an action, so this is recorded as a discrepancy and as Open Question 13.
- **No page head was edited**, although all 12 pages carry zero `og:` tags, zero `twitter:` tags, no
  meta description, and no canonical tag, and all 12 titles are brand-first. Social Sharing Tags and
  Page Titles are both policy records, and the specification puts a page edit outside an audit. The
  work was decided on the same day and is scheduled as Roadmap v2.10.4.
- **`privacy-policy.html` was left as it is** at the audit. Boilerplate describing Google DART cookies
  and ad networks this site does not have, recorded as row 17 and Open Question 6 since the v2.8.5
  audit. The owner decided on 2026-09-28 to rewrite it, scheduled as Roadmap v2.10.5, and it is now
  the page that has to carry the real Cloudflare disclosure.
- **`tools/build-nav.py`'s `SKIP` set** still names two files that no longer exist. Harmless dead
  configuration in a working script, outside this audit's write scope, logged in `docs/TODO.md`.
- **No version control command that changes state was run.** Nothing was staged, committed, pushed, or
  untracked by the audit.

---

## [2.9.8] - 2026-09-28

### Added: Automate Fundamentals on the Projects grid
The v2.9.7 note said this project was left off `projects.html` because that page's card
array requires a `github` field and there is no public repository. The rule below settles
that, so the card is now on both pages.

- Added a fifteenth entry to the `PROJECTS` array, placed first to match its position in
  the Invests grid.

### Changed: the `github` field falls back to the project's own site
**Adopted as a standing rule.** When a project has no public repository, its `github` field
points at the project's own site and `demo` is set to the same URL.

- This is not a new pattern so much as a named one. Two entries already did it, No Fee
  Apartments and LV Guest List, both external commercial sites. Automate Fundamentals is
  the third and the first that is private rather than external.
- The GitHub icon button was hardcoded to `title="View on GitHub"`, which became false the
  moment the link went anywhere else, and had been false on those two cards for as long as
  they have existed. `buildCard` now tests the `github` value against
  `^https://github.com/` and labels the button "No public repository, opens the project
  site" when it does not match.
- The label is derived from the URL rather than from a flag on the entry, because a flag is
  a second thing to remember and would eventually disagree with the link it describes.
- The button also gained an `aria-label`. A `title` alone is not reliably announced, and an
  unlabelled link containing only an SVG reads as nothing useful.
- The octocat mark itself still renders on all three. It marks the repository slot rather
  than the destination, and relabeling it is what keeps that honest.

### Documentation
- `docs/PRD.md`: the project count moved from 14 to 15 in the page inventory, in F1, and in
  the array-order list.
- `docs/PRD.md`: the sentence describing the two external-site entries is replaced by a
  full statement of the fallback rule, how the card detects it, and why it is read off the
  host instead of a flag.
- `docs/PRD.md`: the `PROJECTS` schema comment for `github` now describes the fallback.
- The new entry is tagged `lang-cs`, for .NET. That class has been defined in the page's
  stylesheet since it was written but no project had used it, so this is the first card to
  render the C# green.

---

## [2.9.7] - 2026-09-28

### Added: Automate Fundamentals on the Invests page
A new site is in progress at `automatefundamentals.com`, and the Invests project grid is
where it belongs.

- Added a seventh card to the `invests.html` project grid, placed first because it is the
  newest work and the rest of the grid has no meaningful order. Icon, title, arrow and
  description follow the existing `project-card` pattern exactly, so no CSS changed.
- The description says what the site says about itself, a strategy builder for investors
  who work from earnings reports rather than charts, and states plainly that it is in free
  beta. The site is a beta with its trading and backtesting features still hypothetical,
  and a card that implied a finished product would be wrong within a week.
- This is the first project card on the site that points at a domain other than
  `azqato.github.io`. It keeps `target="_blank" rel="noopener"` like every other outbound
  link on the page, so nothing about the link handling is special.
- Not added to `projects.html`. That page's card array carries a `github` field alongside
  `demo`, and there is no public repository to put in it yet.

### Documentation
- `docs/PRD.md`: the page inventory said the Invests page carries six project cards.

---

## [2.9.6] - 2026-09-08

### Added: `.gitignore` now excludes the local brand folder
A brand and merchandise concept folder was built in the working tree: three planning
documents, 100 concept files under `brand/assets/`, and a generated reading page. It is
deliberately not part of this repository.

- Added `brand/` and `tools/build-brand-page.py` to `.gitignore`. GitHub Pages serves this
  repository publicly from the root, so a committed `brand/` would be readable at
  `azqato.com/brand/`, including supplier notes, priority scores, and an unresolved question
  about the mascot artwork's licensing provenance.
- Ignoring it is the point rather than a side effect. Leaving the folder merely unstaged
  means a single `git add .` publishes it, and this folder will sit in the working tree for
  months. The generator is ignored alongside it because it only builds that folder and would
  be a dangling reference in a fresh clone.
- The trade is that none of it is backed up by git. That is recorded in the folder's own
  review document so it is not discovered the hard way.

### Documentation
- `docs/PRD.md`: the folder tree now lists `brand/` and its contents under the existing
  untracked-and-local-only block, with the reasoning for the exclusion and a note that
  reversing it is a two-line edit.
- `docs/PRD.md`: the `.gitignore` line in the tree said "env-file patterns only", which
  stopped being true with this change.
- No page changed and nothing on the deployed site is affected. Version 2.9.5 stays reserved
  for the roadmap item that gates the visualizer's brightness modulation on the fire.

---

## [2.9.4] - 2026-08-30

### Fixed: the screens pulsed with the music
The v2.9.3 work capped the rate of discrete flashes. It did nothing for this, because this was continuous modulation rather than flashing and no rate limit touches it.

The cause was one deliberate decision applied in the wrong place. `sampleAudio()` smooths asymmetrically on purpose: it jumps 75 percent of the way to a new peak in a single frame so that a kick reads as impact. That is right for anything that moves and wrong for anything that glows, because the same step spread across a large area of the screen is seen as the whole picture pulsing rather than as a hit landing.

- Added two slow luminance envelopes, `envBroad` and `envLow`: the same signal, symmetrically smoothed with roughly a 300 ms time constant and frame-rate corrected. Brightness now reads from these; motion still reads from `favg()`. Fast things stay fast, lit things swell.
- Repointed the four brightness terms at them: panel bloom, the white wash over the main panel, the background radial gradient with its horizon glow, and the stage floor grid.
- Reduced the background's swing (0.45 to 0.30 on the inner stop, 0.20 to 0.14 on the mid stop). It is the largest lit area on the page, so it contributes most to the sensation of the room breathing.

Measured by driving the real `updateEnvelopes()` at simulated refresh rates, worst single-frame change in the panel bloom term:

| Display | Largest one-frame luminance step | `t` advance over 4 s |
|---|---|---|
| 60 Hz | 0.0073 | 239.1 |
| 120 Hz | 0.0037 | 239.6 |
| 144 Hz | 0.0031 | 239.6 |

Before the change a single attack could move that term by roughly 0.22 in one frame, so the worst case is about thirty times smaller. The envelope still reaches the same range (0.001 to 0.601 at every refresh rate), so nothing is flattened; it only gets there smoothly.

### Fixed: second instance of the frame-count defect
`t` was a plain frame counter incremented once per `requestAnimationFrame`, and fourteen call sites multiply it by a coefficient tuned on a 60 Hz panel (`t * 0.018`, `t * 0.05`, and so on). The whole idle animation therefore ran about 2.4 times too fast on a 144 Hz display. `t` now advances in 60 fps-equivalent frames, which keeps every one of those coefficients correct without touching them; the table above shows it advancing identically at all three rates. `glTime` had the same defect via a hardcoded `1 / 60` per frame and is now on the wall clock too.

This is the same class of bug as the beat refractory fixed in v2.9.3. Anything counted in frames is a rate that changes with the viewer's monitor.

### Changed
- Removed the "Drives the visualizer" text under the track. The span is now empty by default and populates only with the serve-over-http warning when the audio path is unavailable. The credit line above it is unchanged.

---

## [2.9.3] - 2026-08-30

### Fixed
- **The stage was flashing above the WCAG 2.3.1 limit on any high-refresh display, and the page's
  own documentation said otherwise.** Every rate in the light rig was a frame count, and
  `requestAnimationFrame` runs at the display's refresh rate, so the 26-frame beat refractory was
  the documented 433 ms only on a 60 Hz panel. Driving the real detector with a worst-case signal
  that clears its threshold on every frame:

  | Display | Before | After | Limit |
  |---|---|---|---|
  | 60 Hz | 2.40 /s | **1.70 /s** | 3 /s |
  | 120 Hz | **4.70 /s** | **1.70 /s** | 3 /s |
  | 144 Hz | **5.60 /s** | **1.70 /s** | 3 /s |

  Every rate is now wall-clock milliseconds, so the rig behaves identically on a phone, a TV and a
  144 Hz monitor, and the refractory is 600 ms rather than 433, which sits under the limit instead
  of on it. The per-frame decays are refresh-rate independent too, so a pulse now lasts as long on a
  gaming monitor as on a TV instead of being half as long and twice as sharp.
- **Screen-mode cycling had the same defect.** `MODE_LEN` was 1800 frames, commented as "~30 s at 60
  fps", which meant the whole centre panel swapped every 15 seconds on a 120 Hz display. Now 30
  seconds on a clock.

### Changed
- **Luminance amplitude cut across the rig, because rate is only half of photosensitivity.** The
  full-width light pump is halved (0.55 to 0.26) with its gradient stops reduced, the white wash
  over the main panel cut to roughly a third (0.30 to 0.12 on the flash term, 0.10 to 0.05 on the
  ambient term), panel bloom's beat and flash contributions roughly halved, and the laser response
  softened (0.35 to 0.22). The rare full-screen drop flash is gated to one per 8 seconds rather than
  one per 5.
- **Impact is carried by motion, not brightness.** The beat-synced panel zoom, the crowd bounce and
  the laser beam count are untouched. They read as impact and cannot flicker.
- **The screen only flashes when the pyro is firing.** Both the full-width light pump and the white
  wash over the main panel are now gated on `fireActive`, which is true while any of the four jets
  is actually burning. A flash with nothing visibly causing it reads as a glitch; the same flash
  with fire behind it reads as the blast throwing light across the room, which is what it was always
  meant to be. The flag is set in `drawFire()`, which runs after the flashes in the frame, so the
  gate uses the previous frame's state. That is 16 ms at 60 fps and is not perceivable. It also
  narrows the photosensitivity exposure further, since the flash can no longer fire during quiet
  passages when the jets are down.
- **The track credit now names the artists.** The tag under the title reads "EOB, Azqato" at all
  times. It previously read "Drives the visualizer", and was overwritten with a serve-over-http
  warning on local file loads, so the artists were never credited on the page at all. The warning
  moved to its own muted line underneath rather than being dropped.

### Notes
- **This closes an accessibility item that had been open since v2.8.7** and was listed in both
  DESIGN.md and the PRD as "the beat flash rate has never been measured". It has now been measured,
  and it failed. The pause control from v2.8.7 was the mitigation; it was never the fix.
- **The earlier documentation was confidently wrong.** DESIGN.md and the PRD both described the rate
  as "at the limit rather than under it" and treated that as the safe case. It was over the limit by
  a wide margin on hardware a large share of visitors own. Both documents are corrected rather than
  quietly updated.
- **The general lesson, which is not specific to this page: a rate expressed in frames is not a
  rate.** Anything that has to respect a per-second limit must be measured against a clock, and on
  more than one refresh rate, or the measurement only describes the machine it was taken on.
- **Verified in headless Edge** (never Chrome), before and after, by driving the page's real
  `updateBeat` at simulated 60, 120 and 144 Hz rather than by reading the constants. The credit line
  and the http note were checked in the rendered DOM in the same pass.

## [2.9.2] - 2026-08-30

### Fixed: the logarithmic band mapping collapsed at the low end
v2.9.1 claimed to give the bass its fair share of the display. It did not, and the claim was wrong rather than merely optimistic.

- Each band is about 10 percent wider than the one below it, but 10 percent of 30 Hz is 3 Hz and one bin at `fftSize` 1024 spans about 47 Hz. The first fourteen bands therefore all rounded to the same bin and moved as a single value. Instrumenting the running page showed it directly: `bandBins` read `1,1,1,1,1,1,1` and bands 0 through 5 all held an identical `0.28`.
- Each band is now forced to advance at least one bin. That makes the low end linear and the top end logarithmic, which is what a mel or bark scale does and what the v2.9.1 change was supposed to deliver. After the fix `bandBins` reads `1,2,3,4,5,6,7,8,9` and the bands hold distinct values.

### Fixed: the page failed invisibly on a local file
- Opened over `file://`, the browser treats the same-folder mp3 as cross-origin, so the page skips Web Audio and runs the synthetic idle animation. That is the correct behaviour and it has been in place since v2.8.10, but nothing on screen said so: the tag under the track still read "Drives the visualizer", and a stage running its idle loop looks exactly like a stage that is ignoring the music. The tag now reads "Serve over http to make the visualizer react" whenever the audio path is unavailable.
- This is the difference between a feature that is broken and a feature that is not connected, and the page was giving no way to tell them apart. On the deployed site, which is HTTPS, the condition never arises.

### Verification note
Instrumenting the live page found both of the above; the v2.9.1 measurement did not, because it tested the detector algorithm against decoded audio rather than the running page. Both are worth doing and neither substitutes for the other: the offline harness proves the maths, the live probe proves the wiring. The kick detector's behaviour in a real browser, with a real audio device, is still unconfirmed. Headless Edge has no audio device and its analyser returns a frozen snapshot, so it cannot answer that question, and the deployed site is now the place to check it.

---

## [2.9.1] - 2026-08-30

### Fixed: the visualizer now reads as reacting to the music
v2.8.10 wired a real analyser and the stage moved with the audio, but it did not look like it was listening: the kick did not land and a drum hit was not distinguishable from a pad. Four causes, all real, all now fixed.

- **Two low-pass filters in series.** `analyser.smoothingTimeConstant` was 0.8 and `freq()` smoothed again at `0.72 / 0.28`. A kick is a transient, and each filter rounded off its leading edge; together they removed it. The analyser now smooths at 0.35 and `freq()` smooths asymmetrically instead: it jumps to a new peak at `0.25 / 0.75` and falls back at `0.82 / 0.18`. Attack survives, decay stays smooth, and the leading edge of a hit is the part the eye reads as impact.
- **Linear band mapping.** 64 bands spread evenly across the spectrum put the entire kick region inside band 0 while sixty-odd bands displayed hiss. Bands are now spaced logarithmically from 30 Hz to 16 kHz, built once from the actual sample rate, which is how hearing divides pitch and therefore how the display has to divide it.
- **Resolution too coarse to see a kick.** `fftSize` was 256, about 190 Hz per bin, wider than the whole kick band. Now 1024. Deliberately not 2048: frequency resolution trades against time resolution, and a 2048 window spans 46 ms, longer than a frame at 60 fps, which smears the transients this change exists to preserve.
- **Averaging within a band.** Band level is now the peak of its bins rather than the mean, so one loud bin is not averaged away by quiet neighbours.

### Added: kick detection
- Added a second analyser dedicated to finding kicks: `fftSize` 2048 for about 23 Hz per bin, `smoothingTimeConstant` 0, tapping the same source but not connected to the output. It takes the opposite resolution trade from the general analyser because it needs frequency precision rather than time precision.
- Detection is by onset, not by level. On a modern master the bass sits near the ceiling almost continuously, so "is the bass loud" is true nearly always and fires on nothing. A kick is instead identified by its attack: a sharp rise in 30-150 Hz energy over the last few frames, with a threshold that adapts to the track's own recent behaviour so quiet passages still register and loud ones do not fire continuously. Ported from `feature/native-audio-player`, where the constants were tuned with `ffmpeg` against a known tempo.
- `beatPulse` now drives the screen zoom, the crowd bounce, the laser intensity, and the WebGL clock, so a hit moves several independent things at once. That is what reads as reaction; a single brightness change does not.
- Added the loud-moment gate from the same branch: a full brightness flash fires only when loudness is a genuine statistical outlier against a slowly adapting baseline, coincides with an actual kick, and has not fired in the last 5 seconds. It reads as a drop rather than as every beat.
- Replaced the old `drawBeatFlash` trigger, which was `favg(0, 5) >= 0.76`. On a loud master that test is either true continuously or never true, and both look identical to no reaction at all.

### Verified
Measured offline rather than judged by eye. The mp3 was decoded in the browser and the detector run over a 2048-point FFT at a 60 Hz hop, reproducing exactly what the page sees per frame:

| Measure | Result |
|---------|--------|
| Hits detected | 92 over 44.5 s |
| Rate | 124.0 per minute |
| Median interval | 0.480 s, implying 125.0 BPM |
| Intervals in 380-620 ms | 94 percent |
| Interval p10 / p90 | 0.430 s / 0.560 s |

124 BPM against the 124-128 BPM the branch measured independently for its own test track. The detector is locking to the real beat, not firing on noise.

### Accessibility
- **WCAG 2.3.1 measured, not assumed.** The 26-frame refractory caps beat-driven events at 2.3 per second in principle, and the measurement found a maximum of 3 in any one-second window, which is at the limit rather than under it. So the full-width light pump is scaled to 0.55 on the audio path and the impact is carried by the screen zoom, the crowd, and the lasers, which are motion rather than luminance. The one true full-screen brightness flash remains gated to at most one per 5 seconds. There is a comment in the source saying not to raise the pump; it is load-bearing.
- The reduced-motion behaviour from v2.8.7 is unchanged: the loop still starts paused when the system asks for reduced motion, and the pause control still stops everything.

### Performance
- `freq()` called `getByteFrequencyData` on every band, so the full spectrum was refetched 64 times per frame and more once `favg()` was counted. Sampling now happens once per frame in `sampleAudio()` and `freq()` only reads the result.

### Documentation
- Closed milestone v2.9.1 in `docs/PRD.md` and recorded the measured figures, so the next person tuning this has a baseline to compare against rather than an opinion.
- Updated the signal sections of `docs/PRD.md` and `docs/DESIGN.md`, and removed the DESIGN.md warning against tuning visuals to the old signal, which no longer applies.
- `music.html` is now 110 KB, still the one acknowledged exception to the 50 KB page budget.

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

---

## Azqato Invests history (v0.1.0 to v1.1.1, before the docs merge)

Azqato Invests' own PATCHNOTES.md, merged word for word (Merged 2026-10-02); headings moved down a level and prefixed "Invests". Its versions were a separate line; from 2.12.0 Invests changes are main entries above. "PRD.md" and the other file names here mean the invests files, now merged (PRD Part 2).

Every change to this project, newest first. Versions follow semantic versioning and stay below 1.0.0 until the site launches (see Conventions in PRD.md). Dates come from the system clock.

### Invests v1.1.1 - 2026-10-02 - Documentation audit

#### Changed

- README.md rewritten for the live site: the address, the five sections as they are now, the status, and the doc list (HOSTING.md marked as a record).
- LICENSE.md: permission requests go to https://github.com/Azqato/azqato.github.io/issues; github.com/Azqato/invests no longer exists.
- PRD.md: every statement that described the site as unpublished, the old section names or the separate repository is marked with the current state, original text kept (Decisions D4, D5, D12, D20; Constraints; Feature list; Runbook; Monitoring; Security; Deprecation and Removal, including the retired pre-v1.1.0 addresses; Press Release and FAQ facts). Roadmap items P13 to P17 moved from inside Writing Style to Future updates; P13.4 (delete the empty repository) marked done. New Documentation Versus Reality entries 13 to 17 and a new entry under Documentation audits.
- DESIGN.md: the intro, Sidebar, Breadcrumbs and pager, Search, Theme button, the 640px breakpoint and the measured pairings note brought up to date for v1.0.1 and v1.1.0.
- HOSTING.md and UI-REVIEW.md marked as records, with what came after.

#### Tested

- Docs only: no page or script changed, so no browser test (Testing Cadence). `python scripts/check.py` still passes.

### Invests v1.1.0 - 2026-10-02 - Sections by topic

#### Changed

- Navigation restructured at the author's request: the sidebar groups are Individual Stocks (Overview, Philosophy, Stock metrics, Screener), Indices & ETFs (Overview, Market Overview), VIX Strategy (Overview, VIX Dashboard, VIX Custom builder), Leveraged Strategies (Overview and the six strategies) and Resources (Curated resources, Finviz and Seeking Alpha setup guides, FAQ). Before: Learn, Tools, Strategies, Resources, FAQ. Each topic group's first page is its landing page: the old Learn Overview became Individual Stocks, and Index & ETF methodology became Indices & ETFs. No page content changed.
- Addresses moved with the groups: learn/, tools/, strategies/ and faq.html are gone; pages live in stocks/, indices/, vix/, leveraged/ and resources/ (PRD, Site map). No redirects, by the author's decision: the old addresses had been live about an hour.
- Breadcrumbs read Home > group > page; the pager follows the sidebar order; the Home cards, the footer's FAQ link, search's popular pages and the browser tests use the new addresses.
- PRD: Site map, Folder structure and the D7 redirect list updated; roadmap items P15 (azqato.com's colors), P16 (one VIX page) and P17 (SEO and landing-page review) added.

#### Tested

- `python scripts/check.py`: 21 pages, 0 failures (0 broken internal links). `python scripts/browser.py`: 0 failures, the usual 9 notes.

### Invests v1.0.1 - 2026-10-02 - Pager and sidebar note

#### Changed

- Pager: each button fits its text instead of taking half the page. Next sits at the right edge even when it's alone (Home), Previous at the left (FAQ), so there's no empty half-width column (assets/css/site.css).
- Home and Resources: the gap above the pager is 32px like every other page; invests.html's last section no longer adds its 48px bottom padding there.
- Sidebar: the "Educational use only. Not financial advice." note sits at the bottom of the sidebar, on two lines (scripts/site.py wraps it in `.site-sidebar-foot`; site.css pins it). When open groups fill the sidebar it follows them, 32px below.
- Docs: the session handover (HANDOVER.md, never committed) moved into PRD.md: the live state under Current phase, P10 marked done for steps 1 to 3, P13 (post-launch list: D7 redirects, the author's review, the two dead Resources links, deleting the empty Azqato/invests repository after testing) and P14 (folding into azqato.com's structure), and four Never rules (the private project and the backup bundle, staging by name, stopping only your own servers). Repository Hygiene and the Runbook describe `invests/` as the single source of truth.

#### Tested

- `python scripts/check.py`: 21 pages, 0 failures. `python scripts/browser.py`: 0 failures, the usual 9 notes. Pager measured in headless Edge at 1550px and 390px on Home, Learn/Metrics and FAQ; sidebar note measured at the bottom of the sidebar at 2100x1250.

### Invests v1.0.0 - 2026-10-02 - Live

#### Changed

- Published at https://azqato.com/invests/ as part of azqato.github.io v2.11.0 (D20 go-ahead). Post-deploy check passed (PRD, Current phase). The separate repository is retired; `invests/` in azqato.github.io is the single source of truth.

### Invests v0.18.0 - 2026-10-02 - Merging into the main site

#### Changed

- Hosting (Question 18, option D, D21): the site moves into the azqato.github.io repository as a self-contained `invests/` folder, served at https://azqato.com/invests/. `SITE_URL` in scripts/site.py is now https://azqato.com/invests/, and canonical links, og:url and sitemap.xml use azqato.com's clean addresses (for example https://azqato.com/invests/learn/metrics).
- History (Question 16): the private project's name was replaced with "private project" in every past commit with `git filter-repo`; all 24 commits kept with new ids. A backup of the old history stays outside the repository and is never pushed.
- Runbook: Deploy and Rollback rewritten for the main repository.
- Missing values show an en dash (–) instead of an em dash on the screener and Market Overview, 27 places (Question 19), so the main repository's em-dash hook passes. check.py now fails on any em dash in a page file.

### Invests v0.17.1 - 2026-10-02 - Hosting analysis

#### Added

- docs/HOSTING.md: the hosting options (GitHub Pages, a Cloudflare Worker, publishing into the main repo's invests/ folder, a full merge, a subdomain), compared, with a recommendation (Question 18).
- The author's answers to Questions 16 and 17 recorded in PRD.md; Question 18 added.

### Invests v0.17.0 - 2026-10-02 - Site-wide checks, documentation and publish plan (P7 to P9)

Development plan P7 (steps 1 to 8), P8 and P9, at the author's request. Nothing was pushed or published (D20). Each step's findings are recorded under its phase in docs/PRD.md.

#### Added

- Every page has `<link rel="canonical">` and og:url with its published address under https://azqato.github.io/invests/ (`SITE_URL` and `page_url()` in scripts/site.py). All six sharing tags are now on all 21 pages.
- sitemap.xml at the root, listing the 21 pages, generated by scripts/site.py. No robots.txt: azqato.github.io owns the origin (PRD, P9.3).
- The D7 redirect list (19 old addresses, one hop each) and the redirect-page mechanism for GitHub Pages, under Deprecation and Removal in docs/PRD.md.
- Runbook: Build (every script, in order, with the expected output), Deploy and Rollback for GitHub Pages (written, not run), more Common errors.
- Conventions, filled in from the code and the git history.
- Questions 16 (what becomes public with the repository: its history and the Template Interface files) and 17 (azqato.com/invests and invests.html, with a recommendation), both for the author.
- LICENSE.md names the issue tracker for permission requests: https://github.com/Azqato/invests/issues, open once the repository is public.
- `.gitignore`: `__pycache__/`.

#### Changed

- The author's private project is no longer named anywhere in the docs (P9.6), because github.com/Azqato/invests, created by the author on 2026-10-02, will be public. D2 is unchanged in meaning; earlier commits in the local history still contain the name (Question 16).
- PRD: the milestone table (M4 to M8 complete, M9 and M10 in progress), Current phase, the verification checklist (every section dated 2026-10-02), System architecture, Tech stack, Folder structure, Data models, Security, Repository Hygiene, Social Sharing Tags, Metrics and Documentation Versus Reality (entries 5, 7 and 8 resolved; 9 to 12 added).
- DESIGN.md: the Home page, Footer, Breakpoints, focus and Page layouts notes marked with what was built, the earlier text kept.
- README.md: status and live-site lines brought up to date; a link to docs/UI-REVIEW.md.

#### Fixed

- Screener layout shift: Lighthouse measured CLS 0.175 on mobile, because the disclaimer under the table moved down when the data arrived. The table area now holds 70vh of room while loading; CLS 0.003 on the rerun.
- Feed text in HTML: the screener and Market Overview put tickers and names from the stock feeds into the page with `innerHTML` unescaped. scripts/site.py now wraps their `res.json()` in `azqClean()`, which removes `<` and `>` from every text value in a fetched feed.
- `.gitignore`'s comment named tools/snapshot.py; it's scripts/snapshot.py.

#### Removed

- The empty `previews/` folder left from the width previews.

#### Checks run

- Fresh snapshots (stocks 860ee2b9, vix 37eeadd1, leverage c86321cd, azqato.github.io 58767b54), then `python scripts/inventory.py`, `python scripts/site.py` (21 pages, 242 search entries, 47 em dashes replaced) and `python scripts/check.py`: 21 pages, 0 failures.
- `python scripts/browser.py` after the fixes: 0 failures, the same 9 notes as before (feeds deliberately blocked in the test, the stocks feed's 2026-09-30 data, the VIX allorigins fallback).
- Lighthouse 13.5.0, mobile, in Edge: Home LCP 1.7 s, CLS 0, TBT 0 ms; Screener LCP 2.1 s, CLS 0.003, TBT 0 ms; 9 Sig LCP 1.7 s, CLS 0, TBT 0 ms. Accessibility, best practices and SEO 100 on all three.
- Keyboard and focus in headless Edge: skip link, focus order, drawer and search focus in and out, landmarks, accessible names.
- Outside links: 96 checked, 2 dead (dividendstocksonline.com, expired certificate; www.denvercondomania.com, times out), both source content on Resources, left as they are for P11 (D19). 8 more refused automated requests, which isn't a dead link.
- Em dashes: none in this site's own text or any page. Secrets: none.
- Not browser-tested: the canonical, og:url and sitemap additions are head tags and a new file, checked by script only; Deploy and Rollback weren't run (D20).

### Invests v0.16.1 - 2026-10-02 - VIX Custom builder order

#### Changed

- VIX Custom builder: "Your Categories" (the ticker inputs) sits above "Your Custom Allocation", after the reading and tier line, at the author's request.

#### Fixed

- The VIX section headings inside a header row (such as "Your Categories") no longer carry the article heading's 48px top margin, which left a large gap at the top of their box.

### Invests v0.16.0 - 2026-10-02 - UI review fixes

Every decision in docs/UI-REVIEW.md, built and then tested. Its "Done" section has the full detail.

#### Added

- An "Azqato.com" group in the sidebar with azqato.com's links, shown on phones, where its top bar is hidden.
- Three Home cards, in the source's card style, for the sections no source card covered: Market Overview & VIX tools, Curated Resources and FAQ.
- site.js labels each VIX table cell with its column heading, for the phone layout.
- A "Swipe sideways for more columns →" line above the screener table on phones.

#### Changed

- Page width, option C: content runs full width to 1400px on every page; the stocks pages' 820px and the VIX pages' 1100px caps are lifted; Resources and the FAQ give back the empty "On this page" column; Market Overview's grid fills the width.
- One footer per page: the source footers that repeat it are hidden (kept in the page), and the VIX disclaimer and copyright lines move into the site footer.
- Home: one grid of 10 project cards instead of "Explore the site" plus "Projects"; emoji icons share one size and tile; on phones the icon sits beside the title.
- No text under 12px (scripts/site.py `min_font`, and site.css).
- Sidebar groups collapse unless they hold the current page.
- Phones: breadcrumb, "On this page", footer and sidebar links at least 24px tall; FAQ toggles 48px.
- Stocks table figures use the site font with tabular digits.
- The stocks pages' tag ("Strategy Q&A" and the others) is a plain label, not a pill.
- Stock metrics: subtitles line up with their headings.
- Screener: the disclaimer is a left-aligned paragraph; the ticker column casts a shadow; on phones the tier chips wrap and the filter box is full width.
- Market Overview: card names wrap.
- Resources: masonry columns.
- VIX tables are stacked cards on phones.
- VIX Custom builder: the result (reading, tier, chart, breakdown) comes before the ticker inputs, and its tier line reads like the Dashboard's.
- VIX pages: mono font is SF Mono, Consolas or Liberation Mono; the tool sections have less padding.
- VIX Strategy: site headings, borders and card styles.
- Leverage callouts: 15px text.

#### Fixed

- The VIX tools showed CACHED on the second page opened within 30 minutes, for the same live reading; a reading under 30 minutes old now shows LIVE (STALE still marks an old one).
- QQQ and TQQQ looked underlined (Courier New's Q).
- Home and Resources card titles sat far below their icons (the article heading margin).
- Market Overview card names were cut off on phones.

#### Removed

- The "Explore the site" tiles on Home (this site's own, not source content; their sections are cards in the one grid).
- The width previews (previews/, scripts/previews.py) and check.py's skip for them, once option C was chosen.

### Invests v0.15.0 - 2026-10-02 - Width previews

#### Added

- previews/: three page-width options (A, grids wide with prose capped; B, one column of about 1100px; C, everything full width), each on Market Overview, Stock metrics and Resources, built by scripts/previews.py. The real pages are unchanged.

#### Changed

- scripts/check.py skips previews/.

### Invests v0.14.4 - 2026-10-02 - UI review

#### Added

- docs/UI-REVIEW.md: a full-scroll review of every page in headless Edge, with the issues found and suggested fixes, for the author to decide on. No page was changed.
- The author's decisions on the review, in docs/UI-REVIEW.md.

### Invests v0.14.3 - 2026-10-02 - VIX hero size

#### Changed

- The VIX pages' sections have 40px top and bottom padding instead of the source's landing-page spacing, and a section's first heading drops the template's 48px top margin.
- The VIX Strategy hero fits its content instead of filling 90% of the window (the source built it as a full-page landing section), in both themes, at the author's request.

### Invests v0.14.2 - 2026-10-02 - Rule: no data feeds here

#### Added

- PRD Constraints: this repo holds no data feeds, data files or data-fetching jobs; the only automation is the GitHub Pages or Cloudflare Pages build that publishes the site.

### Invests v0.14.1 - 2026-10-02 - Roadmap: old repos

#### Added

- PRD Future updates, P12: after launch, the stocks and vix repos become redirects and data feeds only, and the VIX feed gets a second source in place of allorigins.

### Invests v0.14.0 - 2026-10-02 - Wider layout and light-mode legibility

#### Changed

- Page content starts at the sidebar instead of being centered, and uses up to 1400px (Home's and the VIX pages' own centered containers too), at the author's request.
- Light mode: darker body and muted text, stronger lines, larger card text.
- VIX Strategy in light mode: a light hero background, a dark headline, and no scanlines (the source's were made for its dark page). Dark mode is unchanged.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.13.0 - 2026-10-02 - Tests for P2 to P6

#### Added

- scripts/browser.py: browser tests in headless Edge (page errors in both themes and at phone width, sideways scroll, WCAG AA text contrast, the shell's controls, the FAQ, live data and feed fallbacks).

#### Changed

- Light-theme data colors darkened to pass contrast, the screener tiers and VIX ticker colors given light counterparts, white text on the light VIX button, and a lighter red for the stocks badge in dark (DESIGN.md, Data colors).
- The VIX ticker colors in strategy.js and custom.js are CSS variables with the source colors as fallback; chart.js reads their values for the donut (scripts/site.py patches the copies).

#### Fixed

- The leverage pages' risk notices were laid out as a row by the template's `.callout`, which made TQQQ FTLT and Holy Grail scroll sideways on phones.
- scripts/check.py compares text with spaces and punctuation removed, so items split across tags are no longer reported missing.

#### Removed

- None.

### Invests v0.12.0 - 2026-10-02 - P6: Tools

#### Added

- Screener, Market Overview, VIX Dashboard and VIX Custom builder, in tools/, with their scripts in assets/js/stocks/ and assets/js/vix/.
- An integrity hash and `crossorigin` on Chart.js 4.4.0 (Question 12).

#### Changed

- The stocks tools' local `data/` fallback now points to azqato.github.io/stocks/data/, since this site has no data folder; the first source is still raw.githubusercontent.com.
- The VIX pages load the reading from azqato.github.io/vix/data/vix.js instead of a local `data/vix.js`.
- The VIX donut chart's center text, label and border colors follow the theme (assets/js/vix/chart.js).
- 12 em dashes in the tool pages and their inline scripts, and 1 in screener.js, were replaced (Question 14). The dashes that stand for a missing value ("(-)" in the methodology, and the dash the tools show in empty cells) are kept.
- The screener's links to the Metrics and Indices pages keep opening in a new tab, as in the source.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.11.0 - 2026-10-02 - P5: Strategies

#### Added

- VIX Strategy (strategies/vix.html), with its live VIX reading from azqato.github.io/vix/data/vix.js.
- The leveraged strategies landing and 3 Sig, 6 Sig, 9 Sig, TQQQ FTLT, Holy Grail and HFEA, in strategies/leveraged/.
- An "On Composer Atlas" note on TQQQ FTLT (three strategies), Holy Grail (two) and HFEA (the database page and the symphony id, since Atlas has no link to a single entry; Question 4).

#### Changed

- 19 em dashes in the VIX Strategy page and its inline script, and 15 in the VIX scripts it shares with the tools, were replaced (Question 14; inventory/em-dashes.md lists each one).

#### Fixed

- None.

#### Removed

- None. The leverage sites' main.js isn't carried; it only drove their own navigation.

### Invests v0.10.0 - 2026-10-02 - P4: Learn and FAQ

#### Added

- Learn: the landing (from stocks' home page), Philosophy, Stock metrics, Index & ETF methodology, and the Finviz and Seeking Alpha setup guides, in learn/.
- FAQ (faq.html): all 37 questions and answers, with a filter box and links that open the answer they point to.

#### Changed

- Links between the stocks pages now point to the new addresses; section anchors are unchanged. Relative links between pages in the same folder are written plainly (scripts/site.py).

#### Fixed

- None.

#### Removed

- None. The stocks sidebar's "On This Page" list is replaced by the shell's own; its highlighting code in script.js is carried but finds nothing to highlight.

### Invests v0.9.0 - 2026-10-02 - P3: Home and Resources

#### Added

- Home (index.html): invests.html's intro and Discord button, five new tiles into the site's sections, and all 7 project cards. The Stocks, Stock Screener, VIX Strategy and Leveraged Strategies cards now link inside the site.
- Resources (resources/index.html): all 15 categories, all 71 links (referral links included) and the disclaimer, word for word.

#### Changed

- Links that pointed at the old copies now point at the live sites: azqato.github.io/composer to composeratlas.com, and invests.html's relative `discord.html` to azqato.com/discord.
- Source snapshots refreshed before the move (P1.4); nothing had changed.

#### Fixed

- None.

#### Removed

- None. invests.html's own nav script isn't carried: it only opened azqato.com's menu, which the site's copy of that nav replaces.

### Invests v0.8.0 - 2026-10-02 - P2: the shell

#### Added

- scripts/site.py: builds every page from the source snapshots, with one shared shell (top bar with azqato.com's nav above it, sidebar, breadcrumbs, pager, footer, search dialog) and the source content moved whole inside it. Needs BeautifulSoup 4.
- assets/css: Template Interface's theme.css, base.css and components.css and documentation-site's styles.css (as docs.css), copied unchanged from commit ed840da; site.css, this site's own styles; src-stocks.css, src-vix.css and src-leverage.css, the sources' stylesheets scoped to their content.
- assets/js: theme.js (light and dark, system theme first, adapted from the template's theme-toggle.js), site.js (drawer, "On this page", search, FAQ filter, adapted from documentation-site's script.js), and search-index.js (generated; loads when search first opens).
- A "Skip to content" link (Question 8) and the 💰 favicon.
- `_sources/templateinterface/`: a snapshot of the template files used, at ed840da.

#### Changed

- The Python scripts moved from `tools/` to `scripts/`, since the Tools section's pages live in `tools/`. The docs' references were updated; older patch notes keep the old paths.
- scripts/check.py: skips `assets/` and `scripts/`; the em dash check now fails only on an em dash used as punctuation (followed by a word), so a lone dash standing for a missing value, as the screener shows, passes; inventory items in the source sites' own navigation (region nav or aside) are skipped, since the shell replaces that navigation. The literal em dash left in the script was replaced with its escape.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.7.0 - 2026-10-02 - Host: a new invests repository; stocks stays the data source

#### Added

- None.

#### Changed

- D21 changed: the stocks repository is not renamed. The site lives in its own new `invests` repository with no data feeds; stocks keeps its workflows and data and serves them at azqato.github.io/stocks/data/ (same origin as the site). The earlier D21 text and P9 note are kept, marked as superseded.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.6.0 - 2026-10-02 - Host: the renamed stocks repository

#### Added

- D21: at publish time the stocks repository is renamed to `invests` and becomes Azqato Invests, keeping its data workflows, data and history; a new `stocks` repository holds the redirects. P9 step 1 lists what to check before the rename.

#### Changed

- None.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.5.0 - 2026-10-01 - The remaining open questions answered

#### Added

- Development plan step P7.10: the author reviews the drafted sections once the MVP is ready (Question 15).

#### Changed

- Answered Questions 1, 4, 7, 11, 13, 14 and 15 (recorded in PRD.md). The site will be a GitHub Pages project site at azqato.github.io/invests/ from a public repository named `invests` (D4 updated, old text kept; P9 now checks the collision with invests.html first). HFEA links to its Composer Atlas community entry. Permission requests go to the repository's issue tracker. Traffic is measured only by host counts and search consoles. What's being merged now names alert-on-failure.yml (Documentation Versus Reality entry 3 resolved). Em dashes in moved text are replaced and logged, and tools/check.py now fails on them. The drafted sections wait for review after the MVP.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.4.0 - 2026-10-01 - Development plan P0 and P1: setup, snapshots and inventories

#### Added

- A local git repository (branch `main`, no remote, nothing pushed), with `.gitattributes` pinning LF line endings and `.gitignore` excluding `_sources/`.
- tools/snapshot.py: downloads read-only copies of the source pages, their scripts and stylesheets into `_sources/` and records each commit. First snapshot: stocks 60a599e (12 files), vix cd92561 (8), leverage c86321c (9), azqato.github.io 58767b5 (invests.html).
- tools/inventory.py and inventory/: one inventory per source page, 20 in all, 2,898 items, listing every heading, paragraph, list item, table row, link, control, chart and script in page order with its full text. A check confirmed all 4,096 visible text fragments of the source pages are in the inventories.
- tools/check.py: read-only checks for titles, links, template demo text, em dashes and inventory coverage. Tested against planted failures.

#### Changed

- Answered Questions 2, 3, 5, 6, 8, 9, 10 and 12 (recorded in PRD.md): keep azqato.com's nav (D9 confirmed), section-folder addresses, a local git repository, "Azqato Invests" as the brand, add a skip link, the site's own themes on Home, remove the template's remaining demo parts, and add an integrity hash to Chart.js.
- Findings from P1 recorded: the stocks fallbacks are relative `data/` paths, and azqato.github.io/stocks/data/ can replace them (Background findings, Documentation Versus Reality entry 8); the screener and Market Overview insert feed values with `innerHTML` unescaped (Security); the tools' data colors and the VIX charts' labels (DESIGN.md); 28 visible em dashes in source text (Question 14).
- Milestone M3 complete; M4 in progress. Folder structure, Repository Hygiene, Browser Testing and the Runbook's common errors updated.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.3.0 - 2026-10-01 - Step-by-step development plan

#### Added

- A Development plan in PRD.md's Roadmap, at the author's request: phases P0 to P11 mapped to milestones M3 to M11, each with what it needs first, numbered steps and substeps, and what "done" means. It covers setup and the blocking questions, source snapshots and page inventories, the shell, each section's pages, the tools and their data, site-wide checks, documentation, the publish plan, publishing and the redirects, and the correction pass. It proposes a folder layout pending Question 3.

#### Changed

- None.

#### Fixed

- None.

#### Removed

- None.

### Invests v0.2.0 - 2026-10-01 - First documentation audit: the doc set, and README as the front door

#### Added

- docs/PRD.md: the whole plan from README.md, moved word for word by script (core rule, decisions D1-D20, site map, sources, Composer Atlas, background findings, assumptions, next steps and points to settle), plus every section the documentation prompt requires, from the problem statement to the FAQ. Its Risks and Open Questions section lists 15 numbered questions, each with the default applied meanwhile. Sections the audit drafted (tenets, personas, user stories, goals, success criteria, metrics, press release, FAQ) say so.
- docs/DESIGN.md: the design details and template ratings from README.md, moved word for word, plus the design system read from Template Interface at commit 61acfcb: both palettes with every token's use, typography, spacing, breakpoints, components, accessibility (with contrast ratios measured by script) and motion.
- docs/PATCHNOTES.md: this file.
- docs/TODO.md: the ideas file, with its placeholder only.
- LICENSE.md: all rights reserved, with the AI and search referencing carve-out, no waiver, no warranty, and not financial advice.
- Defaults adopted where the project had no rule, recorded in PRD.md: writing style, browser testing, verification environment, testing cadence, repository hygiene, licensing, social sharing tags, page titles, and deprecation and removal for this site's own pages.
- The audit's date and process, under Documentation audits in PRD.md.

#### Changed

- README.md rewritten as the public front door: what the site is, a plain statement that there's no hosted instance yet (with links to the four current sites), what it will offer, who it's for, status, the core rule in short, and links to the docs. Two lines of the old README weren't moved and are kept here. Its opening line read:
  > Project plan for Azqato Invests: one site, in its own repo, that merges the stocks, vix and leverage sites with the current invests.html page, built on the documentation-site template.

  Its status line read:
  > **Status: paused (2026-10-01).** Planning is done apart from the points the move to an independent repo reopened (see To settle). The documentation prompt is approved but was stopped partway, before it wrote anything; it reruns for the independent repo when you say to resume. No site files exist yet.
- Headings changed in the move: "Assumptions (correct any that are wrong)" became "Assumptions", with "Correct any that are wrong." as its first line; "Next steps" became "Next steps (from the plan)" under the Roadmap; the "To settle along the way:" list sits under Risks and Open Questions.
- Next steps 1 and 2 of the plan are done (resume; move the plan into docs), as noted in the Roadmap.

#### Fixed

- None. The writing-style sweep of README.md, the only text file before the audit, found 0 em dashes, 0 `&mdash;` entities and 0 double hyphens used as punctuation. The new files were swept the same way after writing, with the same result outside the rule text that names the character.

#### Removed

- None. No plan content was removed: a script copied each part of the plan from the original file, and a check confirmed every non-empty line of the old README.md is in PRD.md or DESIGN.md, apart from the two lines quoted above and the headings listed under Changed.

### Invests v0.1.0 - 2026-10-01 - The plan

Reconstructed by the 2026-10-01 audit; the folder has no version history.

#### Added

- README.md with the project plan: the core rule (preserve everything), the decisions, the 21-page site map, the Composer Atlas mapping, the four sources being merged, background findings, assumptions, next steps, points to settle, and ratings of all 21 Template Interface templates.
- D20: everything stays local until the author says otherwise.

#### Changed

- The plan was corrected for the move to an independent repo: D4 and D5 changed (their old text kept after "Before:"), D8 now says the design comes from Template Interface rather than azqato.github.io, D9 and the dark-mode assumption were marked to re-check, and the design details, background findings, next steps and points to settle were updated to match.

#### Fixed

- None.

#### Removed

- From the points to settle: where this site's docs live in the azqato.github.io repo, moot once the site became its own repo. The design detail about extending azqato.github.io's tools/build-nav.py to pages in an `invests/` folder was replaced by one saying this site would carry its own copy of the nav, if D9 stays.
