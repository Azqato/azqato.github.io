# 9 Sig — Content Source

**Strategy:** The 9% Signal (9 Sig)
**Rebalancing cadence:** Quarterly
**Tickers:** TQQQ (ProShares UltraPro QQQ, 3x Nasdaq-100), plus bond fund (AGG, or alternatives such as SGOV, USFR, SPAXX)
**Allocation:** 60% TQQQ / 40% bonds (base, also reset target after 30 Down phase)
**Source file for:** 9sig.html

<!-- RESEARCH SOURCES — internal reference only, do not port to HTML -->
- https://jasonkelly.com/resources/strategies/ (official plan family overview; 9 Sig fund confirmed as TQQQ + AGG, 60/40 base)
- https://jasonkelly.com/2017/01/how-my-signal-system-works/ (core signal mechanics; applies to all three plans)
- https://jasonkelly.com/2017/02/how-to-use-leveraged-etfs/ (Kelly's rationale for using 3x leverage in 9 Sig)
- https://jasonkelly.com/2023/02/tqqq-and-volatility-decay/ (Kelly's argument that quarterly rebalancing offsets TQQQ volatility decay)
- https://jasonkelly.substack.com/p/get-systematic-in-2024 (2024 update; no rule changes; confirms three plans unchanged)
- https://jasonkelly.substack.com/p/managing-cash-contributions (cash contribution mechanics; identical across 3 Sig, 6 Sig, and 9 Sig)
- https://turboscribe.ai/transcript/2017612633175703830/the-30-down-rule (Jason Kelly video transcript; 9 Sig uses TQQQ, 2 sell signals ignored, resets to 60/40 after 30 Down; historical activations in 2020 and 2022)
- https://bestfolio.app/blog/kelly-signal-danger-v2 (independent corrected backtest; 9 Sig CAGR 39.4%, max DD -72.1%, Sharpe 0.82 on real data; -99.73% in closed-system dot-com simulation; five corrected implementation errors documented)
- https://www.reddit.com/r/TQQQ/comments/1i0ens0/can_anyone_explain_9sig_strategy_in_the_words_for/ (Reddit community explanation; confirms 60/40 start; Kelly Letter 9 Sig account went from $733k (Jan 2018) to $5.9m (Dec 2024); 2023: $1.5m → $4.1m with 99% TQQQ allocation all year; dot-com simulated recovery: 18-20 years without new cash; 2004-2024 CAGR ~25%)
- https://www.reddit.com/r/TQQQ/comments/1i2g5lz/can_someone_explain_the_9sig_strategy_like_im_5/ (Reddit thread; confirms 9% is derived from QQQ's ~12% annual historical return ≈ 3% quarterly × 3x leverage; bond alternatives discussed: BOXX, JAAA, SGOV, TBLL, USFR)
<!-- END RESEARCH SOURCES -->

---

## Overview

The 9% Signal (9 Sig) is the most aggressive tier of Jason Kelly's Signal plan family. It pairs TQQQ — the ProShares UltraPro QQQ 3x leveraged Nasdaq-100 ETF — with a bond fund and rebalances quarterly to a 9% quarterly growth target.

The plan belongs to a three-tier family based on leverage multiplier. The quarterly target scales with the fund's leverage ratio: 3% × 1x (unleveraged, 3 Sig), 3% × 2x (6 Sig), 3% × 3x (9 Sig). The 9% target derives from the Nasdaq-100's historical annual return of approximately 12–14%, which corresponds to roughly 3% per quarter. Applied to a 3x leveraged fund, the equivalent quarterly target is 9%.

The core mechanics — value averaging, signal line calculation, quarterly execution, and the 30 Down Rule — are the same across all three plans. The differences are the fund used, the quarterly target percentage, the 30 Down Rule's ignore count, and some additional safeguards unique to 9 Sig that manage the extreme volatility of 3x leverage.

The system is described as purely reactive: there are no forecasts, no market timing decisions, and no macroeconomic analysis. Each quarter, the investor compares the current TQQQ balance to a target balance that grows at 9% per quarter. If below target, buy. If above target, sell the excess. The bond fund serves as the reserve for purchases and the destination for profits.

Jason Kelly created 9 Sig as an extension of the 3 Sig system he introduced in his 2015 book *The 3% Signal*. The 9 Sig plan is managed through The Kelly Letter subscription service and is not covered in a standalone book. Kelly's own account following 9 Sig grew from approximately $733,000 in January 2018 to approximately $5.9 million by the end of December 2024.

---

## Rules and Logic

**Starting allocation:**

| Asset | Fund | Weight |
|-------|------|--------|
| Stock fund | TQQQ (ProShares UltraPro QQQ, 3x Nasdaq-100) | 60% |
| Bond fund | AGG (or cash equivalents: SGOV, USFR, SPAXX, BOXX) | 40% |

The 60/40 allocation is both the starting position and the allocation to which the plan resets after the 30 Down phase ends. During normal operation, the actual ratio drifts continuously — it has ranged historically as high as 99% TQQQ and as low as approximately 50% TQQQ depending on market conditions.

The official plan uses AGG (iShares Core U.S. Aggregate Bond ETF) as the bond fund. Community practitioners often substitute short-term Treasury ETFs (SGOV, TBLL), money market funds (SPAXX), or other stable instruments to avoid the interest rate sensitivity of intermediate-term bond funds.

**Signal line calculation:**

Each quarter, a target dollar balance for the TQQQ position is calculated:

> Signal line = (Previous quarter-end TQQQ balance) × 1.09

When new cash contributions are added during the quarter:
> Signal line = (Previous quarter-end TQQQ balance) × 1.09 + (Half of new quarterly contributions)

All new cash contributed during a quarter goes entirely to the bond fund. At rebalancing time, half of those contributions is added to the signal line target.

**Quarterly rebalancing:**

| Outcome | Action |
|---------|--------|
| TQQQ balance > signal line | Sell the surplus; proceeds go to bond fund |
| TQQQ balance < signal line | Buy the shortfall; funded from bond fund |
| TQQQ balance = signal line | No trade |

**Additional safeguards (9 Sig only):**

**90% Buying Power Throttle:** No single quarterly buy signal may use more than 90% of the current bond fund balance. This preserves a minimum reserve after large purchases and prevents a single extreme buy signal from exhausting the entire buffer.

**Spike Reset Trigger:** If all three of the following conditions are true simultaneously, the plan resets TQQQ to a 60% allocation:
1. TQQQ's quarterly gain was 100% or more
2. The TQQQ balance after the quarterly rebalance is between 60% and 100% of total portfolio
3. The plan is not currently in a 30 Down no-sell period

This rule books profits during extreme bull-market spikes and rebuilds the bond buffer while TQQQ is at an elevated price.

**30 Down Rule:**

The 30 Down Rule activates when TQQQ's quarterly closing price falls at least 30% below its quarterly closing price high within the rolling past two years. Only quarterly closing prices are monitored — intra-quarter prices do not trigger the rule.

When active:
- The next **2 sell signals are ignored**
- Buy signals during the locked phase are followed as normal

After 2 sell signals have been ignored (within two years), the plan **resets to the 60/40 base allocation** and resumes normal operations.

Historical 30 Down activations for 9 Sig:
- Spring 2020: COVID crash. Plan locked through the 2020–2021 recovery; TQQQ allocation ran as high as 99% while locked in. The 30 Down phase prevented the plan from selling during the ascent. The plan eventually signaled a rebalance reset near the recovery peak and then resumed normal operations.
- 2022: Federal Reserve rate hike cycle. TQQQ dropped sharply. Plan locked in. Bond fund was exhausted by mid-2022, leaving the plan in a state of 100% TQQQ with no buffer. The 30 Down rule prevented any sell signals during the subsequent recovery. The plan reset to 60/40 in January 2024 after the two ignored-sell threshold was reached.

---

## Performance Notes

The 9% quarterly signal projects to approximately 41.2% annually (1.09^4 − 1 ≈ 41.16%). This is the target growth rate for the TQQQ position each quarter, funded from bonds when the market falls short. It is a high target that TQQQ can and does exceed in strong bull quarters, triggering large sell signals that move profits into bonds.

**Kelly Letter official portfolio:**

| Period | Portfolio value | Notes |
|--------|----------------|-------|
| January 2018 | ~$733,000 | Start of tracked period |
| 2022 (low) | Not disclosed | Bond fund exhausted; 100% TQQQ during 2022 bear |
| January 2023 | ~$1,500,000 | Start of 2023 tracking period |
| December 2023 | ~$4,100,000 | +173% for the year; 99% TQQQ allocation all year |
| December 2024 | ~$5,900,000 | End of tracked period |

The 2023 result was driven by two factors: TQQQ's recovery from 2022 lows, and the 30 Down lock-in that kept the plan at 99% TQQQ allocation through the entire year rather than selling into the recovery.

**Independent corrected backtest (BestFolio, 2024, real data only):**

| Metric | 9 Sig (TQQQ + AGG, 2010–2026) |
|--------|-------------------------------|
| CAGR | 39.4% |
| Max drawdown | −72.1% |
| Sharpe ratio | 0.82 |

This window (2010–2026) is almost entirely within an exceptionally favorable period for the Nasdaq-100.

**Simulated dot-com bubble scenario (community backtesting, simulated TQQQ data pre-2009):**
- Without ongoing cash contributions, 9 Sig through the dot-com crash (2000–2002) would have taken approximately 18–20 years to recover to pre-crash levels
- The 2004–2024 period (avoiding the crash) simulated a CAGR of approximately 25%
- Note: simulated TQQQ data for this period uses a mathematical approximation formula and cannot be verified with the same confidence as actual fund returns

**Closed-system stress test (BestFolio bootstrap, extended synthetic history):**
- Testing 2,000 resampled 27-year histories of 9 Sig's actual returns:
  - Median outcome: −98% maximum drawdown with 7.7x terminal multiple
  - Worst 5%: effectively total loss
  - Best 5%: −82% drawdown with 3,665x terminal multiple
- The −99.73% closed-system drawdown in an extended synthetic dot-com scenario "is not a tail event — it is essentially the median" without ongoing contributions

**Plan family comparison (BestFolio corrected backtest):**

| Plan | Stock fund | CAGR | Max DD | Sharpe |
|------|-----------|------|--------|--------|
| 3 Sig | IJR + BND | 9.0% | −52.3% | 0.31 |
| 6 Sig | MVV + AGG | 11.7% | −78.3% | 0.23 |
| 9 Sig | TQQQ + AGG | 39.4% | −72.1% | 0.82 |

9 Sig's Sharpe ratio is higher than 6 Sig's despite its deeper leverage because TQQQ's risk-adjusted returns in the test window (post-2010) were exceptional. This changes substantially in extended simulated histories.

---

## Risks and Caveats

**The plan is not viable as a closed system without ongoing contributions.** The most important structural risk of 9 Sig is that the strategy is designed for investors who continuously add new cash. Regular contributions refill the bond buffer after bear market draw-downs, raise the signal line, and sustain the buy-low mechanic. Without contributions, a severe and extended bear market exhausts the bond fund. At that point the plan holds 100% TQQQ at a depressed price with nothing left to buy further dips. The dot-com simulation shows this can result in 18–20 years to break even. Any investor with a fixed lump-sum and no future contributions should understand this risk clearly before starting 9 Sig.

**3x leverage amplifies losses at a non-linear rate.** TQQQ resets its 3x leverage ratio daily. A 50% decline in the Nasdaq-100 does not produce a 150% loss in TQQQ — it produces a near-total wipeout due to daily compounding of amplified moves. In the 2022 bear market, TQQQ declined approximately 77% from its peak. Recovering a 77% loss requires a 335% gain in the fund.

**Bond buffer depletion.** In 2022, the 9 Sig plan exhausted its bond buffer mid-year. With no bonds remaining, every subsequent buy signal went unfunded. The plan held 100% TQQQ through the rest of 2022 and into 2023, with no ability to buy at the lows and no buffer against continued decline. This is the plan's most dangerous state, and it occurred in a real live account within a few years of the plan's public documentation.

**Bond fund losses in rising rate environments.** AGG lost value in 2022 due to the rate hiking cycle, simultaneously with TQQQ's decline. The buffer was being depleted by equity purchases at the same time the bond fund's value was shrinking from interest rate pressure. Community members have migrated to short-term Treasury ETFs (SGOV, TBLL) and money market funds for the bond sleeve precisely to avoid this correlation.

**TQQQ volatility decay.** TQQQ resets its leverage daily. In sideways, choppy markets, the mathematical effect of daily compounding produces a performance drag against the theoretical 3x return of the unleveraged Nasdaq-100. Jason Kelly argues that quarterly rebalancing partially counteracts this: "when TQQQ goes up a little, we sell a little; when it goes up a lot, we sell a lot." However, the offset is partial, not complete, and in extended sideways periods the decay accumulates.

**The 9% target does not adapt to market conditions.** The signal line grows at 9% per quarter regardless of whether the Nasdaq-100 is trading at 40x earnings or 15x earnings. In sustained bear markets, the plan keeps buying regardless of valuation. There is no intrinsic mechanism to recognize that recovery may be delayed and to adjust accordingly.

**Sequence of returns risk at entry.** Entering 9 Sig near a market peak with a large lump sum and immediately encountering a multi-year bear market is the worst-case scenario. The starting 60% TQQQ allocation sustains a large leveraged loss, the bond buffer is spent buying falling TQQQ shares for several quarters, and the recovery requires both TQQQ to return to prior levels and the portfolio to compound back from a deeply depleted state. New investors are sometimes advised to consider a scaled-in entry rather than immediate full deployment.

**Tax drag in taxable accounts.** Quarterly sell signals on TQQQ in a taxable account generate short-term capital gains at ordinary income rates (if held less than a year, which most TQQQ gains are after quarterly rebalancing). Over years of operation with substantial sell signals, this is a significant cost. Tax-advantaged accounts are strongly preferred for 9 Sig.

---

## Resources

*The 3% Signal* (Jason Kelly, 2015, Plume/Penguin) — covers the core signal mechanics in detail via the unleveraged 3 Sig plan; these apply directly to 9 Sig with TQQQ and the 9% target substituted. ISBN: 978-0142180952.

The Kelly Letter (jasonkelly.com) — Jason Kelly's subscriber newsletter. Contains the official weekly plan status, current TQQQ signal line value, 30 Down Rule state, and all plan rules including the Spike Reset and 90% throttle that are not publicly documented elsewhere.

Jason Kelly's strategy overview (jasonkelly.com/resources/strategies/) — free public summary of all three plans.

BestFolio corrected backtest (bestfolio.app/blog/kelly-signal-danger-v2) — independent analysis with corrected implementation across all three plans; includes 9 Sig's closed-system stress test and the five simulation errors present in prior community tools.
