"""Browser tests for Azqato's Prompts on azqato.com (/prompts/), in headless Microsoft Edge.

    python scripts/prompts/browser.py [--shots DIR]

Reuses the Invests harness (scripts/invests/browser.py). Every page, both
themes, desktop and phone: no script errors or failed requests, no sideways
scroll, text contrast at WCAG AA (desktop, with the prompt expanded). Then
the list search, Expand / Hide, and the Copy pointer. Exits 1 on any failure.
"""
import importlib.util, pathlib, sys
sys.dont_write_bytecode = True
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("invests_browser", HERE.parent / "invests" / "browser.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)

ROOT = HERE.parent.parent
PAGES = sorted(p.relative_to(ROOT / "prompts").as_posix() for p in (ROOT / "prompts").rglob("index.html"))


def behavior(ctx, base):
    p = B.load(ctx, base, "index.html", "light", B.DESKTOP, wait=500)
    total = p.locator(".prompt-list-item").count()
    p.fill("#prompt-search", "audit mobile")
    shown = p.evaluate("[...document.querySelectorAll('.prompt-list-item')].filter(a => !a.hidden).map(a => a.textContent)")
    side = p.evaluate("[...document.querySelectorAll('.sidebar-nav a[data-slug]')].filter(a => !a.hidden).length")
    if side != 1:
        B.fail(f"search 'audit mobile': sidebar shows {side} prompts, expected 1")
    if len(shown) != 1 or "Mobile Audit" not in shown[0]:
        B.fail(f"search 'audit mobile': expected Mobile Audit only, got {len(shown)} of {total}")
    p.fill("#prompt-search", "zzzz")
    if "No prompts match" not in p.inner_text("#home-empty"):
        B.fail("search with no match: no message")
    p.fill("#prompt-search", "mobile audit")
    p.press("#prompt-search", "Enter")
    p.wait_for_load_state("load")
    if not p.url.endswith("/prompts/mobile-responsive-audit/"):
        B.fail(f"Enter did not open the first match: {p.url}")
    p.close()

    p = B.load(ctx, base, "mobile-responsive-audit/index.html", "light", B.DESKTOP, wait=500)
    if p.get_attribute(".sidebar-nav a.active", "data-slug") != "mobile-responsive-audit":
        B.fail("sidebar does not mark the open prompt")
    p.fill("#prompt-search", "wiki")
    if p.evaluate("[...document.querySelectorAll('.sidebar-nav a[data-slug]')].filter(a => !a.hidden).length") != 1:
        B.fail("sidebar search on a prompt page: 'wiki' should leave GitHub Wiki only")
    p.fill("#prompt-search", "")
    phone = B.load(ctx, base, "mobile-responsive-audit/index.html", "light", B.PHONE, wait=300)
    if phone.is_visible(".sidebar-nav"):
        B.fail("phone: prompt list is open on load")
    phone.click("#pr-nav-toggle")
    if not phone.is_visible(".sidebar-nav") or not phone.is_visible("#prompt-search"):
        B.fail("phone: the Prompts button does not open the list and search")
    phone.close()
    if p.is_visible("#prompt-body"):
        B.fail("prompt block is not collapsed on load")
    p.click(".code-label")  # the whole bar toggles
    if not p.is_visible("#prompt-body") or p.inner_text(".code-toggle") != "Hide":
        B.fail("clicking the bar did not expand the prompt")
    p.click(".copy-btn")
    p.wait_for_timeout(300)
    if not p.is_visible("#prompt-body"):
        B.fail("Copy collapsed the prompt")
    clip = p.evaluate("navigator.clipboard.readText()")
    want = ("Review the full prompt on this website, provide a summary of what it does and then ask if I "
            "would like to run it: https://azqato.com/prompts/mobile-responsive-audit/")
    if clip != want:
        B.fail(f"Copy pointer is {clip!r}")
    if p.inner_text(".copy-btn") != "Copied!":
        B.fail("Copy shows no confirmation")
    src = (ROOT / "prompts/md/mobile-responsive-audit.md").read_text(encoding="utf-8")
    shown = p.inner_text("#prompt-body code")
    if shown.strip() not in src:
        B.fail("the prompt text on the page differs from the .md file")
    p.close()
    md = ctx.request.get(base + "md/mobile-responsive-audit.md")
    if md.status != 200 or md.text() != src:
        B.fail("prompts/md/mobile-responsive-audit.md is not served as written")


def main():
    shots = None
    if "--shots" in sys.argv:
        shots = sys.argv[sys.argv.index("--shots") + 1]
        pathlib.Path(shots).mkdir(parents=True, exist_ok=True)
    httpd, base = B.serve()
    base = base.replace("/invests/", "/prompts/")
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(channel="msedge", headless=True)
            ctx = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
            for path in PAGES:
                for theme in ("light", "dark"):
                    for size in (B.DESKTOP, B.PHONE):
                        p = B.load(ctx, base, path, theme, size,
                                   shots if path in ("index.html", "documentation/index.html") else None, wait=300)
                        if p.query_selector(".code-block-wrapper"):
                            p.click(".code-label")
                            sx = p.evaluate("document.documentElement.scrollWidth - window.innerWidth")
                            if sx > 1:
                                B.fail(f"prompts/{path} [{theme} {size['width']}px] expanded: scrolls sideways by {sx}px")
                        if size is B.DESKTOP:
                            B.contrast(p, f"prompts/{path} [{theme}]")
                        p.close()
            print(f"checked {len(PAGES)} pages", flush=True)
            behavior(ctx, base)
            browser.close()
    finally:
        httpd.shutdown()
    print(f"{len(B.fails)} failure(s)")
    sys.exit(1 if B.fails else 0)


if __name__ == "__main__":
    main()
