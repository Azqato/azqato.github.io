#!/usr/bin/env python3
"""Stamp the shared navigation bar and footer into every page.

The nav and footer live here once. Running this script rewrites the block
between the `<!-- NAV -->` marker and the closing `</nav>` tag, and the block
between the `<!-- FOOTER -->` marker and the closing `</footer>` tag, in every
HTML file in the project root, setting the active link from the file's own name.

The output is committed and deployed exactly as it is now. Nothing runs at
request time, nothing is compiled, and the repository still contains complete,
readable HTML. If this script is ever deleted the site keeps working and you go
back to editing the nav by hand with nothing lost. It is a convenience, not a
dependency.

Usage:
    python tools/build-nav.py            rewrite the nav in every page
    python tools/build-nav.py --check    report drift, write nothing, exit 1 if any

To change the nav: edit PAGES below, run the script, review `git diff`, commit.
"""

import argparse
import pathlib
import re
import sys

# ── The nav, in display order ─────────────────────────────
# (filename, label). A page whose filename appears here gets `class="active"`
# on its own link. Pages not listed (accounts.html, privacy-policy.html) still
# receive the nav, they simply have no active item.
PAGES = [
    ('index.html', 'Home'),
    ('about.html', 'About'),
    ('discord.html', 'Discord'),
    ('invests/index.html', 'Invests'),
    ('codes.html', 'Codes'),
    ('music.html', 'Music'),
    ('links.html', 'Links'),
    ('projects.html', 'Projects'),
    ('youtube.html', 'YouTube'),
    ('support.html', 'Support'),
]

# Each page's emoji favicon (owner's answers, 2026-10-02). A page not listed
# here, and the home page, use the lion.
ICONS = {
    'about.html': '🙋', 'discord.html': '💬', 'codes.html': '💻', 'music.html': '🎧',
    'links.html': '🔗', 'projects.html': '🛠️', 'youtube.html': '📺', 'support.html': '☕',
    'accounts.html': '🎮', 'privacy-policy.html': '🔒',
}
ICON_DEFAULT = '🦁'
ICON_LINK = re.compile(r'<link rel="icon" href="data:image/svg\+xml,[^"]*" />')

# Section brands in the top bar. Every other page shows "Azqato."
BRANDS = {
    'music.html': '🎧 Azqato <span>Music</span>',
    'codes.html': '💻 Azqato <span>Codes</span>',
}
BRAND_DEFAULT = 'Azqato<span>.</span>'


def icon_for(filename):
    return ("<link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' "
            "viewBox='0 0 100 100'><text y='.9em' font-size='90'>%s</text></svg>\" />"
            % ICONS.get(filename, ICON_DEFAULT))


# Everything from the marker through the closing tag is regenerated. Both appear
# exactly once per page, which is what makes this safe without extra markers.
BLOCK = re.compile(r'<!-- NAV -->.*?</nav>', re.DOTALL)

TEMPLATE = """<!-- NAV -->
  <nav>
    <div class="nav-inner">
      <a class="nav-logo" href="index.html">{brand}</a>
      <button class="nav-toggle" aria-label="Toggle navigation menu" aria-expanded="false">☰</button>
      <ul class="nav-links">
{items}
      </ul>
    </div>
  </nav>"""

# ── The footer ────────────────────────────────────────────
# Plain crawlable links to every major section (owner's request, 2026-10-02:
# "all the major categories, for SEO"). Two groups: the site, and Azqato
# Invests' sections. No sitemap link: robots.txt points crawlers at sitemap.xml.
FOOTER_SITE = PAGES + [
    ('accounts.html', 'Gaming Accounts'),
    ('privacy-policy.html', 'Privacy Policy'),
]
FOOTER_INVESTS = [
    ('invests/index.html', 'Azqato Invests'),
    ('invests/stocks/index.html', 'Individual Stocks'),
    ('invests/indices/index.html', 'Indices & ETFs'),
    ('invests/vix/index.html', 'VIX Strategy'),
    ('invests/leveraged/index.html', 'Leveraged Strategies'),
    ('invests/resources/index.html', 'Investing Resources'),
]

FOOTER_BLOCK = re.compile(r'<!-- FOOTER -->.*?</footer>', re.DOTALL)

FOOTER_TEMPLATE = """<!-- FOOTER -->
  <footer class="site-footer{variant}">
    <div class="site-footer-in">
      <p class="site-footer-brand">Azqato<span>.</span></p>
      <nav class="site-footer-nav" aria-label="Footer">
        <ul aria-label="Site">
{site}
        </ul>
        <ul aria-label="Azqato Invests">
{invests}
        </ul>
      </nav>
      <p class="site-footer-legal">&copy; 2026 Azqato</p>
    </div>
  </footer>"""

# music.html's footer sits inside the fixed stage console, so it gets a compact,
# translucent variant of the same block.
FOOTER_VARIANT = {'music.html': ' site-footer--stage'}


def footer_for(filename):
    """Return the footer block for one page."""
    def items(pairs):
        return '\n'.join(
            '          <li><a href="%s"%s>%s</a></li>'
            % (href, ' aria-current="page"' if href == filename else '', label.replace('&', '&amp;'))
            for href, label in pairs
        )
    return FOOTER_TEMPLATE.format(variant=FOOTER_VARIANT.get(filename, ''),
                                  site=items(FOOTER_SITE), invests=items(FOOTER_INVESTS))


# Files that are in the project root but are not site pages.
# Pages in the root that the nav is deliberately not stamped into. Empty today:
# the two test harnesses that used to be listed here were deleted long ago, and
# leaving their names in place implied a rule the project no longer has.
SKIP = set()


def nav_for(filename):
    """Return the nav block for one page, with its own link marked active."""
    items = '\n'.join(
        '        <li><a href="%s"%s>%s</a></li>'
        % (href, ' class="active"' if href == filename else '', label)
        for href, label in PAGES
    )
    return TEMPLATE.format(items=items, brand=BRANDS.get(filename, BRAND_DEFAULT))


def main():
    ap = argparse.ArgumentParser(description='Stamp the shared nav into every page.')
    ap.add_argument('--check', action='store_true',
                    help='report pages whose nav is out of date and write nothing')
    args = ap.parse_args()

    root = pathlib.Path(__file__).resolve().parent.parent
    changed = []
    skipped = []

    for path in sorted(root.glob('*.html')):
        if path.name in SKIP:
            continue

        # newline='' keeps each file's own line endings intact. music.html is
        # CRLF while every other page is LF, and rewriting that would produce a
        # diff of the whole file instead of the nav.
        src = path.read_text(encoding='utf-8', newline='')
        if '<!-- NAV -->' not in src:
            skipped.append(path.name)
            continue

        newline = '\r\n' if '\r\n' in src else '\n'
        block = nav_for(path.name).replace('\n', newline)
        out = BLOCK.sub(lambda _: block, src, count=1)
        out = ICON_LINK.sub(lambda _: icon_for(path.name), out, count=1)
        if '<!-- FOOTER -->' in out:
            fblock = footer_for(path.name).replace('\n', newline)
            out = FOOTER_BLOCK.sub(lambda _: fblock, out, count=1)

        if out == src:
            continue

        changed.append(path.name)
        if not args.check:
            path.write_text(out, encoding='utf-8', newline='')

    for name in skipped:
        print('skipped (no NAV marker): %s' % name)

    if not changed:
        print('nav and footer are up to date in every page')
        return 0

    verb = 'out of date' if args.check else 'updated'
    for name in changed:
        print('%s: %s' % (verb, name))

    if args.check:
        print('\n%d page(s) out of date. Run: python tools/build-nav.py' % len(changed))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
