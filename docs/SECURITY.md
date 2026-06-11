# Security: Azqato Portfolio

---

## Authentication Model

There is no authentication. The portfolio is a fully public, read-only static site. No user accounts, no login, no sessions, no cookies. Every page is accessible to anyone with the URL.

The only privileged access is the GitHub repository itself, which is protected by Azqato's GitHub account credentials (username + password + 2FA). Repository access controls who can push changes and trigger deployments.

---

## Authorization Model

There are no user roles or authorization layers. All visitors have identical read-only access to all pages.

The only authorization boundary is GitHub repository access:
- **Owner (Azqato):** full read/write access to the repository; can push, merge, and modify GitHub Pages settings.
- **Public:** read-only access to all deployed files via `azqato.github.io`.

---

## Data Storage

The portfolio stores no user data. There are no databases, no server-side storage, no cookies, no `localStorage`, no `sessionStorage`, and no `IndexedDB` in use.

The only data in the project is static content hardcoded in HTML files:
- Project metadata in the `PROJECTS` array in `index.html`
- Affiliate link URLs in `support.html`
- Bio content in `about.html`

This data is public by design and contains no personal information about visitors.

**GitHub Pages** (the hosting provider) may log standard web server access data (IP address, user agent, timestamp) as part of its infrastructure. This is outside the portfolio's control and governed by GitHub's privacy policy.

---

## Environment Variables

There are no environment variables. The project has no server, no build pipeline, and no configuration files that reference secrets.

Affiliate link URLs are hardcoded directly in `support.html` as plain HTML `href` attributes. These are not secrets; they are public referral URLs intended to be shared. No API keys, tokens, or credentials exist in this codebase.

**Confirmation:** no `.env` files, no secrets in git history, no hardcoded passwords or tokens.

---

## Third-Party Trust

Every external navigation link opens in a new tab. The portfolio itself makes zero outbound HTTP requests on page load; no external resources are fetched, no scripts are loaded from CDNs, and no analytics pixels fire.

When a visitor clicks a link, they navigate to a third-party site. Data they share with those sites is governed by those sites' privacy policies, not by this portfolio.

| Third Party       | Data Received from Visitor          | Privacy Policy                                  |
|-------------------|-------------------------------------|--------------------------------------------------|
| GitHub Pages      | IP address, user agent (server logs) | github.com/privacy                              |
| Buy Me a Coffee   | User-provided data on their platform | buymeacoffee.com/privacy-policy                 |
| Tesla             | User-provided data on their platform | tesla.com/legal/privacy                         |
| Robinhood         | User-provided data on their platform | robinhood.com/legal/privacy-policy              |
| M1 Finance        | User-provided data on their platform | m1.com/legal/privacy-policy                     |
| Public            | User-provided data on their platform | public.com/privacy                              |
| Lyft              | User-provided data on their platform | lyft.com/legal/privacy-policy                   |

The portfolio is a referral gateway; it links to these services but does not transmit visitor data to them in any automated way.

---

## Known Attack Surface

### Cross-Site Scripting (XSS)

**Risk level: Low**

The `PROJECTS` array is hardcoded in `index.html` and rendered via `innerHTML` template literals. If the array were ever populated from user input or an external API, this would be a critical XSS vector. Currently, only the owner can modify the array (via repository push), so the attack surface is limited to the repository itself.

**Mitigation:** The array is maintainer-controlled. If GitHub API integration is added in a future version (see ROADMAP.md), all API-sourced strings must be escaped with `textContent` assignments or a sanitizer before being inserted into the DOM.

### Affiliate Link Integrity

**Risk level: Low**

Affiliate URLs are hardcoded and not validated at runtime. If a referral URL is modified in the repository (e.g., by a compromised commit), visitors would be sent to incorrect or malicious destinations.

**Mitigation:** All changes go through the owner's GitHub account, which is protected by 2FA. Review all changes to `support.html` before merging.

### Content Security Policy

**Risk level: Informational**

GitHub Pages does not support custom HTTP response headers, so a Content Security Policy cannot be applied. This means the browser has no header-level protection against injected scripts.

**Mitigation:** Acceptable for a static, no-user-input site. If the project migrates to a host that supports custom headers (Vercel, Cloudflare Pages, Netlify), adding a CSP header would be a worthwhile improvement.

### Dependency Vulnerabilities

**Risk level: None (currently)**

There are zero npm dependencies, zero CDN scripts, and zero external stylesheets. There is no dependency graph and therefore no transitive dependency vulnerabilities.

---

## Dependency Policy

**Current state:** zero dependencies.

If a dependency is ever added:
1. Prefer well-maintained packages with a clear security disclosure process.
2. Pin to an exact version in `package.json` (no `^` or `~`).
3. Run `npm audit` before committing.
4. Do not use CDN-hosted scripts (e.g., unpkg, jsDelivr) without Subresource Integrity (SRI) hashes.
5. Review the package's source if it handles any user data or DOM manipulation.

Until a dependency is strictly necessary to solve a specific problem, the zero-dependency default must be maintained per Tenet 2 (see [TENETS.md](TENETS.md)).
