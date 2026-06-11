# PR/FAQ: Azqato Portfolio

---

## Press Release

**FOR IMMEDIATE RELEASE**

### Azqato Launches Personal Portfolio Site to Showcase Developer Projects and Community Work

*A fast, no-frills portfolio that puts the work front and center*

Azqato today launched a personal portfolio website at azqato.github.io, giving visitors a single place to browse all public GitHub projects, learn about the person behind the work, and support the journey through referral programs and direct contributions.

The site displays five live projects spanning personal finance tools, social community sites, and utility apps, all filterable by category. Each card links directly to the live demo and the source code, making it easy for developers and recruiters to evaluate the work without friction.

"I wanted something that looked like it belonged on GitHub, not on a Wix template," said Azqato. "Fast, clean, and honest about what it is."

The portfolio is built entirely without frameworks or dependencies (plain HTML, CSS, and JavaScript) and loads in under a second on any connection. It also includes a Support page where visitors can sign up for financial and lifestyle services through affiliate referral links, earning bonuses for themselves while helping fund continued development.

The site is live today at **https://azqato.github.io/**.

---

## Internal FAQ

**Q: Why build a custom portfolio instead of using an existing platform like GitHub profile, LinkedIn, or a page builder?**
A: The goal is a developer-first aesthetic and zero maintenance overhead. Existing platforms don't let you control the visual language precisely, and page builders add bloat. A hand-coded site is the fastest and most credible signal to other developers.

**Q: Why inline CSS and JS instead of separate files?**
A: With only three HTML pages, separate files add deployment complexity with no benefit. Each page is self-contained, which makes it easier to read and modify. The trade-off is some CSS repetition across pages, acceptable at this scale and worth addressing if the page count grows past ~8.

**Q: Why no analytics?**
A: The PRD explicitly excludes analytics and tracking. The portfolio represents a developer who cares about privacy, and tracking visitors would contradict that. GitHub Pages provides basic traffic data (clones, referrers) in the repository Insights tab as a lightweight alternative.

**Q: What happens if an affiliate program changes or cancels a referral link?**
A: Links are hardcoded in `support.html`. If a link breaks or a program ends, it requires a manual edit and a new commit. This is the correct trade-off for a project with no backend; it keeps the site dependency-free and gives full control over what is displayed.

**Q: How does the portfolio monetize without feeling like an ad?**
A: The Support page is a separate, clearly labeled section of the site rather than embedded ads in the portfolio grid. Visitors arrive there by clicking "Support" in the nav; it's opt-in. The affiliate disclosure is visible above the fold and written in plain language.

**Q: What assumption must be true for this to succeed as a monetization channel?**
A: Visitors from Twitch, YouTube, and the B5TA community (who already have an affinity for Azqato) are more likely to convert on affiliate links than cold traffic. If the site is only discovered by developers evaluating the code, the affiliate channel will underperform.

**Q: Why is there no contact form or hire-me section?**
A: GitHub profile and the linked repositories already provide contact paths (GitHub Issues, profile email). A contact form would require a backend or third-party form service, both of which conflict with the zero-dependency constraint. This is deferred to a future version.

**Q: What is the plan if GitHub Pages goes down or becomes paid?**
A: The entire site is plain HTML files; it can be deployed to Vercel, Netlify, or Cloudflare Pages in under five minutes with no configuration changes. There is no lock-in.

**Q: How will new projects be added after launch?**
A: The owner edits the `PROJECTS` array in `index.html`, adds the project object, commits, and pushes. GitHub Pages deploys within ~60 seconds. Estimated time per new project: 2–5 minutes.

**Q: Is there a roadmap for v2?**
A: Yes. See [ROADMAP.md](ROADMAP.md) for the full milestone plan. Prioritized future features include a dark/light mode toggle, GitHub API star count sync, and a contact/hire-me section.

---

## External FAQ

**Q: What is this site?**
A: It's Azqato's personal portfolio: a one-stop place to see all public projects, read about the person who built them, and find ways to support the work.

**Q: How do I find a specific project?**
A: Use the filter buttons above the project grid to narrow by category (Finance, Social, Tools). Click a card title or the ↗ button to open the live version of the project.

**Q: What are the affiliate links on the Support page?**
A: They are referral links for services Azqato personally uses or recommends. If you sign up through one, you get a signup bonus (like free stock or a ride discount), and Azqato earns a referral commission. There's no extra cost to you.

**Q: Do I have to sign up for anything to use this site?**
A: No. Everything on the portfolio, about, and project pages is free to view. The Support page links are optional; you're never prompted to sign up.

**Q: What data does the site collect about me?**
A: None. The portfolio has no analytics, no cookies, no tracking pixels, and no forms. GitHub Pages may log server-level access data (IP address, user agent), but this is standard web hosting and is not controlled by Azqato.

**Q: What is Buy Me a Coffee?**
A: It's a platform where you can make a one-time or monthly contribution to a creator. 100% of the contribution goes to Azqato. The link is buymeacoffee.com/azqato.

**Q: Where do the Buy Me a Coffee funds go?**
A: Azqato intends to invest the funds in the stock market for long-term growth. Circumstances may vary; there is no guaranteed use of funds.

**Q: Can I view the source code for this portfolio site itself?**
A: Yes. The portfolio is open source and hosted on GitHub. Find the repository at github.com/Azqato.

**Q: How do I get in touch with Azqato?**
A: Through the GitHub profile linked in the nav bar. GitHub Issues or the profile's contact email are the primary channels.

**Q: How often is the portfolio updated?**
A: New projects are added as they are built. The site has had regular updates since launch (see the patch notes). There is no fixed release schedule.
