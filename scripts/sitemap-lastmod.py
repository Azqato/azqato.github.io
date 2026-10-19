#!/usr/bin/env python3
"""Stamp <lastmod> on every URL in sitemap.xml and invests/sitemap.xml.

Each date is the last commit that changed the page's file, or today if the file
has uncommitted changes (so a page edited in this commit gets this commit's
date). Run it last in the build chain, after scripts/build-nav.py: the prompt
and Invests generators keep whatever dates are already there.

Usage:
    python scripts/sitemap-lastmod.py            rewrite the dates
    python scripts/sitemap-lastmod.py --check    report stale dates, write nothing, exit 1 if any
"""

import datetime
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://azqato.com/'
SITEMAPS = ['sitemap.xml', 'invests/sitemap.xml']
URL = re.compile(r'(<url>\s*<loc>([^<]+)</loc>)(\s*<lastmod>[^<]*</lastmod>)?')


def page_file(url):
    """The file behind a URL: a folder's index.html, or an Invests page's name.html."""
    path = url[len(SITE):]
    f = ROOT / (path + 'index.html' if path == '' or path.endswith('/') else path + '.html')
    if not f.exists():
        sys.exit('no file for %s (looked for %s)' % (url, f.relative_to(ROOT)))
    return f.relative_to(ROOT).as_posix()


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()


def lastmod(f):
    if git('status', '--porcelain', '--', f):
        return datetime.date.today().isoformat()
    return git('log', '-1', '--format=%cs', '--', f) or datetime.date.today().isoformat()


def stamp(text):
    def one(m):
        indent = re.search(r'\n([ \t]*)<loc>', m.group(1))
        sep = '\n' + indent.group(1) if indent else ''
        return '%s%s<lastmod>%s</lastmod>' % (m.group(1), sep, lastmod(page_file(m.group(2))))
    return URL.sub(one, text)


def main():
    check = '--check' in sys.argv
    stale = []
    for name in SITEMAPS:
        path = ROOT / name
        cur = path.read_text(encoding='utf-8')
        new = stamp(cur)
        if new != cur:
            stale.append(name)
            if not check:
                path.write_text(new, encoding='utf-8', newline='\n')
    if check:
        if stale:
            sys.exit('lastmod out of date in %s. Run: python scripts/sitemap-lastmod.py' % ', '.join(stale))
        print('sitemap lastmod dates are up to date')
    else:
        print('updated: %s' % ', '.join(stale) if stale else 'sitemap lastmod dates already up to date')


if __name__ == '__main__':
    main()
