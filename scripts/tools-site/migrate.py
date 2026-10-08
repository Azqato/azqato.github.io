#!/usr/bin/env python3
"""Move Azqato's Tools (github.com/Azqato/tools) into azqato.com/codes/tools/ (roadmap item 22).

    python scripts/tools-site/migrate.py [path to the tools repo, default ../tools]
    python scripts/build-nav.py          then stamp the nav, footer and search

A one-time move, kept so the conversion can be read and rerun while the old
repo is still the reference. Once the owner retires that repo, the pages under
tools/ are this site's own and are edited directly; rerunning this would
overwrite those edits.

What it does, per page:
- keeps the page's <main> word for word, and its own scripts;
- drops the old top bar, footer and early theme script (theme.js, the shared
  nav and footer replace them);
- gives every page a clean address, codes/tools/<old file name>/;
- points links to tools now on azqato.com (the VIX Strategy, the Nasdaq 100
  Screener) at their pages here;
- rewrites css/style.css onto the site's color roles (colors.css), scoped to
  <body class="tl"> so it cannot reach the shared nav or footer.
"""

import pathlib
import re
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / 'codes' / 'tools'

# Old addresses of Azqato projects that now live on azqato.com, as links
# relative to codes/tools/ (the landing page). A tool page adds one more ../.
MOVED = {
    'https://azqato.github.io/VIX/': '../../invests/indices/vix/index.html',
    'https://azqato.github.io/stocks/screener.html': '../../invests/stocks/screener.html',
}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="https://azqato.com/codes/tools/{path}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="https://azqato.com/codes/tools/{path}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Azqato" />
  <meta name="twitter:card" content="summary" />
  <link rel="icon" href="data:image/svg+xml,x" />
  <link rel="stylesheet" href="{up}styles.css" />
  <link rel="stylesheet" href="{up}codes/tools/assets/tools.css" />
</head>
<body class="tl">

  <!-- NAV -->
  <!-- /NAV -->

  {main}

  <!-- FOOTER -->
  </footer>
{scripts}
  <script>
    (function () {{
      var toggle = document.querySelector('.nav-toggle');
      var links = document.querySelector('.nav-links');
      if (!toggle || !links) return;
      toggle.addEventListener('click', function () {{
        var open = links.classList.toggle('open');
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      }});
      links.addEventListener('click', function (e) {{
        if (e.target.tagName === 'A') {{
          links.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
        }}
      }});
      document.addEventListener('click', function (e) {{
        if (!links.contains(e.target) && !toggle.contains(e.target)) {{
          links.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
        }}
      }});
    }})();
  </script>
</body>
</html>
"""


def one(pattern, text, name):
    m = re.search(pattern, text, re.S)
    if not m:
        sys.exit('%s: no match for %s' % (name, pattern))
    return m.group(1)


def links(html, landing):
    """Old file links to clean addresses, from tools/ (landing) or tools/<x>/."""
    pre = '' if landing else '../'
    html = re.sub(r'href="index\.html(#[^"]*)?"', lambda m: 'href="%sindex.html%s"' % (pre, m.group(1) or ''), html)
    html = re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"',
                  lambda m: 'href="%s%s/index.html%s"' % (pre, m.group(1), m.group(2) or ''), html)
    for old, new in MOVED.items():
        html = re.sub(r'href="%s" target="_blank" rel="noopener"' % re.escape(old),
                      'href="%s%s"' % (pre, new), html)
        html = html.replace('href="%s"' % old, 'href="%s%s"' % (pre, new))
    return html


def page(src, name):
    text = src.read_text(encoding='utf-8')
    landing = name == 'index'
    path = '' if landing else name + '/'
    up = '../../' if landing else '../../../'
    main = one(r"(<main id=\"main\".*?)\s*<footer", text, name)
    scripts = one(r'</footer>(.*?)</body>', text, name)
    scripts = scripts.replace('src="js/', 'src="%scodes/tools/assets/js/' % up).rstrip() + '\n'
    out = HEAD.format(title=one(r'<title>(.*?)</title>', text, name),
                      desc=one(r'<meta name="description" content="(.*?)"', text, name),
                      path=path, up=up, main=links(main, landing), scripts=scripts)
    dest = OUT / path / 'index.html'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out, encoding='utf-8', newline='\n')


# ── The stylesheet ───────────────────────────────────────────
# The old palette's names, pointed at the site's roles. Names the main
# stylesheet also defines (--bg, --border, --accent, --text...) get the same
# value it gives them, so setting them on <body> changes nothing outside main.
TOKENS = """/* As on the old site, the page sits a step back from its cards: a soft gray
   page with white cards in light, a dark page with lighter cards in dark. */
.tl {
  --tl-page: var(--ti-color-surface);
  --bg-elev: var(--ti-color-canvas);
  --bg-inset: var(--ti-color-hover);
  --border: var(--ti-color-border);
  --border-strong: var(--ti-color-border-strong);
  --text: var(--ti-color-text);
  --text-soft: var(--ti-color-text-muted);
  --text-faint: var(--ti-color-text-muted);
  --accent: var(--ti-color-accent);
  --accent-hover: var(--ti-color-accent-hover);
  --accent-soft: var(--ti-color-accent-muted);
  --success: var(--ti-color-success);
  --danger: var(--ti-color-danger);
  --shadow: 0 1px 2px rgba(16, 22, 32, .06), 0 8px 24px rgba(16, 22, 32, .06);
  --shadow-sm: 0 1px 2px rgba(16, 22, 32, .08);
  --radius: 14px;
  --radius-sm: 9px;
  --maxw: 1100px;
  --mono: "SF Mono", "JetBrains Mono", "Cascadia Code", ui-monospace, Menlo,
    Consolas, monospace;
}
/* The site's reset (styles.css) zeroes every margin and padding; the tools
   were written against the browser's defaults, so they get those back. Zero
   specificity, so any spacing a tool sets still wins. */
.tl main :where(p, h1, h2, h3, h4, ul, ol, dl, dd, figure, blockquote, pre, fieldset, table) { margin: revert; }
.tl main :where(ul, ol, fieldset, legend) { padding: revert; }
.tl { accent-color: var(--ti-color-accent); }
[data-theme="dark"] .tl {
  --tl-page: var(--ti-color-canvas);
  --bg-elev: var(--ti-color-surface);
  --bg-inset: var(--ti-color-canvas);
  --shadow: 0 1px 2px rgba(0, 0, 0, .4), 0 12px 32px rgba(0, 0, 0, .35);
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, .4);
}
"""

# Rules for the old top bar, footer and skip link, which the shared ones replace.
# .icon-btn and .spacer stay: the tools use them inside their own pages too.
CHROME = re.compile(r'^(html|body|\.topbar|\.brand|\.nav-link|\.footer|\.skip-link|\.nav-toggle|\.nav-menu)\b')

# Fixed colors, onto roles.
SWAPS = [
    ('.btn.primary {\n  background: var(--accent);\n  border-color: var(--accent);\n  color: #fff;',
     '.btn.primary {\n  background: var(--ti-color-accent-bg);\n  border-color: var(--ti-color-accent-bg);\n  color: var(--ti-color-on-accent);'),
    ('.btn.primary:hover { background: var(--accent-hover); border-color: var(--accent-hover); }',
     '.btn.primary:hover { background: var(--ti-color-accent-hover); border-color: var(--ti-color-accent-hover); }'),
    ('background: linear-gradient(120deg, var(--accent), #b15bff 70%);\n  -webkit-background-clip: text;\n  background-clip: text;\n  -webkit-text-fill-color: transparent;',
     'color: var(--accent);'),
    ('.ws-pill.soon { background: #fdf0d5; color: #8a5a00; }',
     '.ws-pill.soon { background: var(--ti-color-warning-muted); color: var(--ti-color-warning); }'),
    ('.ws-pill.now { background: #fdeaed; color: var(--danger); }',
     '.ws-pill.now { background: var(--ti-color-danger-muted); color: var(--ti-color-danger); }'),
    ('[data-theme="dark"] .ws-pill.soon { background: #3a2e12; color: #f0c04a; }\n', ''),
    ('[data-theme="dark"] .ws-pill.now { background: #3a1c22; color: #ff8fa0; }\n', ''),
    # .page came after .wrap and zeroed its side padding: tools ran edge to edge on phones.
    ('.page { padding: 34px 0 70px; }', '.page { padding-top: 34px; padding-bottom: 70px; }'),
    ('.pg-fill.level-1 { background: #d98a1f; }', '.pg-fill.level-1 { background: var(--ti-color-orange); }'),
]


def scope(selector):
    s = selector.strip()
    if s.startswith('[data-theme="dark"] '):
        return '[data-theme="dark"] .tl ' + s[len('[data-theme="dark"] '):]
    if re.match(r'^[a-z*]', s):  # element selectors: main only, never the nav or footer
        return '.tl main ' + s
    return '.tl ' + s


def css(src):
    text = src.read_text(encoding='utf-8')
    body = text[text.index('* { box-sizing'):]
    for old, new in SWAPS:
        if old not in body:
            sys.exit('style.css: expected text not found: %r' % old[:60])
        body = body.replace(old, new)
    out = []
    # Walk the top-level rules and @media blocks, scoping each selector list.
    pos = 0
    rule = re.compile(r'(/\*.*?\*/)|(@media[^{]*\{)|(\})|([^{}]+)\{([^{}]*)\}', re.S)
    while pos < len(body):
        if body[pos].isspace():
            out.append(body[pos])
            pos += 1
            continue
        m = rule.match(body, pos)
        if not m:
            sys.exit('style.css: cannot parse at %r' % body[pos:pos + 60])
        comment, media, close, sel, decl = m.groups()
        if comment or media or close:
            out.append(m.group(0))
        else:
            lead = sel[:len(sel) - len(sel.lstrip())]
            sels = [x for x in sel.split(',')]
            kept = [x for x in sels if not CHROME.match(x.strip())]
            if kept:
                inside = 'prefers-reduced-motion' in ''.join(out[-3:]) and sel.strip().startswith('*')
                scoped = ',\n'.join(x.strip() if inside else scope(x) for x in kept)
                out.append('%s%s {%s}' % (lead, scoped, decl))
        pos = m.end()
    # The page color has its own name, so the shared bars' --bg is untouched.
    out = [x.replace('var(--bg)', 'var(--tl-page)') for x in out]
    out.insert(0, 'body.tl { background: var(--tl-page); }\n')
    # Widths come from codes/assets/codes.css, as on Invests (owner, 2026-10-08).
    header = ('/* Azqato\'s Tools on azqato.com (item 22). Generated from the old repo\'s\n'
              '   css/style.css by scripts/tools-site/migrate.py: its rules, scoped to\n'
              '   <body class="tl">, with its palette pointed at colors.css. */\n\n')
    return header + TOKENS + '\n' + ''.join(out)


def main():
    src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / 'tools'
    if (src / 'css' / 'style.css').exists() is False:
        sys.exit('not the tools repo: %s' % src)
    pages = sorted(p.stem for p in src.glob('*.html'))
    (OUT / 'assets' / 'js').mkdir(parents=True, exist_ok=True)
    for js in (src / 'js').glob('*.js'):
        shutil.copy2(js, OUT / 'assets' / 'js' / js.name)
    (OUT / 'assets' / 'tools.css').write_text(css(src / 'css' / 'style.css'), encoding='utf-8', newline='\n')
    for name in pages:
        page(src / (name + '.html'), name)
    print('%d pages, %d scripts, tools.css' % (len(pages), len(list((OUT / 'assets' / 'js').glob('*.js')))))


if __name__ == '__main__':
    main()
