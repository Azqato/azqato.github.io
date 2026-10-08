"""Download read-only snapshots of the source sites into _sources/.

Fetches every HTML, CSS and JS file (not data files) from each source repo's
main branch with the GitHub CLI, and writes _sources/COMMITS.txt with the
commit each snapshot came from. Never writes to the source repos.
"""
import json, pathlib, subprocess, datetime

# The site pages are in invests/ at the repository root; this folder
# (scripts/invests/) holds the scripts, the source snapshots and the inventories
# (build pass item 8, 2.14.0).
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent / "invests"
OUT = HERE / "_sources"
REPOS = {"stocks": None, "vix": None, "leverage": None, "azqato.github.io": ["invests.html"]}

def gh(*args):
    return subprocess.run(["gh", "api", *args], capture_output=True, check=True).stdout

lines = [f"Snapshot taken {datetime.datetime.now().astimezone():%Y-%m-%d %H:%M %Z}"]
for repo, only in REPOS.items():
    sha = json.loads(gh(f"repos/Azqato/{repo}/commits/main"))["sha"]
    tree = json.loads(gh(f"repos/Azqato/{repo}/git/trees/{sha}?recursive=1"))["tree"]
    paths = [t["path"] for t in tree if t["type"] == "blob"]
    if only:
        paths = [p for p in paths if p in only]
    else:
        paths = [p for p in paths if p.endswith((".html", ".css", ".js")) and not p.startswith(("data/", "docs/"))]
    for p in paths:
        dest = OUT / repo / p
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(gh(f"repos/Azqato/{repo}/contents/{p}?ref={sha}", "-H", "Accept: application/vnd.github.raw"))
    lines.append(f"{repo} {sha} {len(paths)} files")
    print(lines[-1])
(OUT / "COMMITS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
