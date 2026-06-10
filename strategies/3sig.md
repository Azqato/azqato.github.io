# 3 Sig — Content Source

**Strategy:** The 3% Signal (3 Sig)
**Rebalancing cadence:** Quarterly
**Tickers:** IJR (original book) or SPY (current Kelly Letter), plus bond fund (BND, AGG, VFIIX, or SCHZ)
**Allocation:** 80% stock / 20% bond (starting base)
**Source file for:** 3sig.html

<!-- RESEARCH SOURCES — internal reference only, do not port to HTML -->
- https://jasonkelly.com/3sig/ (official 3 Sig plan overview and current implementation notes)
- https://jasonkelly.com/resources/strategies/ (comparison of 3 Sig, 6 Sig, and 9 Sig; fund selections and allocation details)
- https://jasonkelly.com/2017/01/how-my-signal-system-works/ (mechanical explanation of the signal line calculation)
- https://jasonkelly.com/2017/02/how-to-use-leveraged-etfs/ (Kelly's rationale for using leverage in the 6 Sig and 9 Sig variants)
- https://jasonkelly.com/2023/02/tqqq-and-volatility-decay/ (volatility decay discussion across all three plan variants)
- https://jasonkelly.substack.com/p/get-systematic-in-2024 (2024 update; confirms all three plans unchanged in structure)
- https://jasonkelly.substack.com/p/managing-cash-contributions (cash contribution mechanics common to all three plans)
- https://jasonkelly.com/books/3sig/ (The 3% Signal book; original fund selection, signal calculation, starting allocation)
- https://www.amazon.com/3-Signal-Investing-Technique-Change/dp/0142180955 (The 3% Signal book — Amazon listing)
- https://turboscribe.ai/transcript/2017612633175703830/the-30-down-rule (Jason Kelly video transcript explaining the 30 Down Rule for all three plans; fund assignments and ignore-count per plan)
- https://www.bogleheads.org/forum/viewtopic.php?t=190514 (2016 Bogleheads thread; independent analysis and value-averaging critique)
- https://www.cxoadvisory.com/volatility-effects/a-few-notes-on-the-3-signal/ (CXO Advisory review: testing limitations, data snooping risk, bond risk in rising rate environments)
- https://abovethegreenline.com/3sig/ (community implementation reference)
- https://medium.com/@Tech_Charles/the-3-signal-a-solid-core-investment-strategy-a01fa4b70c7e (community walkthrough of 3 Sig mechanics with starting allocation example)
- https://bestfolio.app/blog/kelly-signal-danger-v2 (independent corrected backtest; CAGR 9.0%, max DD -52.3%, Sharpe 0.31; identifies five prior simulation errors)
- https://www.reddit.com/r/TQQQ/comments/1i0ens0/can_anyone_explain_9sig_strategy_in_the_words_for/ (Reddit community explanation; confirms signal family math: target = 3% × leverage multiplier)
- https://www.reddit.com/r/TQQQ/comments/1i2g5lz/can_someone_explain_the_9sig_strategy_like_im_5/ (Reddit thread confirming 9% chosen for TQQQ's specific volatility characteristics)
<!-- END RESEARCH SOURCES -->

---

## Overview

The 3% Signal (3 Sig) is the conservative, unleveraged tier of Jason Kelly's Signal plan family, introduced in his 2015 book *The 3% Signal: The Investment Technique That Will Change Your Life*. It pairs a single stock index fund with a bond fund and rebalances quarterly to a 3% quarterly growth target.

The core principle is value averaging: the investor targets a specific dollar balance in the stock fund that grows at exactly 3% per quarter — approximately 12.6% annualized — regardless of what the market actually did. Each quarter, the portfolio is adjusted to hit that target. If the stock fund underperformed the target, bonds are sold to buy more shares. If the stock fund overperformed, the surplus is sold into bonds. The bond fund serves as the reserve from which purchases are funded and into which profits are deposited.

This structure mechanically compels buying when prices are low and selling when prices are high, relative to the signal line — inverting the emotional pattern that causes most retail investors to buy into rallies and sell into declines.

The three Signal plans form a family based on leverage. The quarterly target scales directly with the leverage multiplier of the stock fund: 3% for a 1x unleveraged fund (3 Sig), 6% for a 2x leveraged fund (6 Sig), and 9% for a 3x leveraged fund (9 Sig). 3 Sig is the entry point for the system and the subject of Kelly's book.

**Stock fund — original (book):** IJR (iShares Core S&P Small-Cap ETF). Kelly selected small-cap because its higher historical volatility creates larger buy-low and sell-high opportunities within each quarterly cycle. Small-cap index funds have historically returned approximately 11–12% annually, which supports a 3% quarterly target.

**Stock fund — current Kelly Letter version:** SPY (SPDR S&P 500 ETF Trust). The Kelly Letter's published 30 Down Rule documentation (October 2024) identifies SPY as the 3 Sig fund. The book's IJR-based implementation remains valid for readers following the original text.

Jason Kelly explicitly positions 3 Sig as an "easy" system: "just one stock index fund and one bond index fund," quarterly rebalancing that takes approximately 15 minutes, no market timing, no news monitoring, and no predictions required. The system requires only reaction to what prices already did, not forecasts of what they will do.

---

## Rules and Logic

**Starting allocation:**

| Asset | Fund | Weight |
|-------|------|--------|
| Stock fund | IJR (book) or SPY (Kelly Letter) | 80% |
| Bond fund | BND, AGG, VFIIX, or SCHZ | 20% |

The 80/20 allocation is the starting base only. The actual ratio drifts continuously between quarterly rebalances as markets move; the plan targets a signal line dollar amount, not a fixed percentage.

**Signal line calculation:**

Each quarter, a target dollar balance is calculated called the signal line:

> Signal line = (Previous quarter-end stock fund balance) × 1.03

When new cash contributions are added during the quarter:
> Signal line = (Previous quarter-end stock fund balance) × 1.03 + (Half of new quarterly contributions)

All new cash contributed during a quarter goes entirely to the bond fund. At rebalancing time, half of those new contributions is added to the signal line target, which effectively deploys the new money partially into equities.

**Quarterly rebalancing:**

| Outcome | Action |
|---------|--------|
| Stock fund balance > signal line | Sell the surplus; proceeds go to bond fund |
| Stock fund balance < signal line | Buy the shortfall; funded from bond fund |
| Stock fund balance = signal line | No trade |

All dividends from both funds are reinvested into the bond fund, keeping the bond sleeve as the capital reserve.

**30 Down Rule:**

The 30 Down Rule activates when the stock fund's quarterly closing price falls at least 30% below its quarterly closing price high within the rolling past two years. Only quarterly closing prices count toward the trigger — intra-quarter prices are ignored.

When active, the plan locks in place:
- The next **4 consecutive sell signals are ignored**
- Buy signals during the locked phase are followed as normal

After 4 sell signals have been ignored (within two years), the plan **resumes normal operations without resetting** the allocation. This distinguishes 3 Sig from 6 Sig and 9 Sig, which do reset to a base allocation after their locked phases end.

The rule's purpose is psychological: after a 30%+ quarterly decline, media coverage will uniformly project further losses. Without the rule, the plan would resume selling as markets recover, reducing gains from the rebound. Locking in place preserves full equity exposure during the ascent.

Historical 30 Down activations for 3 Sig:
- Spring 2020: COVID crash. Plans locked in for the 2020–2021 recovery.
- 2022: SPY did not close a quarter 30% below its 2-year high, so this rule did not activate for 3 Sig during the 2022 bear market.

---

## Performance Notes

The 3% quarterly signal projects to approximately 12.6% annually (1.03^4 − 1 ≈ 12.55%). This target was calibrated to small-cap index historical averages of roughly 11–12% annually. It is a target that must be funded from bonds when not met by market performance, not a return that is delivered passively.

**Independent corrected backtest (BestFolio, 2024):**

| Metric | 3 Sig (IJR + BND, real data) |
|--------|------------------------------|
| CAGR | 9.0% |
| Max drawdown | −52.3% |
| Sharpe ratio | 0.31 |

The BestFolio analysis corrected five implementation errors present in prior community simulators: wrong starting allocation (80/20 vs. 60/40), incorrect 30 Down trigger lookback (all-time high vs. rolling 8-quarter high), wrong trigger response (dumping all bonds vs. skipping the specified number of sells), missing buy throttle, and absent reset logic. The corrected figures represent a more realistic live implementation.

**Community backtest (Bogleheads forum, 2016):** An independent investor ran 3 Sig against a buy-and-hold position in the same underlying fund from 2000 and from 1993. In both test windows, simple buy-and-hold outperformed 3 Sig in total return by the end of the period.

**Open-system vs. closed-system distinction:** Published community simulations of the Signal plans almost universally assume regular monthly contributions of several hundred dollars. These ongoing deposits continuously replenish the bond buffer. In a closed system — starting capital only, no new money — the bond buffer eventually depletes after a severe multi-quarter decline. For 3 Sig (unleveraged), the exposure to this failure mode is lower than for 6 Sig and 9 Sig, but extreme bear markets lasting several years can still exhaust the buffer and leave the plan effectively as 100% equities.

**Performance during bull markets:** In a sustained, strong bull market, the quarterly sell signal fires consistently, moving profit from the stock fund into bonds. This reduces equity exposure over time and caps upside capture relative to a full buy-and-hold position in the same fund. The plan's advantage is better performance in choppy and bear markets; its disadvantage is underperformance in extended bull runs.

---

## Risks and Caveats

**Bond buffer depletion.** In a severe or extended bear market, the plan repeatedly signals to buy from the bond fund. Each quarter the market falls short of the signal line, bonds are sold to fund TQQQ purchases. If this continues for many quarters, the bond fund depletes. At that point the plan holds 100% equities with no dry powder for further dips and no buffer against continued losses. Recovery from this state depends entirely on markets reversing. This risk is lower for 3 Sig than for the leveraged variants but is not eliminated.

**Bond fund losses in rising rate environments.** The bond fund is not a riskless cash equivalent. Intermediate-term and total bond market funds fall in value when interest rates rise. The Federal Reserve's 2022–2023 rate hiking cycle produced simultaneous losses in both the equity fund and the bond fund, reducing the buffer just as it was being drawn down for equity purchases. The plan assumes the bond fund is a stable reserve; this assumption fails in inflationary rate-hiking cycles.

**The 3% target is fixed regardless of market conditions.** The signal line grows at 3% per quarter whether the underlying index is returning 2% or 20% over that period. In a prolonged bear market, the plan keeps buying — drawing the buffer down toward zero. The target does not adapt to valuations, interest rates, or market regimes. There is no built-in recognition that the market might not recover on the same timeline the plan assumes.

**Performance vs. buy-and-hold is not reliably superior.** Community backtesting has not consistently demonstrated that 3 Sig outperforms simple buy-and-hold in the same fund. The value-averaging mechanics force buying lower and selling higher relative to the signal line, but this is measured against a 3% quarterly target — not against the fund's actual trajectory. In a strong bull market, constant profit-taking reduces equity exposure and captures a smaller share of the rally.

**The 3% and IJR parameter choices carry data snooping risk.** CXO Advisory notes that selecting small-cap equity and 3% as the signal threshold both involve parameters that were likely chosen partly because they fit the historical period being examined. Out-of-sample performance may differ from backtest results.

**Tax drag in taxable accounts.** Each sell signal generates capital gains. With up to four potential sell events per year, held over many years, the tax drag on after-tax compounding is significant. The plan is best suited to Roth IRAs, traditional IRAs, or 401k accounts where rebalancing does not trigger taxable events.

---

## Resources

*The 3% Signal* (Jason Kelly, 2015, Plume/Penguin) — the full original book. Covers the 3 Sig mechanics, historical backtest, the 30 Down Rule, and implementation guidance for 401ks and IRAs. ISBN: 978-0142180952.

The Kelly Letter (jasonkelly.com) — Jason Kelly's subscriber newsletter. Contains the official weekly plan status, current signal line values, 30 Down Rule state for all three plans, and all plan updates.

Jason Kelly's strategy overview (jasonkelly.com/resources/strategies/) — free public summary of the 3 Sig, 6 Sig, and 9 Sig plans with fund selections.

BestFolio corrected backtest (bestfolio.app/blog/kelly-signal-danger-v2) — independent backtesting with corrected implementation and critical drawdown analysis across all three plan variants.
