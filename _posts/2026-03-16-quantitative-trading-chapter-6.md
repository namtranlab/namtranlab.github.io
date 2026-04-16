---
layout: distill
title: "Quantitative Trading — Chapter 6 Study Notes"
description: Notes on Chapter 6 of Quantitative Trading (2nd Ed.) — how much to bet, how to size positions across multiple strategies, what risks to manage beyond market moves, and why your own psychology may be the biggest threat to your trading.
tags: Finance Quant Trading Risk Management Kelly Notes
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
  - name: Section 1 — The Core Question — How Much Should You Bet?
  - name: Section 2 — The Kelly Formula — Your Optimal Leverage Calculator
  - name: Section 3 — Allocating Capital Across Multiple Strategies
  - name: Section 4 — Risk Management Beyond the Formula
  - name: Section 5 — Stop Losses — Are They Actually Helpful?
  - name: Section 6 — Other Risks You Might Not Have Thought About
  - name: Section 7 — The Psychological Side of Trading
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
  .cat-kelly   { background: #d1fae5; color: #064e3b; }
  .cat-risk    { background: #fce8e6; color: #7f1d1d; }
  .cat-psych   { background: #ede8fc; color: #3c2a8a; }
  .cat-market  { background: #dbeafe; color: #1e3a8a; }
  .cat-method  { background: #fef3c7; color: #78350f; }
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

## Section 1 — The Core Question — How Much Should You Bet?

<div class="note-abstract">
Every trading strategy — no matter how good — will sometimes lose money. The question is not whether you will have losing periods, but whether those losing periods will destroy you or just inconvenience you. The answer depends almost entirely on how much leverage you are using. Too little leverage and your strategy grows painfully slowly. Too much and a single bad month can cause losses from which you never recover. Finding the sweet spot between these two extremes is what this chapter is about.
</div>

### The big ideas

<div class="key-idea"><strong>The goal is not to maximise returns — it is to maximise long-term compounded wealth.</strong> These sound like the same thing but they are not. Maximising returns often means taking on so much risk that eventual ruin becomes almost certain. Maximising long-term compounded wealth means finding the leverage level where your account grows the fastest without ever being wiped out.</div>

<div class="key-idea"><strong>Risk always costs you something, even when the expected return is zero.</strong> This is one of the most counterintuitive results in finance. If a strategy has a 50/50 chance of going up 1% or down 1%, most people assume you will break even over time. You will not — you will slowly lose money. The mathematics of compounding means that volatility itself erodes your wealth, even when the expected return is exactly zero.</div>

<div class="key-idea"><strong>The Sharpe ratio determines the maximum possible growth rate of your wealth.</strong> There is a clean mathematical formula for this: maximum compounded growth rate = risk-free rate + (Sharpe ratio)² ÷ 2. This is the mathematical proof, finally spelled out, for the claim made back in Chapter 2 — that a higher Sharpe ratio is more important than a higher nominal return. A high-Sharpe strategy with modest nominal returns will always grow your wealth faster, once properly levered, than a low-Sharpe strategy with high nominal returns.</div>

### Example

<div class="example-block">
<div class="ex-title">Example 6.1 — The coin flip puzzle: why volatility costs you money even with zero expected return <span class="ex-pill pill-puzzle">Puzzle</span></div>

<strong>Here is the puzzle:</strong>

<p>> A stock goes up exactly 1% or down exactly 1% each minute, with equal 50/50 probability. If you buy this stock, will you — in the long run — make money, lose money, or break even?</p>

<p>Most experienced traders answer: <strong>break even</strong>. The answer is wrong.</p>

<p><strong>You will slowly lose money</strong> — at a rate of about 0.005% per minute (0.5 basis points per minute).</p>

<p><strong>Why?</strong> Because the mathematics of compounding is not symmetric. Consider two minutes:</p>
<p>- Minute 1: up 1% → your $100 becomes $101</p>
<p>- Minute 2: down 1% → your $101 becomes $99.99</p>

<p>You did not break even — you lost $0.01. The 1% gain and 1% loss are equal in percentage terms, but they are applied to different base amounts, so they do not cancel out.</p>

<p>More precisely, the long-run compounded growth rate is:</p>

$$g = m - \frac{s^2}{2}$$

<p><strong>Where:</strong></p>
- $m$ = average return per period (0% here)
- $s$ = standard deviation per period (1% here)  
- $\frac{s^2}{2} = \frac{0.01^2}{2} = 0.00005 = 0.005\%$

**So:**
$$g = 0\% - 0.005\% = -0.005\% \text{ per minute — slowly losing money}$$

<div class="ex-lesson"><strong>Takeaway:</strong> Volatility is not free. Even when your strategy has a zero average return, if it has any risk at all, compounding mathematics means you will gradually lose money over time. This is why risk management — controlling volatility — is as important as finding a strategy with positive expected returns. Risk always reduces long-term growth.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Kelly formula</span> <span class="ref-tag">Compounded growth rate</span> <span class="ref-tag">Sharpe ratio</span> <span class="ref-tag">Leverage</span>
</div>

---

## Section 2 — The Kelly Formula — Your Optimal Leverage Calculator

<div class="note-abstract">
The Kelly formula is the mathematical answer to the question "how much should I bet?" It was originally developed by a Bell Labs scientist named J.L. Kelly in 1956 for telephone signal problems, then famously applied to gambling by Ed Thorp (the mathematician who beat the casinos at blackjack). Applied to trading, it tells you exactly how much leverage to use to make your wealth grow as fast as possible — without risking ruin.
</div>

### The big ideas

<div class="key-idea"><strong>The Kelly formula for a single strategy is simple: divide the average excess return by the variance of returns.</strong> If your strategy averages 7% annual excess return and has a standard deviation of 15%, the formula says to use 7% ÷ (15%)² = 3.1× leverage. That is how much you should borrow to maximise your long-term wealth growth.</div>

<div class="key-idea"><strong>In practice, most traders use half-Kelly — half the recommended leverage.</strong> The Kelly formula assumes your return estimates are perfectly accurate, which they never are. Real return distributions also have "fat tails" — extreme events happen more often than the formula assumes. Using half of the Kelly-recommended leverage builds in a safety buffer for these inaccuracies and still achieves close to optimal long-term growth.</div>

<div class="key-idea"><strong>You must update your leverage continuously as your equity changes.</strong> Kelly is not a one-time calculation. If you suffer a loss, your equity shrinks and Kelly says reduce your position size immediately. If you profit, your equity grows and Kelly says you can increase your position size. Doing this update at least once per day keeps your leverage close to optimal at all times.</div>

### The Kelly formula

```
For a single strategy:

  Optimal leverage (f) = Average excess return (m) ÷ Variance of returns (s²)

  Where:
    m = average one-period return minus the risk-free rate
    s = standard deviation of one-period returns
    s² = variance = s × s

Example: m = 7%, s = 15%
  f = 0.07 ÷ (0.15)² = 0.07 ÷ 0.0225 = 3.11×

This means: for every $1 of your own capital,
borrow an additional $2.11 to invest a total of $3.11.
```

### Examples from the book

<div class="example-block">
<div class="ex-title">Example 6.2 — Kelly leverage for buying and holding SPY (the S&P 500 ETF) <span class="ex-pill pill-num">Worked numbers</span></div>

**The strategy:** Simply buy and hold SPY — the ETF that tracks the S&P 500 index.

**Historical numbers (at the time of calculation):**
- Average annual return: 11.23%
- Standard deviation of annual returns: 16.91%
- Risk-free rate: 4% per year
- Average excess return: 11.23% − 4% = **7.23%**

**Step 1 — Calculate the Sharpe ratio:**
```
Sharpe ratio = 7.23% ÷ 16.91% = 0.428
```

**Step 2 — Calculate the Kelly leverage:**
```
f = 7.23% ÷ (16.91%)² = 0.0723 ÷ 0.02860 = 2.53×
```

So Kelly says: if you have $100,000, borrow money to invest a total of $253,000 in SPY.

**Step 3 — Calculate the optimal compounded growth rate:**
```
g = risk-free rate + Sharpe² ÷ 2
  = 4% + (0.428)² ÷ 2
  = 4% + 9.14% ÷ 2
  = 4% + 4.57%
  = 13.1% per year (compounded, after financing costs)
```

For comparison, if you just buy SPY with cash and no leverage:
```
g = 11.23% − (16.91%)²/2 = 11.23% − 1.43% = 9.8% per year
```

<div class="result-box">
<strong>Unleveraged SPY: 9.8% compounded annual growth</strong><br>
<strong>Kelly-leveraged SPY (2.53×): 13.1% compounded annual growth</strong>
</div>

Spreadsheet available at [epchan.com/book/example6_2.xls](http://epchan.com/book/example6_2.xls)

<div class="ex-lesson"><strong>Takeaway:</strong> The Kelly-leveraged approach grows wealth significantly faster — 13.1% vs 9.8% per year. But notice that the Kelly-recommended leverage of 2.53× for just buying the S&P 500 is already quite aggressive. If you can only tolerate modest drawdowns, you should use a lower leverage — which brings us to the half-Kelly approach.</div>
</div>

<div class="example-block">
<div class="ex-title">Adjusting Kelly when your broker limits your leverage <span class="ex-pill pill-num">Practical adjustment</span></div>

Retail brokers impose legal limits on how much leverage you can use:
- **Overnight positions in stocks:** Maximum 2× (Regulation T)
- **Intraday positions in stocks:** Maximum 4×
- **Futures and forex:** Higher leverage available (10× or more)

If Kelly tells you to use 3.11× leverage but your broker only allows 2×, you cannot follow the formula exactly. The solution: scale down all your individual strategy positions proportionally until the total leverage fits within the broker's limit.

<div class="ex-lesson"><strong>Takeaway:</strong> When broker leverage limits are binding, the Kelly formula still tells you the optimal *direction* — which strategies to allocate more to and which to allocate less to. You just apply a scaling factor to keep the total leverage within the allowed range.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Kelly formula</span> <span class="ref-tag">Half-Kelly</span> <span class="ref-tag">Leverage</span> <span class="ref-tag">Compounded growth rate</span> <span class="ref-tag">Sharpe ratio</span>
</div>

---

## Section 3 — Allocating Capital Across Multiple Strategies

<div class="note-abstract">
Most serious traders run more than one strategy at a time — different strategies for different markets, timeframes, or instruments. The Kelly formula extends naturally to this multi-strategy case. The key insight is that strategies that are uncorrelated (or negatively correlated) with each other provide a diversification benefit: you can often run a higher total leverage when strategies do not all lose at the same time.
</div>

### The big ideas

<div class="key-idea"><strong>The multi-strategy Kelly formula automatically recommends shorting strategies with negative expected returns.</strong> If you have three strategies and one of them has a negative expected return, the formula will literally tell you to short that strategy (bet against it). This makes intuitive sense — if you expect a strategy to lose money, the right position is the opposite of what the strategy says.</div>

<div class="key-idea"><strong>Combining strategies can grow wealth faster than any individual strategy alone.</strong> Even when two strategies have the same expected return, if they lose money at different times (low correlation), combining them reduces total volatility. Lower volatility means compounding works better for you — and the formula proves that the combined portfolio can beat either strategy's solo performance.</div>

<div class="key-idea"><strong>Update the leverage inputs regularly — at least monthly, ideally daily.</strong> The Kelly formula uses your strategy's recent mean return and standard deviation. These change over time as market conditions evolve. Using a lookback period of about six months is a practical balance between being responsive to recent performance and not overreacting to short-term noise. As a strategy's performance fades, the formula naturally reduces its recommended leverage toward zero.</div>

### Example from the book

<div class="example-block">
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

Code files: [example6_3.m](http://epchan.com/book/example6_3.m) · [example6_3.ipynb](http://epchan.com/book/example6_3.ipynb) · [example6_3.R](http://epchan.com/book/example6_3.R)

<div class="ex-lesson"><strong>Takeaway:</strong> Combining multiple strategies — even ones with weak individual performance — almost always beats any single strategy if they are not perfectly correlated. The Kelly formula handles all of this automatically by computing the optimal allocation across the full portfolio simultaneously.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Kelly formula</span> <span class="ref-tag">Diversification</span> <span class="ref-tag">Covariance matrix</span> <span class="ref-tag">Portfolio allocation</span>
</div>

---

## Section 4 — Risk Management Beyond the Formula

<div class="note-abstract">
The Kelly formula gives you the mathematically optimal leverage — assuming your return estimates are correct and returns follow a normal bell-curve distribution. In the real world, neither of these assumptions holds perfectly. Returns can be more extreme than the formula predicts (fat tails), and your estimates of average returns are always uncertain. This section explains how to handle these realities, including one of the most dramatic examples in recent financial history: the August 2007 quant fund meltdown.
</div>

### The big ideas

<div class="key-idea"><strong>Real financial markets have "fat tails" — extreme events happen far more often than the formula assumes.</strong> The Kelly formula assumes that returns follow a neat bell curve. In reality, stock markets occasionally experience moves of 10%, 20%, or even more in a single day — events that a bell curve would say are essentially impossible but which happen regularly. These are called black swan events. The formula does not protect you from them, which is why you should use half-Kelly or even less as your starting point.</div>

<div class="key-idea"><strong>Use your historical worst-case loss as an additional safety check.</strong> Beyond the Kelly formula, calculate the worst single day (or week) your strategy ever experienced in the backtest. Then ask: how much of your equity could you tolerate losing in that single period? The answer to that question sets a maximum leverage limit independently of the Kelly formula. Always use the more conservative of the two limits.</div>

<div class="key-idea"><strong>When losses happen, you must reduce your position — even though it feels exactly wrong.</strong> Risk management requires selling into losses and buying into gains. This feels backwards and painful in the moment. But the Kelly formula makes it mathematically explicit: after a loss, your equity is smaller, so the formula says your position should be smaller too. Failing to reduce after losses is how small drawdowns turn into catastrophic ones.</div>

### The practical worst-case check

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

### The 2007 quant meltdown — financial contagion in action

<div class="example-block">
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

## Section 5 — Stop Losses — Are They Actually Helpful?

<div class="note-abstract">
Many traders use stop losses — automatic rules to exit a position once it has lost a certain percentage. The intuition is that stop losses cap your downside and prevent catastrophic losses. The reality is more nuanced: stop losses are genuinely helpful for some types of strategies and actively harmful for others. Using them in the wrong context can turn a winning strategy into a losing one.
</div>

### The big ideas

<div class="key-idea"><strong>Stop losses only help when the market is trending — and hurt when the market is mean-reverting.</strong> If prices tend to keep going in the same direction after a move (momentum or trending regime), then exiting a losing position quickly makes sense — the losses are likely to continue. But if prices tend to snap back (mean-reverting regime), then exiting a losing position locks in a loss right before the recovery. Most quantitative strategies are mean-reverting, which means most quant strategies should be cautious about stop losses.</div>

<div class="key-idea"><strong>Stop losses cannot prevent catastrophic losses during sudden market crashes.</strong> This is a common misconception. When a genuine market crash happens (a company announces fraud, a country defaults overnight, a pandemic is declared), prices do not fall gradually past your stop-loss price — they gap down instantly. Your stop loss order executes at whatever price is available, which may be far worse than your intended exit. Stop losses give you a false sense of protection against the very events they are supposed to guard against.</div>

<div class="key-idea"><strong>The right question to ask before using a stop loss: is this a trending or a mean-reverting situation?</strong> News-driven moves (real fundamental changes to a company's value) tend to be permanent — prices move to a new level and stay there. These are trending situations where stop losses make sense. Liquidity-driven moves (a large fund being forced to sell, a short squeeze, a temporary panic) tend to reverse — these are mean-reverting situations where stop losses are harmful and patience is rewarded.</div>

### When to use stop losses and when to avoid them

| Situation type | Price behaviour | Stop loss verdict | Example |
|---|---|---|---|
| **News-driven:** real bad news about the company | Trending — prices fall further | ✅ Use stop losses — the trend is likely to continue | Earnings fraud revealed, revenue collapse |
| **Liquidity-driven:** forced selling with no fundamental cause | Mean-reverting — prices eventually snap back | ❌ Avoid stop losses — patience is rewarded | Quant fund forced to liquidate, short squeeze |
| **Sudden market crash** | Gap down — stop loss executes far below trigger | ❌ Stop losses execute at crisis prices, not your target | Black Monday, pandemic announcement |

<div class="example-block">
<div class="ex-title">The mistake — entering a position by error and waiting for mean reversion <span class="ex-pill pill-warn">Personal cautionary tale</span></div>

The book describes a specific psychological trap related to stop losses:

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

## Section 6 — Other Risks You Might Not Have Thought About

<div class="note-abstract">
Market risk — the possibility that prices move against you — is what most traders think about. But there are three other types of risk that can destroy your trading business even when the markets are being perfectly kind: model risk (your strategy was never actually correct), software risk (your trading system has bugs), and operational risk (a power cut or internet outage at the worst possible moment).
</div>

### The three hidden risks

<div class="key-idea"><strong>Model risk — your strategy may have never had a real edge.</strong> The strategy worked beautifully in backtesting but fails in live trading. The causes are all the ones from Chapter 3: data-snooping bias, survivorship bias, look-ahead bias, or regime shifts. The best protection is having a collaborator independently reproduce your backtest results — the same "peer review" process that real scientific research requires. If someone else cannot replicate your results from scratch, that is a serious warning sign.</div>

<div class="key-idea"><strong>Software risk — your trading system may not faithfully implement your strategy.</strong> Bugs exist in all software. A bug in your automated trading system can cause it to trade differently from what your backtest model specifies — placing wrong orders, using stale prices, or trading at incorrect sizes. The check: run your live system and your backtest system on the same recent data and verify that the trades they generate are identical. Any discrepancy is a bug that needs fixing before real money is at stake.</div>

<div class="key-idea"><strong>Operational risk — physical and infrastructure failures are more common than you think.</strong> Your internet connection goes down at 9:31am. Your power fails mid-order. Your computer crashes during a volatile market session. None of these is exotic — all of them have happened to real traders. Having a backup internet connection, an uninterruptible power supply, and a plan for what to do in each failure scenario is not paranoia — it is basic operational hygiene.</div>

### Risk type summary

| Risk type | What it means in plain English | How to reduce it |
|---|---|---|
| **Model risk** | Your strategy never had a real edge, or market conditions changed | Have someone else independently replicate your backtest; keep strategies simple; update parameters regularly |
| **Software risk** | Your trading system has bugs that cause it to trade differently from your backtest | Compare live system trades vs. backtest trades on the same data daily; paper trade extensively |
| **Operational risk** | Physical infrastructure failures (internet, power, hardware) | Backup internet connection; uninterruptible power supply; clear emergency procedures |

<div class="ref-tags">
<span class="ref-tag">Model risk</span> <span class="ref-tag">Software risk</span> <span class="ref-tag">Operational risk</span>
</div>

---

## Section 7 — The Psychological Side of Trading

<div class="note-abstract">
Quantitative trading is supposed to remove emotion from the equation — the computer makes the decisions, not you. But the human running the computer still has to decide when to override it, when to shut it down, and when to increase its size. These decisions are where psychology becomes the decisive factor. Two emotions in particular — despair when things go wrong and greed when things go right — cause more trading disasters than any market event.
</div>

### The big ideas

<div class="key-idea"><strong>Despair during a drawdown causes two opposite mistakes — and both are wrong.</strong> One type of trader in a drawdown panics and shuts the strategy down completely, even when it still has a valid edge and just needs more time. The other type doubles down on the losing strategy, betting more to recover losses faster. Both are irrational. The correct response — systematically reducing leverage according to the Kelly formula — feels neither heroic nor dramatic, which is precisely why it is so hard to actually do.</div>

<div class="key-idea"><strong>Greed during a winning run is just as dangerous as despair during a losing run.</strong> When a strategy is performing brilliantly, the temptation is to lever it up quickly to "make money while it's hot." This is how overleveraging happens — not during obvious danger, but during apparent success. The historical examples of this are enormous: Long-Term Capital Management (2000), Amaranth Advisors (2006, $6 billion loss), and numerous hedge fund collapses. The pattern is always the same: a previously excellent strategy, overlevered on the basis of past success.</div>

<div class="key-idea"><strong>Loss aversion — your instinct to avoid losses more than you seek equivalent gains — is actually rational for traders, not a psychological flaw.</strong> Economists often treat loss aversion as an irrational bias. Box 6.1 in the chapter (and Example 6.1) show why this view is mathematically wrong. The coin-flip puzzle demonstrates that refusing a fair bet (expected gain $5, equal chance of winning $110 or losing $100) is the correct rational decision when you are playing with finite capital in sequence — because the compounding mathematics erode your wealth even in positive expected value games with high variance. Your instinct to avoid losses is correct. It is the economists who have the wrong model.</div>

### The representativeness trap — changing your strategy after a loss

<div class="example-block">
<div class="ex-title">The temptation to "fix" your strategy after a big loss <span class="ex-pill pill-warn">Psychological pitfall</span></div>

After a large unexpected loss, the almost universal human response is to look at the historical data and ask: "What rule would have avoided this specific loss?" You then add that rule to your strategy.

**The problem:** This is pure data-snooping bias applied in real time. You are tuning your strategy to avoid a loss that has already happened, not to prevent future losses. Almost certainly, your new rule will:
- Eliminate profit opportunities that would have existed
- Introduce a different vulnerability to future losses that you have not yet seen
- Reduce overall performance on out-of-sample data

**The correct response:** If you feel the strategy genuinely needs improvement after a loss, run a proper backtest of the modified version over a long historical period — not just the recent weeks that hurt you. If the modified strategy genuinely outperforms on a multi-year backtest, the change may be justified. If it only helps for the recent period, you are curve-fitting to recent noise.

<div class="ex-lesson"><strong>Takeaway:</strong> No strategy can avoid all losses. Trading operates in a probabilistic regime — losses happen even to strategies with genuine edges. The correct mental model is to evaluate your strategy over its full historical record, not to react to individual painful losses by restructuring the model.</div>
</div>

### Real personal examples from the book

<div class="example-block">
<div class="ex-title">Two personal disasters from overleveraging — and what was learned <span class="ex-pill pill-warn">Personal cautionary tales</span></div>

**Disaster 1 — Greed at an institutional fund:**
While working at a money management firm, a strategy had been running successfully for about six months. In a fit of enthusiasm (greed), over $100 million was added to that portfolio. The strategy had not been running long enough to validate whether the six months of performance was genuine or lucky. The result: over $1 million in losses for the fund's investors.

**Disaster 2 — Despair while trading independently:**
A mean-reverting spread strategy between XLE (energy ETF) and crude oil futures (CL) was not reverting as expected. Instead of reducing the position according to Kelly principles, the position was stubbornly increased to almost $500,000, hoping the reversion would come. Eventually despair set in, the position was exited with close to a six-figure loss. Shortly after — as is always the case in such stories — the spread reverted exactly as the strategy predicted. The strategy was right. The position management was catastrophically wrong.

**The lesson the book draws from both:**
Both disasters shared the same root cause: letting emotion override a systematic process. In the first case, greed — adding capital too quickly. In the second, the combination of overconfidence and then despair — increasing a losing position and then exiting at the worst possible moment.

The solution is not more discipline in the abstract — it is more concrete: start small, follow the Kelly formula mechanically, and build up position sizes gradually only as track record justifies it.

<div class="ex-lesson"><strong>Takeaway:</strong> The Kelly formula is not just a mathematical tool. It is a psychological anchor. Having a formula to follow prevents the two emotions — despair and greed — from dictating position sizes. Discipline means trusting the formula, especially when your gut says to do something different.</div>
</div>

### Box 6.1 — Why loss aversion is rational (not a bias)

<div class="example-block">
<div class="ex-title">Box 6.1 — The coin flip gamble: why refusing a positive expected value bet is smart <span class="ex-pill pill-puzzle">Puzzle</span></div>

Nobel laureate Daniel Kahneman famously used this gamble to illustrate what he called "loss aversion bias":

> "You are offered a fair coin flip. Tails: you lose $100. Heads: you win $110. Would you take it?"

Most people refuse. Kahneman called this irrational — the expected gain is $5.

**The book argues that the person refusing is actually correct.**

Here is why. Suppose you start with $1,000 and keep playing this game repeatedly, adjusting stakes proportionally to your current wealth:
- Average return per round: +0.5% (the $5 gain on $1,000)
- Standard deviation per round: 10.5% ($105 range on $1,000)
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

## Term Glossary

Plain-English definitions for every key term introduced in Chapter 6.

### The Kelly Framework

<div class="glossary-entry">
<div class="gterm">Kelly formula <span class="gcat cat-kelly">Kelly</span></div>
The mathematical formula that calculates the optimal leverage to use to maximise long-term compounded wealth growth. For a single strategy: Optimal leverage = Average excess return ÷ Variance of returns (m ÷ s²). Named after J.L. Kelly, a Bell Labs scientist, and famously applied to gambling and investing by mathematician Ed Thorp. Key property: the Kelly leverage is the same regardless of whether you use daily, monthly, or annual return figures — it is time-scale independent.
</div>

<div class="glossary-entry">
<div class="gterm">Half-Kelly <span class="gcat cat-kelly">Kelly</span></div>
Using half of the leverage recommended by the Kelly formula. The full Kelly formula is derived assuming perfectly accurate return estimates and normally-distributed returns. Since neither assumption holds in practice, using half-Kelly provides a safety buffer. Half-Kelly achieves roughly 75% of the maximum possible compounded growth rate while being far more tolerant of estimation errors and fat-tail events.
</div>

<div class="glossary-entry">
<div class="gterm">Compounded growth rate <span class="gcat cat-kelly">Kelly</span></div>
The actual annual rate at which your wealth grows when you reinvest all profits — accounting for the drag caused by volatility. It is always less than the simple average return. Formula: g = average return − variance/2 (for no leverage). This is the number that matters for long-term wealth building, not the average return. A strategy with a 10% average return and 20% volatility has a compounded growth rate of only 10% − (20%)²/2 = 8%.
</div>

<div class="glossary-entry">
<div class="gterm">Leverage <span class="gcat cat-kelly">Kelly</span></div>
The ratio of your total investment to your own capital. A leverage of 2× means for every $1 of your own money, you have borrowed $1 more and invested a total of $2. Leverage amplifies both gains and losses proportionally. The Kelly formula tells you the exact leverage level that maximises your long-term compounded wealth — above this level, additional leverage actually reduces long-term growth due to the cost of increased volatility.
</div>

<div class="glossary-entry">
<div class="gterm">Covariance matrix <span class="gcat cat-kelly">Kelly</span></div>
A table showing how much different strategies' returns move together. The diagonal shows each strategy's own variance (how volatile it is on its own). The off-diagonal elements show the covariance between pairs of strategies (how much they tend to gain and lose at the same time). In the multi-strategy Kelly formula, the covariance matrix captures diversification benefits: strategies that tend to lose at different times can be combined at higher total leverage than strategies that all lose together.
</div>

<div class="glossary-entry">
<div class="gterm">Portfolio allocation <span class="gcat cat-kelly">Kelly</span></div>
How much of your capital to allocate to each strategy in a multi-strategy portfolio. The Kelly formula's multi-strategy extension calculates the optimal allocation simultaneously across all strategies, taking into account their individual expected returns and how correlated they are with each other. Strategies with negative expected returns receive negative allocations — meaning you should short them or bet against them.
</div>

### Risk Concepts

<div class="glossary-entry">
<div class="gterm">Fat tails <span class="gcat cat-risk">Risk</span></div>
The property of real financial returns where extreme events (very large gains or losses) happen far more frequently than a normal bell-curve distribution would predict. A bell curve says a 5-standard-deviation move should happen roughly once in 3.5 million trading days. In financial markets, moves of that magnitude happen every few years. "Fat tails" refers to the fact that the probability curve for returns has thicker ends than a bell curve — meaning extreme events are not as rare as the formula assumes.
</div>

<div class="glossary-entry">
<div class="gterm">Black swan event <span class="gcat cat-risk">Risk</span></div>
An extreme market event that was considered essentially impossible based on historical data — until it happened. Coined by Nassim Taleb in his book of the same name (2007). Examples: the 1987 Black Monday crash (−20% in one day), the 2008 global financial crisis, Covid-19 market crash. The Kelly formula does not protect against black swans — which is one of the main reasons to use half-Kelly or less as a starting leverage.
</div>

<div class="glossary-entry">
<div class="gterm">Financial contagion <span class="gcat cat-risk">Risk</span></div>
The cascade effect where one fund's losses force it to sell, causing prices to drop, which causes other funds holding the same positions to also suffer losses, which forces them to sell, and so on. The summer 2007 quant meltdown (Goldman's Global Alpha fund −22.5%, Renaissance −8.7%) is the most cited example. Contagion can spread losses from one market sector to completely unrelated ones — in 2007, mortgage losses spread to quant equity strategies that held zero mortgage exposure.
</div>

<div class="glossary-entry">
<div class="gterm">Model risk <span class="gcat cat-risk">Risk</span></div>
The risk that your trading model is wrong — either because of statistical biases in the backtest (data-snooping, survivorship bias, look-ahead bias) or because market conditions have changed (regime shifts) and the model's edge no longer exists. Unlike market risk (which is random and expected), model risk is a systematic error that means you are consistently getting the wrong answer. Best protection: have someone else independently replicate your backtest results.
</div>

<div class="glossary-entry">
<div class="gterm">Software risk <span class="gcat cat-risk">Risk</span></div>
The risk that your automated trading system contains bugs that cause it to trade differently from what your backtest model specifies. Even small bugs can cause large losses if they result in wrong position sizes, wrong order directions, or trading at incorrect prices. The check: run both your live ATS and your backtest program on the same recent historical data and verify the trades they generate are identical.
</div>

<div class="glossary-entry">
<div class="gterm">Operational risk <span class="gcat cat-risk">Risk</span></div>
The risk of loss from physical or infrastructure failures — internet outages, power cuts, computer crashes, or other non-market events that disrupt your trading. Particularly dangerous if a failure occurs while you have a large open position that needs to be managed. Basic mitigations: backup internet connection (4G mobile hotspot as backup to broadband), uninterruptible power supply (UPS), clear procedures for what to do in each type of failure.
</div>

<div class="glossary-entry">
<div class="gterm">Stop loss <span class="gcat cat-method">Method</span></div>
An automatic exit rule that closes a position once it has lost a specified percentage. Helpful in trending markets (where losses tend to continue) and harmful in mean-reverting markets (where losses tend to reverse). Cannot prevent losses during sudden market crashes — prices gap past the stop level and execute at far worse prices. Most effective for news-driven moves where a fundamental change justifies a sustained price trend; most harmful for liquidity-driven moves where prices snap back quickly.
</div>

<div class="glossary-entry">
<div class="gterm">Drawdown <span class="gcat cat-risk">Risk</span></div>
The decline in your portfolio's value from a previous peak. In the context of risk management, drawdown triggers the Kelly formula requirement to reduce position size — you must shrink your portfolio in proportion to how much you have lost. The maximum drawdown you can tolerate without being forced to quit is a key constraint that should be used alongside the Kelly formula to determine your actual leverage.
</div>

### Psychology

<div class="glossary-entry">
<div class="gterm">Loss aversion <span class="gcat cat-psych">Psychology</span></div>
The human tendency to feel the pain of a loss more intensely than the pleasure of an equivalent gain. Often called an irrational bias, but Box 6.1 demonstrates it is mathematically rational for traders playing repeated games with finite capital: the compounding mathematics means that high-variance strategies lose compounded wealth even when the expected return is positive. Your instinct to avoid large losses protects you from the volatility drag that erodes long-term growth.
</div>

<div class="glossary-entry">
<div class="gterm">Despair (in trading) <span class="gcat cat-psych">Psychology</span></div>
The emotional state during a prolonged drawdown that leads traders to either: (1) shut down the strategy entirely and lock in losses at the worst possible moment, or (2) double down on the losing strategy to try to recover faster. Both responses are irrational. The systematic response — gradually reducing leverage according to the Kelly formula as the lookback-period performance deteriorates — is correct but feels neither heroic nor satisfying, which is why it is rarely done instinctively.
</div>

<div class="glossary-entry">
<div class="gterm">Greed (in trading) <span class="gcat cat-psych">Psychology</span></div>
The emotional state during a winning run that tempts traders to increase leverage rapidly — "make hay while the sun shines." This is the most common cause of overleveraging disasters. Long-Term Capital Management and Amaranth Advisors are canonical examples: both had previously excellent strategies that were overleveraged on the basis of recent success, leading to catastrophic losses. The Kelly formula caps leverage at the level justified by long-run statistics, not recent run of luck.
</div>

<div class="glossary-entry">
<div class="gterm">Overleveraging <span class="gcat cat-psych">Psychology</span></div>
Using more leverage than the Kelly formula recommends — resulting in a portfolio that is too large relative to the strategy's actual edge. Can arise from both greed (adding capital during a winning run) and despair (adding capital to a losing strategy to try to recover). Overleveraging does not just increase risk proportionally — above the Kelly-optimal leverage, additional leverage actually reduces long-term compounded growth while dramatically increasing the probability of catastrophic loss.
</div>

<div class="glossary-entry">
<div class="gterm">Representativeness bias <span class="gcat cat-psych">Psychology</span></div>
The human tendency to give too much weight to recent events and too little weight to long-run averages. In trading, this appears as the urge to modify your strategy immediately after any significant loss — adding a rule that would have avoided that specific loss. This is data-snooping applied in real time: the modification fits the past but may not help (and may actively hurt) future performance. The correct test: run a full backtest of the modified strategy over a long history, not just the recent painful period.
</div>

<div class="glossary-entry">
<div class="gterm">Ensemble average vs. time series average <span class="gcat cat-psych">Psychology</span></div>
A key distinction introduced in Box 6.1, following the work of physicists Ole Peters and Murray Gell-Mann. The ensemble average asks: "What is the average outcome across many traders playing simultaneously?" The time series average asks: "What is the average outcome for one trader playing repeatedly over time?" For evaluating financial risk, the time series average is the relevant one — because if you go broke, you stop playing. A bet that looks attractive in ensemble terms can be losing in time series terms if variance is high enough, which is why loss aversion is rational.
</div>
