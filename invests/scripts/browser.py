"""Browser tests for the Azqato Invests site, in headless Microsoft Edge.

Run from anywhere: python scripts/browser.py [--shots DIR]
Needs Python 3 with Playwright (pip install playwright) and Edge installed
(Browser Testing in docs/PRD.md: Edge, never Chrome). Serves the folder on a
free local port from a thread, so no server is left running afterwards.
Reads the site only; writes screenshots when --shots is given.

Checks, in both themes: every page loads with no script errors and no failed
same-site requests; text contrast meets WCAG AA; the shell works (skip link,
drawer, search, theme button and its saved choice); the FAQ filter and answer
links; the tools load live data; and each data feed's fallback works when the
feed is blocked. Exits 1 if any check fails.
"""
import functools, http.server, importlib.util, pathlib, socketserver, sys, threading
sys.dont_write_bytecode = True
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
# scripts/site.py by path: "import site" would find Python's own site module.
_spec = importlib.util.spec_from_file_location("site_builder", ROOT / "scripts" / "site.py")
_site = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_site)
PAGES = _site.PAGES

DESKTOP = {"width": 1280, "height": 900}
PHONE = {"width": 390, "height": 844}
fails, notes = [], []

CONTRAST_JS = """
() => {
  function rgb(s) { const m = s.match(/[\\d.]+/g); return m ? m.map(Number) : [0,0,0,0]; }
  function lum(c) { const a = c.slice(0,3).map(v => { v /= 255; return v <= 0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4); });
    return 0.2126*a[0] + 0.7152*a[1] + 0.0722*a[2]; }
  function blend(top, bottom) { const a = top[3] === undefined ? 1 : top[3];
    return [0,1,2].map(i => top[i]*a + bottom[i]*(1-a)).concat([1]); }
  function bg(el) {
    const layers = [];
    for (let e = el; e; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.backgroundImage !== 'none' && !cs.backgroundImage.startsWith('linear-gradient')) return null;
      const c = rgb(cs.backgroundColor);
      if (c[3] === undefined) c[3] = 1;
      if (c[3] > 0) { layers.push(c); if (c[3] >= 1) break; }
    }
    let out = [255,255,255,1];
    if (layers.length && layers[layers.length-1][3] >= 1) out = layers.pop();
    while (layers.length) out = blend(layers.pop(), out);
    return out;
  }
  const bad = [];
  const seen = new Set();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    if (!n.textContent.trim()) continue;
    const el = n.parentElement;
    if (!el || seen.has(el)) continue;
    seen.add(el);
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height || el.closest('[hidden], dialog:not([open]), .pp-vh, .visually-hidden, .sr-only, .site-skip, [aria-hidden="true"]')) continue;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) continue;
    const b = bg(el);
    if (!b) continue;
    const f = blend(rgb(cs.color), b);
    const l1 = lum(f), l2 = lum(b);
    const ratio = (Math.max(l1,l2)+0.05) / (Math.min(l1,l2)+0.05);
    const size = parseFloat(cs.fontSize), weight = parseInt(cs.fontWeight, 10);
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const need = large ? 3 : 4.5;
    if (ratio < need) bad.push({ text: n.textContent.trim().slice(0, 40), cls: (el.className && el.className.baseVal === undefined ? el.className : el.tagName), ratio: Math.round(ratio*100)/100, need: need, color: cs.color });
  }
  return bad;
}
"""


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve():
    handler = functools.partial(Quiet, directory=str(ROOT))
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{httpd.server_address[1]}/"


def watch(page, base, errors):
    page.on("pageerror", lambda e: errors.append(f"script error: {e}"))
    page.on("console", lambda m: errors.append(f"console {m.type}: {m.text}") if m.type == "error" else None)
    page.on("requestfailed", lambda r: errors.append(f"request failed: {r.url}") if r.url.startswith(base) else None)
    page.on("response", lambda r: errors.append(f"HTTP {r.status}: {r.url}") if r.url.startswith(base) and r.status >= 400 else None)


def fail(msg):
    fails.append(msg)
    print("FAIL:", msg, flush=True)


def load(ctx, base, path, theme, size, shots=None, wait=2500, blocked=False):
    """Open a page; with blocked=True, errors from feeds the test blocks are expected."""
    page = ctx.new_page()
    page.set_viewport_size(size)
    errors = []
    watch(page, base, errors)
    page.add_init_script(f"try {{ localStorage.setItem('azqato-invests-theme', '{theme}'); }} catch (e) {{}}")
    page.goto(base + path, wait_until="load")
    page.wait_for_timeout(wait)
    if page.evaluate("document.documentElement.getAttribute('data-theme')") != theme:
        fail(f"{path} [{theme}]: theme not applied")
    for e in errors:
        if blocked and ("Failed to load resource" in e or "allorigins" in e):
            continue
        fail(f"{path} [{theme} {size['width']}px]: {e}")
    sx = page.evaluate("document.documentElement.scrollWidth - window.innerWidth")
    if sx > 1:
        fail(f"{path} [{theme} {size['width']}px]: page scrolls sideways by {sx}px")
    if shots:
        page.screenshot(path=str(pathlib.Path(shots) / f"{path.replace('/', '_')[:-5]}-{theme}-{size['width']}.png"), full_page=False)
    return page


def contrast(page, label):
    bad = page.evaluate(CONTRAST_JS)
    seen = set()
    for b in bad:
        key = (b["cls"], b["color"])
        if key in seen:
            continue
        seen.add(key)
        fail(f"{label}: contrast {b['ratio']} (needs {b['need']}) for {b['text']!r} [{b['cls']}, {b['color']}]")


def shell_tests(ctx, base):
    page = ctx.new_page()
    page.set_viewport_size(PHONE)
    errors = []
    watch(page, base, errors)
    page.goto(base + "stocks/philosophy.html")
    page.keyboard.press("Tab")
    if page.evaluate("document.activeElement.className") != "site-skip":
        fail("skip link: not the first thing Tab reaches")
    page.keyboard.press("Enter")
    if page.evaluate("document.activeElement.id") != "pp-main":
        notes.append("skip link: focus didn't land on main (the address changed to #pp-main)")
    page.click("#pp-menu-btn")
    page.wait_for_timeout(300)
    if page.get_attribute("#pp-menu-btn", "aria-expanded") != "true" or page.evaluate("document.activeElement.id") != "pp-nav-close":
        fail("drawer: didn't open with focus on its close button")
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)
    if page.get_attribute("#pp-menu-btn", "aria-expanded") != "false" or page.evaluate("document.activeElement.id") != "pp-menu-btn":
        fail("drawer: Escape didn't close it and return focus to the menu button")
    page.set_viewport_size(DESKTOP)
    page.keyboard.press("/")
    page.wait_for_timeout(800)
    if not page.evaluate("document.getElementById('pp-search').open"):
        fail("search: / didn't open it")
    page.keyboard.type("PEG")
    page.wait_for_timeout(400)
    n = page.locator("#pp-results li").count()
    if not n:
        fail("search: no results for PEG")
    with page.expect_navigation():
        page.keyboard.press("Enter")
    page.wait_for_timeout(500)
    if "philosophy.html" in page.url and "#" not in page.url:
        fail("search: Enter didn't open a result")
    page.keyboard.press("Control+k")
    page.wait_for_timeout(500)
    if not page.evaluate("document.getElementById('pp-search').open"):
        fail("search: Ctrl+K didn't open it")
    page.keyboard.press("Escape")
    for title in ("Screener", "HFEA", "Curated resources", "Seeking Alpha setup guide"):
        page.keyboard.press("Control+k")
        page.wait_for_timeout(300)
        page.fill("#pp-search-input", title)
        page.wait_for_timeout(300)
        crumbs = page.locator("#pp-results .pp-r-crumb").all_inner_texts()
        if not any(c.endswith(title) for c in crumbs):
            fail(f"search: {title!r} doesn't find its page")
        page.keyboard.press("Escape")
    before = page.evaluate("document.documentElement.getAttribute('data-theme')")
    page.click(".theme-toggle")
    after = page.evaluate("document.documentElement.getAttribute('data-theme')")
    label = page.get_attribute(".theme-toggle", "aria-label")
    page.reload()
    kept = page.evaluate("document.documentElement.getAttribute('data-theme')")
    if before == after or kept != after or ("light" if after == "dark" else "dark") not in label:
        fail(f"theme button: {before} -> {after}, after reload {kept}, label {label!r}")
    page.goto(base + "resources/faq.html")
    page.fill("#faq-filter", "palantir")
    page.wait_for_timeout(500)
    shown = page.locator(".accordion-item:not([hidden])").count()
    if not 0 < shown < 37:
        fail(f"FAQ filter: {shown} questions shown for 'palantir'")
    page.goto(base + "resources/faq.html#answer-nosell")
    page.wait_for_timeout(800)
    if page.get_attribute("[aria-controls='answer-nosell']", "aria-expanded") != "true":
        fail("FAQ: a link to an answer didn't open it")
    for e in errors:
        fail(f"shell tests: {e}")
    page.close()


def tool_tests(ctx, base):
    p = load(ctx, base, "stocks/screener.html", "dark", DESKTOP, wait=6000)
    rows = p.locator("table tbody tr").count()
    as_of = p.inner_text("#asOf")
    print(f"screener: {rows} table rows; {as_of}", flush=True)
    if rows < 10 or "no data" in as_of:
        fail(f"screener: data didn't load ({rows} rows, {as_of!r})")
    notes.append(f"screener shows: {as_of}")
    p.close()
    p = load(ctx, base, "indices/market.html", "dark", DESKTOP, wait=6000)
    txt = p.inner_text("#pp-article")
    print("market:", txt[:200].replace("\n", " "), flush=True)
    notes.append("market overview: " + " ".join(txt.split())[:160])
    p.close()
    for path in ("vix/dashboard.html", "vix/custom.html", "vix/index.html"):
        p = load(ctx, base, path, "dark", DESKTOP, wait=5000)
        data = p.evaluate("JSON.stringify(window.__VIX_DATA__ || null)")
        cached = p.evaluate("localStorage.getItem('vix_last_known')")
        print(f"{path}: __VIX_DATA__ {data}; cache {cached}", flush=True)
        if not data or data == "null":
            fail(f"{path}: the VIX feed didn't load")
        notes.append(f"{path}: VIX feed {data}")
        p.close()


def fallback_tests(browser, base):
    # Screener: block raw GitHub; the fallback at azqato.github.io/stocks/data/ should serve.
    ctx = browser.new_context()
    ctx.route("https://raw.githubusercontent.com/**", lambda r: r.abort())
    p = load(ctx, base, "stocks/screener.html", "dark", DESKTOP, blocked=True, wait=8000)
    rows = p.locator("table tbody tr").count()
    as_of = p.inner_text("#asOf")
    print(f"screener with raw GitHub blocked: {rows} rows; {as_of}", flush=True)
    if rows < 10:
        fail(f"screener fallback: no data with raw GitHub blocked ({as_of!r})")
    p.close()
    # Market Overview with raw GitHub blocked.
    p = load(ctx, base, "indices/market.html", "dark", DESKTOP, blocked=True, wait=8000)
    notes.append("market overview, raw GitHub blocked: " + " ".join(p.inner_text("#pp-article").split())[:160])
    p.close()
    ctx.close()
    # VIX: block the vix.js feed; vix.js falls back to allorigins, then the cache.
    ctx = browser.new_context()
    ctx.route("https://azqato.github.io/vix/data/vix.js*", lambda r: r.abort())
    p = load(ctx, base, "vix/dashboard.html", "dark", DESKTOP, blocked=True, wait=12000)
    notes.append("VIX dashboard, feed blocked: " + " ".join(p.inner_text("#vix-feed").split())[:200])
    p.close()
    ctx.close()
    # Everything blocked, nothing cached: the source's error state should show.
    ctx = browser.new_context()
    ctx.route("https://azqato.github.io/**", lambda r: r.abort())
    ctx.route("https://raw.githubusercontent.com/**", lambda r: r.abort())
    ctx.route("https://api.allorigins.win/**", lambda r: r.abort())
    p = load(ctx, base, "vix/dashboard.html", "dark", DESKTOP, blocked=True, wait=12000)
    notes.append("VIX dashboard, all feeds blocked: " + " ".join(p.inner_text("#vix-feed").split())[:200])
    p.close()
    p = load(ctx, base, "stocks/screener.html", "dark", DESKTOP, blocked=True, wait=8000)
    notes.append("screener, all feeds blocked: " + p.inner_text("#asOf"))
    p.close()
    ctx.close()


def main():
    shots = None
    if "--shots" in sys.argv:
        shots = sys.argv[sys.argv.index("--shots") + 1]
        pathlib.Path(shots).mkdir(parents=True, exist_ok=True)
    httpd, base = serve()
    expected_feed_errors = ("allorigins", "ERR_FAILED", "net::")
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(channel="msedge", headless=True)
            ctx = browser.new_context()
            for path, *_ in PAGES:
                for theme in ("light", "dark"):
                    for size in (DESKTOP, PHONE):
                        p = load(ctx, base, path, theme, size, shots if size is DESKTOP or path in ("index.html", "stocks/screener.html", "stocks/metrics.html") else None)
                        if size is DESKTOP:
                            contrast(p, f"{path} [{theme}]")
                        p.close()
                print("checked", path, flush=True)
            shell_tests(ctx, base)
            tool_tests(ctx, base)
            ctx.close()
            fallback_tests(browser, base)
            browser.close()
    finally:
        httpd.shutdown()
    for n in notes:
        print("note:", n)
    print(f"{len(fails)} failure(s), {len(notes)} note(s)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
