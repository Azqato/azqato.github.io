# Holy Grail: Content Source

**Strategy:** The Holy Grail
**Rebalancing cadence:** Event-driven (rebalances when conditions change) with 5% drift corridor
**Primary ticker:** TQQQ
**Instruments used:** TQQQ, UVXY, TECL, SOXL, SQQQ, BSV
**Signal inputs:** TQQQ 200D SMA, TQQQ 20D SMA, 10D RSI on TQQQ and SOXL
**Source file for:** holy-grail.html

**⚠ Corrections for HTML port:**
- The current hero badge says "Rules-Based Allocation"; acceptable but should clarify it's event-driven, not periodic
- The current lead paragraph mentions TMF as an inverse-correlated asset. **TMF is not used in this strategy.** The instruments are UVXY, TECL, SOXL, SQQQ, and BSV. Remove TMF from the lead.
- The Composer JSON confirms this is a copy of the original ("The Holy Grail (Invest Copy)"). Attribution to the original creator is unknown from available sources.

<!-- RESEARCH SOURCES: internal reference only, do not port to HTML -->
- https://app.composer.trade/symphony/VPVpD1SoqR5ykVu4NdWS/factsheet?tab=backtest (Composer.trade factsheet for this symphony: requires authentication; factsheet performance data not retrieved; JSON pasted by user contains full decision tree)
- https://www.reddit.com/user/derecknielsen/comments/yorwm0/educating_you_on_how_my_algo_tqqq_for_the_long/ (TQQQ FTLT original post: structural basis; Holy Grail is a close variant of derecknielsen's approach with key modifications)
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2741701 (Michael Gayed & Charles Bilello, "Leverage for the Long Run": academic basis for SMA-gated leverage used by both TQQQ FTLT and the Holy Grail)
- https://www.cxoadvisory.com/volatility-effects/leveraging-the-u-s-stock-market-based-on-sma-rules/ (CXO Advisory review of the Gayed/Bilello paper; SMA-based leverage performance data)
- https://the7circles.uk/leverage-for-the-long-run/ (The7Circles analysis of Leverage for the Long Run; regime logic and drawdown comparison)
<!-- END RESEARCH SOURCES -->

---

## Overview

The Holy Grail is a rules-based algorithmic strategy that uses TQQQ's own 200-day simple moving average to detect bull and bear market regimes, then rotates among leveraged long ETFs, a volatility instrument, inverse ETFs, and short-term bonds depending on current conditions. The strategy rebalances event-driven (only when a condition changes) rather than on a fixed daily or weekly schedule.

The strategy is closely related to TQQQ For The Long Term (TQQQ FTLT) and shares its conceptual foundation: using the 200-day SMA to gate leverage exposure and 10-day RSI to identify mean reversion opportunities within each regime. Both draw from Michael Gayed's and Charles Bilello's 2015 paper *Leverage for the Long Run* (SSRN #2741701), which showed that applying leverage only when the S&P 500 is above its 200-day moving average (and moving to safety below it) produced improved Sharpe ratios and lower maximum drawdowns versus constant-leverage buy-and-hold over an 87-year backtest.

The Holy Grail's key differences from TQQQ FTLT:

1. **Primary regime signal uses TQQQ's own 200D SMA**, not SPY's. Because TQQQ is a 3x leveraged instrument that amplifies every Nasdaq-100 move, TQQQ's 200D SMA is crossed more frequently than SPY's. This makes regime detection faster but also more prone to whipsawing near the boundary.

2. **Bull regime is 80% TQQQ + 20% implicit cash**. TQQQ FTLT is 100% in bull mode. The 20% cash buffer is a structural feature that reduces bull-market drawdown slightly at the cost of some upside.

3. **Bear regime adds SOXL** (Direxion Daily Semiconductor Bull 3x) as a mean reversion signal. When the semiconductor sector is oversold on a 10-day RSI basis within a bear market, the strategy rotates into SOXL for the expected mean reversion bounce. This sector-specific layer is not present in TQQQ FTLT.

4. **Bear regime uses BSV** (Vanguard Short-Term Bond ETF) instead of TLT (20+ year Treasuries) as the defensive alternative to SQQQ. BSV has significantly less interest rate sensitivity than TLT and did not suffer the 2022 concurrent decline that made TLT an unreliable safe haven.

5. **Rebalancing is event-driven** with a 5% corridor threshold. The portfolio only rebalances when a condition flips (TQQQ crosses its 200D SMA, or an RSI threshold is crossed), plus a 5% allocation drift trigger. This produces fewer transactions than a daily-rebalancing approach.

The Composer symphony is titled "The Holy Grail (Invest Copy)" indicating this is a saved copy of a publicly shared original strategy. The original creator is unknown from the sources available; it appears to be a community evolution of the TQQQ FTLT framework.

---

## Rules and Logic

**Instruments:**

| Instrument | Ticker | Role in strategy |
|-----------|--------|-----------------|
| ProShares UltraPro QQQ | TQQQ | Primary long position (3x Nasdaq-100) |
| ProShares Ultra VIX Short-Term Futures | UVXY | Overbought hedge (1.5x short VIX futures) |
| Direxion Daily Technology Bull 3x | TECL | Mean reversion long in bear regime (3x tech) |
| Direxion Daily Semiconductor Bull 3x | SOXL | Semiconductor oversold mean reversion (3x semis) |
| ProShares UltraPro Short QQQ | SQQQ | Bear regime short (−3x Nasdaq-100) |
| Vanguard Short-Term Bond ETF | BSV | Defensive alternative to SQQQ in bear regime |

**Signal inputs (monitoring only, not traded directly):**

| Signal | Condition tested |
|--------|----------------|
| TQQQ vs. TQQQ 200D SMA | Primary macro regime detector: bull or bear |
| TQQQ vs. TQQQ 20D SMA | Short-term downtrend detector within bear regime |
| TQQQ 10D RSI | Overbought (> 79) and oversold (< 31) |
| SOXL 10D RSI | Semiconductor oversold (< 30) |

**Allocation:**

- Bull regime: 80% TQQQ or UVXY / 20% cash
- Bear regime: 100% in one instrument at a time

**Decision tree (evaluated on condition change + 5% drift):**

**Step 1, Primary regime: TQQQ vs. its 200D SMA**

| Condition | Regime |
|-----------|--------|
| TQQQ current price > TQQQ 200D SMA | BULL |
| TQQQ current price ≤ TQQQ 200D SMA | BEAR |

---

**BULL REGIME (80% allocation)**

| Condition | Action | Rationale |
|-----------|--------|-----------|
| TQQQ 10D RSI > 79 | 80% UVXY | TQQQ overbought; volatility spike likely; mean reversion trade |
| Neither condition met | 80% TQQQ | Default bull position; 20% cash held at all times |

---

**BEAR REGIME (100% allocation)**

| Condition | Action | Rationale |
|-----------|--------|-----------|
| TQQQ 10D RSI < 31 | 100% TECL | TQQQ oversold in bear; leveraged tech mean reversion |
| SOXL 10D RSI < 30 | 100% SOXL | Semiconductors oversold; sector mean reversion |
| TQQQ < TQQQ 20D SMA | Top of [SQQQ, BSV] by 10D RSI | Downtrend confirmed; hold best-momentum short/defensive |
| None of the above | 100% TQQQ | Transitional: TQQQ above 20D SMA within bear but no signal |

**SQQQ vs. BSV selection:** When TQQQ is below its 20D SMA in the bear regime, the strategy selects whichever of SQQQ or BSV has the higher 10-day RSI at that moment. BSV replaces the TLT used in TQQQ FTLT; its short-duration profile avoids the interest rate sensitivity that made TLT unreliable in 2022.

**Rebalancing mechanics:** The symphony's rebalance setting is "none," meaning no calendar-based rebalancing is scheduled. Rebalancing occurs only when: (a) a condition in the decision tree changes state, or (b) the portfolio drifts more than 5% from its target allocation. This contrasts with TQQQ FTLT's daily evaluation and results in fewer transactions in stable trending markets.

---

## Performance Notes

No public factsheet data was retrievable (Composer requires authentication). The following observations are drawn from the strategy's structural properties and the academic basis.

**Structural performance properties:**

The 20% cash buffer in the bull regime acts as a partial dampener on bull-market returns. In a strong TQQQ rally, the strategy captures only 80% of the gain (plus any UVXY trade when the overbought signal fires). In exchange, the cash buffer reduces the drawdown when the bull regime ends: at the point TQQQ crosses below its 200D SMA, 20% of the portfolio is already in cash and not exposed.

The SOXL mean reversion layer adds a sector-specific entry point not present in TQQQ FTLT. Semiconductor stocks are among the most volatile major sector constituents of the Nasdaq-100. When SOXL's 10D RSI drops below 30 within a bear market, the strategy treats this as an extreme short-term oversold condition and takes a 3x leveraged position in semiconductors to capture the expected mean reversion. This is a high-variance bet: SOXL can recover 15-30% in days after an extreme selloff, but it can also continue declining.

**Comparison to the TQQQ FTLT structural properties:**

| Feature | TQQQ FTLT | Holy Grail |
|---------|-----------|------------|
| Primary regime signal | SPY 200D SMA | TQQQ 200D SMA |
| Bull allocation | 100% TQQQ or UVXY | 80% TQQQ or UVXY + 20% cash |
| Bear mean reversion instruments | TECL, UPRO | TECL, SOXL |
| Bear defensive/short selection | SQQQ vs. TLT | SQQQ vs. BSV |
| Rebalancing | Daily | Event-driven + 5% corridor |
| Additional signals | SPXL RSI, SPY RSI | SOXL RSI |

**Academic basis: Leverage for the Long Run (Gayed & Bilello, 2015):**
The underlying regime-switching framework was validated over 87 years (October 1928 to October 2015):
- Above 200D SMA: +14.1% annualized return, 14.7% volatility
- Below 200D SMA: −2.3% annualized return, 26.5% volatility
- 2x leveraged LRS: Sharpe 0.51, max drawdown −78%
- Unleveraged SMA200 timing: Sharpe 0.60, max drawdown −50%
- Buy-and-hold S&P 500: Sharpe 0.30, max drawdown −86%
- The strategy outperformed buy-and-hold in 80% of rolling three-year periods

These figures are for the Gayed/Bilello LRS using S&P 500 + leverage/cash. The Holy Grail applies this regime logic to TQQQ (3x Nasdaq-100) with a significantly different instruments set, so direct performance comparison is not possible from the published paper.

---

## Risks and Caveats

**Using TQQQ's own 200D SMA as the regime signal creates faster but noisier switching.** Because TQQQ is 3x leveraged, it oscillates much more than the underlying Nasdaq-100 or SPY. TQQQ can cross its own 200D SMA multiple times during a period where SPY remains clearly above or below its 200D SMA. Each crossing triggers a full regime flip in the Holy Grail, generating a rotation and its associated transaction costs. In choppy markets, this produces repeated whipsaw rotations between TQQQ and bear-regime instruments.

**The 20% cash buffer in bull mode has a real cost.** Holding 20% cash while TQQQ is in a sustained bull phase means the strategy underperforms a fully-invested TQQQ position by approximately 20% of TQQQ's gain per period. In the 2020–2021 TQQQ run of several hundred percent, a 20% cash drag was a material cost. This is a deliberate design choice trading upside for downside protection; investors should understand it as a feature, not an accident.

**UVXY is an extreme-risk instrument.** The overbought-into-UVXY rotation (TQQQ RSI > 79 → buy UVXY) is a high-variance short-duration trade. UVXY tracks 1.5x short-term VIX futures, which have a structural decay from futures roll costs in normal markets. A correct signal captures a large volatility spike within days. An incorrect signal (TQQQ's RSI cools without a volatility spike) results in a rapid UVXY loss. The strategy holds UVXY only for the duration of the overbought condition, not as a long-term position.

**SOXL mean reversion carries amplified risk within a bear market.** Buying SOXL (3x semiconductors) when its 10D RSI drops below 30 within a period when TQQQ is already below its 200D SMA is a counter-trend trade using 3x leverage. If the semiconductor downturn is fundamental rather than technical (as it was during parts of 2022 and 2023), the mean reversion signal can generate large losses before any recovery materializes. SOXL has historically experienced drawdowns exceeding 90%.

**Event-driven rebalancing does not eliminate lag at regime changes.** Although the strategy rebalances whenever a condition changes, there is an inherent lag between the moment a regime change becomes meaningful and the moment the signal fires. TQQQ can fall significantly below its 200D SMA before the bull-to-bear transition is acted on. The 5% corridor threshold adds additional lag.

**SQQQ vs. BSV selection is momentum-based, not fundamentals-based.** In the bear regime's downtrend condition (TQQQ < 20D SMA), the strategy picks whichever of SQQQ or BSV has higher 10-day RSI. This is a relative momentum comparison between an inverse leveraged ETF and a defensive bond fund. The higher-RSI instrument may be the one that has been rallying for idiosyncratic reasons unrelated to which will continue to outperform. In some periods, both instruments lose value simultaneously (BSV in a rate-hike cycle, SQQQ during a bear market rally).

**All leveraged instruments carry daily reset decay.** TQQQ, TECL, SOXL, and SQQQ all use daily leverage reset. In volatile, mean-reverting markets, each of these instruments decays even when the underlying index is roughly flat. The strategy attempts to reduce this exposure by rotating out of positions based on momentum and regime signals, but does not eliminate daily decay from the individual instruments.

**No public performance record is available.** Unlike the Kelly Letter 9 Sig plan (which has a published multi-year live account) or HFEA (which has a published live tracking thread from 2019 onward), this strategy has no publicly verified live performance record in the sources reviewed. The backtest data on the Composer factsheet was not accessible without authentication.

---

## Resources

**Composer.trade symphony**: ID `VPVpD1SoqR5ykVu4NdWS`: The published implementation ("The Holy Grail (Invest Copy)"). Can be viewed and cloned on Composer.trade. The Composer platform handles daily condition evaluation and event-driven execution.

**TQQQ For The Long Term**: u/derecknielsen (Reddit, October 2022): The structural predecessor strategy that introduced the SPY 200D SMA + 10D RSI framework on which the Holy Grail is a variant. See `strategies/tqqq-ftlt.md` for the full TQQQ FTLT documentation.

**"Leverage for the Long Run"**: Michael Gayed & Charles Bilello (2015, SSRN #2741701): The academic paper providing the theoretical basis for 200D SMA-gated leverage. Documents the Leverage Rotation Strategy's 87-year backtest and shows why above-SMA environments are systematically better for leveraged exposure than below-SMA environments.

**CXO Advisory analysis** (cxoadvisory.com): Independent review of the Gayed/Bilello paper with performance metrics and critical notes on backtest friction assumptions.
