"""Import the owner's one-time AAII sentiment history download.

Usage:  python scripts/invests/weekly/aaii_import.py PATH
PATH is AAII's members' download (sentiment.xls), or the same table saved as
.xlsx or .csv. Reading .xls needs: pip install xlrd

Writes private/aaii-history.csv (date,bull,neut,bear in percent), which is
git-ignored: the history is AAII member data, so only statistics calculated
from it (averages, percentiles, streaks, past S&P 500 returns) are published.
fetch.py merges it with the public readings in data/aaii.json.

The header row is found by looking for a row naming Bullish, Neutral and
Bearish; the date is the first column. Values given as fractions (0.308) are
turned into percent. Rows without three numbers (AAII's notes and blank rows)
are skipped.
"""
import csv, pathlib, sys
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "private" / "aaii-history.csv"


def load(path):
    p = pathlib.Path(path)
    if p.suffix.lower() == ".csv":
        raw = pd.read_csv(p, header=None, dtype=str)
    else:
        raw = pd.read_excel(p, header=None, dtype=object)
    for i in range(min(len(raw), 30)):
        cells = [str(x).strip().lower() for x in raw.iloc[i]]
        if all(any(c.startswith(k) for c in cells) for k in ("bullish", "neutral", "bearish")):
            col = {k: next(j for j, c in enumerate(cells) if c.startswith(k)) for k in ("bullish", "neutral", "bearish")}
            return raw.iloc[i + 1:], col
    sys.exit("No header row naming Bullish, Neutral and Bearish in the first 30 rows.")


def num(x):
    try:
        f = float(str(x).replace("%", ""))
    except ValueError:
        return None
    return None if f != f else f


def main(path):
    body, col = load(path)
    out = {}
    for _, r in body.iterrows():
        d = pd.to_datetime(r.iloc[0], errors="coerce")
        vals = [num(r.iloc[col[k]]) for k in ("bullish", "neutral", "bearish")]
        if pd.isna(d) or None in vals:
            continue
        if sum(vals) < 2:  # fractions, not percent
            vals = [v * 100 for v in vals]
        if not 95 <= sum(vals) <= 105:
            print("skipped (does not add to 100):", d.date(), vals)
            continue
        out[str(d.date())] = [round(v, 1) for v in vals]
    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="\n") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["date", "bull", "neut", "bear"])
        for d in sorted(out):
            w.writerow([d] + out[d])
    days = sorted(out)
    print(f"wrote {len(days)} weeks, {days[0]} to {days[-1]}, to {OUT}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
