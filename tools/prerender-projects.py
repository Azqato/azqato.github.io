"""Write the Projects page's cards into its HTML (SEO review S6, 2026-10-03).

projects/index.html draws its cards from the PROJECTS array with a script, so
a crawler that doesn't run scripts saw an empty grid. This runs the page in
Edge (Playwright), copies the cards the script drew and the project count
into the HTML, between the PROJECTS markers. The script still draws the
cards on load, replacing the copy with the same markup, and keeps the
filtering. Run it after editing PROJECTS:

    python tools/prerender-projects.py          write
    python tools/prerender-projects.py --check  report only; exit 1 if stale
"""

import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

PAGE = pathlib.Path(__file__).resolve().parent.parent / 'projects' / 'index.html'
GRID = re.compile(r'(<div class="project-grid" id="project-grid">).*?(\n    </div>\n  </section>)', re.DOTALL)
COUNT = re.compile(r'(<span class="section-meta" id="project-count">)[^<]*(</span>)')


def main():
    src = PAGE.read_text(encoding='utf-8')
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='msedge')
        page = browser.new_page()
        page.route(re.compile(r'^https?://'), lambda route: route.abort())  # no outside requests
        page.goto(PAGE.as_uri())
        cards = page.eval_on_selector('#project-grid', 'el => el.innerHTML').strip()
        count = page.eval_on_selector('#project-count', 'el => el.textContent')
        browser.close()
    block = ('\n      <!-- PROJECTS: written by tools/prerender-projects.py from the PROJECTS array; '
             'the script redraws it on load. -->\n      ' + cards + '\n      <!-- /PROJECTS -->')
    out = GRID.sub(lambda m: m.group(1) + block + m.group(2), src, count=1)
    out = COUNT.sub(lambda m: m.group(1) + count + m.group(2), out, count=1)
    if out == src:
        print('projects/index.html: cards are up to date')
        return 0
    if '--check' in sys.argv:
        print('projects/index.html: cards out of date. Run: python tools/prerender-projects.py')
        return 1
    PAGE.write_text(out, encoding='utf-8', newline='\n')
    print('projects/index.html: cards written')
    return 0


if __name__ == '__main__':
    sys.exit(main())
