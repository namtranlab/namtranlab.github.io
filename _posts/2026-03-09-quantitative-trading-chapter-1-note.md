---
layout: distill
title: "Quantitative Trading — Chapter 2 Study Notes"
description: Deep-dive notes on Chapter 2 of Ernest P. Chan's Quantitative Trading (2nd Ed.) — covering idea sources, strategy screening, performance metrics, transaction costs, data biases, and a full term glossary.
tags: Finance Quant Trading Notes
giscus_comments: true
date: 2026-03-09
featured: true
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NYSE_floor.jpg/1280px-NYSE_floor.jpg

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Section 1 — Core Thesis & Idea Sources
  - name: Section 2 — Personal Fit
  - name: Section 3 — Capital & Leverage
  - name: Section 4 — Performance Measurement
  - name: Section 5 — Transaction Costs
  - name: Section 6 — Data Biases
  - name: Section 7 — Pre-Backtest Screening Checklist
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
  .cat-data     { background: #dbeafe; color: #1e3a8a; }
  .cat-risk     { background: #fce8e6; color: #7f1d1d; }
  .cat-perf     { background: #fef3c7; color: #78350f; }
  .cat-capital  { background: #d1fae5; color: #064e3b; }
  .cat-inst     { background: #ede8fc; color: #3c2a8a; }
  .cat-bias     { background: #dcfce7; color: #14532d; }
  .cat-cost     { background: #fce7f3; color: #831843; }
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
  table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.88rem; }
  th { background: #f0f4ff; text-align: left; padding: 7px 10px; border: 1px solid #ddd; }
  td { padding: 7px 10px; border: 1px solid #ddd; vertical-align: top; }

---

> **Book:** *Quantitative Trading* (2nd Ed.) — Ernest P. Chan
> **Chapter:** 2 — Fishing for Ideas: Where Can We Find Good Strategies?

These notes provide a section-by-section abstract of the author's core intellectual position, strategy examples drawn directly from the text, and a full term glossary at the end for reference.

---

## Section 1 — Core Thesis & Idea Sources

<div class="note-abstract">
The scarcity of good trading ideas is not the real problem — ideas are abundant, public, and free. The genuine intellectual work is developing a discriminating taste for viable strategies without wasting time on a full backtest. This reframes the trader's primary effort from discovery to curation: the ability to filter noise from signal before any analytical commitment is made.
</div>

### Core ideas

<div class="key-idea"><strong>Modification is the real alpha source.</strong> Public strategies are raw material. The proprietary edge lives in the variations — holding period, universe, timing — not the base idea itself. What feels like a secret is usually widely known; the implementation is what is protected.</div>

<div class="key-idea"><strong>Openness generates more ideas than it costs.</strong> The paranoid secrecy of institutional culture is counterproductive for independents. Sharing an idea publicly invites correction of errors and surfaces better ideas in return.</div>

<div class="key-idea"><strong>Academic strategies are often stale, complex, or small-cap constrained.</strong> By the time a strategy appears in a journal, it is frequently already arbitraged away, requires expensive data, or only works in illiquid stocks where execution erodes the theoretical gain entirely.</div>

---

## Section 2 — Personal Fit

<div class="note-abstract">
Strategy viability is inseparable from the trader's personal circumstances. The most technically superior strategy is worthless if it cannot be operated, funded, or psychologically sustained. Before evaluating any strategy on its merits, an honest audit of four personal dimensions — time, skill, capital, and goal — must define the feasible set. Fit precedes merit.
</div>

### Core ideas

<div class="key-idea"><strong>Personal fit is assessed before analytical merit.</strong> A great strategy requiring full-time monitoring is not a great strategy for a part-time trader. Establish the feasible set first, then evaluate strategies within it.</div>

<div class="key-idea"><strong>Buy-and-hold is mathematically suboptimal for long-term growth.</strong> Maximum long-term capital growth comes from finding the highest Sharpe ratio strategy and applying optimal leverage — not from holding indefinitely. The Kelly Criterion (Chapter 6) proves this formally.</div>

<div class="key-idea"><strong>Trading frequency and income regularity are directly coupled.</strong> Consistent monthly income requires short holding periods. Longer holding periods produce higher P&L variance — fundamentally incompatible with predictable income needs regardless of average annual return.</div>

### Strategy examples

<div class="example-block">
<div class="ex-title">Short-term vs. long-term strategy — Sharpe comparison <span class="ex-pill pill-num">Conceptual</span></div>
A short-term strategy with a small annual return but very high Sharpe ratio is preferable to a long-term strategy with a high annual return but lower Sharpe ratio — even if the goal is long-term capital growth. Sharpe determines how aggressively leverage can be applied, and leveraged return is the true terminal wealth driver. A Sharpe 3.0 / 8% return strategy outperforms a Sharpe 0.8 / 25% return strategy once leverage is correctly sized.
<div class="ex-lesson"><strong>Lesson:</strong> Never compare strategies on nominal return alone. Always compare on Sharpe ratio, then apply leverage to the winner.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">ETF</span> <span class="ref-tag">Limit order</span> <span class="ref-tag">Intraday vs. overnight</span> <span class="ref-tag">Sharpe ratio</span>
</div>

---

## Section 3 — Capital & Leverage

<div class="note-abstract">
Capital level is not merely a financial parameter — it is a master constraint that cascades into every subsequent decision. Available capital determines which instruments are tradeable, what leverage is accessible, what data quality can be afforded, and therefore which strategies are worth considering. This is a decision tree, not a set of soft preferences.
</div>

### Core ideas

<div class="key-idea"><strong>Capital determines the feasible strategy universe more than skill does.</strong> Different capital levels open structurally different strategy spaces across instruments, leverage, and data quality.</div>

<div class="key-idea"><strong>Low-capital traders should use futures, FX, and options — not stocks.</strong> The leverage embedded in these instruments compensates for limited capital in ways that direct stock ownership cannot.</div>

<div class="key-idea"><strong>Dollar-neutral portfolios require double the capital for the same gross exposure.</strong> This arithmetic constraint makes market-neutral strategies inaccessible without portfolio margin at ~$100K minimum NAV.</div>

### Capital constraint decision table

| Factor | Low capital (&lt;$100K) | High capital (&gt;$100K) |
|---|---|---|
| Account type | Proprietary trading firm | Retail brokerage |
| Instruments | Futures, FX, options | Everything incl. stocks |
| Holding period | Intraday only | Intra- and overnight |
| Position type | Directional only | Directional or market-neutral |
| Data quality | Daily, survivorship-biased OK | Tick-level, survivorship-free |
| News access | Delayed/low-coverage | Real-time Bloomberg-tier |

---

## Section 4 — Performance Measurement

<div class="note-abstract">
Raw return is the wrong primary metric for evaluating trading strategies — and most practitioners, including senior risk managers at billion-dollar funds, get this wrong. The Sharpe ratio is the correct master metric because it determines how much leverage can safely be applied, and it is leveraged return — not nominal return — that determines terminal wealth. This is the theoretical foundation on which every subsequent chapter builds.
</div>

### Core ideas

<div class="key-idea"><strong>Sharpe ratio, not return, is the master performance metric.</strong> Higher Sharpe permits more aggressive leverage, which multiplies terminal wealth. A strategy with Sharpe 3.0 and modest nominal return will outperform a Sharpe 0.8 strategy with high nominal return once both are optimally levered.</div>

<div class="key-idea"><strong>Drawdown is the metric that determines psychological survivability.</strong> Drawdowns cause traders to abandon valid strategies at the worst possible moment — at the trough. Drawdown tolerance must be calibrated honestly before a strategy is selected, not after.</div>

<div class="key-idea"><strong>Trading frequency is a leading indicator of Sharpe ratio.</strong> Strategies trading only a few times per year almost certainly have low Sharpe. Deep drawdowns (>10%, >4 months) signal low Sharpe before any calculation is needed.</div>

### Sharpe ratio benchmarks

| Sharpe ratio | Interpretation | Viability |
|---|---|---|
| < 1.0 | High volatility relative to returns | Not viable as standalone |
| ≥ 1.0 | Minimum acceptable threshold | Borderline |
| ≥ 2.0 | Profitable almost every month | Good |
| ≥ 3.0 | Profitable almost every day | Excellent |

**Formula:**

```
Sharpe Ratio = (Avg Portfolio Return − Risk-Free Rate) ÷ Std Dev of Portfolio Returns

Annualise: daily Sharpe × √252   |   monthly Sharpe × √12
```

<div class="ref-tags">
<span class="ref-tag">Sharpe ratio</span> <span class="ref-tag">Information ratio</span> <span class="ref-tag">Risk-free rate</span> <span class="ref-tag">Equity curve</span> <span class="ref-tag">Drawdown</span> <span class="ref-tag">Maximum drawdown</span>
</div>

---

## Section 5 — Transaction Costs

<div class="note-abstract">
Transaction costs do not merely reduce returns — they can completely invert a strategy's sign, turning an apparently exceptional strategy into a systematically losing one. The lesson is not a minor accounting adjustment; it is a structural warning that high-frequency strategies are fundamentally fragile. Costs must be modelled rigorously and upfront, not treated as an afterthought once the strategy looks attractive.
</div>

### Core ideas

<div class="key-idea"><strong>Transaction costs can completely invert a strategy's Sharpe sign.</strong> High trading frequency amplifies cost destruction multiplicatively. The Bollinger Band ES example: Sharpe +3.0 before costs → Sharpe −3.0 after just 1 basis point per trade.</div>

<div class="key-idea"><strong>All four cost components must be modelled — not just commission.</strong> Bid-ask spread, market impact, and slippage are systematically underestimated in published backtests and frequently larger than commission combined.</div>

<div class="key-idea"><strong>Limit orders save the spread but create opportunity cost.</strong> The choice between order types is a strategic decision with measurable consequences on both fill rate and per-trade profitability.</div>

### The four components of transaction cost

| Component | Definition | Typical size |
|---|---|---|
| Commission | Explicit broker fee per trade | Negligible with discount brokers |
| Bid-ask spread | Gap between bid and ask prices | ~5 bps one-way for S&P 500 stocks; ~1 bp for ES futures |
| Market impact | Your own order moves the price against you | Dominant cost for large/illiquid positions |
| Slippage | Difference between signal price and execution price | Average cost due to transmission delays |

### Strategy examples

<div class="example-block">
<div class="ex-title">ES Bollinger Band mean-reversion — Sharpe +3.0 to −3.0 <span class="ex-pill pill-warn">Failed live</span></div>

Buy when price falls more than 2 standard deviations below its moving average; short when it rises more than 2 standard deviations above. Exit at ±1 standard deviation. Entry and exit every 5 minutes throughout the trading day.

- Before transaction costs: Sharpe ≈ **+3.0** (excellent)
- After 1 basis point per trade (ES standard): Sharpe ≈ **−3.0** (deeply unprofitable)

The strategy's sign completely reverses with the addition of a single basis point per trade.
<div class="ex-lesson"><strong>Lesson:</strong> Any strategy with very high pre-cost Sharpe and very high trading frequency is unproven until full cost modelling is applied. The more trades per day, the more aggressive the cost drag.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Basis points</span> <span class="ref-tag">Bid-ask spread</span> <span class="ref-tag">Market impact</span> <span class="ref-tag">Slippage</span> <span class="ref-tag">Bollinger bands</span> <span class="ref-tag">Mean reversion</span>
</div>

---

## Section 6 — Data Biases

<div class="note-abstract">
The most dangerous backtesting errors are statistical biases that make a strategy appear profitable when it is not. Two distinct mechanisms are identified — survivorship bias (a data contamination problem) and data-snooping bias (a modelling problem) — both endemic and largely invisible to practitioners who do not actively look for them. Regime shifts extend the point further: even a well-constructed, bias-free backtest becomes unreliable when its historical window spans structurally different market conditions.
</div>

### Core ideas

<div class="key-idea"><strong>More data is not always better — regime-shifted data is actively misleading.</strong> Financial time series is non-stationary. Data from pre-decimalization or pre-crisis markets describes conditions that no longer apply.</div>

<div class="key-idea"><strong>Simple models generalise; complex models memorise.</strong> Data-snooping bias scales directly with the number of free parameters. Fewer parameters almost always produces more durable out-of-sample performance.</div>

<div class="key-idea"><strong>AI works in trading only on non-reflexive, private targets via metalabeling.</strong> Standard ML targets (market returns) change in response to being successfully predicted. Metalabeling predicts proprietary signal performance instead, avoiding that reflexivity problem.</div>

### Strategy examples

<div class="example-block">
<div class="ex-title">"Buy cheap" value strategy — survivorship bias inflates results <span class="ex-pill pill-warn">Cautionary</span></div>
Any strategy that tends to buy cheap stocks is especially vulnerable to survivorship bias. Some stocks were cheap precisely because the company was approaching bankruptcy and delisting. A database that excludes delisted stocks shows only the cases where cheap stocks survived and recovered — the failed cases, which a live trader would have held, are entirely absent. This is the clearest illustration of why point-in-time data matters most for value strategies (see Example 3.3 in the book for a quantified illustration).
<div class="ex-lesson"><strong>Lesson:</strong> Always ask whether a "buy cheap" backtest used point-in-time data. If not, the results are fundamentally unreliable.</div>
</div>

<div class="example-block">
<div class="ex-title">100-parameter model — data-snooping in practice <span class="ex-pill pill-warn">Cautionary</span></div>
A trading strategy built with 100 free parameters can almost certainly be optimised to produce a spectacular historical backtest. It is equally certain that its live performance will look nothing like the backtest. The model has fitted to historical accidents — random noise that will not repeat — rather than genuine market structure. Even a strategy with just 1–2 parameters (entry and exit thresholds) is susceptible, though less severely.
<div class="ex-lesson"><strong>Lesson:</strong> Treat every additional parameter as a cost paid in out-of-sample reliability. Simple models almost always generalise better.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Survivorship bias</span> <span class="ref-tag">Data-snooping bias</span> <span class="ref-tag">Look-ahead bias</span> <span class="ref-tag">Regime shift</span> <span class="ref-tag">Stationarity</span> <span class="ref-tag">Metalabeling</span>
</div>

---

## Section 7 — Pre-Backtest Screening Checklist

<div class="note-abstract">
The closing synthesis is a two-stage decision framework built on disciplined asymmetry: invest analytical effort only where the prior probability of success is already high. The checklist eliminates the majority of candidate strategies before any significant time is committed. Strategies that survive both stages are not guaranteed to be profitable, but they have cleared the conditions necessary to make full backtesting worthwhile rather than wasteful.
</div>

### Core ideas

<div class="key-idea"><strong>The independent trader's structural moat is low strategy capacity.</strong> Strategies too small, too frequent, or too illiquid for institutional capital are a durable competitive advantage — occupying niches that large funds cannot enter without destroying their own returns through market impact.</div>

<div class="key-idea"><strong>Eight filters before one backtest.</strong> Pre-screening is the correct sequence. Running a full backtest on a strategy that fails these filters wastes time and distorts judgment through sunk-cost effects.</div>

<div class="key-idea"><strong>Recent performance matters more than long-run average performance.</strong> A strategy with a stellar 15-year backtest dominated by its first 10 years is a decaying strategy, not a proven one.</div>

### Stage 1 — Personal fit (before evaluating the strategy)

- [ ] Does the strategy match your available working hours and automation level?
- [ ] Does it fit your programming skill level?
- [ ] Is it appropriate for your capital level and the instruments it grants access to?
- [ ] Does the holding period match your income frequency goal?

### Stage 2 — Strategy quality (pre-backtest triage)

- [ ] Does it beat its appropriate benchmark (index for long-only; risk-free rate for dollar-neutral)?
- [ ] Is the Sharpe ratio ≥ 1.0 (minimum) or ≥ 2.0 (monthly profitability target)?
- [ ] Is the maximum drawdown depth and duration within your personal tolerance?
- [ ] Have all four transaction cost components been realistically accounted for?
- [ ] Is the historical database free of survivorship bias?
- [ ] Is recent performance still strong, or has the strategy decayed?
- [ ] Does the strategy use few parameters (avoiding data-snooping bias)?
- [ ] Is the strategy's capacity too low for institutional capital — protecting it from competition?

---

## Term Glossary

A reference glossary of all financial terms introduced in Chapter 2:

<div class="glossary-entry">
<div class="gterm">Backtest / Backtesting <span class="gcat cat-data">Data</span></div>
Applying a trading strategy to historical data to simulate past performance. The primary validation tool before risking real capital. Reliability depends on data quality, realistic cost assumptions, and resistance to statistical biases. A backtest is an upper bound on future performance, not a prediction of it.
</div>

<div class="glossary-entry">
<div class="gterm">Bollinger bands <span class="gcat cat-data">Data</span></div>
A technical indicator: a moving average flanked by bands at ±N standard deviations. Mean-reversion use: short when price exceeds +2σ, buy when below −2σ, exit at ±1σ. Illustrates how high-frequency strategies are destroyed by minimal transaction costs.
</div>

<div class="glossary-entry">
<div class="gterm">Mean reversion <span class="gcat cat-data">Data</span></div>
The statistical tendency of a price, spread, or ratio to return toward its long-run average after deviating from it. Mean-reversion strategies profit by buying when something is cheap relative to history and selling when expensive. The conceptual opposite of momentum strategies.
</div>

<div class="glossary-entry">
<div class="gterm">PEAD — Post-Earnings Announcement Drift <span class="gcat cat-data">Data</span></div>
A documented market anomaly: stock prices continue drifting in the direction of an earnings surprise for weeks after announcement rather than adjusting immediately. Attributed to investor under-reaction. Contradicts the strong form of the Efficient Market Hypothesis.
</div>

<div class="glossary-entry">
<div class="gterm">Drawdown <span class="gcat cat-perf">Performance</span></div>
At time t, the difference between the portfolio's current value and its prior peak (the high watermark), expressed as a percentage. Drawdowns cause traders to abandon valid strategies at exactly the worst moment — at the trough.
</div>

<div class="glossary-entry">
<div class="gterm">Drawdown duration (maximum) <span class="gcat cat-perf">Performance</span></div>
The longest continuous period the equity curve remained below a prior high watermark. Does not necessarily coincide with the deepest drawdown. From Figure 2.1: ~20 months (Feb 2001 to Oct 2002).
</div>

<div class="glossary-entry">
<div class="gterm">Information ratio (IR) <span class="gcat cat-perf">Performance</span></div>
Risk-adjusted performance metric for long-only strategies. Average excess return over a market benchmark divided by the standard deviation of that excess return (tracking error). The Sharpe ratio is a special case where the benchmark is always the risk-free rate.
</div>

<div class="glossary-entry">
<div class="gterm">Risk-free rate <span class="gcat cat-perf">Performance</span></div>
The theoretical return on a zero-risk investment. Approximated by the 3-month US Treasury bill yield. Subtracted from portfolio returns in the Sharpe ratio formula.
</div>

<div class="glossary-entry">
<div class="gterm">Sharpe ratio <span class="gcat cat-perf">Performance</span></div>
The universal risk-adjusted return metric. Formula: (Avg Portfolio Return − Risk-Free Rate) ÷ Std Dev of Portfolio Returns. Annualise: daily × √252, monthly × √12. Benchmarks: &lt;1 = not viable; ≥1 = minimum; ≥2 = monthly profitability; ≥3 = daily profitability.
</div>

<div class="glossary-entry">
<div class="gterm">Dollar-neutral portfolio <span class="gcat cat-capital">Capital</span></div>
Portfolio where total long market value equals total short market value. Net dollar exposure = $0. Requires twice the capital of a directional portfolio for the same gross exposure.
</div>

<div class="glossary-entry">
<div class="gterm">Market-neutral portfolio <span class="gcat cat-capital">Capital</span></div>
A portfolio whose beta (sensitivity to the market index) is close to zero. Requires beta-weighting positions, not just dollar-matching.
</div>

<div class="glossary-entry">
<div class="gterm">NAV (net asset value) <span class="gcat cat-capital">Capital</span></div>
True equity in a trading account: cash + market value of long positions − market value of short positions − margin debt.
</div>


<div class="glossary-entry">
<div class="gterm">Regulation T (Reg T) <span class="gcat cat-capital">Capital</span></div>
The Federal Reserve rule governing broker credit for purchasing securities.
</div>

<div class="glossary-entry">
<div class="gterm">Statistical arbitrage <span class="gcat cat-inst">Instrument</span></div>
A family of quant strategies exploiting short-term pricing discrepancies between related securities, betting on reversion to their historical statistical relationship. Carries risk — the relationship may not hold on any individual trade even if it holds on average.
</div>

<div class="glossary-entry">
<div class="gterm">Strategy capacity <span class="gcat cat-capital">Capital</span></div>
The maximum capital a strategy can deploy before its own trading degrades returns through market impact.
</div>

<div class="glossary-entry">
<div class="gterm">Bid-ask spread <span class="gcat cat-cost">Cost</span></div>
Gap between the price buyers will pay (bid) and sellers will accept (ask).
</div>

<div class="glossary-entry">
<div class="gterm">Data-snooping bias (overfitting) <span class="gcat cat-bias">Bias</span></div>
A modelling error where excessive parameter optimisation causes the strategy to fit historical noise rather than genuine repeatable patterns. Severity scales with number of free parameters. Simple models generalise better; complex models memorise the past.
</div>

<div class="glossary-entry">
<div class="gterm">Look-ahead bias <span class="gcat cat-bias">Bias</span></div>
A backtesting error where information not yet available at a historical moment is inadvertently used in the trading decision.
</div>

<div class="glossary-entry">
<div class="gterm">Metalabeling <span class="gcat cat-bias">Bias</span></div>
An ML technique where a model predicts whether a proprietary trading signal will be profitable on a specific trade — rather than predicting market direction directly.
</div>

<div class="glossary-entry">
<div class="gterm">Survivorship bias <span class="gcat cat-bias">Bias</span></div>
A distortion in historical databases that include only stocks surviving to the present, omitting those that went bankrupt, were delisted, or merged. Especially dangerous for value-oriented (buy-cheap) strategies.
</div>
