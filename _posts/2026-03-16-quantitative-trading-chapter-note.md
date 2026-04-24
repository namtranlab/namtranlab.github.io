---
layout: distill
title: "Quantitative Trading — Complete Study Notes (Ch. 2, 3, 5, 6, 7)"
description: Combined study notes for Chapters 2, 3, 5, 6, and 7 of Quantitative Trading (2nd Ed.) by Ernest P. Chan. Each chapter is collapsible — click any chapter title to expand or collapse it.
tags: Finance Quant Trading Notes
giscus_comments: true
date: 2026-03-16
featured: true
thumbnail: https://m.media-amazon.com/images/I/51s4givoDeL._SY445_SX342_ML2_.jpg

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Chapter 2 — Fishing for Ideas
  - name: Chapter 3 — Backtesting
  - name: Chapter 5 — Execution Systems
  - name: Chapter 6 — Money and Risk Management
  - name: Chapter 7 — Special Topics

_styles: >
  /* ── Collapsible chapter blocks ── */
  .chapter-block { margin-bottom: 1.5rem; border: 0.5px solid #e0e0e0; border-radius: 10px; overflow: hidden; }
  .chapter-toggle { width: 100%; background: #f0f4ff; border: none; cursor: pointer; padding: 1rem 1.25rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; text-align: left; border-radius: 0; }
  .chapter-toggle:hover { background: #e4eaff; }
  .chapter-toggle-left { display: flex; align-items: center; gap: 0.75rem; }
  .chapter-badge { font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; background: #5b7de8; color: #fff; padding: 2px 9px; border-radius: 20px; flex-shrink: 0; }
  .chapter-title { font-size: 1rem; font-weight: 600; color: #1a1a2e; }
  .chapter-subtitle { font-size: 0.78rem; color: #666; margin-top: 1px; }
  .chapter-arrow { font-size: 1rem; color: #5b7de8; flex-shrink: 0; transition: transform 0.25s ease; display: inline-block; }
  .chapter-arrow.open { transform: rotate(180deg); }
  .chapter-body { display: none; padding: 1.25rem 1.5rem 1.5rem; border-top: 0.5px solid #e0e0e0; }
  .chapter-body.open { display: block; }
  /* ── Shared content styles ── */
  .note-abstract { background: #f0f4ff; border-left: 4px solid #5b7de8; padding: 0.9rem 1.1rem; margin: 1rem 0 1.5rem 0; border-radius: 0 6px 6px 0; font-style: italic; color: #333; }
  .example-block { background: #f8f8f8; border: 1px solid #e0e0e0; border-radius: 6px; padding: 0.85rem 1.1rem; margin: 0.75rem 0; }
  .example-block .ex-title { font-weight: 600; font-size: 0.9rem; margin-bottom: 0.4rem; color: #1a1a2e; }
  .example-block .ex-pill { display: inline-block; font-size: 0.72rem; font-weight: 600; padding: 1px 8px; border-radius: 20px; margin-left: 6px; vertical-align: middle; }
  .pill-live { background: #d4edda; color: #155724; }
  .pill-warn { background: #fce8e6; color: #7f1d1d; }
  .pill-num  { background: #ede8fc; color: #3c2a8a; }
  .pill-code { background: #e2f0fb; color: #0c4a7c; }
  .pill-tip  { background: #fff3cd; color: #856404; }
  .pill-puzzle { background: #fff3cd; color: #856404; }
  .example-block .ex-lesson { margin-top: 0.5rem; font-size: 0.85rem; color: #555; border-top: 1px solid #ddd; padding-top: 0.4rem; }
  .key-idea { padding: 0.3rem 0; border-bottom: 1px dotted #ddd; margin-bottom: 0.4rem; }
  .key-idea:last-child { border-bottom: none; }
  .glossary-entry { border-bottom: 1px solid #eee; padding: 0.7rem 0; }
  .glossary-entry:last-child { border-bottom: none; }
  .glossary-entry .gterm { font-weight: 600; font-size: 0.95rem; margin-bottom: 0.25rem; }
  .glossary-entry .gcat { display: inline-block; font-size: 0.7rem; font-weight: 600; padding: 1px 7px; border-radius: 20px; margin-left: 6px; vertical-align: middle; }
  .cat-data     { background: #dbeafe; color: #1e3a8a; }
  .cat-risk     { background: #fce8e6; color: #7f1d1d; }
  .cat-perf     { background: #fef3c7; color: #78350f; }
  .cat-capital  { background: #d1fae5; color: #064e3b; }
  .cat-inst     { background: #ede8fc; color: #3c2a8a; }
  .cat-bias     { background: #dcfce7; color: #14532d; }
  .cat-cost     { background: #fce7f3; color: #831843; }
  .cat-system   { background: #d1fae5; color: #064e3b; }
  .cat-market   { background: #dbeafe; color: #1e3a8a; }
  .cat-method   { background: #ede8fc; color: #3c2a8a; }
  .cat-platform { background: #d1fae5; color: #064e3b; }
  .cat-kelly    { background: #d1fae5; color: #064e3b; }
  .cat-psych    { background: #ede8fc; color: #3c2a8a; }
  .cat-strategy { background: #d1fae5; color: #064e3b; }
  .cat-stats    { background: #dbeafe; color: #1e3a8a; }
  .cat-model    { background: #fef3c7; color: #78350f; }
  .cat-exit     { background: #fce7f3; color: #831843; }
  .cat-seasonal { background: #ede8fc; color: #3c2a8a; }
  .cat-hft      { background: #dcfce7; color: #14532d; }
  .quote-block { background: #f9fafb; border-radius: 6px; padding: 0.75rem 1rem; margin-top: 1rem; font-style: italic; color: #444; font-size: 0.9rem; }
  .result-box { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 6px; padding: 0.6rem 1rem; margin: 0.5rem 0; font-size: 0.88rem; }
  .result-box strong { color: #276749; }
  .warning-box { background: #fff8e1; border: 1px solid #ffe082; border-radius: 6px; padding: 0.75rem 1rem; margin: 0.75rem 0; font-size: 0.88rem; color: #5d4037; }
  .warning-box strong { color: #e65100; }
  .ref-tags { margin-top: 1rem; }
  .ref-tag { display: inline-block; font-size: 0.72rem; padding: 2px 8px; border-radius: 20px; border: 1px solid #ccc; color: #666; margin: 2px 3px 2px 0; }
  .checklist { list-style: none; padding: 0; margin: 0.5rem 0; }
  .checklist li { padding: 0.3rem 0; font-size: 0.9rem; color: #333; border-bottom: 1px dotted #eee; display: flex; align-items: flex-start; gap: 0.5rem; }
  .checklist li:last-child { border-bottom: none; }
  .checklist li::before { content: "→"; color: #5b7de8; flex-shrink: 0; }
  table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.88rem; }
  th { background: #f0f4ff; text-align: left; padding: 7px 10px; border: 1px solid #ddd; }
  td { padding: 7px 10px; border: 1px solid #ddd; vertical-align: top; }

---

> **Book:** *Quantitative Trading* (2nd Ed.) — Ernest P. Chan
>
> This page combines study notes for Chapters 2, 3, 5, 6, and 7. Each chapter is **collapsed by default** — click a chapter title to expand or collapse it.

<script>
function toggleChapter(id) {
  var body = document.getElementById(id + '-body');
  var arrow = document.getElementById(id + '-arrow');
  var isOpen = body.classList.contains('open');
  body.classList.toggle('open', !isOpen);
  arrow.classList.toggle('open', !isOpen);
}
</script>


## Chapter 2 — Fishing for Ideas

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('ch2')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">Chapter 2</span>
      <div>
        <div class="chapter-title">Chapter 2 — Fishing for Ideas</div>
        <div class="chapter-subtitle">Where to find strategies, how to filter them, and what makes one worth backtesting</div>
      </div>
    </div>
    <span class="chapter-arrow" id="ch2-arrow">▼</span>
  </button>
  <div class="chapter-body" id="ch2-body">

### Section 1 — Core Thesis & Idea Sources

<div class="note-abstract">
There’s no shortage of trading ideas—they are everywhere, open, and free. The real difficulty is not finding them, but knowing which ones are worth your time before you even start backtesting. In that sense, trading is less about discovery and more about curation: filtering out noise and recognizing signal early.
</div>

#### Core ideas

<div class="key-idea"><strong>Modification is the real alpha source.</strong> Public strategies are often just shared building blocks. The real edge comes from how they are adapted—through choices like holding period, asset selection, and timing. Most “secret” ideas are already widely known; what truly matters is the execution and how they are engineered.</div>

<div class="key-idea"><strong>Academic strategies are often outdated, overly complex, or constrained to small-cap universes.</strong> By the time a method is published in a journal, it may already be arbitraged away, require costly data to reproduce, or only work in illiquid markets where execution costs eliminate most of the theoretical edge.</div>

#### Table 2.1 — Sources of trading ideas

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

### Section 2 — Personal Fit

<div class="note-abstract">
A strategy is only as good as its fit with the trader’s personal constraints. Even the most theoretically strong strategy is useless if it cannot be executed, funded, or psychologically maintained. Before assessing any strategy on its merits, it is essential to first evaluate four dimensions—time, skill, capital, and objectives—to define what is actually feasible. Fit comes before merit.
</div>

#### Core ideas

<div class="key-idea"><strong>Personal fit is assessed before analytical merit.</strong> A great strategy requiring full-time monitoring is not a great strategy for a part-time trader. Establish the feasible set first, then evaluate strategies within it.</div>

<div class="key-idea"><strong>Buy-and-hold is not necessarily optimal for long-term capital growth.</strong> In theory, higher growth can be achieved by identifying strategies with strong risk-adjusted returns and applying optimal leverage.</div>

<div class="key-idea"><strong>Trading frequency and income regularity are directly coupled.</strong> Generating consistent monthly income generally requires shorter holding periods. As holding periods increase, profit and loss become more volatile, making returns less predictable—even if the long-term average return is high.</div>

#### Strategy examples

<div class="example-block">
<div class="ex-title">Short-term vs. long-term strategy — Sharpe comparison <span class="ex-pill pill-num">Conceptual</span></div>
A short-term strategy with a small annual return but very high Sharpe ratio is preferable to a long-term strategy with a high annual return but lower Sharpe ratio — even if the goal is long-term capital growth. Sharpe determines how aggressively leverage can be applied, and leveraged return is the true terminal wealth driver. A Sharpe 3.0 / 8% return strategy outperforms a Sharpe 0.8 / 25% return strategy once leverage is correctly sized.
<div class="ex-lesson"><strong>Lesson:</strong> Never compare strategies on nominal return alone. Always compare on Sharpe ratio, then apply leverage to the winner.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Sharpe ratio</span>
</div>

---

### Section 3 — Capital & Leverage

<div class="note-abstract">
Capital is more than just money—it sets the boundaries for everything else. It decides what markets you can trade, how much leverage you can use, what data you can realistically access, and which strategies are feasible in the first place. It’s less a preference and more a hard filter.
</div>

#### Core ideas

<div class="key-idea"><strong>Capital determines the feasible strategy universe more than skill does.</strong> Different capital levels open structurally different strategy spaces across instruments, leverage, and data quality.</div>

<div class="key-idea"><strong>Low-capital traders should use futures, FX, and options — not stocks.</strong> The leverage embedded in these instruments compensates for limited capital in ways that direct stock ownership cannot.</div>

<div class="key-idea"><strong>Dollar-neutral portfolios require double the capital for the same gross exposure.</strong> This arithmetic constraint makes market-neutral strategies inaccessible without portfolio margin at ~$100K minimum NAV.</div>

#### Capital constraint decision table

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
### Section 4 — Performance Measurement

<div class="note-abstract">
Raw returns are not the right primary metric for evaluating trading strategies. Even experienced practitioners sometimes focus on them incorrectly. The Sharpe ratio is more fundamental because it determines how much leverage can be applied safely. Ultimately, it is leveraged returns—not nominal returns—that drive long-term wealth.
</div>

#### Core ideas

<div class="key-idea"><strong>Sharpe ratio, not return, is the master performance metric.</strong> A higher Sharpe means you can safely use more leverage, which ultimately drives wealth growth. With optimal leverage, a low-return but high-Sharpe strategy can easily beat a high-return but low-Sharpe one.</div>

<div class="key-idea"><strong>Drawdown is the metric that determines psychological survivability.</strong> Drawdowns cause traders to abandon valid strategies at the worst possible moment. Drawdown tolerance must be calibrated honestly before a strategy is selected, not after.</div>

<div class="key-idea"><strong>Trading frequency is a leading indicator of Sharpe ratio.</strong> Strategies trading only a few times per year almost certainly have low Sharpe. Deep drawdowns (>10%, >4 months) signal low Sharpe before any calculation is needed.</div>

#### Sharpe ratio benchmarks

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

### Section 5 — Transaction Costs

<div class="note-abstract">
Trading costs are not just a drag on performance—they can completely flip a strategy from profitable to unprofitable. A strategy that looks excellent on paper can fail once costs are included. This is a fundamental warning: high-frequency strategies are especially sensitive and fragile. Costs need to be built into the model from the beginning.
</div>

#### Core ideas

<div class="key-idea"><strong>Transaction costs can completely invert a strategy's Sharpe sign.</strong> High trading frequency amplifies cost destruction multiplicatively. The Bollinger Band ES example: Sharpe +3.0 before costs → Sharpe −3.0 after just 1 basis point per trade.</div>

<div class="key-idea"><strong>All four cost components must be modelled — not just commission.</strong> Bid-ask spread, market impact, and slippage are systematically underestimated in published backtests and frequently larger than commission combined.</div>

<div class="key-idea"><strong>Limit orders save the spread but create opportunity cost.</strong> The choice between order types is a strategic decision with measurable consequences on both fill rate and per-trade profitability.</div>

#### The four components of transaction cost

| Component | Definition | Typical size |
|---|---|---|
| Commission | Explicit broker fee per trade | Negligible with discount brokers |
| Bid-ask spread | Gap between bid and ask prices | ~5 bps one-way for S&P 500 stocks; ~1 bp for ES futures |
| Market impact | Your own order moves the price against you | Dominant cost for large/illiquid positions |
| Slippage | Difference between signal price and execution price | Average cost due to transmission delays |

#### Strategy examples

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

### Section 6 — Data Biases

<div class="note-abstract">
The biggest risk in backtesting is statistical bias, which can make a bad strategy look good. Two major issues are survivorship bias, where the dataset itself is distorted, and data-snooping bias, where repeated testing leads to overfitting. These problems are widespread and often invisible without careful checks. On top of that, changing market regimes mean that even clean backtests may not hold up when conditions in the future differ from the past.
</div>

#### Core ideas

<div class="key-idea"><strong>More data is not always better — regime-shifted data is actively misleading.</strong> Financial time series is non-stationary. Data from pre-decimalization or pre-crisis markets describes conditions that no longer apply.</div>

<div class="key-idea"><strong>Simple models tend to generalize better, while complex models are more likely to memorize patterns in the data.</strong> Data-snooping bias increases with the number of free parameters. In practice, models with fewer parameters are usually more robust and deliver more stable out-of-sample performance.</div>

<div class="key-idea"><strong>AI is effective in trading only when applied to non-reflexive, private targets through meta-labeling. </strong> Standard ML targets (market returns) change in response to being successfully predicted. Metalabeling predicts proprietary signal performance instead, avoiding that reflexivity problem.</div>

#### Strategy examples

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

### Section 7 — Pre-Backtest Screening Checklist

<div class="note-abstract">
The final framework is a two-stage decision process based on disciplined asymmetry: only invest analytical effort when the prior probability of success is already high. The checklist serves to eliminate most candidate strategies before any significant time is spent. Strategies that pass both stages are not guaranteed to be profitable, but they are sufficiently promising to justify full backtesting rather than wasteful exploration.
</div>

#### Core ideas

<div class="key-idea"><strong>The independent trader's structural moat is low strategy capacity.</strong> Strategies too small, too frequent, or too illiquid for institutional capital are a durable competitive advantage. These areas can become a lasting advantage for smaller players, because large funds cannot enter without pushing prices against themselves.</div>

<div class="key-idea"><strong>You should apply a set of filters before doing any full backtest.</strong> This pre-screening step saves time and prevents you from getting emotionally attached to weak ideas. Without it, you risk wasting effort and being influenced by sunk-cost bias.</div>

<div class="key-idea"><strong>Recent performance matters more than long-run average performance.</strong> A strategy with a stellar 15-year backtest dominated by its first 10 years is a decaying strategy, not a proven one.</div>

#### Stage 1 — Personal fit (before evaluating the strategy)

- [ ] Does the strategy match your available working hours and automation level?
- [ ] Does it fit your programming skill level?
- [ ] Is it appropriate for your capital level and the instruments it grants access to?
- [ ] Does the holding period match your income frequency goal?

#### Stage 2 — Strategy quality (pre-backtest triage)

- [ ] Does it beat its appropriate benchmark (index for long-only; risk-free rate for dollar-neutral)?
- [ ] Is the Sharpe ratio ≥ 1.0 (minimum) or ≥ 2.0 (monthly profitability target)?
- [ ] Is the maximum drawdown depth and duration within your personal tolerance?
- [ ] Have all four transaction cost components been realistically accounted for?
- [ ] Is the historical database free of survivorship bias?
- [ ] Is recent performance still strong, or has the strategy decayed?
- [ ] Does the strategy use few parameters (avoiding data-snooping bias)?
- [ ] Is the strategy's capacity too low for institutional capital — protecting it from competition?

---

### Term Glossary

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

  </div>
</div>


## Chapter 3 — Backtesting

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('ch3')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">Chapter 3</span>
      <div>
        <div class="chapter-title">Chapter 3 — Backtesting</div>
        <div class="chapter-subtitle">Platforms, historical data, performance measurement, pitfalls, and worked examples</div>
      </div>
    </div>
    <span class="chapter-arrow" id="ch3-arrow">▼</span>
  </button>
  <div class="chapter-body" id="ch3-body">

### Section 1 — What Is Backtesting and Why Should You Do It Yourself?

<div class="note-abstract">
Backtesting is simply running a trading strategy on historical data to see how it would have done in the past. Think of it like a practice exam before the real test. Even if someone hands you a strategy with all the details and historical results already written up, you should still run it yourself — because doing so forces you to truly understand it, catch any hidden mistakes, and spot ways to make it even better.
</div>

#### Core ideas

<div class="key-idea"><strong>Running it yourself is the proof that you understand it.</strong> If you cannot reproduce someone else's backtest results step by step, you do not really understand the strategy well enough to bet real money on it. The process of replication forces you to confront every assumption and decision.</div>

<div class="key-idea"><strong>Other people make mistakes — and you need to catch them.</strong> Published strategies can contain hidden errors like using tomorrow's data to make today's trade decisions. These mistakes are invisible in a write-up but jump out when you actually build the code and run it yourself.</div>

<div class="key-idea"><strong>Your own backtest opens the door to improvements.</strong> Once you can reproduce a strategy, you can start tweaking it — try a different entry time, a different set of stocks, a different holding period. Often these small tweaks turn a mediocre strategy into a great one.</div>

---

### Section 2 — Which Tool Should You Use?

<div class="note-abstract">
Picking the right tool for backtesting matters more than most people think. It is not just about personal preference — the tool you choose determines what kinds of mistakes you are likely to make, how fast you can test ideas, and how complex a strategy you can realistically build. The best tool is the simplest one that can handle your strategy.
</div>

#### Core ideas

<div class="key-idea"><strong>Simpler tools force simpler strategies — and that is often a good thing.</strong> Excel shows you everything on screen at once, which makes it almost impossible to accidentally use tomorrow's data in today's trading decision. Its limitation to simpler models is actually a safety feature.</div>

<div class="key-idea"><strong>MATLAB is still the best choice for serious quant research, despite Python's popularity.</strong> It runs faster, has better built-in statistics tools, and comes with real customer support. Python is free and widely used, but its packages frequently conflict with each other, it is slower, and there is no one to call when something breaks.</div>

<div class="key-idea"><strong>Web platforms like QuantConnect and Blueshift solve the data problem for you.</strong> These platforms come bundled with years of historical data and let you switch from backtesting to live trading without rewriting any code — which is a big deal, because a lot can go wrong in that translation.</div>

#### Choosing the right tool for you

| Tool | Good for | Best thing about it | Watch out for |
|---|---|---|---|
| **Excel** | Simple daily strategies, part-time traders | Everything visible on screen — very hard to make hidden mistakes | Cannot handle hundreds of stocks or complex models |
| **MATLAB** | Serious quant research, large stock universes | Fast, powerful statistics, real customer support | Costs money (home version is affordable though) |
| **Python** | Building production systems, using machine learning | Free, huge library of add-ons, most popular in industry | Packages often break each other; slower than MATLAB; no support |
| **R** | Classical statistics and econometrics | Best statistical packages available anywhere | Weaker machine learning support; basic interface |
| **QuantConnect** | Research all the way through to live trading | 400TB of data included; Python or C#; backtest and live trading use identical code | Requires programming knowledge |
| **Blueshift** | Python users who want data and backtesting in one place | Free minute-by-minute data; also has a no-code visual builder | Fewer markets than QuantConnect |

---

### Section 3 — Where Do You Get Historical Data?

<div class="note-abstract">
Getting historical data is the easy part — the internet is full of free sources. The hard part is understanding what problems are hiding inside that data. Three issues silently ruin most backtests: prices that have not been corrected for stock splits or dividends, databases that are missing stocks that went bankrupt, and noisy daily high and low prices that are less reliable than they look.
</div>

#### Core ideas

<div class="key-idea"><strong>Always use prices that have been adjusted for stock splits and dividends.</strong> When a company splits its stock 2-for-1, the price drops by half overnight — but nothing actually changed for shareholders. If your data is not adjusted, your backtest sees a huge fake price drop and generates a false buy signal.</div>

<div class="key-idea"><strong>Databases that are missing bankrupt companies make strategies look much better than they really are.</strong> If your database only includes stocks that are still trading today, you are missing all the ones that went bust. A "buy cheap" strategy looks amazing in this kind of biased data — because you never see the cheap stocks that went to zero. This is called survivorship bias.</div>

<div class="key-idea"><strong>Daily high and low prices are unreliable — stick to open and close wherever possible.</strong> The day's high or low is often set by a single tiny trade, a data entry error, or a trade on a different exchange. Any strategy that assumes you can buy at exactly the daily low or sell at exactly the daily high will look better in backtest than it ever will in real trading.</div>

#### Table 3.1 — Where to find historical data

| Source | What it covers | Good things | Problems |
|---|---|---|---|
| [finance.yahoo.com](https://finance.yahoo.com) | Daily stocks | Free; already adjusted for splits and dividends | Missing bankrupt stocks (survivorship bias); can only download one stock at a time |
| [Sharadar.com](https://sharadar.com) | Daily stocks | Includes delisted stocks — no survivorship bias | Paid subscription |
| [Algoseek.com](https://algoseek.com) | Stocks, futures, tick-by-tick data | Rent the data instead of buying it; very detailed | Moderately expensive |
| [CSIdata.com](https://csidata.com) | Daily stocks and futures | Cheap; can download many stocks at once | Has survivorship bias (delisted history can be bought separately) |
| [CRSP.com](https://crsp.com) | Daily stocks | No survivorship bias; very clean data | Expensive; only updated once a month |
| [Tickdata.com](https://tickdata.com) | Tick-by-tick stocks and futures | Institutional-grade quality | Expensive |
| Interactive Brokers | Forex data | Free if you already have an IB account | Need an IB account first |


<div class="ref-tags">
<span class="ref-tag">Survivorship bias</span> <span class="ref-tag">Split adjustment</span> <span class="ref-tag">Dividend adjustment</span> <span class="ref-tag">Point-in-time data</span>
</div>

---

### Section 4 — How Do You Measure If a Strategy Is Good?

<div class="note-abstract">
Most people judge a trading strategy by how much money it made. But raw returns are misleading because they do not tell you how much risk was taken to earn them. A strategy that made 20% by putting everything on one risky bet is far worse than one that made 15% through smooth, consistent gains. The Sharpe ratio, maximum drawdown, and MAR ratio together give you a much more honest and complete picture.
</div>

#### Core ideas

<div class="key-idea"><strong>The Sharpe ratio tells you how much you are earning per unit of risk taken.</strong> Think of it as asking: "How smooth and consistent were your gains?" A high Sharpe ratio means you made money reliably without wild swings. A low Sharpe ratio means the returns were bumpy and unreliable. Anything below 1 generally means the strategy is not worth running on its own.</div>

<div class="key-idea"><strong>For a fully hedged long–short strategy, you don’t need to subtract the risk-free rate.</strong> The short side pays for the long side, so the portfolio is basically self-funded. In that case, you can compute Sharpe using the raw strategy returns.</div>

<div class="key-idea"><strong>Scaling a Sharpe ratio to an annual number uses the square root, not a simple multiplication.</strong> You cannot just multiply a daily Sharpe by 252 trading days. You multiply by the square root of 252 (about 15.87). This is because risk does not grow in a straight line with time — it grows more slowly. Getting this wrong is a common mistake even among experienced traders.</div>

#### The Sharpe ratio formula

$$\text{Sharpe ratio} = \frac{\text{Average return} - \text{Risk-free rate}}{\text{Standard deviation of returns}}$$

**Annualization:**
- Daily returns: multiply by $\sqrt{252}$ (≈ 15.87)
- Monthly returns: multiply by $\sqrt{12}$ (≈ 3.46)
- Hourly returns: multiply by $\sqrt{1638}$ (252 trading days × 6.5 trading hours per day)

⚠️ **Common mistake:** using $252 \times 24 = 6,048$ for hourly data. Only count actual trading hours (6.5 hours per NYSE day), not all 24 hours.

#### The MAR ratio — a quick gut-check

$$\text{MAR ratio} = \frac{\text{Annual growth rate}}{\text{Maximum drawdown}}$$

**Example:** Strategy grows 20% per year and the worst loss from peak was 40%
$$\text{MAR ratio} = \frac{20\%}{40\%} = 0.5$$

Higher is better. Useful because it roughly cancels out leverage effects, making it easier to compare strategies with different risk levels.

<div class="ref-tags">
<span class="ref-tag">Sharpe ratio</span> <span class="ref-tag">MAR ratio</span> <span class="ref-tag">Maximum drawdown</span> <span class="ref-tag">Drawdown duration</span> <span class="ref-tag">High watermark</span>
</div>

---

### Section 5 — What Are the Most Common Mistakes?

<div class="note-abstract">
The frustrating thing about backtesting mistakes is that they almost always make a strategy look better than it really is. The two biggest culprits are accidentally using future information to make past trading decisions (look-ahead bias), and tuning a model so precisely to historical patterns that it stops working on new data (data-snooping bias). Both are sneaky, both are common, and both have practical tests that can catch them.
</div>

#### Core ideas

<div class="key-idea"><strong>Look-ahead bias means your backtest accidentally used information that was not yet available at the time of the trade.</strong> A simple example: your entry rule says "buy if today's price is within 1% of today's lowest price." But you cannot know what today's lowest price is until the market closes! Using that information to make a trade decision earlier in the day is cheating — and it makes the backtest look better than it ever could in real life.</div>

<div class="key-idea"><strong>There is a simple test to catch look-ahead bias: chop off the end of your data and see if anything changes.</strong> Run your full backtest and save the trading positions. Then delete the most recent 60 days of data and run it again. Compare the positions for the overlapping period. If they differ even slightly, your program is peeking at future data — you have look-ahead bias to fix.</div>

<div class="key-idea"><strong>Data-snooping bias is what happens when you tune a strategy too precisely to the past.</strong> Imagine testing 500 different combinations of settings until you find one that looks incredible on your historical data. Almost certainly, that "incredible" result is just a coincidence — you found the settings that happened to fit historical noise, not a real market pattern. The golden rule: use no more than 5 adjustable settings in total.</div>

#### How much data do you need to trust your backtest?

| Your backtest Sharpe ratio | You want confidence that live trading will achieve Sharpe of at least... | Minimum data needed |
|---|---|---|
| 1.0 | Greater than 0 | 681 trading days — about 2.7 years of daily data |
| 2.0 | Greater than 0 | 174 trading days — about 0.7 years of daily data |
| 1.5 | Greater than 1.0 | 2,739 trading days — about 10.9 years of daily data |

> These requirements apply to paper trading (running a live strategy with no real money) just as much as to the backtest itself. You need the same amount of clean out-of-sample testing (test set) to be confident your strategy is real. Meaning the minimum data is required for both training set and test set when split data for training

#### How to protect yourself from data-snooping bias

Split your historical data into two halves:
- **Training half** (the earlier period): Build and fine-tune your strategy here
- **Test half** (the more recent period): Run the strategy unchanged on this data. Do not adjust anything based on what you see here.

If the strategy works well on both halves, the result is much more credible. If it only works on the training half, it was overfit to the past and is unlikely to hold up in real trading.

#### Example

<div class="example-block">
<div class="ex-title">Example 3.6 — GLD vs. GDX pair trading: does it hold up on unseen data? <span class="ex-pill pill-live">Real strategy test</span></div>

<p><strong>The idea:</strong> GLD tracks the price of gold. GDX holds a basket of gold-mining company stocks. Since gold miners' profits depend on gold prices, these two ETFs should generally move together. When their prices drift unusually far apart, we bet they will snap back — this is called pair trading.</p>

<strong>How it works:**</strong>
<p>- Calculate the "spread" = GLD price − (1.637 × GDX price). The 1.637 is the hedge ratio — how many dollars of GDX to balance against each dollar of GLD, found by running a simple regression on the training data</p>
<p>- When the spread drops more than 2 standard deviations below normal → **buy the spread** (buy GLD, short GDX)</p>
<p>- When the spread rises more than 2 standard deviations above normal → **short the spread** (short GLD, buy GDX)</p>
<p>- Exit when the spread returns to within 1 standard deviation of normal</p>

<strong>Splitting the data:</strong>
<p>- Training set: first 252 trading days (about 1 year)</p>
<p>- Test set: all remaining days — the strategy runs here without any changes</p>

<strong>Results with default settings (entry at ±2 standard deviations, exit at ±1):</strong>

<div class="result-box">
<strong>Sharpe on training data: 2.08</strong><br>
<strong>Sharpe on out-of-sample test data: 1.49</strong>
</div>

Both are solid — the strategy holds up on data it was never trained on.

<div class="ex-lesson"><strong>Takeaway:</strong> When tuning your settings on training data also improves the test data, that is a genuine green flag. When it only improves the training data and hurts the test data, you have overfit — and the strategy probably will not survive real trading.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Look-ahead bias</span> <span class="ref-tag">Data-snooping bias</span> <span class="ref-tag">Training set</span> <span class="ref-tag">Test set</span> <span class="ref-tag">Out-of-sample testing</span> <span class="ref-tag">Pair trading</span> <span class="ref-tag">Hedge ratio</span>
</div>

---

### Section 6 — How Do Transaction Costs Destroy Strategies?

<div class="note-abstract">
Trading costs are not just a small footnote — they can completely destroy a strategy that looks great on paper. The more often a strategy trades, the more costs pile up, and the damage is multiplicative. A strategy claiming a Sharpe ratio of 4.47 could collaps to −3.19 after adding realistic trading costs. Learning to include costs properly is not optional detail — it is what separates a working strategy from an expensive illusion.
</div>

#### Core ideas

<div class="key-idea"><strong>The more often a strategy trades, the more costs eat into returns.</strong> A strategy that rebalances once per week and one that rebalances every day face vastly different cost burdens over the same period. Any strategy that trades very frequently and looks impressive before costs needs to be treated as unproven until the costs are applied properly.</div>

<div class="key-idea"><strong>Which stocks you trade matters as much as how the strategy is designed.</strong> The below example (example 3.7) is a perfect demonstration: the same mean-reversion strategy achieves a Sharpe of 4.47 on small and micro-cap stocks, but collapses to 0.25 on large S&P 500 stocks. The logic of the strategy is identical — the difference is that small stocks are less efficiently priced and snap back more reliably than large ones.</div>

<div class="key-idea"><strong>Tiny execution changes — like trading at the open instead of the close — can flip a strategy from losing money to making money.</strong> Example 3.8 shows that one single code change (swap closing prices for opening prices) transforms a strategy losing money every day into one that profits. When and how you execute is just as important as the underlying trading idea.</div>

#### Examples from the book

<div class="example-block">
<div class="ex-title">Example 3.7 — A Sharpe 4.47 strategy becomes Sharpe −3.19 after 5 basis points per trade <span class="ex-pill pill-warn">Warning example</span></div>

<strong>The strategy (from MIT researchers Khandani and Lo):</strong> Every day, buy the S&P 500 stocks that fell the most yesterday and short the ones that rose the most. Bet that yesterday's big losers will bounce back and yesterday's big winners will pull back. Rebalance the whole portfolio every single trading day.

<strong>Without any transaction costs in 2006 (applied to the S&P 500):</strong>

<div class="result-box"><strong>Sharpe ratio: 0.25</strong> — already far below the paper's reported 4.47. The reason: the original paper used small and micro-cap stocks where this bounce-back effect is much stronger. Large-cap S&P 500 stocks are too efficiently priced for the strategy to work as well.</div>

<strong>After adding 5 basis points (0.05%) per trade:</strong>

<div class="result-box"><strong>Sharpe ratio: −3.19</strong> — deeply and consistently unprofitable</div>

<div class="ex-lesson"><strong>Takeaway:</strong> Never assume a strategy works just because a published paper says it does. Always apply it to the exact universe you plan to trade, and always include realistic transaction costs. Both of those checks can independently turn a winner into a loser.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Transaction costs</span> <span class="ref-tag">Basis points</span> <span class="ref-tag">Portfolio turnover</span> <span class="ref-tag">Universe selection</span> <span class="ref-tag">Mean reversion</span> <span class="ref-tag">Execution timing</span>
</div>

---

### Section 7 — How Do You Improve a Strategy That Is Not Working?

<div class="note-abstract">
When a strategy does not perform well in the first backtest, that does not mean it is hopeless. Often a small, targeted tweak — trying a different universe of stocks, a different time to execute, or a slightly different signal threshold — can dramatically improve results. The key rule is that any change that helps on your training data must also help on your test data. If it only helps on the data you already used to develop the strategy, you have not found a real improvement — you have just found a cleverer way to fit to the past.
</div>

#### Core ideas

<div class="key-idea"><strong>Any improvement must hold up on data the strategy has never seen before.</strong> This is the non-negotiable rule. If you tweak the strategy to look better on your training data and it gets worse on your test data, you have not improved it — you have overfit it. The test set is your reality check and it must be kept sacred.</div>

<div class="key-idea"><strong>The best improvements have a logical, real-world reason behind them.</strong> "Exclude pharmaceutical stocks because surprise drug trial results can trigger huge random price swings unrelated to the strategy's logic" is a sensible, well-grounded refinement. "Exclude stocks whose ticker starts with the letter T" is not — it is just curve-fitting in disguise, and it will almost certainly stop working in the future.</div>

<div class="key-idea"><strong>The three most powerful levers to pull are: which stocks you trade, when you execute, and how often you rebalance.</strong> As shown in Examples 3.7 and 3.8, changing the stock universe or the execution timing can transform a losing strategy into a winning one. Try these clear, economically motivated changes before reaching for more exotic adjustments.</div>

<div class="ref-tags">
<span class="ref-tag">Training set</span> <span class="ref-tag">Test set</span> <span class="ref-tag">Data-snooping bias</span> <span class="ref-tag">Sensitivity analysis</span> <span class="ref-tag">Universe selection</span> <span class="ref-tag">Execution timing</span>
</div>

---

### Term Glossary

Plain-English definitions for every key term introduced in Chapter 3.

#### Data Quality

<div class="glossary-entry">
<div class="gterm">Backtest <span class="gcat cat-data">Data</span></div>
Running a trading strategy on historical data to simulate how it would have performed in the past. Think of it as a practice run before using real money. The result is always somewhat optimistic — live trading almost always performs a bit worse than the backtest because the backtest does not capture every real-world friction.
</div>

<div class="glossary-entry">
<div class="gterm">Split adjustment <span class="gcat cat-data">Data</span></div>
Correcting historical stock prices to account for stock splits. In a 2-for-1 split, the stock price drops by half but shareholders get twice as many shares — nothing really changed. Unadjusted data makes this look like a genuine price crash.
</div>

<div class="glossary-entry">
<div class="gterm">Dividend adjustment <span class="gcat cat-data">Data</span></div>
Correcting historical prices to remove the price drop that happens when a company pays a dividend. On the day a dividend is paid (the ex-date), the stock price drops by roughly the dividend amount — even though shareholders received that cash. Without adjustment, this looks like a genuine price decline and generates false trading signals.
</div>

<div class="glossary-entry">
<div class="gterm">Point-in-time data <span class="gcat cat-data">Data</span></div>
A database that records which stocks actually existed and were tradeable on each specific historical date — including those that later went bankrupt or were removed from exchanges. The gold standard for backtesting. Without it, your database only shows "winners" (companies still alive today), which makes strategies that buy cheap stocks appear far more profitable than they were in reality.
</div>

<div class="glossary-entry">
<div class="gterm">Survivorship bias <span class="gcat cat-bias">Bias</span></div>
The distortion that happens when a database is missing stocks that went bankrupt or were delisted. Only the "survivors" remain in the data.
</div>

<div class="glossary-entry">
<div class="gterm">High/low price noise <span class="gcat cat-data">Data</span></div>
The problem that daily high and low prices are much less trustworthy than opening and closing prices. The day's recorded high could be set by a single tiny off-exchange trade or a data entry mistake. Any strategy that assumes you can reliably buy at exactly the daily low or sell at exactly the daily high will look better in backtesting than it ever will in real trading.
</div>

#### Performance Metrics

<div class="glossary-entry">
<div class="gterm">Sharpe ratio <span class="gcat cat-perf">Performance</span></div>
A score that measures how much return you earned per unit of risk. Formula: (Average return − Risk-free rate) ÷ Standard deviation of returns.
</div>

<div class="glossary-entry">
<div class="gterm">MAR ratio <span class="gcat cat-perf">Performance</span></div>
A quick gut-check metric: your annual growth rate divided by your worst loss from peak. Higher is better. It roughly cancels out the effect of leverage, making it easier to compare strategies with different risk profiles alongside the Sharpe ratio.
</div>

<div class="glossary-entry">
<div class="gterm">CAGR (compound annual growth rate) <span class="gcat cat-perf">Performance</span></div>
The annual rate at which your investment grows if profits are reinvested each year. It sounds simple but is actually unreliable for comparing strategies because the answer depends on tricky definitional choices about how to count capital — especially for long-short strategies. The Sharpe ratio mostly avoids these ambiguities, which is why it is preferred.
</div>

<div class="glossary-entry">
<div class="gterm">Maximum drawdown (MDD) <span class="gcat cat-perf">Performance</span></div>
The biggest loss from any peak to a subsequent trough in your account value, expressed as a percentage. This answers the question: "How bad could it get before I recover?" It must be a number you could survive — both financially and psychologically.
</div>

<div class="glossary-entry">
<div class="gterm">Maximum drawdown duration <span class="gcat cat-perf">Performance</span></div>
The longest stretch of time a strategy spent below its previous peak.
</div>

<div class="glossary-entry">
<div class="gterm">High watermark <span class="gcat cat-perf">Performance</span></div>
The best result your strategy has ever achieved up to any given point in time. All drawdowns are measured relative to this level. When you hit a new best and set a new high watermark, the drawdown counter resets to zero.
</div>

<div class="glossary-entry">
<div class="gterm">Deflated Sharpe ratio <span class="gcat cat-perf">Performance</span></div>
A more honest version of the Sharpe ratio that shrinks it based on how many times you tweaked your strategy during development. The more different settings and variations you tried before landing on the "best" result, the more that result gets deflated — because some of the apparent performance was probably just getting lucky with historical noise rather than finding something real.
</div>

#### Backtesting Pitfalls

<div class="glossary-entry">
<div class="gterm">Look-ahead bias <span class="gcat cat-bias">Bias</span></div>
Using information in your backtest that you could not have known at the time of the trade. For example: basing today's trade on today's lowest price — but you do not know that until the market closes. Or fitting a statistical model to your full historical dataset and then using that model to generate signals throughout the same data — the model has effectively "seen the future."
</div>

<div class="glossary-entry">
<div class="gterm">Data-snooping bias <span class="gcat cat-bias">Bias</span></div>
The mistake of tuning a strategy so precisely to historical data that it stops working on new data. Happens naturally when you test hundreds of combinations and pick the best-looking one — that "best" result is usually just historical coincidence, not a real pattern. Rule of thumb: limit yourself to 5 or fewer adjustable settings. Reduce its impact by holding out a test set and validating your finalised strategy there before declaring success.
</div>

<div class="glossary-entry">
<div class="gterm">Out-of-sample testing <span class="gcat cat-method">Method</span></div>
Testing your finished strategy on data it was never trained on. Running it on live real-time data with no money at risk (paper trading) is the ultimate version of this.
</div>

<div class="glossary-entry">
<div class="gterm">Training set / Test set <span class="gcat cat-method">Method</span></div>
Two separate halves of your historical data. The training set (older data) is where you build and refine the strategy. The test set (more recent data) is where you validate it without making any further adjustments.
</div>

<div class="glossary-entry">
<div class="gterm">Sensitivity analysis <span class="gcat cat-method">Method</span></div>
Checking how your strategy's results change when you nudge the parameters slightly away from the optimal values. If the performance collapses dramatically with even a tiny change, data-snooping bias is likely — the strategy is too precisely tuned to the past to generalise. A trustworthy strategy should still produce reasonable results with parameters that are close to (but not exactly at) the sweet spot.
</div>

<div class="glossary-entry">
<div class="gterm">Parameterless trading model <span class="gcat cat-method">Method</span></div>
A model where instead of the researcher fixing parameters upfront (like always using a 20-day moving average), the model recalculates its own optimal parameters continuously from recent data. This removes one major source of data-snooping bias. It does not mean there are literally no parameters — it means the model determines them dynamically rather than the researcher picking them once and locking them in.
</div>


#### Strategy Concepts

<div class="glossary-entry">
<div class="gterm">Hedge ratio <span class="gcat cat-data">Data</span></div>
In pair trading, this is the number that tells you how many dollars of the second security to trade for each dollar of the first, so that the two sides of the trade are properly balanced. It is calculated using a simple linear regression. From Example 3.6: the hedge ratio between GLD and GDX is 1.637, meaning for every USD 1 of GLD you trade, you trade USD 1.637 of GDX on the opposite side.
</div>

<div class="glossary-entry">
<div class="gterm">Z-score <span class="gcat cat-data">Data</span></div>
A way of measuring how unusual the current value of something is compared to its recent history. Formula: (Current value − Average) ÷ Standard deviation. A z-score of +2 means the value is 2 standard deviations above average. A z-score of −2 means unusually low. In pair trading, you enter the trade when the spread's z-score reaches ±2 (unusual enough to bet on reversion) and exit when it returns to ±1 (back to near-normal).
</div>

<div class="glossary-entry">
<div class="gterm">Portfolio turnover <span class="gcat cat-cost">Cost</span></div>
How much of your portfolio you buy or sell in each trading period, as a fraction of total portfolio size. High turnover means lots of trading activity and lots of transaction costs.
</div>

<div class="glossary-entry">
<div class="gterm">Universe selection <span class="gcat cat-method">Method</span></div>
Choosing which stocks (or other instruments) your strategy is allowed to trade. One of the most powerful decisions in strategy design.
</div>

<div class="glossary-entry">
<div class="gterm">Execution timing (open vs. close) <span class="gcat cat-method">Method</span></div>
Whether your strategy places trades at the start of the day (market open) or the end (market close). This is not a minor implementation detail — it can determine whether the strategy makes or loses money.
</div>

  </div>
</div>


## Chapter 5 — Execution Systems

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('ch5')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">Chapter 5</span>
      <div>
        <div class="chapter-title">Chapter 5 — Execution Systems</div>
        <div class="chapter-subtitle">Building your automated trading system, cutting costs, and testing safely</div>
      </div>
    </div>
    <span class="chapter-arrow" id="ch5-arrow">▼</span>
  </button>
  <div class="chapter-body" id="ch5-body">

### Section 1 — What Does an Automated Trading System Actually Do?

<div class="note-abstract">
An automated trading system (ATS) is the software that turns your trading idea into real orders. It grabs the latest market prices, runs your strategy to figure out what to buy and sell, and sends those orders to your broker automatically. Without this, you are back to manually clicking "buy" and "sell" all day — which defeats the whole point of quantitative trading.
</div>

#### Core ideas

<div class="key-idea"><strong>An ATS does three things in sequence: get data, generate orders, send orders.</strong> It pulls fresh price data from your broker or a data service, feeds that data into your trading algorithm, and transmits the resulting orders to your brokerage account. These three steps can happen every second for high-frequency strategies, or just once before the market opens for slower daily strategies.</div>

<div class="key-idea"><strong>Fully automated systems are no longer only for professional programmers.</strong> A few years ago, building a system that communicated directly with a broker's API required writing code in Java or C++. Today, platforms like QuantConnect and Blueshift handle all of that for you. You can build and run a fully automated system knowing only Python — or in Blueshift's case, no coding at all.</div>

<div class="key-idea"><strong>The data your system needs is not always just prices.</strong> Many strategies also need earnings estimates, dividend schedules, or announcement dates. Interactive Brokers provides earnings estimates (via Zacks) and expected announcement dates (via Wall Street Horizon) directly to customers, often at low or no cost. Factor this into your system design early — it is painful to discover a data gap after you go live.</div>

#### What flows through your system each day

| Step | What happens | Example |
|---|---|---|
| **1. Data retrieval** | Pull fresh prices and any other data needed | Download today's closing prices for all 500 S&P stocks |
| **2. Signal generation** | Run your algorithm to decide what to trade | Strategy says: buy IGE, short SPY |
| **3. Order creation** | Turn the signals into a proper order list | Generate file: `("IGE", "BUY", "200"), ("SPY", "SELL", "150")` |
| **4. Order transmission** | Send orders to your broker | Upload to basket trader or send via API |
| **5. Monitoring** | Watch for fills, cancel anything unfilled at end of day | Press "cancel unfilled" before close |

<div class="ref-tags">
<span class="ref-tag">ATS</span> <span class="ref-tag">API</span> <span class="ref-tag">DDE link</span> <span class="ref-tag">Basket trader</span>
</div>

---

### Section 2 — How Do You Keep Trading Costs as Low as Possible?

<div class="note-abstract">
We already know from Chapter 3 that transaction costs can destroy a strategy that looks great on paper. Chapter 5 adds the execution layer: there are specific things you can do at the time of placing orders — not just in the strategy design — to keep costs manageable. The core insight is simple: do not trade too large a slice of a stock's daily volume, and avoid very cheap low-priced stocks entirely.
</div>

#### Core ideas

<div class="key-idea"><strong>Never trade more than 1% of a stock's average daily trading volume in a single order.</strong> When your order is large relative to how much of that stock normally trades in a day, you start moving the price against yourself just by trying to buy or sell. Sticking to under 1% of average daily volume keeps your market impact small. This threshold sounds conservative, but for small-cap stocks it can be surprisingly restrictive.</div>

<div class="key-idea"><strong>Avoid stocks priced below $5.</strong> Institutional traders have a well-known rule: skip stocks under $5. Two reasons: first, you need to buy far more shares to deploy the same capital, which means more commission. Second, cheap stocks have wider bid-ask spreads as a percentage of their price, making every trade more expensive. Stick to more liquid, higher-priced stocks where spreads are tighter.</div>

<div class="key-idea"><strong>Scale your position sizes to market capitalisation — but do not do it linearly.</strong> A linear scale (buying proportionally more of bigger companies) sounds sensible, but it means the largest company gets 10,000× more weight than the smallest, effectively eliminating any small stocks from your portfolio. Instead, scale to the fourth root of market cap — this keeps the weight ratio between the biggest and smallest stocks within a manageable factor of about 10, preserving diversification while still respecting size differences.</div>

#### The four types of transaction cost — a quick reminder

| Cost type | What it is | How to reduce it |
|---|---|---|
| **Commission** | Fee your broker charges per trade | Use low-cost brokers; avoid high-turnover strategies |
| **Bid-ask spread** | Gap between buy price and sell price | Avoid low-priced stocks; use limit orders where possible |
| **Market impact** | Your own buying pushes prices up; your own selling pushes them down | Keep order size below 1% of average daily volume |
| **Slippage** | Price moves between when your signal fires and when the order fills | Use faster execution infrastructure; choose brokers with better speed |

<div class="ref-tags">
<span class="ref-tag">Average daily volume</span> <span class="ref-tag">Market capitalisation scaling</span> <span class="ref-tag">Slippage</span> <span class="ref-tag">Bid-ask spread</span>
</div>

---

### Section 3 — Paper Trading — The Essential Safety Net

<div class="note-abstract">
Paper trading means running your automated system on real live market data — but with fake money. It is the only practical way to catch software bugs, discover timing problems, and verify that your system actually behaves the way your backtest predicted. Skipping paper trading is one of the most common and costly mistakes new traders make.
</div>

#### Core ideas

<div class="key-idea"><strong>Paper trading reveals bugs that backtesting simply cannot.</strong> Backtesting uses historical data that just sits there passively. Paper trading runs against live market data in real time, exposing timing issues, data feed problems, order routing failures, and look-ahead bias that only shows up when you cannot actually obtain certain data before placing a trade. Many traders discover a serious look-ahead bias in their strategy the moment they try to paper trade it — because they realise there is no way to get that crucial piece of data before the market opens.</div>

<div class="key-idea"><strong>Paper trading builds genuine intuition that backtesting never can.</strong> Running a backtest shows you the performance statistics. Running a paper trading system for a month shows you what the strategy actually feels like — how much the P&L swings day to day, how much capital gets tied up at peak, how many trades fire on a typical day, and what unexpected operational headaches arise. These are the things you need to understand before putting real money at risk.</div>

<div class="key-idea"><strong>The timing surprises are always bigger than expected.</strong> Downloading and processing data each morning took about 20 minutes. Transmitting all orders to the broker account took another 15 minutes. Total: 35 minutes of preparation before the market opens. If your strategy relies on data or news that cannot be more than 30 minutes old at market open, you have a problem — and you will only discover that problem through paper trading, not through backtesting.</div>

#### What paper trading reveals that backtesting misses

| What you discover | Why backtesting misses it |
|---|---|
| **Software bugs in your ATS** | Backtesting runs on stored historical data; bugs only show up with live systems |
| **Look-ahead bias** | In a backtest you have all the data; in live trading you discover what you actually cannot obtain in time |
| **Data feed problems** | Historical data is clean; live feeds drop out, arrive late, or contain bad ticks |
| **Operational timing issues** | How long does downloading + order generation + transmission actually take? |
| **Transaction cost estimates** | Your real fills often differ from theoretical ones; paper trading gives you real fill prices |
| **Data-snooping bias** | A month of live paper trading is a genuine out-of-sample test |

#### A practical paper trading checklist

<ul class="checklist">
  <li>Run the paper trading system on a real brokerage paper account, not just a simulation you wrote yourself</li>
  <li>Compare paper trade results daily against what your backtest program generates for the same data — differences reveal bugs</li>
  <li>Time every operational step: how long does data download take? Order generation? Transmission?</li>
  <li>Observe P&L swings day-to-day — are they larger or smaller than the backtest suggested?</li>
  <li>Note how much capital is tied up at peak — is it consistent with what you planned?</li>
  <li>Run for at least a month before going live with real money</li>
  <li>Pay close attention to any trades that look wrong — investigate immediately rather than assuming it will fix itself</li>
</ul>

<div class="warning-box">
<strong>⚠️ Warning:</strong> Paper trading attention tends to fade over time as other things compete for your focus. A paper trading system that is being ignored will perform poorly due to neglect — missed data refreshes, unresolved errors, stale parameters. If your attention is wandering, it might be better to start trading with a very small amount of real capital rather than continuing to paper trade half-heartedly. Real money has a remarkable ability to focus the mind.
</div>

<div class="ref-tags">
<span class="ref-tag">Paper trading</span> <span class="ref-tag">Look-ahead bias</span> <span class="ref-tag">Data-snooping bias</span> <span class="ref-tag">Out-of-sample testing</span> <span class="ref-tag">ATS</span>
</div>

---

### Section 4 — Why Does Live Trading Sometimes Disappoint?

<div class="note-abstract">
You have done everything right. You backtested carefully, paper traded for a month, and went live. Three months later, the strategy is barely breaking even — or losing money. This is one of the most disheartening experiences in quantitative trading, and it is also one of the most common. This section gives you a systematic way to diagnose what went wrong, starting with the simplest possible fixes and working up to the hardest truths.
</div>

#### Core ideas

<div class="key-idea"><strong>Start with the simplest diagnoses first — most problems are not mysterious.</strong> Before assuming something deep and structural has gone wrong, check the obvious things: Does your live system actually match your backtest program trade for trade? Are the execution costs higher than you modelled? Are you accidentally trading illiquid stocks that cause large market impact? These mundane issues cause the majority of live/backtest gaps and are fixable.</div>

<div class="key-idea"><strong>If simple fixes do not work, face the two hardest possibilities: data-snooping bias and regime shifts.</strong> Data-snooping bias means the strategy was overfit to historical noise — it never had a real edge. Regime shifts mean the market structure has genuinely changed, so a strategy that worked before no longer works now. Both are difficult to diagnose and both require serious action: either simplify the strategy aggressively or accept that you need to find a new one.</div>

<div class="key-idea"><strong>When the strategy is underperforming, simplify it — do not add complexity.</strong> If you suspect data-snooping bias, the test is to strip away as many rules and parameters as possible. If the backtest performance completely falls apart when you simplify, data-snooping bias is almost certainly the cause — the strategy was relying on those extra rules to fit historical noise. If performance holds up after simplification, poor live results may just be bad luck, and patience may be warranted.</div>

#### Your live trading diagnostic checklist

<ul class="checklist">
  <li><strong>Do the trades match?</strong> Compare every trade your live system generates against what your backtest would have generated for the same data on the same day. If they differ, there is a bug to fix.</li>
  <li><strong>Are execution costs higher than expected?</strong> Add up what you are actually paying in commissions, spreads, and slippage. Compare to your backtest assumptions. If real costs are significantly higher, this alone can explain underperformance.</li>
  <li><strong>Are you trading illiquid stocks?</strong> Check whether your orders are routinely exceeding 1% of average daily volume. If so, you are paying large market impact costs that your backtest did not account for.</li>
  <li><strong>Does the strategy survive simplification?</strong> Remove parameters and rules one by one. If backtest performance collapses immediately, data-snooping bias is likely. If performance holds, the live underperformance may be temporary bad luck.</li>
  <li><strong>Has the market structure changed?</strong> Consider whether a regime shift could have altered the conditions your strategy relies on.</li>
</ul>

#### Two specific regime shifts to know about

<div class="example-block">
<div class="ex-title">Regime shift 1 — Stock price decimalization in 2001 <span class="ex-pill pill-warn">Historical warning</span></div>

<p>Before April 9, 2001, US stock prices were quoted in fractions — sixteenths or eighths of a dollar (e.g., $10 and 3/16). Those wide fractional price increments created friction in the market that statistical arbitrage traders could exploit.</p>

<p>When the US switched to fully decimal pricing on April 9, 2001, those fractions disappeared. Bid-ask spreads narrowed dramatically. The friction that stat arb traders relied on was reduced significantly, and many strategies that looked great in pre-2001 backtests stopped working in the decimal era.</p>

<p><strong>Practical implication:</strong> If your backtest data extends before 2001, the pre-decimalization period will show much better performance than you should expect going forward. Be especially sceptical of any strategy that shows most of its historical edge in the pre-2001 period.</p>

<div class="ex-lesson"><strong>Takeaway:</strong> Always check when most of your backtest returns were generated. If the strategy was unusually profitable before 2001 and the edge has clearly shrunk since, the decimalization regime shift may be the explanation — and the pre-2001 performance is not a reliable guide to future returns.</div>
</div>

<div class="example-block">
<div class="ex-title">Regime shift 2 — The short-selling uptick rule (pre-2007 and post-2010) <span class="ex-pill pill-warn">Historical warning</span></div>

<p>If your strategy involves shorting stocks, there is a specific regulatory trap in the historical data.</p>

<p>Before June 2007, the SEC's "uptick rule" stated that you could only short a stock on an "uptick" — meaning the last trade had to have been at a higher price than the one before it. This rule prevented short sellers from piling on during a price decline. In practice, it meant that many profitable short positions simply could not be entered during fast-moving markets.</p>

<p><strong>Before June 2007:</strong> Uptick rule in force. Shorting is constrained. Backtest performance for short strategies is artificially inflated because the backtest ignores the uptick constraint.</p>
<p><strong>June 2007 – February 2010:</strong> No uptick rule at all. Shorting is unrestricted. This is the most realistic period for backtesting short strategies.</p>
<p><strong>After February 2010:</strong> Alternative uptick rule (Rule 201) introduced. Shorting is restricted again when a stock drops more than 10% in a day.</p>

<p><strong>Additional complication — hard-to-borrow stocks:</strong> Even when the uptick rule does not apply, many stocks — especially small-caps with low liquidity — are "hard to borrow." To short a stock, your broker has to borrow it from someone else (usually a mutual fund or another client). If no one will lend it, you simply cannot short it, regardless of what your backtest says. This can eliminate many of the best short opportunities in a strategy.</p>

<div class="ex-lesson"><strong>Takeaway:</strong> If your strategy involves shorting, the most realistic backtest period is June 2007 through February 2010 — the only window when neither the old uptick rule nor the new alternative rule was in force. For any other period, assume your backtest performance on the short side is somewhat optimistic.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Data-snooping bias</span> <span class="ref-tag">Regime shift</span> <span class="ref-tag">Decimalization</span> <span class="ref-tag">Uptick rule</span> <span class="ref-tag">Hard to borrow</span> <span class="ref-tag">Market impact</span>
</div>

---

### Term Glossary

#### Trading Systems

<div class="glossary-entry">
<div class="gterm">ATS (Automated Trading System) <span class="gcat cat-system">System</span></div>
Software that automatically retrieves market data, runs a trading algorithm, and sends orders to a brokerage account — all without requiring a human to manually click "buy" or "sell".
</div>

<div class="glossary-entry">
<div class="gterm">DDE link (Dynamic Data Exchange) <span class="gcat cat-system">System</span></div>
A formula you insert into an Excel spreadsheet cell that automatically fetches live market data from your broker.
</div>

<div class="glossary-entry">
<div class="gterm">Basket trader <span class="gcat cat-system">System</span></div>
A broker-provided application that lets you upload a file containing hundreds or thousands of orders and submit them all to the exchange simultaneously with one keystroke.
</div>

<div class="glossary-entry">
<div class="gterm">Spread trader <span class="gcat cat-system">System</span></div>
A broker-provided application specifically designed for pair trading and spread strategies. You specify pairs of securities and the conditions (spread prices) at which you want to enter. The spread trader then monitors live prices throughout the day and automatically enters orders when your conditions are met — without you having to watch the screen.
</div>

#### Cost Reduction

<div class="glossary-entry">
<div class="gterm">Average daily volume (ADV) <span class="gcat cat-cost">Cost</span></div>
The average number of shares of a given stock traded per day, calculated over a recent period (typically 30 or 90 days).
</div>


<div class="glossary-entry">
<div class="gterm">Market capitalisation scaling <span class="gcat cat-cost">Cost</span></div>
The practice of giving larger companies bigger positions in your portfolio, scaled by their market capitalisation (total value of all shares).
</div>

<div class="glossary-entry">
<div class="gterm">Slippage <span class="gcat cat-cost">Cost</span></div>
The difference between the price your strategy's signal was triggered at and the actual price your order filled at. Slippage happens because markets move in the tiny gap between when your system generates the order and when the exchange actually executes it. Slippage is usually a cost (prices move against you on average during that gap), but occasionally works in your favour.
</div>

<div class="glossary-entry">
<div class="gterm">Dark pool <span class="gcat cat-market">Market</span></div>
Private trading venues where large orders can be matched without being publicly displayed on the exchange order book. Because the orders are hidden, large institutional trades do not move the market the way they would on a public exchange.
</div>

#### Testing & Diagnosis

<div class="glossary-entry">
<div class="gterm">Decimalization <span class="gcat cat-market">Market</span></div>
The switch in April 2001 when US stock prices moved from being quoted in fractions (sixteenths and eighths of a dollar) to full decimal pricing.
</div>

<div class="glossary-entry">
<div class="gterm">Uptick rule <span class="gcat cat-market">Market</span></div>
An SEC regulation (in force until June 2007) that required a stock's price to have just ticked upward before you could short it.
</div>

<div class="glossary-entry">
<div class="gterm">Hard to borrow <span class="gcat cat-market">Market</span></div>
A stock is "hard to borrow" when your broker cannot find anyone willing to lend their shares for you to short.
</div>


<div class="glossary-entry">
<div class="gterm">NDA (Non-Disclosure Agreement) <span class="gcat cat-method">Method</span></div>
A legal contract where the other party (e.g., a programming consultant) agrees not to share your confidential information. Useful but hard to enforce in practice — if a programmer decides to trade your strategy in their personal account, you would rarely know.
</div>

  </div>
</div>


## Chapter 6 — Money and Risk Management

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('ch6')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">Chapter 6</span>
      <div>
        <div class="chapter-title">Chapter 6 — Money and Risk Management</div>
        <div class="chapter-subtitle">The Kelly formula, optimal leverage, risk types, and the psychology of trading</div>
      </div>
    </div>
    <span class="chapter-arrow" id="ch6-arrow">▼</span>
  </button>
  <div class="chapter-body" id="ch6-body">

### Section 1 — The Core Question — How Much Should You Bet?

<div class="note-abstract">
Every trading strategy — no matter how good — will sometimes lose money. The question is not whether you will have losing periods, but whether those losing periods will destroy you or just inconvenience you. The answer depends almost entirely on how much leverage you are using. Too little leverage and your strategy grows painfully slowly. Too much and a single bad month can cause losses from which you never recover. Finding the sweet spot between these two extremes is what this chapter is about.
</div>

#### Core ideas

<div class="key-idea"><strong>The goal is not to maximise returns — it is to maximise long-term compounded wealth.</strong> These sound like the same thing but they are not. Maximising returns often means taking on so much risk that eventual ruin becomes almost certain. Maximising long-term compounded wealth means finding the leverage level where your account grows the fastest without ever being wiped out.</div>

<div class="key-idea"><strong>Risk always costs you something, even when the expected return is zero.</strong> This is one of the most counterintuitive results in finance. If a strategy has a 50/50 chance of going up 1% or down 1%, most people assume you will break even over time. You will not — you will slowly lose money. The mathematics of compounding means that volatility itself erodes your wealth, even when the expected return is exactly zero.</div>

<div class="key-idea"><strong>The Sharpe ratio determines the maximum possible growth rate of your wealth.</strong> There is a clean mathematical formula for this: $$g_{\max} = r_f + \frac{\text{Sharpe}^2}{2}$$ A high-Sharpe strategy with modest nominal returns will always grow your wealth faster, once properly levered, than a low-Sharpe strategy with high nominal returns.</div>

#### Example

<div class="example-block" markdown="1">
<div class="ex-title">Example 6.1 — The coin flip puzzle: why volatility costs you money even with zero expected return <span class="ex-pill pill-puzzle">Puzzle</span></div>

<strong>Here is the puzzle:</strong>

<p>A stock goes up exactly 1% or down exactly 1% each minute, with equal 50/50 probability. If you buy this stock, will you — in the long run — make money, lose money, or break even?</p>

<p>Most experienced traders answer: <strong>break even</strong>. The answer is wrong.</p>

<p><strong>You will slowly lose money</strong> — at a rate of about 0.005% per minute (0.5 basis points per minute).</p>

<p><strong>Why?</strong> Because the mathematics of compounding is not symmetric. Consider two minutes:</p>
- Minute 1: up 1% → your `$100` becomes `$101`
<p>- Minute 2: down 1% → your \$101 becomes \$99.99</p>

<p>You did not break even — you lost \$0.01. The 1% gain and 1% loss are equal in percentage terms, but they are applied to different base amounts, so they do not cancel out.</p>

<p>More precisely, the long-run compounded growth rate is:</p>

$$g = m - \frac{s^2}{2}$$

<p>Where:</p>
<p>$m$ = average return per period (0% here)</p>
<p>$s$ = standard deviation per period (1% here)</p>
<p>$\frac{s^2}{2} = \frac{0.01^2}{2} = 0.00005 = 0.005\%$</p>

<p>So:</p>
$$g = -0.005\% \text{ per minute — slowly losing money}$$

<p><strong>The full general formula extends this to any leverage:</strong></p>

$$g(f) = r + f \cdot m - \frac{f^2 \cdot s^2}{2}$$

<p>Where:</p>
<p>$g(f)$ = compounded growth rate when using leverage $f$</p>
<p>$r$ = risk-free rate (what your cash earns if not invested)</p>
<p>$f$ = leverage (1 = no leverage, 2 = 2× leverage, etc.)</p>
<p>$m$ = average one-period excess return (return minus risk-free rate)</p>
<p>$s$ = standard deviation of one-period returns</p>
<p>$s^2$ = variance of returns</p>

<div class="ex-lesson"><strong>Takeaway:</strong> Volatility is not free. Even when your strategy has a zero average return, if it has any risk at all, compounding mathematics means you will gradually lose money over time. This is why risk management — controlling volatility — is as important as finding a strategy with positive expected returns. Risk always reduces long-term growth.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Kelly formula</span> <span class="ref-tag">Compounded growth rate</span> <span class="ref-tag">Sharpe ratio</span> <span class="ref-tag">Leverage</span>
</div>

---

### Section 2 — The Kelly Formula — Your Optimal Leverage Calculator

<div class="note-abstract">
The Kelly formula is the mathematical answer to the question "how much should I bet?" It was originally developed by a Bell Labs scientist named J.L. Kelly in 1956 for telephone signal problems, then famously applied to gambling by Ed Thorp (the mathematician who beat the casinos at blackjack). Applied to trading, it tells you exactly how much leverage to use to make your wealth grow as fast as possible — without risking ruin.
</div>

#### Core ideas

<div class="key-idea"><strong>Divide the average excess return by the variance of returns.</strong> If your strategy averages 7% annual excess return and has a standard deviation of 15%, the formula says to use $$f = \frac{7\%}{(15\%)^2} = 3.1\times$$ leverage. That is how much you should borrow to maximise your long-term wealth growth.</div>

<div class="key-idea"><strong>In practice, most traders use half-Kelly — half the recommended leverage.</strong> The Kelly formula assumes your return estimates are perfectly accurate, which they never are. Real return distributions also have "fat tails" — extreme events happen more often than the formula assumes. Using half of the Kelly-recommended leverage builds in a safety buffer for these inaccuracies.</div>

<div class="key-idea"><strong>You must update your leverage continuously as your equity changes.</strong> Kelly is not a one-time calculation. If you suffer a loss, your equity shrinks and Kelly says reduce your position size immediately. If you profit, your equity grows and Kelly says you can increase your position size. Doing this update at least once per day keeps your leverage close to optimal at all times.</div>

#### The Kelly formula

<p>For a single strategy:</p>

$$f = \frac{m}{s^2}$$

Where:
- $m$ = average one-period return minus the risk-free rate
- $s$ = standard deviation of one-period returns
- $s^2$ = variance of returns

<p>Example:</p> 

$m = 7\%$, $s = 15\%$

$$f = \frac{0.07}{(0.15)^2} = \frac{0.07}{0.0225} = 3.11$$

<p>This means: for every \$1 of your own capital, borrow an additional \$2.11 to invest a total of \$3.11.</p>

#### Examples

<div class="example-block" markdown="1">
<div class="ex-title">Example 6.2 — Kelly leverage for buying and holding SPY (the S&P 500 ETF) <span class="ex-pill pill-num">Worked numbers</span></div>

**The strategy:** Simply buy and hold SPY — the ETF that tracks the S&P 500 index.

**Historical numbers (at the time of calculation):**
- Average annual return: 11.23%
- Standard deviation of annual returns: 16.91%
- Risk-free rate: 4% per year
- Average excess return: 11.23% − 4% = 7.23%

**Step 1 — Calculate the Sharpe ratio:**

$$\text{Sharpe ratio} = \frac{7.23\%}{16.91\%} = 0.428$$

**Step 2 — Calculate the Kelly leverage:**

$$f = \frac{7.23\%}{(16.91\%)^2} = \frac{0.0723}{0.02860} = 2.53$$

<p>So Kelly says: if you have \$100,000, borrow money to invest a total of \$253,000 in SPY.</p>

**Step 3 — Calculate the optimal compounded growth rate:**

$$g_{\max} = r_f + \frac{\text{Sharpe}^2}{2} = 4\% + \frac{(0.428)^2}{2} = 13.1\%$$

(per year, compounded after financing costs)

For comparison, if you just buy SPY with cash and no leverage:

$$g = 11.23\% - \frac{(16.91\%)^2}{2} = 11.23\% - 1.43\% = 9.8\% \text{ per year}$$

<div class="result-box">
<strong>Unleveraged SPY: 9.8% compounded annual growth</strong><br>
<strong>Kelly-leveraged SPY (2.53): 13.1% compounded annual growth</strong>
</div>

<div class="ex-lesson"><strong>Takeaway:</strong> The Kelly-leveraged approach grows wealth significantly faster — 13.1% vs 9.8% per year. But notice that the Kelly-recommended leverage of 2.53 for just buying the S&P 500 is already quite aggressive. If you can only tolerate modest drawdowns, you should use a lower leverage — which brings us to the half-Kelly approach.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Kelly formula</span> <span class="ref-tag">Half-Kelly</span> <span class="ref-tag">Leverage</span> <span class="ref-tag">Compounded growth rate</span> <span class="ref-tag">Sharpe ratio</span>
</div>


---

### Section 3 — Allocating Capital Across Multiple Strategies

<div class="note-abstract">
Most serious traders run more than one strategy at a time — different strategies for different markets, timeframes, or instruments. The Kelly formula extends naturally to this multi-strategy case. The key insight is that strategies that are uncorrelated (or negatively correlated) with each other provide a diversification benefit: you can often run a higher total leverage when strategies do not all lose at the same time.
</div>

#### Core ideas

<div class="key-idea"><strong>The multi-strategy Kelly formula automatically recommends shorting strategies with negative expected returns.</strong> If you have three strategies and one of them has a negative expected return, the formula will literally tell you to short that strategy (bet against it). This makes intuitive sense — if you expect a strategy to lose money, the right position is the opposite of what the strategy says.</div>

<div class="key-idea"><strong>Combining strategies can grow wealth faster than any individual strategy alone.</strong> Even when two strategies have the same expected return, if they lose money at different times (low correlation), combining them reduces total volatility.</div>

<div class="key-idea"><strong>Update the leverage inputs regularly — at least monthly, ideally daily.</strong> The Kelly formula uses your strategy's recent mean return and standard deviation. These change over time as market conditions evolve. Using a lookback period of about six months is a practical balance between being responsive to recent performance and not overreacting to short-term noise.</div>

#### Examples

<div class="example-block" markdown="1">
<div class="ex-title">Example 6.3 — Optimal allocation across three sector ETFs: OIH, RKH, and RTH <span class="ex-pill pill-num">Worked numbers</span></div>

**The three strategies (actually just three ETFs held simultaneously):**

- **OIH** — Oil services ETF
- **RKH** — Regional bank ETF
- **RTH** — Retail ETF

**Historical performance (annualised excess returns above 4% risk-free rate):**

| ETF | Annual excess return | What this means |
|---|---|---|
| OIH | +13.96% | Oil services — positive edge, should go long |
| RKH | +2.94% | Regional banks — small positive edge, should go long |
| RTH | −0.73% | Retail — slightly negative, Kelly says short it |

**Kelly-recommended leverage for each ETF:**

| ETF | Kelly leverage | Meaning |
|---|---|---|
| OIH | +1.29× | Long — invest 1.29× your equity in oil services |
| RKH | +1.17× | Long — invest 1.17× your equity in regional banks |
| RTH | −1.49× | Short — short 1.49× your equity in retail |

**Combined portfolio result:**

<div class="result-box">
<strong>Portfolio Sharpe ratio: 0.475</strong><br>
<strong>Maximum compounded annual growth rate: 15.29%</strong>
</div>

For reference, the best individual ETF (OIH) achieves only 12.78% compounded annual growth on its own. The combined portfolio of three ETFs beats OIH's solo performance — even though RTH is being shorted and RKH barely contributes — because diversification across uncorrelated strategies reduces total volatility.

<div class="ex-lesson"><strong>Takeaway:</strong> Combining multiple strategies — even ones with weak individual performance — almost always beats any single strategy if they are not perfectly correlated. The Kelly formula handles all of this automatically by computing the optimal allocation across the full portfolio simultaneously.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Kelly formula</span> <span class="ref-tag">Diversification</span> <span class="ref-tag">Covariance matrix</span> <span class="ref-tag">Portfolio allocation</span>
</div>

---

### Section 4 — Risk Management Beyond the Formula

<div class="note-abstract">
The Kelly formula gives you the mathematically optimal leverage — assuming your return estimates are correct and returns follow a normal bell-curve distribution. In the real world, neither of these assumptions holds perfectly. Returns can be more extreme than the formula predicts (fat tails), and your estimates of average returns are always uncertain. This section explains how to handle these realities.
</div>

#### Core ideas

<div class="key-idea"><strong>Real financial markets have "fat tails" — extreme events happen far more often than the formula assumes.</strong> The Kelly formula assumes that returns follow a neat bell curve. In reality, stock markets occasionally experience moves of 10%, 20%, or even more in a single day — events that a bell curve would say are essentially impossible but which happen regularly. These are called black swan events. The formula does not protect you from them, which is why you should use half-Kelly or even less as your starting point.</div>

<div class="key-idea"><strong>Use your historical worst-case loss as an additional safety check.</strong> Beyond the Kelly formula, calculate the worst single day (or week) your strategy ever experienced in the backtest. Then ask: how much of your equity could you tolerate losing in that single period? The answer to that question sets a maximum leverage limit independently of the Kelly formula. Always use the more conservative of the two limits.</div>

<div class="key-idea"><strong>When losses happen, you must reduce your position — even though it feels exactly wrong.</strong> Risk management requires selling into losses and buying into gains. This feels backwards and painful in the moment. But the Kelly formula makes it mathematically explicit: after a loss, your equity is smaller, so the formula says your position should be smaller too. Failing to reduce after losses is how small drawdowns turn into catastrophic ones.</div>

#### The practical worst-case check

```
Maximum safe leverage from historical loss:

  Step 1: Find the single worst one-period loss in your backtest
  Step 2: Decide the maximum one-period equity loss you could tolerate
  Step 3: Maximum leverage = Max tolerable loss ÷ Worst historical loss

Example (from the book — S&P 500):
  Worst single-day loss in history: −20.47% (Black Monday, October 19, 1987)
  If you can tolerate a 20% one-day equity drop:
  Max leverage = 20% ÷ 20.47% ≈ 0.98×

  Meanwhile, half-Kelly recommends: 2.53× ÷ 2 = 1.26×
  Use the more conservative: 0.98× — barely any leverage at all
```

This shows that even half-Kelly can sometimes be too aggressive once you factor in historical extremes.

#### The 2007 quant meltdown — financial contagion in action

<div class="example-block" markdown="1">
<div class="ex-title">August 2007 — How one fund's problem became everyone's crisis <span class="ex-pill pill-warn">Historical case study</span></div>

In August 2007, at the start of the subprime mortgage crisis, a series of large hedge funds experienced shocking losses — even funds that held zero mortgage-backed securities.

**What happened:**
1. A large fund suffered major losses on mortgage-backed securities
2. Its risk management system required it to sell liquid stock positions to reduce overall leverage
3. This selling pushed down stock prices that other quant funds also held
4. Those other funds now showed losses — even though their models were fine
5. Their risk management systems also required them to sell, pushing prices down further
6. A domino effect spread losses across the entire quant fund industry

**The numbers:**
- Goldman Sachs's Global Alpha fund: −22.5% in one week
- Renaissance Technologies (the most successful quant fund ever): −8.7% in early August
- Melvin Capital (January 2021 GameStop squeeze, a similar contagion): −53%

**The lesson:** Risk management rules that make sense for each individual fund (reduce positions when you lose money) can combine to create a collective problem. When many funds all try to sell the same things at the same time, they create the very price crashes that trigger further selling. This is called financial contagion.

<div class="ex-lesson"><strong>Takeaway:</strong> No amount of individual-level risk management completely protects you from contagion. But keeping leverage well below the Kelly maximum — using half-Kelly or less — reduces the size of forced selling when things go wrong, limiting your contribution to and your exposure from these cascades.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Fat tails</span> <span class="ref-tag">Black swan</span> <span class="ref-tag">Half-Kelly</span> <span class="ref-tag">Financial contagion</span> <span class="ref-tag">Drawdown</span>
</div>

---

### Section 5 — Stop Losses — Are They Actually Helpful?

<div class="note-abstract">
Many traders use stop losses, which are automatic rules that sell a position once it drops by a certain amount. The idea is simple: stop losses are supposed to limit losses and protect you from a major crash. But in practice, it’s not that straightforward. Stop losses can be very useful for some strategies, but they can also hurt performance in others.
</div>

#### Core ideas

<div class="key-idea"><strong>Stop losses only help when the market is trending — and hurt when the market is mean-reverting.</strong> If prices usually keep moving in the same direction after a drop (a momentum or trending market), then cutting losses quickly makes sense, because the decline may continue. But if prices usually bounce back after falling (a mean-reverting market), then a stop loss can force you to sell at the worst moment—right before the price recovers—so you end up locking in a loss unnecessarily. Since many quantitative strategies are designed around mean reversion, most quant traders need to be careful about using stop losses blindly.</div>

<div class="key-idea"><strong>Stop losses cannot prevent catastrophic losses during sudden market crashes.</strong> In a real shock event—such as fraud news, a sovereign default, or a major crisis—prices usually don’t slide smoothly past your stop level. Instead, they can gap down instantly, skipping over your stop price entirely. When that happens, your stop-loss order will fill at the next available market price, which may be much worse than what you expected.</div>

<div class="key-idea"><strong>The right question to ask before using a stop loss: is this a trending or a mean-reverting situation?</strong> When a move is news-driven—meaning it reflects a real change in a company’s true value—the price often shifts to a new level and stays there. That’s a trending situation, where stop losses can be helpful. But when a move is liquidity-driven—caused by forced selling, short squeezes, or temporary panic—the price distortion is often temporary and tends to reverse. That’s a mean-reverting situation, where stop losses can do more harm than good, and staying patient is usually the better choice.</div>

#### When to use stop losses and when to avoid them

| Situation type | Price behaviour | Stop loss verdict | Example |
|---|---|---|---|
| **News-driven:** real bad news about the company | Trending — prices fall further | ✅ Use stop losses — the trend is likely to continue | Earnings fraud revealed, revenue collapse |
| **Liquidity-driven:** forced selling with no fundamental cause | Mean-reverting — prices eventually snap back | ❌ Avoid stop losses — patience is rewarded | Quant fund forced to liquidate, short squeeze |
| **Sudden market crash** | Gap down — stop loss executes far below trigger | ❌ Stop losses execute at crisis prices, not your target | Black Monday, pandemic announcement |

<div class="example-block" markdown="1">
<div class="ex-title">The mistake — entering a position by error and waiting for mean reversion <span class="ex-pill pill-warn">Personal cautionary tale</span></div>

Psychological trap related to stop losses:

**Scenario:** Your automated system has a bug and enters a large position by mistake. You discover it quickly and have a big unrealised loss.

**The rational response:** Exit immediately. The position was entered in error — you have no model for whether it will recover.

**The emotional response most traders take:** Wait for mean reversion. "I'll exit once it comes back a bit and the loss is smaller."

**The result:** The position usually keeps losing, because there was no model that said now was a good time to hold it. The irrational wait for mean reversion turns a manageable loss into a larger one.

**The rule:** If you entered a position by mistake (software bug, wrong button pressed, data error), exit it immediately regardless of the current P&L. Never wait for mean reversion on an accidental position — you have no basis for assuming mean reversion will occur on that specific security at that specific time.

<div class="ex-lesson"><strong>Takeaway:</strong> Loss aversion causes traders to hold losing mistake positions longer than they should. The rational action — cut the loss immediately — feels painful. The irrational action — wait for recovery — feels less painful but usually leads to bigger losses.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Stop loss</span> <span class="ref-tag">Mean reversion</span> <span class="ref-tag">Momentum</span> <span class="ref-tag">Loss aversion</span>
</div>

---

### Section 6 — Other Risks You Might Not Have Thought About

<div class="note-abstract">
Market risk — the possibility that prices move against you — is what most traders think about. But there are three other types of risk that can destroy your trading business even when the markets are being perfectly kind: model risk (your strategy was never actually correct), software risk (your trading system has bugs), and operational risk (a power cut or internet outage at the worst possible moment).
</div>

#### The three hidden risks

<div class="key-idea"><strong>Model risk — your strategy may have never had a real edge.</strong> The strategy worked beautifully in backtesting but fails in live trading. The best protection is having a collaborator independently reproduce your backtest results — the same "peer review" process that real scientific research requires. If someone else cannot replicate your results from scratch, that is a serious warning sign.</div>

<div class="key-idea"><strong>Software risk — your trading system may not faithfully implement your strategy.</strong> A bug in your automated trading system can cause it to trade differently from what your backtest model specifies — placing wrong orders, using stale prices, or trading at incorrect sizes. The check: run your live system and your backtest system on the same recent data and verify that the trades they generate are identical. Any discrepancy is a bug that needs fixing before real money is at stake.</div>

<div class="key-idea"><strong>Operational risk — physical and infrastructure failures are more common than you think.</strong> Your internet connection goes down at 9:31am. Your power fails mid-order. Your computer crashes during a volatile market session. None of these is exotic — all of them have happened to real traders. Having a backup internet connection, an uninterruptible power supply, and a plan for what to do in each failure scenario is not paranoia — it is basic operational hygiene.</div>

#### Risk type summary

| Risk type | What it means in plain English | How to reduce it |
|---|---|---|
| **Model risk** | Your strategy never had a real edge, or market conditions changed | Have someone else independently replicate your backtest; keep strategies simple; update parameters regularly |
| **Software risk** | Your trading system has bugs that cause it to trade differently from your backtest | Compare live system trades vs. backtest trades on the same data daily; paper trade extensively |
| **Operational risk** | Physical infrastructure failures (internet, power, hardware) | Backup internet connection; uninterruptible power supply; clear emergency procedures |

<div class="ref-tags">
<span class="ref-tag">Model risk</span> <span class="ref-tag">Software risk</span> <span class="ref-tag">Operational risk</span>
</div>

---

### Section 7 — The Psychological Side of Trading

<div class="note-abstract">
Quantitative trading is supposed to remove emotion from the equation — the computer makes the decisions, not you. But the human running the computer still has to decide when to override it, when to shut it down, and when to increase its size. These decisions are where psychology becomes the decisive factor. Two emotions in particular — despair when things go wrong and greed when things go right — cause more trading disasters than any market event.
</div>

#### The big ideas

<div class="key-idea"><strong>Despair during a drawdown causes two opposite mistakes — and both are wrong.</strong> One type of trader in a drawdown panics and shuts the strategy down completely, even when it still has a valid edge and just needs more time. The other type doubles down on the losing strategy, betting more to recover losses faster. Both are irrational. The correct response — systematically reducing leverage according to the Kelly formula — feels neither heroic nor dramatic, which is precisely why it is so hard to actually do.</div>

<div class="key-idea"><strong>Greed during a winning run is just as dangerous as despair during a losing run.</strong> When a strategy is performing brilliantly, the temptation is to lever it up quickly to "make money while it's hot." This is how overleveraging happens — not during obvious danger, but during apparent success. The historical examples of this are enormous: Long-Term Capital Management (2000), Amaranth Advisors (2006, \$6 billion loss), and numerous hedge fund collapses. The pattern is always the same: a previously excellent strategy, overlevered on the basis of past success.</div>

<div class="key-idea"><strong>Loss aversion — your instinct to avoid losses more than you seek equivalent gains — is actually rational for traders, not a psychological flaw.</strong> Economists often treat loss aversion as an irrational bias. The coin-flip puzzle below demonstrates that refusing a fair bet is the correct rational decision when you are playing with finite capital in sequence. The reason is compounding. In sequential investing, large losses hurt disproportionately, and high volatility can destroy long-term growth even when the average payoff looks favorable. 
</div>

#### The representativeness trap — changing your strategy after a loss

<div class="example-block" markdown="1">
<div class="ex-title">The temptation to "fix" your strategy after a big loss <span class="ex-pill pill-warn">Psychological pitfall</span></div>

After a large unexpected loss, the almost universal human response is to look at the historical data and ask: "What rule would have avoided this specific loss?" You then add that rule to your strategy.

**The problem:** This is pure data-snooping bias applied in real time. You are tuning your strategy to avoid a loss that has already happened, not to prevent future losses. Almost certainly, your new rule will:
- Eliminate profit opportunities that would have existed
- Introduce a different vulnerability to future losses that you have not yet seen
- Reduce overall performance on out-of-sample data

**The correct response:** If you feel the strategy genuinely needs improvement after a loss, run a proper backtest of the modified version over a long historical period — not just the recent weeks that hurt you. If the modified strategy genuinely outperforms on a multi-year backtest, the change may be justified. If it only helps for the recent period, you are curve-fitting to recent noise.

<div class="ex-lesson"><strong>Takeaway:</strong> No strategy can avoid all losses. Trading operates in a probabilistic regime — losses happen even to strategies with genuine edges. The correct mental model is to evaluate your strategy over its full historical record, not to react to individual painful losses by restructuring the model.</div>
</div>

#### Real personal examples from the book

<div class="example-block" markdown="1">
<div class="ex-title">Two personal disasters from overleveraging — and what was learned <span class="ex-pill pill-warn">Personal cautionary tales</span></div>

**Disaster 1 — Greed at an institutional fund:**
While working at a money management firm, a strategy had been running successfully for about six months. In a fit of enthusiasm (greed), over `$100` million was added to that portfolio. The strategy had not been running long enough to validate whether the six months of performance was genuine or lucky. The result: over `$1` million in losses for the fund's investors.

**Disaster 2 — Despair while trading independently:**
A mean-reverting spread strategy between XLE (energy ETF) and crude oil futures (CL) was not reverting as expected. Instead of reducing the position according to Kelly principles, the position was stubbornly increased to almost \$500,000, hoping the reversion would come. Eventually despair set in, the position was exited with close to a six-figure loss. Shortly after — as is always the case in such stories — the spread reverted exactly as the strategy predicted. The strategy was right. The position management was catastrophically wrong.

**The lesson the book draws from both:**
Both disasters shared the same root cause: letting emotion override a systematic process. In the first case, greed — adding capital too quickly. In the second, the combination of overconfidence and then despair — increasing a losing position and then exiting at the worst possible moment.

The solution is not more discipline in the abstract — it is more concrete: start small, follow the Kelly formula mechanically, and build up position sizes gradually only as track record justifies it.

<div class="ex-lesson"><strong>Takeaway:</strong> The Kelly formula is not just a mathematical tool. It is a psychological anchor. Having a formula to follow prevents the two emotions — despair and greed — from dictating position sizes. Discipline means trusting the formula, especially when your gut says to do something different.</div>
</div>

#### Box 6.1 — Why loss aversion is rational (not a bias)

<div class="example-block" markdown="1">
<div class="ex-title">Box 6.1 — The coin flip gamble: why refusing a positive expected value bet is smart <span class="ex-pill pill-puzzle">Puzzle</span></div>

Nobel laureate Daniel Kahneman famously used this gamble to illustrate what he called "loss aversion bias":

You are offered a fair coin flip. Tails: you lose `$100`. Heads: you win `$110`. Would you take it?

Most people refuse. Kahneman called this irrational — the expected gain is $5.

**The book argues that the person refusing is actually correct.**

Here is why. Suppose you start with \$1,000 and keep playing this game repeatedly, adjusting stakes proportionally to your current wealth:
- Average return per round: +0.5% (the `$5` gain on `$1,000`)
- Standard deviation per round: 10.5% (`$105` range on `$1,000`)
- Compounded growth rate per round: 0.5% − (10.5%)²/2 = 0.5% − 0.55% = **−0.05%**

You are **losing money** on average, even though the expected gain is positive. The variance is large enough that the compounding math works against you.

The key insight: the standard economic argument for taking this bet assumes you have infinite capital and can play many games simultaneously. In reality, you have one bankroll and must play rounds in sequence — and if you go broke, you stop playing forever. From that perspective (the "time series view"), refusing the bet is the mathematically correct decision.

The takeaway for traders: focusing purely on expected return while ignoring variance is a mistake. Variance destroys compounded wealth. The Kelly formula captures this precisely — it maximises *compounded growth*, not just expected return, which is why it penalises high-volatility strategies.

<div class="ex-lesson"><strong>Takeaway:</strong> Your instinct to be more worried about losses than excited about equivalent gains is mathematically correct for a trader with finite capital playing a repeated game. The economists who call this irrational are using the wrong model — they assume infinite capital, when in reality ruin ends the game permanently.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Loss aversion</span> <span class="ref-tag">Despair</span> <span class="ref-tag">Greed</span> <span class="ref-tag">Overleveraging</span> <span class="ref-tag">Representativeness bias</span> <span class="ref-tag">Kelly formula</span>
</div>

---

### Term Glossary

Definitions for key terms.

#### The Kelly Framework

<div class="glossary-entry">
<div class="gterm">Half-Kelly <span class="gcat cat-kelly">Kelly</span></div>
Using half of the leverage recommended by the Kelly formula. The full Kelly formula is derived assuming perfectly accurate return estimates and normally-distributed returns. Since neither assumption holds in practice, using half-Kelly provides a safety buffer.
</div>

<div class="glossary-entry">
<div class="gterm">Compounded growth rate <span class="gcat cat-kelly">Kelly</span></div>
The actual annual rate at which your wealth grows when you reinvest all profits — accounting for the drag caused by volatility. It is always less than the simple average return.
</div>

<div class="glossary-entry">
<div class="gterm">Covariance matrix <span class="gcat cat-kelly">Kelly</span></div>
A table showing how much different strategies' returns move together. The diagonal shows each strategy's own variance (how volatile it is on its own). The off-diagonal elements show the covariance between pairs of strategies (how much they tend to gain and lose at the same time). In the multi-strategy Kelly formula, the covariance matrix captures diversification benefits: strategies that tend to lose at different times can be combined at higher total leverage than strategies that all lose together.
</div>

#### Risk Concepts

<div class="glossary-entry">
<div class="gterm">Fat tails <span class="gcat cat-risk">Risk</span></div>
The property of real financial returns where extreme events (very large gains or losses) happen far more frequently than a normal bell-curve distribution would predict. A bell curve says a 5-standard-deviation move should happen roughly once in 3.5 million trading days. In financial markets, moves of that magnitude happen every few years. "Fat tails" refers to the fact that the probability curve for returns has thicker ends than a bell curve — meaning extreme events are not as rare as the formula assumes.
</div>

<div class="glossary-entry">
<div class="gterm">Black swan event <span class="gcat cat-risk">Risk</span></div>
An extreme market event that was considered essentially impossible based on historical data — until it happened.
</div>

<div class="glossary-entry">
<div class="gterm">Financial contagion <span class="gcat cat-risk">Risk</span></div>
The cascade effect where one fund's losses force it to sell, causing prices to drop, which causes other funds holding the same positions to also suffer losses, which forces them to sell, and so on.
</div>

<div class="glossary-entry">
<div class="gterm">Model risk <span class="gcat cat-risk">Risk</span></div>
The risk that your trading model is wrong — either because of statistical biases in the backtest (data-snooping, survivorship bias, look-ahead bias) or because market conditions have changed (regime shifts) and the model's edge no longer exists.
</div>

<div class="glossary-entry">
<div class="gterm">Software risk <span class="gcat cat-risk">Risk</span></div>
The risk that your automated trading system contains bugs that cause it to trade differently from what your backtest model specifies. Even small bugs can cause large losses if they result in wrong position sizes, wrong order directions, or trading at incorrect prices.
</div>

<div class="glossary-entry">
<div class="gterm">Operational risk <span class="gcat cat-risk">Risk</span></div>
The risk of loss from physical or infrastructure failures — internet outages, power cuts, computer crashes, or other non-market events that disrupt your trading.
</div>


#### Psychology

<div class="glossary-entry">
<div class="gterm">Loss aversion <span class="gcat cat-psych">Psychology</span></div>
The human tendency to feel the pain of a loss more intensely than the pleasure of an equivalent gain. Often called an irrational bias. Your instinct to avoid large losses protects you from the volatility drag that erodes long-term growth.
</div>




<div class="glossary-entry">
<div class="gterm">Representativeness bias <span class="gcat cat-psych">Psychology</span></div>
The human tendency to give too much weight to recent events and too little weight to long-run averages. In trading, this appears as the urge to modify your strategy immediately after any significant loss — adding a rule that would have avoided that specific loss. This is data-snooping applied in real time: the modification fits the past but may not help (and may actively hurt) future performance. The correct test: run a full backtest of the modified strategy over a long history, not just the recent painful period.
</div>

<div class="glossary-entry">
<div class="gterm">Ensemble average vs. time series average <span class="gcat cat-psych">Psychology</span></div>
The ensemble average asks: "What is the average outcome across many traders playing simultaneously?" The time series average asks: "What is the average outcome for one trader playing repeatedly over time?" For evaluating financial risk, the time series average is the relevant one — because if you go broke, you stop playing. A bet that looks attractive in ensemble terms can be losing in time series terms if variance is high enough, which is why loss aversion is rational.
</div>

  </div>
</div>


## Chapter 7 — Special Topics

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('ch7')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">Chapter 7</span>
      <div>
        <div class="chapter-title">Chapter 7 — Special Topics</div>
        <div class="chapter-subtitle">Mean reversion, cointegration, factor models, seasonal trades, and high-frequency strategies</div>
      </div>
    </div>
    <span class="chapter-arrow" id="ch7-arrow">▼</span>
  </button>
  <div class="chapter-body" id="ch7-body">

### Section 1 — Mean Reversion vs. Momentum — Which Way Will the Price Go?

<div class="note-abstract">
Every profitable trading strategy boils down to one of two beliefs about price behaviour: either prices tend to bounce back toward where they came from (mean reversion), or prices tend to keep going in the same direction (momentum). These two views require completely opposite trading actions — and knowing which regime you are in at any given moment is the central challenge of quantitative trading.
</div>

#### The big ideas

<div class="key-idea"><strong>Mean reversion says: prices that move away from their normal range will eventually come back.</strong> If you believe this, you buy when something has fallen unusually far and sell when it has risen unusually high, waiting for it to snap back. Most pairs of similar stocks (like two gold ETFs, or two bank stocks) tend to mean-revert — their prices do not diverge forever. This is the basis of pair trading.</div>

<div class="key-idea"><strong>Momentum says: prices that are moving in one direction will continue moving that way for a while.</strong> If you believe this, you buy what is already rising and short what is already falling. Momentum is often driven by the slow spread of news — as more investors gradually discover and react to a company's improving earnings, the price keeps drifting up for days or weeks. PEAD (Post-Earnings Announcement Drift) is a classic momentum strategy.</div>

<div class="key-idea"><strong>The same price can be both mean-reverting and trending, depending on the time horizon.</strong> Over minutes or hours, a price might bounce around a recent average (mean-reverting). Over weeks, it might be in a long upward trend (momentum). This is why the same strategy needs different parameters for different timeframes, and why the regime question never has a single permanent answer.</div>

#### What causes each type of behaviour?

| Cause | Type it creates | Example |
|---|---|---|
| News diffusing slowly to investors | Momentum | Earnings beat — price drifts up for weeks as more investors react |
| A large institution executing a big order gradually | Momentum | Fund buying 10 million shares over several days — price trends up |
| Herd behaviour — following what others are doing | Momentum | Meme stocks (GameStop, 2021) — price goes to irrational extremes |
| Liquidity events — forced selling for unrelated reasons | Mean reversion | Fund forced to liquidate — price overshoots, then recovers |
| Two fundamentally linked stocks temporarily diverge | Mean reversion | GLD and GDX — gold ETF and gold miners drift apart, then reconnect |

#### Pitfalls specific to mean-reversion backtests

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

### Section 2 — Regime Changes and Conditional Parameter Optimization

<div class="note-abstract">
Markets shift between different "regimes" — periods when mean reversion works well, periods when momentum dominates, periods of high volatility, low volatility, and so on. The problem is that trading strategy parameters optimised for one regime often work poorly in another. Conditional Parameter Optimization (CPO) is a machine-learning approach that lets the strategy's own parameters adapt to the current market conditions every single day .
</div>

#### The big ideas

<div class="key-idea"><strong>Most strategies use fixed parameters that cannot adapt to changing markets.</strong> Standard optimisation picks one set of parameters (entry threshold, lookback window, hedge ratio) that worked best on historical data, then keeps those settings forever. When the market regime changes, the fixed parameters become suboptimal — and there is no automatic mechanism to update them.</div>

<div class="key-idea"><strong>CPO uses machine learning to pick the best parameters for tomorrow based on today's market conditions.</strong> Instead of predicting whether a stock will go up or down (which everyone is trying to do), CPO predicts which combination of your strategy's own parameters will generate the best return tomorrow given the current technical indicators and market environment. This is a much less crowded prediction target.</div>

<div class="key-idea"><strong>CPO is transparent — your strategy still makes the actual trading decisions.</strong> Machine learning is often criticised as a black box. In CPO, the trading strategy (e.g., a Bollinger Band mean-reversion rule) still decides what to buy and sell. The ML only optimises the input parameters. This preserves interpretability while gaining the adaptability benefit of machine learning.</div>

#### Example

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

The PredictNow.ai API (predictnow.ai) provides the ML prediction service used in this example. Sample code is available in the book.

<div class="ex-lesson"><strong>Takeaway:</strong> The key insight is that CPO is predicting the performance of your own strategy's parameters — not predicting gold's price directly. That is a much harder problem for competitors to arbitrage away, and it is why CPO tends to work when generic ML applied to price prediction does not.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Regime</span> <span class="ref-tag">CPO</span> <span class="ref-tag">Walk Forward Optimization</span> <span class="ref-tag">Bollinger bands</span> <span class="ref-tag">Machine learning</span>
</div>

---

### Section 3 — Stationarity and Cointegration — The Science of Pair Trading

<div class="note-abstract">
Pair trading works because some pairs of stocks do not diverge forever — their price relationship is "sticky" in a statistical sense. The technical name for this stickiness is cointegration. If two stocks are cointegrated, you can combine their prices (long one, short the other) to form a spread that bounces around a stable average indefinitely. That spread is stationary — and a stationary series is almost perfectly suited for a mean-reversion strategy. But cointegration is not the same as correlation, and confusing the two leads to bad pair selections.
</div>

#### The big ideas

<div class="key-idea"><strong>A stationary time series is one that stays close to its average instead of wandering away forever.</strong> Most individual stock prices are not stationary — they just drift further and further from where they started. But the spread between two carefully chosen, related stocks can be stationary, meaning it keeps bouncing back toward the same average level. A stationary spread is ideal for a mean-reversion strategy because it guarantees the spread will revert — as long as the stationarity persists.</div>

<div class="key-idea"><strong>Cointegration is not the same as correlation — and the difference matters enormously.</strong> Correlation measures how much two stocks move in the same direction on a day-to-day basis. Cointegration measures whether their long-run price relationship is stable. Two stocks can be highly correlated (moving in the same direction most days) but completely non-cointegrated (their prices drift further and further apart over years). Conversely, two stocks can be cointegrated (their combined spread stays stable long-term) while being largely uncorrelated on a daily basis.</div>

<div class="key-idea"><strong>Not all stocks from the same industry are cointegrated — you have to test.</strong> It might seem obvious that Coca-Cola and Pepsi, being in the same industry, would be cointegrated. Testing shows they are not — their prices do drift apart over time despite moving in the same direction most days. GLD and GDX, on the other hand, are cointegrated — long GLD, short ~1.63 shares of GDX gives a spread that remains stationary.</div>

#### Cointegration vs. correlation — the key distinction

| Property | Correlation | Cointegration |
|---|---|---|
| **Measures** | Whether daily returns move together | Whether the price *relationship* is stable long-term |
| **Time horizon** | Short-term (day by day) | Long-term (months to years) |
| **What it guarantees** | Nothing about where prices end up | That the weighted spread won't drift away forever |
| **Useful for** | Risk management, beta hedging | Pair trading — finding mean-reverting spreads |
| **KO vs. PEP** | Correlation = 0.48 (statistically significant) | Not cointegrated — prices drift apart |
| **GLD vs. GDX** | Some correlation | Cointegrated — spread stays stationary |

#### Examples from the book

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

### Section 4 — Factor Models — What Actually Drives Stock Returns?

<div class="note-abstract">
Financial commentators often say things like "the market is favouring value stocks" or "small-cap stocks are outperforming." Factor models are the mathematical framework that makes these casual observations precise. A factor model says: a stock's return can be broken down into contributions from a small number of common drivers (factors) plus a random component specific to that stock. Understanding which factors are driving returns right now is one of the most powerful tools in a quant trader's toolkit.
</div>

#### The big ideas

<div class="key-idea"><strong>A factor model explains stock returns using a small number of common market forces.</strong> Instead of trying to predict each stock individually, a factor model says that most of a stock's return comes from broad forces that affect many stocks at once — things like "the market went up today" or "small-cap stocks outperformed today." These broad forces are called factors. The part that a factor model cannot explain is called the specific return — essentially just noise specific to that one company.</div>

<div class="key-idea"><strong>The Fama-French Three-Factor model is the most famous example.</strong> It says a stock's return depends on three things: (1) the overall market return (beta), (2) whether small-cap stocks outperformed large-cap stocks that day (the SMB factor), and (3) whether cheap (value) stocks outperformed expensive (growth) stocks that day (the HML factor). Factor models like this have been shown to explain a large fraction of most stocks' returns without knowing anything specific about those companies.</div>

<div class="key-idea"><strong>Principal Component Analysis (PCA) finds factors automatically from historical data without needing to define them in advance.</strong> Instead of deciding upfront that "small-cap vs. large-cap" is a factor, PCA just looks at the pattern of historical stock returns and finds the directions of maximum variation. The result is a set of statistical factors that are mathematically guaranteed to be uncorrelated — even if their economic interpretation is not always obvious.</div>

#### The Fama-French Three-Factor model explained simply

| Factor | What it measures | Example exposure |
|---|---|---|
| **Market (beta)** | How much does this stock move when the whole market moves? | Beta = 1.5 means the stock moves 1.5× the market |
| **SMB (small minus big)** | Does this stock behave more like small-cap or large-cap? | A micro-cap stock has positive SMB exposure |
| **HML (high minus low)** | Is this a value stock (cheap) or growth stock (expensive)? | A stock with a low P/E ratio has positive HML exposure |

#### Example from the book

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

### Section 5 — When Should You Exit a Trade?

<div class="note-abstract">
Entry signals get all the attention in trading strategy design, but exit signals are just as important — and often more so. Getting out at the wrong time can turn a winning strategy into a losing one. The right exit approach depends entirely on whether your strategy is mean-reverting or momentum-based, and treating these two types the same way is a common and costly mistake.
</div>

#### The big ideas

<div class="key-idea"><strong>For mean-reverting strategies, the half-life of mean reversion tells you how long to hold a position.</strong> The Ornstein-Uhlenbeck formula describes how a mean-reverting spread decays back to its average. By fitting this formula to historical spread data, you can calculate the "half-life" — the expected time for the spread to move halfway back toward its mean. This is your natural holding period, and you can estimate it from the entire historical time series, not just from the limited number of actual trades.</div>

<div class="key-idea"><strong>For momentum strategies, the optimal holding period is shorter than you think — and getting shorter over time.</strong> Momentum is driven by information diffusing slowly to investors. As news spreads faster (more financial media, faster internet, more active quant traders), the diffusion completes sooner, and prices reach their new equilibrium faster. A momentum strategy that needed a week-long holding period five years ago might only work with a one-day holding period today.</div>

<div class="key-idea"><strong>Stop losses work for momentum strategies but hurt mean-reverting strategies.</strong> In a momentum strategy, a reversal in price direction is a genuine signal that the trend has ended — exiting at a loss makes sense. In a mean-reverting strategy, a price moving further away from the mean is not a signal of a trend change — it is just the spread overshooting temporarily. Exiting with a stop loss in this case locks in a loss at exactly the wrong moment — right before the reversal that your strategy was counting on.</div>

#### Exit strategy decision tree

| Strategy type | Normal exit | Alternative exit | Stop loss? |
|---|---|---|---|
| **Mean-reversion** | Fixed holding period = half-life of mean reversion | Target price = historical mean (µ) | ❌ No — exits at the worst moment |
| **Momentum** | Fixed holding period (backtested) | Opposite entry signal fires | ✅ Yes — a price reversal signals the trend has ended |

#### The Ornstein-Uhlenbeck half-life formula

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

#### Example from the book

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

### Section 6 — Seasonal Trading Strategies

<div class="note-abstract">
Some patterns in financial markets repeat at roughly the same time every year, driven by recurring real-world events — tax deadlines, seasonal demand for energy, agricultural harvests, summer driving. Seasonal trading strategies try to exploit these predictable patterns. The key finding from the book: seasonal effects in stock markets have mostly disappeared over the years as they became widely known, but seasonal effects in commodity futures are alive and well because they are driven by genuine physical demand cycles, not investor psychology.
</div>

#### The big ideas

<div class="key-idea"><strong>Seasonal equity strategies like the "January effect" have largely stopped working.</strong> The January effect — where small-cap stocks that fell the most in December tend to recover in January (as tax-loss selling pressure reverses) — was well-documented for decades. But once enough traders knew about it and started buying in late December in anticipation, the effect was arbitraged away. The backtested version looks great; the out-of-sample version often does not.</div>

<div class="key-idea"><strong>Commodity futures seasonal strategies are still profitable because they are driven by real economic needs, not investor psychology.</strong> Gasoline demand rises every spring as summer driving season approaches. Natural gas demand rises as summer air conditioning kicks in. These patterns are driven by physical reality, not by traders' beliefs about other traders — making them harder to arbitrage away completely.</div>

<div class="key-idea"><strong>Seasonal commodity strategies only trade once a year — so you need out-of-sample validation to trust them.</strong> When a strategy only triggers once per year, a 10-year backtest only gives you 10 data points. That is not enough to statistically validate that the pattern is real and not just coincidence. The book explicitly marks the post-2007 results for gasoline and natural gas as out-of-sample, which is essential honesty — and those results are what actually matter.</div>

#### Examples from the book

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

### Section 7 — High-Frequency Trading

<div class="note-abstract">
High-frequency trading (HFT) strategies do not hold positions overnight — and often hold for only seconds or minutes. Their defining advantage is the law of large numbers: with thousands of small bets per day, even a tiny average edge per trade compounds into impressive daily consistency. This consistency translates into very high Sharpe ratios, which, as we know from Chapter 6, allows aggressive leverage and very high returns on capital. But the barriers to entry — speed, infrastructure, capital, and technical expertise — are genuinely high.
</div>

#### The big ideas

<div class="key-idea"><strong>HFT generates high Sharpe ratios through the law of large numbers.</strong> If your strategy has a tiny but genuine edge on every trade, doing that trade 1,000 times per day means the daily result will be very close to 1,000 × the average edge per trade — with very little variance. This is pure mathematics: more independent bets of the same type produce more stable outcomes. High Sharpe ratios, from Chapter 6, unlock the highest possible compounded growth.</div>

<div class="key-idea"><strong>Transaction costs and speed are everything in HFT — more so than the trading idea itself.</strong> A strategy that generates 0.01% profit per trade before costs might generate 0.005% after costs — or be completely unprofitable if costs are slightly higher. Unlike daily strategies where costs are a significant but manageable concern, HFT lives or dies entirely on execution quality. Professional HFT firms co-locate servers physically next to exchange matching engines to shave microseconds off execution time.</div>

<div class="key-idea"><strong>Backtesting HFT strategies is much harder than backtesting daily strategies — and often unreliable.</strong> Reliable HFT backtesting requires tick-by-tick data with bid and ask prices (not just last trade prices), historical order book data, and a highly realistic market simulator that accounts for queue position, partial fills, and latency. Without all of this, HFT backtests are essentially meaningless. Often the only true test is to run the strategy live with small capital.</div>

#### HFT vs. daily strategies — a comparison

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

### Section 8 — Low-Beta vs. High-Beta — Which Is the Better Portfolio?

<div class="note-abstract">
If you want more return, you could either apply more leverage to a low-risk portfolio or switch to a portfolio of high-risk (high-beta) stocks. Both seem like they should give the same result. But they do not — and the reason why connects directly back to the Kelly formula and Sharpe ratios from Chapter 6.
</div>

#### The big ideas

<div class="key-idea"><strong>Higher beta does not automatically mean higher compounded growth — it just means higher average return and higher risk in equal proportion.</strong> The Fama-French model says that a stock's return is proportional to its beta. So doubling the beta of your portfolio doubles the average return — but it also doubles the volatility. From the Kelly formula (Chapter 6), compounded growth rate depends on Sharpe ratio squared, not raw return. If doubling beta doubles both return and volatility, the Sharpe ratio stays the same and compounded growth stays the same.</div>

<div class="key-idea"><strong>Empirically, low-beta stocks tend to have higher Sharpe ratios than high-beta stocks.</strong> This is a consistent empirical finding: the market tends to underprice low-beta stocks and overprice high-beta stocks (perhaps because many investors cannot use leverage and therefore chase beta as a substitute). A portfolio of low-beta stocks, properly levered using the Kelly formula, will beat a portfolio of high-beta stocks in long-run compounded wealth — because the lower volatility allows more aggressive optimal leverage.</div>

<div class="key-idea"><strong>The practical implication: prefer low-beta, then lever up.</strong> Dr. Edward Qian at PanAgora Asset Management showed that the traditional 60/40 stock-bond portfolio is not optimal — it has too much risk concentration in stocks. A 23% stocks / 77% bonds portfolio, levered up to match the same risk level, achieves a higher Sharpe ratio and therefore higher long-run compounded wealth. The insight: diversify first, lever second.</div>

<div class="ref-tags">
<span class="ref-tag">Beta</span> <span class="ref-tag">Low-beta portfolio</span> <span class="ref-tag">Leverage</span> <span class="ref-tag">Kelly formula</span> <span class="ref-tag">Fama-French</span> <span class="ref-tag">Risk parity</span>
</div>

---

### Term Glossary

Definitions for every key terms.

#### Statistical Concepts

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

#### Models & Frameworks

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

#### Exit Strategies

<div class="glossary-entry">
<div class="gterm">Fixed holding period <span class="gcat cat-exit">Exit</span></div>
The simplest exit strategy: hold every trade for a pre-set number of days (or hours, or minutes) and then close it regardless of profit or loss. For mean-reverting strategies, the optimal holding period is typically the half-life of mean reversion calculated from the OU formula.
</div>

<div class="glossary-entry">
<div class="gterm">Opposite entry signal exit <span class="gcat cat-exit">Exit</span></div>
Exiting a position when the same strategy that generated the original entry signal now generates an opposite signal. For a momentum strategy: if you entered long because the signal said "bullish" and now the signal says "bearish," exit the long. This is a principled alternative to stop losses that is directly justified by the logic of the strategy itself, without introducing an arbitrary extra parameter.
</div>

#### Seasonal & HFT

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

  </div>
</div>

