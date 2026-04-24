---
layout: distill
title: "Quantitative Trading — Chapter 7 Study Notes"
description: Friendly notes on Chapter 7 of Quantitative Trading (2nd Ed.) — the big ideas in statistical arbitrage explained plainly, from mean reversion vs momentum to cointegration, factor models, seasonal trades, and high-frequency strategies.
tags: Finance Quant Trading Statistical Arbitrage Notes
giscus_comments: true
date: 2026-03-20
featured: true
thumbnail: https://m.media-amazon.com/images/I/51s4givoDeL._SY445_SX342_ML2_.jpg

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Section 1 — Mean Reversion vs. Momentum — Which Way Will the Price Go?
  - name: Section 2 — Regime Changes and Conditional Parameter Optimization
  - name: Section 3 — Stationarity and Cointegration — The Science of Pair Trading
  - name: Section 4 — Factor Models — What Actually Drives Stock Returns?
  - name: Section 5 — When Should You Exit a Trade?
  - name: Section 6 — Seasonal Trading Strategies
  - name: Section 7 — High-Frequency Trading
  - name: Section 8 — Low-Beta vs. High-Beta — Which Is the Better Portfolio?
  - name: Term Glossary

_styles: >
  .note-abstract {
    background: #f0f4ff;
    border-left: 4px solid #5b7de8;
    padding: 0.9rem 1.1rem;
    margin: 1rem 0 1.5rem 0;
    border-radius: 0 6px 6px 0;
    font-style: italic;
    color: #333;
  }
  .example-block {
    background: #f8f8f8;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    padding: 0.85rem 1.1rem;
    margin: 0.75rem 0;
  }
  .example-block .ex-title {
    font-weight: 600;
    font-size: 0.9rem;
    margin-bottom: 0.4rem;
    color: #1a1a2e;
  }
  .example-block .ex-pill {
    display: inline-block;
    font-size: 0.72rem;
    font-weight: 600;
    padding: 1px 8px;
    border-radius: 20px;
    margin-left: 6px;
    vertical-align: middle;
  }
  .pill-live   { background: #d4edda; color: #155724; }
  .pill-warn   { background: #fce8e6; color: #7f1d1d; }
  .pill-num    { background: #ede8fc; color: #3c2a8a; }
  .pill-code   { background: #e2f0fb; color: #0c4a7c; }
  .example-block .ex-lesson {
    margin-top: 0.5rem;
    font-size: 0.85rem;
    color: #555;
    border-top: 1px solid #ddd;
    padding-top: 0.4rem;
  }
  .key-idea {
    padding: 0.3rem 0;
    border-bottom: 1px dotted #ddd;
    margin-bottom: 0.4rem;
  }
  .key-idea:last-child { border-bottom: none; }
  .glossary-entry {
    border-bottom: 1px solid #eee;
    padding: 0.7rem 0;
  }
  .glossary-entry:last-child { border-bottom: none; }
  .glossary-entry .gterm {
    font-weight: 600;
    font-size: 0.95rem;
    margin-bottom: 0.25rem;
  }
  .glossary-entry .gcat {
    display: inline-block;
    font-size: 0.7rem;
    font-weight: 600;
    padding: 1px 7px;
    border-radius: 20px;
    margin-left: 6px;
    vertical-align: middle;
  }
  .cat-strategy { background: #d1fae5; color: #064e3b; }
  .cat-stats    { background: #dbeafe; color: #1e3a8a; }
  .cat-model    { background: #fef3c7; color: #78350f; }
  .cat-exit     { background: #fce7f3; color: #831843; }
  .cat-seasonal { background: #ede8fc; color: #3c2a8a; }
  .cat-hft      { background: #dcfce7; color: #14532d; }
  .quote-block {
    background: #f9fafb;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    margin-top: 1rem;
    font-style: italic;
    color: #444;
    font-size: 0.9rem;
  }
  .ref-tags { margin-top: 1rem; }
  .ref-tag {
    display: inline-block;
    font-size: 0.72rem;
    padding: 2px 8px;
    border-radius: 20px;
    border: 1px solid #ccc;
    color: #666;
    margin: 2px 3px 2px 0;
  }
  .result-box {
    background: #f0fff4;
    border: 1px solid #9ae6b4;
    border-radius: 6px;
    padding: 0.6rem 1rem;
    margin: 0.5rem 0;
    font-size: 0.88rem;
  }
  .result-box strong { color: #276749; }
  .warning-box {
    background: #fff8e1;
    border: 1px solid #ffe082;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    margin: 0.75rem 0;
    font-size: 0.88rem;
    color: #5d4037;
  }
  .warning-box strong { color: #e65100; }
  table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.88rem; }
  th { background: #f0f4ff; text-align: left; padding: 7px 10px; border: 1px solid #ddd; }
  td { padding: 7px 10px; border: 1px solid #ddd; vertical-align: top; }

---

## Section 1 — Mean Reversion vs. Momentum — Which Way Will the Price Go?

<div class="note-abstract">
Every profitable trading strategy boils down to one of two beliefs about price behaviour: either prices tend to bounce back toward where they came from (mean reversion), or prices tend to keep going in the same direction (momentum). These two views require completely opposite trading actions — and knowing which regime you are in at any given moment is the central challenge of quantitative trading.
</div>

### The big ideas

<div class="key-idea"><strong>Mean reversion says: prices that move away from their normal range will eventually come back.</strong> If you believe this, you buy when something has fallen unusually far and sell when it has risen unusually high, waiting for it to snap back. Most pairs of similar stocks (like two gold ETFs, or two bank stocks) tend to mean-revert — their prices do not diverge forever. This is the basis of pair trading.</div>

<div class="key-idea"><strong>Momentum says: prices that are moving in one direction will continue moving that way for a while.</strong> If you believe this, you buy what is already rising and short what is already falling. Momentum is often driven by the slow spread of news — as more investors gradually discover and react to a company's improving earnings, the price keeps drifting up for days or weeks. PEAD (Post-Earnings Announcement Drift) is a classic momentum strategy.</div>

<div class="key-idea"><strong>The same price can be both mean-reverting and trending, depending on the time horizon.</strong> Over minutes or hours, a price might bounce around a recent average (mean-reverting). Over weeks, it might be in a long upward trend (momentum). This is why the same strategy needs different parameters for different timeframes, and why the regime question never has a single permanent answer.</div>

### What causes each type of behaviour?

| Cause | Type it creates | Example |
|---|---|---|
| News diffusing slowly to investors | Momentum | Earnings beat — price drifts up for weeks as more investors react |
| A large institution executing a big order gradually | Momentum | Fund buying 10 million shares over several days — price trends up |
| Herd behaviour — following what others are doing | Momentum | Meme stocks (GameStop, 2021) — price goes to irrational extremes |
| Liquidity events — forced selling for unrelated reasons | Mean reversion | Fund forced to liquidate — price overshoots, then recovers |
| Two fundamentally linked stocks temporarily diverge | Mean reversion | GLD and GDX — gold ETF and gold miners drift apart, then reconnect |

### Pitfalls specific to mean-reversion backtests

<div class="warning-box">
<strong>⚠️ Data quality trap:</strong> Mean-reversion strategies are especially vulnerable to price data errors. A single wrong tick (e.g., a stock briefly quoted at \$1 instead of \$100) looks like a massive price drop, triggers a huge buy signal, and then generates a fake profit when the correct price is restored. Always clean your data for outliers before backtesting any mean-reversion strategy.
</div>

<div class="warning-box">
<strong>⚠️ Survivorship bias trap:</strong> Mean-reversion strategies tend to buy stocks that have fallen a lot and short stocks that have risen a lot. Stocks that fell and never recovered (because the company went bankrupt) are often missing from biased databases — making the strategy look better than it really was. See Chapter 3 for the survivorship bias deep-dive.
</div>

<div class="ref-tags">
<span class="ref-tag">Mean reversion</span> <span class="ref-tag">Momentum</span> <span class="ref-tag">PEAD</span> <span class="ref-tag">Regime</span> <span class="ref-tag">Pair trading</span>
</div>

---

## Section 2 — Regime Changes and Conditional Parameter Optimization

<div class="note-abstract">
Markets shift between different "regimes" — periods when mean reversion works well, periods when momentum dominates, periods of high volatility, low volatility, and so on. The problem is that trading strategy parameters optimised for one regime often work poorly in another. Conditional Parameter Optimization (CPO) is a machine-learning approach that lets the strategy's own parameters adapt to the current market conditions every single day .
</div>

### The big ideas

<div class="key-idea"><strong>Most strategies use fixed parameters that cannot adapt to changing markets.</strong> Standard optimisation picks one set of parameters (entry threshold, lookback window, hedge ratio) that worked best on historical data, then keeps those settings forever. When the market regime changes, the fixed parameters become suboptimal — and there is no automatic mechanism to update them.</div>

<div class="key-idea"><strong>CPO uses machine learning to pick the best parameters for tomorrow based on today's market conditions.</strong> Instead of predicting whether a stock will go up or down (which everyone is trying to do), CPO predicts which combination of your strategy's own parameters will generate the best return tomorrow given the current technical indicators and market environment. This is a much less crowded prediction target.</div>

<div class="key-idea"><strong>CPO is transparent — your strategy still makes the actual trading decisions.</strong> Machine learning is often criticised as a black box. In CPO, the trading strategy (e.g., a Bollinger Band mean-reversion rule) still decides what to buy and sell. The ML only optimises the input parameters. This preserves interpretability while gaining the adaptability benefit of machine learning.</div>

### Example

<div class="example-block" markdown="1">
<div class="ex-title">Example 7.1 — CPO applied to GLD/GDX Bollinger Band strategy (1-minute bars, 2006–2020) <span class="ex-pill pill-num">Worked results</span></div>

**The base strategy:** Trade GLD (gold ETF) based on its relationship with GDX (gold miners ETF). Every minute, compute the spread between GLD and GDX (weighted by a hedge ratio). When the spread is unusually low (more than X standard deviations below its exponential moving average), buy GLD. When it is unusually high, short GLD. Exit when the spread returns to near-normal.

**Three adjustable parameters:**
- `GDX_weight` — how many GDX shares' worth to compare against each GLD share (tested from 2 to 4)
- `entry_threshold` — how far below normal the spread must be before entering (tested from 0.2 to 5 standard deviations)
- `lookback` — how many minutes of history to use for the moving average (tested from 30 to 720 minutes)

**Standard approach (Unconditional Parameter Optimization):** Pick the one best combination on training data. Use those same settings forever on the test data.

**CPO approach (Conditional Parameter Optimization):** Every day after market close, run 400 combinations of the three parameters through a machine learning model trained to predict each combination's next-day return. Select the combination predicted to work best tomorrow. Use those settings the next day only — then repeat.

**Out-of-sample test set results (last 3 years ending December 31, 2020):**

| Metric | Standard (unconditional) | CPO (conditional) |
|---|---|---|
| Annual return | 17.29% | 19.77% |
| Sharpe ratio | 1.947 | 2.325 |
| Calmar ratio (return ÷ max drawdown) | 0.984 | 1.454 |
| 3-year cumulative return | 73% | 83% |

Every performance metric improved with CPO. The machine learning step adds roughly 2-3% annual return and meaningfully improves the risk-adjusted profile.

<div class="ex-lesson"><strong>Takeaway:</strong> The key insight is that CPO is predicting the performance of your own strategy's parameters — not predicting gold's price directly. That is a much harder problem for competitors to arbitrage away, and it is why CPO tends to work when generic ML applied to price prediction does not.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Regime</span> <span class="ref-tag">CPO</span> <span class="ref-tag">Walk Forward Optimization</span> <span class="ref-tag">Bollinger bands</span> <span class="ref-tag">Machine learning</span>
</div>

---

## Section 3 — Stationarity and Cointegration — The Science of Pair Trading

<div class="note-abstract">
Pair trading works because some pairs of stocks do not diverge forever — their price relationship is "sticky" in a statistical sense. The technical name for this stickiness is cointegration. If two stocks are cointegrated, you can combine their prices (long one, short the other) to form a spread that bounces around a stable average indefinitely. That spread is stationary — and a stationary series is almost perfectly suited for a mean-reversion strategy. But cointegration is not the same as correlation, and confusing the two leads to bad pair selections.
</div>

### The big ideas

<div class="key-idea"><strong>A stationary time series is one that stays close to its average instead of wandering away forever.</strong> Most individual stock prices are not stationary — they just drift further and further from where they started. But the spread between two carefully chosen, related stocks can be stationary, meaning it keeps bouncing back toward the same average level. A stationary spread is ideal for a mean-reversion strategy because it guarantees the spread will revert — as long as the stationarity persists.</div>

<div class="key-idea"><strong>Cointegration is not the same as correlation — and the difference matters enormously.</strong> Correlation measures how much two stocks move in the same direction on a day-to-day basis. Cointegration measures whether their long-run price relationship is stable. Two stocks can be highly correlated (moving in the same direction most days) but completely non-cointegrated (their prices drift further and further apart over years). Conversely, two stocks can be cointegrated (their combined spread stays stable long-term) while being largely uncorrelated on a daily basis.</div>

<div class="key-idea"><strong>Not all stocks from the same industry are cointegrated — you have to test.</strong> It might seem obvious that Coca-Cola and Pepsi, being in the same industry, would be cointegrated. Testing shows they are not — their prices do drift apart over time despite moving in the same direction most days. GLD and GDX, on the other hand, are cointegrated — long GLD, short ~1.63 shares of GDX gives a spread that remains stationary.</div>

### Cointegration vs. correlation — the key distinction

| Property | Correlation | Cointegration |
|---|---|---|
| **Measures** | Whether daily returns move together | Whether the price *relationship* is stable long-term |
| **Time horizon** | Short-term (day by day) | Long-term (months to years) |
| **What it guarantees** | Nothing about where prices end up | That the weighted spread won't drift away forever |
| **Useful for** | Risk management, beta hedging | Pair trading — finding mean-reverting spreads |

### Examples from the book

<div class="example-block" markdown="1">
<div class="ex-title">Example 7.2 — Testing GLD vs. GDX for cointegration and finding the hedge ratio <span class="ex-pill pill-code">Code example</span></div>

**The test:** Use an Augmented Dickey-Fuller (ADF) statistical test to check whether GLD and GDX are cointegrated. If they are, find the hedge ratio — how many GDX shares to short per share of GLD to create a stationary spread.

**MATLAB result:**
```
CADF t-statistic: -3.18
5% critical value: -3.38
10% critical value: -3.08
→ t-stat is between these two: >90% probability of cointegration
Hedge ratio (β): 1.6766
Spread = GLD − 1.6766 × GDX  (this spread is stationary — see Figure 7.2)
```

**Python result:** ADF t-statistic = −2.4, which does not reach even the 90% critical value — suggesting no cointegration. However, this contradicts both the MATLAB and R results, and is likely a library accuracy issue.

**R result:**
```
CADF t-statistic: -3.24
p-value: 0.005
→ Reject the null hypothesis of no cointegration at 99.5% confidence
Hedge ratio: 1.631
```

GLD and GDX are cointegrated. The stationary spread is shown in Figure 7.2 — it bounces around a stable mean without drifting away.

<div class="ex-lesson"><strong>Takeaway:</strong> Always use a formal statistical test for cointegration — do not assume that stocks in the same industry are cointegrated just because they seem related. And when Python and MATLAB disagree on a statistical result, trust MATLAB (which has professionally verified statistical libraries) over Python's free, community-maintained packages.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Example 7.3 — KO vs. PEP: correlated but NOT cointegrated <span class="ex-pill pill-warn">Counterexample</span></div>

Coca-Cola (KO) and PepsiCo (PEP) seem like a natural pair — same industry, same products, same customer base. Most pair traders would assume they are cointegrated.

**Cointegration test result:**
```
ADF t-statistic: -2.14
10% critical value: -3.038
→ t-stat is ABOVE the critical value: less than 90% probability of cointegration
Conclusion: KO and PEP are NOT reliably cointegrated
```

**Correlation test result:**
```
Daily return correlation: 0.4849
P-value: effectively 0
→ They are highly and significantly correlated on a daily basis
```

So KO and PEP move in the same direction most days (correlated), but their prices can and do drift apart indefinitely over long periods (not cointegrated). This means a pair trade between KO and PEP has no mathematical guarantee of mean-reverting — the spread could just keep widening.

Figure 7.3 shows this: the KO-PEP spread is clearly non-stationary, with no tendency to return to a fixed mean.

<div class="ex-lesson"><strong>Takeaway:</strong> Correlation tells you how stocks move together day to day. Cointegration tells you whether their long-run relationship is stable. You need the latter for pair trading — correlation alone is not enough. Always run the formal ADF test before trading any pair.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Stationarity</span> <span class="ref-tag">Cointegration</span> <span class="ref-tag">Correlation</span> <span class="ref-tag">Hedge ratio</span> <span class="ref-tag">ADF test</span> <span class="ref-tag">Pair trading</span>
</div>

---

## Section 4 — Factor Models — What Actually Drives Stock Returns?

<div class="note-abstract">
Financial commentators often say things like "the market is favouring value stocks" or "small-cap stocks are outperforming." Factor models are the mathematical framework that makes these casual observations precise. A factor model says: a stock's return can be broken down into contributions from a small number of common drivers (factors) plus a random component specific to that stock. Understanding which factors are driving returns right now is one of the most powerful tools in a quant trader's toolkit.
</div>

### The big ideas

<div class="key-idea"><strong>A factor model explains stock returns using a small number of common market forces.</strong> Instead of trying to predict each stock individually, a factor model says that most of a stock's return comes from broad forces that affect many stocks at once — things like "the market went up today" or "small-cap stocks outperformed today." These broad forces are called factors. The part that a factor model cannot explain is called the specific return — essentially just noise specific to that one company.</div>

<div class="key-idea"><strong>The Fama-French Three-Factor model is the most famous example.</strong> It says a stock's return depends on three things: (1) the overall market return (beta), (2) whether small-cap stocks outperformed large-cap stocks that day (the SMB factor), and (3) whether cheap (value) stocks outperformed expensive (growth) stocks that day (the HML factor). Factor models like this have been shown to explain a large fraction of most stocks' returns without knowing anything specific about those companies.</div>

<div class="key-idea"><strong>Principal Component Analysis (PCA) finds factors automatically from historical data without needing to define them in advance.</strong> Instead of deciding upfront that "small-cap vs. large-cap" is a factor, PCA just looks at the pattern of historical stock returns and finds the directions of maximum variation. The result is a set of statistical factors that are mathematically guaranteed to be uncorrelated — even if their economic interpretation is not always obvious.</div>

### The Fama-French Three-Factor model explained simply

| Factor | What it measures | Example exposure |
|---|---|---|
| **Market (beta)** | How much does this stock move when the whole market moves? | Beta = 1.5 means the stock moves 1.5× the market |
| **SMB (small minus big)** | Does this stock behave more like small-cap or large-cap? | A micro-cap stock has positive SMB exposure |
| **HML (high minus low)** | Is this a value stock (cheap) or growth stock (expensive)? | A stock with a low P/E ratio has positive HML exposure |

### Example from the book

<div class="example-block" markdown="1">
<div class="ex-title">Example 7.4 — PCA factor model applied to S&P 600 small-cap stocks <span class="ex-pill pill-num">Strategy result</span></div>

**The approach:** Instead of using named factors (market, SMB, HML), use PCA to extract 5 statistical factors from the daily returns of all S&P 600 small-cap stocks over the past 252 trading days. Assume these factor returns have momentum — they will remain roughly the same tomorrow as they are today. Based on that assumption, predict each stock's next-day return. Buy the 50 stocks with the highest predicted return and short the 50 with the lowest.

**Results (no transaction costs):**

<div class="result-box">
<strong>Average annual return: 2% (MATLAB) to 4% (Python/R)</strong><br>
<strong>Sharpe ratio: ~0.21 (MATLAB) to ~0.58 (Python/R)</strong>
</div>

The strategy generates positive returns but they are modest — and this is before transaction costs. The difference in results between MATLAB and Python/R are due to rounding differences in the PCA implementation, not a fundamental disagreement.

<div class="ex-lesson"><strong>Takeaway:</strong> PCA factor models work in the right conditions — when factor returns genuinely have momentum from one day to the next. But they cannot capture mean reversion (which requires factor exposures that change with recent price moves) and are sensitive to regime shifts where the factors' momentum breaks down.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Factor model</span> <span class="ref-tag">Fama-French</span> <span class="ref-tag">PCA</span> <span class="ref-tag">Beta</span> <span class="ref-tag">SMB</span> <span class="ref-tag">HML</span> <span class="ref-tag">Factor exposure</span>
</div>

---

## Section 5 — When Should You Exit a Trade?

<div class="note-abstract">
Entry signals get all the attention in trading strategy design, but exit signals are just as important — and often more so. Getting out at the wrong time can turn a winning strategy into a losing one. The right exit approach depends entirely on whether your strategy is mean-reverting or momentum-based, and treating these two types the same way is a common and costly mistake.
</div>

### The big ideas

<div class="key-idea"><strong>For mean-reverting strategies, the half-life of mean reversion tells you how long to hold a position.</strong> The Ornstein-Uhlenbeck formula describes how a mean-reverting spread decays back to its average. By fitting this formula to historical spread data, you can calculate the "half-life" — the expected time for the spread to move halfway back toward its mean. This is your natural holding period, and you can estimate it from the entire historical time series, not just from the limited number of actual trades.</div>

<div class="key-idea"><strong>For momentum strategies, the optimal holding period is shorter than you think — and getting shorter over time.</strong> Momentum is driven by information diffusing slowly to investors. As news spreads faster (more financial media, faster internet, more active quant traders), the diffusion completes sooner, and prices reach their new equilibrium faster. A momentum strategy that needed a week-long holding period five years ago might only work with a one-day holding period today.</div>

<div class="key-idea"><strong>Stop losses work for momentum strategies but hurt mean-reverting strategies.</strong> In a momentum strategy, a reversal in price direction is a genuine signal that the trend has ended — exiting at a loss makes sense. In a mean-reverting strategy, a price moving further away from the mean is not a signal of a trend change — it is just the spread overshooting temporarily. Exiting with a stop loss in this case locks in a loss at exactly the wrong moment — right before the reversal that your strategy was counting on.</div>

### Exit strategy decision tree

| Strategy type | Normal exit | Alternative exit | Stop loss? |
|---|---|---|---|
| **Mean-reversion** | Fixed holding period = half-life of mean reversion | Target price = historical mean (µ) | ❌ No — exits at the worst moment |
| **Momentum** | Fixed holding period (backtested) | Opposite entry signal fires | ✅ Yes — a price reversal signals the trend has ended |

### The Ornstein-Uhlenbeck half-life formula

The Ornstein-Uhlenbeck (OU) formula describes mean-reverting processes mathematically:

```
dz(t) = −θ × (z(t) − μ) × dt + dW

Where:
  z(t)  = the spread at time t
  μ     = the long-run average value of the spread
  θ     = the speed of mean reversion (higher = faster reversion)
  dW    = random noise (Gaussian)

Half-life = ln(2) / θ

To find θ: run a linear regression of daily changes in the spread
(dz) against the spread itself (z − mean(z)).
The slope of this regression is −θ.
```

### Example from the book

<div class="example-block" markdown="1">
<div class="ex-title">Example 7.5 — Calculating the half-life of the GLD-GDX spread <span class="ex-pill pill-num">Worked numbers</span></div>

Using the GLD-GDX spread from Example 7.2 (Spread = GLD − 1.67 × GDX):

**MATLAB steps:**
1. Calculate the daily change in the spread: `dz = z(t) − z(t−1)`
2. Regress `dz` against `z(t−1) − mean(z)`: the slope of this regression is `−θ`
3. Calculate the half-life: `half-life = ln(2) / θ`

```matlab
results = ols(dz, prevz - mean(prevz));
theta = results.beta;
halflife = -log(2) / theta
% halflife = 7.84 trading days
```

**Python result:** half-life = 7.84 trading days  
**R result:** half-life = 7.84 trading days — all three agree.

<div class="result-box"><strong>Half-life of GLD-GDX mean reversion: approximately 7-10 trading days</strong></div>

This means: after entering a spread trade, you should expect to hold it for roughly 7–10 trading days before the spread has reverted about halfway back to its mean. This is your natural holding period estimate — derived mathematically from the data, not guessed from a backtest of individual trades.

<div class="ex-lesson"><strong>Takeaway:</strong> The half-life calculated from the Ornstein-Uhlenbeck formula is far more statistically robust than trying to infer holding period from the limited number of actual trades in your backtest. It uses all the historical data, not just the subset of days when a trade was triggered.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Half-life</span> <span class="ref-tag">Ornstein-Uhlenbeck</span> <span class="ref-tag">Stop loss</span> <span class="ref-tag">Exit strategy</span> <span class="ref-tag">Target price</span>
</div>

---

## Section 6 — Seasonal Trading Strategies

<div class="note-abstract">
Some patterns in financial markets repeat at roughly the same time every year, driven by recurring real-world events — tax deadlines, seasonal demand for energy, agricultural harvests, summer driving. Seasonal trading strategies try to exploit these predictable patterns. The key finding from the book: seasonal effects in stock markets have mostly disappeared over the years as they became widely known, but seasonal effects in commodity futures are alive and well because they are driven by genuine physical demand cycles, not investor psychology.
</div>

### The big ideas

<div class="key-idea"><strong>Seasonal equity strategies like the "January effect" have largely stopped working.</strong> The January effect — where small-cap stocks that fell the most in December tend to recover in January (as tax-loss selling pressure reverses) — was well-documented for decades. But once enough traders knew about it and started buying in late December in anticipation, the effect was arbitraged away. The backtested version looks great; the out-of-sample version often does not.</div>

<div class="key-idea"><strong>Commodity futures seasonal strategies are still profitable because they are driven by real economic needs, not investor psychology.</strong> Gasoline demand rises every spring as summer driving season approaches. Natural gas demand rises as summer air conditioning kicks in. These patterns are driven by physical reality, not by traders' beliefs about other traders — making them harder to arbitrage away completely.</div>

<div class="key-idea"><strong>Seasonal commodity strategies only trade once a year — so you need out-of-sample validation to trust them.</strong> When a strategy only triggers once per year, a 10-year backtest only gives you 10 data points. That is not enough to statistically validate that the pattern is real and not just coincidence. The book explicitly marks the post-2007 results for gasoline and natural gas as out-of-sample, which is essential honesty — and those results are what actually matter.</div>

### Examples from the book

<div class="example-block" markdown="1">
<div class="ex-title">Example 7.6 — The January effect (equity seasonal) — works in backtest, fails out-of-sample <span class="ex-pill pill-warn">Cautionary example</span></div>

**The strategy:** From S&P 600 small-cap stocks, identify those with the worst returns in December. Buy them at the end of December, sell them at the end of January. Rationale: tax-loss selling pressure in December depresses these stocks artificially; when the pressure lifts in January, prices recover.

This worked well in historical backtests covering many years before 2006. But by 2006–2007, enough traders knew about it that the trade had been arbitraged away. It worked again in January 2008 — but that was during an unusual period of extreme market turmoil (the Société Générale scandal and a surprise Fed rate cut) that benefited mean-reversion strategies broadly, not specifically the January effect.

<div class="ex-lesson"><strong>Takeaway:</strong> When a widely-published seasonal pattern in equities stops working, it is probably because the strategy itself has been arbitraged away. Equity markets are efficient enough that patterns driven by investor psychology tend to disappear once they become widely known.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Example 7.7 — Year-on-year seasonal trending (equity) — also does not work out-of-sample <span class="ex-pill pill-warn">Cautionary example</span></div>

**The strategy:** At each month-end, buy the stocks from the S&P 500 that had the best returns in the same month one year earlier, and short those with the worst returns in that same month one year earlier. The idea: whatever drove returns in that calendar month last year (seasonal factors, sector rotations) may repeat this year.

**Out-of-sample results:**

<div class="result-box">
<strong>Average annual return: −1.3%  |  Sharpe ratio: −0.12</strong><br>
Strategy loses money on average out-of-sample.
</div>

<div class="ex-lesson"><strong>Takeaway:</strong> The "same-month-last-year" seasonal effect in stocks is not a reliable pattern, at least not on the S&P 500 universe. Testing on the most recent 5 years shows even worse results, suggesting the pattern was always weak and has continued to deteriorate.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Gasoline futures seasonal trade — profitable 19 of 21 years (2007–2015 out-of-sample) <span class="ex-pill pill-live">Real strategy</span></div>

**The trade:**
- **Instrument:** RB (unleaded gasoline futures on NYMEX), May contract
- **Entry:** Buy at close of April 13 (or next trading day if holiday)
- **Exit:** Sell at close of April 25 (or previous trading day if holiday)
- **Rationale:** Summer driving season approaches → gasoline demand rises → May futures price increases in late April

**Annual P&L (selected years, post-2007 are out-of-sample):**

| Year | P&L ($) | Max drawdown ($) |
|---|---|---|
| 2007 (out-of-sample) | +4,322 | −5,279 |
| 2008 (out-of-sample) | +9,740 | −1,156 |
| 2009 (out-of-sample) | −890 | −4,167 |
| 2012 (out-of-sample) | −7,997 | −8,742 |
| 2015 (out-of-sample) | +8,539 | −1,753 |

**Overall:** Profitable in 19 of the 21 years shown, including many out-of-sample years. The two losing years were modest. The trade is economically motivated and has held up out-of-sample better than any equity seasonal strategy.

<div class="ex-lesson"><strong>Takeaway:</strong> Commodity seasonal trades driven by real physical demand — not investor psychology — are far more durable than equity seasonal trades. The gasoline trade has a clear economic mechanism (summer driving) that will not disappear just because traders know about it.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Natural gas futures seasonal trade — profitable 13 consecutive years, but volatile out-of-sample <span class="ex-pill pill-warn">Use caution</span></div>

**The trade:**
- **Instrument:** NG (natural gas futures on NYMEX), June contract
- **Entry:** Buy at close of February 25
- **Exit:** Sell at close of April 15
- **Rationale:** Rising summer demand for air conditioning electricity → more natural gas burned by power generators → June futures price rises in the spring

**Out-of-sample results (2007–2016):** Mixed. The trade had large losses in 2009 (−$4,240), 2010 (−$8,360), and 2012 (−$7,180). Natural gas is extremely volatile — Amaranth Advisors lost $6 billion on natural gas trades in 2006.

<div class="warning-box"><strong>⚠️ Caution:</strong> Natural gas futures are notoriously volatile. Unlike the gasoline trade, this strategy's out-of-sample record is much weaker. If you do trade it, consider the mini QG contracts at half the position size of the full NG contract to limit risk.</div>

<div class="ex-lesson"><strong>Takeaway:</strong> Having a sensible economic rationale for a seasonal trade is necessary but not sufficient. Natural gas has a real seasonal demand pattern — but the market is so volatile that the pattern is often swamped by other factors. Small position sizing is essential.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Seasonal trading</span> <span class="ref-tag">January effect</span> <span class="ref-tag">Gasoline futures</span> <span class="ref-tag">Natural gas futures</span> <span class="ref-tag">Calendar effect</span>
</div>

---

## Section 7 — High-Frequency Trading

<div class="note-abstract">
High-frequency trading (HFT) strategies do not hold positions overnight — and often hold for only seconds or minutes. Their defining advantage is the law of large numbers: with thousands of small bets per day, even a tiny average edge per trade compounds into impressive daily consistency. This consistency translates into very high Sharpe ratios, which, as we know from Chapter 6, allows aggressive leverage and very high returns on capital. But the barriers to entry — speed, infrastructure, capital, and technical expertise — are genuinely high.
</div>

### The big ideas

<div class="key-idea"><strong>HFT generates high Sharpe ratios through the law of large numbers.</strong> If your strategy has a tiny but genuine edge on every trade, doing that trade 1,000 times per day means the daily result will be very close to 1,000 × the average edge per trade — with very little variance. This is pure mathematics: more independent bets of the same type produce more stable outcomes. High Sharpe ratios, from Chapter 6, unlock the highest possible compounded growth.</div>

<div class="key-idea"><strong>Transaction costs and speed are everything in HFT — more so than the trading idea itself.</strong> A strategy that generates 0.01% profit per trade before costs might generate 0.005% after costs — or be completely unprofitable if costs are slightly higher. Unlike daily strategies where costs are a significant but manageable concern, HFT lives or dies entirely on execution quality. Professional HFT firms co-locate servers physically next to exchange matching engines to shave microseconds off execution time.</div>

<div class="key-idea"><strong>Backtesting HFT strategies is much harder than backtesting daily strategies — and often unreliable.</strong> Reliable HFT backtesting requires tick-by-tick data with bid and ask prices (not just last trade prices), historical order book data, and a highly realistic market simulator that accounts for queue position, partial fills, and latency. Without all of this, HFT backtests are essentially meaningless. Often the only true test is to run the strategy live with small capital.</div>

### HFT vs. daily strategies — a comparison

| Feature | Daily strategy | High-frequency strategy |
|---|---|---|
| **Holding period** | Days to months | Seconds to minutes (never overnight) |
| **Bets per day** | 1–10 | 100 to 10,000+ |
| **Typical Sharpe ratio** | 1–3 | 3–10+ |
| **Leverage possible** | 2–10× | 10–100×+ |
| **Main cost driver** | Transaction costs | Transaction costs + latency |
| **Backtesting reliability** | High (with clean daily data) | Low (requires very specialised tick data) |
| **Infrastructure needed** | Standard PC, internet connection | Co-location, C++ code, low-latency feeds |
| **Drawdown profile** | Can have multi-month drawdowns | Very quick to go flat — risk is manageable |
| **Independent trader feasibility** | Achievable | Difficult but not impossible to work toward |

<div class="ref-tags">
<span class="ref-tag">High-frequency trading</span> <span class="ref-tag">Law of large numbers</span> <span class="ref-tag">Co-location</span> <span class="ref-tag">Latency</span> <span class="ref-tag">Sharpe ratio</span>
</div>

---

## Section 8 — Low-Beta vs. High-Beta — Which Is the Better Portfolio?

<div class="note-abstract">
If you want more return, you could either apply more leverage to a low-risk portfolio or switch to a portfolio of high-risk (high-beta) stocks. Both seem like they should give the same result. But they do not — and the reason why connects directly back to the Kelly formula and Sharpe ratios from Chapter 6.
</div>

### The big ideas

<div class="key-idea"><strong>Higher beta does not automatically mean higher compounded growth — it just means higher average return and higher risk in equal proportion.</strong> The Fama-French model says that a stock's return is proportional to its beta. So doubling the beta of your portfolio doubles the average return — but it also doubles the volatility. From the Kelly formula (Chapter 6), compounded growth rate depends on Sharpe ratio squared, not raw return. If doubling beta doubles both return and volatility, the Sharpe ratio stays the same and compounded growth stays the same.</div>

<div class="key-idea"><strong>Empirically, low-beta stocks tend to have higher Sharpe ratios than high-beta stocks.</strong> This is a consistent empirical finding: the market tends to underprice low-beta stocks and overprice high-beta stocks (perhaps because many investors cannot use leverage and therefore chase beta as a substitute). A portfolio of low-beta stocks, properly levered using the Kelly formula, will beat a portfolio of high-beta stocks in long-run compounded wealth — because the lower volatility allows more aggressive optimal leverage.</div>

<div class="key-idea"><strong>The practical implication: prefer low-beta, then lever up.</strong> Dr. Edward Qian at PanAgora Asset Management showed that the traditional 60/40 stock-bond portfolio is not optimal — it has too much risk concentration in stocks. A 23% stocks / 77% bonds portfolio, levered up to match the same risk level, achieves a higher Sharpe ratio and therefore higher long-run compounded wealth. The insight: diversify first, lever second.</div>

<div class="ref-tags">
<span class="ref-tag">Beta</span> <span class="ref-tag">Low-beta portfolio</span> <span class="ref-tag">Leverage</span> <span class="ref-tag">Kelly formula</span> <span class="ref-tag">Fama-French</span> <span class="ref-tag">Risk parity</span>
</div>

---

## Term Glossary

Definitions for every key terms.

### Statistical Concepts

<div class="glossary-entry">
<div class="gterm">Stationarity <span class="gcat cat-stats">Statistics</span></div>
A time series is stationary when it stays close to a stable average rather than wandering away over time. Most individual stock prices are non-stationary — they just drift further from their starting point. A stationary time series is ideal for mean-reversion strategies because it mathematically guarantees the price will revert — as long as stationarity persists. Formally described as "integrated of order zero" or I(0).
</div>

<div class="glossary-entry">
<div class="gterm">Cointegration <span class="gcat cat-stats">Statistics</span></div>
A statistical property where a linear combination of two (or more) non-stationary price series produces a stationary series. In practice: long one stock, short another in the right proportion, and the resulting spread is stationary (mean-reverting). Two stocks from the same industry are often cointegrated, but not always — you must test with an Augmented Dickey-Fuller (ADF) test. Being cointegrated is not the same as being correlated.
</div>

<div class="glossary-entry">
<div class="gterm">Correlation vs. cointegration <span class="gcat cat-stats">Statistics</span></div>
Correlation measures whether two stocks' daily returns move in the same direction (short-term, return-based). Cointegration measures whether the long-run price relationship between two stocks is stable (long-term, price-level-based). KO and PEP are correlated (their daily returns move together) but not cointegrated (their price levels drift apart over years). GLD and GDX are cointegrated (their price spread stays bounded). For pair trading, you need cointegration, not just correlation.
</div>

<div class="glossary-entry">
<div class="gterm">ADF test (Augmented Dickey-Fuller) <span class="gcat cat-stats">Statistics</span></div>
The standard statistical test for whether a time series is stationary (ADF test on a single series) or whether two series are cointegrated (CADF test, a variation). The test produces a t-statistic: the more negative it is, the stronger the evidence for stationarity or cointegration. Standard critical values: −3.94 (1% level, very strong evidence), −3.38 (5%), −3.08 (10%). If the t-statistic is less negative than the 10% critical value, there is insufficient evidence of cointegration.
</div>

<div class="glossary-entry">
<div class="gterm">Ornstein-Uhlenbeck (OU) process <span class="gcat cat-stats">Statistics</span></div>
A mathematical model for mean-reverting processes. The formula: dz = −θ × (z − μ) × dt + dW, where z is the spread, μ is its long-run mean, θ is the speed of reversion, and dW is random noise. The key output for traders is the half-life: ln(2) / θ — the expected time for the spread to revert halfway back to its mean. Found by regressing daily spread changes against the spread level. The GLD-GDX spread has a half-life of approximately 7-10 trading days.
</div>

<div class="glossary-entry">
<div class="gterm">Half-life (of mean reversion) <span class="gcat cat-stats">Statistics</span></div>
The expected time for a mean-reverting spread to move halfway back toward its long-run average after a deviation. Calculated from the Ornstein-Uhlenbeck formula as ln(2) / θ. Serves as the natural estimate for how long to hold a mean-reverting position. More statistically robust than inferring holding period from the limited number of actual trades in a backtest, because it uses the entire time series of spread values.
</div>

### Models & Frameworks

<div class="glossary-entry">
<div class="gterm">Factor model (APT) <span class="gcat cat-model">Model</span></div>
A mathematical framework that explains a stock's return as the sum of contributions from a small number of common market forces (factors) plus a random component specific to that stock alone. The formula: R = X·b + u, where R is the vector of stock returns, X is the matrix of factor exposures, b is the vector of factor returns, and u is the specific (idiosyncratic) return. The most famous example is the Fama-French Three-Factor model.
</div>

<div class="glossary-entry">
<div class="gterm">Fama-French Three-Factor model <span class="gcat cat-model">Model</span></div>
A factor model that explains stock returns using three factors: (1) the overall market return (beta), (2) the SMB factor (small-minus-big: whether small-cap stocks outperformed large-cap stocks), and (3) the HML factor (high-minus-low: whether value stocks outperformed growth stocks). One of the most widely used and academically validated factor models in finance.
</div>

<div class="glossary-entry">
<div class="gterm">Beta <span class="gcat cat-model">Model</span></div>
The sensitivity of a stock's or portfolio's returns to the overall market. Beta = 1 means the stock moves in lockstep with the market. Beta = 2 means it moves twice as much. Beta = 0.5 means half as much. Higher beta means higher average returns and higher risk in equal proportion — which means the Sharpe ratio stays the same. Empirically, low-beta stocks tend to have slightly better Sharpe ratios than high-beta stocks, making a levered low-beta portfolio superior to an unlevered high-beta one.
</div>

<div class="glossary-entry">
<div class="gterm">SMB and HML factors <span class="gcat cat-model">Model</span></div>
Two of the three Fama-French factors. SMB (Small Minus Big) captures the return difference between small-cap and large-cap stocks — positive when small caps outperform. HML (High Minus Low) captures the return difference between value stocks (high book-to-price ratio) and growth stocks (low book-to-price ratio) — positive when value stocks outperform. Both have been positive on average historically, though HML has underperformed in recent years (2017–2020) as growth stocks dominated.
</div>

<div class="glossary-entry">
<div class="gterm">Factor exposure <span class="gcat cat-model">Model</span></div>
How sensitive a particular stock is to each factor in a factor model. Found by regressing a stock's historical returns against the factor returns. A small-cap stock has positive SMB exposure. A growth stock has negative HML exposure. Factor exposures are different for every stock — they describe that stock's individual sensitivity to each common market force.
</div>

<div class="glossary-entry">
<div class="gterm">CPO (Conditional Parameter Optimization) <span class="gcat cat-model">Model</span></div>
A machine-learning approach to adapting a trading strategy's parameters to current market conditions. Instead of using fixed parameters or slowly updating them on expanding historical data, CPO predicts every day which combination of parameters will generate the best return tomorrow, given today's market conditions (captured by technical indicators). Uses random forest with boosting as the ML algorithm. Applied to GLD/GDX Bollinger Band strategy, CPO improved annual return from 17.3% to 19.8% and Sharpe from 1.95 to 2.33 out-of-sample.
</div>

### Exit Strategies

<div class="glossary-entry">
<div class="gterm">Fixed holding period <span class="gcat cat-exit">Exit</span></div>
The simplest exit strategy: hold every trade for a pre-set number of days (or hours, or minutes) and then close it regardless of profit or loss. For mean-reverting strategies, the optimal holding period is typically the half-life of mean reversion calculated from the OU formula.
</div>

<div class="glossary-entry">
<div class="gterm">Opposite entry signal exit <span class="gcat cat-exit">Exit</span></div>
Exiting a position when the same strategy that generated the original entry signal now generates an opposite signal. For a momentum strategy: if you entered long because the signal said "bullish" and now the signal says "bearish," exit the long. This is a principled alternative to stop losses that is directly justified by the logic of the strategy itself, without introducing an arbitrary extra parameter.
</div>

### Seasonal & HFT

<div class="glossary-entry">
<div class="gterm">January effect <span class="gcat cat-seasonal">Seasonal</span></div>
A historically observed seasonal pattern where small-cap stocks that fell the most in December tend to recover in January, as tax-loss selling pressure (which depressed prices in December) reverses. Well-documented for decades but largely arbitraged away in recent years as the strategy became widely known and traders began buying in late December in anticipation of the January recovery.
</div>

<div class="glossary-entry">
<div class="gterm">Commodity futures seasonal trade <span class="gcat cat-seasonal">Seasonal</span></div>
A strategy that buys or sells a commodity futures contract at a specific time of year and closes the position at another specific time, based on recurring real-world demand patterns. 
</div>

<div class="glossary-entry">
<div class="gterm">High-frequency trading (HFT) <span class="gcat cat-hft">HFT</span></div>
Trading strategies that do not hold positions overnight — often holding for seconds or minutes. Generate high Sharpe ratios through the law of large numbers: many small independent bets per day produce very stable outcomes. The high Sharpe ratios allow aggressive leverage and very high returns on capital. Require specialised infrastructure (co-location servers, C++ code, low-latency data feeds) that makes them difficult for independent traders to implement from scratch.
</div>

<div class="glossary-entry">
<div class="gterm">Law of large numbers (in trading) <span class="gcat cat-hft">HFT</span></div>
The statistical principle that as the number of independent bets increases, the average outcome converges toward the true expected value. Applied to HFT: placing 1,000 independent trades per day with a genuine positive average edge produces a daily result very close to 1,000 × the average edge, with very little day-to-day variance. This is why HFT strategies have high Sharpe ratios even with tiny per-trade edges.
</div>

<div class="glossary-entry">
<div class="gterm">Co-location <span class="gcat cat-hft">HFT</span></div>
Placing your trading server physically inside or adjacent to the exchange's data centre, to minimise the time it takes for your orders to reach the exchange. A co-located server can respond to market data and submit orders in microseconds. Signals must travel through fibre optic cables — the speed of light itself is the limiting factor. Professional HFT firms pay significant fees to exchanges for co-location rights.
</div>

<div class="glossary-entry">
<div class="gterm">Risk parity <span class="gcat cat-model">Model</span></div>
A portfolio construction approach that allocates capital based on equalising risk contribution from each asset, rather than equalising dollar amounts. Dr. Edward Qian at PanAgora argued that a traditional 60% stocks / 40% bonds portfolio is not risk-efficient because stocks dominate the risk. A 23% stocks / 77% bonds portfolio, levered to the same total risk, achieves a higher Sharpe ratio because the risk is more evenly distributed. The principle: diversify risk first, then lever up to the desired return level.
</div>
