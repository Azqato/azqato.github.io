# 9 Sig Calculator: interpretation and plan

Written 2026-10-05 at the owner's request. It covers phase 1 (interpretation, read only) and phase 2 (the plan). Phase 3, the build, starts on the owner's go-ahead. The owner gave Claude the final say on best practice and formatting.

**Source.** Screenshots of a community Google Sheet, the "9-SIG Excel Calculator" posted to r/TQQQ, with its author's notes. It was checked against the site's own 9 Sig page (`invests/leveraged/9sig.html`). The sheet's sample run (Kelly Letter figures, $300,000 TQQQ and $200,000 AGG from 2017-01-31, plus $3,000 a quarter) matches those rules exactly. For example, round 2's signal line is 300,000 × 1.09 + 3,000 ÷ 2 = 328,500, and the sheet shows 328,500.

---

## Phase 1: interpretation

### What the sheet is

It's a **journal and calculator, not a backtester**. Each quarter you type in what happened: the date, TQQQ's quarter-end price, the bond fund's price, any cash income, and the command for that quarter. The sheet then works out the signal line, the trade, the new holdings, and a dashboard of results. Nothing is fetched automatically, and the strategy's judgment calls (HOLD, REBALANCE) are commands you enter, not decisions the sheet makes.

### Settings (cells C3 to C7, plus the picker at the bottom right)

| Setting | Meaning | Example |
|---|---|---|
| Stock positions | Starting amount in the stock fund | $300,000 (60%) |
| Bond positions | Starting amount in the bond fund | $200,000 (40%) |
| Investment Amount | New cash added each quarter | $3,000 |
| "Monthly" Growth Rate | The quarterly target: 3% (3 Sig), 6% (6 Sig) or 9% (9 Sig). Labeled "monthly" in the sheet, but it is quarterly | 9% |
| Buying Power Throttle | The reserve kept in bonds on a buy: 10% means a buy can use at most 90% of the bond balance | 10% |
| Stock fund | TQQQ, MVV or IJR | TQQQ |
| Bond fund | AGG, BND or SCHZ | AGG |
| Language | EN or Chinese | EN |

### One row per quarter: inputs and calculations

| Column | Input or calculated | What it is |
|---|---|---|
| Date | **Input** | Quarter-end date. Entering it starts the row's calculations |
| Price | **Input** | Stock fund's quarter-end close |
| MoM | Calculated | Price change since the last quarter (the label says month; it's per quarter) |
| Round | Calculated | Quarter number, 0 for the start |
| Balance Before Action | Calculated | Stock shares × price |
| Sig Line | Calculated | Last quarter's stock balance after trades × (1 + target) + half of this quarter's new cash |
| 30% RULE | Calculated flag | Price is at least 30% below the highest quarter-end close of the last two years (8 quarters) |
| Order Adjust | **Input** (N/A, HOLD, REBALANCE) | N/A: follow the signal. HOLD: skip this quarter's sell (the 30 Down rule's ignored sells). REBALANCE: reset to the starting split (60/40) |
| Bond price, shares, value | Price is **input** | The bond fund before the trade; the new cash buys bond shares |
| Expected Investment | Calculated | Sig line − balance: positive means buy, negative means sell |
| Stock Price at Adjustment | **Input** (defaults to Price) | The price the trade actually filled at |
| Adjusted Amount, Shares | Calculated | The trade after the throttle and the command |
| Accumulated Shares | Calculated | Stock shares after the trade (fractional) |
| Bond adjustment price, Bond Adjustment, Bond shares | Price is **input** (defaults to the bond price) | Bond shares sold to fund a buy, or bought with a sell's proceeds (whole shares) |
| Stock value, Bond value, Cash, Total Assets, Cash ratio | Calculated | Holdings after the trade. Cash is what's left over from whole bond shares. "Cash ratio" is the bond and cash share of the total |
| Contributions | From the settings | The new cash this quarter |
| Profit and Loss This Period, Unrealized Gain/Loss, Stock Growth, Total Gain/Loss, ROI, MoM | Calculated | Performance |
| Stock Cost Price, Average Price, Total Investment Cost, Net Value | Calculated | Cost basis. Net Value is total assets ÷ money put in |
| Drawdown | Calculated | Fall from the highest total assets so far |
| Cash Income | **Input** | Dividends or bond interest received |
| Accumulated Cash Income, Realized Cash Amount, Cumulative cash-out | Calculated | Income and money taken out |

### Dashboard

- A one-line headline: rounds run, start and end value, total cost, return, annualized return.
- A summary column: current holdings, cost, shares, gain, ROI, annualized return, total cost, max drawdown, and counts of HOLD, REBALANCE and N/A quarters, bond and cash shortages, profitable and unprofitable rounds.
- Four charts: ROI over time (line), drawdown (area), total assets by quarter (bars) and the stock/bond split today (pie).
- Highest stock value and highest total assets.

### Key concepts the tool has to get right

1. **Value averaging toward a signal line.** The target grows at 3, 6 or 9% a quarter. Above the line, sell the excess into bonds; below it, buy from bonds.
2. **New cash** goes to bonds first, and half of it raises the signal line.
3. **The throttle.** A buy never uses more than (100% − throttle) of the bond balance. When bonds run out, the buy is cut short and counted as a bond shortage.
4. **The 30 Down rule.** A drop of 30% or more from the two-year quarterly high flags the quarter. While the rule is on, the next two sells are ignored (HOLD), and then the plan resets to 60/40 (REBALANCE).
5. **Spike Reset** (9 Sig only, from our page). After a quarter with a gain of 100% or more, if the stock share is between 60% and 100% and the 30 Down rule is off, reset to 60%.
6. **Whole bond shares, fractional stock shares,** with leftover cash.
7. **Results:** ROI, annualized return, drawdown, cost basis.

### What the sheet leaves to the user, and what the web version can do better

- In the sheet, the commands are typed by hand. The web version should **suggest** the command (it knows the 30 Down and Spike Reset rules from our own page) and let the user override it, so it stays a journal of what they actually did.
- Its labels are confusing in places ("Monthly Growth Rate", "MoM", "Cash ratio"). The web version uses plain names.
- The sheet is for one plan only. The web version keeps the 3/6/9% choice, so it serves 3 Sig and 6 Sig too, with 9 Sig as the default.

### What needs to be built

1. A settings panel (the C3 to C7 equivalents, plus the funds).
2. A quarter table: add, edit and delete rows, with inputs in a few columns and everything else calculated.
3. The calculation engine (the rules above), shown live as you type.
4. A dashboard: a headline, summary tiles and four charts.
5. Saving in the browser, automatically.
6. Export to Excel (.xlsx), plus a backup file you can import again, because browser storage can be cleared.
7. **Import** (owner's request, 2026-10-05): bring in a user's own history, from a file of ours or from their own spreadsheet.
8. A disclaimer, and the attribution the source asks for.

---

## Phase 2: the plan

### Where it lives

- **A new tool page: `invests/leveraged/9sig-calculator.html`**, titled "9 Sig Calculator". It sits in the sidebar under Leveraged Strategies, right after 9 Sig. It is listed in the site search and sitemap, and gets the full site shell (top bar, second bar, theme button, footer).
- The 9 Sig page gets a "Track your own plan: 9 Sig Calculator" link near the top. The 3 Sig and 6 Sig pages get a line that the calculator also runs at 3% and 6%.
- `scripts/invests/site.py` learns one new kind of page: one written for this site rather than moved from an old one. Its source is in `scripts/invests/pages/`. That keeps the core rule's inventory check meaningful (there is nothing old to preserve on this page) while the page still gets the generated shell.

### How it's built (the site's rules: no build step, no dependencies)

- **Plain HTML, CSS and JavaScript.** One script, `invests/assets/js/sig-calc.js`. There are no outside libraries, and it works offline once the page has loaded.
- **Charts are drawn as SVG by the script.** A charting library would be the site's first dependency. Four simple charts don't justify one, and SVG follows the light and dark themes through the site's color tokens.
- **Excel export without a library.** A real `.xlsx` is a zip of a few XML files. The script writes it directly, using an uncompressed zip with CRC32: about 120 lines. The workbook has three sheets, Settings, Quarters (every column above, as numbers, with formats) and Summary. It opens cleanly in Excel, Google Sheets and Numbers. A CSV export comes along almost free.
- **Saving.** Everything is in `localStorage` under one key (`azqato-sig-calc-v1`), saved on every change. The "v1" lets a later version migrate old data. Every read and write is wrapped in try/catch, as the site already does, so a private window still works; it just doesn't remember.
- **Backup and restore.** "Download backup" saves a `.json` file and "Restore" loads one, because cleared browser data would otherwise lose a user's whole history. The page says so plainly next to the buttons.
- **Import (owner's request, 2026-10-05).** One "Import" button takes any of these:
  - **Our own files:** the backup `.json`, our `.xlsx` export, or our CSV. These restore everything exactly.
  - **The user's own spreadsheet,** as `.xlsx` or `.csv`. That includes the community 9-SIG sheet downloaded from Google Sheets (File, Download, .xlsx). The script reads the file's header row and matches the columns it knows by name: Date, Price, Order Adjust, Bond prices, Stock Price at Adjustment, Adjustment of bond prices and Cash Income. It also matches common alternatives (for example "Close", "TQQQ", "Action", "Bond price", "Dividends"). It reads the starting amounts and new cash from a Settings sheet if one is there.
  - **Only the inputs are imported.** Every calculated column is recalculated by our engine rather than trusted from the file, so a sheet with its own rounding or a broken formula can't put wrong numbers into the plan.
  - **A preview before anything changes.** The preview shows how many quarters were found, which columns matched (and any it ignored), the first and last rows, and any problems row by row, such as an unreadable date, a missing price or a date out of order. The user picks **New plan** (the default, so nothing is overwritten) or **Replace this plan**, then confirms.
  - **No library.** `.xlsx` files are zips. Browsers unzip them natively (`DecompressionStream`), and the script reads the sheet XML itself. Dates stored as Excel serial numbers and as text (2025/10/31, 2025-10-31, 10/31/2025) are all understood.
  - The file never leaves the browser; the page says so next to the button.
- **Several plans.** A plan picker lets someone track, say, a real account and a test plan side by side. Each plan has its own settings and quarters. One plan is enough to start; the picker is cheap to add now and costly to retrofit.

### Layout (best practice: inputs first, the answer at the top)

1. **"This quarter" card, at the top.** It's the reason people come back each quarter: today's signal line, the suggested action ("Buy $12,340 of TQQQ (102.4 shares) from AGG"), and any rule in force ("30 Down: 1 of 2 sells ignored"). One glance answers "what do I do now?".
2. **Settings,** collapsible once the plan has quarters. It holds the starting stock and bond amounts, the quarterly new cash, the target (3, 6 or 9%, default 9%), the throttle (default 10% reserve, which is the 90% rule), the stock fund (TQQQ default; MVV, IJR or any ticker) and the bond fund (AGG default; BND, SCHZ, SGOV or any ticker).
3. **Dashboard:** the headline sentence, then summary tiles (total assets, total gain, ROI, annualized return, max drawdown, stock/bond split), then the four charts. On phones the tiles become two columns and the charts stack.
4. **Quarter table.** "Add quarter" opens a short form with only the inputs: date, stock price, bond price, cash income, the command (pre-filled with the suggestion), and optional fill prices. The full calculated table sits below it. It scrolls sideways inside its own box, with Date and Round frozen on the left, and the column groups are color-banded as in the sheet. On phones the table offers a "key columns" view. Rows are editable in place and recalculate everything after them.
5. **Data:** Import, Export to Excel, Export CSV, Download backup, and Clear plan (asks for confirmation). Restoring a backup goes through Import.
6. **Notes:** what each rule does (linking to our 9 Sig page), the disclaimer, and credit.

### Formatting rules

- Money as $1,234,567, with no cents in the table and cents in the trade line. Prices with two decimals; shares with three decimals for stock and whole numbers for bonds; percentages with two decimals.
- Losses in the site's red token, gains in its green, with an arrow or sign as well, so color is never the only signal.
- Every input has a label, works by keyboard, and has a sensible default. The suggested action is announced to screen readers.
- No em dashes (site writing rule). Numbers are right-aligned in tabular figures.

### Checking it's right

- **Golden test.** Enter the first six quarters of the sheet's sample run (prices from the screenshot) and check the signal line, the trades, the shares and the totals against the sheet's own figures, to the dollar. This goes into `scripts/invests/browser.py` so it reruns on every change.
- `check.py` and `browser.py` cover the new page: 0 console errors in both themes, no sideways page scroll on phones, and an export that produces a valid zip.
- Open the exported `.xlsx` in Excel and confirm it opens without a repair prompt.

### Legal and attribution

- The page says: an independent tool, not affiliated with Jason Kelly or The Kelly Letter; for the official plan, subscribe at jasonkelly.com. It also carries the site's "Educational use only. Not financial advice."
- It uses only rules already published on our 9 Sig page. Nothing beyond them from the paid letter.
- Credit: "Layout inspired by a community 9-SIG spreadsheet shared on r/TQQQ." The sheet is shared privately and its author asks that it not be redistributed, so we don't copy its files, formulas or wording. We rebuilt the idea from the public rules.

### Build order (phase 3)

1. The calculation engine and the golden test, first and on their own, so the numbers are proven before any screen exists.
2. The page shell (site.py support), settings, quarter form and table, and saving.
3. The dashboard and charts.
4. Excel, CSV, backup, and Import (our files first, then outside spreadsheets with the column matcher and preview). The golden test also imports a copy of the sample run as `.xlsx` and `.csv` and checks the same figures.
5. Links from 3, 6 and 9 Sig; docs (PRD feature entry, DESIGN, PATCHNOTES 2.16.0); checks; screenshots in both themes and on phones; commit and push.

### Open points (Claude's default in bold; the build uses it unless the owner says otherwise)

1. The page name: **"9 Sig Calculator"** (it also runs 3% and 6%).
2. Language: **English only** for now; the sheet's Chinese option is left out.
3. Prices are typed in by hand, as in the sheet. **Later, optionally:** pre-fill the quarter-end close from a data feed. That would mean a new feed in the stocks repo (site rule: no data jobs in this repository), so it's a separate item.
