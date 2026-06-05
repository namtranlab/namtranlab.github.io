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

## Sections 1.5–1.7 — Square Integrable Martingales, Random Walk Integrals, and Maximal Inequality

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('s1567')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">§ 1.5–1.7</span>
      <div>
        <div class="chapter-title">Sections 1.5–1.7 — Square Integrable Martingales, Random Walk Integrals, and Maximal Inequality</div>
        <div class="chapter-subtitle">Orthogonality of increments, the variance rule, the discrete stochastic integral, and Doob's maximal inequality</div>
      </div>
    </div>
    <span class="chapter-arrow" id="s1567-arrow">▼</span>
  </button>
  <div class="chapter-body" id="s1567-body" markdown="1">

### Notation at a Glance

| Symbol | Meaning |
|---|---|
| $$E[M_n^2] < \infty$$ | Square integrability — the hypothesis of §1.5 |
| $$L^2(\Omega, \mathcal{F}, P)$$ | Hilbert space of square-integrable random variables with inner product $$(X,Y) = E[XY]$$ |
| $$(X, Y) = E[XY]$$ | Inner product on $$L^2$$ — orthogonality means $$(X,Y) = 0$$ |
| $$\Delta M_n = M_n - M_{n-1}$$ | Increment of $$M_n$$ at step $$n$$ |
| $$E[\Delta M_{n+1} \cdot \Delta M_{m+1}] = 0,\; m \neq n$$ | Orthogonality of martingale increments |
| $$J_n$$ | Predictable integrand — $$J_n$$ is $$\mathcal{F}_{n-1}$$-measurable |
| $$Z_n = \sum_{j=1}^n J_j X_j$$ | Discrete stochastic integral of $$J$$ with respect to the random walk $$S_n$$ |
| $$\sigma^2 = E[X_j^2]$$ | Variance of each i.i.d. increment |
| $$\mathrm{Var}[Z_n] = \sigma^2 \sum_{j=1}^n E[J_j^2]$$ | Variance rule for the discrete stochastic integral |
| $$\bar{Y}_n = \max\{Y_0, Y_1, \ldots, Y_n\}$$ | Running maximum of a nonneg submartingale $$Y_n$$ |
| $$\overline{M}_n = \max\{\lvert M_0 \rvert, \ldots, \lvert M_n \rvert\}$$ | Running maximum of $$\lvert M_n \rvert$$ |
| $$P\{\bar{Y}_n \geq a\} \leq a^{-1} E[Y_n]$$ | Doob's maximal inequality for submartingales |
| $$P\{\overline{M}_n \geq a\} \leq a^{-2} E[M_n^2]$$ | Doob's $$L^2$$ maximal inequality for square integrable martingales |

---

### Part 1 — Section 1.5: Square Integrable Martingales

<div class="example-block" markdown="1">
<div class="ex-title">Definition — Square Integrable Martingale <span class="ex-pill pill-defn">Definition</span></div>

"A martingale $$M_n$$ is called **square integrable** if for each $$n$$, $$E[M_n^2] < \infty$$."

This is the condition that $$M_n \in L^2(\Omega, \mathcal{F}_n, P)$$ at every time $$n$$.

**Why stronger than integrability:** Square integrability $$E[M_n^2] < \infty$$ implies integrability $$E[\lvert M_n \rvert] < \infty$$ by Jensen's inequality, but not vice versa.

**Why weaker than uniform $$L^2$$ boundedness:** The definition requires $$E[M_n^2] < \infty$$ for each fixed $$n$$, but the bound may grow with $$n$$. The stronger condition $$\sup_n E[M_n^2] \leq C < \infty$$ (used in OST III and the MCT) is a separate, stricter requirement.
</div>

#### Orthogonality of increments

"Random variables $$X, Y$$ are **orthogonal** if $$E[XY] = E[X]\, E[Y]$$."

For zero-mean random variables, orthogonality reduces to $$E[XY] = 0$$, i.e., $$(X, Y) = 0$$ in the $$L^2$$ inner product. Independent random variables are always orthogonal, but the converse fails in general.

<div class="example-block" markdown="1">
<div class="ex-title">Proposition 1.5.1 — Orthogonality of Martingale Increments <span class="ex-pill pill-prop">Proposition</span></div>

"Suppose that $$M_n$$ is a square integrable martingale with respect to $$\{\mathcal{F}_n\}$$. Then if $$m < n$$,

$$E[(\Delta M_{n+1})(\Delta M_{m+1})] = 0,$$

where $$\Delta M_k = M_k - M_{k-1}$$. Moreover, for all $$n$$,

$$E[M_n^2] = E[M_0^2] + \sum_{j=1}^n E\bigl[(\Delta M_j)^2\bigr].$$"

**Proof of orthogonality:**

For $$m < n$$, the increment $$\Delta M_{m+1} = M_{m+1} - M_m$$ is $$\mathcal{F}_n$$-measurable (since $$m+1 \leq n$$). Therefore:

$$E[(\Delta M_{n+1})(\Delta M_{m+1}) \mid \mathcal{F}_n] = (\Delta M_{m+1})\, E[\Delta M_{n+1} \mid \mathcal{F}_n] = (\Delta M_{m+1}) \cdot 0 = 0.$$

The second equality uses the martingale property: $$E[\Delta M_{n+1} \mid \mathcal{F}_n] = E[M_{n+1} - M_n \mid \mathcal{F}_n] = 0$$. Taking full expectations gives $$E[(\Delta M_{n+1})(\Delta M_{m+1})] = 0$$.

**Proof of the Pythagorean identity:**

Write $$M_n = M_0 + \sum_{j=1}^n \Delta M_j$$ and expand the square:

$$M_n^2 = M_0^2 + \sum_{j=1}^n (\Delta M_j)^2 + \sum_{j \neq k} (\Delta M_j)(\Delta M_k).$$

Taking expectations and using orthogonality (all cross terms vanish):

$$E[M_n^2] = E[M_0^2] + \sum_{j=1}^n E[(\Delta M_j)^2].$$

<div class="ex-lesson"><strong>Interpretation:</strong> This is the Pythagorean theorem in $L^2$. The variance of $M_n$ equals the sum of variances of all its increments — because the increments are mutually orthogonal (uncorrelated), there are no cross-term contributions. This is the exact analogue of $\lvert a_1 e_1 + \cdots + a_n e_n \rvert^2 = a_1^2 + \cdots + a_n^2$ for orthonormal vectors.</div>
</div>

#### The $$L^2$$ Hilbert space interpretation

The space $$L^2(\Omega, \mathcal{F}, P)$$ of square-integrable random variables is a Hilbert space under the inner product $$(X, Y) = E[XY]$$. The conditional expectation $$E[Y \mid \mathcal{F}_n]$$ is the orthogonal projection of $$Y$$ onto the closed subspace $$L^2(\Omega, \mathcal{F}_n, P)$$. This minimises the mean-squared error:

$$E[Y \mid \mathcal{F}_n] = \arg\min_{Z\, \mathcal{F}_n\text{-measurable}} E[(Y - Z)^2].$$

Proposition 1.5.1 says the increments $$\Delta M_1, \Delta M_2, \ldots$$ are mutually orthogonal in this Hilbert space — a discrete analogue of having orthogonal basis vectors.

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "Orthogonal martingale increments are independent."</div>
  <div class="mc-correct"><strong>Correct:</strong> Orthogonality ($E[\Delta M_{n+1} \cdot \Delta M_{m+1}] = 0$ for $m \neq n$) is weaker than independence. It says the increments are uncorrelated, not that they have no dependence structure. Independence implies orthogonality (for zero-mean variables), but the converse fails. The proof only uses the martingale property — no independence assumption is needed.</div>
</div>


---

### Part 2 — Section 1.6: Integrals with Respect to Random Walk

<div class="note-abstract">
Section 1.6 defines the discrete stochastic integral and establishes its three fundamental properties. The setting is a predictable integrand $J_n$ and a random walk $S_n$ with i.i.d. mean-zero increments. The integral $Z_n = \sum_{j=1}^n J_j X_j$ is the discrete prototype of the Itô integral $\int_0^t A_s\, dB_s$.
</div>

#### Setup

"Suppose that $$X_1, X_2, \ldots$$ are independent, identically distributed random variables with mean zero and variance $$\sigma^2$$."

The two main examples are:
- **Coin-tossing:** $$P\{X_j = 1\} = P\{X_j = -1\} = \tfrac{1}{2}$$, giving $$\sigma^2 = 1$$.
- **Normal increments:** $$X_j \sim N(0, \sigma^2)$$.

Let $$S_n = X_1 + \cdots + X_n$$ and let $$\{\mathcal{F}_n\}$$ be the filtration generated by $$X_1, \ldots, X_n$$.

"A sequence of random variables $$J_1, J_2, \ldots$$ is called **predictable** (with respect to $$\{\mathcal{F}_n\}$$) if for each $$n$$, $$J_n$$ is $$\mathcal{F}_{n-1}$$-measurable."

This is the non-anticipating condition from §1.2: the integrand $$J_n$$ is determined by observations strictly before time $$n$$.

The **discrete stochastic integral** is defined by:

$$Z_n = \sum_{j=1}^n J_j X_j = \sum_{j=1}^n J_j \,\Delta S_j.$$

#### Three fundamental properties

<div class="example-block" markdown="1">
<div class="ex-title">Three Properties of the Discrete Stochastic Integral <span class="ex-pill pill-prop">Proposition</span></div>

**Property 1 — Martingale property**

$$Z_n \text{ is a martingale with respect to } \{\mathcal{F}_n\}.$$

*Proof:* $$E[Z_{n+1} \mid \mathcal{F}_n] = E[Z_n + J_{n+1} X_{n+1} \mid \mathcal{F}_n] = Z_n + J_{n+1}\, E[X_{n+1} \mid \mathcal{F}_n] = Z_n + J_{n+1} \cdot 0 = Z_n.$$

Here: $$Z_n$$ is $$\mathcal{F}_n$$-measurable (Property 1 of §1.1); $$J_{n+1}$$ is $$\mathcal{F}_n$$-measurable and pulls out (Property 5); $$X_{n+1}$$ is independent of $$\mathcal{F}_n$$ with $$E[X_{n+1}] = 0$$ (Property 3).

---

**Property 2 — Linearity**

If $$J_n, K_n$$ are predictable sequences and $$a, b$$ constants, then $$aJ_n + bK_n$$ is predictable and:

$$\sum_{j=1}^n (aJ_j + bK_j) X_j = a \sum_{j=1}^n J_j X_j + b \sum_{j=1}^n K_j X_j.$$

*Proof:* Immediate from linearity of summation.

---

**Property 3 — Variance rule**

$$\mathrm{Var}[Z_n] = E[Z_n^2] = \sigma^2 \sum_{j=1}^n E[J_j^2].$$

*Proof:* Using orthogonality of martingale increments (§1.5), the cross terms $$E[J_j X_j \cdot J_k X_k]$$ vanish for $$j \neq k$$:

$$E[Z_n^2] = \sum_{j=1}^n E[J_j^2 X_j^2].$$

Since $$J_j$$ is $$\mathcal{F}_{j-1}$$-measurable and $$X_j$$ is independent of $$\mathcal{F}_{j-1}$$:

$$E[J_j^2 X_j^2] = E\bigl[E[J_j^2 X_j^2 \mid \mathcal{F}_{j-1}]\bigr] = E\bigl[J_j^2\, E[X_j^2 \mid \mathcal{F}_{j-1}]\bigr] = E[J_j^2]\, \sigma^2.$$

Summing over $$j$$ gives $$E[Z_n^2] = \sigma^2 \sum_{j=1}^n E[J_j^2]$$.

<div class="ex-lesson"><strong>Why the variance rule matters:</strong> It gives an explicit formula for the second moment of $Z_n$ purely in terms of the integrand $J_j$ and the variance $\sigma^2$ of the increments. This is the discrete analogue of the Itô isometry $E\!\left[\left(\int_0^t A_s\, dB_s\right)^2\right] = \int_0^t E[A_s^2]\, ds$, which is the cornerstone of the $L^2$ theory of stochastic integration.</div>
</div>

#### Comparison: discrete stochastic integral vs. Itô integral

| Feature | Discrete: $$Z_n = \sum J_j X_j$$ | Continuous: $$\int_0^t A_s\, dB_s$$ |
|---|---|---|
| **Integrand condition** | $$J_n$$ is $$\mathcal{F}_{n-1}$$-measurable (predictable) | $$A_s$$ is adapted, square-integrable |
| **Martingale property** | $$Z_n$$ is a martingale | $$\int_0^t A_s\, dB_s$$ is a martingale |
| **Variance rule** | $$E[Z_n^2] = \sigma^2 \sum E[J_j^2]$$ | $$E\!\left[\left(\int_0^t A_s\, dB_s\right)^2\right] = \int_0^t E[A_s^2]\, ds$$ |
| **Linearity** | ✓ direct from summation | ✓ by construction |

---

### Part 3 — Section 1.7: A Maximal Inequality

<div class="note-abstract">
Doob's maximal inequality bounds the probability that a submartingale's running maximum exceeds a level $a$. It is the discrete analogue of the continuous maximal inequality used throughout Chapter 4. The corollary for square integrable martingales follows immediately from the fact that $M_n^2$ is a submartingale.
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Theorem 1.7.1 — Doob's Maximal Inequality for Submartingales <span class="ex-pill pill-thm">Theorem</span></div>

"Suppose $$Y_n$$ is a nonneg submartingale with respect to $$\{\mathcal{F}_n\}$$, and $$\bar{Y}_n = \max\{Y_0, Y_1, \ldots, Y_n\}$$. Then for every $$a > 0$$,

$$P\{\bar{Y}_n \geq a\} \leq \frac{1}{a}\, E[Y_n].$$"

**Proof:**

Let $$T = \min\{k \leq n : Y_k \geq a\}$$ (with $$T = n+1$$ if no such $$k$$ exists). Then:

$$\{{\bar{Y}_n \geq a}\} = \bigsqcup_{k=0}^n A_k, \quad A_k = \{T = k\}.$$

Each $$A_k \in \mathcal{F}_k$$. Since $$Y_n$$ is a submartingale, $$E[Y_n \mid \mathcal{F}_k] \geq Y_k$$ for $$k \leq n$$, so:

$$E[Y_n \mathbf{1}_{A_k}] = E\bigl[E[Y_n \mid \mathcal{F}_k]\, \mathbf{1}_{A_k}\bigr] \geq E[Y_k\, \mathbf{1}_{A_k}] \geq a\, P(A_k).$$

Summing over $$k = 0, 1, \ldots, n$$:

$$E[Y_n] \geq E\!\left[Y_n\, \mathbf{1}_{\{\bar{Y}_n \geq a\}}\right] = \sum_{k=0}^n E[Y_n\, \mathbf{1}_{A_k}] \geq a\, P\{\bar{Y}_n \geq a\}.$$

Dividing by $$a$$ gives the result.
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Corollary 1.7.2 — Doob's $$L^2$$ Maximal Inequality <span class="ex-pill pill-thm">Corollary</span></div>

"If $$M_n$$ is a square integrable martingale with respect to $$\{\mathcal{F}_n\}$$ and $$\overline{M}_n = \max\{\lvert M_0 \rvert, \ldots, \lvert M_n \rvert\}$$, then for every $$a > 0$$,

$$P\{\overline{M}_n \geq a\} \leq \frac{E[M_n^2]}{a^2}.$$"

**Proof:** Exercise 1.15 shows that if $$M_n$$ is a martingale and $$\varphi$$ is a convex function, then $$\varphi(M_n)$$ is a submartingale. Taking $$\varphi(x) = x^2$$ gives that $$M_n^2$$ is a nonneg submartingale. Apply Theorem 1.7.1 to $$Y_n = M_n^2$$ with threshold $$a^2$$:

$$P\{\bar{Y}_n \geq a^2\} \leq \frac{E[M_n^2]}{a^2}.$$

Since $$\{\bar{Y}_n \geq a^2\} = \{\max_k M_k^2 \geq a^2\} = \{\overline{M}_n \geq a\}$$, the result follows.

<div class="ex-lesson"><strong>Why this matters:</strong> The $L^2$ maximal inequality is used throughout Chapter 3 to show that stochastic integrals defined on dyadic times extend continuously to all times (the Kolmogorov continuity argument). It is also used in Chapter 4 to prove the OST under the $L^2$ boundedness condition (Theorem 1.3.3). Controlling the running maximum by the second moment at the final time is the key tool.</div>
</div>




  </div>
</div>