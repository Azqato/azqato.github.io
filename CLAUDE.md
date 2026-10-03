# CLAUDE.md

## Project
Static GitHub Pages site (plain HTML/CSS). No build step and no workflows in `.github/workflows`; Pages deploys via GitHub's built in "pages build and deployment" Action.

## GitHub Actions storage limit (alert received 2026-10-03)
- The azqato account has used 100% (0.5 GB / 0.5 GB) of the free plan's included Actions storage for the billing cycle.
- Storage resets on 2026-11-01.
- Overage is billed unless a $0 Actions budget is set. With a $0 budget, further storage use is blocked until reset.
- Storage counts workflow artifacts and caches across every repo on the account, including the `github-pages` artifact uploaded on each Pages deploy.

## Rules while the limit is in effect
- Do not add workflows that upload artifacts or use `actions/cache`.
- If a workflow is ever added, set `retention-days: 1` on `actions/upload-artifact`.
- Batch commits to `main` where practical; each push triggers a Pages deploy that uploads a new artifact.
- If Pages deploys start failing, check Actions storage first. Old artifacts can be deleted in each repo under Actions, and caches under Actions > Caches.
- Keep large media (audio, images) small; it adds to the Pages artifact size.
