---
layout: distill
title: "Stochastic Calculus (Lawler) — Chapter 1"
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
  - name: 1.1 — Conditional Expectation
  - name: 1.2 — Martingales
  - name: 1.3 — Optional Sampling Theorem
  - name: 1.4 — Martingale Convergence Theorem

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
| $$\Omega$$ | Sample space — the set of all possible outcomes |
| $$\mathcal{F}$$ | $$\sigma$$-algebra — the collection of all observable events |
| $$P$$ | Probability measure — assigns numbers in $$[0,1]$$ to events in $$\mathcal{F}$$ |
| $$(\Omega, \mathcal{F}, P)$$ | Probability space — the full mathematical arena |
| $$A \in \mathcal{F}$$ | A is a measurable event (we can assign it a probability) |
| $$\Omega \setminus A$$ | Complement of A — all outcomes not in A |
| $$\mathcal{F}_n$$ | $$\sigma$$-algebra generated by $$X_1,\ldots,X_n$$ — information at time n |
| $$\mathcal{F}_m \subseteq \mathcal{F}_n$$ | All events knowable at time m are also knowable at time n |
| $$E[Y]$$ | Unconditional expectation — best guess for Y with no information |
| $$E[Y \mid \mathcal{F}_n]$$ | Conditional expectation — best guess for Y given information $$\mathcal{F}_n$$ |
| $$\mathbf{1}_A$$ | Function equal to 1 on event A, 0 elsewhere |
| i.i.d. | Independent and identically distributed |
| $$\mu \ll P$$ | $$\mu$$ absolutely continuous w.r.t. $$P$$ — every P-null set is also a $$\mu$$-null set |
| $$S_n$$ | Partial sum $$X_1 + X_2 + \cdots + X_n$$ |


---

### Part 1 — The Core Intuition

<div class="note-abstract">
Conditional expectation is the central object of stochastic calculus. At its core it answers one question: <em>given that we have observed some (but not all) information, what is our best guess for a random variable $Y$?</em> The answer is not a single number but another random variable — one that changes as our information changes.
</div>

<b>CORE IDEAS</b>

<strong>$$E[Y]$$ is the best guess for $$Y$$ given no information at all.</strong> The unconditional expectation is the baseline: if you know nothing about the outcome of an experiment, your single best guess (in the mean-squared-error sense) is $$E[Y]$$.

<strong>$$E[Y \mid \mathcal{F}_n]$$ is the best guess for Y given the information $$\mathcal{F}_n$$.</strong> As data arrives one variable at a time — $$X_1, X_2, \ldots, X_n$$ — we collect more information. The conditional expectation updates our best guess for Y using whatever is currently known.

<strong>$$E[Y \mid \mathcal{F}_n]$$ is itself a random variable, not a fixed number.</strong> Because it depends on the observed values of $$X_1, \ldots, X_n$$ — which are random — it is a function of those observations, hence random.

<strong>The formal definition bypasses explicit computation via one key property.</strong> $$E[Y \mid \mathcal{F}_n]$$ is defined as the unique $$\mathcal{F}_n$$-measurable random variable satisfying $$E[E[Y \mid \mathcal{F}_n] \cdot \mathbf{1}_A] = E[Y \cdot \mathbf{1}_A]$$ for all $$\mathcal{F}_n$$-measurable events A.

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "$E[Y \mid \mathcal{F}_n]$ is just a number, like $E[Y]$ but computed with less data."</div>
  <div class="mc-correct"><strong>Correct:</strong> $E[Y \mid \mathcal{F}_n]$ is a <em>random variable</em>. Its value changes depending on which values $X_1, \ldots, X_n$ take. If you observe different data, you get a different conditional expectation. $E[Y]$ is the special case where zero data is observed — a single fixed number. $E[Y \mid \mathcal{F}_n]$ is a whole function of the observations.</div>
</div>

---

### Part 2 — The Probability Space

<div class="note-abstract">
Before defining conditional expectation rigorously, we need the underlying mathematical arena: a probability space $(\Omega, \mathcal{F}, P)$. Everything — random variables, events, filtrations — lives inside this structure.
</div>

We assume that the random variables $$X_1, X_2, \ldots$$ are defined on a probability space $$(\Omega, \mathcal{F}, P)$$. Here $$\mathcal{F}$$ is a $$\sigma$$-algebra or $$\sigma$$-field of subsets of $$\Omega$$, that is, a collection of subsets satisfying:<br>

i. $$\emptyset \in \mathcal{F}$$<br>
ii. $$A \in \mathcal{F}$$ implies $$\Omega \setminus A \in \mathcal{F}$$ <br>
iii. $$A_1, A_2, \ldots \in \mathcal{F}$$ implies $$\bigcup_{n=1}^{\infty} A_n \in \mathcal{F}$$.<br>

This defines the three $$\sigma$$-algebra axioms. (i) The empty set — the impossible event — must be an event. (ii) If A is observable, so is its complement: "A did not happen" must also be observable. (iii) Countable unions of events are events: "at least one of $$A_1, A_2, \ldots$$ happened" is observable. These three rules make $$\mathcal{F}$$ a self-consistent collection of questions we can ask about the experiment.

<div class="example-block" markdown="1">
<div class="ex-title">Minimal example: two fair coin flips </div>

**Sample space:** $$\Omega = \{HH, HT, TH, TT\}$$

**The full $$\sigma$$-algebra** $$\mathcal{F} = 2^\Omega$$ contains all 16 subsets. This always satisfies all three axioms and encodes complete information.

**A smaller valid $$\sigma$$-algebra** encoding only the first flip:

$$\mathcal{F}_1 = \{ \emptyset, \{HH, HT\}, \{TH, TT\}, \Omega \}$$

- $$\emptyset \in \mathcal{F}_1$$ ✓ &emsp;(axiom i)
- $$\{HH,HT\}^c = \{TH,TT\} \in \mathcal{F}_1$$ ✓ &emsp;(axiom ii)
- Any union of these four sets stays in $$\mathcal{F}_1$$ ✓ &emsp;(axiom iii)

$$\mathcal{F}_1$$ lets us distinguish "first flip = H" from "first flip = T" — nothing more.

<div class="ex-lesson"><strong>Key point:</strong> A $\sigma$-algebra is a mathematical encoding of a state of knowledge. Larger $\sigma$-algebra = more information. $\mathcal{F}_1 \subseteq 2^\Omega$ reflects that knowing one flip is strictly less information than knowing both.</div>
</div>

---

### Part 3 — The Filtration

<div class="note-abstract">
A filtration is a growing sequence of σ-algebras modelling information accumulating over time. At time $n$, $F_n$ records everything observed up to time $n$ — and once something is known it is never forgotten.<br>

Let $X_1, X_2, \ldots$ be random variables which we think of as a time series with the data arriving one at a time. At time $n$ we have viewed the values $X_1, \ldots, X_n$. … We will write $\mathcal{F}_n$ for 'the information contained in $X_1, \ldots, X_n$.
</div>

$$\mathcal{F}_n$$ is not a number or a random variable — it is a $$\sigma$$-algebra: a collection of events. "Information in $$X_1,\ldots,X_n$$" means all questions of the form "did the observations satisfy some condition?" that can be answered once $$X_1,\ldots,X_n$$ are known.<br>

"The information $$\mathcal{F}_n$$ is the smallest sub $$\sigma$$-algebra $$G$$ of $$\mathcal{F}$$ such that $$X_1, \ldots, X_n$$ are $$G$$-measurable. The latter statement means that for all $$t \in \mathbb{R}$$, the event $$\{X_j \leq t\} \in \mathcal{F}_n$$."<br>

"$$X_j$$ is $$\mathcal{F}_n$$-measurable" means: for every threshold $$t$$, the set of outcomes where $$X_j \leq t$$ is an event in $$\mathcal{F}_n$$. Knowing $$X_1,\ldots,X_n$$ is enough to determine $$X_j$$. The word "smallest" is important — we take only events genuinely required to describe $$X_1,\ldots,X_n$$, not any extras.

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "$X$ is $\mathcal{F}_n$-measurable just means $X$ is one of the variables $X_1,\ldots,X_n$."</div>
  <div class="mc-correct"><strong>Correct:</strong> Any function of $X_1,\ldots,X_n$ is also $\mathcal{F}_n$-measurable — e.g., $X_1 + X_2$, $\max(X_1,\ldots,X_n)$, or $S_n^2$. The condition is that X's value is fully determined once $X_1,\ldots,X_n$ are known, not that X appears explicitly in the list.</div>
</div>


<div class="example-block" markdown="1">
<div class="ex-title">Example of a Measurable random variable on a finite space</div>

Let $$\Omega=\{\omega_1,\omega_2,\omega_3\}$$ and define the $$\sigma$$-algebra
$$\mathcal{F}=\{\emptyset, \Omega, \{\omega_1,\omega_2\}, \{\omega_3\}\}$$.

Define the random variable
$$X(\omega_1)=0,\; X(\omega_2)=0,\; X(\omega_3)=1$$.

To check measurability, verify that
$$\{X\le t\}\in\mathcal{F}\quad \forall t\in\mathbb{R}$$.

For example:

$$\{X\le 0\}=\{\omega_1,\omega_2\}\in\mathcal{F}$$,

$$\{X\le 0.5\}=\{\omega_1,\omega_2\}\in\mathcal{F}$$,

$$\{X\le 2\}=\Omega\in\mathcal{F}$$.

Hence $$X$$ is $$\mathcal{F}$$-measurable.

<div class="ex-lesson">
<strong>Key point:</strong> A random variable is measurable if the information structure $\mathcal{F}$ can distinguish exactly the events needed to determine its value. Here, $\mathcal{F}$ separates $\omega_3$ from $\{\omega_1,\omega_2\}$, which is exactly what $X$ depends on.
</div>
</div>


<div class="example-block" markdown="1">
<div class="ex-title">Example of a non-measurable function</div>

Let $$\Omega=\{\omega_1,\omega_2,\omega_3\}$$ and consider the same $$\sigma$$-algebra
$$\mathcal{F}=\{\emptyset,\Omega,\{\omega_1,\omega_2\},\{\omega_3\}\}$$

Define the function
$$Y(\omega_1)=0,\; Y(\omega_2)=1,\; Y(\omega_3)=0$$.

Now check measurability.

Consider the event
$$\{Y\le 0\}=\{\omega_1,\omega_3\}$$.

But $$\{\omega_1,\omega_3\}\notin\mathcal{F}$$.

Hence $$Y$$ is not $$\mathcal{F}$$-measurable.

<div class="ex-lesson">
<strong>Key point:</strong> The $\sigma$-algebra $\mathcal{F}$ cannot distinguish $\omega_1$ from $\omega_2$ in a way consistent with $Y$. Since $Y$ separates these outcomes differently while $\mathcal{F}$ does not, the function is “too fine” for the available information structure.
</div>
</div>

---

### Part 4 — Motivating the Definition (Density Case)

<div class="note-abstract">"Suppose that $(X, Y)$ have a joint density $f(x, y)$, $0 < x, y < \infty$, with marginal densities $f(x) = \int f(x,y)\,dy$, $g(y) = \int f(x,y)\,dx$. The conditional density $f(y\mid x)$ is defined by $f(y\mid x) = \frac{f(x,y)}{f(x)}$."</div>

$$f(x,y)$$ is the joint probability density near $$(x,y)$$. $$f(x)$$ is the marginal density of $$X$$ — the probability near $$x$$ regardless of $$Y$$, obtained by integrating out all $$y$$-values. $$f(y\mid x)$$ is the relative weight on each $$y$$-value given $$X = x$$. Division by $$f(x)$$ normalises so that $$f(y\mid x)$$ integrates to 1 over $$y$$.

This gives the familiar undergraduate formula:

$$E[Y \mid X = x] = \int_{-\infty}^{\infty} y\, f(y \mid x)\, dy = \frac{\int_{-\infty}^{\infty} y\, f(x,y)\, dy}{f(x)}$$

Note that $$E[Y \mid X]$$ is a random variable which is determined by the value of the random variable $$X$$.

$$E[Y \mid X = x]$$ for a fixed $$x$$ is a number. But $$E[Y \mid X]$$ — without fixing $$x$$ — is a function of $$X$$. Since $$X$$ is random, this function is itself random. This is the key conceptual leap the formal definition must capture.

**The tower property emerges naturally:**

$$E\bigl[E[Y \mid X]\bigr] = \int_{-\infty}^{\infty} E[Y \mid X = x]\, f(x)\, dx = \iint y\, f(x,y)\, dy\, dx = E[Y]$$

Averaging the conditional best-guess over all possible observations recovers the unconditional expectation. This is the **tower property**, generalised by the abstract definition below.

---

### Part 5 — The Formal Definition

<div class="note-abstract">
The conditional expectation $E[Y \mid \mathcal{F}_n]$ is the unique random variable satisfying the following. <br>

(i) $E[Y \mid \mathcal{F}_n]$ is $\mathcal{F}_n$-measurable. <br>

(ii) For every $\mathcal{F}_n$-measurable event A, $E[E[Y \mid \mathcal{F}_n] \cdot \mathbf{1}_A] = E[Y \cdot \mathbf{1}_A]$.
</div>

Condition (i): The output is computable from $$X_1,\ldots,X_n$$ alone — it cannot use future information.

Condition (ii): On every slice of $$\Omega$$ that can be identified from current information (any $$A \in \mathcal{F}_n$$), the average of $$E[Y \mid \mathcal{F}_n]$$ over that slice equals the average of Y over the same slice.

These two conditions uniquely determine $$E[Y \mid \mathcal{F}_n]$$ without requiring a closed-form formula.

**What is $$\mathbf{1}_A$$?**

$$\mathbf{1}_A(\omega) = \begin{cases} 1 & \text{if } \omega \in A \\ 0 & \text{if } \omega \notin A \end{cases}$$

So $$E[Z \cdot \mathbf{1}_A]$$ = probability-weighted average of Z over outcomes where A occurs = $$\int_A Z \, dP$$.

**Why not give an explicit formula?** In general probability spaces (uncountable $$\Omega$$, continuous distributions), no single formula works universally. The two-condition characterisation is both sufficient and rigorous. Existence follows from the Radon-Nikodym theorem; uniqueness from: if $$Z_1$$ and $$Z_2$$ both satisfy the conditions then $$E[(Z_1 - Z_2)^2] = 0$$, so $$Z_1 = Z_2$$ almost surely.

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> Condition (ii) $E[E[Y \mid \mathcal{F}_n] \cdot \mathbf{1}_A] = E[Y \cdot \mathbf{1}_A]$ is just saying $E[Y \mid \mathcal{F}_n] = Y$ </div>
  <div class="mc-correct"><strong>Correct:</strong> It says they agree <em>on average over every observable event A</em> — not pointwise. $E[Y \mid \mathcal{F}_n]$ is a smoothed version of $Y$: it preserves the same probability mass on every $\mathcal{F}_n$-identifiable slice, but replaces $Y$'s within-slice variation with a single average value. The pointwise equality $E[Y \mid \mathcal{F}_n](\omega) = Y(\omega)$ only holds when $Y$ is itself $\mathcal{F}_n$-measurable.</div>
</div>



---

### Part 6 — Properties of Conditional Expectation

<b>Proposition 1.1.1:</b> Suppose $$X_1, X_2, \ldots$$ is a sequence of random variables and $$\mathcal{F}_n$$ denotes the information at time n. The conditional expectation $$E[Y \mid \mathcal{F}_n]$$ satisfies the following properties.

**Property 1 — If Y is already known, conditioning changes nothing**

$$\text{If } Y \text{ is } \mathcal{F}_n\text{-measurable}, \quad E[Y \mid \mathcal{F}_n] = Y.$$

<b>Why:</b> Y is determined by $$X_1,\ldots,X_n$$. No uncertainty remains — the best guess is the value itself.


**Property 2 — Tower property (law of iterated expectations)**

$$m < n \implies E\bigl[\,E[Y \mid \mathcal{F}_n]\;\big|\;\mathcal{F}_m\bigr] = E[Y \mid \mathcal{F}_m].$$

<b>Why:</b> Compute the best guess for $$Y$$ using information up to time $$n$$, then downgrade it to only use information up to time $$m < n$$. The result is identical to computing the best guess with time $$m$$ information directly.

Special case $$m = 0$$: **$$E[E[Y \mid \mathcal{F}_n]] = E[Y]$$**.


**Property 3 — Independence means conditioning is useless**

$$X_1,\dots,X_n \perp Y \implies E[Y \mid \mathcal{F}_n] = E[Y].$$

<b>Why:</b> If the observations carry zero information about $$Y$$, the best guess remains the unconditional mean.


**Property 4 — Linearity**

$$E[aY + bZ \mid \mathcal{F}_n] = a\,E[Y \mid \mathcal{F}_n] + b\,E[Z \mid \mathcal{F}_n].$$

<b>Why:</b> Conditional expectation is an integral, and integrals are linear.


**Property 5 — Known factors pull out (constants rule)**

$$Z \text{ is } \mathcal{F}_n\text{-measurable} \implies E[YZ \mid \mathcal{F}_n] = Z\cdot E[Y \mid \mathcal{F}_n].$$

<b>Why:</b> Z is already determined by current information — it plays the role of a known constant. Only $$Y$$ carries residual randomness to average over.

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception — Tower Property</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "$E[E[Y \mid \mathcal{F}_n] \mid \mathcal{F}_m] = E[Y \mid \mathcal{F}_n]$ — the inner conditioning dominates because it has more information."</div>
  <div class="mc-correct"><strong>Correct:</strong> The <em>outer</em> conditioning dominates: the result is $E[Y \mid \mathcal{F}_m]$. When you condition on less information ($\mathcal{F}_m \subseteq \mathcal{F}_n$), you lose the fine detail provided by $\mathcal{F}_n$. The coarser $\sigma$-algebra always wins. Think of it as: the final answer can only use what the outermost conditioning permits.</div>
</div>

---

### Part 7 — Worked Examples

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.1.1 — $E[S_n \mid \mathcal{F}_m]$ for independent increments </div>

**Setup:** $$X_1, X_2, \ldots$$ independent with $$E[X_j] = \mu$$. Let $$S_n = X_1 + \cdots + X_n$$, $$\mathcal{F}_m = \sigma(X_1,\ldots,X_m)$$, $$m < n$$.

$$E[S_n \mid \mathcal{F}_m] = E[S_m \mid \mathcal{F}_m] + E[S_n - S_m \mid \mathcal{F}_m]$$

$$S_m = X_1+\cdots+X_m$$ is fully determined by $$X_1,\ldots,X_m$$, so it is $$\mathcal{F}_m$$-measurable:

$$E[S_m \mid \mathcal{F}_m] = S_m$$

$$S_n - S_m = X_{m+1}+\cdots+X_n$$

$$E[S_n - S_m \mid \mathcal{F}_m] = E[S_n - S_m] = (n-m)\mu$$

$$E[S_n \mid \mathcal{F}_m] = S_m + (n-m)\mu$$
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.1.2 — $E[S_n^2 \mid \mathcal{F}_m]$ for zero-mean increments </div>

**Setup:** $$\mu = 0$$, $$E[X_j^2] = \sigma^2 < \infty$$. Same $$S_n$$, $$\mathcal{F}_m$$ as above.

Write $$S_n = S_m + (S_n - S_m)$$ and expand the square:

$$E[S_n^2 \mid \mathcal{F}_m] = E[S_m^2 \mid \mathcal{F}_m] + 2 E[S_m(S_n-S_m) \mid \mathcal{F}_m] + E[(S_n-S_m)^2 \mid \mathcal{F}_m]$$

<b>Term 1:</b> $$S_m^2$$ is $$\\mathcal{F}_m$$-measurable so $$E[S_m^2 \mid \mathcal{F}_m] = S_m^2$$

<b>Term 2:</b> $$S_m$$ pulls out ($$\mathcal{F}_m$$-measurable); $$S_n-S_m$$ is independent of $$\mathcal{F}_m$$ with mean 0:

$$2 E[S_m(S_n-S_m) \mid \mathcal{F}_m] = 2 S_m \cdot E[S_n-S_m] = 2 S_m \cdot 0 = 0$$

<b>Term 3:</b> $$(S_n-S_m)^2$$ is independent of $$\mathcal{F}_m$$; its expectation is the variance of $$(n-m)$$ increments:

$$E[(S_n-S_m)^2 \mid \mathcal{F}_m] = \text{Var}(S_n-S_m) = (n-m)\sigma^2$$

Combine Terms 1, 2, 3:

$$E[S_n^2 \mid \mathcal{F}_m] = S_m^2 + (n-m)\sigma^2$$

</div>

---

### Part 8 — Filtration (Formal Definition)

<div class="note-abstract">
"Definition If $X_1, X_2, \ldots$ is a sequence of random variables, then the associated (discrete time) filtration is the collection $\{\mathcal{F}_n\}$ where $\mathcal{F}_n$ denotes the information in $X_1, \ldots, X_n$. One assumption in the definition of a filtration, which may sometimes not reflect reality, is that information is never lost. If m < n, then everything known at time m is still known at time n."
</div>

The key mathematical consequence of "information is never lost" is the set inclusion $$\mathcal{F}_m \subseteq \mathcal{F}_n$$ for all $$m < n$$. Every event in $$\mathcal{F}_m$$ is also in $$\mathcal{F}_n$$. This is not a philosophical claim — it is a precise constraint that the sequence of $$\sigma$$-algebras must satisfy to qualify as a filtration.

**Formally:** A filtration is an increasing sequence of $$\sigma$$-algebras:

$$\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \mathcal{F}_2 \subseteq \cdots \subseteq \mathcal{F}$$

**$$\mathcal{F}_0 = \{\emptyset, \Omega\}$$** — the trivial $$\sigma$$-algebra, representing the state before any observation.

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
<div class="gterm">Conditional expectation $E[Y \mid \mathcal{F}_n]$ <span class="gcat cat-defn">Definition</span></div>
The unique $\mathcal{F}_n$-measurable random variable satisfying $E[E[Y \mid \mathcal{F}_n]\cdot\mathbf{1}_A] = E[Y\cdot\mathbf{1}_A]$ for all $A \in \mathcal{F}_n$. The minimum-MSE predictor of Y given information $\mathcal{F}_n$. A random variable — not a number — because its value depends on the observations $X_1,\ldots,X_n$.
</div>

<div class="glossary-entry">
<div class="gterm">Indicator function $\mathbf{1}_A$ <span class="gcat cat-notn">Notation</span></div>
$\mathbf{1}_A(\omega) = 1$ if $\omega \in A$, else $0$. So $E[Z\cdot\mathbf{1}_A] = \int_A Z \, dP$ = the probability-weighted average of Z over outcomes where A occurs. Central to the formal two-condition definition of conditional expectation.
</div>

<div class="glossary-entry">
<div class="gterm">Tower property <span class="gcat cat-prop">Property</span></div>
$E[E[Y \mid \mathcal{F}_n] \mid \mathcal{F}_m] = E[Y \mid \mathcal{F}_m]$ for $m < n$. The outer (coarser) conditioning always governs. Special case: $E[E[Y \mid \mathcal{F}_n]] = E[Y]$. Proved using the defining property of conditional expectation and the inclusion $\mathcal{F}_m \subseteq \mathcal{F}_n$.
</div>

<div class="glossary-entry">
<div class="gterm">Constants rule (pull-out property) <span class="gcat cat-prop">Property</span></div>
If Z is $\mathcal{F}_n$-measurable then $E[YZ \mid \mathcal{F}_n] = Z\cdot E[Y \mid \mathcal{F}_n]$. Z behaves as a known constant. Proved first for $Z = \mathbf{1}_A$ ($A \in \mathcal{F}_n$) using the definition, extended to simple random variables by linearity, then to general Z by monotone convergence.
</div>

<div class="glossary-entry">
<div class="gterm">Radon-Nikodym theorem <span class="gcat cat-thm">Theorem</span></div>
Guarantees existence of conditional expectation. The function $\mu(A) = E[Y\cdot\mathbf{1}_A]$ is a signed measure on $(\Omega, \mathcal{F}_n, P)$ with $\mu \ll P$. By Radon-Nikodym, there exists an $\mathcal{F}_n$-measurable Z with $\mu(A) = E[Z\cdot\mathbf{1}_A]$ for all $A \in \mathcal{F}_n$. This Z is $E[Y \mid \mathcal{F}_n]$.
</div>


  </div>
</div>





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
| $$M_n$$ | The martingale process at time $$n$$ |
| $$\mathcal{F}_n$$ | Filtration at time $$n$$ — information in $$M_0, M_1, \ldots, M_n$$ |
| $$E[M_n \mid \mathcal{F}_m] = M_m$$ | The defining martingale condition for $$m < n$$ |
| $$\Delta M_n = M_n - M_{n-1}$$ | Increment of the martingale at step $$n$$ |
| $$B_n$$ | The "bet" at time $$n$$ — an $$\mathcal{F}_{n-1}$$-measurable process |
| $$W_n = \sum_{j=1}^n B_j \Delta M_j$$ | Winnings under a betting strategy — the discrete stochastic integral |
| $$S_n = X_1 + \cdots + X_n$$ | Partial sum of i.i.d. mean-zero random variables |
| $$A_n = \sigma_1^2 + \cdots + \sigma_n^2$$ | Cumulative variance (predictable compensator) |
| $$E[M_n \mid \mathcal{F}_m] \geq M_m$$ | Submartingale condition |
| $$E[M_n \mid \mathcal{F}_m] \leq M_m$$ | Supermartingale condition |
| $$\mathcal{F}_{n-1}$$-measurable | $$B_n$$ is known before time $$n$$ — the "non-anticipating" condition |


---

### Part 1 — The Core Intuition

<div class="note-abstract">
A martingale is the mathematical model of a <em>fair game</em>. At every moment, no matter what has happened so far, the expected future value of the process equals its current value.
</div>

<b>CORE IDEAS</b>

<strong>A martingale models a fair game.</strong> If $$M_n$$ represents cumulative winnings, "fair" means: regardless of the history of play, the expected winnings at any future time equal the current winnings. No strategy can give you a systematic advantage over a martingale in finite time.

<strong>The martingale condition is a statement about conditional expectations.</strong> The defining equation $$E[M_n \mid \mathcal{F}_m] = M_m$$ for $$m < n$$ is a direct application of §1.1: given everything observed up to time $$m$$, the best prediction of $$M_n$$ is simply $$M_m$$ itself.

<strong>To verify the martingale property it suffices to check one step at a time (The One-Step Criterion).</strong> Rather than checking $$E[M_n \mid \mathcal{F}_m] = M_m$$ for all pairs $$m < n$$, it is enough to verify $$E[M_{n+1} \mid \mathcal{F}_n] = M_n$$ for every $$n$$. The tower property of §1.1 propagates this to all future times.</div>

<strong>A martingale has constant expected value.</strong> Taking the full expectation: $\mathbb{E}[M_n] = \mathbb{E}[E[M_n \mid \mathcal{F}_0]] = \mathbb{E}[M_0]$ for all $n$. The mean is time-invariant — a necessary (but not sufficient) condition for fairness.

---

### Part 2 — The Formal Definition

<div class="note-abstract" markdown="1">
Suppose $$X_1, X_2, \ldots$$ is a sequence of random variables to which we associate the filtration $$\{\mathcal{F}_n\}$$ where $$\mathcal{F}_n$$ is the information contained in $$X_1, \ldots, X_n$$. 

A sequence of random variables $$M_0, M_1, \ldots$$ is called a <b>martingale</b> with respect to the filtration $$\{\mathcal{F}_n\}$$ if:

(i) For each $$n$$, $$M_n$$ is an $$\mathcal{F}_n$$-measurable random variable with $$E[\lvert M_n \rvert] < \infty$$.

(ii) If $$m < n$$, then

$$E[M_n \mid \mathcal{F}_m] = M_m. \tag{1.4}$$
</div>


**Unpacking condition (i):**
- *$$\mathcal{F}_n$$-measurable:* the value of $$M_n$$ is fully determined by the information available at time $$n$$. It does not look into the future.
- *$$E[\lvert M_n \rvert] < \infty$$:* integrability — the process cannot take infinitely large values on average. This is needed for the conditional expectation $$E[M_n \mid \mathcal{F}_m]$$ to be well-defined.

**Unpacking condition (ii):** Given everything observed up to time $$m$$, the best prediction of $$M_n$$ at any later time $$n > m$$ is simply the current value $$M_m$$. The process has no predictable drift in either direction.

<div class="ex-lesson"><strong>Equivalent one-step form:</strong> It suffices to check $E[M_{n+1} \mid \mathcal{F}_n] = M_n$ for every $n \geq 0$. The tower property then gives $E[M_{n+2} \mid \mathcal{F}_n] = E[E[M_{n+2} \mid \mathcal{F}_{n+1}] \mid \mathcal{F}_n] = E[M_{n+1} \mid \mathcal{F}_n] = M_n$, and so on for all future times.</div>

---

### Part 3 — Sub- and Supermartingales

<div class="note-abstract" markdown="1">
If the condition of martingale ($$E[M_n \mid \mathcal{F}_m] = M_m$$) is replaced with $$E[M_n \mid \mathcal{F}_m] \geq M_m$$, then the process is called a <b>submartingale</b>. If it is replaced with $$E[M_n \mid \mathcal{F}_m] \leq M_m$$, then it is called a <b>supermartingale</b>. 
</div>

| Process | Condition | Interpretation |
|---|---|---|
| **Martingale** | $$E[M_n \mid \mathcal{F}_m] = M_m$$ | Fair game — no systematic gain or loss |
| **Submartingale** | $$E[M_n \mid \mathcal{F}_m] \geq M_m$$ | Favourable game — expected value grows over time |
| **Supermartingale** | $$E[M_n \mid \mathcal{F}_m] \leq M_m$$ | Unfavourable game — expected value shrinks over time |

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
Suppose that $$M_0, M_1, \ldots$$ is a martingale with respect to the filtration $$\mathcal{F}_n$$ . For $$n \geq 1$$, let $$\Delta M_n = M_n - M_{n-1}$$. Let $$B_j$$ denote the 'bet' on the $$j$$th game. We allow negative values of $$B_j$$ which indicate betting that the price will go down or the game will be lost. Let $$W_n$$ denote the winnings in this strategy: $$W_0 = 0$$ and for $$n \geq 1$$,

$$W_n = \sum_{j=1}^n B_j [M_j - M_{j-1}] = \sum_{j=1}^n B_j \Delta M_j.$$"
</div>


**Three conditions on the betting strategy $$B_n$$:**

1. **Boundedness:** $$\lvert B_n \rvert \leq K_n < \infty$$ for some finite constant $$K_n$$ — bets cannot be infinite.
2. **Non-anticipating (predictability):** $$B_n$$ is $$\mathcal{F}_{n-1}$$-measurable — the bet at time $$n$$ can only use information from before time $$n$$. You cannot see the outcome before placing the bet.
3. **Integrability:** The bound above ensures $$E[\lvert W_n \rvert] < \infty$$.

**$$W_n$$ is a martingale — verification:**


$$E[W_{n+1} \mid \mathcal{F}_n] = E[W_n + B_{n+1}(M_{n+1} - M_n) \mid \mathcal{F}_n].$$

Since $$W_n$$ is $$\mathcal{F}_n$$-measurable, $$E[W_n \mid \mathcal{F}_n] = W_n$$. Also, since $$B_{n+1}$$ is $$\mathcal{F}_n$$-measurable and $$M$$ is a martingale,

$$E[B_{n+1}(M_{n+1} - M_n) \mid \mathcal{F}_n] = B_{n+1} E[M_{n+1} - M_n \mid \mathcal{F}_n] = 0.$$

Therefore, $$E[W_{n+1} \mid \mathcal{F}_n] = W_n$$.

$$W_n$$ is known at time $$n$$. $$B_{n+1}$$ is known at time $$n$$ and pulls out. The remaining factor $$E[M_{n+1} - M_n \mid \mathcal{F}_n] = 0$$ by the martingale property of $$M$$.

---

### Part 5 — Worked Examples

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.2.1 — Simple random walk as a martingale <span class="ex-pill pill-ex">Example</span></div>

Suppose $$X_1, X_2, \ldots$$ are independent random variables with $$E[X_j] = 0$$ for each $$j$$. Let $$S_0 = 0$$ and $$S_n = X_1 + \cdots + X_n$$. In the last section we showed that if $$m < n$$, then $$E[S_n \mid \mathcal{F}_m] = S_m$$. Hence, $$S_n$$ is a martingale with respect to $$\mathcal{F}_n$$, the information in $$X_1, \ldots, X_n$$.

**Verification using the one-step criterion:**

Check $$E[S_{n+1} \mid \mathcal{F}_n] = S_n$$:

$$E[S_{n+1} \mid \mathcal{F}_n] = E[S_n + X_{n+1} \mid \mathcal{F}_n] = E[S_n \mid \mathcal{F}_n] + E[X_{n+1} \mid \mathcal{F}_n].$$

- $$S_n$$ is $$\mathcal{F}_n$$-measurable $$\Rightarrow$$ $$E[S_n \mid \mathcal{F}_n] = S_n$$.
- $$X_{n+1}$$ is independent of $$\mathcal{F}_n$$ and $$E[X_{n+1}] = 0$$ $$\Rightarrow$$ $$E[X_{n+1} \mid \mathcal{F}_n] = 0$$.

$$E[S_{n+1} \mid \mathcal{F}_n] = S_n + 0 = S_n. \checkmark$$

<div class="ex-lesson"><strong>Key point:</strong> Mean-zero independent increments are the prototype martingale. The increments $X_j$ play the role of "fair coin tosses" — no single step has a predictable direction, so the running sum has no predictable drift.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.2.2 — $S_n^2 - A_n$ as a martingale <span class="ex-pill pill-ex">Example</span></div>

Suppose $$X_n, S_n, \mathcal{F}_n$$ are as in Example 1.2.1 and also assume $$\text{Var}[X_j] = E[X_j^2] = \sigma_j^2 < \infty$$. Let

$$A_n = \sigma_1^2 + \cdots + \sigma_n^2, \qquad M_n = S_n^2 - A_n,$$

where $$M_0 = 0$$. Then $$M_n$$ is a martingale with respect to $$\mathcal{F}_n$$.

**Verification — one-step check:**

$$E[S_{n+1}^2 \mid \mathcal{F}_n] = E[(S_n + X_{n+1})^2 \mid \mathcal{F}_n]$$

$$= E[S_n^2 \mid \mathcal{F}_n] + 2E[S_n X_{n+1} \mid \mathcal{F}_n] + E[X_{n+1}^2 \mid \mathcal{F}_n].$$

- **Term 1:** $$S_n^2$$ is $$\mathcal{F}_n$$-measurable $$\Rightarrow$$ $$E[S_n^2 \mid \mathcal{F}_n] = S_n^2$$.
- **Term 2:** $$S_n$$ pulls out; $$E[X_{n+1} \mid \mathcal{F}_n] = E[X_{n+1}] = 0$$ $$\Rightarrow$$ $$2S_n \cdot 0 = 0$$.
- **Term 3:** $$X_{n+1}$$ independent of $$\mathcal{F}_n$$ $$\Rightarrow$$ $$E[X_{n+1}^2 \mid \mathcal{F}_n] = E[X_{n+1}^2] = \sigma_{n+1}^2$$.

Therefore $$E[S_{n+1}^2 \mid \mathcal{F}_n] = S_n^2 + \sigma_{n+1}^2$$, and:

$$
\begin{aligned}
E[M_{n+1} \mid \mathcal{F}_n]
&= E[S_{n+1}^2 - A_{n+1} \mid \mathcal{F}_n] \\
&= S_n^2 + \sigma_{n+1}^2 - (A_n + \sigma_{n+1}^2)
 = S_n^2 - A_n = M_n. \checkmark
\end{aligned}
$$

<div class="ex-lesson"><strong>Key point:</strong> $S_n^2$ alone is a submartingale (it grows by $\sigma_{n+1}^2$ in expectation at each step). Subtracting the cumulative variance $A_n$ exactly compensates this drift and restores the martingale property. The sequence $A_n$ is called the <em>predictable compensator</em> of $S_n^2$. This is the discrete analogue of the quadratic variation.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.2.4 — The martingale betting strategy: infinite time beats the game <span class="ex-pill pill-ex">Example</span></div>

Martingale betting strategy. Let $$X_1, X_2, \ldots$$ be independent random variables with

$$P\{X_j = 1\} = P\{X_j = -1\} = \tfrac{1}{2}$$

… We will consider the following betting strategy. We start by betting <span>$1</span>. If we win, we quit; otherwise, we bet <span>$2</span> on the next game. If we win the second game, we quit; otherwise we double our bet to <span>$4</span> and play. Each time we lose, we double our bet. At the time that we win, we will be ahead <span>$1</span>d.

**The bets are:**

$$B_1 = 1$$, $$B_j = 2^{j-1} \text{ if } X_1 = X_2 = \cdots = X_{j-1} = -1$$, otherwise  $$B_j = 0$$.

**The winnings $$W_n$$:** either $$+1$$ (if we won at some point), or $$-(1 + 2 + 4 + \cdots + 2^{n-1}) = -(2^n - 1)$$ (if we lost all $$n$$ rounds).

**Direct verification that $$E[W_n] = 0$$:**

$$E[W_n] = 1 \cdot \Bigl(1 - \tfrac{1}{2^n}\Bigr) + \bigl(-(2^n - 1)\bigr) \cdot \tfrac{1}{2^n} = 1 - \tfrac{1}{2^n} - 1 + \tfrac{1}{2^n} = 0.$$

**The paradox:** With probability one we eventually win, so $$W_\infty = \lim_{n \to \infty} W_n = 1$$, giving $$E[W_\infty] = 1 \neq 0 = E[W_0]$$.

This does **not** contradict the martingale property of $$W_n$$. The issue is that the strategy requires potentially infinite bets ($$B_n = 2^{n-1}$$) — the boundedness condition $$\lvert B_n \rvert \leq K_n$$ is satisfied for each fixed $$n$$, but the constants $$K_n$$ grow without bound. In finite time $$W_n$$ is always a martingale; the "beating" of the game only emerges after infinitely many steps.

<div class="ex-lesson"><strong>Key point:</strong> You can beat a fair game in infinite time by tolerating potentially unbounded bets and losses. The martingale property of $W_n$ — which holds for every finite $n$ — does not prevent $E[W_\infty] \neq E[W_0]$. This distinction motivates the Optional Sampling Theorem in §1.3, which gives conditions under which $E[W_T] = E[W_0]$ is preserved at stopping times $T$.</div>
</div>

---

### Part 6 — Connection to §1.1 Properties

Every step in §1.2 relies directly on the five properties of conditional expectation from §1.1. The table below makes these dependencies explicit.

| Martingale argument | §1.1 property used |
|---|---|
| $$E[S_n \mid \mathcal{F}_n] = S_n$$ — current sum is known | Property 1 — Known $$Y$$ |
| $$E[X_{n+1} \mid \mathcal{F}_n] = E[X_{n+1}] = 0$$ — future increment is independent | Property 3 — Independence |
| $$E[S_n X_{n+1} \mid \mathcal{F}_n] = S_n E[X_{n+1} \mid \mathcal{F}_n]$$ — $$S_n$$ pulls out | Property 5 — Constants rule |
| $$E[W_n \mid \mathcal{F}_n] = W_n$$ — current winnings are known | Property 1 — Known $$Y$$ |
| $$E[B_{n+1}(M_{n+1} - M_n) \mid \mathcal{F}_n] = B_{n+1} \cdot 0$$ — $$B_{n+1}$$ pulls out | Property 5 — Constants rule |
| One-step check implies all-future check | Property 2 — Tower property |

---

### Term Glossary


<div class="glossary-entry">
<div class="gterm">Adapted process <span class="gcat cat-defn">Definition</span></div>
A sequence $M_0, M_1, \ldots$ is adapted to $\{\mathcal{F}_n\}$ if $M_n$ is $\mathcal{F}_n$-measurable for every $n$. Equivalently, the value of $M_n$ is fully determined by the information $X_1, \ldots, X_n$ available at time $n$. All martingales must be adapted — they cannot depend on future observations.
</div>

<div class="glossary-entry">
<div class="gterm">Integrability condition $E[\lvert M_n \rvert] < \infty$ <span class="gcat cat-prop">Property</span></div>
Required so that $E[M_n \mid \mathcal{F}_m]$ is well-defined. Without this, the conditional expectation may not exist. It is a weak condition — it rules out processes that take infinitely large values with positive probability but allows unbounded processes as long as their absolute mean is finite.
</div>

<div class="glossary-entry">
<div class="gterm">Increment $\Delta M_n = M_n - M_{n-1}$ <span class="gcat cat-notn">Notation</span></div>
The change in the martingale from step $n-1$ to step $n$. For a martingale, $E[\Delta M_n \mid \mathcal{F}_{n-1}] = 0$ — increments have conditional mean zero given all past information. This is the one-step restatement of the martingale condition.
</div>

<div class="glossary-entry">
<div class="gterm">Predictable process (non-anticipating) <span class="gcat cat-defn">Definition</span></div>
A sequence $B_1, B_2, \ldots$ where $B_n$ is $\mathcal{F}_{n-1}$-measurable for every $n$. The bet at time $n$ can only use information strictly before time $n$. This is the key condition that prevents "cheating" in the discrete stochastic integral and ensures $W_n$ remains a martingale.
</div>

<div class="glossary-entry">
<div class="gterm">Discrete stochastic integral $W_n = \sum_{j=1}^n B_j \Delta M_j$ <span class="gcat cat-defn">Definition</span></div>
The cumulative winnings from applying a predictable betting strategy $\{B_j\}$ to a martingale $\{M_j\}$. When $B_j$ is predictable and bounded, $W_n$ is itself a martingale. This is the discrete-time prototype of the Itô integral $\int_0^t A_s \, dB_s$ in Chapter 3.
</div>

  </div>
</div>





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

| Symbol | Meaning |
|---|---|
| $$T$$ | A stopping time — a random time that depends only on past and present observations |
| $$\{T = n\} \in \mathcal{F}_n$$ | The defining measurability condition for a stopping time |
| $$n \wedge T$$ | $$\min\{n, T\}$$ — the process stopped at time $$T$$ |
| $$M_{n \wedge T}$$ | The stopped process — equals $$M_T$$ once $$T$$ is reached, stays there afterwards |
| $$E[M_T] = E[M_0]$$ | The optional sampling conclusion — martingale mean preserved at stopping time $$T$$ |
| $$P\{T \leq k\} = 1$$ | $$T$$ is bounded — the strongest assumption guaranteeing $$E[M_T] = E[M_0]$$ |
| $$P\{T < \infty\} = 1$$ | $$T$$ is almost surely finite — weaker condition, needs extra hypotheses |
| $$\mathbf{1}_{\{T > n\}}$$ | Indicator function equal 1 if $$T > n$$ and 0 if $$T < n$$|
| $$E[\lvert M_n \rvert \mathbf{1}_{\{T>n\}}] \to 0$$ | The uniform integrability condition in OST II |
| $$E[M_{n \wedge T}^2] \leq C$$ | The $$L^2$$ boundedness condition in OST III |
| $$S_n$$ | Simple symmetric random walk $$X_1 + \cdots + X_n$$ with $$P\{X_j = \pm 1\} = \tfrac{1}{2}$$ |

---

### Part 1 — The Core Intuition

<div class="note-abstract">
The Optional Sampling Theorem (OST) answers the question: <em>if you are allowed to stop a martingale at a random time of your choosing, can you change its expected value?</em> The answer is no — under appropriate conditions. This is the mathematical statement that you cannot beat a fair game even by choosing <em>when</em> to stop playing.
</div>

<b>CORE IDEAS</b>

<strong>Stopping a martingale produces another martingale.</strong> The stopped process $$Y_n = M_{n \wedge T}$$ is always a martingale, regardless of what the stopping time $$T$$ is.

<strong>$$E[M_T] = E[M_0]$$ requires extra conditions beyond just $$P\{T < \infty\} = 1$$.</strong> The stopped process has constant mean $$E[M_{n \wedge T}] = E[M_0]$$ for all finite $$n$$. Passing this to the limit $$n \to \infty$$ — to get $$E[M_T] = E[M_0]$$ — requires uniform integrability or $$L^2$$ boundedness.

<strong>The OST is a tool for computing probabilities and expectations.</strong> By choosing a clever stopping time $T$ and applying OST to two different martingales simultaneously — $$S_n$$ and $$S_n^2 - n$$ — one can extract exact formulas for hitting probabilities and expected hitting times. Examples 1.3.1 and 1.3.2 demonstrate this technique completely.

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

<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label"><b>Common Misconception</b></span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "Any random time $T$ with $P\{T < \infty\} = 1$ is a stopping time."</div>
  <div class="mc-correct"><strong>Correct:</strong> A random time is a stopping time only if the event $\{T = n\}$ is $\mathcal{F}_n$-measurable for every $n$ — it can only depend on the observations up to time $n$, not on future values. The condition $P\{T < \infty\} = 1$ is a statement about the distribution of $T$, not about its measurability structure.</div>
</div>

---

### Part 3 — The Stopped Process

Let $T$ be the <b>stopping time</b> for the betting strategy in §1.2. Then the winnings at time $t$ is

$$M_0 + \sum_{j=1}^n B_j [M_j - M_{j-1}],$$

where $$B_j = 1$$ if $$j \leq T$$ and $$B_j = 0$$ if $$j > T$$. We can write this as $$M_{n \wedge T}$$, where $$n \wedge T$$ is shorthand for $$\min\{n, T\}$$.

**The stopped process $$M_{n \wedge T}$$:** at time $n$, the process equals:
- $$M_n$$ if $$T > n$$ (we have not stopped yet),
- $$M_T$$ if $$T \leq n$$ (we have already stopped and the value is frozen at $$M_T$$).

Since $$B_j = \mathbf{1}_{\{j \leq T\}}$$ is predictable (it is $$\mathcal{F}_{j-1}$$-measurable because $$\{T \geq j\} \in \mathcal{F}_{j-1}$$), the discrete stochastic integral result from §1.2 immediately gives:

<div class="result-box">The stopped process $Y_n = M_{n \wedge T}$ is always a martingale with respect to $\{\mathcal{F}_n\}$. In particular, $E[M_{n \wedge T}] = E[M_0]$ for every finite $n$.</div>

---

### Part 4 — The Three Versions of the OST

<div class="example-block" markdown="1">
<div class="ex-title">Theorem 1.3.1 — OST I - Bounded Stopping Times<span class="ex-pill pill-thm">Theorem</span></div>

Suppose $$T$$ is a stopping time and $$M_n$$ is a martingale with respect to $$\{\mathcal{F}_n\}$$. Then $$Y_n = M_{n \wedge T}$$ is a martingale. In particular, for each $$n$$,

$$E[M_{n \wedge T}] = E[M_0].$$

If $$T$$ is bounded, that is, if there exists $$k < \infty$$ such that $$P\{T \leq k\} = 1$$, then

$$E[M_T] = E[M_0]. \tag{1.7}$$

**Why:** Since $$P\{T \leq k\} = 1$$, we have $$n \wedge T = T$$ for all $$n \geq k$$. Therefore $$E[M_{n \wedge T}] = E[M_T]$$ for $$n \geq k$$. Combined with $$E[M_{n \wedge T}] = E[M_0]$$ for all $$n$$, we get $$E[M_T] = E[M_0]$$.

**No extra conditions are needed** when $$T$$ is bounded — the martingale property of the stopped process is all that is required.
</div>

<div class="example-block" markdown="1">
<div class="ex-title" >Theorem 1.3.2 — OST II (a.s. finite $T$ with UI condition) <span class="ex-pill pill-thm">Theorem</span></div>

Suppose $$T$$ is a stopping time and $$M_n$$ is a martingale with respect to $$\{\mathcal{F}_n\}$$. Suppose that $$P\{T < \infty\} = 1$$, $$E[\lvert M_T \rvert] < \infty$$, and for each $$n$$,

$$\lim_{n \to \infty} E[\lvert M_n \rvert \mathbf{1}_{\{T > n\}}] = 0. \tag{1.8}$$

Then, $$E[M_T] = E[M_0]$$.

**Where the condition comes from:** For every finite $$n$$,

$$E[M_0] = E[M_{n \wedge T}] = E[M_T \mathbf{1}_{\{T \leq n\}}] + E[M_n \mathbf{1}_{\{T > n\}}].$$

As $$n \to \infty$$, the first term converges to $$E[M_T]$$. The second term vanishes by condition (1.8). Hence $$E[M_0] = E[M_T]$$.

**Condition (1.8) in plain English:** The contribution to the expected value from paths that have not yet stopped by time $$n$$ must vanish as $$n \to \infty$$. Paths that take very long to stop and reach very large values can violate this.

**The doubling strategy fails here:** In Example 1.2.4, if $$T = \min\{n : W_n = 1\}$$, then $$P\{T < \infty\} = 1$$ but $$E[\lvert W_n \rvert \mathbf{1}_{\{T > n\}}] = (2^n - 1) \cdot 2^{-n} \to 1 \neq 0$$. Condition (1.8) is violated, consistently with $$E[W_T] = 1 \neq 0 = E[W_0]$$.
</div>

<div class="example-block" markdown="1">
<div class="ex-title" >Theorem 1.3.3 — OST III ($L^2$ bounded stopped process) <span class="ex-pill pill-thm">Theorem</span></div>

Suppose $$T$$ is a stopping time and $$M_n$$ is a martingale with respect to $$\{\mathcal{F}_n\}$$. Suppose that $$P\{T < \infty\} = 1$$, $$E[\lvert M_T \rvert] < \infty$$, and that there exists $$C < \infty$$ such that for each $$n$$,

$$E[M_{n \wedge T}^2] \leq C. \tag{1.9}$$

Then, $$E[M_T] = E[M_0]$$.

**Why (1.9) implies (1.8) — the key argument:**

For any $$b > 0$$, split the expectation:

$$E[\lvert M_n \rvert \mathbf{1}_{\{T > n\}}] = E[\lvert M_n \rvert \mathbf{1}_{\{T > n,\, \lvert M_n \rvert \geq b\}}] + E[\lvert M_n \rvert \mathbf{1}_{\{T > n,\, \lvert M_n \rvert < b\}}].$$

- **First term:** By the H ̈older inequality and (1.9), $$E[\lvert M_n \rvert \mathbf{1}_{\{\lvert M_n \rvert \geq b,\, T > n\}}] \leq \frac{C}{b}$$.
- **Second term:** $$E[\lvert M_n \rvert \mathbf{1}_{\{T > n,\, \lvert M_n \rvert < b\}}] \leq b \cdot P\{T > n\} \to 0$$ since $$P\{T < \infty\} = 1$$.

Therefore $$\limsup_{n \to \infty} E[\lvert M_n \rvert \mathbf{1}_{\{T > n\}}] \leq C/b$$ for every $$b > 0$$, so the limit is $$0$$.

**Practical value:** Condition (1.9) is often easier to verify than (1.8) directly — it suffices to bound the second moment of the stopped process uniformly in $$n$$.
</div>

#### Summary — Three OST Versions

| Version | Assumption on $T$ | Extra condition | Conclusion |
|---|---|---|---|
| **OST I** | $$P\{T \leq k\} = 1$$ (bounded) | None | $$E[M_T] = E[M_0]$$ |
| **OST II** | $$P\{T < \infty\} = 1$$ | $$E[M_{n}\mathbf{1}_{\{T>n\}}] \to 0$$ | $$E[M_T] = E[M_0]$$ |
| **OST III** | $$P\{T < \infty\} = 1$$ | $$E[M_{n \wedge T}^2] \leq C < \infty$$ | $$E[M_T] = E[M_0]$$ |

---

### Part 5 — Worked Examples

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.3.1 — Gambler's ruin: hitting probability for random walk <span class="ex-pill pill-ex">Example</span></div>

Gambler's ruin for random walk. Let $$X_1, X_2, \ldots$$ be independent, coin-tosses as in (1.6) and let $$S_n = 1 + X_1 + \cdots + X_n$$. $S_n$ is called simple (symmetric) random walk starting at 1. … Let $$K > 1$$ be a positive integer and let $T$ denote the first time $n$ such that $$S_n = 0$$ or $$S_n = K$$.

**Setup:**
- $$S_n$$ is a martingale (zero-mean increments, §1.2 Example 1.2.1).
- $$T = \min\{n : S_n = 0 \text{ or } S_n = K\}$$ is a stopping time.
- $$S_n$$ stays in $$[0, K]$$ for all $$n \leq T$$, so $$0 \leq M_{n \wedge T} \leq K$$ — the stopped process is bounded.
- Therefore (1.9) holds with $$C = K^2$$, and OST III applies.

**Apply OST to $$S_n$$:**

$$1 = E[S_0] = E[S_T] = 0 \cdot P\{S_T = 0\} + K \cdot P\{S_T = K\}.$$

Solving:

$$\boxed{P\{S_T = K\} = \frac{1}{K}, \qquad P\{S_T = 0\} = \frac{K-1}{K}.}$$

**Interpretation:** Starting at 1, with a fair game, the probability of reaching $$K$$ before 0 is $$1/K$$. As $$K \to \infty$$, $$P\{S_T = K\} \to 0$$: a gambler with <span>$1</span> playing against a casino with <span>$K</span> almost surely goes broke. This is the **gambler's ruin estimate**.

<div class="ex-lesson"><strong>Key technique:</strong> The OST converts a martingale identity ($E[S_T] = E[S_0]$) into a linear equation in the unknown probability $P\{S_T = K\}$. The bounded stopping time (or $L^2$ bound) is what justifies passing the martingale identity through to time $T$.</div>
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.3.2 — Expected hitting time via the $S_n^2 - n$ martingale <span class="ex-pill pill-ex">Example</span></div>

Let $$S_n = X_1 + \cdots + X_n$$ be simple random walk starting at 0. We have seen that $$M_n = S_n^2 - n$$ is a martingale. Let $$J, K$$ be positive integers and let $$T = \min\{n : S_n = -J \text{ or } S_n = K\}$$.

**Step 1 — Find $$P\{S_T = K\}$$ using $$S_n$$:**

Apply OST to $$S_n$$ (same argument as Example 1.3.1, starting at 0):

$$0 = E[S_T] = (-J) P\{S_T = -J\} + K \cdot P\{S_T = K\}.$$

$$\boxed{P\{S_T = K\} = \frac{J}{J+K}, \qquad P\{S_T = -J\} = \frac{K}{J+K}.}$$

**Step 2 — Find $$E[T]$$ using $$M_n = S_n^2 - n$$:**

Exercise 1.13 establishes that $$E[M_{n \wedge T}^2] \leq C < \infty$$, so OST III applies to $$M_n$$:

$$E[M_T] = E[M_0] \implies E[S_T^2] - E[T] = 0 \implies E[T] = E[S_T^2].$$

Compute $$E[S_T^2]$$ directly:

$$
\begin{aligned}
E[S_T^2] = J^2 P\{S_T = -J\} + K^2 P\{S_T = K\}
&= J^2 \cdot \frac{K}{J+K} + K^2 \cdot \frac{J}{J+K} \\
&= \frac{JK(J+K)}{J+K} = JK.
\end{aligned}
$$

$$\boxed{E[T] = JK.}$$

**Interpretation:** The expected time for symmetric random walk to exit $$(-J, K)$$ starting from 0 is exactly $$JK$$. In particular, to travel distance $$$K$$ from the origin in either direction, the expected time is $$K^2$$ (set $$J = K$$).
</div>

<div class="example-block" markdown="1">
<div class="ex-title">Example 1.3.3 — OST fails: $P\{T < \infty\} = 1$ but $E[S_0] \neq E[S_T]$ <span class="ex-pill pill-warn">Counterexample</span></div>

As in Example 1.3.2, let $$S_n = X_1 + \cdots + X_n$$ be simple random walk starting at 0. Let $$T = \min\{n : S_n = 1\}$$.

**$$P\{T < \infty\} = 1$$:** From Example 1.3.2, Probility random walk hits 1 before $$-J$$ $$P\{S_T = 1\}= J/(J+1) \to 1$$ as $$J \to \infty$$. So with probability one the walk reaches 1.

**But $$E[T] = \infty$$:** From Example 1.3.2, the expected time to exit $$(-J, 1)$$ starting at 0 is $$J \cdot 1 = J$$. Since this holds for all $$J$$ and $$T \geq T_J$$ (where $$T_J$$ is the exit time from $$(-J,1)$$), we have $$E[T] \geq J$$ for all $$J$$, so $$E[T] = \infty$$.

**OST fails:** $$S_T = 1$$ almost surely, so $$E[S_T] = 1 \neq 0 = E[S_0]$$.

**Why:** Neither condition (1.8) nor (1.9) holds for this $$T$$. In particular, $$E[M_{n \wedge T}^2] = E[S_{n \wedge T}^2] \to \infty$$ as $$n \to \infty$$, violating (1.9).

<div class="ex-lesson"><strong>Key lesson:</strong> $P\{T < \infty\} = 1$ is not sufficient on its own. An infinite expected stopping time ($E[T] = \infty$) is a warning sign that the extra conditions of OST II or III may fail. Always verify one of the three conditions before applying OST.</div>
</div>

---

### Part 6 — Why the Doubling Strategy Does Not Contradict OST

The martingale betting strategy from §1.2 Example 1.2.4 has:
- $$W_n$$ is a martingale for every finite $$n$$, so $$E[W_n] = 0$$.
- $$T = \min\{n : W_n = 1\}$$ satisfies $$P\{T < \infty\} = 1$$.
- $$W_T = 1$$, so $$E[W_T] = 1 \neq 0 = E[W_0]$$.

**Checking that OST conditions fail:**

$$E[\lvert W_n \rvert \mathbf{1}_{\{T > n\}}] = (2^n - 1) \cdot 2^{-n} \to 1 \neq 0,$$

so condition (1.8) is violated. Since $$E[W_{n \wedge T}^2] \to \infty$$ as well, condition (1.9) also fails. And $$T$$ is clearly unbounded. All three OST conditions fail, consistently with $$E[W_T] \neq E[W_0]$$.

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


### Part 4 — Pólya's Urn

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

### Part 5 — Connection to Bayesian Statistics

<div class="note-abstract">
Pólya's urn is not merely a toy model — it is exactly the Bayesian update rule for a Bernoulli parameter $\theta$ with a uniform prior. The MCT, reinterpreted, is a Bayesian consistency theorem: the posterior mean converges a.s. to the true $\theta$ as data accumulates.
</div>

**Setup:** Run Bernoulli trials with unknown success probability $$\theta$$, starting from a $$\mathrm{Uniform}[0,1]$$ prior. After $$n$$ trials with $$S_n = k$$ successes, the Bayes update gives the posterior:

$$f_{n,k}(\theta) \propto \theta^k (1-\theta)^{n-k}, \quad \theta \in (0,1).$$

This is the $$\mathrm{Beta}(k+1,\, n-k+1)$$ density, with posterior mean:

$$E[\theta \mid S_n = k] = \frac{k+1}{n+2} = \frac{S_n + 1}{n+2}.$$

This is **identical to the Pólya urn fraction** $$M_n = R_n/(n+2)$$ when $$R_n = S_n + 1$$ (successes plus the one initial red ball). The urn fraction equals the posterior mean at every step.

**MCT as Bayesian law of large numbers:** By the strong law, $$S_n/n \to \theta$$ a.s. Combined with $$M_n \to M_\infty$$ a.s., we get $$M_\infty = \theta$$ a.s. — the posterior mean converges to the true parameter.

---

### Part 6 — MCT vs OST: Complementary Tools

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

  </div>
</div>



