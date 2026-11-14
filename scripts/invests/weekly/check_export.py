"""Check the built Weekly Investing Report. Changes nothing in the repository.

Usage, from anywhere, after build.py:  python scripts/invests/weekly/check_export.py
Needs: pip install playwright && python -m playwright install chromium

Opens invests/weekly/index.html in a headless browser and fails (exit 1) if:
  - the page throws a script error;
  - any Explain button has no popup text;
  - the page scrolls sideways at phone width (375px);
  - in the Export (the US Letter report, one section per page), any page's
    content runs past the sheet, or any table is wider than the page.
Prints the spare space at the bottom of each export page, so a page that is
nearly full is visible before it overflows in a later week.
"""
import pathlib, sys, tempfile
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[3]
PAGE = (ROOT / "invests" / "weekly" / "index.html").as_uri()


def main():
    bad = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        errs = []
        pg = b.new_page(viewport={"width": 1000, "height": 900})
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(PAGE)
        missing = pg.evaluate("[...document.querySelectorAll('.explain')].filter(b=>!document.getElementById('x-'+b.dataset.x)).map(b=>b.dataset.x)")
        if missing:
            bad.append(f"Explain popups missing: {missing}")
        report = pg.evaluate("buildReport()")
        m = b.new_page(viewport={"width": 375, "height": 800})
        m.goto(PAGE)
        side = m.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        if side > 0:
            bad.append(f"phone width scrolls sideways by {side}px")
        with tempfile.TemporaryDirectory() as tmp:
            f = pathlib.Path(tmp) / "export.html"
            f.write_text(report, encoding="utf-8")
            e = b.new_page(viewport={"width": 900, "height": 1100})
            e.on("pageerror", lambda x: errs.append(str(x)))
            e.goto(f.as_uri())
            titles = e.evaluate("[...document.querySelectorAll('.page h2')].map(h=>h.textContent)")
            over = e.evaluate("[...document.querySelectorAll('.page')].map(p=>p.scrollHeight-p.clientHeight)")
            spare = e.evaluate("[...document.querySelectorAll('.page')].map(p=>{var f=p.querySelector('footer');"
                               "return Math.round(f.getBoundingClientRect().top-f.previousElementSibling.getBoundingClientRect().bottom)})")
            wide = e.evaluate("[...document.querySelectorAll('.page')].map(p=>[...p.querySelectorAll('.wrap')].some(w=>w.scrollWidth>w.clientWidth))")
            for i, t in enumerate(titles):
                flag = " OVERFLOWS" if over[i] > 0 else (" TABLE TOO WIDE" if wide[i] else "")
                print(f"page {i + 1}: {t:<40} spare {spare[i]:>4}px{flag}")
                if over[i] > 0:
                    bad.append(f"export page {i + 1} ({t}) runs {over[i]}px past the sheet")
                if wide[i]:
                    bad.append(f"export page {i + 1} ({t}) has a table wider than the page")
        b.close()
    bad += [f"script error: {x}" for x in errs]
    print("\n".join(["FAIL: " + x for x in bad]) or "OK: all checks passed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
