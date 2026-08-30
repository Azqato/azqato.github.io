#!/usr/bin/env python3
"""Stamp the shared navigation bar into every page.

The nav lives here once. Running this script rewrites the block between the
`<!-- NAV -->` marker and the closing `</nav>` tag in every HTML file in the
project root, setting the active link from the file's own name.

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
    ('invests.html', 'Invests'),
    ('codes.html', 'Codes'),
    ('music.html', 'Music'),
    ('links.html', 'Links'),
    ('projects.html', 'Projects'),
    ('youtube.html', 'YouTube'),
    ('support.html', 'Support'),
]

# Everything from the marker through the closing tag is regenerated. Both appear
# exactly once per page, which is what makes this safe without extra markers.
BLOCK = re.compile(r'<!-- NAV -->.*?</nav>', re.DOTALL)

TEMPLATE = """<!-- NAV -->
  <nav>
    <div class="nav-inner">
      <a class="nav-logo" href="index.html">Azqato<span>.</span></a>
      <button class="nav-toggle" aria-label="Toggle navigation menu" aria-expanded="false">☰</button>
      <ul class="nav-links">
{items}
      </ul>
    </div>
  </nav>"""

# Files that are in the project root but are not site pages.
SKIP = {'nav-extraction-test.html', 'reduced-motion-test.html'}


def nav_for(filename):
    """Return the nav block for one page, with its own link marked active."""
    items = '\n'.join(
        '        <li><a href="%s"%s>%s</a></li>'
        % (href, ' class="active"' if href == filename else '', label)
        for href, label in PAGES
    )
    return TEMPLATE.format(items=items)


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

        if out == src:
            continue

        changed.append(path.name)
        if not args.check:
            path.write_text(out, encoding='utf-8', newline='')

    for name in skipped:
        print('skipped (no NAV marker): %s' % name)

    if not changed:
        print('nav is up to date in every page')
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
