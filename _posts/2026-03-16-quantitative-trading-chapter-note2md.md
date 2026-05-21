---
layout: distill
title: "Stochastic Calculus — Study Notes"
description: Study notes for Lawler Stochastic Calculus (Chapter 1).
tags: Stochastic Calculus
giscus_comments: true
date: 2026-03-24
featured: true
thumbnail: https://magica.com/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FIBw5a8ByyzY%2Fmaxresdefault.jpg&w=3840&q=75

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Chapter 2 — Fishing for Ideas
  - name: Chapter 3 — Backtesting
  - name: Chapter 5 — Execution Systems
  - name: Chapter 6 — Money and Risk Management
  - name: Chapter 7 — Special Topics

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
  .pill-code { background: #e2f0fb; color: #0c4a7c; }
  .pill-tip  { background: #fff3cd; color: #856404; }
  .pill-puzzle { background: #fff3cd; color: #856404; }
  .example-block .ex-lesson { margin-top: 0.5rem; font-size: 0.85rem; color: #555; border-top: 1px solid #ddd; padding-top: 0.4rem; }
  .key-idea { padding: 0.3rem 0; border-bottom: 1px dotted #ddd; margin-bottom: 0.4rem; }
  .key-idea:last-child { border-bottom: none; }
  .glossary-entry { border-bottom: 1px solid #eee; padding: 0.7rem 0; }
  .glossary-entry:last-child { border-bottom: none; }
  .glossary-entry .gterm { font-weight: 600; font-size: 0.95rem; margin-bottom: 0.25rem; }
  .glossary-entry .gcat { display: inline-block; font-size: 0.7rem; font-weight: 600; padding: 1px 7px; border-radius: 20px; margin-left: 6px; vertical-align: middle; }
  .cat-data     { background: #dbeafe; color: #1e3a8a; }
  .cat-risk     { background: #fce8e6; color: #7f1d1d; }
  .cat-perf     { background: #fef3c7; color: #78350f; }
  .cat-capital  { background: #d1fae5; color: #064e3b; }
  .cat-inst     { background: #ede8fc; color: #3c2a8a; }
  .cat-bias     { background: #dcfce7; color: #14532d; }
  .cat-cost     { background: #fce7f3; color: #831843; }
  .cat-system   { background: #d1fae5; color: #064e3b; }
  .cat-market   { background: #dbeafe; color: #1e3a8a; }
  .cat-method   { background: #ede8fc; color: #3c2a8a; }
  .cat-platform { background: #d1fae5; color: #064e3b; }
  .cat-kelly    { background: #d1fae5; color: #064e3b; }
  .cat-psych    { background: #ede8fc; color: #3c2a8a; }
  .cat-strategy { background: #d1fae5; color: #064e3b; }
  .cat-stats    { background: #dbeafe; color: #1e3a8a; }
  .cat-model    { background: #fef3c7; color: #78350f; }
  .cat-exit     { background: #fce7f3; color: #831843; }
  .cat-seasonal { background: #ede8fc; color: #3c2a8a; }
  .cat-hft      { background: #dcfce7; color: #14532d; }
  .quote-block { background: #f9fafb; border-radius: 6px; padding: 0.75rem 1rem; margin-top: 1rem; font-style: italic; color: #444; font-size: 0.9rem; }
  .result-box { background: #f0fff4; border: 1px solid #9ae6b4; border-radius: 6px; padding: 0.6rem 1rem; margin: 0.5rem 0; font-size: 0.88rem; }
  .result-box strong { color: #276749; }
  .warning-box { background: #fff8e1; border: 1px solid #ffe082; border-radius: 6px; padding: 0.75rem 1rem; margin: 0.75rem 0; font-size: 0.88rem; color: #5d4037; }
  .warning-box strong { color: #e65100; }
  .ref-tags { margin-top: 1rem; }
  .ref-tag { display: inline-block; font-size: 0.72rem; padding: 2px 8px; border-radius: 20px; border: 1px solid #ccc; color: #666; margin: 2px 3px 2px 0; }
  .checklist { list-style: none; padding: 0; margin: 0.5rem 0; }
  .checklist li { padding: 0.3rem 0; font-size: 0.9rem; color: #333; border-bottom: 1px dotted #eee; display: flex; align-items: flex-start; gap: 0.5rem; }
  .checklist li:last-child { border-bottom: none; }
  .checklist li::before { content: "→"; color: #5b7de8; flex-shrink: 0; }
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


## Section 1.1 — Conditional Expectation

<div class="chapter-block">
  <button class="chapter-toggle" onclick="toggleChapter('s11')">
    <div class="chapter-toggle-left">
      <span class="chapter-badge">§ 1.1</span>
      <div>
        <div class="chapter-title">Section 1.1 — Conditional Expectation</div>
        <div class="chapter-subtitle">The foundational tool underlying every concept in this book — probability-space setup, the definition and properties of $E[Y \mid \mathcal{F}_n]$</div>
      </div>
    </div>
    <span class="chapter-arrow" id="s11-arrow">▼</span>
  </button>
  <div class="chapter-body" id="s11-body" markdown="1">



### Notation at a Glance

| Symbol | Meaning |
|---|---|
| $\Omega$ | Sample space — the set of all possible outcomes |
| $\mathcal{F}$ | $\sigma$-algebra — the collection of all observable events |
| $P$ | Probability measure — assigns numbers in $[0,1]$ to events in $\mathcal{F}$ |
| $(\Omega, \mathcal{F}, P)$ | Probability space — the full mathematical arena |
| $A \in \mathcal{F}$ | A is a measurable event (we can assign it a probability) |
| $\Omega \setminus A$ | Complement of A — all outcomes not in A |
| $\mathcal{F}_n$ | $\sigma$-algebra generated by $X_1,\ldots,X_n$ — information at time n |
| $\mathcal{F}_m \subseteq \mathcal{F}_n$ | All events knowable at time m are also knowable at time n |
| $E[Y]$ | Unconditional expectation — best guess for Y with no information |
| $E[Y \mid \mathcal{F}_n]$ | Conditional expectation — best guess for Y given information $\mathcal{F}_n$ |
| $\mathbf{1}_A$ | Function equal to 1 on event A, 0 elsewhere |
| i.i.d. | Independent and identically distributed |
| $\mu \ll P$ | $\mu$ absolutely continuous w.r.t. $P$ — every P-null set is also a $\mu$-null set |
| $S_n$ | Partial sum $X_1 + X_2 + \cdots + X_n$ |



---

### Part 1 — The Core Intuition

<div class="note-abstract">
Conditional expectation is the central object of stochastic calculus. At its core it answers one question: <em>given that we have observed some (but not all) information, what is our best guess for a random variable $Y$?</em> The answer is not a single number but another random variable — one that changes as our information changes.
</div>

#### Core ideas

<div class="key-idea"><strong>$E[Y]$ is the best guess for $Y$ given no information at all.</strong> The unconditional expectation is the baseline: if you know nothing about the outcome of an experiment, your single best guess (in the mean-squared-error sense) is $E[Y]$.</div>

<div class="key-idea"><strong>$E[Y \mid \mathcal{F}_n]$ is the best guess for Y given the information $\mathcal{F}_n$.</strong> As data arrives one variable at a time — $X_1, X_2, \ldots, X_n$ — we collect more information. The conditional expectation updates our best guess for Y using whatever is currently known.</div>

<div class="key-idea"><strong>$E[Y \mid \mathcal{F}_n]$ is itself a random variable, not a fixed number.</strong> Because it depends on the observed values of $X_1, \ldots, X_n$ — which are random — it is a function of those observations, hence random.</div>

<div class="key-idea"><strong>The formal definition bypasses explicit computation via one key property.</strong> $E[Y \mid \mathcal{F}_n]$ is defined as the unique $\mathcal{F}_n$-measurable random variable satisfying $E[E[Y \mid \mathcal{F}_n] \cdot \mathbf{1}_A] = E[Y \cdot \mathbf{1}_A]$ for all $\mathcal{F}_n$-measurable events A.</div>

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label">Common Misconception</span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "$E[Y \mid \mathcal{F}_n]$ is just a number, like $E[Y]$ but computed with less data."</div>
  <div class="mc-correct"><strong>Correct:</strong> $E[Y \mid \mathcal{F}_n]$ is a <em>random variable</em>. Its value changes depending on which values $X_1, \ldots, X_n$ take. If you observe different data, you get a different conditional expectation. $E[Y]$ is the special case where zero data is observed — a single fixed number. $E[Y \mid \mathcal{F}_n]$ is a whole function of the observations.</div>
</div>

---

### Part 2 — The Probability Space

<div class="note-abstract">
Before defining conditional expectation rigorously, we need the underlying mathematical arena: a probability space $(\Omega, \mathcal{F}, P)$. Everything — random variables, events, filtrations — lives inside this structure.
</div>

"We assume that the random variables Y, $X_1, X_2, \ldots$ are defined on a probability space $(\Omega, \mathcal{F}, P)$. Here $\mathcal{F}$ is a $\sigma$-algebra or $\sigma$-field of subsets of $\Omega$, that is, a collection of subsets satisfying:<br>

i. $\emptyset \in \mathcal{F}$<br>
ii. $A \in \mathcal{F}$ implies $\Omega \setminus A \in \mathcal{F}$ <br>
iii. $A_1, A_2, \ldots \in \mathcal{F}$ implies $\bigcup_{n=1}^{\infty} A_n \in \mathcal{F}$."<br>

This defines the three $\sigma$-algebra axioms. (i) The empty set — the impossible event — must be an event. (ii) If A is observable, so is its complement: "A did not happen" must also be observable. (iii) Countable unions of events are events: "at least one of $A_1, A_2, \ldots$ happened" is observable. These three rules make $\mathcal{F}$ a self-consistent collection of questions we can ask about the experiment.

<div class="example-block" markdown="1">
<div class="ex-title">Minimal example: two fair coin flips </div>

**Sample space:** $\Omega = \{HH, HT, TH, TT\}$

**The full $\sigma$-algebra** $\mathcal{F} = 2^\Omega$ contains all 16 subsets. This always satisfies all three axioms and encodes complete information.

**A smaller valid $\sigma$-algebra** encoding only the first flip:

$$\mathcal{F}_1 = \{ \emptyset, \quad \{HH, HT\}, \quad \{TH, TT\}, \quad \Omega \}$$

- $\emptyset \in \mathcal{F}_1$ ✓ &emsp;(axiom i)
- $\{HH,HT\}^c = \{TH,TT\} \in \mathcal{F}_1$ ✓ &emsp;(axiom ii)
- Any union of these four sets stays in $\mathcal{F}_1$ ✓ &emsp;(axiom iii)

$\mathcal{F}_1$ lets us distinguish "first flip = H" from "first flip = T" — nothing more.

<div class="ex-lesson"><strong>Key point:</strong> A $\sigma$-algebra is a mathematical encoding of a state of knowledge. Larger $\sigma$-algebra = more information. $\mathcal{F}_1 \subseteq 2^\Omega$ reflects that knowing one flip is strictly less information than knowing both.</div>
</div>

---

### Part 3 — The Filtration

<div class="note-abstract">
A filtration is a growing sequence of σ-algebras modelling information accumulating over time. At time n, F_n records everything observed up to time n — and once something is known it is never forgotten.
</div>

"Let $X_1, X_2, \ldots$ be random variables which we think of as a time series with the data arriving one at a time. At time $n$ we have viewed the values $X_1, \ldots, X_n$. … We will write $\mathcal{F}_n$ for 'the information contained in $X_1, \ldots, X_n$."<br>

$\mathcal{F}_n$ is not a number or a random variable — it is a $\sigma$-algebra: a collection of events. "Information in $X_1,\ldots,X_n$" means all questions of the form "did the observations satisfy some condition?" that can be answered once $X_1,\ldots,X_n$ are known.<br>

"The information $\mathcal{F}_n$ is the smallest sub $\sigma$-algebra $G$ of $\mathcal{F}$ such that $X_1, \ldots, X_n$ are $G$-measurable. The latter statement means that for all $t \in \mathbb{R}$, the event $\{X_j \leq t\} \in \mathcal{F}_n$."<br>

"$X_j$ is $\mathcal{F}_n$-measurable" means: for every threshold $t$, the set of outcomes where $X_j \leq t$ is an event in $\mathcal{F}_n$. Knowing $X_1,\ldots,X_n$ is enough to determine $X_j$. The word "smallest" is important — we take only events genuinely required to describe $X_1,\ldots,X_n$, not any extras.

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label">Common Misconception</span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "$X$ is $\mathcal{F}_n$-measurable just means $X$ is one of the variables $X_1,\ldots,X_n$."</div>
  <div class="mc-correct"><strong>Correct:</strong> Any function of $X_1,\ldots,X_n$ is also $\mathcal{F}_n$-measurable — e.g., $X_1 + X_2$, $\max(X_1,\ldots,X_n)$, or $S_n^2$. The condition is that X's value is fully determined once $X_1,\ldots,X_n$ are known, not that X appears explicitly in the list.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Measurable random variable on a finite space</div>

Let $\Omega=\{\omega_1,\omega_2,\omega_3\}$ and define the $\sigma$-algebra
$\mathcal{F}=\{\emptyset, \Omega, \{\omega_1,\omega_2\}, \{\omega_3\}\}$.


<!-- $$\mathcal{F}_1 = \{ \emptyset, \quad \{HH, HT\}, \quad \{TH, TT\}, \quad \Omega \}$$ -->


Define the random variable
$X(\omega_1)=0,\; X(\omega_2)=0,\; X(\omega_3)=1$.

To check measurability, verify that
$\{X\le t\}\in\mathcal{F}\quad \forall t\in\mathbb{R}$.

For example:

$\{X\le 0\}=\{\omega_1,\omega_2\}\in\mathcal{F}$,

$\{X\le 0.5\}=\{\omega_1,\omega_2\}\in\mathcal{F}$,

$\{X\le 2\}=\Omega\in\mathcal{F}$.

Hence $X$ is $\mathcal{F}$-measurable.

<div class="ex-lesson">
<strong>Key point:</strong> A random variable is measurable if the information structure $\mathcal{F}$ can distinguish exactly the events needed to determine its value. Here, $\mathcal{F}$ separates $\omega_3$ from $\{\omega_1,\omega_2\}$, which is exactly what $X$ depends on.
</div>
</div>


<div class="example-block" markdown="1">
<div class="ex-title">Example of a non-measurable function</div>

Let $\Omega=\{\omega_1,\omega_2,\omega_3\}$ and consider the same $\sigma$-algebra
$\mathcal{F}=\{\emptyset,\Omega,\{\omega_1,\omega_2\},\{\omega_3\}\}$.

Define the function
$Y(\omega_1)=0,\; Y(\omega_2)=1,\; Y(\omega_3)=0$.

Now check measurability.

Consider the event
$\{Y\le 0\}=\{\omega_1,\omega_3\}$.

But $\{\omega_1,\omega_3\}\notin\mathcal{F}$.

Hence $Y$ is not $\mathcal{F}$-measurable.

<div class="ex-lesson">
<strong>Key point:</strong> The $\sigma$-algebra $\mathcal{F}$ cannot distinguish $\omega_1$ from $\omega_2$ in a way consistent with $Y$. Since $Y$ separates these outcomes differently while $\mathcal{F}$ does not, the function is “too fine” for the available information structure.
</div>
</div>

---

### Part 4 — Motivating the Definition (Density Case)

<div class="note-abstract">
Before giving the abstract definition, Lawler derives it in the familiar setting of joint densities. This motivates why the abstract definition takes the form it does.
</div>

"Suppose that (X, Y) have a joint density f(x, y), 0 &lt; x, y &lt; ∞, with marginal densities f(x) = ∫ f(x,y)dy, g(y) = ∫ f(x,y)dx. The conditional density f(y|x) is defined by f(y|x) = f(x,y)/f(x)."
<div class="quote-explain">f(x,y) is the joint probability density near (x,y). f(x) is the marginal density of X — the probability near x regardless of Y, obtained by integrating out all y-values. f(y|x) is the relative weight on each y-value given X = x. Division by f(x) normalises so that f(y|x) integrates to 1 over y.</div>

This gives the familiar undergraduate formula:

$$E[Y \mid X = x] = \int_{-\infty}^{\infty} y\, f(y \mid x)\, dy = \frac{\int_{-\infty}^{\infty} y\, f(x,y)\, dy}{f(x)}$$

"Note that E[Y | X] is a random variable which is determined by the value of the random variable X."
<div class="quote-explain">E[Y | X = x] for a fixed x is a number. But E[Y | X] — without fixing x — is a function of X. Since X is random, this function is itself random. This is the key conceptual leap the formal definition must capture.</div>

**The tower property emerges naturally:**

$$E\bigl[E[Y \mid X]\bigr] = \int_{-\infty}^{\infty} E[Y \mid X = x]\, f(x)\, dx = \iint y\, f(x,y)\, dy\, dx = E[Y]$$

Averaging the conditional best-guess over all possible observations recovers the unconditional expectation. This is the **tower property**, generalised by the abstract definition below.

---

### Part 5 — The Formal Definition

<div class="example-block">
<div class="ex-title">Definition — Conditional Expectation E[Y | F_n] <span class="ex-pill pill-defn">Definition</span></div>

"The conditional expectation $E[Y \mid \mathcal{F}_n]$ is the unique random variable satisfying the following. (i) $E[Y \mid \mathcal{F}_n]$ is $\mathcal{F}_n$-measurable. (ii) For every $\mathcal{F}_n$-measurable event A, $E[E[Y \mid \mathcal{F}_n] \cdot \mathbf{1}_A] = E[Y \cdot \mathbf{1}_A]$."
<div class="quote-explain">Condition (i): the output is computable from $X_1,\ldots,X_n$ alone — it cannot use future information. Condition (ii): on every slice of $\Omega$ that can be identified from current information (any $A \in \\mathcal{F}_n$), the average of $E[Y|\\mathcal{F}_n]$ over that slice equals the average of Y over the same slice. These two conditions uniquely determine $E[Y|\\mathcal{F}_n]$ without requiring a closed-form formula.</div>

**What is $\mathbf{1}_A$?**

$$\mathbf{1}_A(\omega) = \begin{cases} 1 & \text{if } \omega \in A \\ 0 & \text{if } \omega \notin A \end{cases}$$

So $E[Z \cdot \mathbf{1}_A]$ = probability-weighted average of Z over outcomes where A occurs = $\int_A Z \, dP$.

**Why not give an explicit formula?** In general probability spaces (uncountable Ω, continuous distributions), no single formula works universally. The two-condition characterisation is both sufficient and rigorous. Existence follows from the Radon-Nikodym theorem; uniqueness from: if Z₁ and Z₂ both satisfy the conditions then E[(Z₁ − Z₂)²] = 0, so Z₁ = Z₂ almost surely.
</div>

<!-- CHANGE 3 — Misconception block for the definition -->
<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label">Common Misconception</span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "Condition (ii) $E[E[Y|\\mathcal{F}_n]\\cdot\\mathbf{1}_A] = E[Y\\cdot\\mathbf{1}_A]$ is just saying $E[Y|\\mathcal{F}_n] = Y$."</div>
  <div class="mc-correct"><strong>Correct:</strong> It says they agree <em>on average over every observable event A</em> — not pointwise. $E[Y|\\mathcal{F}_n]$ is a smoothed version of Y: it preserves the same probability mass on every $\\mathcal{F}_n$-identifiable slice, but replaces Y's within-slice variation with a single average value. The pointwise equality $E[Y|\\mathcal{F}_n](\\omega) = Y(\\omega)$ only holds when Y is itself $\\mathcal{F}_n$-measurable (Property 1).</div>
</div>

---

### Part 6 — Properties of Conditional Expectation

<div class="example-block">
<div class="ex-title">Proposition 1.1.1 — Five key properties <span class="ex-pill pill-prop">Proposition</span></div>

"Proposition 1.1.1. Suppose X₁, X₂, … is a sequence of random variables and F_n denotes the information at time n. The conditional expectation E[Y | F_n] satisfies the following properties."
<div class="quote-explain">All five properties are consequences of the two defining conditions — not additional assumptions. Lawler proves linearity and the constants rule explicitly in the text; the others follow by analogous arguments using the definition.</div>

---

**Property 1 — If Y is already known, conditioning changes nothing**

$$\text{If } Y \text{ is } \mathcal{F}_n\text{-measurable}, \quad E[Y \mid \mathcal{F}_n] = Y.$$

*Why:* Y is determined by $X_1,\ldots,X_n$. No uncertainty remains — the best guess is the value itself.

---

**Property 2 — Tower property (law of iterated expectations)**

$$m < n \implies E\bigl[\,E[Y \mid \mathcal{F}_n]\;\big|\;\mathcal{F}_m\bigr] = E[Y \mid \mathcal{F}_m].$$

*Plain English:* Compute the best guess for Y using information up to time n, then downgrade it to only use information up to time m < n. The result is identical to computing the best guess with time-m information directly. The outer (coarser) conditioning always governs the answer.

Special case m = 0: **$E[E[Y \mid \mathcal{F}_n]] = E[Y]$**.

---

**Property 3 — Independence means conditioning is useless**

$$X_1,\dots,X_n \perp Y \implies E[Y \mid \mathcal{F}_n] = E[Y].$$

*Why:* If the observations carry zero information about Y, the best guess remains the unconditional mean.

---

**Property 4 — Linearity**

$$E[aY + bZ \mid \mathcal{F}_n] = a\,E[Y \mid \mathcal{F}_n] + b\,E[Z \mid \mathcal{F}_n].$$

*Why:* Conditional expectation is an integral, and integrals are linear.

---

**Property 5 — Known factors pull out (constants rule)**

$$Z \text{ is } \mathcal{F}_n\text{-measurable} \implies E[YZ \mid \mathcal{F}_n] = Z\cdot E[Y \mid \mathcal{F}_n].$$

*Why:* Z is already determined by current information — it plays the role of a known constant. Only Y carries residual randomness to average over. *Example:* $E[X_1 \cdot Y | \\mathcal{F}_1] = X_1 \cdot E[Y | \\mathcal{F}_1]$.
</div>

<!-- CHANGE 3 — Misconception block for the tower property -->
<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label">Common Misconception — Tower Property</span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "$E[E[Y|\\mathcal{F}_n]|\\mathcal{F}_m] = E[Y|\\mathcal{F}_n]$ — the inner conditioning dominates because it has more information."</div>
  <div class="mc-correct"><strong>Correct:</strong> The <em>outer</em> conditioning dominates: the result is $E[Y|\\mathcal{F}_m]$. When you condition on less information ($\\mathcal{F}_m \\subseteq \\mathcal{F}_n$), you lose the fine detail provided by $\\mathcal{F}_n$. The coarser $\\sigma$-algebra always wins. Think of it as: the final answer can only use what the outermost conditioning permits.</div>
</div>

---

### Part 7 — Worked Examples

<div class="example-block">
<div class="ex-title">Example 1.1.1 — $E[S_n | \\mathcal{F}_m]$ for independent increments <span class="ex-pill pill-ex">Example</span></div>

**Setup:** $X_1, X_2, \\ldots$ independent with $E[X_j] = \\mu$. Let $S_n = X_1 + \\cdots + X_n$, $\\mathcal{F}_m = \\sigma(X_1,\\ldots,X_m)$, $m < n$.

<!-- CHANGE 2 — Proof-step component -->
<div class="proof-steps">
<div class="ps-title">Step-by-step derivation</div>

<div class="proof-step">
  <div class="ps-num">1</div>
  <div class="ps-body">
    Split $S_n$ at time m using linearity of conditional expectation:
    <span class="ps-eq">$E[S_n | \\mathcal{F}_m] = E[S_m | \\mathcal{F}_m] + E[S_n - S_m | \\mathcal{F}_m]$</span>
  </div>
  <div class="ps-why">Property 4 — Linearity</div>
</div>

<div class="proof-step">
  <div class="ps-num">2</div>
  <div class="ps-body">
    First term: $S_m = X_1+\\cdots+X_m$ is fully determined by $X_1,\\ldots,X_m$, so it is $\\mathcal{F}_m$-measurable:
    <span class="ps-eq">$E[S_m | \\mathcal{F}_m] = S_m$</span>
  </div>
  <div class="ps-why">Property 1 — Known Y</div>
</div>

<div class="proof-step">
  <div class="ps-num">3</div>
  <div class="ps-body">
    Second term: $S_n - S_m = X_{m+1}+\\cdots+X_n$ depends only on future variables, independent of $\\mathcal{F}_m$:
    <span class="ps-eq">$E[S_n - S_m | \\mathcal{F}_m] = E[S_n - S_m] = (n-m)\\mu$</span>
  </div>
  <div class="ps-why">Property 3 — Independence</div>
</div>

<div class="proof-step">
  <div class="ps-num">4</div>
  <div class="ps-body">
    Combine Steps 2 and 3:
    <span class="ps-eq">$E[S_n | \\mathcal{F}_m] = S_m + (n-m)\\mu$</span>
    Given observations up to time m, the best guess for $S_n$ is the current sum plus $(n-m)$ expected future increments.
  </div>
  <div class="ps-why">Result</div>
</div>

</div>

<div class="ex-lesson"><strong>Why this matters:</strong> When $\\mu = 0$ the result becomes $E[S_n | \\mathcal{F}_m] = S_m$ — the current sum is the best guess for all future sums. This is exactly the martingale property defined in §1.2.</div>
</div>

<div class="example-block">
<div class="ex-title">Example 1.1.2 — $E[S_n^2 | \\mathcal{F}_m]$ for zero-mean increments <span class="ex-pill pill-ex">Example</span></div>

**Setup:** $\\mu = 0$, $E[X_j^2] = \\sigma^2 < \\infty$. Same $S_n$, $\\mathcal{F}_m$ as above.

<div class="proof-steps">
<div class="ps-title">Step-by-step derivation</div>

<div class="proof-step">
  <div class="ps-num">1</div>
  <div class="ps-body">
    Write $S_n = S_m + (S_n - S_m)$ and expand the square:
    <span class="ps-eq">$E[S_n^2 | \\mathcal{F}_m] = E[S_m^2 | \\mathcal{F}_m] + 2 E[S_m(S_n-S_m) | \\mathcal{F}_m] + E[(S_n-S_m)^2 | \\mathcal{F}_m]$</span>
  </div>
  <div class="ps-why">Property 4 — Linearity</div>
</div>

<div class="proof-step">
  <div class="ps-num">2</div>
  <div class="ps-body">
    Term 1: $S_m^2$ is $\\mathcal{F}_m$-measurable:
    <span class="ps-eq">$E[S_m^2 | \\mathcal{F}_m] = S_m^2$</span>
  </div>
  <div class="ps-why">Property 1</div>
</div>

<div class="proof-step">
  <div class="ps-num">3</div>
  <div class="ps-body">
    Term 2: $S_m$ pulls out ($\\mathcal{F}_m$-measurable); $S_n-S_m$ is independent of $\\mathcal{F}_m$ with mean 0:
    <span class="ps-eq">$2 E[S_m(S_n-S_m) | \\mathcal{F}_m] = 2 S_m \\cdot E[S_n-S_m] = 2 S_m \\cdot 0 = 0$</span>
  </div>
  <div class="ps-why">Properties 5 + 3</div>
</div>

<div class="proof-step">
  <div class="ps-num">4</div>
  <div class="ps-body">
    Term 3: $(S_n-S_m)^2$ is independent of $\\mathcal{F}_m$; its expectation is the variance of $(n-m)$ increments:
    <span class="ps-eq">$E[(S_n-S_m)^2 | \\mathcal{F}_m] = \\text{Var}(S_n-S_m) = (n-m)\\sigma^2$</span>
  </div>
  <div class="ps-why">Property 3</div>
</div>

<div class="proof-step">
  <div class="ps-num">5</div>
  <div class="ps-body">
    Combine Terms 1, 2, 3:
    <span class="ps-eq">$E[S_n^2 | \\mathcal{F}_m] = S_m^2 + (n-m)\\sigma^2$</span>
  </div>
  <div class="ps-why">Result</div>
</div>

</div>

<div class="ex-lesson"><strong>Why this matters:</strong> The process $M_n = S_n^2 - n\\sigma^2$ is a martingale — this computation is the exact verification. It also shows that $S_n^2$ grows on average by $\\sigma^2$ per step, connecting to the quadratic variation of random walk.</div>
</div>

<div class="example-block">
<div class="ex-title">Example 1.1.3 — $E[X_1 | S_n]$: conditioning on a coarser statistic <span class="ex-pill pill-ex">Example</span></div>

**Setup:** $X_1,\\ldots,X_n$ i.i.d. We observe only $S_n = X_1+\\cdots+X_n$. Goal: compute $E[X_1 | S_n]$.

<div class="proof-steps">
<div class="ps-title">Step-by-step derivation</div>

<div class="proof-step">
  <div class="ps-num">1</div>
  <div class="ps-body">
    Since $X_1,\\ldots,X_n$ are i.i.d., conditioning on $S_n$ treats every index symmetrically — no single component is favoured:
    <span class="ps-eq">$E[X_1 | S_n] = E[X_2 | S_n] = \\cdots = E[X_n | S_n]$</span>
  </div>
  <div class="ps-why">Symmetry of i.i.d.</div>
</div>

<div class="proof-step">
  <div class="ps-num">2</div>
  <div class="ps-body">
    Sum both sides over $j = 1,\\ldots,n$ and apply linearity. Since $S_n$ is $\\sigma(S_n)$-measurable (already known), $E[S_n | S_n] = S_n$:
    <span class="ps-eq">$n \\cdot E[X_1 | S_n] = E[X_1+\\cdots+X_n | S_n] = E[S_n | S_n] = S_n$</span>
  </div>
  <div class="ps-why">Properties 4 + 1</div>
</div>

<div class="proof-step">
  <div class="ps-num">3</div>
  <div class="ps-body">
    Divide both sides by n:
    <span class="ps-eq">$E[X_1 | S_n] = S_n / n$</span>
    Given only the total sum, the best guess for any single component is an equal share.
  </div>
  <div class="ps-why">Result</div>
</div>

</div>

*Interpretation:* The answer does not depend on $E[X_1]$ — counterintuitive but correct, because $S_n$ already encodes all aggregate information and symmetry forces equal attribution.

<div class="warning-box"><strong>⚠️ Subtle point:</strong> Conditioning on $S_n$ is strictly coarser than conditioning on all of $X_1,\\ldots,X_n$. The $\\sigma$-algebra $\\sigma(S_n) \\subseteq \\mathcal{F}_n$. With less information our best guess for $X_1$ worsens: from knowing $X_1$ exactly (under $\\mathcal{F}_n$) to knowing only $S_n/n$ (under $\\sigma(S_n)$).</div>
</div>

---

### Part 8 — Filtration (Formal Definition)

<div class="example-block">
<div class="ex-title">Definition — Discrete-time filtration <span class="ex-pill pill-defn">Definition</span></div>

"Definition If $X_1, X_2, \ldots$ is a sequence of random variables, then the associated (discrete time) filtration is the collection $\{\mathcal{F}_n\}$ where $\mathcal{F}_n$ denotes the information in $X_1, \ldots, X_n$. One assumption in the definition of a filtration, which may sometimes not reflect reality, is that information is never lost. If m &lt; n, then everything known at time m is still known at time n."
<div class="quote-explain">The key mathematical consequence of "information is never lost" is the set inclusion $\\mathcal{F}_m \\subseteq \\mathcal{F}_n$ for all $m &lt; n$. Every event in $\\mathcal{F}_m$ is also in $\\mathcal{F}_n$. This is not a philosophical claim — it is a precise constraint that the sequence of $\\sigma$-algebras must satisfy to qualify as a filtration.</div>

**Formally:** A filtration is an increasing sequence of $\\sigma$-algebras:

$$\\mathcal{F}_0 \\subseteq \\mathcal{F}_1 \\subseteq \\mathcal{F}_2 \\subseteq \\cdots \\subseteq \\mathcal{F}$$

**$\\mathcal{F}_0 = \\{\\emptyset, \\Omega\\}$** — the trivial $\\sigma$-algebra, representing the state before any observation.
</div>

---

### Property Summary Table

| Property | Formula | Plain English | Proved via |
|---|---|---|---|
| **Known Y** | $E[Y\\|\\mathcal{F}_n] = Y$ if Y is $\\mathcal{F}_n$-meas. | No uncertainty → best guess is the value itself | Definition — condition (i) |
| **Tower** | $E[E[Y\\|\\mathcal{F}_n]\\|\\mathcal{F}_m] = E[Y\\|\\mathcal{F}_m], m < n$ | Outer (coarser) conditioning always governs | Definition — condition (ii) + $\\mathcal{F}_m \\subseteq \\mathcal{F}_n$ |
| **Independence** | $E[Y\\|\\mathcal{F}_n] = E[Y]$ if $X_1,\\ldots,X_n \\perp Y$ | Irrelevant data leaves best guess unchanged | Definition — condition (ii) |
| **Linearity** | $E[aY+bZ\\|\\mathcal{F}_n] = aE[Y\\|\\mathcal{F}_n]+bE[Z\\|\\mathcal{F}_n]$ | Cond. expectation is a linear integral | Linearity of $E[\\cdot]$ + uniqueness |
| **Constants pull out** | $E[YZ\\|\\mathcal{F}_n] = Z\\cdot E[Y\\|\\mathcal{F}_n]$ if Z $\\mathcal{F}_n$-meas. | Known quantities act as constants | Proved for $\\mathbf{1}_A$, extended by MCT |

---

### Term Glossary

<div class="glossary-entry">
<div class="gterm">Probability space $(\Omega, \mathcal{F}, P)$ <span class="gcat cat-defn">Definition</span></div>
The triple: $\Omega$ = sample space (all outcomes); $\mathcal{F}$ = $\sigma$-algebra (observable events); $P : \mathcal{F} \to [0,1]$ probability measure with $P(\Omega) = 1$ and countable additivity. All random variables and stochastic processes in this book live on such a triple.
</div>

<div class="glossary-entry">
<div class="gterm">$\sigma$-algebra <span class="gcat cat-defn">Definition</span></div>
A collection $\mathcal{F}$ of subsets of $\Omega$ closed under complementation and countable unions, containing $\emptyset$. Encodes "which events are distinguishable." The trivial $\sigma$-algebra $\{\emptyset, \Omega\}$ encodes no information; the power set $2^\Omega$ encodes complete information.
</div>

<div class="glossary-entry">
<div class="gterm">Filtration $\{\mathcal{F}_n\}$ <span class="gcat cat-defn">Definition</span></div>
An increasing sequence $\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \mathcal{F}_2 \subseteq \cdots$ modelling accumulating information. $\mathcal{F}_n = \sigma(X_1,\ldots,X_n)$ — the smallest $\sigma$-algebra making $X_1,\ldots,X_n$ measurable. Information never shrinks: $m < n$ implies $\mathcal{F}_m \subseteq \mathcal{F}_n$.
</div>

<div class="glossary-entry">
<div class="gterm">$\mathcal{F}_n$-measurable <span class="gcat cat-meas">Measurability</span></div>
A random variable Z is $\mathcal{F}_n$-measurable if $\{Z \leq t\} \in \mathcal{F}_n$ for every $t \in \mathbb{R}$. Equivalently: $Z = \varphi(X_1,\ldots,X_n)$ for some measurable $\varphi$. Z's value is fully determined by the first n observations.
</div>

<div class="glossary-entry">
<div class="gterm">Conditional expectation $E[Y | \mathcal{F}_n]$ <span class="gcat cat-defn">Definition</span></div>
The unique $\mathcal{F}_n$-measurable random variable satisfying $E[E[Y|\\mathcal{F}_n]\\cdot\\mathbf{1}_A] = E[Y\\cdot\\mathbf{1}_A]$ for all $A \\in \\mathcal{F}_n$. The minimum-MSE predictor of Y given information $\\mathcal{F}_n$. A random variable — not a number — because its value depends on the observations $X_1,\\ldots,X_n$.
</div>

<div class="glossary-entry">
<div class="gterm">Indicator function $\mathbf{1}_A$ <span class="gcat cat-notn">Notation</span></div>
$\mathbf{1}_A(\omega) = 1$ if $\omega \in A$, else $0$. So $E[Z\cdot\mathbf{1}_A] = \int_A Z \, dP$ = the probability-weighted average of Z over outcomes where A occurs. Central to the formal two-condition definition of conditional expectation.
</div>

<div class="glossary-entry">
<div class="gterm">Tower property <span class="gcat cat-prop">Property</span></div>
$E[E[Y|\\mathcal{F}_n]|\\mathcal{F}_m] = E[Y|\\mathcal{F}_m]$ for $m < n$. The outer (coarser) conditioning always governs. Special case: $E[E[Y|\\mathcal{F}_n]] = E[Y]$. Proved using the defining property of conditional expectation and the inclusion $\\mathcal{F}_m \\subseteq \\mathcal{F}_n$.
</div>

<div class="glossary-entry">
<div class="gterm">Constants rule (pull-out property) <span class="gcat cat-prop">Property</span></div>
If Z is $\\mathcal{F}_n$-measurable then $E[YZ|\\mathcal{F}_n] = Z\\cdot E[Y|\\mathcal{F}_n]$. Z behaves as a known constant. Proved first for $Z = \\mathbf{1}_A$ ($A \\in \\mathcal{F}_n$) using the definition, extended to simple random variables by linearity, then to general Z by monotone convergence.
</div>

<div class="glossary-entry">
<div class="gterm">Radon-Nikodym theorem <span class="gcat cat-thm">Theorem</span></div>
Guarantees existence of conditional expectation. The function $\\mu(A) = E[Y\\cdot\\mathbf{1}_A]$ is a signed measure on $(\\Omega, \\mathcal{F}_n, P)$ with $\\mu \\ll P$. By Radon-Nikodym, there exists an $\\mathcal{F}_n$-measurable Z with $\\mu(A) = E[Z\\cdot\\mathbf{1}_A]$ for all $A \\in \\mathcal{F}_n$. This Z is $E[Y|\\mathcal{F}_n]$.
</div>

---

### Study-Note Summary

- **$E[Y | \\mathcal{F}_n]$** is the minimum-MSE predictor of Y given information $\\mathcal{F}_n$. It is a *random variable* — its value changes with the observations $X_1,\\ldots,X_n$. $E[Y]$ is the zero-information special case (a fixed number).
- **Probability space $(\\Omega, \\mathcal{F}, P)$:** $\\Omega$ = all outcomes; $\\mathcal{F}$ = $\\sigma$-algebra of observable events; $P$ = probability measure. The three $\\sigma$-algebra axioms (contains $\\emptyset$, closed under complements and countable unions) make $\\mathcal{F}$ self-consistent.
- **Filtration $\\{\\mathcal{F}_n\\}$:** increasing chain $\\mathcal{F}_0 \\subseteq \\mathcal{F}_1 \\subseteq \\cdots$ encoding growing information. $\\mathcal{F}_n = \\sigma(X_1,\\ldots,X_n)$. Information never shrinks.
- **Formal definition** uses two conditions — $\\mathcal{F}_n$-measurability + $E[E[Y|\\mathcal{F}_n]\\cdot\\mathbf{1}_A] = E[Y\\cdot\\mathbf{1}_A]$ for all $A \\in \\mathcal{F}_n$ — instead of a formula, because no single formula works in all probability spaces. Existence: Radon-Nikodym. Uniqueness: MSE argument.
- **Five properties:** (1) Known Y unchanged; (2) Tower — outer conditioning wins; (3) Independence → $E[Y]$; (4) Linearity; (5) Known factors pull out. All follow from the two defining conditions.
- **Example 1.1.1:** $E[S_n | \\mathcal{F}_m] = S_m + (n-m)\\mu$. When $\\mu = 0$ this becomes the martingale property of §1.2.
- **Example 1.1.3:** $E[X_1 | S_n] = S_n/n$. Conditioning on a coarser statistic gives an equal-share answer, independent of $E[X_1]$.

<div class="ref-tags">
<span class="ref-tag">Conditional expectation</span>
<span class="ref-tag">σ-algebra</span>
<span class="ref-tag">Filtration</span>
<span class="ref-tag">Measurability</span>
<span class="ref-tag">Tower property</span>
<span class="ref-tag">Indicator function</span>
<span class="ref-tag">Radon-Nikodym</span>
<span class="ref-tag">Probability space</span>
</div>

  </div>
</div>

