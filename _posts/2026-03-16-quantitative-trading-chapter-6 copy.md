
---

## Section 3 — Allocating Capital Across Multiple Strategies

<div class="note-abstract">
Most serious traders run more than one strategy at a time — different strategies for different markets, timeframes, or instruments. The Kelly formula extends naturally to this multi-strategy case. The key insight is that strategies that are uncorrelated (or negatively correlated) with each other provide a diversification benefit: you can often run a higher total leverage when strategies do not all lose at the same time.
</div>

### The big ideas

<div class="key-idea"><strong>The multi-strategy Kelly formula automatically recommends shorting strategies with negative expected returns.</strong> If you have three strategies and one of them has a negative expected return, the formula will literally tell you to short that strategy (bet against it). This makes intuitive sense — if you expect a strategy to lose money, the right position is the opposite of what the strategy says.</div>

<div class="key-idea"><strong>Combining strategies can grow wealth faster than any individual strategy alone.</strong> Even when two strategies have the same expected return, if they lose money at different times (low correlation), combining them reduces total volatility.</div>

<div class="key-idea"><strong>Update the leverage inputs regularly — at least monthly, ideally daily.</strong> The Kelly formula uses your strategy's recent mean return and standard deviation. These change over time as market conditions evolve. Using a lookback period of about six months is a practical balance between being responsive to recent performance and not overreacting to short-term noise.</div>

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

Definitions for key terms.

### The Kelly Framework

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

### Risk Concepts

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


### Psychology

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
