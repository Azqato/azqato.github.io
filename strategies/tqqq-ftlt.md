# TQQQ For The Long Term — Content Source

**Strategy:** TQQQ For The Long Term (TQQQ FTLT)
**Rebalancing cadence:** Daily (rules-based algorithmic, not buy-and-hold)
**Primary ticker:** TQQQ
**Instruments used:** TQQQ, UVXY, TECL, UPRO, SQQQ, TLT
**Signal inputs:** SPY 200D SMA, TQQQ 20D SMA, 10D RSI on TQQQ / SPXL / SPY / SQQQ
**Source file for:** tqqq-ftlt.html

**⚠ Note for HTML port:** The current tqqq-ftlt.html hero badge and lead paragraph describe this as a "buy and hold" strategy. Based on research, this is inaccurate. The strategy is rules-based with daily rebalancing and multiple instruments. The hero badge should be updated to "Rules-Based / Daily" and the lead paragraph revised when porting this content.

<!-- RESEARCH SOURCES — internal reference only, do not port to HTML -->
- https://www.reddit.com/user/derecknielsen/comments/yorwm0/educating_you_on_how_my_algo_tqqq_for_the_long/ (original strategy post by u/derecknielsen; full decision tree explanation, performance claims, design rationale, community evolution)
- https://app.composer.trade/symphony/ovM8FTJXYZX1uFmh0vRI/factsheet (Composer.trade factsheet — the canonical published symphony; JSON contains the exact decision tree logic)
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2741701 (Michael Gayed & Charles Bilello, "Leverage for the Long Run," 2015 — the academic basis for SMA-gated leverage; 403 Forbidden when fetched, content obtained from secondary sources)
- https://www.cxoadvisory.com/volatility-effects/leveraging-the-u-s-stock-market-based-on-sma-rules/ (CXO Advisory review of the Gayed/Bilello paper; performance data Oct 1928–Oct 2015; critical notes on backtest assumptions)
- https://the7circles.uk/leverage-for-the-long-run/ (The7Circles analysis of the LRS; regime logic, drawdown comparison, risk analysis)
- https://proactiveadvisormagazine.com/moving-averages-leverage-long-run/ (Proactive Advisor Magazine summary of SMA + leverage approach)
<!-- END RESEARCH SOURCES -->

---

## Overview

TQQQ For The Long Term (TQQQ FTLT) is a rules-based algorithmic strategy created by Reddit user u/derecknielsen and published in October 2022. Despite its name suggesting a passive buy-and-hold approach, the strategy is an active, daily-rebalancing algorithm that uses a cascading set of conditions to rotate between leveraged long positions, a volatility ETF, leveraged short positions, and long-duration Treasuries depending on the prevailing market regime.

The strategy was designed to address a problem the author encountered firsthand: discovering TQQQ in October 2021, just before a 70%+ drawdown over the following 12 months. The stated goal was to build something that could profit in both bull and bear markets, rather than accepting the full drawdown of simply holding TQQQ through a prolonged decline.

The strategy operates on two primary ideas:

**1. Momentum switching via the 200-day SMA.** The 200-day simple moving average of SPY is used as a macro regime detector. When SPY is above its 200D SMA, the market is in a low-volatility trending environment and the strategy takes leveraged long positions. When SPY is below its 200D SMA, the market is in a high-volatility regime and the strategy switches to bearish or defensive instruments.

**2. Mean reversion via 10-day RSI.** Within each regime, the 10-day RSI is used to identify when individual ETFs are overbought or oversold and take the opposite-direction position, anticipating a reversion toward the mean.

This design is directly inspired by Michael Gayed's and Charles Bilello's 2015 academic paper, *Leverage for the Long Run* (SSRN #2741701), which demonstrated that applying leverage only when the S&P 500 is above its 200-day moving average — and exiting to cash or Treasuries below it — produced a superior Sharpe ratio, reduced maximum drawdown, and higher terminal wealth than constant-leverage buy-and-hold over an 87-year backtest (October 1928 to October 2015).

u/derecknielsen published the strategy on Composer.trade, a platform for building and running algorithmic trading symphonies. The post attracted extensive community engagement: at least 10 community variants were created and over 900 comments generated in the Composer Discord alone.

By October 2022 — approximately four months after the author began running the strategy live — it was up approximately 150% cumulative from the June 2022 start date, a period during which TQQQ itself was experiencing a major bear market bottom.

---

## Rules and Logic

The strategy is a daily-rebalancing decision tree. All conditions are checked every trading day. The portfolio holds one instrument at a time (100% allocation, minus a 5% cash buffer maintained by the Composer symphony wrapper).

**Instruments:**

| Instrument | Ticker | Role in strategy |
|-----------|--------|----------------|
| ProShares UltraPro QQQ | TQQQ | Primary long position (3x Nasdaq-100) |
| ProShares Ultra VIX Short-Term Futures | UVXY | Overbought hedge (1.5x short VIX futures) |
| Direxion Daily Technology Bull 3x | TECL | Mean reversion long in bear regime (3x tech) |
| ProShares UltraPro S&P 500 | UPRO | Mean reversion long in bear regime (3x S&P 500) |
| ProShares UltraPro Short QQQ | SQQQ | Bear regime short (−3x Nasdaq-100) |
| iShares 20+ Year Treasury Bond ETF | TLT | Defensive alternative to SQQQ in bear regime |

**Signal inputs (monitoring only, not traded directly):**

| Signal | Purpose |
|--------|---------|
| SPY vs. SPY 200D SMA | Primary macro regime detector: bull or bear |
| TQQQ vs. TQQQ 20D SMA | Short-term bear trend detector within the bear regime |
| TQQQ 10D RSI | Overbought (>79) and oversold (<31) detection |
| SPXL 10D RSI | Secondary overbought detection (>80) |
| SPY 10D RSI | S&P 500 oversold detection (<30) |
| SQQQ 10D RSI | Inverse ETF oversold detection (<31) |

**Decision tree (evaluated daily):**

**Step 1 — Macro regime: SPY vs. its 200D SMA**

| Condition | Go to |
|-----------|-------|
| SPY current price > SPY 200D SMA | BULL REGIME |
| SPY current price ≤ SPY 200D SMA | BEAR REGIME |

---

**BULL REGIME**

| Condition | Action | Rationale |
|-----------|--------|-----------|
| TQQQ 10D RSI > 79 | Buy UVXY | TQQQ overbought; volatility spike expected; mean reversion play |
| SPXL 10D RSI > 80 | Buy UVXY | S&P 500 3x also overbought; confirms overextension |
| Neither condition met | Buy TQQQ | Default bull-market position |

---

**BEAR REGIME**

| Condition | Action | Rationale |
|-----------|--------|-----------|
| TQQQ 10D RSI < 31 | Buy TECL | TQQQ oversold in bear; mean reversion long on leveraged tech |
| SPY 10D RSI < 30 | Buy UPRO | S&P oversold; mean reversion long on 3x S&P 500 |
| TQQQ < its 20D SMA | Select: top of [SQQQ, TLT] by 10D RSI | Downtrend confirmed; hold best-performing defensive/short |
| TQQQ ≥ 20D SMA AND SQQQ 10D RSI < 31 | Buy SQQQ | Inverse ETF pulled back; re-enter short at better price |
| None of the above | Buy TQQQ | Transitional: bear macro but TQQQ in short-term recovery |

**SQQQ vs. TLT selection logic:** When TQQQ is below its 20D SMA in a bear regime, the strategy selects whichever of SQQQ or TLT has the higher 10-day RSI. This prevents holding SQQQ after a prolonged short-side rally when TLT may offer a better risk-adjusted continuation position.

**UVXY note:** The author flags UVXY as extremely risky. It tracks 1.5x short-term VIX futures and can decline 20-30% in a single day when volatility drops. The overbought-into-UVXY trade is described as "a somewhat rare event but when it happens, the profits can be very generous."

---

## Performance Notes

The strategy's performance claims come primarily from the original author's backtest and the community extension into historical data.

**10-year backtest (October 2012 to October 2022):**

| Metric | TQQQ FTLT | TQQQ buy-and-hold |
|--------|-----------|-------------------|
| Cumulative return | +298% | +35% |
| Relative performance | 8.5× faster growth | baseline |
| Approximate max drawdown | ~half of TQQQ | ~80%+ (2022) |

The backtest window ended at October 2022, near the trough of the 2022 TQQQ drawdown of approximately 77%. TQQQ's 10-year buy-and-hold result of +35% reflects starting in October 2012 and ending at the 2022 bear market low — a period that would show a dramatically higher return if the end date were different. The +298% for FTLT reflects the bear market protection providing relative outperformance during the drawdown.

**Extended backtest (1970s to present, community run):**
A community member stripped the strategy to bare essentials to enable backtesting to the 1970s. Results showed the strategy can perform well in periods of stagflation, high inflation, and Federal Reserve quantitative tightening — the same macro environment that made 2022 difficult for standard TQQQ holding.

**Live tracking from June to October 2022:**
The author reports approximately +150% cumulative return over the four-month period following the strategy's June 2022 launch, during a time when TQQQ was near its bear market bottom. This window coincided with extreme TQQQ volatility that the bear-side regime and mean reversion signals were designed to exploit.

**Academic basis — Leverage for the Long Run (Gayed & Bilello, 2015):**
The paper backtested the Leverage Rotation Strategy (LRS) from October 1928 to October 2015 (87 years):

| Strategy | Sharpe ratio | Max drawdown |
|----------|-------------|--------------|
| Buy-and-hold S&P 500 | 0.30 | −86% |
| Unleveraged 200D SMA timing | 0.60 | −50% |
| LRS with 2x leverage | 0.51 | −78% |

Key findings from the paper:
- Above the 200D SMA: +14.1% annualized return, 14.7% volatility
- Below the 200D SMA: −2.3% annualized return, 26.5% volatility
- The LRS outperformed buy-and-hold in 80% of rolling three-year periods
- A $10,000 investment in 1928 grew to approximately $39 billion with 3x LRS vs. $19 million with buy-and-hold over the same period (note: these figures assume zero additional friction costs and are not achievable in practice)
- Approximately 5 regime switches per year on average

CXO Advisory notes the paper's backtest assumptions understate real-world friction: leverage costs in earlier decades were substantially higher than the 1% annual fee assumed, and fund-level expenses are not included in early period returns.

---

## Risks and Caveats

**Daily rebalancing creates compounding transaction costs and tax events.** Unlike the quarterly-rebalancing Kelly Signal plans, TQQQ FTLT checks conditions every trading day. Any day a condition flips — SPY crosses its 200D SMA, or an RSI crosses a threshold — the portfolio rotates into a new instrument. In a taxable account, each rotation generates a capital gains event. In a volatile, choppy market near the 200D SMA, this can produce daily whipsaws with high transaction frequency.

**Choppy markets near the 200D SMA cause repeated false signals.** When SPY oscillates above and below its 200D SMA without establishing a clear trend, the strategy repeatedly switches between the bull regime (TQQQ) and the bear regime (SQQQ/TLT). Each switch incurs costs, and the whipsaw between long and short positions can produce losses in both directions.

**UVXY is one of the most volatile instruments available.** UVXY tracks 1.5x short-term VIX futures, which have a persistent structural headwind due to futures roll cost (VIX futures are almost always in contango, meaning longer-dated contracts cost more than near-dated ones). UVXY loses value in calm markets and during volatility mean reversion. The author explicitly warns it "can easily decline 20-30% in one day." The overbought-into-UVXY trade is high risk even when the RSI signal fires correctly.

**All instruments carry leveraged ETF daily reset risk.** The strategy holds 3x and 1.5x leveraged instruments almost exclusively. TQQQ, TECL, UPRO, and SQQQ all use daily reset leverage. In volatile, sideways markets, each instrument individually decays through volatility drag. The strategy attempts to reduce total decay by rotating out of positions when they are overbought or oversold, but does not eliminate leverage decay entirely.

**The 10-year backtest window was favorable.** The October 2012 to October 2022 window captures a 10-year period of extraordinary Nasdaq-100 performance including a historic bull run. TQQQ's own +35% return over that window ending at the bear market trough is deceptively low; at the 2021 peak, TQQQ's 10-year return was dramatically higher. A backtest that starts at any bear market low will show strong relative performance for a protection-oriented strategy.

**Bear regime instruments are not hedges.** SQQQ (−3x Nasdaq-100) is a directional short-selling instrument, not a hedge. If the bear regime signal fires but the market immediately reverses upward, SQQQ produces large leveraged losses against the recovery. The strategy relies on the 200D SMA correctly identifying sustained downtrends — which it does historically, but with lag at turning points.

**Community evolutions vary significantly.** The original author noted that at least 10 variations of the strategy were circulating in the Composer Discord within weeks of publication. Variations may differ in RSI thresholds, instrument substitutions, leverage levels, and regime definitions. Performance of any specific variant may differ materially from the original.

**Backtest survivorship and regime dependency.** The academic foundation (Gayed & Bilello) used October 1928 as its start date, beginning just before the Great Depression — a period where the 200D SMA's protective effect was extreme and favorable to the strategy's thesis. CXO Advisory notes this start date biases the results toward the SMA's best historical performance.

---

## Resources

**Original strategy post** — u/derecknielsen (Reddit, October 2022): The complete explanation of the strategy design, decision tree, performance claims, and community evolution history.

**Composer.trade symphony** — ID `ovM8FTJXYZX1uFmh0vRI`: The canonical published implementation. The symphony can be cloned and run on Composer.trade. The JSON contains the full decision tree; note that conditions and instruments have been modified by the community in subsequent versions.

**"Leverage for the Long Run"** — Michael Gayed & Charles Bilello (2015, SSRN #2741701): The academic paper providing the theoretical foundation for SMA-gated leverage. Documents the Leverage Rotation Strategy's 87-year backtest showing improved Sharpe ratios and reduced maximum drawdown versus constant-leverage buy-and-hold.

**CXO Advisory analysis** (cxoadvisory.com) — Independent review of the Gayed/Bilello paper with corrected performance metrics and critical notes on backtest friction assumptions.

**The7Circles analysis** (the7circles.uk/leverage-for-the-long-run/) — Extended discussion of the LRS regime logic, drawdown profiles, and volatility regime theory.
