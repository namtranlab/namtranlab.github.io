---
layout: distill
title: "Quantitative Trading — Chapter 3 Study Notes"
description: Friendly notes on Chapter 3 of Quantitative Trading (2nd Ed.) — what backtesting is, which tools to use, where to get data, how to measure results, what mistakes to avoid, and a plain-English glossary.
tags: Finance Quant Trading Backtesting Notes
giscus_comments: true
date: 2026-03-15
featured: true
thumbnail: https://m.media-amazon.com/images/I/51s4givoDeL._SY445_SX342_ML2_.jpg

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Section 1 — What Is Backtesting and Why Should You Do It Yourself?
  - name: Section 2 — Which Tool Should You Use?
  - name: Section 3 — Where Do You Get Historical Data?
  - name: Section 4 — How Do You Measure If a Strategy Is Good?
  - name: Section 5 — What Are the Most Common Mistakes?
  - name: Section 6 — How Do Transaction Costs Destroy Strategies?
  - name: Section 7 — How Do You Improve a Strategy That Is Not Working?
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
  .cat-data     { background: #dbeafe; color: #1e3a8a; }
  .cat-risk     { background: #fce8e6; color: #7f1d1d; }
  .cat-perf     { background: #fef3c7; color: #78350f; }
  .cat-platform { background: #d1fae5; color: #064e3b; }
  .cat-bias     { background: #dcfce7; color: #14532d; }
  .cat-cost     { background: #fce7f3; color: #831843; }
  .cat-method   { background: #ede8fc; color: #3c2a8a; }
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
  table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.88rem; }
  th { background: #f0f4ff; text-align: left; padding: 7px 10px; border: 1px solid #ddd; }
  td { padding: 7px 10px; border: 1px solid #ddd; vertical-align: top; }

---

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

### Choosing the right tool for you

| Tool | Good for | Best thing about it | Watch out for |
|---|---|---|---|
| **Excel** | Simple daily strategies, part-time traders | Everything visible on screen — very hard to make hidden mistakes | Cannot handle hundreds of stocks or complex models |
| **MATLAB** | Serious quant research, large stock universes | Fast, powerful statistics, real customer support | Costs money (home version is affordable though) |
| **Python** | Building production systems, using machine learning | Free, huge library of add-ons, most popular in industry | Packages often break each other; slower than MATLAB; no support |
| **R** | Classical statistics and econometrics | Best statistical packages available anywhere | Weaker machine learning support; basic interface |
| **QuantConnect** | Research all the way through to live trading | 400TB of data included; Python or C#; backtest and live trading use identical code | Requires programming knowledge |
| **Blueshift** | Python users who want data and backtesting in one place | Free minute-by-minute data; also has a no-code visual builder | Fewer markets than QuantConnect |

---

## Section 3 — Where Do You Get Historical Data?

<div class="note-abstract">
Getting historical data is the easy part — the internet is full of free sources. The hard part is understanding what problems are hiding inside that data. Three issues silently ruin most backtests: prices that have not been corrected for stock splits or dividends, databases that are missing stocks that went bankrupt, and noisy daily high and low prices that are less reliable than they look.
</div>

### Core ideas

<div class="key-idea"><strong>Always use prices that have been adjusted for stock splits and dividends.</strong> When a company splits its stock 2-for-1, the price drops by half overnight — but nothing actually changed for shareholders. If your data is not adjusted, your backtest sees a huge fake price drop and generates a false buy signal.</div>

<div class="key-idea"><strong>Databases that are missing bankrupt companies make strategies look much better than they really are.</strong> If your database only includes stocks that are still trading today, you are missing all the ones that went bust. A "buy cheap" strategy looks amazing in this kind of biased data — because you never see the cheap stocks that went to zero. This is called survivorship bias.</div>

<div class="key-idea"><strong>Daily high and low prices are unreliable — stick to open and close wherever possible.</strong> The day's high or low is often set by a single tiny trade, a data entry error, or a trade on a different exchange. Any strategy that assumes you can buy at exactly the daily low or sell at exactly the daily high will look better in backtest than it ever will in real trading.</div>

### Table 3.1 — Where to find historical data

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

## Section 4 — How Do You Measure If a Strategy Is Good?

<div class="note-abstract">
Most people judge a trading strategy by how much money it made. But raw returns are misleading because they do not tell you how much risk was taken to earn them. A strategy that made 20% by putting everything on one risky bet is far worse than one that made 15% through smooth, consistent gains. The Sharpe ratio, maximum drawdown, and MAR ratio together give you a much more honest and complete picture.
</div>

### The big ideas

<div class="key-idea"><strong>The Sharpe ratio tells you how much you are earning per unit of risk taken.</strong> Think of it as asking: "How smooth and consistent were your gains?" A high Sharpe ratio means you made money reliably without wild swings. A low Sharpe ratio means the returns were bumpy and unreliable. Anything below 1 generally means the strategy is not worth running on its own.</div>

<div class="key-idea"><strong>For a fully hedged long–short strategy, you don’t need to subtract the risk-free rate.</strong> The short side pays for the long side, so the portfolio is basically self-funded. In that case, you can compute Sharpe using the raw strategy returns.</div>

<div class="key-idea"><strong>Scaling a Sharpe ratio to an annual number uses the square root, not a simple multiplication.</strong> You cannot just multiply a daily Sharpe by 252 trading days. You multiply by the square root of 252 (about 15.87). This is because risk does not grow in a straight line with time — it grows more slowly. Getting this wrong is a common mistake even among experienced traders.</div>

### The Sharpe ratio formula

$$\text{Sharpe ratio} = \frac{\text{Average return} - \text{Risk-free rate}}{\text{Standard deviation of returns}}$$

**Annualization:**
- Daily returns: multiply by $\sqrt{252}$ (≈ 15.87)
- Monthly returns: multiply by $\sqrt{12}$ (≈ 3.46)
- Hourly returns: multiply by $\sqrt{1638}$ (252 trading days × 6.5 trading hours per day)

⚠️ **Common mistake:** using $252 \times 24 = 6,048$ for hourly data. Only count actual trading hours (6.5 hours per NYSE day), not all 24 hours.

### The MAR ratio — a quick gut-check

$$\text{MAR ratio} = \frac{\text{Annual growth rate}}{\text{Maximum drawdown}}$$

**Example:** Strategy grows 20% per year and the worst loss from peak was 40%
$$\text{MAR ratio} = \frac{20\%}{40\%} = 0.5$$

Higher is better. Useful because it roughly cancels out leverage effects, making it easier to compare strategies with different risk levels.

### Examples from the book

<div class="example-block">
<div class="ex-title">Example 3.4 — Sharpe ratio: simple buy-and-hold IGE vs. IGE hedged with SPY <span class="ex-pill pill-num">Numbers walkthrough</span></div>

**Strategy A — Simple buy-and-hold:** Buy IGE (an energy ETF) in November 2001 and sell it in November 2007. Assume the risk-free rate was 4% per year during this period.

Step-by-step in Excel:
1. Calculate the daily percentage return: `= (today's price − yesterday's price) / yesterday's price`
2. Subtract the daily version of the risk-free rate: `= daily return − (4% ÷ 252)`
3. Apply the Sharpe formula: `= SQRT(252) × AVERAGE(excess returns) / STDEV(excess returns)`

<div class="result-box"><strong>Sharpe ratio for buying and holding IGE: 0.789</strong></div>

**Strategy B — Hedged version:** Same IGE position, but simultaneously short an equal dollar amount of SPY (the S&P 500 ETF). This way if the whole market drops, the SPY short partially offsets IGE losses.

Net daily return = (IGE return − SPY return) ÷ 2  *(divide by 2 because double the capital is now deployed)*

No risk-free rate subtraction needed here — the long and short sides finance each other.

<div class="result-box"><strong>Sharpe ratio for hedged IGE−SPY strategy: 0.784</strong></div>

Both strategies end up with almost the same Sharpe ratio. The hedge cut the returns and the risk by similar proportions, so the ratio stayed about the same.

Code files: [example3_4.xls](http://epchan.com/book/example3_4.xls) · [example3_4.m](http://epchan.com/book/example3_4.m) · [example3_4.ipynb](http://epchan.com/book/example3_4.ipynb) · [example3_4.R](http://epchan.com/book/example3_4.R)

<div class="ex-lesson"><strong>Takeaway:</strong> For fully hedged strategies (where longs and shorts fund each other), do not subtract the risk-free rate in the Sharpe formula. The financing costs cancel out, so just use the raw daily net returns.</div>
</div>

<div class="example-block">
<div class="ex-title">Example 3.5 — Maximum drawdown: how deep did it drop and how long did recovery take? <span class="ex-pill pill-num">Numbers walkthrough</span></div>

Continuing with the IGE−SPY hedged strategy from Example 3.4, here is how to calculate the drawdown in Excel:

1. **Running total return:** Compound the daily returns day by day
2. **Best level ever:** Track the highest total return reached so far — updates whenever a new high is set: `= MAX(yesterday's best, today's total return)`
3. **Today's drawdown:** How far below the best are we right now? `= (1 + today's total return) / (1 + best ever) − 1`
4. **Worst single drop:** The most negative value in the drawdown column
5. **Recovery time:** Count consecutive days below the best level — resets to zero when a new high is reached

<div class="result-box">
<strong>Worst loss from peak: −10.53%</strong><br>
<strong>Longest stretch below the previous best: 497 trading days (roughly two years)</strong>
</div>

Notice that the worst loss and the longest dry spell do not overlap — the biggest single drop was quick, but the recovery to a new high took nearly two full years.

<div class="ex-lesson"><strong>Takeaway:</strong> A 10% drawdown sounds manageable on paper. But spending two years below your previous best is psychologically exhausting — and can push traders to quit right before the rebound. Always look at both how deep and how long when judging a drawdown.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Sharpe ratio</span> <span class="ref-tag">MAR ratio</span> <span class="ref-tag">Maximum drawdown</span> <span class="ref-tag">Drawdown duration</span> <span class="ref-tag">High watermark</span>
</div>

---

## Section 5 — What Are the Most Common Mistakes?

<div class="note-abstract">
The frustrating thing about backtesting mistakes is that they almost always make a strategy look better than it really is — never worse. The two biggest culprits are accidentally using future information to make past trading decisions (look-ahead bias), and tuning a model so precisely to historical patterns that it stops working on new data (data-snooping bias). Both are sneaky, both are common, and both have practical tests that can catch them.
</div>

### The big ideas

<div class="key-idea"><strong>Look-ahead bias means your backtest accidentally used information that was not yet available at the time of the trade.</strong> A simple example: your entry rule says "buy if today's price is within 1% of today's lowest price." But you cannot know what today's lowest price is until the market closes! Using that information to make a trade decision earlier in the day is cheating — and it makes the backtest look better than it ever could in real life.</div>

<div class="key-idea"><strong>There is a simple test to catch look-ahead bias: chop off the end of your data and see if anything changes.</strong> Run your full backtest and save the trading positions. Then delete the most recent 60 days of data and run it again. Compare the positions for the overlapping period. If they differ even slightly, your program is peeking at future data — you have look-ahead bias to fix.</div>

<div class="key-idea"><strong>Data-snooping bias is what happens when you tune a strategy too precisely to the past.</strong> Imagine testing 500 different combinations of settings until you find one that looks incredible on your historical data. Almost certainly, that "incredible" result is just a coincidence — you found the settings that happened to fit historical noise, not a real market pattern. The golden rule: use no more than 5 adjustable settings in total.</div>

### How much data do you need to trust your backtest?

| Your backtest Sharpe ratio | You want confidence that live trading will achieve Sharpe of at least... | Minimum data needed |
|---|---|---|
| 1.0 | Greater than 0 | 681 trading days — about 2.7 years of daily data |
| 2.0 | Greater than 0 | 174 trading days — about 0.7 years of daily data |
| 1.5 | Greater than 1.0 | 2,739 trading days — about 10.9 years of daily data |

> These requirements apply to paper trading (running a live strategy with no real money) just as much as to the backtest itself. You need the same amount of clean out-of-sample testing to be confident your strategy is real.

### How to protect yourself from data-snooping bias

Split your historical data into two halves:
- **Training half** (the earlier period): Build and fine-tune your strategy here
- **Test half** (the more recent period): Run the strategy unchanged on this data. Do not adjust anything based on what you see here.

If the strategy works well on both halves, the result is much more credible. If it only works on the training half, it was overfit to the past and is unlikely to hold up in real trading.

### Example from the book

<div class="example-block">
<div class="ex-title">Example 3.6 — GLD vs. GDX pair trading: does it hold up on unseen data? <span class="ex-pill pill-live">Real strategy test</span></div>

**The idea:** GLD tracks the price of gold. GDX holds a basket of gold-mining company stocks. Since gold miners' profits depend on gold prices, these two ETFs should generally move together. When their prices drift unusually far apart, we bet they will snap back — this is called pair trading.

**How it works:**
- Calculate the "spread" = GLD price − (1.637 × GDX price). The 1.637 is the hedge ratio — how many dollars of GDX to balance against each dollar of GLD, found by running a simple regression on the training data
- When the spread drops more than 2 standard deviations below normal → **buy the spread** (buy GLD, short GDX)
- When the spread rises more than 2 standard deviations above normal → **short the spread** (short GLD, buy GDX)
- Exit when the spread returns to within 1 standard deviation of normal

**Splitting the data:**
- Training set: first 252 trading days (about 1 year)
- Test set: all remaining days — the strategy runs here without any changes

**Results with default settings (entry at ±2 standard deviations, exit at ±1):**

<div class="result-box">
<strong>Sharpe on training data: 2.08</strong><br>
<strong>Sharpe on out-of-sample test data: 1.49</strong>
</div>

Both are solid — the strategy holds up on data it was never trained on.

**After tuning the settings (entry at ±1 standard deviation, exit at ±0.5):**

<div class="result-box">
<strong>Sharpe on training data: 2.9</strong><br>
<strong>Sharpe on out-of-sample test data: 3.0</strong>
</div>

This is a rare and encouraging result — the improvement on the training data also improved the test data, which suggests the better settings reflect a real pattern, not just luck with historical noise.

**Look-ahead bias check:** Remove the last 60 days of data and re-run. The positions for the remaining overlapping period were identical — the strategy is clean.

Code files: [example3_6.m](http://epchan.com/book/example3_6.m) · [example3_6.ipynb](http://epchan.com/book/example3_6.ipynb) · [example3_6.R](http://epchan.com/book/example3_6.R)

<div class="ex-lesson"><strong>Takeaway:</strong> When tuning your settings on training data also improves the test data, that is a genuine green flag. When it only improves the training data and hurts the test data, you have overfit — and the strategy probably will not survive real trading.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Look-ahead bias</span> <span class="ref-tag">Data-snooping bias</span> <span class="ref-tag">Training set</span> <span class="ref-tag">Test set</span> <span class="ref-tag">Out-of-sample testing</span> <span class="ref-tag">Pair trading</span> <span class="ref-tag">Hedge ratio</span>
</div>

---

## Section 6 — How Do Transaction Costs Destroy Strategies?

<div class="note-abstract">
Trading costs are not just a small footnote — they can completely destroy a strategy that looks great on paper. The more often a strategy trades, the more costs pile up, and the damage is multiplicative. This section contains one of the most dramatic examples in the book: a strategy claiming a Sharpe ratio of 4.47 collapses to −3.19 after adding realistic trading costs. Learning to include costs properly is not optional detail — it is what separates a working strategy from an expensive illusion.
</div>

### The big ideas

<div class="key-idea"><strong>The more often a strategy trades, the more costs eat into returns.</strong> A strategy that rebalances once per week and one that rebalances every day face vastly different cost burdens over the same period. Any strategy that trades very frequently and looks impressive before costs needs to be treated as unproven until the costs are applied properly.</div>

<div class="key-idea"><strong>Which stocks you trade matters as much as how the strategy is designed.</strong> Example 3.7 is a perfect demonstration: the same mean-reversion strategy achieves a Sharpe of 4.47 on small and micro-cap stocks, but collapses to 0.25 on large S&P 500 stocks. The logic of the strategy is identical — the difference is that small stocks are less efficiently priced and snap back more reliably than large ones.</div>

<div class="key-idea"><strong>Tiny execution changes — like trading at the open instead of the close — can flip a strategy from losing money to making money.</strong> Example 3.8 shows that one single code change (swap closing prices for opening prices) transforms a strategy losing money every day into one that profits. When and how you execute is just as important as the underlying trading idea.</div>

### Examples from the book

<div class="example-block">
<div class="ex-title">Example 3.7 — A Sharpe 4.47 strategy becomes Sharpe −3.19 after 5 basis points per trade <span class="ex-pill pill-warn">Warning example</span></div>

**The strategy** (from MIT researchers Khandani and Lo): Every day, buy the S&P 500 stocks that fell the most yesterday and short the ones that rose the most. Bet that yesterday's big losers will bounce back and yesterday's big winners will pull back. Rebalance the whole portfolio every single trading day.

**Without any transaction costs in 2006 (applied to the S&P 500):**

<div class="result-box"><strong>Sharpe ratio: 0.25</strong> — already far below the paper's reported 4.47. The reason: the original paper used small and micro-cap stocks where this bounce-back effect is much stronger. Large-cap S&P 500 stocks are too efficiently priced for the strategy to work as well.</div>

**After adding 5 basis points (0.05%) per trade:**

<div class="result-box"><strong>Sharpe ratio: −3.19</strong> — deeply and consistently unprofitable</div>

Why does even a tiny cost cause such a big collapse? Because the strategy rebalances the entire S&P 500 every single day — hundreds of trades daily. Even a 0.05% cost per trade, multiplied across hundreds of stocks every day, snowballs into a massive daily loss. The MATLAB line that adds costs is just:

```matlab
onewaytcost = 0.0005;  % 5 basis points
daily_pnl_after_costs = daily_pnl - sum(abs(weight_changes)) .* onewaytcost;
```

The key insight: calculate costs based on how much the portfolio actually changed each day, not as a flat fee. Bigger daily changes mean bigger costs.

Code files: [example3_7.m](http://epchan.com/book/example3_7.m) · [example3_7.ipynb](http://epchan.com/book/example3_7.ipynb) · [example3_7.R](http://epchan.com/book/example3_7.R)

<div class="ex-lesson"><strong>Takeaway:</strong> Never assume a strategy works just because a published paper says it does. Always apply it to the exact universe you plan to trade, and always include realistic transaction costs. Both of those checks can independently turn a winner into a loser.</div>
</div>

<div class="example-block">
<div class="ex-title">Example 3.8 — One word changed in the code rescues the entire strategy <span class="ex-pill pill-live">Real improvement</span></div>

**The fix:** Take the exact same strategy from Example 3.7. The only change: instead of using yesterday's closing prices to set positions at today's close, use them to set positions at today's market open.

In MATLAB, the entire change is replacing every instance of `cl` (closing prices) with `op` (opening prices). One word. Nothing else changes.

**Before the change — trade at the close:**
- Sharpe before costs: 0.25
- Sharpe after 5 bps per trade: −3.19

**After the change — trade at the open:**

<div class="result-box"><strong>Both before-cost and after-cost Sharpe ratios are positive — the strategy now works.</strong></div>

Why? Trading at the open captures a genuine market phenomenon: stocks that dropped heavily yesterday tend to bounce back at the next morning's open. By the time the market closes that same day, the bounce has already largely played out and there is less edge left to capture — but the costs are just as real.

Code files: [example3_8.ipynb](http://epchan.com/book/example3_8.ipynb) · [example3_8.R](http://epchan.com/book/example3_8.R)

<div class="ex-lesson"><strong>Takeaway:</strong> Always test both open-of-day and close-of-day execution when you are developing a strategy. It is not a cosmetic detail — it changes the fundamental economics of the trade. The open and close capture different market effects, and one is often far more profitable than the other after costs.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Transaction costs</span> <span class="ref-tag">Basis points</span> <span class="ref-tag">Portfolio turnover</span> <span class="ref-tag">Universe selection</span> <span class="ref-tag">Mean reversion</span> <span class="ref-tag">Execution timing</span>
</div>

---

## Section 7 — How Do You Improve a Strategy That Is Not Working?

<div class="note-abstract">
When a strategy does not perform well in the first backtest, that does not mean it is hopeless. Often a small, targeted tweak — trying a different universe of stocks, a different time to execute, or a slightly different signal threshold — can dramatically improve results. The key rule is that any change that helps on your training data must also help on your test data. If it only helps on the data you already used to develop the strategy, you have not found a real improvement — you have just found a cleverer way to fit to the past.
</div>

### The big ideas

<div class="key-idea"><strong>Any improvement must hold up on data the strategy has never seen before.</strong> This is the non-negotiable rule. If you tweak the strategy to look better on your training data and it gets worse on your test data, you have not improved it — you have overfit it. The test set is your reality check and it must be kept sacred.</div>

<div class="key-idea"><strong>The best improvements have a logical, real-world reason behind them.</strong> "Exclude pharmaceutical stocks because surprise drug trial results can trigger huge random price swings unrelated to the strategy's logic" is a sensible, well-grounded refinement. "Exclude stocks whose ticker starts with the letter T" is not — it is just curve-fitting in disguise, and it will almost certainly stop working in the future.</div>

<div class="key-idea"><strong>The three most powerful levers to pull are: which stocks you trade, when you execute, and how often you rebalance.</strong> As shown in Examples 3.7 and 3.8, changing the stock universe or the execution timing can transform a losing strategy into a winning one. Try these clear, economically motivated changes before reaching for more exotic adjustments.</div>

<div class="ref-tags">
<span class="ref-tag">Training set</span> <span class="ref-tag">Test set</span> <span class="ref-tag">Data-snooping bias</span> <span class="ref-tag">Sensitivity analysis</span> <span class="ref-tag">Universe selection</span> <span class="ref-tag">Execution timing</span>
</div>

---

## Term Glossary

Plain-English definitions for every key term introduced in Chapter 3.

### Backtesting & Platforms

<div class="glossary-entry">
<div class="gterm">Backtest <span class="gcat cat-data">Data</span></div>
Running a trading strategy on historical data to simulate how it would have performed in the past. Think of it as a practice run before using real money. The result is always somewhat optimistic — live trading almost always performs a bit worse than the backtest because the backtest does not capture every real-world friction.
</div>

<div class="glossary-entry">
<div class="gterm">WYSIWYG (What You See Is What You Get) <span class="gcat cat-platform">Platform</span></div>
A term for Excel's layout where all data and formulas sit visible on one screen at once. Because everything is right in front of you, it is very hard to accidentally use future data in a past decision — you can literally see if a formula is referencing the wrong row. This is why Excel is considered safer than code-based tools when it comes to avoiding look-ahead bias.
</div>

<div class="glossary-entry">
<div class="gterm">QuantConnect <span class="gcat cat-platform">Platform</span></div>
A web-based trading platform where you write and test strategies in Python or C#, with 400TB of historical data already included. One of its standout features: the exact same code you write for backtesting runs directly in live trading — no translation or rewriting needed, which removes a big source of errors between research and real trading.
</div>

<div class="glossary-entry">
<div class="gterm">Blueshift <span class="gcat cat-platform">Platform</span></div>
A platform by QuantInsti that bundles backtesting and live trading together in Python, with free minute-by-minute data for US, Indian, and forex markets. Also includes a visual drag-and-drop builder for people who prefer not to write code.
</div>

### Data Quality

<div class="glossary-entry">
<div class="gterm">Split adjustment <span class="gcat cat-data">Data</span></div>
Correcting historical stock prices to account for stock splits. In a 2-for-1 split, the stock price drops by half but shareholders get twice as many shares — nothing really changed. Unadjusted data makes this look like a genuine price crash. The fix: multiply all prices before the split date by the inverse of the split ratio (e.g., ½ for a 2-for-1 split).
</div>

<div class="glossary-entry">
<div class="gterm">Dividend adjustment <span class="gcat cat-data">Data</span></div>
Correcting historical prices to remove the price drop that happens when a company pays a dividend. On the day a dividend is paid (the ex-date), the stock price drops by roughly the dividend amount — even though shareholders received that cash. Without adjustment, this looks like a genuine price decline and generates false trading signals. Yahoo Finance handles this automatically.
</div>

<div class="glossary-entry">
<div class="gterm">Point-in-time data <span class="gcat cat-data">Data</span></div>
A database that records which stocks actually existed and were tradeable on each specific historical date — including those that later went bankrupt or were removed from exchanges. The gold standard for backtesting. Without it, your database only shows "winners" (companies still alive today), which makes strategies that buy cheap stocks appear far more profitable than they were in reality.
</div>

<div class="glossary-entry">
<div class="gterm">Survivorship bias <span class="gcat cat-bias">Bias</span></div>
The distortion that happens when a database is missing stocks that went bankrupt or were delisted. Only the "survivors" remain in the data. The problem hits hardest for strategies that buy cheap stocks — cheap stocks are often cheap because the company is struggling, but a biased database never shows the ones that eventually failed. Example 3.3 demonstrates a 430 percentage-point distortion (−42% real vs. +388% fictitious) from this one flaw alone.
</div>

<div class="glossary-entry">
<div class="gterm">High/low price noise <span class="gcat cat-data">Data</span></div>
The problem that daily high and low prices are much less trustworthy than opening and closing prices. The day's recorded high could be set by a single tiny off-exchange trade or a data entry mistake. Any strategy that assumes you can reliably buy at exactly the daily low or sell at exactly the daily high will look better in backtesting than it ever will in real trading.
</div>

### Performance Metrics

<div class="glossary-entry">
<div class="gterm">Sharpe ratio <span class="gcat cat-perf">Performance</span></div>
A score that measures how much return you earned per unit of risk. Formula: (Average return − Risk-free rate) ÷ Standard deviation of returns. To make it annual: multiply by √252 for daily returns or √12 for monthly returns. A Sharpe below 1 is generally not worth trading on its own. Above 2 is good. Above 3 is excellent. For fully hedged strategies, skip subtracting the risk-free rate — the two sides of the trade cancel it out.
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
The biggest loss from any peak to a subsequent trough in your account value, expressed as a percentage. From Example 3.5, the IGE/SPY strategy had an MDD of −10.53%. This answers the question: "How bad could it get before I recover?" It must be a number you could survive — both financially and psychologically.
</div>

<div class="glossary-entry">
<div class="gterm">Maximum drawdown duration <span class="gcat cat-perf">Performance</span></div>
The longest stretch of time a strategy spent below its previous peak. From Example 3.5: 497 trading days — roughly two years. Even if the loss was only −10%, spending two full years below your best result is exhausting. Many traders give up right before the recovery, locking in their losses permanently.
</div>

<div class="glossary-entry">
<div class="gterm">High watermark <span class="gcat cat-perf">Performance</span></div>
The best result your strategy has ever achieved up to any given point in time. All drawdowns are measured relative to this level. When you hit a new best and set a new high watermark, the drawdown counter resets to zero.
</div>

<div class="glossary-entry">
<div class="gterm">Deflated Sharpe ratio <span class="gcat cat-perf">Performance</span></div>
A more honest version of the Sharpe ratio that shrinks it based on how many times you tweaked your strategy during development. The more different settings and variations you tried before landing on the "best" result, the more that result gets deflated — because some of the apparent performance was probably just getting lucky with historical noise rather than finding something real. Developed by Bailey et al.
</div>

### Backtesting Pitfalls

<div class="glossary-entry">
<div class="gterm">Look-ahead bias <span class="gcat cat-bias">Bias</span></div>
Using information in your backtest that you could not have known at the time of the trade. For example: basing today's trade on today's lowest price — but you do not know that until the market closes. Or fitting a statistical model to your full historical dataset and then using that model to generate signals throughout the same data — the model has effectively "seen the future." Caught by the truncation test: remove the last 60 days of data, re-run, and compare positions — any difference indicates look-ahead bias.
</div>

<div class="glossary-entry">
<div class="gterm">Data-snooping bias <span class="gcat cat-bias">Bias</span></div>
The mistake of tuning a strategy so precisely to historical data that it stops working on new data. Happens naturally when you test hundreds of combinations and pick the best-looking one — that "best" result is usually just historical coincidence, not a real pattern. Rule of thumb: limit yourself to 5 or fewer adjustable settings. Reduce its impact by holding out a test set and validating your finalised strategy there before declaring success.
</div>

<div class="glossary-entry">
<div class="gterm">Out-of-sample testing <span class="gcat cat-method">Method</span></div>
Testing your finished strategy on data it was never trained on. The right approach: build and tune the strategy using the older portion of your historical data (training set), then run it once — without any further changes — on the more recent portion (test set). Running it on live real-time data with no money at risk (paper trading) is the ultimate version of this.
</div>

<div class="glossary-entry">
<div class="gterm">Training set / Test set <span class="gcat cat-method">Method</span></div>
Two separate halves of your historical data. The training set (older data) is where you build and refine the strategy. The test set (more recent data) is where you validate it without making any further adjustments. If you start tweaking the strategy based on what you see in the test set results, you have effectively turned the test set into a second training set and lost your honest out-of-sample check.
</div>

<div class="glossary-entry">
<div class="gterm">Sensitivity analysis <span class="gcat cat-method">Method</span></div>
Checking how your strategy's results change when you nudge the parameters slightly away from the optimal values. If the performance collapses dramatically with even a tiny change, data-snooping bias is likely — the strategy is too precisely tuned to the past to generalise. A trustworthy strategy should still produce reasonable results with parameters that are close to (but not exactly at) the sweet spot.
</div>

<div class="glossary-entry">
<div class="gterm">Parameterless trading model <span class="gcat cat-method">Method</span></div>
A model where instead of the researcher fixing parameters upfront (like always using a 20-day moving average), the model recalculates its own optimal parameters continuously from recent data. This removes one major source of data-snooping bias. It does not mean there are literally no parameters — it means the model determines them dynamically rather than the researcher picking them once and locking them in.
</div>

<div class="glossary-entry">
<div class="gterm">Paper trading <span class="gcat cat-method">Method</span></div>
Running your strategy on live real-time market data without committing any actual money. The best possible out-of-sample test because the data is completely new and unseen — you cannot accidentally fit to it. Also catches practical problems like bad data feeds, order timing issues, and software bugs that would never appear in a historical backtest.
</div>

### Strategy Concepts

<div class="glossary-entry">
<div class="gterm">Pair trading <span class="gcat cat-data">Data</span></div>
A strategy that simultaneously buys one security and shorts a closely related one, betting that their price relationship will return to normal after an unusual divergence. For example, GLD (tracks gold prices) and GDX (basket of gold-mining stocks) normally move together. When GLD gets unusually cheap relative to GDX, you buy GLD and short GDX, then wait for the prices to realign.
</div>

<div class="glossary-entry">
<div class="gterm">Hedge ratio <span class="gcat cat-data">Data</span></div>
In pair trading, this is the number that tells you how many dollars of the second security to trade for each dollar of the first, so that the two sides of the trade are properly balanced. It is calculated using a simple linear regression. From Example 3.6: the hedge ratio between GLD and GDX is 1.637, meaning for every $1 of GLD you trade, you trade $1.637 of GDX on the opposite side.
</div>

<div class="glossary-entry">
<div class="gterm">Z-score <span class="gcat cat-data">Data</span></div>
A way of measuring how unusual the current value of something is compared to its recent history. Formula: (Current value − Average) ÷ Standard deviation. A z-score of +2 means the value is 2 standard deviations above average — quite unusual. A z-score of −2 means unusually low. In pair trading, you enter the trade when the spread's z-score reaches ±2 (unusual enough to bet on reversion) and exit when it returns to ±1 (back to near-normal).
</div>

<div class="glossary-entry">
<div class="gterm">Portfolio turnover <span class="gcat cat-cost">Cost</span></div>
How much of your portfolio you buy or sell in each trading period, as a fraction of total portfolio size. High turnover means lots of trading activity and lots of transaction costs. When calculating costs for a strategy that trades many stocks, always base it on how much the portfolio actually changed each period — not on a flat per-period fee. Bigger changes mean bigger costs.
</div>

<div class="glossary-entry">
<div class="gterm">Universe selection <span class="gcat cat-method">Method</span></div>
Choosing which stocks (or other instruments) your strategy is allowed to trade. One of the most powerful decisions in strategy design. Example 3.7 showed the same mean-reversion strategy achieving a Sharpe of 4.47 on small-cap stocks but only 0.25 on large-cap S&P 500 stocks. Small stocks are less efficiently priced and tend to bounce back from unusual moves more reliably — but they also face higher trading costs and market impact.
</div>

<div class="glossary-entry">
<div class="gterm">Execution timing (open vs. close) <span class="gcat cat-method">Method</span></div>
Whether your strategy places trades at the start of the day (market open) or the end (market close). This is not a minor implementation detail — it can determine whether the strategy makes or loses money. Example 3.8 showed that switching from close-of-day to open-of-day execution turned a strategy losing money daily (Sharpe −3.19 after costs) into a profitable one. Always test both during strategy development.
</div>
