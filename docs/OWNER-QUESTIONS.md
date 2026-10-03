# Questions for the Owner

Written 2026-10-03, at the end of the 2026-10-02 build pass (main 2.13.1 to 2.14.1). Every decision that waits on you is here, in one place, with the background, the options and my recommendation. Nothing listed here has been changed on the site.

**How to answer.** Reply with the question number and your choice, for example "Q3: A" or "C5: keep with the date". A short reply is enough; "your recommendation" is a valid answer to any of them. Once a question is answered, it gets marked here with the date and moved into the docs it belongs to (PRD or DESIGN).

**Contents**

| # | Topic | Urgency |
|## Answers (2026-10-03), built in 2.15.0

| # | Answer | Done |
|---|---|---|
| Q1 | Ignore for now: Cloudflare takes 6 to 12 hours after the earlier limits fix | Waiting |
| C1, C2 | Recommended wording | Built |
| C3, C4 | Remove | Built |
| C5 | Keep, with "(historical, to 2020)" | Built |
| C6, C8 | Recommended: no change | Nothing to build |
| C7 | Keep the boxes | Nothing to build |
| Q3 | Yes to all | S1 to S6 built. **S7 held:** the FAQ has no topic groups to label (37 numbered items plus two sections), so a grouping is proposed below for your approval |
| Q4 | Yes to all | Built: Stock, Index and VIX Method pages, cards on the three landing pages, old links to moved sections forward to the Method page |
| Q5 | Brighten the dark C#/HTML tags | Built |
| Q6 | Keep music dark, no button | Nothing to build |
| Q7 | Find the correct number and keep it | **12** (the Metrics page, the reference table and the description all say 12; the grid lacked Gross and Net Margin). Grid and text fixed; `check.py` now fails any page saying another number |
| Q8 | Update the .bat | Done (local file) |
| Q9 | Keep the trailing slash | Nothing to build |
| New | VIX Strategy into Indices & ETFs | Built; its address is unchanged |

**S7, proposed FAQ groups (needs your OK):** Selling and holding (when to sell, trims, losers); Building a portfolio (how many stocks, sizing, ETFs vs stocks); Reading the metrics (PEG vs P/E, margins, RSI); Timing (VIX, DCA vs lump sum, IPOs); The long game. Labels only; no question text changes.

---|---|---|
| Q1 | azqato.com isn't deploying | **Urgent:** the canonical site is six versions behind |
| Q2 | Content corrections C1 to C8 (Invests) | Normal |
| Q3 | SEO small fixes S1 to S7 | Normal |
| Q4 | Landing and Method pages L1 to L4, M1 to M3 | Normal |
| Q5 | Projects page language tags below contrast | Low |
| Q6 | Music page: dark only, no theme button | Low (confirm what's built) |
| Q7 | Individual Stocks: "12 metrics" or "10 metrics" | Low |
| Q8 | `test-local-audio.bat` points at the old music address | Low (local file only) |
| Q9 | Trailing slash in the new addresses | Low (confirm what's built) |
| Q10 | The theme button's place | Resolved 2026-10-03 |
| Later | 15d, smoke-test script | Saved for later at your request; listed so it isn't lost |

---

## Q1. azqato.com isn't deploying (urgent)

**What's happening.** azqato.com, the canonical address, is served by Cloudflare. Cloudflare rebuilds the site from GitHub on every push. Since 2.13.5, every build has failed, so azqato.com still shows **2.13.4**. azqato.github.io, which is served by GitHub Pages, has every version through 2.14.1.

**What visitors to azqato.com are missing:**
- The redirects from the old stocks, vix and leverage sites (2.13.5). Those three repos now send visitors to `azqato.com/invests/...` addresses, which work today, because they existed before 2.13.4.
- The combined VIX page (2.13.6). `azqato.com/invests/vix/dashboard.html` still shows the old separate page there, so nothing is broken yet.
- The light theme, the new top bar and the shared `theme.js` (2.13.7).
- Clean addresses (2.13.8). This one matters most: the sitemap, canonical tags and Invests' top bar on GitHub Pages already point at `azqato.com/about/` and the like, and those addresses don't exist on azqato.com until it deploys. Links from azqato.github.io's Invests pages to azqato.com's root pages lead to a 404 until then.
- `music/viz.js` (2.13.9), the move to `tools/invests/` (2.14.0) and the SEO drafts (2.14.1).

**What I can see from here.** GitHub records each Cloudflare build as a check called "Workers Builds: azqato":

| Commit | Version | Result |
|---|---|---|
| 05bcdc1 | 2.13.3 | success |
| 263de07 | 2.13.4 | failure |
| 73f3938 | docs after 2.13.4 | success (this is what's live) |
| 6ef3ac2 | 2.13.5 | failure |
| 9b4adb8 | 2.13.6 | failure |
| c4555fb | 2.13.7 | failure: about 10 minutes queued, then failed the moment it started |
| ac08bcd | docs, after you resolved the Workers limit | failure (2026-10-03, checked after your message) |

A build that fails the instant it starts never reaches our files, which points to the account or the build settings rather than the code. You said you'd resolved the Workers limits from earlier, but the build after that fix failed too. Either the fix hasn't taken effect yet, or something else is wrong as well.

**What I need.** One of these:
- **A (recommended).** Open the Cloudflare dashboard → Workers & Pages → **azqato** → **Deployments / Builds**, open the newest failed build, and paste me its log, or a screenshot of the first red lines. The link for one failed build: https://dash.cloudflare.com/4188e6cecdc9acb8fbb2e0ae1cff7aa8/workers/services/view/azqato/production/builds/99c552b4-8fd9-4ccb-8f1b-d907f84e6a4c
- **B.** On that same page, press **Retry build** on the newest commit. If the limit fix was the cause and it has now taken effect, the retry succeeds, and azqato.com jumps straight to 2.14.1.
- **C.** Give me a Cloudflare API token with Workers read access, and I'll read the logs myself.

**Worth checking while you're there:** the plan's monthly build minutes and builds-per-month counters, and whether a build is stuck "queued". A stuck build can block the ones after it.

**Once it deploys,** I'll check every page and every old address on azqato.com in one pass (each redirect must take one hop), because none of 2.13.5 to 2.14.1 has been checked there yet.

---

## Q2. Content corrections C1 to C8 (Invests)

Background: under the core rule, I can't change source text without your approval. These eight came out of item 11 (2.13.3). They're also in PRD Part 2, P11.

### C1. Holy Grail, Performance Notes: the "no data" sentence is now false
- **Current text:** "No public factsheet data was retrievable (Composer requires authentication). The following observations are drawn from the strategy's structural properties and the academic basis."
- **Why it's wrong now:** since 2.13.3, the page loads Holy Grail's figures live from Composer Atlas, and they show just above this paragraph.
- **Proposed:** "Composer Atlas publishes this strategy's backtest; the figures above load from it. The following observations are drawn from the strategy's structural properties and the academic basis."
- **Options:** A, the proposed text (recommended). B, your own wording. C, leave it, and the page contradicts itself.

### C2. Holy Grail, Risks: same problem
- **Current text:** "No public performance record is available. ... The backtest data on the Composer factsheet was not accessible without authentication."
- **Proposed:** keep the first sentence, because a backtest isn't a live record, which is still true. Replace the last sentence with "Its backtest is on Composer Atlas (above); a backtest is not a live record."
- **Options:** A, the proposed text (recommended). B, your own wording. C, leave it.

### C3. Resources: "Top-rated stocks" (thestreet.com) returns 404
- The link points to TheStreet's top-rated stocks page, which has returned 404 Not Found since at least 2026-10-02.
- **Options:** A, remove it (recommended; it's what we did with the two other dead links in 2.13.3). B, replace it, if you know TheStreet's current ratings page. C, keep it as it is.

### C4. Resources: "Top-rated ETFs" (thestreet.com) returns 404
- Same as C3, for the ETF page. **Options:** the same; I recommend A.

### C5. Resources, Charts: RobinTrack
- robintrack.net is still up, but its data ends in 2020, when Robinhood stopped publishing how many users held each stock. A visitor clicking it expects current data.
- **Options:** A, keep it, labeled "(historical, to 2020)" (recommended; it's still interesting history). B, remove it. C, keep it as it is.

### C6. HFEA: "Cost of leverage (as of 2018)"
- The figure is eight years old. Leveraged ETF costs follow interest rates, which have moved a lot since 2018, so a reader may take it as current.
- **Options:** A, keep it with its date, as it is now (the text is honest about its age). B, you supply a current figure and its source. C, add one line after it: "Borrowing costs rise and fall with interest rates; check the funds' current figures." This would be new text. I lean towards A, or C if you're happy with the new line.

### C7. "On Composer Atlas" boxes on TQQQ FTLT and Holy Grail
- These boxes link to five Atlas strategy pages. In Atlas's own data, three of them (the **2026 versions** of TQQQ FTLT, UPRO FTLT and Holy Grail) are marked *hidden*, so they may not open for visitors.
- **Options:** A, you open those three on Atlas, logged out or in a private window. If they open, keep them; if not, I drop them from the boxes (recommended). B, drop them now. C, keep them.
- Since you run Composer Atlas: if they should be public, unhiding them there fixes this without touching this site.

### C8. HFEA's Composer Atlas link
- It points at Atlas's database page with a strategy ID to search for, because Atlas has no HFEA entry (checked 2026-10-02).
- **Proposed:** no change until Atlas has an HFEA entry, then link straight to it. Just confirm, or tell me whether an entry is coming.

---

## Q3. SEO small fixes S1 to S7

The full audit table, covering all 30 pages, is in [SEO-REVIEW.md](SEO-REVIEW.md), section 1. These fixes don't move any content.

| ID | What | Pages | My recommendation |
|---|---|---|---|
| S1 | Add an h1, the main page heading search engines look for. **Individual Stocks** and **Screener** have none. Proposed h1s: "Individual Stocks" and "Screener". | 2 | **Yes**; the clearest gap in the audit |
| S2 | Longer titles: 21 are under 30 characters, for example "About - Azqato" (14). Pattern: topic first, then the brand, for example "About Azqato: Gaming, Streaming and Web Tools". I'd draft all 21 for you to approve in one list. | 21 | Yes |
| S3 | Trim meta descriptions over 160 characters, which Google cuts off. The worst is the Screener's (303). Each trimmed version would come from the source's own sentence. | 11 | Yes |
| S4 | Fix two skipped heading levels (Resources, VIX). These are level changes only, no new words. | 2 | Yes |
| S5 | Add a "Related:" line of links at the end of each leveraged strategy page (to the other five), and on Metrics and Philosophy (to each other and the Screener). These are links only, no new prose. | 8 | Yes |
| S6 | Projects: the project cards are drawn by a script, so crawlers that skip scripts see an empty page (41 words). Proposed: put the cards in the HTML, and keep the script for filtering. | 1 | Yes |
| S7 | FAQ: 11,917 words with no headings. Add an h2 for each of the FAQ's existing topic groups, using no new wording. | 1 | Yes |

**Answer with:** yes or no for each, for example "S1–S7 yes, except S6". For S2, say whether you want to see my 21 draft titles first or would rather write them yourself.

---

## Q4. Landing and Method pages (L1 to L4, M1 to M3)

**The idea** (Roadmap item 13): each Invests group's first page becomes a short landing page, with what the section is, 3 to 5 cards and a "Start here" button. Its long text moves, **word for word**, to a new "Method" page in the same group. The full drafts are in [SEO-REVIEW.md](SEO-REVIEW.md), sections 3 and 4.

| ID | Page | Today | Proposed |
|---|---|---|---|
| L1 + M1 | Individual Stocks | 1,368 words, no h1 | Short landing page (the source's own opener, "Buy companies with strong growth fundamentals. Hold them. Do not sell.", plus 4 cards). The method moves to `stocks/method.html`. |
| L2 + M2 | Indices & ETFs | **6,706 words** on the landing page | Short landing page (about 200 words, 5 cards). The method moves to `indices/method.html`. **The biggest win of the four.** |
| L3 + M3 | VIX Strategy | 1,115 words plus the two tools | Short landing page with the live reading and both tools. The method essays move to `vix/method.html`. |
| L4 | Leveraged Strategies | Already a 386-word landing page with 6 cards | **No change** |

**Points to decide:**
1. **For each of L1 to L3: yes or no.**
2. **L3 in particular:** you combined the VIX pages into one in 2.13.6, so splitting the method back out partly reverses that. "Leave VIX as it is" is a perfectly good answer. My lean: do L1 and L2, and skip L3.
3. **The card blurbs** are new text, marked *(new)* in the drafts. Approve them, edit them, or write your own.
4. **The Method page titles** (M1 to M3) are new text. Same choice.
5. **Old bookmarks:** links to sections, such as `/invests/indices/#dollar-cost-averaging`, would be forwarded to the Method page by a small script, in one hop, permanently, like the 2.13.6 VIX redirects. Just confirm that's acceptable.

After you approve, I build it all in one pass, and the inventory check confirms nothing was lost in the move.

---

## Q5. Projects page: two language tags below the contrast minimum (dark theme)

- On the Projects page, in the **dark** theme, the colored language tags for **C#** (contrast 3.42:1) and **HTML** (4.09:1) are below the 4.5:1 minimum for small text (WCAG AA), so they're harder to read for people with low vision.
- This predates this build pass, and I left it alone because the colors are part of each language's look. The light theme already passes; I fixed that in 2.13.7.
- **Options:** A, brighten just those two colors slightly in dark mode, keeping the same hue (recommended). B, leave them.

---

## Q6. Music page: dark only, no theme button (confirm)

- **Update 2026-10-03:** the music page now has the second bar (🎧 Azqato Music and the search), still without a theme button. If you choose B, the button goes into that bar.

- Your answer for item 5 was "the visualizer stays dark". I built that as: **the whole music page stays dark, and it has no theme button** (`data-theme-lock="dark"`). Every other page has the button.
- The alternative reading: the page follows the theme (light top bar, light footer), and only the visualizer stage stays dark.
- **Options:** A, keep it as built (recommended; the page is almost entirely the stage, and a light bar over a dark stage looks broken). B, the page follows the theme, and only the stage stays dark.

---

## Q7. Individual Stocks: "12 metrics" or "10 metrics"?

- The page's description (from the source) says **"12 plain-English metrics"**. Its heading says **"The 10 Metrics"**. The Metrics page also lists "The 12 Signals".
- I changed neither, because it's source text.
- **Options:** A, you tell me which number is right, and I correct the other (the description or the heading). B, leave both.

---

## Q8. `test-local-audio.bat` (local only, not in git)

- This script opens `music.html` in a relaxed Chrome window to test the audio. Since 2.13.8, the page lives at `music/index.html`, and `music.html` forwards to it, so the script still works, with one extra hop.
- **Options:** A, I update the script's last line to `music\index.html` (recommended; it's a one-line local change). B, leave it.

---

## Q9. The new addresses end in a slash (confirm)

- Item 7 asked for "`/discord`, not `discord.html`". Pages in folders are served at **`/discord/`**, with the trailing slash, the same as `/invests/`. `/discord` without the slash still works and takes one hop to `/discord/`.
- The canonical tags, the sitemap and the internal links all use the slash form, so search engines see one address per page.
- **Options:** A, keep the slash (recommended; it matches Invests, and it's how folders work on both hosts). B, you'd prefer no slash. That would need Cloudflare-only rewrite rules, and GitHub Pages would still add the slash.

---

## Q10. The theme button's place (resolved 2026-10-03)

Settled by your 2026-10-03 request: every page except the home page now has the Invests-style second bar, with the page's emoji and name, "Search the site" and the theme button. The top bar shows only "Azqato." and the links. The home page keeps its single bar, with the theme button at its end. Nothing to answer.

---

## Q11. Sign off the Invests tenets and press release (new, 2026-10-03)

**Background.** Roadmap item 2 (P7.10) asked you to review the drafted Invests sections in PRD Part 2. I brought every section up to date with the site (2.15.3): goals, user stories and success criteria are all met; four FAQ answers were out of date and are corrected. Two things are opinions only you can give:

1. **Tenets (PRD Part 2, Invests: Tenets).** In priority order: 1 Preserve before polish; 2 Push only on the owner's word; 4 Reuse the feeds, don't move the pipelines; 5 Template structure, source content; 6 No accounts, no tracking. (3 was removed by D22.) **Recommendation:** keep them as they are.
2. **The press release quote** is from "Sam Rivera", a fictional user, labeled fictional. **Recommendation:** keep it; it's an internal document and it's labeled.

**Answer with:** "Q11: recommended", or the changes you want.

## Q12. One Resources link is down: Zacks (new, 2026-10-03)

**Background.** The live review checked all 79 outside links. Nine refused a script but open fine in a browser. One, "Make money trading the earnings calendar" (finance.zacks.com/make-money-trading-earnings-calendar-11148.html, Resources), returns 503 (server unavailable) even in a browser.

**Options.** A: wait a week and re-check; a 503 is often temporary (**recommended**). B: remove it now, like C3 and C4.

## Q13. FAQ topic group names (built 2.15.3; rename if you like)

You approved S7 ("yes to everything"), and its premise turned out wrong: the FAQ had no groups to label. So I made seven groups from the questions as they already run, without moving or rewording any question: **The long-term mindset** (1 to 6), **How markets move** (7, 8), **Researching a company** (9 to 12), **What makes a company worth owning** (13 to 19), **Timing and signals** (20 to 23), **ETFs, leverage and how to invest** (24 to 27), **Managing your portfolio** (28 to 37). The filter box hides a group when none of its questions match.

**Answer with:** "Q13: keep", or new names.

## Item 1: your own read-through of the live site

The automated review is done and clean (all 21 pages, desktop and phone, light and dark, no errors). What a script can't judge is whether you like what you read. When you have time, browse azqato.com/invests/ and send me anything you want changed, in any form.

## Saved for later (no answer needed now)

- **15d, smoke-test script:** a local `tools/smoke.py` (no GitHub Action) that opens all pages in Edge in both themes, at desktop and phone widths, and fails on errors. Saved for later at your request (2026-10-02). It's listed here only so it isn't forgotten.
