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

### Core ideas

<div class="key-idea"><strong>The goal is not to maximise returns — it is to maximise long-term compounded wealth.</strong> These sound like the same thing but they are not. Maximising returns often means taking on so much risk that eventual ruin becomes almost certain. Maximising long-term compounded wealth means finding the leverage level where your account grows the fastest without ever being wiped out.</div>

<div class="key-idea"><strong>Risk always costs you something, even when the expected return is zero.</strong> This is one of the most counterintuitive results in finance. If a strategy has a 50/50 chance of going up 1% or down 1%, most people assume you will break even over time. You will not — you will slowly lose money. The mathematics of compounding means that volatility itself erodes your wealth, even when the expected return is exactly zero.</div>

<div class="key-idea"><strong>The Sharpe ratio determines the maximum possible growth rate of your wealth.</strong> There is a clean mathematical formula for this: $$g_{\max} = r_f + \frac{\text{Sharpe}^2}{2}$$ A high-Sharpe strategy with modest nominal returns will always grow your wealth faster, once properly levered, than a low-Sharpe strategy with high nominal returns.</div>

### Example

<div class="example-block">
<div class="ex-title">Example 6.1 — The coin flip puzzle: why volatility costs you money even with zero expected return <span class="ex-pill pill-puzzle">Puzzle</span></div>

<strong>Here is the puzzle:</strong>

<p>A stock goes up exactly 1% or down exactly 1% each minute, with equal 50/50 probability. If you buy this stock, will you — in the long run — make money, lose money, or break even?</p>

<p>Most experienced traders answer: <strong>break even</strong>. The answer is wrong.</p>

<p><strong>You will slowly lose money</strong> — at a rate of about 0.005% per minute (0.5 basis points per minute).</p>

<p><strong>Why?</strong> Because the mathematics of compounding is not symmetric. Consider two minutes:</p>
<p>- Minute 1: up 1% → your \$100 becomes \$101</p>
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

## Section 2 — The Kelly Formula — Your Optimal Leverage Calculator

<div class="note-abstract">
The Kelly formula is the mathematical answer to the question "how much should I bet?" It was originally developed by a Bell Labs scientist named J.L. Kelly in 1956 for telephone signal problems, then famously applied to gambling by Ed Thorp (the mathematician who beat the casinos at blackjack). Applied to trading, it tells you exactly how much leverage to use to make your wealth grow as fast as possible — without risking ruin.
</div>

### Core ideas

<div class="key-idea"><strong>Divide the average excess return by the variance of returns.</strong> If your strategy averages 7% annual excess return and has a standard deviation of 15%, the formula says to use $$f = \frac{7\%}{(15\%)^2} = 3.1\times$$ leverage. That is how much you should borrow to maximise your long-term wealth growth.</div>

<div class="key-idea"><strong>In practice, most traders use half-Kelly — half the recommended leverage.</strong> The Kelly formula assumes your return estimates are perfectly accurate, which they never are. Real return distributions also have "fat tails" — extreme events happen more often than the formula assumes. Using half of the Kelly-recommended leverage builds in a safety buffer for these inaccuracies.</div>

<div class="key-idea"><strong>You must update your leverage continuously as your equity changes.</strong> Kelly is not a one-time calculation. If you suffer a loss, your equity shrinks and Kelly says reduce your position size immediately. If you profit, your equity grows and Kelly says you can increase your position size. Doing this update at least once per day keeps your leverage close to optimal at all times.</div>

### The Kelly formula

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

### Examples

<div class="example-block">
<div class="ex-title">Example 6.2 — Kelly leverage for buying and holding SPY (the S&P 500 ETF) <span class="ex-pill pill-num">Worked numbers</span></div>

<p><strong>The strategy:</strong> Simply buy and hold SPY — the ETF that tracks the S&P 500 index.<p>

<p><strong>Historical numbers (at the time of calculation):</strong><p>
<p>- Average annual return: 11.23%</p>
<p>- Standard deviation of annual returns: 16.91%</p>
<p>- Risk-free rate: 4% per year</p>
<p>- Average excess return: 11.23% − 4% = 7.23%</p>

<p><strong>Step 1 — Calculate the Sharpe ratio:</strong></p>

$$\text{Sharpe ratio} = \frac{7.23\%}{16.91\%} = 0.428$$

<p><strong>Step 2 — Calculate the Kelly leverage:</strong></p>

$$f = \frac{7.23\%}{(16.91\%)^2} = \frac{0.0723}{0.02860} = 2.53$$

So Kelly says: if you have \$100,000, borrow money to invest a total of \$253,000 in SPY.

<p><strong>Step 3 — Calculate the optimal compounded growth rate:</strong></p>

$$g = r_f + \frac{\text{Sharpe}^2}{2} = 4\% + \frac{(0.428)^2}{2} = 4\% + \frac{9.14\%}{2} = 4\% + 4.57\% = 13.1\%$$

(per year, compounded after financing costs)

<p>For comparison, if you just buy SPY with cash and no leverage:</p>

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
