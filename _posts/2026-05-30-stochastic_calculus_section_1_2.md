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

### Part 1 — How Sections 1.5–1.7 Fit Together

<div class="note-abstract">
Sections 1.5–1.7 form a tightly connected unit. Section 1.5 introduces the $L^2$ structure of martingales: their increments are orthogonal, giving a Pythagorean identity for the variance. Section 1.6 applies this structure to define and analyse the discrete stochastic integral — the sum $Z_n = \sum J_j X_j$ when $J_j$ is predictable. Section 1.7 uses $L^2$ to prove Doob's maximal inequality, which controls the running maximum of a martingale. All three sections are prerequisites for the continuous-time theory in Chapters 3 and 4.
</div>

#### How they connect

<div class="key-idea"><strong>§1.5 → §1.6:</strong> The orthogonality of martingale increments (§1.5) is exactly what justifies the variance rule $\mathrm{Var}[Z_n] = \sigma^2 \sum E[J_j^2]$ for the stochastic integral (§1.6). Without orthogonality, cross terms would not vanish.</div>

<div class="key-idea"><strong>§1.5 → §1.7:</strong> The fact that $M_n^2$ is a submartingale (§1.5, Exercise 1.15) is what allows Theorem 1.7.1 to be applied to $M_n^2$ to yield the $L^2$ maximal inequality in Corollary 1.7.2.</div>

<div class="key-idea"><strong>§1.6 → Chapter 3:</strong> The three properties of $Z_n$ — martingale, linearity, variance rule — are exactly the three properties that define the Itô integral $\int_0^t A_s\, dB_s$ in continuous time. Section 1.6 is the discrete blueprint.</div>

---

### Part 2 — Section 1.5: Square Integrable Martingales

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

### Part 3 — Section 1.6: Integrals with Respect to Random Walk

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

### Part 4 — Section 1.7: A Maximal Inequality

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

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "Doob's maximal inequality says $P\{\overline{M}_n \geq a\} \leq E[\lvert M_n \rvert]/a$ for any martingale."</div>
  <div class="mc-correct"><strong>Correct:</strong> Theorem 1.7.1 applies to nonneg <em>submartingales</em>, not arbitrary martingales. For a general martingale $M_n$, we apply it to the submartingale $Y_n = \lvert M_n \rvert$ (since $|\cdot|$ is convex) to get $P\{\overline{M}_n \geq a\} \leq E[\lvert M_n \rvert]/a$. The $L^2$ version in Corollary 1.7.2 applies $Y_n = M_n^2$ and replaces $a$ by $a^2$, giving the sharper $1/a^2$ bound under the stronger $L^2$ hypothesis.</div>
</div>

---

### Part 5 — Worked Example: Verifying the Variance Rule

<div class="example-block" markdown="1">
<div class="ex-title">Variance rule for coin-tossing random walk <span class="ex-pill pill-ex">Example</span></div>

**Setup:** $$X_1, X_2, \ldots$$ i.i.d. with $$P\{X_j = \pm 1\} = \tfrac{1}{2}$$, so $$\sigma^2 = 1$$. Let $$S_n = X_1 + \cdots + X_n$$.

**Integrand:** $$J_j = S_{j-1}$$ (the running sum just before step $$j$$, which is $$\mathcal{F}_{j-1}$$-measurable ✓).

**Integral:** $$Z_n = \sum_{j=1}^n S_{j-1} X_j.$$

**Apply the variance rule:**

$$E[Z_n^2] = \sigma^2 \sum_{j=1}^n E[J_j^2] = \sum_{j=1}^n E[S_{j-1}^2] = \sum_{j=1}^n (j-1) = \frac{n(n-1)}{2}.$$

Here we used $$E[S_{j-1}^2] = j - 1$$ (since $$\mathrm{Var}[S_{j-1}] = j-1$$ for zero-mean i.i.d. increments with $$\sigma^2 = 1$$).

**Direct check with Itô's formula analogy:** The integral $$Z_n = \sum S_{j-1} X_j$$ is the discrete analogue of $$\int_0^t B_s\, dB_s$$, which by Itô's formula equals $$\tfrac{1}{2}(B_t^2 - t)$$. The variance of $$\tfrac{1}{2}(B_t^2 - t)$$ at time $$t$$ is $$\tfrac{t^2}{2}$$, consistent with $$n(n-1)/2 \approx n^2/2$$ for large $$n$$.

<div class="ex-lesson"><strong>Key point:</strong> The variance rule allows computing $E[Z_n^2]$ without expanding the square and tracking all cross terms — orthogonality kills them all. The only computation needed is $E[J_j^2]$ for each $j$, which is a much simpler task.</div>
</div>

---

### Part 6 — The Three Properties as a Unified Blueprint

All three sections prepare the same three-property package that will recur throughout Chapters 3 and 4:

| Property | §1.6 Discrete version | Chapter 3 Continuous version |
|---|---|---|
| **Martingale** | $$Z_n = \sum J_j X_j$$ is a martingale | $$\int_0^t A_s\, dB_s$$ is a martingale |
| **Linearity** | $$\sum (aJ_j + bK_j) X_j = a Z_n^J + b Z_n^K$$ | $$\int (aA + bC)\, dB = a\int A\, dB + b \int C\, dB$$ |
| **Variance rule (Itô isometry)** | $$E[Z_n^2] = \sigma^2 \sum E[J_j^2]$$ | $$E\!\left[\left(\int_0^t A_s\, dB_s\right)^2\right] = \int_0^t E[A_s^2]\, ds$$ |

And §1.7's maximal inequality:

| Property | §1.7 Discrete version | Chapter 4 Continuous version |
|---|---|---|
| **Maximal inequality** | $$P\{\overline{M}_n \geq a\} \leq E[M_n^2]/a^2$$ | $$P\{\sup_{s \leq t} \lvert M_s \rvert \geq a\} \leq E[M_t^2]/a^2$$ |

---

### Term Glossary

<div class="glossary-entry">
<div class="gterm">Square integrable martingale <span class="gcat cat-defn">Definition</span></div>
A martingale $M_n$ with $E[M_n^2] < \infty$ for each $n$. Stronger than ordinary integrability ($E[\lvert M_n \rvert] < \infty$), weaker than uniform $L^2$ boundedness ($\sup_n E[M_n^2] \leq C$). The natural domain for the Pythagorean identity and the variance rule.
</div>

<div class="glossary-entry">
<div class="gterm">$L^2(\Omega, \mathcal{F}, P)$ <span class="gcat cat-defn">Definition</span></div>
The Hilbert space of square-integrable random variables on $(\Omega, \mathcal{F}, P)$, with inner product $(X,Y) = E[XY]$ and norm $\lVert X \rVert_2 = \sqrt{E[X^2]}$. The conditional expectation $E[Y \mid \mathcal{F}_n]$ is the orthogonal projection of $Y$ onto the closed subspace $L^2(\Omega, \mathcal{F}_n, P)$, minimising $E[(Y-Z)^2]$ over all $\mathcal{F}_n$-measurable $Z$.
</div>

<div class="glossary-entry">
<div class="gterm">Orthogonal random variables <span class="gcat cat-defn">Definition</span></div>
$X$ and $Y$ are orthogonal if $E[XY] = E[X]\,E[Y]$. For zero-mean variables this reduces to $E[XY] = 0$, i.e., $(X,Y) = 0$ in $L^2$. Independent zero-mean variables are orthogonal; the converse fails. Proposition 1.5.1 shows martingale increments $\Delta M_n$ are mutually orthogonal for $n \neq m$ using only the martingale property.
</div>

<div class="glossary-entry">
<div class="gterm">Pythagorean identity for martingales <span class="gcat cat-prop">Property</span></div>
$E[M_n^2] = E[M_0^2] + \sum_{j=1}^n E[(\Delta M_j)^2]$ for any square integrable martingale. Follows from orthogonality of increments: expanding $M_n^2 = (M_0 + \sum \Delta M_j)^2$ and taking expectations, all cross terms $E[\Delta M_j \cdot \Delta M_k]$ for $j \neq k$ vanish. This is the discrete analogue of the Itô isometry.
</div>

<div class="glossary-entry">
<div class="gterm">Predictable process <span class="gcat cat-defn">Definition</span></div>
A sequence $J_1, J_2, \ldots$ where $J_n$ is $\mathcal{F}_{n-1}$-measurable for every $n$. The value of $J_n$ is known strictly before time $n$. This is the allowable betting condition from §1.2, and the exact discrete analogue of the adapted condition for Itô integrands.
</div>

<div class="glossary-entry">
<div class="gterm">Discrete stochastic integral $Z_n = \sum_{j=1}^n J_j X_j$ <span class="gcat cat-defn">Definition</span></div>
The sum of a predictable integrand $J_j$ against the i.i.d. increments $X_j$ of a random walk. Satisfies three properties: (1) martingale; (2) linearity; (3) variance rule $E[Z_n^2] = \sigma^2 \sum E[J_j^2]$. The discrete prototype of the Itô integral $\int_0^t A_s\, dB_s$ in Chapter 3.
</div>

<div class="glossary-entry">
<div class="gterm">Variance rule (Itô isometry, discrete form) <span class="gcat cat-prop">Property</span></div>
$\mathrm{Var}[Z_n] = E[Z_n^2] = \sigma^2 \sum_{j=1}^n E[J_j^2]$. Proved by using: (a) orthogonality of martingale increments to kill cross terms; (b) the pull-out property to separate $J_j^2$ from $X_j^2$; (c) independence of $X_j$ from $\mathcal{F}_{j-1}$ to replace $E[X_j^2 \mid \mathcal{F}_{j-1}]$ by $\sigma^2$.
</div>

<div class="glossary-entry">
<div class="gterm">Doob's maximal inequality <span class="gcat cat-thm">Theorem</span></div>
For a nonneg submartingale $Y_n$ with running maximum $\bar{Y}_n = \max_{k \leq n} Y_k$:

$$P\{\bar{Y}_n \geq a\} \leq \frac{E[Y_n]}{a}.$$

Proved by partitioning $\{\bar{Y}_n \geq a\}$ into the disjoint events $A_k = \{T = k\}$ (first time $Y$ hits $a$), and using the submartingale inequality $E[Y_n \mathbf{1}_{A_k}] \geq a\,P(A_k)$ for each $k$.
</div>

<div class="glossary-entry">
<div class="gterm">Doob's $L^2$ maximal inequality <span class="gcat cat-thm">Theorem</span></div>
For a square integrable martingale $M_n$ with $\overline{M}_n = \max_{k \leq n} \lvert M_k \rvert$:

$$P\{\overline{M}_n \geq a\} \leq \frac{E[M_n^2]}{a^2}.$$

Follows from Theorem 1.7.1 applied to the submartingale $Y_n = M_n^2$ (convexity of $x^2$ makes $M_n^2$ a submartingale). Controls the running maximum by the terminal second moment — used in the Kolmogorov continuity argument and in the proof of OST III.
</div>

---

### Study-Note Summary

- **§1.5 — Square integrable martingales:** $$E[M_n^2] < \infty$$ for each $$n$$. The key result is Proposition 1.5.1: martingale increments $$\Delta M_j$$ are mutually orthogonal in $$L^2$$ ($$E[\Delta M_{n+1}\cdot\Delta M_{m+1}]=0$$ for $$m \neq n$$), giving the Pythagorean identity $$E[M_n^2] = E[M_0^2] + \sum_j E[(\Delta M_j)^2]$$. Proof uses only the martingale property — no independence required.
- **$$L^2$$ Hilbert space structure:** $$L^2(\Omega,\mathcal{F},P)$$ is a Hilbert space with inner product $$(X,Y)=E[XY]$$. Conditional expectation $$E[Y\mid\mathcal{F}_n]$$ is the orthogonal projection of $$Y$$ onto the subspace $$L^2(\Omega,\mathcal{F}_n,P)$$. Martingale increments are orthogonal vectors in this space.
- **§1.6 — Discrete stochastic integral:** For a predictable sequence $$J_n$$ ($$\mathcal{F}_{n-1}$$-measurable) and i.i.d. mean-zero variance-$$\sigma^2$$ increments $$X_j$$, the integral $$Z_n=\sum_{j=1}^n J_j X_j$$ satisfies three properties: **(1)** martingale; **(2)** linearity; **(3)** variance rule $$E[Z_n^2]=\sigma^2\sum_j E[J_j^2]$$. These are exactly the properties the Itô integral inherits in Chapter 3.
- **§1.7 — Doob's maximal inequality:** For any nonneg submartingale $$Y_n$$: $$P\{\max_{k\leq n} Y_k \geq a\} \leq E[Y_n]/a$$. Corollary: for a square integrable martingale $$M_n$$: $$P\{\max_{k\leq n}\lvert M_k\rvert \geq a\} \leq E[M_n^2]/a^2$$. The corollary follows because $$M_n^2$$ is a submartingale (Jensen's inequality applied to the convex function $$x^2$$).
- **Proof strategy for variance rule:** (a) expand $$E[Z_n^2]$$; (b) orthogonality kills all cross terms $$j \neq k$$; (c) for each $$j$$, pull $$J_j^2$$ out of the conditional expectation and use independence of $$X_j$$ from $$\mathcal{F}_{j-1}$$ to get $$E[J_j^2 X_j^2] = \sigma^2 E[J_j^2]$$.
- **Key forward connections:** The three §1.6 properties are the exact discrete blueprint for the Itô integral (Chapter 3). The §1.7 maximal inequality is used in the Kolmogorov continuity theorem and in the proof of OST III (Theorem 1.3.3). Both appear throughout Chapters 3–4.

<div class="ref-tags">
<span class="ref-tag">Square integrable martingale</span>
<span class="ref-tag">Orthogonal increments</span>
<span class="ref-tag">Pythagorean identity</span>
<span class="ref-tag">Hilbert space $L^2$</span>
<span class="ref-tag">Predictable process</span>
<span class="ref-tag">Discrete stochastic integral</span>
<span class="ref-tag">Variance rule</span>
<span class="ref-tag">Itô isometry</span>
<span class="ref-tag">Doob's maximal inequality</span>
<span class="ref-tag">Submartingale</span>
</div>

  </div>
</div>
