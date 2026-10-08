"""Build the core rule's page inventories from the snapshots in _sources/.

For every source page, lists everything on it in page order: head tags,
headings, paragraphs, list items, tables, links, images, controls, charts,
scripts and the browser storage keys and addresses the scripts use. Writes
inventory/<source>-<page>.md (to read and tick) and .json (for scripts/invests/check.py).
Text is kept in full so each item can be found on the new site.
"""
import html.parser, json, pathlib, re

# The site pages are in invests/ at the repository root; this folder
# (scripts/invests/) holds the scripts, the source snapshots and the inventories
# (build pass item 8, 2.14.0).
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent / "invests"
SRC = HERE / "_sources"
OUT = HERE / "inventory"
PAGES = {
    "stocks": ["index", "philosophy", "metrics", "indices", "finviz", "seekingalpha", "screener", "market", "faq"],
    "vix": ["index", "strategy", "custom"],
    "leverage": ["index", "3sig", "6sig", "9sig", "tqqq-ftlt", "holy-grail", "hfea"],
    "azqato.github.io": ["invests"],
}
WARN = re.compile(r"advice|risk|disclos|affiliate|referral|not (?:a )?recommend|past performance|lose|loss|no guarantee|educational", re.I)
REF = re.compile(r"[?&](ref|referral|aff|affiliate|invite|code|via|r)=|/(ref|referral|invite|join)/|refer", re.I)
BLOCK = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "dt", "dd", "blockquote", "figcaption", "summary", "caption", "label", "button", "option", "th", "td", "pre"}
SKIP = {"script", "style", "noscript", "template"}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items, self.head = [], []
        self.stack, self.texts = [], []
        self.region = []
        self.skip = 0
        self.script = None
        self.table = None

    def where(self):
        return self.region[-1] if self.region else "body"

    def add(self, kind, text, **extra):
        self.items.append({"n": len(self.items) + 1, "kind": kind, "region": self.where(), "text": text, **extra})

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("nav", "header", "footer", "aside", "main"):
            self.region.append(tag)
        if tag in SKIP:
            self.skip += 1
            if tag == "script":
                self.script = {"src": a.get("src"), "body": "", "attrs": {k: v for k, v in a.items() if k != "src"}}
            return
        if tag == "title":
            self.texts.append(["title", ""])
        elif tag == "meta" and a.get("content") and (a.get("name") or a.get("property")):
            self.head.append(f'{a.get("name") or a.get("property")}: {a["content"]}')
        elif tag == "link" and a.get("rel"):
            self.head.append(f'link {a["rel"]}: {a.get("href", "")}')
        elif tag == "a":
            self.texts.append(["a", "", a.get("href", ""), a.get("target"), a.get("rel")])
        elif tag in BLOCK:
            self.texts.append([tag, ""])
        elif tag == "img":
            self.add("image", a.get("alt", ""), src=a.get("src", ""))
        elif tag == "iframe":
            self.add("embed", a.get("title", ""), src=a.get("src", ""))
        elif tag == "canvas":
            self.add("chart canvas", a.get("aria-label", "") or a.get("id", ""), id=a.get("id"))
        elif tag in ("input", "select", "textarea"):
            desc = " ".join(f"{k}={v}" for k, v in a.items() if k in ("type", "id", "name", "value", "placeholder", "min", "max", "step", "checked", "aria-label"))
            self.add("control", desc, tag=tag)
        elif tag == "form":
            self.add("form", a.get("action", ""), id=a.get("id"))
        elif tag == "table":
            self.table = {"rows": 0, "cols": 0, "head": []}
        elif tag == "tr" and self.table is not None:
            self.table["rows"] += 1
            self.table["row"] = []
        elif tag == "svg":
            self.add("svg icon", a.get("aria-label", "") or ("decorative" if a.get("aria-hidden") else ""))
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in ("nav", "header", "footer", "aside", "main") and self.region:
            self.region.pop()
        if tag in SKIP:
            self.skip -= 1
            if tag == "script" and self.script:
                s = self.script
                self.add("script", s["src"] or f"inline, {len(s['body'])} characters", **scan_js(s["body"]))
                self.script = None
            return
        if tag == "table" and self.table is not None:
            t = self.table
            self.add("table", f'{t["rows"]} rows; first row: {" | ".join(t["head"])}')
            self.table = None
        if tag == "tr" and self.table is not None:
            self.add("table row", " | ".join(self.table.get("row", [])))
            self.table["row"] = []
        if not self.texts:
            return
        top = self.texts[-1]
        if tag == "a" and top[0] == "a":
            self.texts.pop()
            href = top[2]
            flags = []
            if REF.search(href or ""):
                flags.append("possible referral link")
            if top[3] == "_blank":
                flags.append("new tab")
            self.add("link", norm(top[1]), href=href, flags=flags)
            if self.texts:
                self.texts[-1][1] += top[1]
        elif tag == top[0]:
            self.texts.pop()
            text = norm(top[1])
            if tag == "title":
                self.head.insert(0, f"title: {text}")
            elif tag in ("th", "td"):
                if self.table is not None:
                    self.table.setdefault("row", []).append(text)
                    if self.table["rows"] <= 1:
                        self.table["head"].append(text)
            elif text:
                kind = {"li": "list item", "p": "paragraph", "dt": "term", "dd": "definition", "pre": "code"}.get(tag, tag)
                extra = {"flags": ["disclaimer or risk wording"]} if WARN.search(text) else {}
                self.add(kind, text, **extra)
    def handle_data(self, data):
        if self.script is not None:
            self.script["body"] += data
            return
        if self.skip:
            return
        if self.texts:
            self.texts[-1][1] += data
        elif norm(data):
            self.add("text", norm(data))


def scan_js(js):
    out = {}
    urls = sorted(set(re.findall(r"https?://[^\s'\"`)]+", js)))
    keys = sorted(set(re.findall(r"(?:local|session)Storage\.(?:get|set|remove)Item\(\s*['\"`]?([\w.-]+)", js)))
    fns = re.findall(r"function\s+(\w+)\s*\(", js)
    if urls:
        out["urls"] = urls
    if keys:
        out["storage keys"] = keys
    if fns:
        out["functions"] = fns
    if re.search(r"\.innerHTML\s*=", js):
        out["sets innerHTML"] = True
    return out


def write(source, name, page_items, head, extra_scripts):
    stem = f"{source}-{name}"
    data = {"source": f"{source}/{name}.html", "head": head, "items": page_items, "linked scripts": extra_scripts}
    (OUT / f"{stem}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    lines = [f"# Inventory - {source}/{name}.html", "",
             f"Generated by scripts/invests/inventory.py from the snapshot in _sources/ (commit in _sources/COMMITS.txt). "
             f"{len(page_items)} items. Tick each item when it's found on the new page; any item not moved needs the author's sign-off (core rule).", "",
             "## Head", ""] + [f"- [ ] {h}" for h in head] + ["", "## Page, in order", ""]
    for it in page_items:
        meta = []
        for k in ("href", "src", "id"):
            if it.get(k):
                meta.append(f"`{it[k]}`")
        meta += it.get("flags", [])
        for k in ("urls", "storage keys", "functions"):
            if it.get(k):
                meta.append(f"{k}: " + ", ".join(f"`{v}`" for v in it[k]))
        if it.get("sets innerHTML"):
            meta.append("sets innerHTML")
        region = "" if it["region"] == "body" else f" [{it['region']}]"
        text = it["text"].replace("|", "\\|")
        lines.append(f"- [ ] {it['n']}. **{it['kind']}**{region}: {text}" + (f" ({'; '.join(meta)})" if meta else ""))
    if extra_scripts:
        lines += ["", "## Scripts this page loads from the repo", ""]
        for path, info in extra_scripts.items():
            lines.append(f"- [ ] `{path}`: " + "; ".join(f"{k}: " + (", ".join(f"`{v}`" for v in val) if isinstance(val, list) else str(val)) for k, val in info.items()))
    (OUT / f"{stem}.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(page_items)


def main():
    OUT.mkdir(exist_ok=True)
    summary = []
    for source, names in PAGES.items():
        for name in names:
            path = SRC / source / f"{name}.html"
            p = Page()
            p.feed(path.read_text(encoding="utf-8"))
            scripts = {}
            for it in p.items:
                src = it["text"] if it["kind"] == "script" else ""
                local = (path.parent / src.split("?")[0]) if src and not src.startswith("http") else None
                if local and local.exists():
                    scripts[src] = scan_js(local.read_text(encoding="utf-8"))
            n = write(source, name, p.items, p.head, scripts)
            flagged = sum(1 for it in p.items if it.get("flags"))
            summary.append(f"| {source}/{name}.html | {n} | {sum(1 for i in p.items if i['kind'] == 'link')} | {flagged} |")
    (OUT / "README.md").write_text(
        "# Inventories\n\nOne per source page, generated by scripts/invests/inventory.py (core rule, step 1). "
        "Regenerate right before a page moves (Development plan, P1.4).\n\n"
        "| Page | Items | Links | Flagged |\n|---|---|---|---|\n" + "\n".join(summary) + "\n",
        encoding="utf-8", newline="\n")
    print("\n".join(summary))


if __name__ == "__main__":
    main()
