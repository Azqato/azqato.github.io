# TODO

A scratchpad for open work, unresolved decisions, and ideas worth keeping. Created 2026-09-28 by the v2.9.9 documentation audit, seeded from open items that were already recorded across the other documents and from what the audit itself turned up.

**What this file is.** A holding place. Nothing here is committed to, scheduled, or approved. Items are the owner's to decide on.

**What this file is not.** It is not an instruction list. An assistant reading this file should not start working through it. Work comes from the PRD Roadmap or from the owner asking directly. This file is never consolidated into another document, merged, moved, or deleted; it is pruned only by removing items that are genuinely done or genuinely abandoned.

---

## Decided 2026-09-28, and shipped the same day

Six questions went to the owner at the v2.9.9 audit and all six came back. They are recorded in full under Decided At The v2.9.9 Audit in the PRD Roadmap, with effort estimates and a recommended order. **All of the resulting work shipped on 2026-09-28 as v2.10.0 through v2.10.5**, with one exception noted below. Summarised here so this file does not contradict that one:

- **Canonical domain: `azqato.com`.** Shipped as v2.10.3, **except the `CNAME`**. The sitemap, robots.txt, README and docs all name `azqato.com`, and so do the canonical and `og:url` tags added in v2.10.4. The `CNAME` file is the one item that can take the site down, because DNS and the GitHub Pages custom-domain setting are both outside this repository, so it was held back. See the open item below.
- **Licence: all rights reserved.** `LICENSE.md` stands. The copy that contradicted it was reworded at the audit as v2.10.0.
- **Cloudflare Web Analytics: keep it, fix the copy.** The docs were aligned as v2.10.0 and `privacy-policy.html` was rewritten as v2.10.5, which carries the real disclosure. Done.
- **Social sharing tags: all 12 pages, full set.** Shipped as v2.10.4: nine tags in every head. Images are off by default, so there is no `og:image` and nothing to design. Done.
- **Page titles: fix them**, in the same pass, since both edit the same heads. Shipped as v2.10.4. All 12 are page-first with a ` - Azqato` suffix. Done.
- **`.gitattributes`: add it and normalize everything.** Shipped as v2.10.2 (`5070b3b`). The 12-file whitespace diff never happened: every committed blob was already LF and `core.autocrlf=true` had been doing the work, so renormalization changed nothing. The file still earns its place by making that guarantee portable. Done.

## Still waiting on the owner

- ~~**Create the `CNAME` file, once DNS is confirmed.**~~ **Closed 2026-09-29 as moot, not done.** A `CNAME` is a GitHub Pages mechanism, and `azqato.com` is not served by GitHub Pages: it is a separate Cloudflare Pages deployment, confirmed by the owner. The file would have had no effect on the canonical domain. Nothing is outstanding; the milestone's actual goal was met by the work that shipped on 2026-09-28. See Roadmap v2.10.3.
- ~~**Paste two or three live URLs into Discord and look at the cards.**~~ **Done 2026-10-02: the owner checked them; they look great.** The only check that tests what v2.10.4 was for, and it could not be done before deploying.
- ~~**Decide whether internal links should drop `.html` too.**~~ **Decided 2026-09-29: leave them.** Every internal link keeps its `.html`, so each internal click on `azqato.com` takes a 307 to the extensionless form first. That is a few milliseconds and it costs nothing that matters. Dropping the extensions would mean changing the nav generator and every page body, and would stop the site working when a page is opened directly from disk, which is how it has always been developed. The canonical and `og:url` tags already point at the extensionless destination, so crawlers and shared links are unaffected either way. Not revisited unless the development workflow changes.
- **One brand or two?** Left open by the brand concept work. Whether Azqato the person and Azqato the label are one visual identity or two.
- **Where did the mascot come from?** Provenance was never established for the lion. It matters before it goes on anything sold.
- **Whether to start reading the Cloudflare analytics.** Now that keeping the beacon is a decision rather than an accident, it holds real page-level visit counts that the north-star metric was designed without. Whether that metric should be redefined around them is unresolved and was not part of the September decisions.

## Site and code

- ~~**Add social sharing tags to all twelve pages.**~~ **Done as v2.10.4**, together with the title rewrite.
- **The visualizer brightness gate, reserved as v2.9.5.** Roadmap item, deliberately not implemented yet.
- **Move the remaining two mixes to local audio.** They are still third-party embedded players. The README already says this is the plan.
- **Extract `music.html`'s inline JavaScript to `viz.js`.** Recorded as known technical debt. The page is 112 KB and roughly 1,900 lines of that is inline script. Offered at the audit and deferred with "revisit this later".
- ~~**Clean up `tools/build-nav.py`'s `SKIP` set.**~~ **Done as v2.10.1.** Deferred at the audit, then pulled back into the batch the same day. `SKIP` is now an empty set with a comment explaining what used to be in it.
- ~~**Consider a `.gitattributes` file.**~~ **Done as v2.10.2.** The predicted twelve-file whitespace diff turned out not to exist; see the note above.
- **Four thumbnails in `img/` are over 500 KB.** Against the project's own informal target. Compress rather than delete; nothing in `img/` gets deleted.

## Brand and merchandise

- **Rewrite concepts 001 through 005** so they follow the same prompt rules as 006 onward. They were written before the rules settled.
- **The `brand/` folder is local only and untracked, and therefore not backed up anywhere.** Recorded in the folder's own review document. If that work matters, it needs a backup that is not this repository.

## Ideas, unranked

- A progress dashboard, as proposed in the PRD Roadmap under Future updates.
- A changelog page on the site itself, rendered from `docs/PATCHNOTES.md`, so visitors can see the thing is alive without opening GitHub.
- ~~An `og:image` per page.~~ **Closed by the specification, not by a decision.** Images are off by default: a declared image that does not exist is worse than none, and `summary_large_image` with no image renders a broken frame in some clients. If it is ever revisited, the full requirement set is recorded under Social Sharing Tags in the PRD, and it is all of them or none.
