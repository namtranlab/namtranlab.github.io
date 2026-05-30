---
layout: distill
title: "Stochastic Calculus — Study Notes"
description: Study notes for Lawler Stochastic Calculus (Chapter 1).
tags: Stochastic Calculus
giscus_comments: true
date: 2026-05-30
featured: true
thumbnail: https://magica.com/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FIBw5a8ByyzY%2Fmaxresdefault.jpg&w=3840&q=75

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Section 1.2 — Martingales

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
  .pill-defn { background: #dbeafe; color: #1e3a8a; }
  .pill-prop { background: #ede8fc; color: #3c2a8a; }
  .pill-ex   { background: #fef3c7; color: #78350f; }
  .example-block .ex-lesson { margin-top: 0.5rem; font-size: 0.85rem; color: #555; border-top: 1px solid #ddd; padding-top: 0.4rem; }
  .key-idea { padding: 0.3rem 0; border-bottom: 1px dotted #ddd; margin-bottom: 0.4rem; }
  .key-idea:last-child { border-bottom: none; }
  .glossary-entry { border-bottom: 1px solid #eee; padding: 0.7rem 0; }
  .glossary-entry:last-child { border-bottom: none; }
  .glossary-entry .gterm { font-weight: 600; font-size: 0.95rem; margin-bottom: 0.25rem; }
  .glossary-entry .gcat { display: inline-block; font-size: 0.7rem; font-weight: 600; padding: 1px 7px; border-radius: 20px; margin-left: 6px; vertical-align: middle; }
  .cat-defn   { background: #dbeafe; color: #1e3a8a; }
  .cat-prop   { background: #ede8fc; color: #3c2a8a; }
  .cat-thm    { background: #d1fae5; color: #064e3b; }
  .cat-notn   { background: #fef3c7; color: #78350f; }
  .cat-meas   { background: #fce7f3; color: #831843; }
  .result-box { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 6px; padding: 0.6rem 1rem; margin: 0.5rem 0; font-size: 0.88rem; }
  .result-box strong { color: #276749; }
  .warning-box { background: #fff8e1; border: 1px solid #ffe082; border-radius: 6px; padding: 0.75rem 1rem; margin: 0.75rem 0; font-size: 0.88rem; color: #5d4037; }
  .warning-box strong { color: #e65100; }
  .ref-tags { margin-top: 1rem; }
  .ref-tag { display: inline-block; font-size: 0.72rem; padding: 2px 8px; border-radius: 20px; border: 1px solid #ccc; color: #666; margin: 2px 3px 2px 0; }
  /* ── Notation panel ── */
  .notation-panel { background: #f0f9ff; border: 1.5px solid #7dd3fc; border-radius: 8px; padding: 0.9rem 1.1rem; margin: 1rem 0 1.5rem 0; }
  .notation-panel .np-title { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #0369a1; margin-bottom: 0.6rem; }
  .notation-panel table { margin: 0; font-size: 0.84rem; }
  .notation-panel th { background: #e0f2fe; color: #0c4a6e; padding: 5px 9px; font-size: 0.78rem; }
  .notation-panel td { padding: 4px 9px; border-color: #bae6fd; vertical-align: middle; }
  .notation-panel td:first-child { font-weight: 700; color: #0369a1; white-space: nowrap; }
  /* ── Misconception block ── */
  .misconception-block { background: #fff1f2; border: 1.5px solid #fda4af; border-radius: 8px; padding: 0.85rem 1.1rem; margin: 0.75rem 0; }
  .misconception-block .mc-header { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem; }
  .misconception-block .mc-icon { font-size: 1rem; }
  .misconception-block .mc-label { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #be123c; }
  .misconception-block .mc-wrong { font-size: 0.88rem; color: #9f1239; margin-bottom: 0.4rem; }
  .misconception-block .mc-wrong strong { color: #be123c; }
  .misconception-block .mc-correct { font-size: 0.88rem; color: #166534; background: #f0fdf4; border-radius: 4px; padding: 0.4rem 0.7rem; border-left: 3px solid #4ade80; }
  .misconception-block .mc-correct strong { color: #15803d; }
  table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.88rem; }
  th { background: #f0f4ff; text-align: left; padding: 7px 10px; border: 1px solid #ddd; }
  td { padding: 7px 10px; border: 1px solid #ddd; vertical-align: top; }

---

<script>
function toggleChapter(id) {
  var body = document.getElementById(id + '-body');
  var arrow = document.getElementById(id + '-arrow');
  var isOpen = body.classList.contains('open');
  body.classList.toggle('open', !isOpen);
  arrow.classList.toggle('open', !isOpen);
}
</script>


## Section 1.2 — Martingales

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('s12')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">§ 1.2</span>
      <div>
        <div class="chapter-title">Section 1.2 — Martingales</div>
        <div class="chapter-subtitle">Definition of a martingale, the one-step criterion, sub/supermartingales, and the discrete stochastic integral</div>
      </div>
    </div>
    <span class="chapter-arrow" id="s12-arrow">▼</span>
  </button>
  <div class="chapter-body" id="s12-body" markdown="1">

### Notation at a Glance


| Symbol | Meaning |
|---|---|
| $M_n$ | The martingale process at time $n$ |
| $\mathcal{F}_n$ | Filtration at time $n$ — information in $M_0, M_1, \ldots, M_n$ |
| $E[M_n \mid \mathcal{F}_m] = M_m$ | The defining martingale condition for $m < n$ |
| $\Delta M_n = M_n - M_{n-1}$ | Increment of the martingale at step $n$ |
| $B_n$ | The "bet" at time $n$ — an $\mathcal{F}_{n-1}$-measurable process |
| $W_n = \sum_{j=1}^n B_j \Delta M_j$ | Winnings under a betting strategy — the discrete stochastic integral |
| $S_n = X_1 + \cdots + X_n$ | Partial sum of i.i.d. mean-zero random variables |
| $A_n = \sigma_1^2 + \cdots + \sigma_n^2$ | Cumulative variance (predictable compensator) |
| $E[M_n \mid \mathcal{F}_m] \geq M_m$ | Submartingale condition |
| $E[M_n \mid \mathcal{F}_m] \leq M_m$ | Supermartingale condition |
| $\mathcal{F}_{n-1}$-measurable | $B_n$ is known before time $n$ — the "non-anticipating" condition |


---

### Part 1 — The Core Intuition

<div class="note-abstract">
A martingale is the mathematical model of a <em>fair game</em>. At every moment, no matter what has happened so far, the expected future value of the process equals its current value.
</div>

#### Core ideas

<div class="key-idea"><strong>A martingale models a fair game.</strong> If $M_n$ represents cumulative winnings, "fair" means: regardless of the history of play, the expected winnings at any future time equal the current winnings. No strategy can give you a systematic advantage over a martingale in finite time.</div>

<div class="key-idea"><strong>The martingale condition is a statement about conditional expectations.</strong> The defining equation $E[M_n \mid \mathcal{F}_m] = M_m$ for $m < n$ is a direct application of §1.1: given everything observed up to time $m$, the best prediction of $M_n$ is simply $M_m$ itself.</div>

<div class="key-idea"><strong>To verify the martingale property it suffices to check one step at a time (The One-Step Criterion).</strong> Rather than checking $E[M_n \mid \mathcal{F}_m] = M_m$ for all pairs $m < n$, it is enough to verify $E[M_{n+1} \mid \mathcal{F}_n] = M_n$ for every $n$. The tower property of §1.1 propagates this to all future times.</div>

<div class="key-idea"><strong>A martingale has constant expected value.</strong> Taking the full expectation: $\mathbb{E}[M_n] = \mathbb{E}[E[M_n \mid \mathcal{F}_0]] = \mathbb{E}[M_0]$ for all $n$. The mean is time-invariant — a necessary (but not sufficient) condition for fairness.</div>

---

### Part 2 — The Formal Definition

<div class="note-abstract" markdown="1">
Suppose $X_1, X_2, \ldots$ is a sequence of random variables to which we associate the filtration $\{\mathcal{F}_n\}$ where $\mathcal{F}_n$ is the information contained in $X_1, \ldots, X_n$. 

A sequence of random variables $M_0, M_1, \ldots$ is called a <b>martingale</b> with respect to the filtration $\{\mathcal{F}_n\}$ if:

(i) For each $n$, $M_n$ is an $\mathcal{F}_n$-measurable random variable with $E[\lvert M_n \rvert] < \infty$.

(ii) If $m < n$, then

$$E[M_n \mid \mathcal{F}_m] = M_m. \tag{1.4}$$
</div>


**Unpacking condition (i):**
- *$\mathcal{F}_n$-measurable:* the value of $M_n$ is fully determined by the information available at time $n$. It does not look into the future.
- *$E[\lvert M_n \rvert] < \infty$:* integrability — the process cannot take infinitely large values on average. This is needed for the conditional expectation $E[M_n \mid \mathcal{F}_m]$ to be well-defined.

**Unpacking condition (ii):** Given everything observed up to time $m$, the best prediction of $M_n$ at any later time $n > m$ is simply the current value $M_m$. The process has no predictable drift in either direction.

<div class="ex-lesson"><strong>Equivalent one-step form:</strong> It suffices to check $E[M_{n+1} \mid \mathcal{F}_n] = M_n$ for every $n \geq 0$. The tower property then gives $E[M_{n+2} \mid \mathcal{F}_n] = E[E[M_{n+2} \mid \mathcal{F}_{n+1}] \mid \mathcal{F}_n] = E[M_{n+1} \mid \mathcal{F}_n] = M_n$, and so on for all future times.</div>

---

### Part 3 — Sub- and Supermartingales

<div class="note-abstract" markdown="1">
If the condition of martingale ($E[M_n \mid \mathcal{F}_m] = M_m$) is replaced with $E[M_n \mid \mathcal{F}_m] \geq M_m$, then the process is called a <b>submartingale</b>. If it is replaced with $E[M_n \mid \mathcal{F}_m] \leq M_m$, then it is called a <b>supermartingale</b>. 
</div>

| Process | Condition | Interpretation |
|---|---|---|
| **Martingale** | $E[M_n \mid \mathcal{F}_m] = M_m$ | Fair game — no systematic gain or loss |
| **Submartingale** | $E[M_n \mid \mathcal{F}_m] \geq M_m$ | Favourable game — expected value grows over time |
| **Supermartingale** | $E[M_n \mid \mathcal{F}_m] \leq M_m$ | Unfavourable game — expected value shrinks over time |

In other words, games that are always in one's favour are submartingales and games that are always against one are supermartingales. (At most games in Las Vegas, one's winnings give a supermartingale.)

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception — Sub vs Super</b></span>
  </div>
  <div class="mc-wrong"><strong>Wrong:</strong> "A supermartingale is 'super' — it grows faster than a martingale."</div>
  <div class="mc-correct"><strong>Correct:</strong> The naming is counterintuitive. A supermartingale has $E[M_n \mid \mathcal{F}_m] \leq M_m$ — its expected value <em>decreases</em> over time (unfavourable game). A submartingale has $E[M_n \mid \mathcal{F}_m] \geq M_m$ — its expected value <em>increases</em> (favourable game). The terminology is inherited from the analogy with superharmonic and subharmonic functions, not from a comparison of growth rates. A martingale is simultaneously both a submartingale and a supermartingale.</div>
</div>

---

### Part 4 — The Discrete Stochastic Integral

<div class="note-abstract" markdown="1">
"Suppose that $M_0, M_1, \ldots$ is a martingale with respect to the filtration $\mathcal{F}_n$. For $n \geq 1$, let $\Delta M_n = M_n - M_{n-1}$. Let $B_j$ denote the 'bet' on the $j$th game. We allow negative values of $B_j$ which indicate betting that the price will go down or the game will be lost. Let $W_n$ denote the winnings in this strategy: $W_0 = 0$ and for $n \geq 1$,

$$W_n = \sum_{j=1}^n B_j [M_j - M_{j-1}] = \sum_{j=1}^n B_j \Delta M_j.$$"
</div>


**Three conditions on the betting strategy $B_n$:**

1. **Boundedness:** $\lvert B_n \rvert \leq K_n < \infty$ for some finite constant $K_n$ — bets cannot be infinite.
2. **Non-anticipating (predictability):** $B_n$ is $\mathcal{F}_{n-1}$-measurable — the bet at time $n$ can only use information from before time $n$. You cannot see the outcome before placing the bet.
3. **Integrability:** The bound above ensures $E[\lvert W_n \rvert] < \infty$.

**$W_n$ is a martingale — verification:**

"Also,

$$E[W_{n+1} \mid \mathcal{F}_n] = E[W_n + B_{n+1}(M_{n+1} - M_n) \mid \mathcal{F}_n].$$

Since $W_n$ is $\mathcal{F}_n$-measurable, $E[W_n \mid \mathcal{F}_n] = W_n$. Also, since $B_{n+1}$ is $\mathcal{F}_n$-measurable and $M$ is a martingale,

$$E[B_{n+1}(M_{n+1} - M_n) \mid \mathcal{F}_n] = B_{n+1} E[M_{n+1} - M_n \mid \mathcal{F}_n] = 0.$$

Therefore, $E[W_{n+1} \mid \mathcal{F}_n] = W_n$."

The key steps use Properties 1 and 5 from §1.1 in sequence: $W_n$ is known at time $n$ (Property 1); $B_{n+1}$ is known at time $n$ and pulls out (Property 5); the remaining factor $E[M_{n+1} - M_n \mid \mathcal{F}_n] = 0$ by the martingale property of $M$.

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception — Predictability</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "$B_n$ being $\mathcal{F}_{n-1}$-measurable is just a technicality — any adapted strategy should work."</div>
  <div class="mc-correct"><strong>Correct:</strong> The $\mathcal{F}_{n-1}$-measurability of $B_n$ is the mathematical statement that you must commit your bet <em>before</em> observing $\Delta M_n$. If $B_n$ were allowed to depend on $M_n$ (i.e., be $\mathcal{F}_n$-measurable), then you could trivially "bet" after seeing the outcome and always win. The non-anticipating condition is what makes the game fair and is precisely the condition that forces $W_n$ to remain a martingale.</div>
</div>



  </div>
</div>
