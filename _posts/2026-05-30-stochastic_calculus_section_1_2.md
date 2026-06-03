---
layout: distill
title: "Stochastic Calculus — Study Notes"
description: Study notes for Lawler's Stochastic Calculus (Chapter 1 — Martingales in Discrete Time).
tags: Stochastic Calculus
giscus_comments: true
date: 2026-06-01
featured: true
thumbnail: https://magica.com/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FIBw5a8ByyzY%2Fmaxresdefault.jpg&w=3840&q=75

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Section 1.4 — Martingale Convergence Theorem

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


## Section 1.4 — Martingale Convergence Theorem

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('s14')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">§ 1.4</span>
      <div>
        <div class="chapter-title">Section 1.4 — Martingale Convergence Theorem</div>
        <div class="chapter-subtitle">Upcrossing proof of a.s. convergence, Pólya's urn, and the Bayesian statistics connection</div>
      </div>
    </div>
    <span class="chapter-arrow" id="s14-arrow">▼</span>
  </button>
  <div class="chapter-body" id="s14-body" markdown="1">

### Notation at a Glance

| Symbol | Meaning |
|---|---|
| $$M_\infty$$ | The almost-sure limit of $$M_n$$ — guaranteed by the MCT when $$E[\lvert M_n \rvert] \leq C$$ |
| $$\sup_n E[\lvert M_n \rvert] \leq C$$ | Uniform $$L^1$$ bound — the hypothesis of the MCT |
| $$\liminf_{n\to\infty} M_n$$, $$\limsup_{n\to\infty} M_n$$ | Smallest and largest cluster points of the sequence $$(M_n)$$ |
| $$U_n(a,b)$$ | Number of upcrossings of $$[a,b]$$ by time $$n$$ |
| $$U_\infty(a,b)$$ | Total upcrossings of $$[a,b]$$; MCT proof shows $$E[U_\infty] < \infty$$ |
| $$S_j,\, T_j$$ | Buy and sell stopping times in the upcrossing strategy |
| $$W_n$$ | Winnings from the buy-low-sell-high strategy used in the proof |
| $$R_n,\, G_n$$ | Number of red and green balls in Pólya's urn after $$n$$ draws |
| $$M_n = R_n/(n+2)$$ | Fraction of red balls — a bounded nonneg martingale converging a.s. |
| $$M_\infty \sim \mathrm{Uniform}[0,1]$$ | The limiting distribution of Pólya's urn |
| $$f_{n,k}(\theta)$$ | Posterior Beta density for $$\theta$$ after $$n$$ Bernoulli trials with $$k$$ successes |

---

### Part 1 — The Core Intuition

<div class="note-abstract">
The Martingale Convergence Theorem (MCT) answers: <em>if a martingale is uniformly bounded in $L^1$, must it converge?</em> The answer is yes — it converges almost surely to a finite limit. The proof uses a financial argument: if the sequence did not converge, it would oscillate infinitely between some values $a$ and $b$, and a "buy low, sell high" strategy would extract infinite expected profit from a fair game. Since that is impossible, convergence must hold. Crucially, the limit $M_\infty$ need not satisfy $E[M_\infty] = E[M_0]$ — the martingale property can fail in the limit even when it holds at every finite time.
</div>

<b>CORE IDEAS</b>

<strong>Uniform $$L^1$$ boundedness forces almost-sure convergence.</strong> The condition $$\sup_n E[\lvert M_n \rvert] \leq C < \infty$$ prevents the martingale from wandering to $$\pm\infty$$, and the upcrossing argument shows it cannot oscillate indefinitely between any two levels $$a < b$$. Together these force $$\lim_{n\to\infty} M_n$$ to exist with probability one.

<strong>The proof is a financial argument via upcrossings.</strong> If $$M_n$$ crossed between $a$ and $b$ infinitely often, buying every time $$M_n \leq a$$ and selling every time $$M_n \geq b$$ would produce infinite expected profit. Since $$M_n$$ is a fair game, that is impossible. The upcrossing inequality makes this precise and quantitative.

<strong>$$E[M_\infty] = E[M_0]$$ does NOT follow from the MCT.</strong> The theorem guarantees a.s. convergence but not convergence of expectations. The martingale doubling strategy from §1.2 illustrates this: $$E[\lvert W_n \rvert] \leq 2$$ for all $$n$$, so the MCT applies and $$W_\infty = 1$$ a.s., yet $$E[W_\infty] = 1 \neq 0 = E[W_0]$$. Preserving the mean requires the extra conditions of the OST.

<strong>Nonnegative martingales automatically satisfy the MCT hypothesis.</strong> If $$M_n \geq 0$$ for all $$n$$, then $$E[\lvert M_n \rvert] = E[M_n] = E[M_0]$$, so the $$L^1$$ bound holds with $$C = E[M_0]$$. Pólya's urn is the prime example.

---

### Part 2 — The Theorem

<div class="example-block" markdown="1">
<div class="ex-title">Theorem 1.4.1 — Martingale Convergence Theorem <span class="ex-pill pill-thm">Theorem</span></div>

Suppose $$M_n$$ is a martingale with respect to $$\{\mathcal{F}_n\}$$ and there exists $$C < \infty$$ such that $$E[\lvert M_n \rvert] \leq C$$ for all $$n$$. Then there exists a random variable $$M_\infty$$ such that with probability one

$$\lim_{n \to \infty} M_n = M_\infty.$$
</div>

**Unpacking the hypothesis** — $$E[\lvert M_n \rvert] \leq C$$ uniformly in $$n$$: The absolute mean of $$M_n$$ stays bounded no matter how far the process runs. Since $$E[\lvert M_n \rvert] \geq \lvert E[M_n] \rvert = \lvert E[M_0] \rvert$$, this implicitly requires $$E[M_0]$$ to be finite, but it is strictly stronger — it controls the size of fluctuations, not just the level.

**Unpacking the conclusion** — "with probability one": There exists a single event $$\Omega^* \subseteq \Omega$$ with $$P(\Omega^*) = 1$$ such that for every $$\omega \in \Omega^*$$, the real sequence $$(M_n(\omega))$$ converges to a finite number $$M_\infty(\omega)$$.

**What the theorem does NOT say:**

- It does not say $$E[M_\infty] = E[M_0]$$.
- It does not say convergence is in $$L^1$$ or $$L^2$$.
- It does say $$E[\lvert M_\infty \rvert] \leq C$$ — this follows from Fatou's lemma: $$E[\lvert M_\infty \rvert] = E[\liminf \lvert M_n \rvert] \leq \liminf E[\lvert M_n \rvert] \leq C$$.

---

### Part 3 — The Upcrossing Proof

<div class="note-abstract">
The proof is built on the "buy low, sell high" strategy. The key object is the number of upcrossings — the number of times the sequence rises from below $a$ to above $b$. The Upcrossing Inequality bounds the expected number of such crossings by a quantity that is finite whenever $E[\lvert M_n \rvert] \leq C$. Finiteness of expected upcrossings then forces a.s. convergence.
</div>

#### Step 1 — Define the upcrossing stopping times

Fix $$a < b$$. Define stopping times implementing "buy at $$a$$, sell at $$b$$":

$$S_1 = \min\{n : M_n \leq a\}, \qquad T_1 = \min\{n > S_1 : M_n \geq b\},$$

$$S_j = \min\{n > T_{j-1} : M_n \leq a\}, \qquad T_j = \min\{n > S_j : M_n \geq b\}.$$

The number of completed upcrossings by time $$n$$ is:

$$U_n = U_n(a,b) = \max\{j : T_j \leq n\}.$$

Each completed upcrossing — going from $$\leq a$$ up to $$\geq b$$ — produces a profit of at least $$b - a$$.

#### Step 2 — Construct the predictable betting strategy

Define bets $$B_k = \mathbf{1}_{\{S_j \leq k-1 < T_j \text{ for some } j\}}$$, i.e., $$B_k = 1$$ when a position is held (bought but not yet sold), $$B_k = 0$$ otherwise. This is $$\mathcal{F}_{k-1}$$-measurable since whether we hold at step $$k$$ depends only on $$M_0, \ldots, M_{k-1}$$.

The winnings from this strategy satisfy:

$$W_n \geq U_n(b - a) - (a - M_n).$$

Here $$U_n(b-a)$$ is the profit from completed upcrossings, and $$(a - M_n)$$ is the potential loss on a position still open at time $$n$$ (held below $$a$$).

#### Step 3 — Apply the martingale property of $$W_n$$

Since $$B_k$$ is predictable and bounded, $$W_n$$ is a martingale (§1.2), so $$E[W_n] = 0$$:

$$0 = E[W_n] \geq (b-a)\, E[U_n] - E[(a - M_n)].$$

Using $$(a - M_n) \leq \lvert a \rvert + \lvert M_n \rvert$$:

$$\boxed{E[U_n(a,b)] \leq \frac{\lvert a \rvert + E[\lvert M_n \rvert]}{b - a} \leq \frac{\lvert a \rvert + C}{b - a} < \infty.}$$

This is **Doob's Upcrossing Inequality**.

#### Step 4 — Conclude almost-sure convergence

Since $$E[U_n] \leq (\lvert a \rvert + C)/(b-a)$$ for every $$n$$, monotone convergence gives:

$$E[U_\infty(a,b)] \leq \frac{\lvert a \rvert + C}{b - a} < \infty \implies U_\infty(a,b) < \infty \quad \text{a.s.}$$

Now let $$a, b$$ range over all rational pairs $$a < b$$. There are only countably many such pairs, so:

$$P\bigl(\exists\, a < b \text{ rational}: U_\infty(a,b) = \infty\bigr) = 0.$$

On the complementary event (probability one), $$U_\infty(a,b) < \infty$$ for every rational pair, which forces $$\liminf_{n \to \infty} M_n = \limsup_{n \to \infty} M_n$$ a.s. Hence $$M_\infty = \lim_{n \to \infty} M_n$$ exists and is finite a.s.

---


### Part 5 — Pólya's Urn

<div class="note-abstract">
Pólya's urn is the canonical application of the MCT. The fraction of red balls $M_n = R_n/(n+2)$ is a bounded nonneg martingale, so the MCT guarantees its a.s. convergence to a limit $M_\infty$. The remarkable fact: $M_\infty$ is uniformly distributed on $[0,1]$ — the urn settles to a random stable fraction that is completely unpredictable in advance.
</div>

#### Setup

Start with one red and one green ball. At each step: draw a ball uniformly at random, observe its colour, return it plus one new ball of the same colour.

- $$R_0 = G_0 = 1$$, and $$R_n + G_n = n + 2$$ after $$n$$ draws.
- $$M_n = R_n/(n+2)$$: fraction of red balls.
- Transition: $$P\{R_{n+1} = R_n + 1 \mid \mathcal{F}_n\} = M_n$$.

#### <span>$$M_n$$</span> is a martingale — verification

$$
\begin{aligned}
$$E[M_{n+1} \mid \mathcal{F}_n] 
&= M_n \cdot \frac{R_n + 1}{n+3} + (1 - M_n) \cdot \frac{R_n}{n+3} \\
&= \frac{R_n(n+3)}{(n+2)(n+3)} \\
&= \frac{R_n}{n+2} \\
&= M_n. \checkmark$$
\end{aligned}
$$

#### MCT applies

Since $$0 \leq M_n \leq 1$$, we have $$E[\lvert M_n \rvert] = E[M_n] = E[M_0] = \tfrac{1}{2}$$. The uniform $$L^1$$ bound holds with $$C = \tfrac{1}{2}$$, so the MCT gives:

$$M_\infty = \lim_{n \to \infty} M_n \quad \text{exists a.s.}$$

#### The limiting distribution is <span>$$\mathrm{Uniform}[0,1]$$</span>

Exercise 1.11 establishes that for each $$n$$, $$M_n$$ is uniform on the finite set $$\bigl\{\tfrac{1}{n+2}, \tfrac{2}{n+2}, \ldots, \tfrac{n+1}{n+2}\bigr\}$$. As $$n \to \infty$$ this discrete uniform converges in distribution to $$\mathrm{Uniform}[0,1]$$, so $$M_\infty \sim \mathrm{Uniform}[0,1]$$.

<div class="result-box"><strong>Starting from one red and one green ball, the long-run fraction of red balls $M_\infty$ is uniformly distributed on $[0,1]$. The urn stabilises to a definite proportion, but that proportion is itself completely random.</strong></div>

---

### Part 6 — Connection to Bayesian Statistics

<div class="note-abstract">
Pólya's urn is not merely a toy model — it is exactly the Bayesian update rule for a Bernoulli parameter $\theta$ with a uniform prior. The MCT, reinterpreted, is a Bayesian consistency theorem: the posterior mean converges a.s. to the true $\theta$ as data accumulates.
</div>

**Setup:** Run Bernoulli trials with unknown success probability $$\theta$$, starting from a $$\mathrm{Uniform}[0,1]$$ prior. After $$n$$ trials with $$S_n = k$$ successes, the Bayes update gives the posterior:

$$f_{n,k}(\theta) \propto \theta^k (1-\theta)^{n-k}, \quad \theta \in (0,1).$$

This is the $$\mathrm{Beta}(k+1,\, n-k+1)$$ density, with posterior mean:

$$E[\theta \mid S_n = k] = \frac{k+1}{n+2} = \frac{S_n + 1}{n+2}.$$

This is **identical to the Pólya urn fraction** $$M_n = R_n/(n+2)$$ when $$R_n = S_n + 1$$ (successes plus the one initial red ball). The urn fraction equals the posterior mean at every step.

**MCT as Bayesian law of large numbers:** By the strong law, $$S_n/n \to \theta$$ a.s. Combined with $$M_n \to M_\infty$$ a.s., we get $$M_\infty = \theta$$ a.s. — the posterior mean converges to the true parameter.

<div class="result-box"><strong>Pólya's urn is the Bayesian update mechanism for a Bernoulli parameter with uniform prior. The MCT is the statement that Bayesian inference is consistent: the posterior mean converges a.s. to the true $\theta$.</strong></div>

---

### Part 7 — When MCT Fails: Simple Random Walk

"Let $$S_n = X_1 + \cdots + X_n$$ be simple symmetric random walk starting at the origin. Then one can easily see that $$E[\lvert S_n \rvert] \to \infty$$. For this example, with probability one $$\limsup_{n \to \infty} S_n = \infty$$ and $$\liminf_{n \to \infty} S_n = -\infty$$."

**Why the hypothesis fails:** $$E[S_n^2] = n \to \infty$$, so by Jensen's inequality $$E[\lvert S_n \rvert] \geq \sqrt{E[S_n^2]/n} \cdot \sqrt{n} \to \infty$$. The uniform $$L^1$$ bound fails. The walk oscillates between $$+\infty$$ and $$-\infty$$, crossing every interval $$[a,b]$$ infinitely often — exactly what the upcrossing bound prevents when the bound holds.

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "Since $S_n$ is a martingale, the MCT says $S_n$ converges."</div>
  <div class="mc-correct"><strong>Correct:</strong> The MCT requires $\sup_n E[\lvert M_n \rvert] \leq C$. For simple random walk $E[\lvert S_n \rvert] \sim \sqrt{2n/\pi} \to \infty$, so the hypothesis fails. Correspondingly, $\limsup S_n = +\infty$ and $\liminf S_n = -\infty$ a.s. — the walk does not converge. The MCT does not apply.</div>
</div>

---

### Part 8 — MCT vs OST: Complementary Tools

| | **MCT** | **OST** |
|---|---|---|
| **Question** | Does $$M_n$$ converge as $$n \to \infty$$? | Does $$E[M_T] = E[M_0]$$ at a stopping time? |
| **Hypothesis** | $$\sup_n E[\lvert M_n \rvert] \leq C$$ | Bounded $$T$$, or (1.8), or (1.9) |
| **Conclusion** | $$M_n \to M_\infty$$ a.s. | $$E[M_T] = E[M_0]$$ |
| **Mean preserved?** | Not guaranteed | Yes — that is the conclusion |
| **Counterexample** | Simple random walk: $$E[\lvert S_n \rvert] \to \infty$$, no convergence | Doubling strategy: $$P\{T<\infty\}=1$$ but $$E[W_T] \neq E[W_0]$$ |
| **Key tool** | Upcrossing inequality | Stopped process is a martingale |

---

### Term Glossary

<div class="glossary-entry">
<div class="gterm">Martingale Convergence Theorem (MCT) <span class="gcat cat-thm">Theorem</span></div>
If $M_n$ is a martingale with $\sup_n E[\lvert M_n \rvert] \leq C < \infty$, then $M_\infty = \lim_{n\to\infty} M_n$ exists and is finite a.s. The limit satisfies $E[\lvert M_\infty \rvert] \leq C$ by Fatou's lemma, but $E[M_\infty]$ need not equal $E[M_0]$.
</div>

<div class="glossary-entry">
<div class="gterm">Uniform $L^1$ bound <span class="gcat cat-prop">Property</span></div>
The condition $\sup_{n \geq 0} E[\lvert M_n \rvert] \leq C < \infty$. The hypothesis of the MCT. Automatically satisfied for nonneg martingales (since $E[\lvert M_n \rvert] = E[M_n] = E[M_0]$) and for $L^\infty$-bounded martingales. Fails for simple random walk.
</div>

<div class="glossary-entry">
<div class="gterm">Upcrossing $U_n(a,b)$ <span class="gcat cat-defn">Definition</span></div>
The number of times $(M_0, M_1, \ldots, M_n)$ rises from $\leq a$ up through $\geq b$ (a complete upward crossing of the interval $[a,b]$). A sequence converges if and only if $U_\infty(a,b) < \infty$ for every rational $a < b$. The MCT proof shows this holds whenever $\sup_n E[\lvert M_n \rvert] \leq C$.
</div>

<div class="glossary-entry">
<div class="gterm">Doob's Upcrossing Inequality <span class="gcat cat-thm">Theorem</span></div>
For any martingale $M_n$ with $\sup_n E[\lvert M_n \rvert] \leq C$ and any $a < b$:

$$E[U_n(a,b)] \leq \frac{\lvert a \rvert + C}{b - a}.$$

The right side is finite and independent of $n$. Monotone convergence then gives $E[U_\infty(a,b)] \leq (\lvert a \rvert + C)/(b-a) < \infty$, forcing $U_\infty(a,b) < \infty$ a.s. and hence a.s. convergence of $M_n$.
</div>

<div class="glossary-entry">
<div class="gterm">Almost-sure (a.s.) convergence <span class="gcat cat-defn">Definition</span></div>
$M_n \to M_\infty$ a.s. means $P(\{\omega : M_n(\omega) \to M_\infty(\omega)\}) = 1$. Stronger than convergence in probability; weaker than $L^1$ convergence. The MCT delivers a.s. convergence. Upgrading to $L^1$ convergence (and hence $E[M_\infty] = E[M_0]$) requires the additional condition of uniform integrability.
</div>

<div class="glossary-entry">
<div class="gterm">Uniform integrability <span class="gcat cat-prop">Property</span></div>
A sequence $(M_n)$ is uniformly integrable if $\lim_{K\to\infty} \sup_n E[\lvert M_n \rvert \mathbf{1}_{\{\lvert M_n \rvert \geq K\}}] = 0$. Strictly stronger than $\sup_n E[\lvert M_n \rvert] \leq C$. Under UI, a.s. convergence implies $L^1$ convergence and $E[M_\infty] = E[M_0]$. The doubling strategy $W_n$ is not uniformly integrable.
</div>

<div class="glossary-entry">
<div class="gterm">Pólya's urn <span class="gcat cat-defn">Definition</span></div>
A reinforcement model: start with one red and one green ball; at each step draw uniformly at random, observe the colour, return it with one extra ball of the same colour. The fraction of red balls $M_n = R_n/(n+2)$ is a nonneg martingale with $0 \leq M_n \leq 1$, converging a.s. to $M_\infty \sim \mathrm{Uniform}[0,1]$. Equivalent to Bayesian updating for a Bernoulli parameter $\theta$ with a uniform prior.
</div>

<div class="glossary-entry">
<div class="gterm">Beta distribution $\mathrm{Beta}(k+1,\, n-k+1)$ <span class="gcat cat-defn">Definition</span></div>
The posterior distribution of a Bernoulli success probability $\theta$ after $n$ trials with $k$ successes, given a $\mathrm{Uniform}[0,1]$ prior. Density $\propto \theta^k(1-\theta)^{n-k}$. Posterior mean $(k+1)/(n+2)$, identical to the Pólya urn fraction $M_n = R_n/(n+2)$.
</div>

<div class="glossary-entry">
<div class="gterm">Markov property (discrete time) <span class="gcat cat-prop">Property</span></div>
A process $Y_n$ is Markov if the conditional distribution of $(Y_{n+1}, Y_{n+2}, \ldots)$ given $(Y_0, \ldots, Y_n)$ depends only on $Y_n$. Pólya's urn satisfies this: future evolution depends only on the current fraction $M_n$. Used in the martingale verification: $E[M_{n+1} \mid \mathcal{F}_n] = E[M_{n+1} \mid M_n]$.
</div>

---

### Study-Note Summary

- The **Martingale Convergence Theorem**: if $$\sup_n E[\lvert M_n \rvert] \leq C < \infty$$, then $$M_n \to M_\infty$$ a.s. to a finite random variable. The MCT does **not** guarantee $$E[M_\infty] = E[M_0]$$ — that requires uniform integrability.
- **Proof via upcrossings**: define buy/sell stopping times at levels $$a$$ and $$b$$; the resulting winnings are a martingale with $$E[W_n] = 0$$; this forces $$E[U_n(a,b)] \leq (\lvert a \rvert + C)/(b-a) < \infty$$ (Doob's inequality). Finite expected upcrossings over all rational pairs implies $$\liminf M_n = \limsup M_n$$ a.s., i.e., convergence.
- **Nonneg martingales** automatically satisfy the hypothesis since $$E[\lvert M_n \rvert] = E[M_n] = E[M_0]$$.
- **Doubling strategy $$W_n$$**: satisfies $$E[\lvert W_n \rvert] \leq 2$$, so MCT applies and $$W_\infty = 1$$ a.s. But $$E[W_\infty] = 1 \neq 0 = E[W_0]$$ — this is not a contradiction; the MCT never promises mean preservation.
- **Pólya's urn**: the fraction $$M_n = R_n/(n+2)$$ is a bounded nonneg martingale converging a.s. to $$M_\infty \sim \mathrm{Uniform}[0,1]$$. The urn stabilises at a random fraction that is uniformly distributed.
- **Bayesian connection**: the Pólya transition probabilities equal the posterior mean for a Bernoulli $$\theta$$ with a uniform prior. The MCT is the consistency theorem: posterior mean $$\to \theta$$ a.s.
- **Simple random walk fails MCT**: $$E[\lvert S_n \rvert] \sim \sqrt{2n/\pi} \to \infty$$, the hypothesis fails, and $$\limsup S_n = +\infty$$, $$\liminf S_n = -\infty$$ a.s. — the walk never converges.

<div class="ref-tags">
<span class="ref-tag">Martingale Convergence Theorem</span>
<span class="ref-tag">Upcrossing inequality</span>
<span class="ref-tag">Almost-sure convergence</span>
<span class="ref-tag">Uniform integrability</span>
<span class="ref-tag">Pólya's urn</span>
<span class="ref-tag">Beta distribution</span>
<span class="ref-tag">Bayesian statistics</span>
<span class="ref-tag">Nonneg martingale</span>
<span class="ref-tag">Martingale</span>
</div>

  </div>
</div>
