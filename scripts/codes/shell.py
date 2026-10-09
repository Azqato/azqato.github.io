#!/usr/bin/env python3
"""Wrap every Codes page in the Contents sidebar, as Azqato Invests is laid out.

    python scripts/tools-site/migrate.py   (only while the old tools repo is the reference)
    python scripts/prompts/build.py
    python scripts/codes/shell.py          this step
    python scripts/build-nav.py            then the nav, footer and search

Codes holds two sections, Prompts (codes/prompts/) and Tools (codes/tools/).
Each page keeps its own interface; this adds, under the site's two bars, a left
sidebar with Home and a collapsible group per section (the group holding the
open page starts open, as on Invests), and Previous / Next links at the foot.
On phones the sidebar folds behind a Contents button. Search is the second
bar's, so the sidebar has none (owner's request, 2026-10-08).

The order comes from the pages themselves: the prompt cards on the Prompts
home page and the tool cards on the Tools home page (tools hosted elsewhere
are left out, as Invests leaves out its outside links). Reruns replace the
blocks between the CODES markers, so this is safe to run any number of times.
"""

import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
CODES = ROOT / 'codes'
CSS = 'codes/assets/codes.css'
SITE = 'https://azqato.com/'
AUTHOR = {'@type': 'Person', 'name': 'Azqato', 'url': SITE + 'about/'}


def cards(page, pattern):
    """(href, label) for each internal card on a section's home page."""
    text = (CODES / page).read_text(encoding='utf-8')
    out = []
    for m in re.finditer(pattern, text, re.S):
        href, label = m.group(1), re.sub(r'<[^>]+>', '', m.group(2)).strip()
        if href.startswith(('http', '#', '../')):
            continue
        out.append((href.rstrip('/').removesuffix('/index.html'), html.unescape(label)))
    return out


def contents():
    """The groups, as lists of (path under codes/, label)."""
    prompts = [('prompts/%s/index.html' % h, t) for h, t in cards(
        'prompts/index.html', r'<a class="prompt-list-item" href="([^"]+)"[^>]*><span class="prompt-list-title">(.*?)</span>')]
    tools = [('tools/%s/index.html' % h, t) for h, t in cards(
        'tools/index.html', r'<a class="tool-card[^"]*" href="([^"]+)"[^>]*>.*?<h3[^>]*>(.*?)</h3>')]
    return [('', [('index.html', 'Home')]),
            ('Prompts', [('prompts/index.html', 'Overview')] + prompts),
            ('Tools', [('tools/index.html', 'Overview')] + tools)]


def rel(here, target):
    """A relative link between two paths under codes/, ending at the folder."""
    # Ends at index.html, as the rest of the site does, so links work when a
    # page is opened from disk as well as on a server.
    return '../' * here.count('/') + target


def sidebar(here, groups):
    parts = []
    for name, items in groups:
        lis = ''.join('<li><a href="%s"%s>%s</a></li>' % (rel(here, p), ' aria-current="page"' if p == here else '',
                                                        html.escape(label)) for p, label in items)
        if not name:
            parts.append('<div class="cd-group"><ul>%s</ul></div>' % lis)
            continue
        gid = 'cd-g-' + name.lower()
        is_open = any(p == here for p, _ in items)
        parts.append('<details class="cd-group"%s><summary class="cd-group-label" id="%s">%s</summary>'
                     '<ul aria-labelledby="%s">%s</ul></details>' % (' open' if is_open else '', gid, name, gid, lis))
    return parts


def pager(here, groups):
    flat = [(p, label if p != 'prompts/index.html' and p != 'tools/index.html' else g)
            for g, items in groups for p, label in items]
    flat = [(p, 'Codes home' if p == 'index.html' else label) for p, label in flat]
    i = [p for p, _ in flat].index(here)
    links = []
    if i > 0:
        p, label = flat[i - 1]
        links.append('<a class="cd-pager-link cd-pager-link--prev" href="%s"><small>Previous</small><span>%s</span></a>'
                     % (rel(here, p), html.escape(label)))
    if i < len(flat) - 1:
        p, label = flat[i + 1]
        links.append('<a class="cd-pager-link cd-pager-link--next" href="%s"><small>Next</small><span>%s</span></a>'
                     % (rel(here, p), html.escape(label)))
    return '<nav class="cd-pager" aria-label="Previous and next page">%s</nav>' % ''.join(links)


def url(here):
    return SITE + 'codes/' + here.removesuffix('index.html')


def trail(here, groups):
    """(label, path) from Codes down to this page; a section's home stands for its group."""
    out = [('Codes', 'index.html')]
    for name, items in groups:
        if name and any(p == here for p, _ in items):
            out.append((name, items[0][0]))
            if here != items[0][0]:
                out.append((dict(items)[here], here))
    return out


def crumbs(here, groups):
    """Visible breadcrumbs, and the trail plus the page's author as structured data
    (SEO audit, owner's approval 2026-10-08: the author is Azqato, linking to About)."""
    steps = trail(here, groups)
    graph = [{'@type': 'WebPage', 'name': steps[-1][0] if len(steps) > 1 else 'Azqato Codes',
              'url': url(here), 'author': AUTHOR}]
    nav = ''
    if len(steps) > 1:
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': i, 'name': n, 'item': url(p)} for i, (n, p) in enumerate(steps, 1)]})
        lis = ''.join('<li><a href="%s">%s</a></li>' % (rel(here, p), html.escape(n)) for n, p in steps[:-1])
        nav = ('<nav class="cd-crumbs" aria-label="Breadcrumb"><ol>%s<li><span aria-current="page">%s</span></li>'
               '</ol></nav>\n  ' % (lis, html.escape(steps[-1][0])))
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False)
    return nav + '<script type="application/ld+json">%s</script>' % ld


def byline(here, text):
    """'By Azqato' under the title of each prompt and of the Codes, Prompts and Tools home pages."""
    text = re.sub(r'\n<p class="cd-byline">.*?</p>', '', text)
    if not (here.startswith('prompts/') or here in ('index.html', 'tools/index.html')):
        return text
    end = text.index('</h1>', text.index('<!-- /CODES -->')) + len('</h1>')
    about = '../' * (here.count('/') + 1) + 'about/index.html'
    return text[:end] + '\n<p class="cd-byline">By <a href="%s" rel="author">Azqato</a></p>' % about + text[end:]


OPEN = """<!-- CODES -->
  <div class="cd-shell">
  <button class="cd-menu-btn" id="cd-menu-btn" type="button" aria-expanded="false" aria-controls="cd-nav">Contents</button>
  <nav class="cd-sidebar" id="cd-nav" aria-label="Codes sections">
    %s
  </nav>
  <div class="cd-main">
  %s
  <!-- /CODES -->"""

CLOSE = """<!-- CODES-END -->
  %s
  </div>
  </div>
  <script>
    (function () {
      var btn = document.getElementById('cd-menu-btn'), nav = document.getElementById('cd-nav');
      btn.addEventListener('click', function () {
        var open = nav.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    })();
  </script>
  <!-- /CODES-END -->"""


def wrap(here, text, groups):
    text = re.sub(r'<!-- CODES -->.*?<!-- /CODES -->', '<!-- CODES --><!-- /CODES -->', text, flags=re.S)
    text = re.sub(r'<!-- CODES-END -->.*?<!-- /CODES-END -->', '<!-- CODES-END --><!-- /CODES-END -->', text, flags=re.S)
    if '<!-- CODES -->' not in text:
        text = text.replace('<!-- /NAV -->', '<!-- /NAV -->\n  <!-- CODES --><!-- /CODES -->', 1)
        text = text.replace('<!-- FOOTER -->', '<!-- CODES-END --><!-- /CODES-END -->\n\n  <!-- FOOTER -->', 1)
    up = '../' * (here.count('/') + 1)
    if CSS not in text:
        text = text.replace('</head>', '  <link rel="stylesheet" href="%s%s" />\n</head>' % (up, CSS), 1)
    text = text.replace('<!-- CODES --><!-- /CODES -->',
                        OPEN % ('\n    '.join(sidebar(here, groups)), crumbs(here, groups)), 1)
    text = byline(here, text)
    return text.replace('<!-- CODES-END --><!-- /CODES-END -->', CLOSE % pager(here, groups), 1)


def main():
    check = '--check' in sys.argv
    groups = contents()
    stale = []
    for here in [p for _, items in groups for p, _ in items]:
        path = CODES / here
        cur = path.read_text(encoding='utf-8', newline='')
        out = wrap(here, cur.replace('\r\n', '\n'), groups)
        if '\r\n' in cur:
            out = out.replace('\n', '\r\n')
        if out != cur:
            stale.append(here)
            if not check:
                path.write_text(out, encoding='utf-8', newline='')
    for here in stale:
        print('%s: codes/%s' % ('out of date' if check else 'written', here))
    print('%d pages in Codes' % sum(len(items) for _, items in groups))
    return 1 if check and stale else 0


if __name__ == '__main__':
    sys.exit(main())
