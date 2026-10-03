"""Read-only checks for the Azqato Invests site. Changes nothing.

Run from anywhere: python scripts/check.py
Checks every site page (*.html outside _sources/, inventory/ and docs/):
  - a title that follows Page Titles in ../docs/PRD.md (Part 2) (brand suffix, 60 characters,
    first 30 characters unique, no placeholders; Home leads with the brand);
  - internal links and assets resolve to files;
  - no template demo text survives;
  - no em dashes in page text, moved source text included (Question 14);
  - inventory coverage: for each page mapped in inventory/map.json, every
    item's text from its source page appears on the new page(s).
Exits 1 if any check fails.
"""
import html.parser, json, pathlib, re, sys
from urllib.parse import urlparse, unquote

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {"_sources", "inventory", "docs", "scripts", ".git", "assets"}
BRAND = "Azqato Invests"
SEP = " - "
DEMO = ["Parcelpoint", "API v3.4", "Get API keys", "Back to Template Interface"]
# No em dash anywhere in a page file, in either form (Question 19: the missing-
# value placeholder is an en dash, and the main repository's hook agrees).
PUNCT_DASH = re.compile(r"\u2014|&mdash;")
# Inventory items removed on purpose, with the owner's approval. The inventories
# stay a record of the sources; these numbers are simply not expected on the
# pages any more. P11, 2026-10-02: two dead links on Resources.
REMOVED = {"azqato.github.io-invests.json": {108, 109, 130, 131}}
PLACEHOLDERS = {"untitled", "document", "home", "index", "introduction - parcelpoint docs"}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


class Read(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.refs, self.text, self.ids = None, [], [], set()
        self._in_title = False
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "title":
            self._in_title, self.title = True, ""
        if tag in ("script", "style"):
            self.skip += 1
        for k in ("href", "src"):
            if a.get(k):
                self.refs.append(a[k])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in ("script", "style"):
            self.skip -= 1

    def handle_data(self, d):
        if self._in_title:
            self.title += d
        elif not self.skip:
            self.text.append(d)


def squash(s):
    """Text for the presence check: no whitespace (inline tags split text
    differently on the new pages), and no em dashes, hyphens or commas (em
    dashes in moved text are replaced with a hyphen, a comma or, as a
    missing-value placeholder, an en dash, Questions 14 and 19)."""
    return re.sub(r"[\s—–,\-|]+", "", s)


def found(item, have, ids):
    """Whether a source inventory item is on its new page(s)."""
    if item["kind"] in ("script", "svg icon", "table"):
        return True
    # Items in the source sites' own navigation (region nav or aside) are
    # replaced by this site's sidebar and top bar, which carry every destination.
    if item.get("region") in ("nav", "aside"):
        return True
    if item["kind"] in ("control", "chart canvas", "form"):
        m = re.search(r"id=(\S+)", item["text"])
        key = item.get("id") or (m.group(1) if m else None)
        return key in ids if key else True
    if item["kind"] in ("image", "embed"):
        return True
    text = squash(item["text"])
    return not text or text in have


REFRESH = re.compile(r'http-equiv="refresh" content="0; url=([^"#]*)(#[^"]*)?"')


def pages():
    """Site pages. A retired address (site.py's MOVED) is a redirect page; it's
    checked by redirects() instead."""
    for p in sorted(ROOT.rglob("*.html")):
        if not SKIP_DIRS & set(p.relative_to(ROOT).parts) and not REFRESH.search(p.read_text(encoding="utf-8")):
            yield p


def redirects():
    """Each redirect page must reach an existing page and section in one hop."""
    fails = []
    for p in sorted(ROOT.rglob("*.html")):
        if SKIP_DIRS & set(p.relative_to(ROOT).parts):
            continue
        t = p.read_text(encoding="utf-8")
        m = REFRESH.search(t)
        if not m:
            continue
        target = (p.parent / m.group(1)).resolve()
        rel = p.relative_to(ROOT).as_posix()
        if not target.exists():
            fails.append(f"{rel}: redirects to a missing page {m.group(1)}")
        elif REFRESH.search(target.read_text(encoding="utf-8")):
            fails.append(f"{rel}: redirects to another redirect {m.group(1)}")
        elif m.group(2) and f'id="{m.group(2)[1:]}"' not in target.read_text(encoding="utf-8"):
            fails.append(f"{rel}: target has no section {m.group(2)}")
    return fails


def main():
    fails, notes = [], []
    seen30 = {}
    parsed = {}
    for p in pages():
        rel = p.relative_to(ROOT).as_posix()
        r = Read()
        r.feed(p.read_text(encoding="utf-8"))
        parsed[rel] = r
        body = norm(" ".join(r.text))
        t = norm(r.title or "")
        is_home = rel == "index.html"
        if not t or t.lower() in PLACEHOLDERS:
            fails.append(f"{rel}: missing or placeholder title {t!r}")
        else:
            if len(t) > 60:
                fails.append(f"{rel}: title is {len(t)} characters (max 60): {t}")
            if is_home and not t.startswith(BRAND + SEP):
                fails.append(f"{rel}: Home's title should lead with the brand: {t}")
            if not is_home and (not t.endswith(SEP + BRAND) or t[: -len(SEP + BRAND)].count(BRAND)):
                fails.append(f"{rel}: title should be '<page>{SEP}{BRAND}': {t}")
            key = t[:30]
            if key in seen30:
                fails.append(f"{rel}: first 30 characters match {seen30[key]}: {key!r}")
            seen30[key] = rel
        for ref in r.refs:
            u = urlparse(ref)
            if u.scheme or ref.startswith(("#", "//", "data:", "mailto:")):
                continue
            target = (p.parent / unquote(u.path)).resolve()
            if u.path and not (target.exists() or (target / "index.html").exists()):
                fails.append(f"{rel}: broken link {ref}")
        for d in DEMO:
            if d in body or d in (r.title or ""):
                fails.append(f"{rel}: template demo text survives: {d!r}")
        dashes = len(PUNCT_DASH.findall(p.read_text(encoding="utf-8")))
        if dashes:
            fails.append(f"{rel}: {dashes} em dash(es) in the page; replace them under Writing Style (Questions 14 and 19)")

    mp = ROOT / "inventory" / "map.json"
    if mp.exists():
        for src, targets in json.loads(mp.read_text(encoding="utf-8")).items():
            inv = json.loads((ROOT / "inventory" / src).read_text(encoding="utf-8"))
            have = squash(" ".join(" ".join(parsed[t].text) for t in targets if t in parsed))
            ids = set().union(*(parsed[t].ids for t in targets if t in parsed))
            missing = [i for i in inv["items"] if i["n"] not in REMOVED.get(src, set()) and not found(i, have, ids)]
            if missing:
                fails.append(f"{src}: {len(missing)} inventory items not found on {', '.join(targets)} (first: #{missing[0]['n']} {missing[0]['text'][:60]!r})")

    fails += redirects()
    n = len(parsed)
    for line in notes:
        print("note:", line)
    for line in fails:
        print("FAIL:", line)
    print(f"{n} page(s) checked, {len(fails)} failure(s), {len(notes)} note(s)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
