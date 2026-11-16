"""Write the export view of the Weekly Investing Report as a demo, to try changes
before they go live. Changes nothing in the repository.

Usage, from anywhere:  python scripts/invests/weekly/demo.py 2026-11-13 [PATH]
PATH defaults to the owner's Downloads/weekly-report-demo.html.
--mock-invert previews the inversion callout with made-up yields (10-year 4.60%,
10-year minus 2-year -0.26), written by default to weekly-report-demo-inverted.html.
Needs: pip install playwright && python -m playwright install chromium

Builds the page with build.py --demo (site links made absolute) into a temporary
folder, runs its Export (buildReport) in a headless browser, and writes the
resulting US Letter report, one section per page, to PATH. Then check it with
check_export.py's export checks by running:  python scripts/invests/weekly/demo.py --check PATH
"""
import os, pathlib, subprocess, sys, tempfile
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT = pathlib.Path.home() / "Downloads" / "weekly-report-demo.html"


def export(friday, out, mock=False):
    with tempfile.TemporaryDirectory() as tmp:
        page = pathlib.Path(tmp) / "index.html"
        env = dict(os.environ, WEEKLY_MOCK_INVERT="1") if mock else None
        subprocess.run([sys.executable, str(HERE / "build.py"), friday, "--demo", str(page)], check=True, env=env)
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page()
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto(page.as_uri())
            report = pg.evaluate("buildReport()")
            b.close()
    if errs:
        sys.exit("script error: " + "; ".join(errs))
    out.write_text(report, encoding="utf-8", newline="\n")
    print("wrote export demo", out)


def check(path):
    bad = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        e = b.new_page(viewport={"width": 900, "height": 1100})
        e.goto(path.resolve().as_uri())
        titles = e.evaluate("[...document.querySelectorAll('.page')].map(p=>p.querySelector('h2').textContent)")
        over = e.evaluate("[...document.querySelectorAll('.page')].map(p=>p.scrollHeight-p.clientHeight)")
        spare = e.evaluate("[...document.querySelectorAll('.page')].map(p=>{var f=p.querySelector('footer');"
                           "return Math.round(f.getBoundingClientRect().top-f.previousElementSibling.getBoundingClientRect().bottom)})")
        wide = e.evaluate("[...document.querySelectorAll('.page')].map(p=>[...p.querySelectorAll('.wrap')].some(w=>w.scrollWidth>w.clientWidth))")
        b.close()
    for i, t in enumerate(titles):
        flag = " OVERFLOWS" if over[i] > 0 else (" TABLE TOO WIDE" if wide[i] else "")
        print(f"page {i + 1}: {t:<40} spare {spare[i]:>4}px{flag}")
        if over[i] > 0 or wide[i]:
            bad.append(t)
    print("FAIL: " + ", ".join(bad) if bad else "OK: all pages fit")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    a = sys.argv[1:]
    mock = "--mock-invert" in a  # preview the inversion callout with made-up yields
    a = [x for x in a if x != "--mock-invert"]
    if a and a[0] == "--check":
        check(pathlib.Path(a[1]) if len(a) > 1 else DEFAULT)
    elif len(a) in (1, 2):
        export(a[0], pathlib.Path(a[1]) if len(a) > 1 else DEFAULT.with_name("weekly-report-demo-inverted.html") if mock else DEFAULT, mock)
    else:
        sys.exit(__doc__)
