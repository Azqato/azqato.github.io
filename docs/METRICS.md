# Metrics: Azqato Portfolio

---

## North Star Metric

**Monthly unique visitors to the portfolio** (`azqato.github.io/`)

This is the single number that best represents whether the portfolio is delivering value. More visitors means more people discovering the projects, more potential affiliate conversions, and more opportunities for community growth. All other metrics are either inputs to this number or downstream effects of it.

---

## Acquisition Metrics

| Metric                             | Description                                                    | Measurement Method                          |
|------------------------------------|----------------------------------------------------------------|---------------------------------------------|
| GitHub profile referral clicks     | Visitors arriving from the GitHub profile link                 | GitHub Insights → Traffic → Referrers       |
| Organic search impressions         | Times the site appears in search results                       | Google Search Console (if configured)       |
| Social / community referrals       | Traffic from Twitch, YouTube, Discord, or direct shares        | GitHub Insights → Traffic → Referrers       |
| Repository clone count             | Developers cloning the portfolio repo                          | GitHub Insights → Traffic → Clones          |

**Note:** The portfolio has no analytics script. All acquisition data comes from GitHub Pages traffic insights, which provides referrer and view data without tracking individual users. This is intentional and consistent with the no-tracking constraint.

---

## Engagement Metrics

| Metric                       | Description                                                            | Measurement Method                  |
|------------------------------|------------------------------------------------------------------------|--------------------------------------|
| Support page visit rate      | Percentage of portfolio visitors who navigate to `support.html`        | GitHub Insights → Traffic (per-page) |
| About page visit rate        | Percentage of portfolio visitors who navigate to `about.html`          | GitHub Insights → Traffic (per-page) |
| Affiliate link click-throughs | Estimated from affiliate program dashboards (conversions, not clicks) | Per-affiliate partner dashboard      |
| Buy Me a Coffee contributions | Count of contributions received                                        | Buy Me a Coffee dashboard            |

---

## Retention Metrics

| Metric                       | Description                                                  | Measurement Method          |
|------------------------------|--------------------------------------------------------------|------------------------------|
| Returning visitor percentage | Portion of visitors who have visited before                  | GitHub Insights (limited)    |
| Repository star growth       | Stars on the portfolio repo over time                        | GitHub repository star count |
| Profile follower growth      | GitHub followers gained over time                            | GitHub profile follower count|

---

## Performance Metrics

| Metric                         | Description                                               | Measurement Method                            |
|--------------------------------|-----------------------------------------------------------|------------------------------------------------|
| Page weight: index.html        | Uncompressed HTML size                                    | Browser DevTools → Network tab                 |
| Page weight: about.html        | Uncompressed HTML size                                    | Browser DevTools → Network tab                 |
| Page weight: support.html      | Uncompressed HTML size                                    | Browser DevTools → Network tab                 |
| Time to First Contentful Paint | How fast the first content appears                        | Chrome DevTools → Lighthouse or PageSpeed      |
| External HTTP requests         | Count of requests to external domains on page load        | Browser DevTools → Network tab (0 is target)   |
| GitHub Pages uptime            | Site availability                                         | GitHub Status page / manual spot checks        |

---

## Targets

| Metric                             | Target                   | Timeframe       |
|------------------------------------|--------------------------|-----------------|
| Monthly unique visitors            | 500+                     | 3 months post-launch |
| Monthly unique visitors            | 2,000+                   | 12 months post-launch |
| Support page visit rate            | > 10% of portfolio visits | Ongoing          |
| Page weight (any page)             | < 50 KB uncompressed     | Always           |
| Time to First Contentful Paint     | < 1.0 second             | Always           |
| External HTTP requests on page load | 0                        | Always           |
| Buy Me a Coffee contributions      | ≥ 1 per month            | 3 months post-launch |
| Affiliate conversion (any program) | ≥ 1 per month            | 6 months post-launch |
| GitHub Pages uptime                | > 99.9%                  | Ongoing (GitHub SLA) |

---

## Measurement Method

| Method                        | What it covers                                      | Access                                   |
|-------------------------------|-----------------------------------------------------|------------------------------------------|
| GitHub Insights → Traffic     | Page views, unique visitors, referrers, top paths   | github.com → repo → Insights → Traffic  |
| GitHub Insights → Clones      | Repository clone count and frequency                | github.com → repo → Insights → Traffic  |
| Affiliate partner dashboards  | Clicks, sign-ups, and commissions per affiliate     | Each partner's affiliate portal          |
| Buy Me a Coffee dashboard     | Contributions received, supporter count             | buymeacoffee.com/azqato (creator view)   |
| Chrome Lighthouse / PageSpeed | Core Web Vitals, performance score                  | Run manually via DevTools or PageSpeed   |
| Browser DevTools → Network    | Page weight, request count, load time               | Run manually; F12 → Network tab          |

---

## Reporting Cadence

| Metric category          | Review frequency | Notes                                                  |
|--------------------------|------------------|--------------------------------------------------------|
| Traffic (views/visitors) | Monthly          | GitHub Insights retains 14 days of daily data; check monthly to catch trends |
| Affiliate performance    | Monthly          | Log into each partner dashboard; note any conversions  |
| Buy Me a Coffee          | Monthly          | Dashboard shows all-time and monthly                   |
| Performance (Lighthouse) | Quarterly or after major changes | Run manually when adding new features |
| Page weight              | On every commit  | Check DevTools after any HTML change; flag if > 45 KB  |
