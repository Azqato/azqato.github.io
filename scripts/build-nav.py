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
    python scripts/build-nav.py            rewrite the nav in every page
    python scripts/build-nav.py --check    report drift, write nothing, exit 1 if any

To change the nav: edit PAGES below, run the script, review `git diff`, commit.
"""

import argparse
import html
import json
import pathlib
import re
import sys

# ── The nav, in display order ─────────────────────────────
# (filename, label). A page whose filename appears here gets `class="active"`
# on its own link. Pages not listed (accounts.html, privacy-policy.html) still
# receive the nav, they simply have no active item.
PAGES = [
    ('index.html', 'Home'),
    ('about/index.html', 'About'),
    ('discord/index.html', 'Discord'),
    ('invests/index.html', 'Invests'),
    ('codes/index.html', 'Codes'),
    ('music/index.html', 'Music'),
    ('links/index.html', 'Links'),
    ('projects/index.html', 'Projects'),
    ('youtube/index.html', 'YouTube'),
    ('support/index.html', 'Support'),
]

# Each page's emoji favicon (owner's answers, 2026-10-02). A page not listed
# here, and the home page, use the lion.
ICONS = {
    'about/index.html': '🙋', 'discord/index.html': '💬', 'codes/index.html': '💻', 'music/index.html': '🎧',
    'links/index.html': '🔗', 'projects/index.html': '🛠️', 'youtube/index.html': '📺', 'support/index.html': '☕',
    'accounts/index.html': '🎮', 'privacy-policy/index.html': '🔒',
}
ICON_DEFAULT = '🦁'

# Sections moved in from their own repos (roadmap item 22): every page under
# the folder gets the section's emoji, second-bar title and home link, and the
# Codes link is marked active, since Codes is where the nav lists them.
SECTIONS = {
    'codes/tools/': {'icon': '🔧', 'bar': "Azqato's Tools", 'active': 'codes/index.html'},
    'codes/prompts/': {'icon': '💬', 'bar': "Azqato's Prompts", 'active': 'codes/index.html'},
}
ROOT = pathlib.Path(__file__).resolve().parent.parent


def section_pages(prefix):
    return sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / prefix).rglob('index.html'))


def section(filename):
    for prefix, sec in SECTIONS.items():
        if filename.startswith(prefix):
            return prefix, sec
    return None, None


def page_label(filename):
    # A section page's name for search: its <title> without the section suffix.
    prefix, sec = section(filename)
    if filename == prefix + 'index.html':
        return sec['bar']
    t = re.search(r'<title>(.*?)</title>', (ROOT / filename).read_text(encoding='utf-8'), re.S).group(1)
    t = html.unescape(t).strip()
    suffix = ' - ' + sec['bar']
    return t[:-len(suffix)] if t.endswith(suffix) else t


# The icon link, then the theme script (unless the page is locked dark), are
# stamped together, so a rerun replaces both instead of adding a script.
ICON_LINK = re.compile(r'<link rel="icon" href="data:image/svg\+xml,[^"]*" />(\s*<script src="(?:\.\./)*theme.js"></script>)?')

# Light and dark themes (build pass item 5): theme.js sets the theme before the
# first paint; the button sits in the bar. music.html stays dark (owner's
# answer: the visualizer stays dark) and gets neither; its <html> carries
# data-theme="dark" data-theme-lock="dark".
THEME_LOCKED = {'music/index.html'}
THEME_BUTTON = ('\n        <button class="theme-toggle" type="button" aria-label="Switch theme">'
                '<span class="theme-toggle-icon" aria-hidden="true"></span></button>')

# The top bar shows "Azqato." on every page (owner's request, 2026-10-03).
BRAND_DEFAULT = 'Azqato<span>.</span>'

# The second bar, under the top bar on every page but the home page (owner's
# request, 2026-10-03: "match the Invests one"): the page's emoji and name,
# "Search the site", and the theme button. The home page keeps one bar.
SECTION_NAMES = {
    'about/index.html': 'About', 'discord/index.html': 'Discord', 'codes/index.html': 'Codes',
    'music/index.html': 'Music', 'links/index.html': 'Links', 'projects/index.html': 'Projects',
    'youtube/index.html': 'YouTube', 'support/index.html': 'Support',
    'accounts/index.html': 'Gaming Accounts', 'privacy-policy/index.html': 'Privacy Policy',
}
# The second bar's wording, where the owner chose it (2026-10-03); any other
# page reads "Azqato <name>".
BAR_TITLES = {
    'about/index.html': 'About Azqato', 'discord/index.html': "Azqato's Discord",
    'music/index.html': "Azqato's Music", 'links/index.html': "Azqato's Links",
    'projects/index.html': "Azqato's Projects", 'support/index.html': 'Support Azqato',
}


def icon_for(filename):
    return ("<link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' "
            "viewBox='0 0 100 100'><text y='.9em' font-size='90'>%s</text></svg>\" />"
            % (section(filename)[1] or {}).get('icon', ICONS.get(filename, ICON_DEFAULT))
            + ('' if filename in THEME_LOCKED else '\n  <script src="%stheme.js"></script>' % up(filename)))


def up(filename):
    """The way back to the site root from a page: '' for index.html, '../' for
    a page in its own folder (clean addresses, build pass item 7)."""
    return '../' * filename.count('/')


def href(page, target):
    """A link from one page to another, relative, so pages open from disk."""
    return up(page) + target


# Everything from the marker through the closing tag is regenerated. Both appear
# exactly once per page, which is what makes this safe without extra markers.
# Since the second bar (2026-10-03) the block ends at <!-- /NAV -->; the second
# alternative reads a page stamped before then.
BLOCK = re.compile(r'<!-- NAV -->.*?<!-- /NAV -->|<!-- NAV -->.*?</nav>', re.DOTALL)

TEMPLATE = """<!-- NAV -->
  <nav>
    <div class="nav-inner">
      <a class="nav-logo" href="{home}">{brand}</a>
      <ul class="nav-links">
{items}
      </ul>
      <div class="nav-tools">{theme}
        <button class="nav-toggle" aria-label="Toggle navigation menu" aria-expanded="false">☰</button>
      </div>
    </div>
  </nav>{sub}
  <!-- /NAV -->"""

SUB_TEMPLATE = """
  <div class="site-sub">
    <a class="site-sub-brand" href="{self}"><span class="site-sub-mark" aria-hidden="true">{icon}</span> {name}</a>
    <button class="site-search-btn" type="button" aria-haspopup="dialog" aria-keyshortcuts="/ Control+K">
      <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/></svg>
      <span class="site-search-text">Search the site</span>
      <kbd aria-hidden="true">/</kbd>
    </button>
    <div class="site-sub-end">{theme}
    </div>
  </div>
  <script src="{up}search.js" defer></script>"""

# ── The footer ────────────────────────────────────────────
# Plain crawlable links to every major section (owner's request, 2026-10-02:
# "all the major categories, for SEO"). Two groups: the site, and Azqato
# Invests' sections. No sitemap link: robots.txt points crawlers at sitemap.xml.
FOOTER_SITE = PAGES + [
    ('codes/tools/index.html', "Azqato's Tools"),
    ('codes/prompts/index.html', "Azqato's Prompts"),
    ('accounts/index.html', 'Gaming Accounts'),
    ('privacy-policy/index.html', 'Privacy Policy'),
]
FOOTER_INVESTS = [
    ('invests/index.html', 'Azqato Invests'),
    ('invests/stocks/index.html', 'Individual Stocks'),
    ('invests/indices/index.html', 'Indices & ETFs'),
    ('invests/indices/vix/index.html', 'VIX Strategy'),
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
FOOTER_VARIANT = {'music/index.html': ' site-footer--stage'}


def footer_for(filename):
    """Return the footer block for one page."""
    def items(pairs):
        return '\n'.join(
            '          <li><a href="%s"%s>%s</a></li>'
            % (href(filename, target), ' aria-current="page"' if target == filename else '', label.replace('&', '&amp;'))
            for target, label in pairs
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
    prefix, sec = section(filename)
    current = sec['active'] if sec else filename
    items = '\n'.join(
        '        <li><a href="%s"%s>%s</a></li>'
        % (href(filename, target), ' class="active"' if target == current else '', label)
        for target, label in PAGES
    )
    theme = '' if filename in THEME_LOCKED else THEME_BUTTON
    if filename == 'index.html':
        # The home page: one bar, with the theme button at its end.
        return TEMPLATE.format(items=items, home='index.html', brand=BRAND_DEFAULT, theme=theme, sub='')
    if sec:
        sub_self, icon, name = href(filename, prefix + 'index.html'), sec['icon'], sec['bar']
    else:
        sub_self, icon = 'index.html', ICONS.get(filename, ICON_DEFAULT)
        name = BAR_TITLES.get(filename, 'Azqato ' + SECTION_NAMES[filename])
    sub = SUB_TEMPLATE.format(self=sub_self, icon=icon, name=name, up=up(filename),
                              theme=theme.replace('\n        ', '\n      '))
    return TEMPLATE.format(items=items, home=href(filename, 'index.html'), brand=BRAND_DEFAULT, theme='', sub=sub)


# ── Search ────────────────────────────────────────────────
# search-index.js, for the second bar's search (search.js): every root page's
# sections, then Azqato Invests' own index (invests/assets/js/search-index.js,
# written by scripts/invests/site.py) with its addresses moved under invests/.
# Same format as Invests' index: pages [{u, t, g}], entries [{p, h, a, x}].
def search_index(root):
    from bs4 import BeautifulSoup
    pages, entries = [], []
    for name in ['index.html'] + list(SECTION_NAMES) + [p for pre in SECTIONS for p in section_pages(pre)]:
        soup = BeautifulSoup((root / name).read_text(encoding='utf-8'), 'html.parser')
        body = soup.body
        for x in body.select('nav, .site-sub, footer, script, style, dialog, noscript, iframe, canvas, .pr-agents, .cd-sidebar, .cd-pager'):
            x.decompose()
        prefix, sec = section(name)
        label = 'Home' if name == 'index.html' else page_label(name) if sec else SECTION_NAMES[name]
        pi = len(pages)
        pages.append({'u': name, 't': label, 'g': sec['bar'] if sec else 'Azqato.com'})
        h1 = body.find('h1')
        head, text = (h1.get_text(' ', strip=True) if h1 else label), []
        anchor = ''
        for el in body.find_all(['h2', 'p', 'li', 'h3', 'td']):
            if el.name == 'h2':
                entries.append({'p': pi, 'h': head, 'a': anchor, 'x': ' '.join(text)[:600]})
                head, anchor, text = el.get_text(' ', strip=True), el.get('id', ''), []
            elif not el.find(['p', 'li']):
                t = el.get_text(' ', strip=True)
                if t:
                    text.append(t)
        entries.append({'p': pi, 'h': head, 'a': anchor, 'x': ' '.join(text)[:600]})
    inv = (root / 'invests/assets/js/search-index.js').read_text(encoding='utf-8')
    inv = json.loads(inv[inv.index('{'):inv.rindex('}') + 1])
    off = len(pages)
    for pg in inv['pages']:
        pages.append({'u': 'invests/' + pg['u'], 't': pg['t'],
                      'g': 'Azqato Invests' + ('' if pg['g'] == 'Home' else ' / ' + pg['g'])})
    for e in inv['entries']:
        entries.append(dict(e, p=e['p'] + off))
    return ('// Generated by scripts/build-nav.py: every page\'s sections, for the site search (search.js).\n'
            'window.SITE_INDEX = ' + json.dumps({'pages': pages, 'entries': entries}, ensure_ascii=False,
                                                separators=(',', ':')) + ';\n')


def main():
    ap = argparse.ArgumentParser(description='Stamp the shared nav into every page.')
    ap.add_argument('--check', action='store_true',
                    help='report pages whose nav is out of date and write nothing')
    args = ap.parse_args()

    root = pathlib.Path(__file__).resolve().parent.parent
    changed = []
    skipped = []

    # The home page, then each page in its own folder (clean addresses, build
    # pass item 7). The old root .html files are redirect pages and get nothing.
    names = ['index.html'] + [t for t, _ in FOOTER_SITE if t != 'index.html' and not t.startswith('invests/')
                              and not section(t)[0]]
    names += [p for pre in SECTIONS for p in section_pages(pre)]
    for name in names:
        path = root / name
        if name in SKIP:
            continue

        # newline='' keeps each file's own line endings intact. music.html is
        # CRLF while every other page is LF, and rewriting that would produce a
        # diff of the whole file instead of the nav.
        src = path.read_text(encoding='utf-8', newline='')
        if '<!-- NAV -->' not in src:
            skipped.append(name)
            continue

        newline = '\r\n' if '\r\n' in src else '\n'
        block = nav_for(name).replace('\n', newline)
        out = BLOCK.sub(lambda _: block, src, count=1)
        out = ICON_LINK.sub(lambda _: icon_for(name), out, count=1)
        if '<!-- FOOTER -->' in out:
            fblock = footer_for(name).replace('\n', newline)
            out = FOOTER_BLOCK.sub(lambda _: fblock, out, count=1)

        if out == src:
            continue

        changed.append(name)
        if not args.check:
            path.write_text(out, encoding='utf-8', newline='')

    for name in skipped:
        print('skipped (no NAV marker): %s' % name)

    idx_path = root / 'search-index.js'
    idx = search_index(root)
    if not idx_path.exists() or idx_path.read_text(encoding='utf-8') != idx:
        changed.append('search-index.js')
        if not args.check:
            idx_path.write_text(idx, encoding='utf-8', newline='\n')

    if not changed:
        print('nav and footer are up to date in every page')
        return 0

    verb = 'out of date' if args.check else 'updated'
    for name in changed:
        print('%s: %s' % (verb, name))

    if args.check:
        print('\n%d page(s) out of date. Run: python scripts/build-nav.py' % len(changed))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
