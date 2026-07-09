# 6 Sig: Content Source

**Strategy:** The 6% Signal (6 Sig)
**Rebalancing cadence:** Quarterly
**Tickers:** MVV (ProShares Ultra MidCap400, 2x leveraged), plus bond fund (BND, AGG, or similar)
**Allocation:** 60% stock / 40% bond (base, resets to this after 30 Down phase)
**Source file for:** 6sig.html

<!-- RESEARCH SOURCES: internal reference only, do not port to HTML -->
- https://jasonkelly.com/resources/strategies/ (comparison of 3 Sig, 6 Sig, and 9 Sig; fund selections and allocation details for 6 Sig)
- https://jasonkelly.com/2017/01/how-my-signal-system-works/ (signal line calculation mechanics; applies equally to all three plans)
- https://jasonkelly.com/2017/02/how-to-use-leveraged-etfs/ (Kelly's rationale for using 2x and 3x leverage in the signal system)
- https://jasonkelly.com/2023/02/tqqq-and-volatility-decay/ (volatility decay discussion; applies to both 6 Sig and 9 Sig leveraged variants)
- https://jasonkelly.substack.com/p/get-systematic-in-2024 (2024 update; confirms no rule changes across all three plans)
- https://jasonkelly.substack.com/p/managing-cash-contributions (cash contribution mechanics, identical across 3 Sig, 6 Sig, and 9 Sig)
- https://turboscribe.ai/transcript/2017612633175703830/the-30-down-rule (Jason Kelly video transcript; 6 Sig uses MVV, 2 sell signals ignored, resets to 60/40 after 30 Down)
- https://bestfolio.app/blog/kelly-signal-danger-v2 (independent corrected backtest; 6 Sig CAGR 11.7%, max DD -78.3%, Sharpe 0.23; identifies failure modes)
- https://www.reddit.com/r/TQQQ/comments/1i0ens0/can_anyone_explain_9sig_strategy_in_the_words_for/ (Reddit thread; signal math explained: target = 3% × leverage multiplier; confirms family structure)
- https://www.reddit.com/r/TQQQ/comments/1i2g5lz/can_someone_explain_the_9sig_strategy_like_im_5/ (Reddit thread; community discussion of target selection, bond alternatives, and dry powder concept)
<!-- END RESEARCH SOURCES -->

---

## Overview

The 6% Signal (6 Sig) is the middle tier of Jason Kelly's Signal plan family. It applies the same quarterly value-averaging mechanics as 3 Sig but uses a 2x leveraged midcap ETF as the stock position and targets 6% quarterly growth instead of 3%.

The three Signal plans form a family based on leverage multiplier. The quarterly target is always 3% times the fund's leverage ratio: 3% × 1 = 3% for 3 Sig (unleveraged), 3% × 2 = 6% for 6 Sig (2x), and 3% × 3 = 9% for 9 Sig (3x). The mechanics (signal line calculation, quarterly buy/sell execution, cash contribution routing, and the 30 Down Rule structure) are identical across all three plans. Only the fund, the target percentage, and the specific 30 Down parameters differ.

6 Sig occupies the middle ground in the family: more return potential than 3 Sig's unleveraged SPY or IJR, but with lower maximum drawdown and less bond buffer depletion risk than 9 Sig's 3x TQQQ. In practice, 2x leverage still produces substantially amplified losses during bear markets compared to 3 Sig.

**Stock fund:** MVV, the ProShares Ultra MidCap400 ETF, which delivers approximately 2x the daily return of the S&P MidCap 400 Index. The midcap index is used rather than large-cap because it exhibits higher volatility, creating larger buy-low and sell-high opportunities within the quarterly cycle. This follows the same logic as 3 Sig's selection of small-cap IJR: more price movement generates more useful signal events.

The 6 Sig plan is available through The Kelly Letter subscription; there is no standalone book covering it specifically. The *3% Signal* book explains the system's core mechanics, which apply directly to 6 Sig with the fund and target percentage substituted.

---

## Rules and Logic

**Starting allocation:**

| Asset | Fund | Weight |
|-------|------|--------|
| Stock fund | MVV (ProShares Ultra MidCap400, 2x) | 60% |
| Bond fund | BND, AGG, or similar | 40% |

The 60/40 base is the allocation to which the plan resets after the 30 Down phase ends. During normal operation, the actual ratio drifts continuously as the market moves; the plan targets a signal line dollar amount, not a fixed percentage.

**Signal line calculation:**

Each quarter, a target dollar balance is calculated:

> Signal line = (Previous quarter-end stock fund balance) × 1.06

When new cash contributions are added during the quarter:
> Signal line = (Previous quarter-end stock fund balance) × 1.06 + (Half of new quarterly contributions)

All new cash goes to the bond fund during the quarter. At rebalancing time, half of the new contributions is added to the signal line, deploying the new money partially into equities.

**Quarterly rebalancing:**

| Outcome | Action |
|---------|--------|
| Stock fund balance > signal line | Sell the surplus; proceeds go to bond fund |
| Stock fund balance < signal line | Buy the shortfall; funded from bond fund |
| Stock fund balance = signal line | No trade |

**30 Down Rule:**

The 30 Down Rule activates when MVV's quarterly closing price falls at least 30% below its quarterly closing price high within the rolling past two years. Only quarterly closing prices are monitored.

When active:
- The next **2 sell signals are ignored**
- Buy signals during the locked phase are followed as normal

After 2 sell signals have been ignored (within two years), the plan **resets to the 60/40 base allocation** and resumes normal operations. This is different from 3 Sig, which resumes without resetting. The reset prepares the plan for the next cycle with a fresh bond buffer.

Because MVV uses 2x leverage, it amplifies both the drawdown trigger and the recovery movement. The 30 Down Rule is more likely to activate for MVV than for SPY (3 Sig) due to this amplification.

---

## Performance Notes

The 6% quarterly signal projects to approximately 26.2% annually (1.06^4 − 1 ≈ 26.25%). This is the target rate of growth for the MVV position each quarter, funded from bonds when the market falls short. It is a performance target that must be met or made up, not a return delivered passively.

**Independent corrected backtest (BestFolio, 2024):**

| Metric | 6 Sig (MVV + AGG, real data) |
|--------|------------------------------|
| CAGR | 11.7% |
| Max drawdown | −78.3% |
| Sharpe ratio | 0.23 |

The BestFolio analysis used corrected implementation matching the actual plan rules. The −78.3% maximum drawdown is notable given that 6 Sig is sometimes positioned as a "moderate" option relative to 9 Sig. A drawdown of this depth requires roughly a 360% gain to recover to the prior peak.

**Comparison within the plan family:**

| Plan | Stock fund | CAGR | Max DD | Sharpe |
|------|-----------|------|--------|--------|
| 3 Sig | IJR + BND | 9.0% | −52.3% | 0.31 |
| 6 Sig | MVV + AGG | 11.7% | −78.3% | 0.23 |
| 9 Sig | TQQQ + AGG | 39.4% | −72.1% | 0.82 |

Source: BestFolio corrected backtest, real data only (no synthetic pre-ETF data). Note that 9 Sig's CAGR reflects the 2010–2026 window, which included an exceptionally favorable Nasdaq run.

**Closed-system risk:** Community simulators that show strong 6 Sig performance almost universally include regular monthly cash contributions. Without contributions, a multi-year bear market will exhaust the bond buffer. The BestFolio analysis found a maximum drawdown of −78.3% in real data. In a hypothetical extended scenario without new cash, the drawdown would be deeper.

---

## Risks and Caveats

**2x leverage amplifies all risks.** MVV delivers approximately twice the daily return of the MidCap 400. This means drawdowns are roughly doubled relative to the unleveraged index. The plan's stated maximum drawdown of −78.3% reflects this amplification. Recovering from a 78% loss requires a 355% gain.

**Volatility decay on the stock fund.** MVV resets its leverage ratio daily. In volatile, choppy markets where the midcap index moves up and down without a clear trend, the 2x reset produces a performance drag relative to the simple leveraged position the daily reset implies. Kelly's argument is that the quarterly buy-low/sell-high mechanics partially offset this decay by purchasing MVV after downward moves and selling after upward ones. Whether this offset is sufficient is not established with certainty.

**Bond buffer depletion.** In a sustained bear market lasting multiple quarters, the bond fund is repeatedly drawn down to fund MVV purchases. If the fund runs dry, the plan holds 100% MVV with no buffer remaining. The 40% starting bond allocation gives more initial buffer than 3 Sig's 20%, but the larger quarterly funding requirement (6% target on 2x leverage) depletes it faster when markets are down.

**Bond fund losses in rising rate environments.** AGG and similar bond ETFs lose value when interest rates rise. In 2022, this created simultaneous losses in both the stock fund and the bond fund, reducing the buffer at the same time equity purchases were being funded. This is the same structural vulnerability as 3 Sig and 9 Sig.

**The 30 Down reset creates a fresh exposure.** When the 30 Down phase ends and the plan resets to 60/40, the investor is re-entering a 60% MVV position at whatever price MVV is at after the recovery. If the recovery is partial and a second decline follows shortly after the reset, the plan re-enters a 30 Down phase quickly with a freshly rebuilt but not fully grown bond buffer.

**Tax drag in taxable accounts.** Quarterly sell signals in a taxable account generate capital gains. For a 2x leveraged fund with higher volatility, sell signals tend to involve larger dollar amounts than in 3 Sig. Tax-advantaged accounts are strongly preferred.

**The "moderate" label is misleading.** 6 Sig is presented as a middle option between 3 Sig and 9 Sig, which is accurate in terms of leverage multiplier. But a maximum drawdown of −78.3% is not moderate in absolute terms. Investors who choose 6 Sig as a "safer" leveraged alternative should understand they are still accepting a risk of near-total portfolio loss in extreme conditions.

---

## Resources

*The 3% Signal* (Jason Kelly, 2015, Plume/Penguin): the core book explaining the signal system mechanics. While written around 3 Sig, the mechanics apply directly to 6 Sig with MVV substituted as the stock fund and 6% as the quarterly target. ISBN: 978-0142180952.

The Kelly Letter (jasonkelly.com): Jason Kelly's subscriber newsletter. Contains official weekly plan status, signal line values, 30 Down Rule state, and all plan updates for 6 Sig.

Jason Kelly's strategy overview (jasonkelly.com/resources/strategies/): free public summary with fund selections for all three Signal plans.

BestFolio corrected backtest (bestfolio.app/blog/kelly-signal-danger-v2): independent analysis with corrected implementation for all three plans, including 6 Sig's drawdown profile and closed-system risk.
