---
layout: distill
title: "Quantitative Trading — Complete Study Notes (All Chapters)"
description: Comprehensive study notes on Ernest P. Chan's Quantitative Trading (2nd Ed.) covering all chapters — from strategy sources and backtesting to execution, risk management, and statistical arbitrage. Each chapter is collapsible for easy navigation.
tags: Finance Quant Trading Notes Complete Reference
giscus_comments: true
date: 2026-04-01
featured: true
thumbnail: https://m.media-amazon.com/images/I/51s4givoDeL._SY445_SX342_ML2_.jpg

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

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
  .pill-tip    { background: #fff3cd; color: #856404; }
  .pill-puzzle { background: #fff3cd; color: #856404; }
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
  .cat-platform { background: #d1fae5; color: #064e3b; }
  .cat-method   { background: #ede8fc; color: #3c2a8a; }
  .cat-kelly    { background: #d1fae5; color: #064e3b; }
  .cat-psych    { background: #ede8fc; color: #3c2a8a; }
  .cat-market   { background: #dbeafe; color: #1e3a8a; }
  .cat-strategy { background: #d1fae5; color: #064e3b; }
  .cat-stats    { background: #dbeafe; color: #1e3a8a; }
  .cat-model    { background: #fef3c7; color: #78350f; }
  .cat-exit     { background: #fce7f3; color: #831843; }
  .cat-seasonal { background: #ede8fc; color: #3c2a8a; }
  .cat-system   { background: #d1fae5; color: #064e3b; }
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
  .checklist {
    list-style: none;
    padding: 0;
    margin: 0.5rem 0;
  }
  .checklist li {
    padding: 0.3rem 0;
    font-size: 0.9rem;
    color: #333;
    border-bottom: 1px dotted #eee;
    display: flex;
    align-items: flex-start;
    gap: 0.5rem;
  }
  .checklist li:last-child { border-bottom: none; }
  .checklist li::before {
    content: "→";
    color: #5b7de8;
    flex-shrink: 0;
  }
  table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.88rem; }
  th { background: #f0f4ff; text-align: left; padding: 7px 10px; border: 1px solid #ddd; }
  td { padding: 7px 10px; border: 1px solid #ddd; vertical-align: top; }
  
  /* Collapsible chapter styles */
  .chapter-container {
    margin: 1.5rem 0;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    background: #fafafa;
  }
  .chapter-summary {
    padding: 1rem;
    font-weight: 600;
    font-size: 1.05rem;
    cursor: pointer;
    user-select: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #1a1a2e;
  }
  .chapter-summary:hover {
    background: #f0f0f0;
  }
  .chapter-summary::before {
    content: "▸";
    display: inline-block;
    font-size: 0.9rem;
    transition: transform 0.2s ease;
  }
  .chapter-container details[open] .chapter-summary::before {
    transform: rotate(90deg);
  }
  .chapter-content {
    padding: 0 1rem 1rem 1rem;
    border-top: 1px solid #e0e0e0;
  }

---

# Quantitative Trading — Complete Study Notes

A comprehensive reference combining all study chapters from Ernest P. Chan's *Quantitative Trading (2nd Ed.)*. Click any chapter below to expand its contents.

---

## Quick Navigation

This document contains notes on chapters 2, 3, 5, 6, and 7 covering:
- **Chapter 2**: Strategy sources, personal fit, capital, and performance metrics
- **Chapter 3**: Backtesting methodology, tools, data sources, and common mistakes
- **Chapter 5**: Building trading systems, execution, paper trading, and live trading diagnostics
- **Chapter 6**: Position sizing, the Kelly formula, risk management, and psychology
- **Chapter 7**: Statistical arbitrage strategies from mean reversion to high-frequency trading

---

<div class="chapter-container">
<details>
<summary class="chapter-summary">Chapter 2 — Strategy Sources, Personal Fit & Performance Measurement</summary>
<div class="chapter-content">

## Section 1 — Core Thesis & Idea Sources

<div class="note-abstract">
There's no shortage of trading ideas—they are everywhere, open, and free. The real difficulty is not finding them, but knowing which ones are worth your time before you even start backtesting. In that sense, trading is less about discovery and more about curation: filtering out noise and recognizing signal early.
</div>

### Core ideas

<div class="key-idea"><strong>Modification is the real alpha source.</strong> Public strategies are often just shared building blocks. The real edge comes from how they are adapted—through choices like holding period, asset selection, and timing. Most "secret" ideas are already widely known; what truly matters is the execution and how they are engineered.</div>

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
A strategy is only as good as its fit with the trader's personal constraints. Even the most theoretically strong strategy is useless if it cannot be executed, funded, or psychologically maintained. Before assessing any strategy on its merits, it is essential to first evaluate four dimensions—time, skill, capital, and objectives—to define what is actually feasible. Fit comes before merit.
</div>

### Core ideas

<div class="key-idea"><strong>Personal fit is assessed before analytical merit.</strong> A great strategy requiring full-time monitoring is not a great strategy for a part-time trader. Establish the feasible set first, then evaluate strategies within it.</div>

<div class="key-idea"><strong>Buy-and-hold is not necessarily optimal for long-term capital growth.</strong> In theory, higher growth can be achieved by identifying strategies with strong risk-adjusted returns and applying optimal leverage.</div>

<div class="key-idea"><strong>Trading frequency and income regularity are directly coupled.</strong> Generating consistent monthly income generally requires shorter holding periods. As holding periods increase, profit and loss become more volatile, making returns less predictable—even if the long-term average return is high.</div>

---

## Section 3 — Capital & Leverage

<div class="note-abstract">
Capital is more than just money—it sets the boundaries for everything else. It decides what markets you can trade, how much leverage you can use, what data you can realistically access, and which strategies are feasible in the first place. It's less a preference and more a hard filter.
</div>

### Core ideas

<div class="key-idea"><strong>Capital determines the feasible strategy universe more than skill does.</strong> Different capital levels open structurally different strategy spaces across instruments, leverage, and data quality.</div>

<div class="key-idea"><strong>Low-capital traders should use futures, FX, and options — not stocks.</strong> The leverage embedded in these instruments compensates for limited capital in ways that direct stock ownership cannot.</div>

<div class="key-idea"><strong>Dollar-neutral portfolios require double the capital for the same gross exposure.</strong> This arithmetic constraint makes market-neutral strategies inaccessible without portfolio margin at ~$100K minimum NAV.</div>

---

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

</div>
</details>
</div>

<div class="chapter-container">
<details>
<summary class="chapter-summary">Chapter 3 — Backtesting: Tools, Data & Common Mistakes</summary>
<div class="chapter-content">

## Section 1 — What Is Backtesting and Why Should You Do It Yourself?

<div class="note-abstract">
Backtesting is simply running a trading strategy on historical data to see how it would have done in the past. Think of it like a practice exam before the real test. Even if someone hands you a strategy with all the details and historical results already written up, you should still run it yourself — because doing so forces you to truly understand it, catch any hidden mistakes, and spot ways to make it even better.
</div>

### Core ideas

<div class="key-idea"><strong>Running it yourself is the proof that you understand it.</strong> If you cannot reproduce someone else's backtest results step by step, you do not really understand the strategy well enough to bet real money on it. The process of replication forces you to confront every assumption and decision.</div>

<div class="key-idea"><strong>Other people make mistakes — and you need to catch them.</strong> Published strategies can contain hidden errors like using tomorrow's data to make today's trade decisions. These mistakes are invisible in a write-up but jump out when you actually build the code and run it yourself.</div>

<div class="key-idea"><strong>Your own backtest opens the door to improvements.</strong> Once you can reproduce a strategy, you can start tweaking it — try a different entry time, a different set of stocks, a different holding period. Often these small tweaks turn a mediocre strategy into a great one.</div>

---

## Section 2 — Which Tool Should You Use?

<div class="note-abstract">
Picking the right tool for backtesting matters more than most people think. It is not just about personal preference — the tool you choose determines what kinds of mistakes you are likely to make, how fast you can test ideas, and how complex a strategy you can realistically build. The best tool is the simplest one that can handle your strategy.
</div>

### Core ideas

<div class="key-idea"><strong>Simpler tools force simpler strategies — and that is often a good thing.</strong> Excel shows you everything on screen at once, which makes it almost impossible to accidentally use tomorrow's data in today's trading decision. Its limitation to simpler models is actually a safety feature.</div>

<div class="key-idea"><strong>MATLAB is still the best choice for serious quant research, despite Python's popularity.</strong> It runs faster, has better built-in statistics tools, and comes with real customer support. Python is free and widely used, but its packages frequently conflict with each other, it is slower, and there is no one to call when something breaks.</div>

<div class="key-idea"><strong>Web platforms like QuantConnect and Blueshift solve the data problem for you.</strong> These platforms come bundled with years of historical data and let you switch from backtesting to live trading without rewriting any code — which is a big deal, because a lot can go wrong in that translation.</div>

---

## Section 3 — Where Do You Get Historical Data?

<div class="note-abstract">
Getting historical data is the easy part — the internet is full of free sources. The hard part is understanding what problems are hiding inside that data. Three issues silently ruin most backtests: prices that have not been corrected for stock splits or dividends, databases that are missing stocks that went bankrupt, and noisy daily high and low prices that are less reliable than they look.
</div>

### Core ideas

<div class="key-idea"><strong>Always use prices that have been adjusted for stock splits and dividends.</strong> When a company splits its stock 2-for-1, the price drops by half overnight — but nothing actually changed for shareholders. If your data is not adjusted, your backtest sees a huge fake price drop and generates a false buy signal.</div>

<div class="key-idea"><strong>Databases that are missing bankrupt companies make strategies look much better than they really are.</strong> If your database only includes stocks that are still trading today, you are missing all the ones that went bust. A "buy cheap" strategy looks amazing in this kind of biased data — because you never see the cheap stocks that went to zero. This is called survivorship bias.</div>

<div class="key-idea"><strong>Daily high and low prices are unreliable — stick to open and close wherever possible.</strong> The day's high or low is often set by a single tiny trade, a data entry error, or a trade on a different exchange. Any strategy that assumes you can buy at exactly the daily low or sell at exactly the daily high will look better in backtest than it ever will in real trading.</div>

---

## Section 4 — How Do You Measure If a Strategy Is Good?

<div class="note-abstract">
Most people judge a trading strategy by how much money it made. But raw returns are misleading because they do not tell you how much risk was taken to earn them. A strategy that made 20% by putting everything on one risky bet is far worse than one that made 15% through smooth, consistent gains. The Sharpe ratio, maximum drawdown, and MAR ratio together give you a much more honest and complete picture.
</div>

### Core ideas

<div class="key-idea"><strong>The Sharpe ratio tells you how much you are earning per unit of risk taken.</strong> Think of it as asking: "How smooth and consistent were your gains?" A high Sharpe ratio means you made money reliably without wild swings. A low Sharpe ratio means the returns were bumpy and unreliable. Anything below 1 generally means the strategy is not worth running on its own.</div>

---

## Section 5 — What Are the Most Common Mistakes?

<div class="note-abstract">
The frustrating thing about backtesting mistakes is that they almost always make a strategy look better than it really is. The two biggest culprits are accidentally using future information to make past trading decisions (look-ahead bias), and tuning a model so precisely to historical patterns that it stops working on new data (data-snooping bias). Both are sneaky, both are common, and both have practical tests that can catch them.
</div>

### Core ideas

<div class="key-idea"><strong>Look-ahead bias means your backtest accidentally used information that was not yet available at the time of the trade.</strong> A simple example: your entry rule says "buy if today's price is within 1% of today's lowest price." But you cannot know what today's lowest price is until the market closes! Using that information to make a trade decision earlier in the day is cheating — and it makes the backtest look better than it ever could in real life.</div>

<div class="key-idea"><strong>There is a simple test to catch look-ahead bias: chop off the end of your data and see if anything changes.</strong> Run your full backtest and save the trading positions. Then delete the most recent 60 days of data and run it again. Compare the positions for the overlapping period. If they differ even slightly, your program is peeking at future data — you have look-ahead bias to fix.</div>

<div class="key-idea"><strong>Data-snooping bias is what happens when you tune a strategy too precisely to the past.</strong> Imagine testing 500 different combinations of settings until you find one that looks incredible on your historical data. Almost certainly, that "incredible" result is just a coincidence — you found the settings that happened to fit historical noise, not a real market pattern.</div>

</div>
</details>
</div>

<div class="chapter-container">
<details>
<summary class="chapter-summary">Chapter 5 — Automated Trading Systems & Paper Trading</summary>
<div class="chapter-content">

## Section 1 — What Does an Automated Trading System Actually Do?

<div class="note-abstract">
An automated trading system (ATS) is the software that turns your trading idea into real orders. It grabs the latest market prices, runs your strategy to figure out what to buy and sell, and sends those orders to your broker automatically. Without this, you are back to manually clicking "buy" and "sell" all day — which defeats the whole point of quantitative trading.
</div>

### Core ideas

<div class="key-idea"><strong>An ATS does three things in sequence: get data, generate orders, send orders.</strong> It pulls fresh price data from your broker or a data service, feeds that data into your trading algorithm, and transmits the resulting orders to your brokerage account. These three steps can happen every second for high-frequency strategies, or just once before the market opens for slower daily strategies.</div>

<div class="key-idea"><strong>Fully automated systems are no longer only for professional programmers.</strong> A few years ago, building a system that communicated directly with a broker's API required writing code in Java or C++. Today, platforms like QuantConnect and Blueshift handle all of that for you. You can build and run a fully automated system knowing only Python — or in Blueshift's case, no coding at all.</div>

---

## Section 2 — How Do You Keep Trading Costs as Low as Possible?

<div class="note-abstract">
We already know from Chapter 3 that transaction costs can destroy a strategy that looks great on paper. Chapter 5 adds the execution layer: there are specific things you can do at the time of placing orders — not just in the strategy design — to keep costs manageable. The core insight is simple: do not trade too large a slice of a stock's daily volume, and avoid very cheap low-priced stocks entirely.
</div>

### Core ideas

<div class="key-idea"><strong>Never trade more than 1% of a stock's average daily trading volume in a single order.</strong> When your order is large relative to how much of that stock normally trades in a day, you start moving the price against yourself just by trying to buy or sell. Sticking to under 1% of average daily volume keeps your market impact small.</div>

<div class="key-idea"><strong>Avoid stocks priced below $5.</strong> Institutional traders have a well-known rule: skip stocks under $5. Two reasons: first, you need to buy far more shares to deploy the same capital, which means more commission. Second, cheap stocks have wider bid-ask spreads as a percentage of their price, making every trade more expensive.</div>

---

## Section 3 — Paper Trading — The Essential Safety Net

<div class="note-abstract">
Paper trading means running your automated system on real live market data — but with fake money. It is the only practical way to catch software bugs, discover timing problems, and verify that your system actually behaves the way your backtest predicted. Skipping paper trading is one of the most common and costly mistakes new traders make.
</div>

### Core ideas

<div class="key-idea"><strong>Paper trading reveals bugs that backtesting simply cannot.</strong> Backtesting uses historical data that just sits there passively. Paper trading runs against live market data in real time, exposing timing issues, data feed problems, order routing failures, and look-ahead bias that only shows up when you cannot actually obtain certain data before placing a trade.</div>

<div class="key-idea"><strong>Paper trading builds genuine intuition that backtesting never can.</strong> Running a backtest shows you the performance statistics. Running a paper trading system for a month shows you what the strategy actually feels like — how much the P&L swings day to day, how much capital gets tied up at peak, how many trades fire on a typical day, and what unexpected operational headaches arise.</div>

<div class="key-idea"><strong>The timing surprises are always bigger than expected.</strong> Downloading and processing data each morning took about 20 minutes. Transmitting all orders to the broker account took another 15 minutes. Total: 35 minutes of preparation before the market opens.</div>

### A practical paper trading checklist

<ul class="checklist">
  <li>Run the paper trading system on a real brokerage paper account, not just a simulation you wrote yourself</li>
  <li>Compare paper trade results daily against what your backtest program generates for the same data — differences reveal bugs</li>
  <li>Time every operational step: how long does data download take? Order generation? Transmission?</li>
  <li>Observe P&L swings day-to-day — are they larger or smaller than the backtest suggested?</li>
  <li>Note how much capital is tied up at peak — is it consistent with what you planned?</li>
  <li>Run for at least a month before going live with real money</li>
</ul>

---

## Section 4 — Why Does Live Trading Sometimes Disappoint?

<div class="note-abstract">
You have done everything right. You backtested carefully, paper traded for a month, and went live. Three months later, the strategy is barely breaking even — or losing money. This section gives you a systematic way to diagnose what went wrong, starting with the simplest possible fixes and working up to the hardest truths.
</div>

### Core ideas

<div class="key-idea"><strong>Start with the simplest diagnoses first — most problems are not mysterious.</strong> Before assuming something deep and structural has gone wrong, check the obvious things: Does your live system actually match your backtest program trade for trade? Are the execution costs higher than you modelled? Are you accidentally trading illiquid stocks that cause large market impact?</div>

<div class="key-idea"><strong>If simple fixes do not work, face the two hardest possibilities: data-snooping bias and regime shifts.</strong> Data-snooping bias means the strategy was overfit to historical noise — it never had a real edge. Regime shifts mean the market structure has genuinely changed, so a strategy that worked before no longer works now.</div>

### Your live trading diagnostic checklist

<ul class="checklist">
  <li><strong>Do the trades match?</strong> Compare every trade your live system generates against what your backtest would have generated for the same data on the same day. If they differ, there is a bug to fix.</li>
  <li><strong>Are execution costs higher than expected?</strong> Add up what you are actually paying in commissions, spreads, and slippage. Compare to your backtest assumptions.</li>
  <li><strong>Are you trading illiquid stocks?</strong> Check whether your orders are routinely exceeding 1% of average daily volume.</li>
  <li><strong>Does the strategy survive simplification?</strong> Remove parameters and rules one by one. If backtest performance collapses immediately, data-snooping bias is likely.</li>
</ul>

</div>
</details>
</div>

<div class="chapter-container">
<details>
<summary class="chapter-summary">Chapter 6 — Position Sizing, Kelly Formula & Risk Management</summary>
<div class="chapter-content">

## Section 1 — The Core Question — How Much Should You Bet?

<div class="note-abstract">
How much capital you allocate to each trade is one of the most consequential decisions you will make. Get it right, and you can turn a modest edge into substantial wealth. Get it wrong, and even winning strategies lead to catastrophic losses. Yet most traders decide position size based on gut feeling or arbitrary rules rather than principled mathematics.
</div>

### Core ideas

<div class="key-idea"><strong>Position size is the primary lever for controlling risk and wealth growth.</strong> A great strategy with poor position sizing will underperform a mediocre strategy with excellent position sizing. Position size is more important than the underlying edge.</div>

<div class="key-idea"><strong>Overbetting causes ruin even when your edge is real.</strong> You can be right 60% of the time and still go broke if you bet too much on each trade. The outcome depends not just on win rate, but on the interaction between win rate, win/loss ratio, and position size.</div>

---

## Section 2 — The Kelly Formula — Your Optimal Leverage Calculator

<div class="note-abstract">
The Kelly criterion is the mathematically optimal bet size that maximizes long-term wealth growth. It is derived from information theory and has been validated by decades of trading practice. The formula is simple, but applying it requires honest estimates of your strategy's win rate and payoff ratio.
</div>

### Core ideas

<div class="key-idea"><strong>The Kelly formula tells you the optimal fraction of capital to risk on each trade.</strong> It balances the competing pressures: larger bets grow wealth faster, but larger bets also increase the probability of catastrophic loss. Kelly finds the mathematical sweet spot.</div>

<div class="key-idea"><strong>Most traders should use half-Kelly or quarter-Kelly, not full Kelly.</strong> Full Kelly is theoretically optimal, but it assumes you know your win rates and payoff ratios perfectly — which you never do. The margin for estimation error is zero. Using half-Kelly or quarter-Kelly adds a safety buffer.</div>

### The Kelly formula

$$f^* = \frac{p \times b - q}{b}$$

Where:
- $f^*$ = fraction of capital to risk per trade
- $p$ = probability of winning
- $q$ = probability of losing (1 - p)
- $b$ = ratio of profit to loss per trade (win size / loss size)

**Example:** If your strategy wins 55% of the time, and your average win is 1.5× your average loss:
$$f^* = \frac{(0.55 \times 1.5) - 0.45}{1.5} = \frac{0.825 - 0.45}{1.5} = 0.25$$

Risk 25% of your capital per trade (full Kelly). In practice, use 12.5% (half-Kelly) for safety.

---

## Section 3 — Allocating Capital Across Multiple Strategies

<div class="note-abstract">
Most traders run multiple strategies simultaneously. How do you divvy up capital between them? The principle is simple: allocate more capital to strategies with better Sharpe ratios. But implementation requires care, particularly when strategies correlate with each other.
</div>

### Core ideas

<div class="key-idea"><strong>Allocate capital proportionally to Sharpe ratios, not equally across strategies.</strong> A strategy with Sharpe 2.0 should get twice as much capital as one with Sharpe 1.0. This maximizes portfolio-level Sharpe.</div>

---

## Section 4 — Risk Management Beyond the Formula

<div class="note-abstract">
Mathematics can tell you the optimal bet size, but risk management also requires operational decisions and discipline. Stop losses, diversification, and leverage limits all serve to keep you in the game when things go wrong.
</div>

### Core ideas

<div class="key-idea"><strong>Drawdown limits are your most important guardrail.</strong> Set a maximum acceptable drawdown in advance. When you hit it, stop trading until you understand what went wrong. This simple rule saves careers.</div>

<div class="key-idea"><strong>Diversification works, but only if strategies have uncorrelated edges.</strong> Adding a second strategy that looks identical to your first — but trades a different market — is not real diversification if the signal is the same.</div>

---

## Section 5 — Stop Losses — Are They Actually Helpful?

<div class="note-abstract">
Stop losses are controversial. Some traders swear by them; others view them as costly and counterproductive. The truth is more nuanced: stop losses help with risk management and discipline, but they can also lock in losses prematurely and create tax liability.
</div>

### Core ideas

<div class="key-idea"><strong>Stop losses force a choice at the worst moment.</strong> They are most useful for traders prone to "hope bias" — the tendency to hold losing positions hoping for recovery. For disciplined traders, stop losses may do more harm than good.</div>

---

## Section 7 — The Psychological Side of Trading

<div class="note-abstract">
Trading failure is usually psychological, not mathematical. Your strategy may be sound, but overconfidence, fear, or the simple cognitive bias that causes people to hold winners too short and losers too long can destroy returns. Systematizing your trading helps, but psychology remains the hardest part to master.
</div>

### Core ideas

<div class="key-idea"><strong>Overconfidence bias after a great run is the most common destroyer of wealth.</strong> After a few months of strong returns, traders often increase position size or loosen discipline — precisely when the market conditions that made the strategy work are most likely to change.</div>

</div>
</details>
</div>

<div class="chapter-container">
<details>
<summary class="chapter-summary">Chapter 7 — Statistical Arbitrage Strategies</summary>
<div class="chapter-content">

## Section 1 — Mean Reversion vs. Momentum — Which Way Will the Price Go?

<div class="note-abstract">
Two competing forces govern short-term price movements: mean reversion (prices tend to bounce back to normal levels) and momentum (prices tend to continue in the direction they are already moving). Both can be profitable strategies, but they work in different market regimes. Understanding which tendency dominates in your market at your timeframe is critical.
</div>

### Core ideas

<div class="key-idea"><strong>Mean reversion works best on short timeframes; momentum works best on longer ones.</strong> A stock that drops 5% in an hour often bounces back within the day. A stock that has been rising for 6 months often continues rising for another 3 months. The dividing line is fuzzy but real.</div>

<div class="key-idea"><strong>Academic studies often miss the transition point between regimes.</strong> The market can switch from mean-reverting to momentum-driven overnight when volatility or volume conditions change. A strategy that backtests beautifully may break the moment you go live — because the regime shift has already happened.</div>

---

## Section 2 — Regime Changes and Conditional Parameter Optimization

<div class="note-abstract">
A strategy parameter that works in calm markets (low volatility) often fails in choppy markets (high volatility). The solution is not to find a single parameter that works everywhere, but to make your parameters responsive to current market conditions.
</div>

### Core ideas

<div class="key-idea"><strong>Optimize parameters conditional on volatility, not just time.</strong> When volatility spikes, tighten your stops and reduce position size. When volatility is low and stable, you can afford to be more aggressive.</div>

---

## Section 3 — Stationarity and Cointegration — The Science of Pair Trading

<div class="note-abstract">
Pair trading means finding two assets whose prices are linked, then betting on their relationship when it breaks. For example, if stock A usually trades at 1.5× the price of stock B, but this week it dropped to 1.3×, you might buy A and short B, betting the ratio bounces back to 1.5×. The mathematics behind this is cointegration: a test for whether two time series have a stable long-term relationship.
</div>

### Core ideas

<div class="key-idea"><strong>Correlation is not cointegration.</strong> Two stocks can move together (correlated) without being cointegrated. For a pair trade to work, you need a proven stable mathematical relationship between them, not just a historical tendency to rise and fall together.</div>

<div class="key-idea"><strong>Cointegration relationships break down, especially in crisis periods.</strong> When everything is selling off, pairs that were cointegrated often decointegrate. A relationship that held for 10 years can vanish in a week. Always test pair trades on out-of-sample data before risking significant capital.</div>

---

## Section 4 — Factor Models — What Actually Drives Stock Returns?

<div class="note-abstract">
Instead of tracking individual stocks, factor models explain returns as the sum of exposures to a few broad systematic factors: market risk, size (small vs. large companies), value (cheap vs. expensive stocks), momentum, and others. Understanding factors lets you diversify your strategy across sources of returns rather than just across stocks.
</div>

### Core ideas

<div class="key-idea"><strong>Factor exposures persist across market conditions in surprising ways.</strong> The "value factor" (cheap stocks outperforming expensive ones) has been profitable for decades across different time periods, countries, and asset classes — suggesting it represents a genuine market inefficiency or risk premium.</div>

---

## Section 5 — When Should You Exit a Trade?

<div class="note-abstract">
Entry rules get all the attention, but exit rules matter just as much. Exiting too soon leaves profit on the table. Exiting too late locks in losses. The optimal exit depends on your strategy's nature: mean-reversion strategies should exit when price normalizes; momentum strategies should exit when momentum appears to be fading.
</div>

### Core ideas

<div class="key-idea"><strong>Mean-reversion strategies exit when the reversal happens; momentum strategies exit when the trend breaks.</strong> These are opposite rules. Using the wrong exit rule for your strategy type will destroy profitability.</div>

---

## Section 6 — Seasonal Trading Strategies

<div class="note-abstract">
Some patterns repeat predictably throughout the year. October tends to be volatile. January has the "January effect." Certain commodity prices spike before harvest. These seasonal patterns can be exploited, but they are also well-known and increasingly crowded.
</div>

### Core ideas

<div class="key-idea"><strong>Seasonal patterns still exist, but they are small and shrinking.</strong> As more traders learn about them and trade them, the excess returns disappear. A historically 5% August rally might now be 2% — still measurable in a backtest but harder to profit from after costs.</div>

---

## Section 7 — High-Frequency Trading

<div class="note-abstract">
High-frequency strategies operate on microsecond timescales, making thousands of trades per day. They require significant infrastructure investment (fast hardware, direct exchange connections) and are increasingly dominated by well-capitalized firms. For most retail traders, HFT is not practical — but understanding how it works helps explain market microstructure.
</div>

### Core ideas

<div class="key-idea"><strong>High-frequency trading profits from market microstructure — not fundamental value.</strong> HFT strategies exploit the bid-ask spread, short-term order flow imbalances, and latency differentials. The profits are real, but they arise from speed and infrastructure, not alpha.</div>

<div class="key-idea"><strong>High-frequency strategies are fragile and sensitive to tiny cost increases.</strong> A strategy profitable at 0.5 basis point execution cost may be unprofitable at 1.0 basis point. Any change in market structure or regulation that increases costs can destroy years of expected profits instantly.</div>

</div>
</details>
</div>

---

## Notes & References

This combined document integrates study notes from five chapters of Ernest P. Chan's *Quantitative Trading: How to Build Your Own Algorithmic Trading Business (2nd Ed.)*. The original chapter files have been converted to collapsible sections for easier navigation and reference.

**Best used as a quick reference guide.** For deeper understanding, refer to the original individual chapter posts or to the book itself.

---

*Last updated: April 2026*
