# Runbook — Azqato Portfolio

---

## Local Setup

Getting the project running from a fresh machine requires no installations.

### Prerequisites
- Git (to clone the repository)
- A modern browser (Chrome, Firefox, Edge, or Safari)
- A text editor (VS Code recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Azqato/Azqato.git
   cd Azqato
   ```

2. Open `index.html` in your browser:
   ```
   # Option A: double-click index.html in File Explorer / Finder
   # Option B: drag the file into a browser window
   # Option C: open via a local server (optional but avoids file:// quirks)
   npx serve .          # http://localhost:3000
   python -m http.server # http://localhost:8000
   ```

3. The site is running. No `npm install`, no build step, no configuration.

---

## Build

There is no build step. The source files are the deployed files.

```bash
# Nothing to run. index.html, about.html, and support.html are the production artifacts.
```

If you ever want to check file sizes before pushing:
```bash
# PowerShell
Get-ChildItem *.html | Select-Object Name, Length
Get-ChildItem img\ | Select-Object Name, Length
```

Target: each HTML file should remain under 50,000 bytes uncompressed. Images in `img/` are static assets with no size target — keep them web-optimised (< 500 KB each).

---

## Deploy

### Production — GitHub Pages

The site is deployed automatically when changes are pushed to the `main` branch.

**Initial setup (one-time):**
1. Push the repository to GitHub.
2. In GitHub → repository → Settings → Pages:
   - Source: **Deploy from a branch**
   - Branch: `main` / `root`
3. Save. The site will be live at `https://<username>.github.io/` within ~60 seconds.

**Routine deploy:**
```bash
git add index.html about.html support.html links.html youtube.html invests.html music.html accounts.html privacy-policy.html img/ docs/
git commit -m "Your commit message"
git push origin main
```

GitHub Pages picks up the push automatically. Propagation time is typically 30–90 seconds.

**Verify deployment:**
- Visit https://azqato.github.io/ and hard-refresh (Ctrl+Shift+R / Cmd+Shift+R).
- Check the GitHub Actions tab or Pages Settings for deploy status if the site doesn't update.

### Alternative Hosts (no configuration required)

| Host              | Steps                                                        | URL                              |
|-------------------|--------------------------------------------------------------|----------------------------------|
| Vercel            | Drag and drop the project folder at vercel.com/new          | Assigned by Vercel               |
| Netlify           | Drag and drop at app.netlify.com/drop                       | Assigned by Netlify              |
| Cloudflare Pages  | Connect repo at dash.cloudflare.com → Pages → Create; leave build command blank | Assigned by Cloudflare |

---

## Rollback

Because there is no server and no database, a rollback is a git operation.

### Option A — Revert the last commit
```bash
git revert HEAD
git push origin main
```
This creates a new commit that undoes the last change. GitHub Pages deploys the revert within ~60 seconds.

### Option B — Reset to a specific commit (destructive — confirm before using)
```bash
git log --oneline          # find the target commit hash
git reset --hard <hash>
git push --force-with-lease origin main
```
Use this only if `git revert` is not practical (e.g., reverting many commits at once).

### Option C — Manually restore a file from a previous commit
```bash
git checkout <hash> -- index.html     # restore index.html from a specific commit
git commit -m "Restore index.html to <hash>"
git push origin main
```

---

## Environment Configs

There is only one environment: **production** (GitHub Pages).

There is no staging, no dev server requirement, and no environment-specific configuration. Local editing and browser preview are the only "development environment."

| Environment  | URL                         | Branch  | Deploy trigger   | Notes                        |
|--------------|-----------------------------|---------|------------------|------------------------------|
| Production   | https://azqato.github.io/   | `main`  | Push to `main`   | Auto-deployed by GitHub Pages |
| Local        | `file://` or localhost:3000 | N/A     | Open in browser  | No server required            |

No `.env` files. No environment variables. No feature flags.

---

## Common Errors

| Symptom                              | Likely Cause                                              | Fix                                                                         |
|--------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------|
| Site shows old version after push    | GitHub Pages CDN cache                                    | Hard-refresh (Ctrl+Shift+R). Wait 2–5 minutes for full propagation.         |
| 404 on `azqato.github.io`            | GitHub Pages not enabled or wrong branch configured       | Settings → Pages → ensure source is `main` / `root`                         |
| Affiliate card shows wrong promo     | Outdated hardcoded text in `support.html`                 | Edit the `promo-badge` span and description in the relevant card in `support.html` |
| Filter bar shows unexpected tags     | New project added with an unintended tag value            | Check the `tags` array in the new project object in `index.html`             |
| Project count is wrong               | `renderProjects()` filter logic                           | Open DevTools Console; check for JS errors; verify `PROJECTS` array syntax   |
| Nav active state not highlighting    | Active nav JS uses `pathname` matching                    | Check that the `href` in the nav link exactly matches the page filename      |
| `iconUrl` image not loading          | URL is unreachable or cross-origin blocked                | Check the URL in DevTools → Network; use an absolute URL to a stable host    |
| Page weight over 50 KB               | Too much inline content added                             | Check file size; consider moving large inline content to a separate file     |

---

## Monitoring

The portfolio has no active monitoring or alerting configured. All checks are manual.

| What to check           | Where to check                                               | How often            |
|-------------------------|--------------------------------------------------------------|----------------------|
| Site availability       | Visit https://azqato.github.io/ in a browser                | Spot-check as needed |
| GitHub Pages status     | githubstatus.com                                             | If site appears down |
| Deploy status           | github.com → repo → Actions (if any workflows exist) or Settings → Pages | After each push |
| Traffic / visitors      | github.com → repo → Insights → Traffic                      | Monthly              |
| Affiliate link validity | Click each link on `support.html` and verify destination     | Monthly or after any affiliate program announcement |
| Page weight             | Browser DevTools → Network tab → check HTML file size        | After significant content changes |
| Lighthouse score        | Chrome DevTools → Lighthouse → run audit                     | Quarterly            |
