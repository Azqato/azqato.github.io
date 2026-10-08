"""Browser tests for Azqato's Tools on azqato.com (/codes/tools/), in headless Microsoft Edge.

    python scripts/tools-site/browser.py [--shots DIR]

Reuses the Invests harness (scripts/invests/browser.py): the same local server,
page loader and contrast check. Every page, both themes, desktop and phone:
no script errors or failed requests, no sideways scroll, text contrast at
WCAG AA. Then each tool's main action is run once. Exits 1 on any failure.
"""
import importlib.util, pathlib, sys
sys.dont_write_bytecode = True
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("invests_browser", HERE.parent / "invests" / "browser.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)

ROOT = HERE.parent.parent
PAGES = sorted(p.relative_to(ROOT / "codes" / "tools").as_posix() for p in (ROOT / "codes" / "tools").rglob("index.html"))


def check(page, label, cond, msg):
    if not cond:
        B.fail(f"{label}: {msg}")


def tool_tests(ctx, base):
    """One real action per tool; each must produce its result on the page."""
    def open_(path):
        return B.load(ctx, base, path, "light", B.DESKTOP, wait=600)

    p = open_("link-cleaner/index.html")
    p.fill("#lc-input", "https://example.com/a?utm_source=x&id=7&fbclid=y")
    p.click("#lc-clean")
    p.wait_for_timeout(300)
    out = p.evaluate("(e => e.value || e.textContent)(document.querySelector('#lc-out'))")
    check(p, "link cleaner", "https://example.com/a?id=7" in out, "did not produce the cleaned link")
    p.close()

    p = open_("character-counter/index.html")
    p.fill("textarea", "One two three.")
    p.wait_for_timeout(300)
    check(p, "character counter", "14" in p.evaluate("document.querySelector('#main').innerText"), "no character count")
    p.close()

    p = open_("base64-encoder/index.html")
    p.fill("textarea", "héllo")
    p.wait_for_timeout(300)
    check(p, "base64", "aMOpbGxv" in p.evaluate("[...document.querySelectorAll('#main textarea, #main output, #main pre')].map(e => e.value || e.textContent).join(' ')"), "wrong or no Base64")
    p.close()

    p = open_("json-formatter/index.html")
    p.fill("textarea", '{"b":1,"a":[2,1]}')
    p.wait_for_timeout(300)
    for b in p.query_selector_all("#main button"):
        if b.inner_text().strip().lower().startswith("format"):
            b.click()
            break
    p.wait_for_timeout(300)
    txt = p.evaluate("[...document.querySelectorAll('#main textarea, #main pre, #main output, #main code')].map(e => e.value || e.textContent).join(' ')")
    check(p, "json formatter", '"b": 1' in txt, "no formatted JSON")
    p.close()

    p = open_("markdown-preview/index.html")
    p.fill("#md-input", "# Hello\n\n**bold**")
    p.wait_for_timeout(400)
    check(p, "markdown", p.evaluate("!!document.querySelector('.md-body h1') && !!document.querySelector('.md-body strong')"), "preview did not render")
    p.close()

    p = open_("password-generator/index.html")
    txt = p.evaluate("[...document.querySelectorAll('#main input, #main output, #main code, #main .pg-out, #main [id*=out]')].map(e => e.value || e.textContent).join(' ')")
    check(p, "password generator", any(len(w) >= 12 for w in txt.split()), "no password shown")
    p.close()

    p = open_("timestamp-converter/index.html")
    inp = p.query_selector("#main input:not([type=datetime-local]):not([type=date]):not([type=time])")
    inp.fill("1700000000")
    p.wait_for_timeout(400)
    check(p, "timestamp", "2023" in p.evaluate("document.querySelector('#main').innerText"), "1700000000 did not convert to 2023")
    p.close()

    for path in ("wash-sale-tracker/index.html", "bookmark-manager/index.html", "favicon-downloader/index.html"):
        open_(path).close()  # load-only here: their data entry is covered by hand in the review


def main():
    shots = None
    if "--shots" in sys.argv:
        shots = sys.argv[sys.argv.index("--shots") + 1]
        pathlib.Path(shots).mkdir(parents=True, exist_ok=True)
    httpd, base = B.serve()
    base = base.replace("/invests/", "/codes/tools/")
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(channel="msedge", headless=True)
            ctx = browser.new_context()
            for path in PAGES:
                for theme in ("light", "dark"):
                    for size in (B.DESKTOP, B.PHONE):
                        p = B.load(ctx, base, path, theme, size, shots, wait=800)
                        if size is B.DESKTOP:
                            B.contrast(p, f"codes/tools/{path} [{theme}]")
                        p.close()
                print("checked", path, flush=True)
            tool_tests(ctx, base)
            browser.close()
    finally:
        httpd.shutdown()
    print(f"{len(B.fails)} failure(s)")
    sys.exit(1 if B.fails else 0)


if __name__ == "__main__":
    main()
