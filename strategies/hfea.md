# HFEA — Content Source

**Strategy:** Hedgefundie's Excellent Adventure (HFEA)
**Rebalancing cadence:** Quarterly
**Tickers:** UPRO, TMF
**Allocation:** 55% UPRO / 45% TMF (current); originally 40% UPRO / 60% TMF
**Source file for:** hfea.html

<!-- RESEARCH SOURCES — internal reference only, do not port to HTML -->
- https://hfea.neocities.org/ (community tracker and variant documentation)
- https://www.bogleheads.org/forum/viewtopic.php?f=10&t=272007 (Thread 1, Feb 2019 — original proposal by Hedgefundie, 40/60 allocation, full theoretical basis, backtest data)
- https://www.bogleheads.org/forum/viewtopic.php?f=10&t=288192 (Thread 2, Aug 2019 — revised to 55/45, continued live tracking)
- https://www.optimizedportfolio.com/hedgefundie-adventure/ (performance tracking, variant analysis, 2022 drawdown documentation)
- https://the7circles.uk/hedgefundies-excellent-adventure/ (independent analysis and UK-perspective writeup)
- https://app.composer.trade/symphony/Cjb5ysKtJsPv6Tm3Fk0R/factsheet?tab=structure (Composer.trade symphony: "HFEA The Resurrection" by u/derecknielsen — regime-adaptive variant using SPY 200D SMA + TLT 400D SMA to switch between TMF and TMV; quarterly rebalancing)
<!-- END RESEARCH SOURCES -->

---

## Overview

Hedgefundie's Excellent Adventure is a leveraged risk parity portfolio proposed by a Bogleheads forum user known as "Hedgefundie" in February 2019. The strategy pairs a 3x leveraged S&P 500 ETF (UPRO) with a 3x leveraged long-duration Treasury ETF (TMF), rebalanced quarterly to a fixed target allocation.

The theoretical foundation is risk parity. Rather than allocating dollars equally, risk parity allocates risk equally by balancing each position's contribution to total portfolio volatility. Hedgefundie calculated that the long-run annual volatility of the S&P 500 is approximately 15% and of long-term Treasuries approximately 10%. Simple arithmetic gives risk parity at 40% stocks and 60% bonds. A 40/60 unleveraged portfolio delivers conservative returns, so leverage is added to bring the risk back up to S&P 500 levels while preserving the diversification benefit. The result, historically, is a higher Sharpe ratio than the S&P 500 alone.

Stocks and long-duration Treasuries have maintained a correlation of approximately zero over the long run, with a meaningfully negative correlation during large single-day equity declines. Hedgefundie's data showed that when the S&P drops 2% or more in a day, there is a 75% chance long-term Treasuries will rise. When the S&P drops 4% or more, the median long-term Treasury return for that day is positive 1 to 3%.

**Thread 1 (February 2019):** Original allocation of 40% UPRO / 60% TMF, based on the risk parity volatility calculation. Starting position: $100,000, representing 15% of Hedgefundie's investable assets.

**Thread 2 (August 2019):** Allocation revised to 55% UPRO / 45% TMF. The shift reflected the view that stocks are the primary return driver and bonds serve as crash insurance, and that the original 60% TMF position was larger than necessary to achieve the hedge. The revision was made mid-strategy as the position had grown to approximately $143,000.

A precedent for this type of portfolio existed before the Bogleheads thread: PIMCO's StocksPLUS Long Duration Fund (PSLDX), launched September 2007, holds effectively 100% S&P 500 futures plus 100% long bonds, achieving a similar leveraged risk parity exposure without daily resetting ETFs. PSLDX has a 5-star Morningstar rating and is available in some 401k plans.

Hedgefundie explicitly framed this as a high-risk satellite position for young investors, to be used with only a small portion of total net worth. His goal was to grow $100,000 to $10,000,000 over 20 to 25 years, at which point he planned to exit into unleveraged Treasuries.

---

## Rules and Logic

**Allocation (current standard):**

| Asset | Ticker | Weight |
|-------|--------|--------|
| ProShares UltraPro S&P 500 (3x S&P 500) | UPRO | 55% |
| Direxion Daily 20+ Year Treasury Bull 3X | TMF | 45% |

**Allocation (original Thread 1):**

| Asset | Ticker | Weight | Basis |
|-------|--------|--------|-------|
| UPRO | UPRO | 40% | Risk parity: S&P 500 vol ~15% |
| TMF | TMF | 60% | Risk parity: LTT vol ~10% |

**Cost of leverage (as of 2018):**

| ETF | Expense Ratio | Borrow Rate (swap cost) | Total |
|-----|--------------|------------------------|-------|
| UPRO | 0.92% | 2.87% | ~3.79% |
| TMF | 1.09% | 1.83% | ~2.92% |

Borrowing costs are paid to swap counterparties (major investment banks) above the short-term treasury rate. These costs reduce the effective leverage return and are embedded in the fund's daily performance; they are not charged separately.

**Rebalancing:** Quarterly, calendar-based. No signal, no threshold. At the end of each quarter the portfolio is reset to the target weights. Hedgefundie chose quarterly rebalancing because it produced the best results in the backtest and he had no better justification for any other frequency.

**Account type:** Strongly preferred in a tax-advantaged account (Roth IRA, Traditional IRA, 401k). Quarterly rebalancing in a taxable account generates short-term capital gains on every trim. M1 Finance was commonly used for automatic rebalancing via new deposit allocation without triggering sales.

**Variants documented in the community:**

| Variant | Allocation | Notes |
|---------|-----------|-------|
| Original (Thread 1) | 40% UPRO / 60% TMF | Risk parity volatility calculation |
| Standard (Thread 2) | 55% UPRO / 45% TMF | Most referenced version |
| Tax-efficient | 43% UPRO / 57% EDV | Replaces 3x TMF with unleveraged long-duration bond ETF |
| Monthly rebalancing | 55% UPRO / 45% TMF | Same weights, higher frequency |
| Threshold-based | 55% UPRO / 45% TMF | Rebalances only when either position drifts beyond a defined band |

**Regime-adaptive variant — "HFEA The Resurrection" (Composer, u/derecknielsen):**

A Composer.trade implementation that adds a two-factor regime-switching model on top of the static HFEA allocation. It rebalances quarterly and uses two moving average signals to detect the macro environment: SPY vs. its 200-day SMA for the equity trend, and TLT vs. its 400-day SMA for the interest rate environment.

| Equity trend | Bond trend | Allocation | Scenario label |
|-------------|------------|-----------|----------------|
| SPY > 200D SMA | TLT > 400D SMA | 55% UPRO / 45% TMF | Bull market, normal inflation |
| SPY > 200D SMA | TLT < 400D SMA | 55% UPRO / 45% TMV | Bull market, high inflation |
| SPY < 200D SMA | TLT > 400D SMA | 55% UPRO / 45% TMF | Bear market, normal inflation |
| SPY < 200D SMA | TLT < 400D SMA | 20% UPRO / 80% TMV | Bear market, high inflation |

TMV (Direxion Daily 20+ Year Treasury Bear 3x Shares) replaces TMF when TLT is below its 400-day SMA, converting the long-bond position to a short-bond position. The 400-day TLT lookback is intentionally longer than the standard 200-day to avoid false triggers from temporary bond dips within a sustained rising-rate trend. In the high-inflation bear scenario, UPRO is reduced to 20% with 80% TMV — a defensive positioning that would have substantially reduced the 2022 drawdown.

Composer symphony ID: `Cjb5ysKtJsPv6Tm3Fk0R`

---

## Performance Notes

UPRO launched June 2009; TMF launched April 2009. All backtests before those dates use a simulation formula applied to S&P 500 and long Treasury daily returns, accounting for daily leverage reset, borrowing costs (1-month LIBOR), and expense ratios. The formula, contributed by forum member EfficientInvestor, is:

> (Daily % of underlying total return index) × X − ER/250 − (X − 1) × (1-month LIBOR) × (days elapsed / 360)

Where X is the leverage multiplier.

**Backtest 1987 to 2018 (40/60 UPRO/TMF, quarterly rebalancing):**

- CAGR: approximately 23.75% (Hedgefundie's model) to approximately 19% (more conservative estimate from forum member vineviz accounting for additional volatility drag)
- The wide range reflects methodological differences in modeling swap costs and daily volatility decay
- Significantly outperformed the S&P 500 in total return over this period
- Drawdowns were smaller than the S&P 500 in most historical periods within this window

**The "lost decade" validation (January 2000 to September 2011):**
- S&P 500 total return: approximately 0% over the period
- HFEA (simulated): approximately 11% CAGR over the same period
- This is the strategy's strongest theoretical argument: the risk parity structure preserved and grew capital during a period when a pure equity position went nowhere for over a decade

**Monte Carlo simulation (forum member pezblanco):**
- Several thousand runs of 20-year periods drawn from 1985-2018 data
- The distribution of 20-year CAGRs for HFEA showed a significantly wider right tail than the S&P 500
- Rerun from 1968 data (including the 1970s) showed the right tail of returns still extended into the 20 to 30% CAGR range, though with a wider range of outcomes

**Live tracking (October 2019 to April 2025):**

| Date | Approximate total return from inception |
|------|-----------------------------------------|
| May 2019 | +15% (Thread 1, from $100k to $115k) |
| August 2019 | +33% (from $100k to $133k) |
| Mid-August 2019 | +43% (at time of allocation change to 55/45) |
| July 2021 | +105% |
| January 2022 | +150% (peak) |
| July 2022 | +14% |
| October 2022 | -14% |
| January 2023 | -10% |
| April 2025 | +37% |

The January to October 2022 drawdown was approximately 65% from peak. By April 2025, the strategy had not recovered to its January 2022 high after more than three years.

---

## Risks and Caveats

**Correlation breakdown is the primary risk, and it materialized in 2022.** Hedgefundie stated in the original February 2019 post: "The main risk is that the S&P 500 and long Treasuries crash together in the same short period of time. In the past 30 years this has not happened, and I can't think of a real-world scenario in which this would happen." The Federal Reserve's 2022 rate hiking cycle proved this scenario does occur. Aggressive rate increases compressed equity valuations while simultaneously pushing long Treasury prices sharply lower. Both UPRO and TMF fell together for an extended period with no offsetting hedge.

**The pre-1982 data gap.** Most backtests begin in 1987 or later, after the Volcker-era rate normalization had concluded. The 1970s stagflation period, during which both stocks and long bonds delivered poor real returns simultaneously for years at a time, is absent from the primary backtest window. The 1968-2018 simulation showed more modest but still positive outcomes; however, the quality of pre-1987 simulated data for a 3x leveraged instrument is lower.

**Both instruments are 3x leveraged.** Unlike a conventional 60/40 allocation where bonds are a lower-volatility stabilizer, here the bond position amplifies losses at 3x. A significant rise in long-term interest rates does not produce a modest bond decline -- it produces a large TMF loss, compounded by volatility decay from the daily reset.

**Long-duration Treasury sensitivity.** TMF tracks the ICE U.S. Treasury 20+ Year Bond Index. Long-duration bonds are among the most interest-rate-sensitive instruments available. A 1% sustained increase in long-term rates produces a proportionally large price decline in 20+ year bonds, then tripled.

**Volatility decay on both sides.** Each fund independently undergoes daily compounding. In volatile sideways markets, both positions decay without the correlation benefit that manifests in trending markets. The daily reset works in the investor's favor during sustained trends but against them during choppy, mean-reverting periods.

**Backtest optimism.** The 23.75% CAGR figure from Hedgefundie's original model has been independently estimated as closer to 19% when swap costs and daily drag are more conservatively modeled. Both figures are from simulated data for most of the period. Live results since 2019 have substantially underperformed the backtest range.

**Tax drag in taxable accounts.** Quarterly rebalancing in a taxable account generates short-term capital gains every time a winning position is trimmed. Over a decade of quarterly rebalancing, this meaningfully erodes after-tax compounding.

**Not for large portfolio allocations.** Hedgefundie invested $100,000, representing 15% of his investable assets at the time, and stated explicitly that losing this amount would not materially change the course of his retirement savings. The strategy is not suited to a majority or core portfolio position.

---

## Resources

Hedgefundie's Excellent Adventure originated in two Bogleheads forum threads in 2019, both authored by the user "Hedgefundie":

- **Thread 1 (February 2019):** Introduced the 40/60 UPRO/TMF strategy, the risk parity theoretical basis, and the 1987-2018 backtest
- **Thread 2 (August 2019):** Revised the allocation to 55/45, continued the live tracking

Backtesting was conducted using Portfolio Visualizer (portfoliovisualizer.com) with the simulated pre-2009 dataset contributed by forum member EfficientInvestor.

PIMCO StocksPLUS Long Duration (PSLDX) is a related unleveraged-ETF analogue that has operated since September 2007 with a similar risk parity structure using futures and active bond management.

The hfea.neocities.org community site documents live performance tracking, variants, and community discussion beyond the original threads.
