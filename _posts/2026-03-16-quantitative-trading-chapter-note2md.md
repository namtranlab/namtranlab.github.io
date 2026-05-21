---
layout: distill
title: "Stochastic Calculus — Study Notes"
description: Study notes for Lawler Stochastic Calculus (Chapter 1).
tags: Stochastic Calculus
giscus_comments: true
date: 2026-03-24
featured: true
thumbnail: https://m.media-amazon.com/images/I/51s4givoDeL._SY445_SX342_ML2_.jpg

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
        <div class="chapter-subtitle">The foundational tool underlying every concept in this book — probability-space setup, the definition and properties of E[Y | F_n]</div>
      </div>
    </div>
    <span class="chapter-arrow" id="s11-arrow">▼</span>
  </button>
  <div class="chapter-body" id="s11-body" markdown="1">

<!-- ══════════════════════════════════════
     CHANGE 1 — Notation-at-a-glance panel
     ══════════════════════════════════════ -->

<div class="notation-panel">
<div class="np-title">§ 1.1 — Notation at a Glance</div>

| Symbol | Reads as | Meaning |
|---|---|---|
| Ω | "Omega" | Sample space — the set of all possible outcomes |
| F | "script F" | σ-algebra — the collection of all observable events |
| P | | Probability measure — assigns numbers in [0,1] to events in F |
| (Ω, F, P) | | Probability space — the full mathematical arena |
| A ∈ F | "A is in F" | A is a measurable event (we can assign it a probability) |
| Ω \ A | "Omega minus A" | Complement of A — all outcomes not in A |
| F_n | "F sub n" | σ-algebra generated by X₁,…,Xₙ — information at time n |
| F_m ⊆ F_n | "F_m contained in F_n" | All events knowable at time m are also knowable at time n |
| E[Y] | | Unconditional expectation — best guess for Y with no information |
| E[Y \| F_n] | "E of Y given F_n" | Conditional expectation — best guess for Y given information F_n |
| 1_A | "indicator of A" | Function equal to 1 on event A, 0 elsewhere |
| i.i.d. | | Independent and identically distributed |
| μ ≪ P | "mu absolutely continuous w.r.t. P" | Every P-null set is also a μ-null set |
| S_n | | Partial sum X₁ + X₂ + ⋯ + Xₙ |

</div>

---

### Part 1 — The Core Intuition

<div class="note-abstract">
Conditional expectation is the central object of stochastic calculus. Every concept in this book — martingales, Itô integrals, Girsanov's theorem — is built on it. At its core it answers one question: <em>given that we have observed some (but not all) information, what is our best guess for a random variable Y?</em> The answer is not a single number but another random variable — one that changes as our information changes.
</div>

#### Core ideas

<div class="key-idea"><strong>E[X] is the best guess for X given no information at all.</strong> The unconditional expectation is the baseline: if you know nothing about the outcome of an experiment, your single best guess (in the mean-squared-error sense) is E[X].</div>

<div class="key-idea"><strong>E[Y | F_n] is the best guess for Y given the information F_n.</strong> As data arrives one variable at a time — X₁, X₂, …, Xₙ — we collect more information. The conditional expectation updates our best guess for Y using whatever is currently known.</div>

<div class="key-idea"><strong>E[Y | F_n] is itself a random variable, not a fixed number.</strong> Because it depends on the observed values of X₁, …, Xₙ — which are random — it is a function of those observations, hence random. This is the single most important conceptual shift from undergraduate probability.</div>

<div class="key-idea"><strong>The formal definition bypasses explicit computation via one key property.</strong> Rather than defining E[Y | F_n] by a formula, Lawler defines it as the unique F_n-measurable random variable satisfying E[E[Y | F_n] · 1_A] = E[Y · 1_A] for all F_n-measurable events A. All other properties follow from this.</div>

<!-- CHANGE 3 — Misconception block immediately after the key idea it targets -->
<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label">Common Misconception</span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "E[Y | F_n] is just a number, like E[Y] but computed with less data."</div>
  <div class="mc-correct"><strong>Correct:</strong> E[Y | F_n] is a <em>random variable</em>. Its value changes depending on which values X₁, …, Xₙ take. If you observe different data, you get a different conditional expectation. E[Y] is the special case where zero data is observed — a single fixed number. E[Y | F_n] is a whole function of the observations.</div>
</div>

---

### Part 2 — The Probability Space

<div class="note-abstract">
Before defining conditional expectation rigorously, we need the underlying mathematical arena: a probability space (Ω, F, P). Everything — random variables, events, filtrations — lives inside this structure.
</div>

<div class="orig-quote">"We assume that the random variables Y, X₁, X₂, … are defined on a probability space (Ω, F, P). Here F is a σ-algebra or σ-field of subsets of Ω, that is, a collection of subsets satisfying: ∅ ∈ F; A ∈ F implies Ω \ A ∈ F; A₁, A₂, … ∈ F implies ⋃_{n=1}^∞ Aₙ ∈ F."</div>
<div class="quote-explain">This defines the three σ-algebra axioms. (i) The empty set — the impossible event — must be an event. (ii) If A is observable, so is its complement: "A did not happen" must also be observable. (iii) Countable unions of events are events: "at least one of A₁, A₂, … happened" is observable. These three rules make F a self-consistent collection of questions we can ask about the experiment.</div>

#### What is a σ-algebra? — Concrete example

<div class="example-block">
<div class="ex-title">Minimal example: two fair coin flips <span class="ex-pill pill-ex">Example</span></div>

**Sample space:** Ω = {HH, HT, TH, TT}

**The full σ-algebra** F = 2^Ω contains all 16 subsets. This always satisfies all three axioms and encodes complete information.

**A smaller valid σ-algebra** encoding only the first flip:

F₁ = { ∅, &nbsp; {HH, HT}, &nbsp; {TH, TT}, &nbsp; Ω }

- ∅ ∈ F₁ ✓ &emsp;(axiom i)
- {HH,HT}ᶜ = {TH,TT} ∈ F₁ ✓ &emsp;(axiom ii)
- Any union of these four sets stays in F₁ ✓ &emsp;(axiom iii)

F₁ lets us distinguish "first flip = H" from "first flip = T" — nothing more.

<div class="ex-lesson"><strong>Key point:</strong> A σ-algebra is a mathematical encoding of a state of knowledge. Larger σ-algebra = more information. F₁ ⊆ 2^Ω reflects that knowing one flip is strictly less information than knowing both.</div>
</div>

---

### Part 3 — The Filtration

<div class="note-abstract">
A filtration is a growing sequence of σ-algebras modelling information accumulating over time. At time n, F_n records everything observed up to time n — and once something is known it is never forgotten.
</div>

<div class="orig-quote">"Let X₁, X₂, … be random variables which we think of as a time series with the data arriving one at a time. At time n we have viewed the values X₁, …, Xₙ. … We will write F_n for 'the information contained in X₁, …, Xₙ'."</div>
<div class="quote-explain">F_n is not a number or a random variable — it is a σ-algebra: a collection of events. "Information in X₁,…,Xₙ" means all questions of the form "did the observations satisfy some condition?" that can be answered once X₁,…,Xₙ are known.</div>

<div class="orig-quote">"The information F_n is the smallest sub σ-algebra G of F such that X₁, …, Xₙ are G-measurable. The latter statement means that for all t ∈ ℝ, the event {X_j ≤ t} ∈ F_n."</div>
<div class="quote-explain">"X_j is F_n-measurable" means: for every threshold t, the set of outcomes where X_j ≤ t is an event in F_n. Knowing X₁,…,Xₙ is enough to determine X_j. The word "smallest" is important — we take only events genuinely required to describe X₁,…,Xₙ, not any extras.</div>

<!-- CHANGE 3 — Misconception block for measurability -->
<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label">Common Misconception</span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "X is F_n-measurable just means X is one of the variables X₁,…,Xₙ."</div>
  <div class="mc-correct"><strong>Correct:</strong> Any function of X₁,…,Xₙ is also F_n-measurable — e.g., X₁ + X₂, max(X₁,…,Xₙ), or S_n². The condition is that X's value is fully determined once X₁,…,Xₙ are known, not that X appears explicitly in the list.</div>
</div>

<div class="example-block">
<div class="ex-title">Filtration on two coin flips <span class="ex-pill pill-ex">Example</span></div>

Ω = {HH, HT, TH, TT}. Let X₁ = result of flip 1 (H=1, T=0), X₂ = result of flip 2.

**F₀** = {∅, Ω} — no observation; we cannot distinguish any outcomes.

**F₁** = σ(X₁) = {∅, {HH,HT}, {TH,TT}, Ω} — we see flip 1 only.

**F₂** = σ(X₁, X₂) = 2^Ω — we see both flips; every subset is distinguishable.

The chain: **F₀ ⊆ F₁ ⊆ F₂** — information never shrinks.

<div class="ex-lesson"><strong>Key point:</strong> F_n is the mathematical formalisation of "what we know at time n." The filtration (F₀, F₁, F₂, …) models how knowledge accumulates step by step.</div>
</div>

---

### Part 4 — Motivating the Definition (Density Case)

<div class="note-abstract">
Before giving the abstract definition, Lawler derives it in the familiar setting of joint densities. This motivates why the abstract definition takes the form it does.
</div>

<div class="orig-quote">"Suppose that (X, Y) have a joint density f(x, y), 0 &lt; x, y &lt; ∞, with marginal densities f(x) = ∫ f(x,y)dy, g(y) = ∫ f(x,y)dx. The conditional density f(y|x) is defined by f(y|x) = f(x,y)/f(x)."</div>
<div class="quote-explain">f(x,y) is the joint probability density near (x,y). f(x) is the marginal density of X — the probability near x regardless of Y, obtained by integrating out all y-values. f(y|x) is the relative weight on each y-value given X = x. Division by f(x) normalises so that f(y|x) integrates to 1 over y.</div>

This gives the familiar undergraduate formula:

$$E[Y \mid X = x] = \int_{-\infty}^{\infty} y\, f(y \mid x)\, dy = \frac{\int_{-\infty}^{\infty} y\, f(x,y)\, dy}{f(x)}$$

<div class="orig-quote">"Note that E[Y | X] is a random variable which is determined by the value of the random variable X."</div>
<div class="quote-explain">E[Y | X = x] for a fixed x is a number. But E[Y | X] — without fixing x — is a function of X. Since X is random, this function is itself random. This is the key conceptual leap the formal definition must capture.</div>

**The tower property emerges naturally:**

$$E\bigl[E[Y \mid X]\bigr] = \int_{-\infty}^{\infty} E[Y \mid X = x]\, f(x)\, dx = \iint y\, f(x,y)\, dy\, dx = E[Y]$$

Averaging the conditional best-guess over all possible observations recovers the unconditional expectation. This is the **tower property**, generalised by the abstract definition below.

---

### Part 5 — The Formal Definition

<div class="example-block">
<div class="ex-title">Definition — Conditional Expectation E[Y | F_n] <span class="ex-pill pill-defn">Definition</span></div>

<div class="orig-quote">"The conditional expectation E[Y | F_n] is the unique random variable satisfying the following. (i) E[Y | F_n] is F_n-measurable. (ii) For every F_n-measurable event A, E[E[Y | F_n] · 1_A] = E[Y · 1_A]."</div>
<div class="quote-explain">Condition (i): the output is computable from X₁,…,Xₙ alone — it cannot use future information. Condition (ii): on every slice of Ω that can be identified from current information (any A ∈ F_n), the average of E[Y|F_n] over that slice equals the average of Y over the same slice. These two conditions uniquely determine E[Y|F_n] without requiring a closed-form formula.</div>

**What is 1_A?**

$$\mathbf{1}_A(\omega) = \begin{cases} 1 & \text{if } \omega \in A \\ 0 & \text{if } \omega \notin A \end{cases}$$

So E[Z · 1_A] = probability-weighted average of Z over outcomes where A occurs = ∫_A Z dP.

**Why not give an explicit formula?** In general probability spaces (uncountable Ω, continuous distributions), no single formula works universally. The two-condition characterisation is both sufficient and rigorous. Existence follows from the Radon-Nikodym theorem; uniqueness from: if Z₁ and Z₂ both satisfy the conditions then E[(Z₁ − Z₂)²] = 0, so Z₁ = Z₂ almost surely.
</div>

<!-- CHANGE 3 — Misconception block for the definition -->
<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label">Common Misconception</span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "Condition (ii) E[E[Y|F_n]·1_A] = E[Y·1_A] is just saying E[Y|F_n] = Y."</div>
  <div class="mc-correct"><strong>Correct:</strong> It says they agree <em>on average over every observable event A</em> — not pointwise. E[Y|F_n] is a smoothed version of Y: it preserves the same probability mass on every F_n-identifiable slice, but replaces Y's within-slice variation with a single average value. The pointwise equality E[Y|F_n](ω) = Y(ω) only holds when Y is itself F_n-measurable (Property 1).</div>
</div>

---

### Part 6 — Properties of Conditional Expectation

<div class="example-block">
<div class="ex-title">Proposition 1.1.1 — Five key properties <span class="ex-pill pill-prop">Proposition</span></div>

<div class="orig-quote">"Proposition 1.1.1. Suppose X₁, X₂, … is a sequence of random variables and F_n denotes the information at time n. The conditional expectation E[Y | F_n] satisfies the following properties."</div>
<div class="quote-explain">All five properties are consequences of the two defining conditions — not additional assumptions. Lawler proves linearity and the constants rule explicitly in the text; the others follow by analogous arguments using the definition.</div>

---

**Property 1 — If Y is already known, conditioning changes nothing**

$$\text{If } Y \text{ is } \mathcal{F}_n\text{-measurable}, \quad E[Y \mid \mathcal{F}_n] = Y.$$

*Why:* Y is determined by X₁,…,Xₙ. No uncertainty remains — the best guess is the value itself.

---

**Property 2 — Tower property (law of iterated expectations)**

$$m < n \implies E\bigl[\,E[Y \mid \mathcal{F}_n]\;\big|\;\mathcal{F}_m\bigr] = E[Y \mid \mathcal{F}_m].$$

*Plain English:* Compute the best guess for Y using information up to time n, then downgrade it to only use information up to time m < n. The result is identical to computing the best guess with time-m information directly. The outer (coarser) conditioning always governs the answer.

Special case m = 0: **E[E[Y | F_n]] = E[Y]**.

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

*Why:* Z is already determined by current information — it plays the role of a known constant. Only Y carries residual randomness to average over. *Example:* E[X₁·Y | F₁] = X₁·E[Y | F₁].
</div>

<!-- CHANGE 3 — Misconception block for the tower property -->
<div class="misconception-block">
  <div class="mc-header"><span class="mc-icon">⚠️</span><span class="mc-label">Common Misconception — Tower Property</span></div>
  <div class="mc-wrong"><strong>Wrong:</strong> "E[E[Y|F_n]|F_m] = E[Y|F_n] — the inner conditioning dominates because it has more information."</div>
  <div class="mc-correct"><strong>Correct:</strong> The <em>outer</em> conditioning dominates: the result is E[Y|F_m]. When you condition on less information (F_m ⊆ F_n), you lose the fine detail provided by F_n. The coarser σ-algebra always wins. Think of it as: the final answer can only use what the outermost conditioning permits.</div>
</div>

---

### Part 7 — Worked Examples

<div class="example-block">
<div class="ex-title">Example 1.1.1 — E[S_n | F_m] for independent increments <span class="ex-pill pill-ex">Example</span></div>

**Setup:** X₁, X₂, … independent with E[X_j] = μ. Let S_n = X₁ + ⋯ + Xₙ, F_m = σ(X₁,…,X_m), m < n.

<!-- CHANGE 2 — Proof-step component -->
<div class="proof-steps">
<div class="ps-title">Step-by-step derivation</div>

<div class="proof-step">
  <div class="ps-num">1</div>
  <div class="ps-body">
    Split S_n at time m using linearity of conditional expectation:
    <span class="ps-eq">E[S_n | F_m] = E[S_m | F_m] + E[S_n − S_m | F_m]</span>
  </div>
  <div class="ps-why">Property 4 — Linearity</div>
</div>

<div class="proof-step">
  <div class="ps-num">2</div>
  <div class="ps-body">
    First term: S_m = X₁+⋯+X_m is fully determined by X₁,…,X_m, so it is F_m-measurable:
    <span class="ps-eq">E[S_m | F_m] = S_m</span>
  </div>
  <div class="ps-why">Property 1 — Known Y</div>
</div>

<div class="proof-step">
  <div class="ps-num">3</div>
  <div class="ps-body">
    Second term: S_n − S_m = X_{m+1}+⋯+X_n depends only on future variables, independent of F_m:
    <span class="ps-eq">E[S_n − S_m | F_m] = E[S_n − S_m] = (n−m)μ</span>
  </div>
  <div class="ps-why">Property 3 — Independence</div>
</div>

<div class="proof-step">
  <div class="ps-num">4</div>
  <div class="ps-body">
    Combine Steps 2 and 3:
    <span class="ps-eq">E[S_n | F_m] = S_m + (n−m)μ</span>
    Given observations up to time m, the best guess for S_n is the current sum plus (n−m) expected future increments.
  </div>
  <div class="ps-why">Result</div>
</div>

</div>

<div class="ex-lesson"><strong>Why this matters:</strong> When μ = 0 the result becomes E[S_n | F_m] = S_m — the current sum is the best guess for all future sums. This is exactly the martingale property defined in §1.2.</div>
</div>

<div class="example-block">
<div class="ex-title">Example 1.1.2 — E[S_n² | F_m] for zero-mean increments <span class="ex-pill pill-ex">Example</span></div>

**Setup:** μ = 0, E[X_j²] = σ² < ∞. Same S_n, F_m as above.

<div class="proof-steps">
<div class="ps-title">Step-by-step derivation</div>

<div class="proof-step">
  <div class="ps-num">1</div>
  <div class="ps-body">
    Write S_n = S_m + (S_n − S_m) and expand the square:
    <span class="ps-eq">E[S_n² | F_m] = E[S_m² | F_m] + 2 E[S_m(S_n−S_m) | F_m] + E[(S_n−S_m)² | F_m]</span>
  </div>
  <div class="ps-why">Property 4 — Linearity</div>
</div>

<div class="proof-step">
  <div class="ps-num">2</div>
  <div class="ps-body">
    Term 1: S_m² is F_m-measurable:
    <span class="ps-eq">E[S_m² | F_m] = S_m²</span>
  </div>
  <div class="ps-why">Property 1</div>
</div>

<div class="proof-step">
  <div class="ps-num">3</div>
  <div class="ps-body">
    Term 2: S_m pulls out (F_m-measurable); S_n−S_m is independent of F_m with mean 0:
    <span class="ps-eq">2 E[S_m(S_n−S_m) | F_m] = 2 S_m · E[S_n−S_m] = 2 S_m · 0 = 0</span>
  </div>
  <div class="ps-why">Properties 5 + 3</div>
</div>

<div class="proof-step">
  <div class="ps-num">4</div>
  <div class="ps-body">
    Term 3: (S_n−S_m)² is independent of F_m; its expectation is the variance of (n−m) increments:
    <span class="ps-eq">E[(S_n−S_m)² | F_m] = Var(S_n−S_m) = (n−m)σ²</span>
  </div>
  <div class="ps-why">Property 3</div>
</div>

<div class="proof-step">
  <div class="ps-num">5</div>
  <div class="ps-body">
    Combine Terms 1, 2, 3:
    <span class="ps-eq">E[S_n² | F_m] = S_m² + (n−m)σ²</span>
  </div>
  <div class="ps-why">Result</div>
</div>

</div>

<div class="ex-lesson"><strong>Why this matters:</strong> The process M_n = S_n² − nσ² is a martingale — this computation is the exact verification. It also shows that S_n² grows on average by σ² per step, connecting to the quadratic variation of random walk.</div>
</div>

<div class="example-block">
<div class="ex-title">Example 1.1.3 — E[X₁ | S_n]: conditioning on a coarser statistic <span class="ex-pill pill-ex">Example</span></div>

**Setup:** X₁,…,X_n i.i.d. We observe only S_n = X₁+⋯+X_n. Goal: compute E[X₁ | S_n].

<div class="proof-steps">
<div class="ps-title">Step-by-step derivation</div>

<div class="proof-step">
  <div class="ps-num">1</div>
  <div class="ps-body">
    Since X₁,…,X_n are i.i.d., conditioning on S_n treats every index symmetrically — no single component is favoured:
    <span class="ps-eq">E[X₁ | S_n] = E[X₂ | S_n] = ⋯ = E[X_n | S_n]</span>
  </div>
  <div class="ps-why">Symmetry of i.i.d.</div>
</div>

<div class="proof-step">
  <div class="ps-num">2</div>
  <div class="ps-body">
    Sum both sides over j = 1,…,n and apply linearity. Since S_n is σ(S_n)-measurable (already known), E[S_n | S_n] = S_n:
    <span class="ps-eq">n · E[X₁ | S_n] = E[X₁+⋯+X_n | S_n] = E[S_n | S_n] = S_n</span>
  </div>
  <div class="ps-why">Properties 4 + 1</div>
</div>

<div class="proof-step">
  <div class="ps-num">3</div>
  <div class="ps-body">
    Divide both sides by n:
    <span class="ps-eq">E[X₁ | S_n] = S_n / n</span>
    Given only the total sum, the best guess for any single component is an equal share.
  </div>
  <div class="ps-why">Result</div>
</div>

</div>

*Interpretation:* The answer does not depend on E[X₁] — counterintuitive but correct, because S_n already encodes all aggregate information and symmetry forces equal attribution.

<div class="warning-box"><strong>⚠️ Subtle point:</strong> Conditioning on S_n is strictly coarser than conditioning on all of X₁,…,X_n. The σ-algebra σ(S_n) ⊆ F_n. With less information our best guess for X₁ worsens: from knowing X₁ exactly (under F_n) to knowing only S_n/n (under σ(S_n)).</div>
</div>

---

### Part 8 — Filtration (Formal Definition)

<div class="example-block">
<div class="ex-title">Definition — Discrete-time filtration <span class="ex-pill pill-defn">Definition</span></div>

<div class="orig-quote">"Definition If X₁, X₂, … is a sequence of random variables, then the associated (discrete time) filtration is the collection {F_n} where F_n denotes the information in X₁, …, X_n. One assumption in the definition of a filtration, which may sometimes not reflect reality, is that information is never lost. If m &lt; n, then everything known at time m is still known at time n."</div>
<div class="quote-explain">The key mathematical consequence of "information is never lost" is the set inclusion F_m ⊆ F_n for all m &lt; n. Every event in F_m is also in F_n. This is not a philosophical claim — it is a precise constraint that the sequence of σ-algebras must satisfy to qualify as a filtration.</div>

**Formally:** A filtration is an increasing sequence of σ-algebras:

$$\mathcal{F}_0 \subseteq \mathcal{F}_1 \subseteq \mathcal{F}_2 \subseteq \cdots \subseteq \mathcal{F}$$

**F₀ = {∅, Ω}** — the trivial σ-algebra, representing the state before any observation.
</div>

---

### Property Summary Table

| Property | Formula | Plain English | Proved via |
|---|---|---|---|
| **Known Y** | E[Y\|F_n] = Y if Y is F_n-meas. | No uncertainty → best guess is the value itself | Definition — condition (i) |
| **Tower** | E[E[Y\|F_n]\|F_m] = E[Y\|F_m], m < n | Outer (coarser) conditioning always governs | Definition — condition (ii) + F_m ⊆ F_n |
| **Independence** | E[Y\|F_n] = E[Y] if X₁,…,Xₙ ⊥ Y | Irrelevant data leaves best guess unchanged | Definition — condition (ii) |
| **Linearity** | E[aY+bZ\|F_n] = aE[Y\|F_n]+bE[Z\|F_n] | Cond. expectation is a linear integral | Linearity of E[·] + uniqueness |
| **Constants pull out** | E[YZ\|F_n] = Z·E[Y\|F_n] if Z F_n-meas. | Known quantities act as constants | Proved for 1_A, extended by MCT |

---

### Term Glossary

<div class="glossary-entry">
<div class="gterm">Probability space (Ω, F, P) <span class="gcat cat-defn">Definition</span></div>
The triple: Ω = sample space (all outcomes); F = σ-algebra (observable events); P : F → [0,1] probability measure with P(Ω) = 1 and countable additivity. All random variables and stochastic processes in this book live on such a triple.
</div>

<div class="glossary-entry">
<div class="gterm">σ-algebra <span class="gcat cat-defn">Definition</span></div>
A collection F of subsets of Ω closed under complementation and countable unions, containing ∅. Encodes "which events are distinguishable." The trivial σ-algebra {∅, Ω} encodes no information; the power set 2^Ω encodes complete information.
</div>

<div class="glossary-entry">
<div class="gterm">Filtration {F_n} <span class="gcat cat-defn">Definition</span></div>
An increasing sequence F₀ ⊆ F₁ ⊆ F₂ ⊆ ⋯ modelling accumulating information. F_n = σ(X₁,…,Xₙ) — the smallest σ-algebra making X₁,…,Xₙ measurable. Information never shrinks: m < n implies F_m ⊆ F_n.
</div>

<div class="glossary-entry">
<div class="gterm">F_n-measurable <span class="gcat cat-meas">Measurability</span></div>
A random variable Z is F_n-measurable if {Z ≤ t} ∈ F_n for every t ∈ ℝ. Equivalently: Z = φ(X₁,…,Xₙ) for some measurable φ. Z's value is fully determined by the first n observations.
</div>

<div class="glossary-entry">
<div class="gterm">Conditional expectation E[Y | F_n] <span class="gcat cat-defn">Definition</span></div>
The unique F_n-measurable random variable satisfying E[E[Y|F_n]·1_A] = E[Y·1_A] for all A ∈ F_n. The minimum-MSE predictor of Y given information F_n. A random variable — not a number — because its value depends on the observations X₁,…,Xₙ.
</div>

<div class="glossary-entry">
<div class="gterm">Indicator function 1_A <span class="gcat cat-notn">Notation</span></div>
1_A(ω) = 1 if ω ∈ A, else 0. So E[Z·1_A] = ∫_A Z dP = the probability-weighted average of Z over outcomes where A occurs. Central to the formal two-condition definition of conditional expectation.
</div>

<div class="glossary-entry">
<div class="gterm">Tower property <span class="gcat cat-prop">Property</span></div>
E[E[Y|F_n]|F_m] = E[Y|F_m] for m < n. The outer (coarser) conditioning always governs. Special case: E[E[Y|F_n]] = E[Y]. Proved using the defining property of conditional expectation and the inclusion F_m ⊆ F_n.
</div>

<div class="glossary-entry">
<div class="gterm">Constants rule (pull-out property) <span class="gcat cat-prop">Property</span></div>
If Z is F_n-measurable then E[YZ|F_n] = Z·E[Y|F_n]. Z behaves as a known constant. Proved first for Z = 1_A (A ∈ F_n) using the definition, extended to simple random variables by linearity, then to general Z by monotone convergence.
</div>

<div class="glossary-entry">
<div class="gterm">Radon-Nikodym theorem <span class="gcat cat-thm">Theorem</span></div>
Guarantees existence of conditional expectation. The function μ(A) = E[Y·1_A] is a signed measure on (Ω, F_n, P) with μ ≪ P. By Radon-Nikodym, there exists an F_n-measurable Z with μ(A) = E[Z·1_A] for all A ∈ F_n. This Z is E[Y|F_n].
</div>

---

### Study-Note Summary

- **E[Y | F_n]** is the minimum-MSE predictor of Y given information F_n. It is a *random variable* — its value changes with the observations X₁,…,Xₙ. E[Y] is the zero-information special case (a fixed number).
- **Probability space (Ω, F, P):** Ω = all outcomes; F = σ-algebra of observable events; P = probability measure. The three σ-algebra axioms (contains ∅, closed under complements and countable unions) make F self-consistent.
- **Filtration {F_n}:** increasing chain F₀ ⊆ F₁ ⊆ ⋯ encoding growing information. F_n = σ(X₁,…,Xₙ). Information never shrinks.
- **Formal definition** uses two conditions — F_n-measurability + E[E[Y|F_n]·1_A] = E[Y·1_A] for all A ∈ F_n — instead of a formula, because no single formula works in all probability spaces. Existence: Radon-Nikodym. Uniqueness: MSE argument.
- **Five properties:** (1) Known Y unchanged; (2) Tower — outer conditioning wins; (3) Independence → E[Y]; (4) Linearity; (5) Known factors pull out. All follow from the two defining conditions.
- **Example 1.1.1:** E[S_n | F_m] = S_m + (n−m)μ. When μ = 0 this becomes the martingale property of §1.2.
- **Example 1.1.3:** E[X₁ | S_n] = S_n/n. Conditioning on a coarser statistic gives an equal-share answer, independent of E[X₁].

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

