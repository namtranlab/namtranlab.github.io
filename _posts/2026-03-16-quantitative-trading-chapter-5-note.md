---
layout: distill
title: "Quantitative Trading — Chapter 5 Study Notes"
description: Friendly notes on Chapter 5 of Quantitative Trading (2nd Ed.) — how to build a trading system that actually executes your strategy, cut costs, test safely, and understand why live results sometimes disappoint.
tags: Finance Quant Trading Execution Notes
giscus_comments: true
date: 2026-03-16
featured: true
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NYSE_floor.jpg/1280px-NYSE_floor.jpg

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Section 1 — What Does an Automated Trading System Actually Do?
  - name: Section 2 — Semi-Automated vs. Fully Automated — What Is the Difference?
  - name: Section 3 — What If You Cannot Code? Hiring a Programmer
  - name: Section 4 — How Do You Keep Trading Costs as Low as Possible?
  - name: Section 5 — Paper Trading — The Essential Safety Net
  - name: Section 6 — Why Does Live Trading Sometimes Disappoint?
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
  .pill-tip    { background: #fff3cd; color: #856404; }
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
  .cat-system  { background: #d1fae5; color: #064e3b; }
  .cat-cost    { background: #fce7f3; color: #831843; }
  .cat-risk    { background: #fce8e6; color: #7f1d1d; }
  .cat-method  { background: #ede8fc; color: #3c2a8a; }
  .cat-market  { background: #dbeafe; color: #1e3a8a; }
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

## Section 1 — What Does an Automated Trading System Actually Do?

<div class="note-abstract">
An automated trading system (ATS) is the software that turns your trading idea into real orders. It grabs the latest market prices, runs your strategy to figure out what to buy and sell, and sends those orders to your broker automatically. Without this, you are back to manually clicking "buy" and "sell" all day — which defeats the whole point of quantitative trading.
</div>

### The big ideas

<div class="key-idea"><strong>An ATS does three things in sequence: get data, generate orders, send orders.</strong> It pulls fresh price data from your broker or a data service, feeds that data into your trading algorithm, and transmits the resulting orders to your brokerage account. These three steps can happen every second for high-frequency strategies, or just once before the market opens for slower daily strategies.</div>

<div class="key-idea"><strong>Fully automated systems are no longer only for professional programmers.</strong> A few years ago, building a system that communicated directly with a broker's API required writing code in Java or C++. Today, platforms like QuantConnect and Blueshift handle all of that for you. You can build and run a fully automated system knowing only Python — or in Blueshift's case, no coding at all.</div>

<div class="key-idea"><strong>The data your system needs is not always just prices.</strong> Many strategies also need earnings estimates, dividend schedules, or announcement dates. Interactive Brokers provides earnings estimates (via Zacks) and expected announcement dates (via Wall Street Horizon) directly to customers, often at low or no cost. Factor this into your system design early — it is painful to discover a data gap after you go live.</div>

### What flows through your system each day

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

## Section 2 — Semi-Automated vs. Fully Automated — What Is the Difference?

<div class="note-abstract">
There are two flavours of automated trading system, and the right choice depends on how often your strategy trades and how comfortable you are with programming. A semi-automated system still requires you to press a few buttons each day — but it is much simpler to build and gives you a chance to sanity-check your orders before they go out. A fully automated system runs without any human involvement, which is essential for high-frequency strategies but carries the risk of a software bug trading by itself all day.
</div>

### The big ideas

<div class="key-idea"><strong>Semi-automated: your algorithm writes the orders, you press the button to send them.</strong> Your MATLAB, Python, or R program generates a list of orders and saves it to a text file. You then manually upload that file to your broker's basket trader or spread trader and click submit. Simple to build, easy to spot errors, but not suitable for strategies that need to react to prices throughout the day.</div>

<div class="key-idea"><strong>Fully automated: the system trades for you all day with no human involvement.</strong> The program connects directly to the broker's API, retrieves real-time prices in a loop, generates new orders continuously, and submits them automatically. You press "start" in the morning and "stop" at the end of the day. Essential for high-frequency strategies, but requires more robust programming and careful testing — because if it bugs out, it bugs out with real money.</div>

<div class="key-idea"><strong>A semi-automated system gives you one powerful safety check: you see the orders before they go.</strong> Fully automated systems can have bugs that cause catastrophic losses before you even notice. The infamous Knight Capital incident in August 2012 cost the firm $440 million in under an hour due to a software error in their fully automated system. Being able to glance at your order list before hitting submit is genuinely valuable insurance.</div>

### Semi-automated vs. fully automated at a glance

| Feature | Semi-automated | Fully automated |
|---|---|---|
| **How orders get sent** | You upload an order file and press submit manually | Program sends orders directly via API, automatically |
| **How often it can trade** | Once or a few times per day | Continuously throughout the day |
| **Programming difficulty** | Lower — Excel or a simple script is enough | Higher — requires API integration |
| **Human check before trading** | Yes — you see orders before they go | No — orders go out immediately |
| **Risk of silent bugs** | Lower — you catch most errors manually | Higher — bugs can trade with real money undetected |
| **Right for** | Daily or end-of-day strategies | Intraday or high-frequency strategies |

### How a semi-automated system works in practice

<div class="example-block">
<div class="ex-title">Real workflow — daily basket trading with Interactive Brokers <span class="ex-pill pill-live">Real example</span></div>

Here is the exact daily routine described in the book for running a large basket strategy with over 1,000 stocks:

1. **Before market open:** Run a MATLAB (or Python/R) program that downloads overnight data, runs the trading algorithm, and writes out an order file. A line in that file might look like: `("IBM", "BUY", "100")`

2. **Upload the file:** Open Interactive Brokers' BasketTrader, upload the order file to your account.

3. **Submit all at once:** Press one key — all orders (potentially 1,000+ of them) are sent to the exchange simultaneously at the open.

4. **Wait:** Some orders fill at the open, others fill later in the day, and some do not fill at all.

5. **End of day:** Press a button to cancel all unfilled orders. Press another button to close any existing positions if needed.

The entire active work each day is about 5 minutes of pressing buttons. The algorithm does everything else.

<div class="ex-lesson"><strong>Takeaway:</strong> Even a "simple" semi-automated system can manage over a thousand positions. The key is that the algorithm does the heavy lifting — you just supervise the handoff between the computer and the broker.</div>
</div>

### How a fully automated system works

<div class="example-block">
<div class="ex-title">Fully automated — press start, walk away <span class="ex-pill pill-live">Real example</span></div>

A fully automated system runs a continuous loop:

1. **Retrieve latest prices** from the broker's API
2. **Run the trading algorithm** on those prices
3. **Submit any new orders** directly via the API
4. **Go back to step 1** and repeat — potentially every few seconds or minutes

You press "start" when the market opens, and "stop" when it closes. In between, the computer trades on its own.

For this to work, your broker must provide an API (a programming interface) that lets your code fetch prices and place orders programmatically. Interactive Brokers, Alpaca, and Robinhood all offer this. Alpaca even offers a RESTful API, meaning any programming language can talk to it using simple web requests.

<div class="warning-box">
<strong>⚠️ The Knight Capital warning:</strong> In August 2012, a software bug in Knight Capital Group's fully automated system sent erroneous orders for 45 minutes before anyone stopped it. The loss: <strong>$440 million</strong> — more than the firm's entire equity. Before going fully automated, build in circuit breakers: maximum daily loss limits, position size caps, and alerts that wake you up if something unusual happens.
</div>

<div class="ex-lesson"><strong>Takeaway:</strong> Full automation is powerful but requires robust error handling. The semi-automated approach — where you review orders before they go — is a reasonable way to start, even if you eventually plan to fully automate later.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">ATS</span> <span class="ref-tag">API</span> <span class="ref-tag">Basket trader</span> <span class="ref-tag">Spread trader</span> <span class="ref-tag">DDE link</span> <span class="ref-tag">RESTful API</span>
</div>

---

## Section 3 — What If You Cannot Code? Hiring a Programmer

<div class="note-abstract">
Building an automated trading system requires more programming skill than backtesting does — especially for high-frequency strategies where every millisecond matters. If programming is not your strength, hiring a specialist is a practical and often affordable option. The tricky part is protecting your strategy idea while still getting the help you need.
</div>

### The big ideas

<div class="key-idea"><strong>Hiring a programming consultant is cheaper than most people expect.</strong> Experienced financial programmers charge $50 to $100 per hour. Most projects for independent traders cost between $1,000 and $5,000 in total. Your broker can often refer you to programmers who already know their API — Interactive Brokers has a dedicated page for this. Elite Trader forums are another good place to find experienced candidates.</div>

<div class="key-idea"><strong>Be cautious with general freelance platforms like Upwork.</strong> While there are thousands of programmers there, most lack specific knowledge of trading technology and financial markets — and that specialised knowledge is crucial for getting the system right. It is worth paying more for someone who understands order types, market data formats, and execution nuances.</div>

<div class="key-idea"><strong>You can protect your strategy without full secrecy by splitting the work.</strong> Hire one programmer to build the general trading infrastructure (data retrieval, order transmission) without knowing your specific strategy. Hire a second programmer to implement the trading logic without having access to the infrastructure. Neither one knows the full picture — and neither knows the specific parameter values you use.</div>

### Protecting your strategy from your own programmers

<div class="example-block">
<div class="ex-title">The compartmentalisation approach <span class="ex-pill pill-tip">Practical tip</span></div>

Here is the three-layer approach to keeping your strategy safe while still getting programming help:

| Layer | What the programmer builds | What they do NOT know |
|---|---|---|
| **Programmer A** | General infrastructure: connects to the broker's API, downloads data, sends orders | Your trading logic or strategy |
| **Programmer B** | The trading algorithm itself — reads input parameters and generates signals | The infrastructure code, and crucially, the actual parameter values |
| **You** | The parameter values (entry/exit thresholds, lookback periods, etc.) | Only you hold the complete picture |

Neither programmer alone can replicate your full system. Even if one of them decides to trade a similar strategy, they are missing critical pieces.

<div class="ex-lesson"><strong>Takeaway:</strong> NDA agreements are important but hard to enforce. The compartmentalisation approach protects you through architecture, not just legal documents. Most strategies are less unique than traders think — but your specific parameters and refinements are where the real edge lives.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">API</span> <span class="ref-tag">ATS</span> <span class="ref-tag">NDA</span>
</div>

---

## Section 4 — How Do You Keep Trading Costs as Low as Possible?

<div class="note-abstract">
We already know from Chapter 3 that transaction costs can destroy a strategy that looks great on paper. Chapter 5 adds the execution layer: there are specific things you can do at the time of placing orders — not just in the strategy design — to keep costs manageable. The core insight is simple: do not trade too large a slice of a stock's daily volume, and avoid very cheap low-priced stocks entirely.
</div>

### The big ideas

<div class="key-idea"><strong>Never trade more than 1% of a stock's average daily trading volume in a single order.</strong> When your order is large relative to how much of that stock normally trades in a day, you start moving the price against yourself just by trying to buy or sell. Sticking to under 1% of average daily volume keeps your market impact small. This threshold sounds conservative, but for small-cap stocks it can be surprisingly restrictive — a stock trading just 30,000 shares per day means your limit is only 300 shares, worth perhaps $3,000.</div>

<div class="key-idea"><strong>Avoid stocks priced below $5.</strong> Institutional traders have a well-known rule: skip stocks under $5. Two reasons: first, you need to buy far more shares to deploy the same capital, which means more commission. Second, cheap stocks have wider bid-ask spreads as a percentage of their price, making every trade more expensive. Stick to more liquid, higher-priced stocks where spreads are tighter.</div>

<div class="key-idea"><strong>Scale your position sizes to market capitalisation — but do not do it linearly.</strong> A linear scale (buying proportionally more of bigger companies) sounds sensible, but it means the largest company gets 10,000× more weight than the smallest, effectively eliminating any small stocks from your portfolio. Instead, scale to the fourth root of market cap — this keeps the weight ratio between the biggest and smallest stocks within a manageable factor of about 10, preserving diversification while still respecting size differences.</div>

### The four types of transaction cost — a quick reminder

| Cost type | What it is | How to reduce it |
|---|---|---|
| **Commission** | Fee your broker charges per trade | Use low-cost brokers; avoid high-turnover strategies |
| **Bid-ask spread** | Gap between buy price and sell price | Avoid low-priced stocks; use limit orders where possible |
| **Market impact** | Your own buying pushes prices up; your own selling pushes them down | Keep order size below 1% of average daily volume |
| **Slippage** | Price moves between when your signal fires and when the order fills | Use faster execution infrastructure; choose brokers with better speed |

### Practical cost-reduction rules

<div class="example-block">
<div class="ex-title">The 1% daily volume rule — a real small-cap example <span class="ex-pill pill-num">Numbers example</span></div>

At the time of writing, Bel Fuse Inc. is a stock in the S&P 600 SmallCap Index. Here are its numbers:

- Three-month average daily trading volume: **~30,000 shares**
- Recent closing price: **~$10 per share**
- 1% of average daily volume: **300 shares**
- Dollar value of that maximum order: **$3,000**

So even for a stock that is part of a recognised index, the safe maximum position size is just **$3,000**. For smaller stocks not in any index, the limit can be even lower. This is why small-cap strategies have such limited capacity — the market simply cannot absorb large orders in these stocks without significant price impact.

<div class="ex-lesson"><strong>Takeaway:</strong> This is not a theoretical constraint — it is a real practical ceiling on what you can trade. Before including any stock in your universe, check its average daily volume and calculate whether your intended position size stays under the 1% limit.</div>
</div>

<div class="example-block">
<div class="ex-title">Breaking up large orders — when it helps and when it backfires <span class="ex-pill pill-tip">Practical tip</span></div>

Institutional traders with very large orders sometimes split them into many smaller pieces spread over hours, to avoid moving the price all at once. This reduces market impact — but it introduces slippage, because the price may drift between the time you start executing and the time you finish.

For most independent retail traders, this trade-off is not worth it. Your order sizes are generally small enough that you can execute in one go without significant market impact. Splitting orders unnecessarily just increases your exposure to slippage. The book's advice: unless you are trading a stock with very low liquidity and your intended position is genuinely large relative to its daily volume, execute in one go.

<div class="ex-lesson"><strong>Takeaway:</strong> Order splitting is a tool for institutional traders managing billions. For independent quants, it usually creates more problems than it solves. The better fix is to simply stay within the 1% daily volume limit and choose liquid enough stocks in the first place.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Market impact</span> <span class="ref-tag">Average daily volume</span> <span class="ref-tag">Market capitalisation scaling</span> <span class="ref-tag">Slippage</span> <span class="ref-tag">Bid-ask spread</span>
</div>

---

## Section 5 — Paper Trading — The Essential Safety Net

<div class="note-abstract">
Paper trading means running your automated system on real live market data — but with fake money. Think of it as a full dress rehearsal before the opening night. It is the only practical way to catch software bugs, discover timing problems, and verify that your system actually behaves the way your backtest predicted. Skipping paper trading is one of the most common and costly mistakes new traders make.
</div>

### The big ideas

<div class="key-idea"><strong>Paper trading reveals bugs that backtesting simply cannot.</strong> Backtesting uses historical data that just sits there passively. Paper trading runs against live market data in real time, exposing timing issues, data feed problems, order routing failures, and look-ahead bias that only shows up when you cannot actually obtain certain data before placing a trade. Many traders discover a serious look-ahead bias in their strategy the moment they try to paper trade it — because they realise there is no way to get that crucial piece of data before the market opens.</div>

<div class="key-idea"><strong>Paper trading builds genuine intuition that backtesting never can.</strong> Running a backtest shows you the performance statistics. Running a paper trading system for a month shows you what the strategy actually feels like — how much the P&L swings day to day, how much capital gets tied up at peak, how many trades fire on a typical day, and what unexpected operational headaches arise. These are the things you need to understand before putting real money at risk.</div>

<div class="key-idea"><strong>The timing surprises are always bigger than expected.</strong> In the book's own experience: downloading and processing data each morning took about 20 minutes. Transmitting all orders to the broker account took another 15 minutes. Total: 35 minutes of preparation before the market opens. If your strategy relies on data or news that cannot be more than 30 minutes old at market open, you have a problem — and you will only discover that problem through paper trading, not through backtesting.</div>

### What paper trading reveals that backtesting misses

| What you discover | Why backtesting misses it |
|---|---|
| **Software bugs in your ATS** | Backtesting runs on stored historical data; bugs only show up with live systems |
| **Look-ahead bias** | In a backtest you have all the data; in live trading you discover what you actually cannot obtain in time |
| **Data feed problems** | Historical data is clean; live feeds drop out, arrive late, or contain bad ticks |
| **Operational timing issues** | How long does downloading + order generation + transmission actually take? |
| **Transaction cost estimates** | Your real fills often differ from theoretical ones; paper trading gives you real fill prices |
| **Data-snooping bias** | A month of live paper trading is a genuine out-of-sample test |

### A practical paper trading checklist

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

## Section 6 — Why Does Live Trading Sometimes Disappoint?

<div class="note-abstract">
You have done everything right. You backtested carefully, paper traded for a month, and went live. Three months later, the strategy is barely breaking even — or losing money. This is one of the most disheartening experiences in quantitative trading, and it is also one of the most common. This section gives you a systematic way to diagnose what went wrong, starting with the simplest possible fixes and working up to the hardest truths.
</note-abstract>

### The big ideas

<div class="key-idea"><strong>Start with the simplest diagnoses first — most problems are not mysterious.</strong> Before assuming something deep and structural has gone wrong, check the obvious things: Does your live system actually match your backtest program trade for trade? Are the execution costs higher than you modelled? Are you accidentally trading illiquid stocks that cause large market impact? These mundane issues cause the majority of live/backtest gaps and are fixable.</div>

<div class="key-idea"><strong>If simple fixes do not work, face the two hardest possibilities: data-snooping bias and regime shifts.</strong> Data-snooping bias means the strategy was overfit to historical noise — it never had a real edge. Regime shifts mean the market structure has genuinely changed, so a strategy that worked before no longer works now. Both are difficult to diagnose and both require serious action: either simplify the strategy aggressively or accept that you need to find a new one.</div>

<div class="key-idea"><strong>When the strategy is underperforming, simplify it — do not add complexity.</strong> If you suspect data-snooping bias, the test is to strip away as many rules and parameters as possible. If the backtest performance completely falls apart when you simplify, data-snooping bias is almost certainly the cause — the strategy was relying on those extra rules to fit historical noise. If performance holds up after simplification, poor live results may just be bad luck, and patience may be warranted.</div>

### Your live trading diagnostic checklist

<ul class="checklist">
  <li><strong>Do the trades match?</strong> Compare every trade your live system generates against what your backtest would have generated for the same data on the same day. If they differ, there is a bug to fix.</li>
  <li><strong>Are execution costs higher than expected?</strong> Add up what you are actually paying in commissions, spreads, and slippage. Compare to your backtest assumptions. If real costs are significantly higher, this alone can explain underperformance.</li>
  <li><strong>Are you trading illiquid stocks?</strong> Check whether your orders are routinely exceeding 1% of average daily volume. If so, you are paying large market impact costs that your backtest did not account for.</li>
  <li><strong>Does the strategy survive simplification?</strong> Remove parameters and rules one by one. If backtest performance collapses immediately, data-snooping bias is likely. If performance holds, the live underperformance may be temporary bad luck.</li>
  <li><strong>Has the market structure changed?</strong> Consider whether a regime shift could have altered the conditions your strategy relies on.</li>
</ul>

### Two specific regime shifts to know about

<div class="example-block">
<div class="ex-title">Regime shift 1 — Stock price decimalization in 2001 <span class="ex-pill pill-warn">Historical warning</span></div>

Before April 9, 2001, US stock prices were quoted in fractions — sixteenths or eighths of a dollar (e.g., $10 and 3/16). This may sound quaint, but it had a big practical effect: those wide fractional price increments created friction in the market that statistical arbitrage traders could exploit.

When the US switched to fully decimal pricing on April 9, 2001, those fractions disappeared. Bid-ask spreads narrowed dramatically. The friction that stat arb traders relied on was reduced significantly, and many strategies that looked great in pre-2001 backtests stopped working in the decimal era.

**Practical implication:** If your backtest data extends before 2001, the pre-decimalization period will show much better performance than you should expect going forward. Be especially sceptical of any strategy that shows most of its historical edge in the pre-2001 period.

<div class="ex-lesson"><strong>Takeaway:</strong> Always check when most of your backtest returns were generated. If the strategy was unusually profitable before 2001 and the edge has clearly shrunk since, the decimalization regime shift may be the explanation — and the pre-2001 performance is not a reliable guide to future returns.</div>
</div>

<div class="example-block">
<div class="ex-title">Regime shift 2 — The short-selling uptick rule (pre-2007 and post-2010) <span class="ex-pill pill-warn">Historical warning</span></div>

If your strategy involves shorting stocks, there is a specific regulatory trap in the historical data.

Before June 2007, the SEC's "uptick rule" stated that you could only short a stock on an "uptick" — meaning the last trade had to have been at a higher price than the one before it. This rule prevented short sellers from piling on during a price decline. In practice, it meant that many profitable short positions simply could not be entered during fast-moving markets.

**Timeline:**
- **Before June 2007:** Uptick rule in force. Shorting is constrained. Backtest performance for short strategies is artificially inflated because the backtest ignores the uptick constraint.
- **June 2007 – February 2010:** No uptick rule at all. Shorting is unrestricted. This is the most realistic period for backtesting short strategies.
- **After February 2010:** Alternative uptick rule (Rule 201) introduced. Shorting is restricted again when a stock drops more than 10% in a day.

**Additional complication — hard-to-borrow stocks:** Even when the uptick rule does not apply, many stocks — especially small-caps with low liquidity — are "hard to borrow." To short a stock, your broker has to borrow it from someone else (usually a mutual fund or another client). If no one will lend it, you simply cannot short it, regardless of what your backtest says. This can eliminate many of the best short opportunities in a strategy.

<div class="ex-lesson"><strong>Takeaway:</strong> If your strategy involves shorting, the most realistic backtest period is June 2007 through February 2010 — the only window when neither the old uptick rule nor the new alternative rule was in force. For any other period, assume your backtest performance on the short side is somewhat optimistic.</div>
</div>

<div class="ref-tags">
<span class="ref-tag">Data-snooping bias</span> <span class="ref-tag">Regime shift</span> <span class="ref-tag">Decimalization</span> <span class="ref-tag">Uptick rule</span> <span class="ref-tag">Hard to borrow</span> <span class="ref-tag">Market impact</span>
</div>

---

## Term Glossary

### Trading Systems

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

### Cost Reduction

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

### Testing & Diagnosis

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
