---
layout: distill
title: "Stochastic Calculus — Study Notes"
description: Study notes for Lawler's Stochastic Calculus (Chapter 1 — Martingales in Discrete Time).
tags: Stochastic Calculus
giscus_comments: true
date: 2026-05-31
featured: true
thumbnail: https://magica.com/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FIBw5a8ByyzY%2Fmaxresdefault.jpg&w=3840&q=75

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Section 1.3 — Optional Sampling Theorem

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
  .pill-thm  { background: #d1fae5; color: #064e3b; }
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


## Section 1.3 — Optional Sampling Theorem

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('s13')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">§ 1.3</span>
      <div>
        <div class="chapter-title">Section 1.3 — Optional Sampling Theorem</div>
        <div class="chapter-subtitle">Stopping times, the three versions of the OST, and the gambler's ruin estimates for random walk</div>
      </div>
    </div>
    <span class="chapter-arrow" id="s13-arrow">▼</span>
  </button>
  <div class="chapter-body" id="s13-body" markdown="1">

### Notation at a Glance

<div class="notation-panel" markdown="1">

| Symbol | Meaning |
|---|---|
| $$T$$ | A stopping time — a random time that depends only on past and present observations |
| $$\{T = n\} \in \mathcal{F}_n$$ | The defining measurability condition for a stopping time |
| $$n \wedge T$$ | $$\min\{n, T\}$$ — the process stopped at time $$T$$ |
| $$M_{n \wedge T}$$ | The stopped process — equals $$M_T$$ once $$T$$ is reached, stays there afterwards |
| $$E[M_T] = E[M_0]$$ | The optional sampling conclusion — martingale mean preserved at stopping time $$T$$ |
| $$P\{T \leq k\} = 1$$ | $$T$$ is bounded — the strongest assumption guaranteeing $$E[M_T] = E[M_0]$$ |
| $$P\{T < \infty\} = 1$$ | $$T$$ is almost surely finite — weaker condition, needs extra hypotheses |
| $$\mathbf{1}_{\{T > n\}}$$ | Indicator that we have not yet stopped by time $$n$$ |
| $$E[\lvert M_n \rvert \mathbf{1}_{\{T>n\}}] \to 0$$ | The uniform integrability condition in OST II |
| $$E[M_{n \wedge T}^2] \leq C$$ | The $$L^2$$ boundedness condition in OST III |
| $$S_n$$ | Simple symmetric random walk $$X_1 + \cdots + X_n$$ with $$P\{X_j = \pm 1\} = \tfrac{1}{2}$$ |

</div>

---

### Part 1 — The Core Intuition

<div class="note-abstract">
The Optional Sampling Theorem (OST) answers the question: <em>if you are allowed to stop a martingale at a random time of your choosing, can you change its expected value?</em> The answer is no — under appropriate conditions. This is the mathematical statement that you cannot beat a fair game even by choosing <em>when</em> to stop playing.
</div>

#### Core ideas

<div class="key-idea"><strong>Stopping a martingale produces another martingale.</strong> The stopped process $Y_n = M_{n \wedge T}$ is always a martingale, regardless of what the stopping time $T$ is.</div>

<div class="key-idea"><strong>$E[M_T] = E[M_0]$ requires extra conditions beyond just $P\{T < \infty\} = 1$.</strong> The stopped process has constant mean $E[M_{n \wedge T}] = E[M_0]$ for all finite $n$. Passing this to the limit $n \to \infty$ — to get $E[M_T] = E[M_0]$ — requires uniform integrability or $L^2$ boundedness.</div>

<div class="key-idea"><strong>The OST is a tool for computing probabilities and expectations.</strong> By choosing a clever stopping time $T$ and applying OST to two different martingales simultaneously — $S_n$ and $S_n^2 - n$ — one can extract exact formulas for hitting probabilities and expected hitting times. Examples 1.3.1 and 1.3.2 demonstrate this technique completely.</div>

---

### Part 2 — Stopping Times

<div class="example-block" markdown="1">
<div class="ex-title">Definition — Stopping Time <span class="ex-pill pill-defn">Definition</span></div>

A nonnegative integer-valued random variable $$T$$ is a <b>stopping time</b> with respect to the filtration $$\{\mathcal{F}_n\}$$ if for each $$n$$ the event $$\{T = n\}$$ is $$\mathcal{F}_n$$-measurable.

**What this means:** The decision to stop at time $$n$$ can only use information available up to and including time $$n$$. You cannot decide to stop "because something will happen tomorrow."

**Equivalent condition:** $$\{T \leq n\} \in \mathcal{F}_n$$ for every $$n$$, since

$$\{T \leq n\} = \{T = 0\} \cup \{T = 1\} \cup \cdots \cup \{T = n\},$$

and each event $$\{T = k\} \in \mathcal{F}_k \subseteq \mathcal{F}_n$$.

**The betting interpretation:** $$T$$ is a stopping time if and only if the strategy "bet 1 on rounds $$1, 2, \ldots, T$$ and bet 0 afterwards" is an allowable (predictable) betting strategy in the sense of §1.2. The bet $$B_j = \mathbf{1}_{\{j \leq T\}}$$ is $$\mathcal{F}_{j-1}$$-measurable precisely because $$\{T \geq j\} = \{T \leq j-1\}^c \in \mathcal{F}_{j-1}$$.
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Examples of stopping times and non-stopping times <span class="ex-pill pill-ex">Example</span></div>

**Valid stopping times:**
- $T = \min\{n : S_n = a\}$ — the first time the random walk hits level $a$. At time $n$ we know whether $S_n = a$, so $\{T = n\}$ is determined by $X_1,\ldots,X_n \in \mathcal{F}_n$. ✓
- $T = \min\{n : S_n \geq a\}$ — same reasoning. ✓
- $T = 5$ — a deterministic constant is always a stopping time since $\{T = 5\} = \Omega \in \mathcal{F}_5$ and $\{T = n\} = \emptyset \in \mathcal{F}_n$ for $n \neq 5$. ✓

**Not a stopping time:**
- $T = \max\{n \leq 10 : S_n = \max_{k \leq 10} S_k\}$ — the time of the overall maximum up to time 10. To know whether $T = n$ you need to know all future values $S_{n+1}, \ldots, S_{10}$, which are not in $\mathcal{F}_n$. ✗

<div class="ex-lesson"><strong>Key point:</strong> A stopping time is a decision rule that looks only backward and at the present — never forward. The "first time" something happens is always a stopping time; the "last time" something happens (over a fixed horizon) generally is not.</div>
</div>

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "Any random time $T$ with $P\{T < \infty\} = 1$ is a stopping time."</div>
  <div class="mc-correct"><strong>Correct:</strong> A random time is a stopping time only if the event $\{T = n\}$ is $\mathcal{F}_n$-measurable for every $n$ — it can only depend on the observations up to time $n$, not on future values. The condition $P\{T < \infty\} = 1$ is a statement about the distribution of $T$, not about its measurability structure.</div>
</div>

---

### Part 3 — The Stopped Process

"Let $T$ be the 'stopping time' for the strategy. Then the winnings at time $t$ is

$$M_0 + \sum_{j=1}^n B_j [M_j - M_{j-1}],$$

where $B_j = 1$ if $j \leq T$ and $B_j = 0$ if $j > T$. We can write this as $M_{n \wedge T}$, where $n \wedge T$ is shorthand for $\min\{n, T\}$."

**The stopped process $M_{n \wedge T}$:** at time $n$, the process equals:
- $M_n$ if $T > n$ (we have not stopped yet),
- $M_T$ if $T \leq n$ (we have already stopped and the value is frozen at $M_T$).

Since $B_j = \mathbf{1}_{\{j \leq T\}}$ is predictable (it is $\mathcal{F}_{j-1}$-measurable because $\{T \geq j\} \in \mathcal{F}_{j-1}$), the discrete stochastic integral result from §1.2 immediately gives:

<div class="result-box"><strong>The stopped process $Y_n = M_{n \wedge T}$ is always a martingale with respect to $\{\mathcal{F}_n\}$.</strong> In particular, $E[M_{n \wedge T}] = E[M_0]$ for every finite $n$.</div>

---

### Part 4 — The Three Versions of the OST

#### OST I — Bounded Stopping Times

<div class="example-block" markdown="1">
<div class="ex-title">Theorem 1.3.1 — OST I (Bounded $$T$$) <span class="ex-pill pill-thm">Theorem</span></div>

"Suppose $$T$$ is a stopping time and $$M_n$$ is a martingale with respect to $$\{\mathcal{F}_n\}$$. Then $$Y_n = M_{n \wedge T}$$ is a martingale. In particular, for each $$n$$,

$$E[M_{n \wedge T}] = E[M_0].$$

If $$T$$ is bounded, that is, if there exists $$k < \infty$$ such that $$P\{T \leq k\} = 1$$, then

$$E[M_T] = E[M_0]. \tag{1.7}$$"

**Why (1.7) follows from boundedness:** Since $$P\{T \leq k\} = 1$$, we have $$n \wedge T = T$$ for all $$n \geq k$$. Therefore $$E[M_{n \wedge T}] = E[M_T]$$ for $$n \geq k$$. Combined with $$E[M_{n \wedge T}] = E[M_0]$$ for all $$n$$, we get $$E[M_T] = E[M_0]$$.

**No extra conditions are needed** when $$T$$ is bounded — the martingale property of the stopped process is all that is required.
</div>

#### OST II — Almost Surely Finite $T$ with Uniform Integrability

<div class="example-block" markdown="1">
<div class="ex-title">Theorem 1.3.2 — OST II (a.s. finite $$T$$ with UI condition) <span class="ex-pill pill-thm">Theorem</span></div>

"Suppose $$T$$ is a stopping time and $$M_n$$ is a martingale with respect to $$\{\mathcal{F}_n\}$$. Suppose that $$P\{T < \infty\} = 1$$, $$E[\lvert M_T \rvert] < \infty$$, and for each $$n$$,

$$\lim_{n \to \infty} E[\lvert M_n \rvert \mathbf{1}_{\{T > n\}}] = 0. \tag{1.8}$$

Then, $$E[M_T] = E[M_0]$$."

**Where the condition comes from:** For every finite $$n$$,

$$E[M_0] = E[M_{n \wedge T}] = E[M_T \mathbf{1}_{\{T \leq n\}}] + E[M_n \mathbf{1}_{\{T > n\}}].$$

As $$n \to \infty$$, the first term converges to $$E[M_T]$$ by dominated convergence (using $$E[\lvert M_T \rvert] < \infty$$). The second term vanishes by condition (1.8). Hence $$E[M_0] = E[M_T]$$.

**Condition (1.8) in plain English:** The contribution to the expected value from paths that have not yet stopped by time $$n$$ must vanish as $$n \to \infty$$. Paths that take very long to stop and reach very large values can violate this.

**The doubling strategy fails here:** In Example 1.2.4, if $$T = \min\{n : W_n = 1\}$$, then $$P\{T < \infty\} = 1$$ but $$E[\lvert W_n \rvert \mathbf{1}_{\{T > n\}}] = (2^n - 1) \cdot 2^{-n} \to 1 \neq 0$$. Condition (1.8) is violated, consistently with $$E[W_T] = 1 \neq 0 = E[W_0]$$.
</div>

#### OST III — $L^2$ Boundedness

<div class="example-block" markdown="1">
<div class="ex-title">Theorem 1.3.3 — OST III ($$L^2$$ bounded stopped process) <span class="ex-pill pill-thm">Theorem</span></div>

"Suppose $$T$$ is a stopping time and $$M_n$$ is a martingale with respect to $$\{\mathcal{F}_n\}$$. Suppose that $$P\{T < \infty\} = 1$$, $$E[\lvert M_T \rvert] < \infty$$, and that there exists $$C < \infty$$ such that for each $$n$$,

$$E[M_{n \wedge T}^2] \leq C. \tag{1.9}$$

Then, $$E[M_T] = E[M_0]$$."

**Why (1.9) implies (1.8) — the key argument:**

For any $$b > 0$$, split the expectation:

$$E[\lvert M_n \rvert \mathbf{1}_{\{T > n\}}] = E[\lvert M_n \rvert \mathbf{1}_{\{T > n,\, \lvert M_n \rvert \geq b\}}] + E[\lvert M_n \rvert \mathbf{1}_{\{T > n,\, \lvert M_n \rvert < b\}}].$$

- **First term:** By the Cauchy-Schwarz inequality and (1.9), $$E[\lvert M_n \rvert \mathbf{1}_{\{\lvert M_n \rvert \geq b,\, T > n\}}] \leq \frac{C}{b}$$.
- **Second term:** $$E[\lvert M_n \rvert \mathbf{1}_{\{T > n,\, \lvert M_n \rvert < b\}}] \leq b \cdot P\{T > n\} \to 0$$ since $$P\{T < \infty\} = 1$$.

Therefore $$\limsup_{n \to \infty} E[\lvert M_n \rvert \mathbf{1}_{\{T > n\}}] \leq C/b$$ for every $$b > 0$$, so the limit is $$0$$.

**Practical value:** Condition (1.9) is often easier to verify than (1.8) directly — it suffices to bound the second moment of the stopped process uniformly in $$n$$.
</div>

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception — When OST Applies</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "If $P\{T < \infty\} = 1$, then $E[M_T] = E[M_0]$ automatically."</div>
  <div class="mc-correct"><strong>Correct:</strong> $P\{T < \infty\} = 1$ is necessary but not sufficient. You additionally need either: (OST I) $T$ is bounded, or (OST II) condition (1.8) holds, or (OST III) condition (1.9) holds. The martingale doubling strategy provides an explicit counterexample where $P\{T < \infty\} = 1$ but $E[M_T] \neq E[M_0]$, because none of these three additional conditions hold.</div>
</div>

#### Summary — Three OST Versions

| Version | Assumption on $T$ | Extra condition | Conclusion |
|---|---|---|---|
| **OST I** | $P\{T \leq k\} = 1$ (bounded) | None | $E[M_T] = E[M_0]$ |
| **OST II** | $P\{T < \infty\} = 1$ | $E[M_{n}\mathbf{1}_{\{T>n\}}] \to 0$ | $E[M_T] = E[M_0]$ |
| **OST III** | $P\{T < \infty\} = 1$ | $E[M_{n \wedge T}^2] \leq C < \infty$ | $E[M_T] = E[M_0]$ |

---

### Part 5 — Worked Examples

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.3.1 — Gambler's ruin: hitting probability for random walk <span class="ex-pill pill-ex">Example</span></div>

"Gambler's ruin for random walk. Let $X_1, X_2, \ldots$ be independent, coin-tosses as in (1.6) and let $S_n = 1 + X_1 + \cdots + X_n$. $S_n$ is called simple (symmetric) random walk starting at 1. … Let $K > 1$ be a positive integer and let $T$ denote the first time $n$ such that $S_n = 0$ or $S_n = K$."

**Setup:**
- $S_n$ is a martingale (zero-mean increments, §1.2 Example 1.2.1).
- $T = \min\{n : S_n = 0 \text{ or } S_n = K\}$ is a stopping time.
- $S_n$ stays in $[0, K]$ for all $n \leq T$, so $0 \leq M_{n \wedge T} \leq K$ — the stopped process is bounded.
- Therefore (1.9) holds with $C = K^2$, and OST III applies.

**Apply OST to $S_n$:**

$$1 = E[S_0] = E[S_T] = 0 \cdot P\{S_T = 0\} + K \cdot P\{S_T = K\}.$$

Solving:

$$\boxed{P\{S_T = K\} = \frac{1}{K}, \qquad P\{S_T = 0\} = \frac{K-1}{K}.}$$

**Interpretation:** Starting at 1, with a fair game, the probability of reaching $K$ before 0 is $1/K$. As $K \to \infty$, $P\{S_T = K\} \to 0$: a gambler with \$1 playing against a casino with \$K almost surely goes broke. This is the **gambler's ruin estimate**.

<div class="ex-lesson"><strong>Key technique:</strong> The OST converts a martingale identity ($E[S_T] = E[S_0]$) into a linear equation in the unknown probability $P\{S_T = K\}$. The bounded stopping time (or $L^2$ bound) is what justifies passing the martingale identity through to time $T$.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.3.2 — Expected hitting time via the $$S_n^2 - n$$ martingale <span class="ex-pill pill-ex">Example</span></div>

"Let $S_n = X_1 + \cdots + X_n$ be simple random walk starting at 0. We have seen that $M_n = S_n^2 - n$ is a martingale. Let $J, K$ be positive integers and let $T = \min\{n : S_n = -J \text{ or } S_n = K\}$."

**Step 1 — Find $P\{S_T = K\}$ using $S_n$:**

Apply OST to $S_n$ (same argument as Example 1.3.1, starting at 0):

$$0 = E[S_T] = (-J) P\{S_T = -J\} + K \cdot P\{S_T = K\}.$$

$$\boxed{P\{S_T = K\} = \frac{J}{J+K}, \qquad P\{S_T = -J\} = \frac{K}{J+K}.}$$

**Step 2 — Find $E[T]$ using $M_n = S_n^2 - n$:**

Exercise 1.13 establishes that $E[M_{n \wedge T}^2] \leq C < \infty$, so OST III applies to $M_n$:

$$E[M_T] = E[M_0] \implies E[S_T^2] - E[T] = 0 \implies E[T] = E[S_T^2].$$

Compute $E[S_T^2]$ directly:

$$E[S_T^2] = J^2 P\{S_T = -J\} + K^2 P\{S_T = K\} = J^2 \cdot \frac{K}{J+K} + K^2 \cdot \frac{J}{J+K} = \frac{JK(J+K)}{J+K} = JK.$$

$$\boxed{E[T] = JK.}$$

**Interpretation:** The expected time for symmetric random walk to exit $(-J, K)$ starting from 0 is exactly $JK$. In particular, to travel distance $K$ from the origin in either direction, the expected time is $K^2$ (set $J = K$).

<div class="ex-lesson"><strong>Key technique:</strong> Apply OST to <em>two different martingales simultaneously</em>: $S_n$ to get hitting probabilities, and $S_n^2 - n$ to get the expected hitting time. The two martingale identities together determine both unknowns ($P\{S_T = K\}$ and $E[T]$) exactly.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.3.3 — OST fails: $$P\{T < \infty\} = 1$$ but $$E[S_0] \neq E[S_T]$$ <span class="ex-pill pill-warn">Counterexample</span></div>

"As in Example 1.3.2, let $S_n = X_1 + \cdots + X_n$ be simple random walk starting at 0. Let $T = \min\{n : S_n = 1\}$."

**$P\{T < \infty\} = 1$:** From Example 1.3.1, $P\{$random walk hits 1 before $-J\} = J/(J+1) \to 1$ as $J \to \infty$. So with probability one the walk reaches 1.

**But $E[T] = \infty$:** From Example 1.3.2, the expected time to exit $(-J, 1)$ starting at 0 is $J \cdot 1 = J$. Since this holds for all $J$ and $T \geq T_J$ (where $T_J$ is the exit time from $(-J,1)$), we have $E[T] \geq J$ for all $J$, so $E[T] = \infty$.

**OST fails:** $S_T = 1$ almost surely, so $E[S_T] = 1 \neq 0 = E[S_0]$.

**Why:** Neither condition (1.8) nor (1.9) holds for this $T$. In particular, $E[M_{n \wedge T}^2] = E[S_{n \wedge T}^2] \to \infty$ as $n \to \infty$, violating (1.9).

<div class="ex-lesson"><strong>Key lesson:</strong> $P\{T < \infty\} = 1$ is not sufficient on its own. An infinite expected stopping time ($E[T] = \infty$) is a warning sign that the extra conditions of OST II or III may fail. Always verify one of the three conditions before applying OST.</div>
</div>

---

### Part 6 — Why the Doubling Strategy Does Not Contradict OST

The martingale betting strategy from §1.2 Example 1.2.4 has:
- $W_n$ is a martingale for every finite $n$, so $E[W_n] = 0$.
- $T = \min\{n : W_n = 1\}$ satisfies $P\{T < \infty\} = 1$.
- $W_T = 1$, so $E[W_T] = 1 \neq 0 = E[W_0]$.

**Checking that OST conditions fail:**

$$E[\lvert W_n \rvert \mathbf{1}_{\{T > n\}}] = (2^n - 1) \cdot 2^{-n} \to 1 \neq 0,$$

so condition (1.8) is violated. Since $E[W_{n \wedge T}^2] \to \infty$ as well, condition (1.9) also fails. And $T$ is clearly unbounded. All three OST conditions fail, consistently with $E[W_T] \neq E[W_0]$.

<div class="result-box"><strong>The OST is not violated by the doubling strategy — the doubling strategy simply does not satisfy any of the three OST conditions.</strong> It is an example constructed precisely to illustrate why these conditions are necessary.</div>

---

### Term Glossary

<div class="glossary-entry">
<div class="gterm">Bounded stopping time <span class="gcat cat-defn">Definition</span></div>
A stopping time $T$ with $P\{T \leq k\} = 1$ for some finite $k$. The strongest assumption — guarantees OST with no additional conditions. In Examples 1.3.1 and 1.3.2 the stopping time is not bounded (the walk may take arbitrarily long to exit the interval) but the stopped process is bounded in value, which gives $L^2$ boundedness.
</div>

<div class="glossary-entry">
<div class="gterm">Uniform integrability condition (1.8) <span class="gcat cat-prop">Property</span></div>
The condition $\lim_{n \to \infty} E[\lvert M_n \rvert \mathbf{1}_{\{T > n\}}] = 0$ required by OST II. Ensures that paths which have not yet stopped by time $n$ contribute negligibly to the expectation as $n \to \infty$. Violated by the martingale doubling strategy: $E[\lvert W_n \rvert \mathbf{1}_{\{T > n\}}] \to 1$.
</div>

<div class="glossary-entry">
<div class="gterm">$L^2$ boundedness condition (1.9) <span class="gcat cat-prop">Property</span></div>
The condition $E[M_{n \wedge T}^2] \leq C < \infty$ for all $n$, required by OST III. Implies the uniform integrability condition (1.8) via Cauchy-Schwarz. Often easier to verify in practice — it suffices to show the stopped martingale has uniformly bounded second moment.
</div>

<div class="glossary-entry">
<div class="gterm">Gambler's ruin estimate <span class="gcat cat-thm">Theorem</span></div>
For simple symmetric random walk $S_n$ starting at $x \in \{0, 1, \ldots, K\}$ and $T = \min\{n : S_n = 0 \text{ or } S_n = K\}$:

$$P\{S_T = K \mid S_0 = x\} = \frac{x}{K}.$$

Derived by applying OST to $S_n$ and solving the resulting linear equation. Shows that starting at 1 against a casino at $K$, the ruin probability is $(K-1)/K \to 1$ as $K \to \infty$.
</div>

<div class="glossary-entry">
<div class="gterm">Expected hitting time <span class="gcat cat-thm">Theorem</span></div>
For simple symmetric random walk starting at 0 and $T = \min\{n : S_n = -J \text{ or } S_n = K\}$:

$$E[T] = JK.$$

Derived by applying OST to the martingale $M_n = S_n^2 - n$ together with the hitting probabilities from the gambler's ruin. In particular, starting at 0, the expected time to first exit the interval $(-K, K)$ is $K^2$.
</div>

<div class="glossary-entry">
<div class="gterm">Recurrence of random walk <span class="gcat cat-thm">Theorem</span></div>
Simple symmetric random walk returns to the origin with probability one: $P\{\tau < \infty\} = 1$ where $\tau = \min\{n \geq 1 : S_n = 0\}$. Follows from the gambler's ruin estimate by letting $K \to \infty$: $P\{S_T = 0\} = (K-1)/K \to 1$.
</div>


  </div>
</div>
