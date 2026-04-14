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
There’s no shortage of trading ideas—they are everywhere, open, and free. The real difficulty is not finding them, but knowing which ones are worth your time before you even start backtesting. In that sense, trading is less about discovery and more about curation: filtering out noise and recognizing signal early.
</div>

### Core ideas

<div class="key-idea"><strong>Modification is the real alpha source.</strong> Public strategies are often just shared building blocks. The real edge comes from how they are adapted—through choices like holding period, asset selection, and timing. Most “secret” ideas are already widely known; what truly matters is the execution and how they are engineered.</div>

<div class="key-idea"><strong>Academic strategies are often outdated, overly complex, or constrained to small-cap universes.</strong> By the time a method is published in a journal, it may already be arbitraged away, require costly data to reproduce, or only work in illiquid markets where execution costs eliminate most of the theoretical edge.</div>

### Table 2.1 — Sources of trading ideas

The following sources are recommended for finding quantitative trading strategy ideas. Most are free or low-cost. The key caveat: treat all of them as *starting points for modification*, not ready-made strategies.

| Category | Source | URL |
|---|---|---|
| **Academic** | Business school finance professors' websites | [hbs.edu/research](https://www.hbs.edu/research/research.html) |
| | Social Science Research Network (SSRN) | [ssrn.com](https://www.ssrn.com) |
| | National Bureau of Economic Research (NBER) | [nber.org](https://www.nber.org) |
| | Quantitative finance seminars | [ieor.columbia.edu](https://www.ieor.columbia.edu/seminars/financialengineering) |
| | Quantpedia (aggregator of all academic quant papers) | [quantpedia.com](https://quantpedia.com) |
| **Blogs & podcasts** | Flirting with Models | [thinknewfound.com](https://www.thinknewfound.com) |
| | Mutiny Fund podcast | [mutinyfund.com/podcast](https://mutinyfund.com/podcast/) |
| | Chat with Traders | [chatwithtraders.com](https://chatwithtraders.com) |
| | Eran Raviv | [eranraviv.com](https://eranraviv.com) |
| | Party at the Moontower | [moontowermeta.com](https://moontowermeta.com) |
| | Ernest Chan's blog | [epchan.blogspot.com](https://epchan.blogspot.com) |
| **Trader forums** | Elite Trader | [elitetrader.com](https://www.Elitetrader.com) |
| | Wealth-Lab | [wealth-lab.com](https://www.wealth-lab.com) |
| **Twitter / X** | Benn Eifert | [@bennpeifert](https://twitter.com/bennpeifert) |
| | Corey Hoffstein | [@choffstein](https://twitter.com/choffstein) |
| | Quantocracy (aggregator of new quant articles) | [@Quantocracy](https://twitter.com/Quantocracy) |
| | Mike Harris | [@mikeharrisNY](https://twitter.com/mikeharrisNY) |
| | Euan Sinclair | [@sinclaireuan](https://twitter.com/sinclaireuan) |
| | Ernest Chan | [@chanep](https://twitter.com/chanep) |
| **Newspapers & magazines** | Stocks, Futures and Options magazine | [sfomag.com](https://www.sfomag.com) |

---

## Section 2 — Personal Fit

<div class="note-abstract">
A strategy is only as good as its fit with the trader’s personal constraints. Even the most theoretically strong strategy is useless if it cannot be executed, funded, or psychologically maintained. Before assessing any strategy on its merits, it is essential to first evaluate four dimensions—time, skill, capital, and objectives—to define what is actually feasible. Fit comes before merit.
</div>

### Core ideas

<div class="key-idea"><strong>Personal fit is assessed before analytical merit.</strong> A great strategy requiring full-time monitoring is not a great strategy for a part-time trader. Establish the feasible set first, then evaluate strategies within it.</div>

<div class="key-idea"><strong>Buy-and-hold is not necessarily optimal for long-term capital growth.</strong> In theory, higher growth can be achieved by identifying strategies with strong risk-adjusted returns and applying optimal leverage.</div>

<div class="key-idea"><strong>Trading frequency and income regularity are directly coupled.</strong> Generating consistent monthly income generally requires shorter holding periods. As holding periods increase, profit and loss become more volatile, making returns less predictable—even if the long-term average return is high.</div>

### Strategy examples

<div class="example-block">
<div class="ex-title">Short-term vs. long-term strategy — Sharpe comparison <span class="ex-pill pill-num">Conceptual</span></div>
A short-term strategy with a small annual return but very high Sharpe ratio is preferable to a long-term strategy with a high annual return but lower Sharpe ratio — even if the goal is long-term capital growth. Sharpe determines how aggressively leverage can be applied, and leveraged return is the true terminal wealth driver. A Sharpe 3.0 / 8% return strategy outperforms a Sharpe 0.8 / 25% return strategy once leverage is correctly sized.
<div class="ex-lesson"><strong>Lesson:</strong> Never compare strategies on nominal return alone. Always compare on Sharpe ratio, then apply leverage to the winner.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Sharpe ratio</span>
</div>

---

## Section 3 — Capital & Leverage

<div class="note-abstract">
Capital is more than just money—it sets the boundaries for everything else. It decides what markets you can trade, how much leverage you can use, what data you can realistically access, and which strategies are feasible in the first place. It’s less a preference and more a hard filter.
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
<div class="ref-tags">
<span class="ref-tag">ETF</span> <span class="ref-tag">Limit order</span> <span class="ref-tag">Intraday vs. overnight</span>
</div>
## Section 4 — Performance Measurement

<div class="note-abstract">
Raw returns are not the right primary metric for evaluating trading strategies. Even experienced practitioners sometimes focus on them incorrectly. The Sharpe ratio is more fundamental because it determines how much leverage can be applied safely. Ultimately, it is leveraged returns—not nominal returns—that drive long-term wealth.
</div>

### Core ideas

<div class="key-idea"><strong>Sharpe ratio, not return, is the master performance metric.</strong> A higher Sharpe means you can safely use more leverage, which ultimately drives wealth growth. With optimal leverage, a low-return but high-Sharpe strategy can easily beat a high-return but low-Sharpe one.</div>

<div class="key-idea"><strong>Drawdown is the metric that determines psychological survivability.</strong> Drawdowns cause traders to abandon valid strategies at the worst possible moment. Drawdown tolerance must be calibrated honestly before a strategy is selected, not after.</div>

<div class="key-idea"><strong>Trading frequency is a leading indicator of Sharpe ratio.</strong> Strategies trading only a few times per year almost certainly have low Sharpe. Deep drawdowns (>10%, >4 months) signal low Sharpe before any calculation is needed.</div>

### Sharpe ratio benchmarks

| Sharpe ratio | Interpretation | Viability |
|---|---|---|
| < 1.0 | High volatility relative to returns | Not viable as standalone |
| ≥ 1.0 | Minimum acceptable threshold | Borderline |
| ≥ 2.0 | Profitable almost every month | Good |
| ≥ 3.0 | Profitable almost every day | Excellent |

**Formula:**

$$\text{Sharpe Ratio} = \frac{\text{Avg Portfolio Return} - \text{Risk-Free Rate}}{\text{Std Dev of Portfolio Returns}}$$

**Annualization:**

$$\text{Daily Sharpe} \times \sqrt{252} \quad \text{or} \quad \text{Monthly Sharpe} \times \sqrt{12}$$

<div class="ref-tags">
<span class="ref-tag">Sharpe ratio</span> <span class="ref-tag">Information ratio</span> <span class="ref-tag">Risk-free rate</span> <span class="ref-tag">Equity curve</span> <span class="ref-tag">Drawdown</span> <span class="ref-tag">Maximum drawdown</span>
</div>

---

## Section 5 — Transaction Costs

<div class="note-abstract">
Trading costs are not just a drag on performance—they can completely flip a strategy from profitable to unprofitable. A strategy that looks excellent on paper can fail once costs are included. This is a fundamental warning: high-frequency strategies are especially sensitive and fragile. Costs need to be built into the model from the beginning.
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
The biggest risk in backtesting is statistical bias, which can make a bad strategy look good. Two major issues are survivorship bias, where the dataset itself is distorted, and data-snooping bias, where repeated testing leads to overfitting. These problems are widespread and often invisible without careful checks. On top of that, changing market regimes mean that even clean backtests may not hold up when conditions in the future differ from the past.
</div>

### Core ideas

<div class="key-idea"><strong>More data is not always better — regime-shifted data is actively misleading.</strong> Financial time series is non-stationary. Data from pre-decimalization or pre-crisis markets describes conditions that no longer apply.</div>

<div class="key-idea"><strong>Simple models tend to generalize better, while complex models are more likely to memorize patterns in the data.</strong> Data-snooping bias increases with the number of free parameters. In practice, models with fewer parameters are usually more robust and deliver more stable out-of-sample performance.</div>

<div class="key-idea"><strong>AI is effective in trading only when applied to non-reflexive, private targets through meta-labeling. </strong> Standard ML targets (market returns) change in response to being successfully predicted. Metalabeling predicts proprietary signal performance instead, avoiding that reflexivity problem.</div>

### Strategy examples

<div class="example-block">
<div class="ex-title">"Buy cheap" value strategy — survivorship bias inflates results <span class="ex-pill pill-warn">Cautionary</span></div>
Any strategy that tends to buy cheap stocks is especially vulnerable to survivorship bias. Some stocks were cheap precisely because the company was approaching bankruptcy and delisting. A database that excludes delisted stocks shows only the cases where cheap stocks survived and recovered — the failed cases, which a live trader would have held, are entirely absent.
<div class="ex-lesson"><strong>Lesson:</strong> Always ask whether a "buy cheap" backtest used point-in-time data. If not, the results are fundamentally unreliable.</div>
</div>

<div class="example-block">
<div class="ex-title">100-parameter model — data-snooping in practice <span class="ex-pill pill-warn">Cautionary</span></div>
A trading strategy built with 100 free parameters can almost certainly be optimised to produce a spectacular historical backtest. It is equally certain that its live performance will look nothing like the backtest. The model has fitted to historical accidents — random noise that will not repeat — rather than genuine market structure.
<div class="ex-lesson"><strong>Lesson:</strong> Treat every additional parameter as a cost paid in out-of-sample reliability. Simple models almost always generalise better.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Survivorship bias</span> <span class="ref-tag">Data-snooping bias</span> <span class="ref-tag">Look-ahead bias</span> <span class="ref-tag">Regime shift</span> <span class="ref-tag">Stationarity</span> <span class="ref-tag">Metalabeling</span>
</div>

---

## Section 7 — Pre-Backtest Screening Checklist

<div class="note-abstract">
The final framework is a two-stage decision process based on disciplined asymmetry: only invest analytical effort when the prior probability of success is already high. The checklist serves to eliminate most candidate strategies before any significant time is spent. Strategies that pass both stages are not guaranteed to be profitable, but they are sufficiently promising to justify full backtesting rather than wasteful exploration.
</div>

### Core ideas

<div class="key-idea"><strong>The independent trader's structural moat is low strategy capacity.</strong> Strategies too small, too frequent, or too illiquid for institutional capital are a durable competitive advantage. These areas can become a lasting advantage for smaller players, because large funds cannot enter without pushing prices against themselves.</div>

<div class="key-idea"><strong>You should apply a set of filters before doing any full backtest.</strong> This pre-screening step saves time and prevents you from getting emotionally attached to weak ideas. Without it, you risk wasting effort and being influenced by sunk-cost bias.</div>

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

A reference glossary of financial terms:

<div class="glossary-entry">
<div class="gterm">Backtest / Backtesting <span class="gcat cat-data">Data</span></div>
Applying a trading strategy to historical data to simulate past performance. A backtest is an upper bound on future performance, not a prediction of it.
</div>

<div class="glossary-entry">
<div class="gterm">Bollinger bands <span class="gcat cat-data">Data</span></div>
A technical indicator: a moving average flanked by bands at ±N standard deviations. Mean-reversion use: short when price exceeds +2σ, buy when below −2σ, exit at ±1σ.
</div>

<div class="glossary-entry">
<div class="gterm">PEAD — Post-Earnings Announcement Drift <span class="gcat cat-data">Data</span></div>
A documented market anomaly: stock prices continue drifting in the direction of an earnings surprise for weeks after announcement rather than adjusting immediately. Attributed to investor under-reaction.
</div>

<div class="glossary-entry">
<div class="gterm">Drawdown <span class="gcat cat-perf">Performance</span></div>
At time t, the difference between the portfolio's current value and its prior peak (the high watermark), expressed as a percentage. Drawdowns cause traders to abandon valid strategies at exactly the worst moment.
</div>

<div class="glossary-entry">
<div class="gterm">Drawdown duration (maximum) <span class="gcat cat-perf">Performance</span></div>
The longest continuous period the equity curve remained below a prior high watermark.
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
Portfolio where total long market value equals total short market value. Net dollar exposure = $0.
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
A modelling error where excessive parameter optimisation causes the strategy to fit historical noise rather than genuine repeatable patterns.
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
A distortion in historical databases that include only stocks surviving to the present, omitting those that went bankrupt, were delisted, or merged.
</div>
