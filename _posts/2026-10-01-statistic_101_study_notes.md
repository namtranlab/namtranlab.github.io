---
layout: distill
title: "Statistics 110 — Study Notes"
description: "Lecture-by-lecture study notes for Statistics 110, beginning with probability and counting."
tags: [Statistics, Probability]
giscus_comments: true
date: 2026-10-01
featured: true
thumbnail: https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_A7fLYd-0jZzTN5eZJwaKA.jpeg

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: Lecture 1 - Probability and Counting
  - name: Lecture 2 - Story Proofs and Axioms of Probability
  - name: Lecture 3 - Birthday Problem and Properties of Probability

_styles: >
  /* ── Collapsible chapter blocks ── */
  .chapter-block { width: 100%; max-width: none; box-sizing: border-box; margin-bottom: 1.5rem; border: 0.5px solid #e0e0e0; border-radius: 10px; overflow: hidden; }
  .chapter-toggle { width: 100%; box-sizing: border-box; background: #f0f4ff; border: none; cursor: pointer; padding: 1rem 1.25rem; display: flex; align-items: center; justify-content: space-between; gap: 1rem; text-align: left; border-radius: 0; }
  .chapter-toggle:hover { background: #e4eaff; }
  .chapter-toggle-left { display: flex; align-items: center; gap: 0.75rem; }
  .chapter-badge { font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; background: #5b7de8; color: #fff; padding: 2px 9px; border-radius: 20px; flex-shrink: 0; }
  .chapter-title { font-size: 1rem; font-weight: 600; color: #1a1a2e; }
  .chapter-subtitle { font-size: 0.78rem; color: #666; margin-top: 1px; }
  .chapter-arrow { font-size: 1rem; color: #5b7de8; flex-shrink: 0; transition: transform 0.25s ease; display: inline-block; }
  .chapter-arrow.open { transform: rotate(180deg); }
  .chapter-body { width: 100%; box-sizing: border-box; display: none; padding: 1.25rem 1.5rem 1.5rem; border-top: 0.5px solid #e0e0e0; }
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

  .chapter-toggle:focus-visible { outline: 3px solid #5b7de8; outline-offset: -3px; }
  .chapter-toggle-left > span { display: block; }
  .chapter-subtitle { display: block; }
  .chapter-body { overflow-wrap: anywhere; }
  .chapter-body pre { overflow-x: auto; }
  @media (max-width: 600px) { .chapter-body { padding: 1rem; } .chapter-toggle { padding: 0.9rem; } .chapter-toggle-left { flex-wrap: wrap; } }
---

<script>
function toggleLecture(id) {
  var body = document.getElementById(id + '-body');
  var arrow = document.getElementById(id + '-arrow');
  var toggle = document.getElementById(id + '-toggle');
  var isOpen = body.classList.contains('open');
  body.classList.toggle('open', !isOpen);
  arrow.classList.toggle('open', !isOpen);
  toggle.setAttribute('aria-expanded', String(!isOpen));
}
</script>

**Statistics 110: Probability**, taught by Joe Blitzstein at Harvard University, introduces probability as a language for understanding uncertainty, randomness, and statistical reasoning. The course develops both intuition and mathematical problem-solving skills, beginning with counting and sample spaces before moving to conditional probability, Bayes’ rule, random variables, probability distributions, expectation, limit theorems, and Markov chains.

Follow the [course video lectures on YouTube](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo), or visit the [official course website](https://stat110.hsites.harvard.edu/) for supporting materials and practice problems.


## Lecture 1 - Probability and Counting

<div class="chapter-block">
  <button type="button" class="chapter-toggle" id="lecture-1-toggle" onclick="toggleLecture('lecture-1')" aria-expanded="true" aria-controls="lecture-1-body">
    <span class="chapter-toggle-left">
      <span class="chapter-badge">Lecture 1</span>
      <span>
        <span class="chapter-title">Lecture 1 - Probability and Counting</span>
        <span class="chapter-subtitle">Sample spaces, equally likely outcomes, counting rules, combinations, and sampling</span>
      </span>
    </span>
    <span class="chapter-arrow open" id="lecture-1-arrow" aria-hidden="true">▼</span>
  </button>
  <div class="chapter-body open" id="lecture-1-body" markdown="1">

<div class="note-abstract" markdown="1">

Probability begins with a precise description of possible outcomes. For finite, equally likely outcomes, probability reduces to counting. The multiplication rule and combinations provide the tools to count poker hands and distinguish the four basic sampling cases.

</div>

### Notation at a Glance

<div class="notation-panel" markdown="1">

| Symbol | Meaning |
|---|---|
| $$S$$ | Sample space: all possible outcomes |
| $$A\subseteq S$$ | Event: a subset of the sample space |
| $$P(A)$$ | Probability of event $$A$$ |
| $$\lvert S\rvert$$, $$\lvert A\rvert$$ | Number of outcomes in the sample space and the event |
| $$n!$$ | Factorial; $$0!=1$$ |
| $$\binom nk$$ | Number of unordered selections of $$k$$ distinct objects from $$n$$ |
| $$n$$ and $$k$$ | Number of available objects or types, and sample size |
| $$A\cup B$$, $$A\cap B$$, $$A^c$$ | Union, intersection, and complement |

</div>

### Learning objectives

After studying these notes, you should be able to:

- Define an experiment, an outcome, a sample space, and an event.
- Explain when probability can be calculated by counting outcomes.
- Apply the multiplication rule for counting.
- Distinguish ordered selections from unordered selections.
- Distinguish sampling with replacement from sampling without replacement.
- Derive the combination formula and calculate the probability of a full house.
- Explain your reasoning in words, including the assumptions behind your calculations.

### Part 1 — Why probability matters

Probability provides a mathematical way to describe uncertainty. Applications of probability and statistics include physics, genetics, economics, game theory, finance, history, government, and everyday reasoning.

#### Historical example: Who wrote the disputed Federalist Papers?

Frederick Mosteller and David Wallace investigated whether Alexander Hamilton or James Madison wrote 12 disputed Federalist essays. They compared word frequencies in texts with known authorship, focusing on common words whose use is relatively stable across topics. These writing habits provided evidence for comparing the two possible authors using statistical methods, including Bayesian inference. Their analysis supported Madison as the author of all 12 disputed essays.

**Core idea:** Uncertainty can concern a fixed historical fact. The author does not change, but our assessment of who it was can change as we examine evidence. Probability provides a way to quantify that uncertainty and update it.

#### Historical example: Dividing the prize in an unfinished game

Games involving dice, coins, and cards have clearly defined outcomes, making them useful for developing probability models. In their 1654 correspondence, Pierre de Fermat and Blaise Pascal explored games of chance, including how to divide a prize fairly when a contest stops before either player wins. Their letters helped establish the foundations of modern probability.

For a simplified example, suppose Alice and Bob have equal chances of winning each independent round. The first to win three rounds receives a $100 prize, but play stops with Alice leading two wins to one. Alice needs one more win; Bob needs two.

Imagine two further rounds, including an unused round if Alice wins immediately. The four equally likely sequences of round winners are:

| Next two round winners | Winner of the contest |
|---|---|
| Alice, Alice | Alice |
| Alice, Bob | Alice |
| Bob, Alice | Alice |
| Bob, Bob | Bob |

Alice wins the contest in three of the four sequences, so her chance of winning is $$3/4$$; Bob's is $$1/4$$. Dividing the prize in proportion to these chances gives Alice $$75$$ and Bob $$25$$.

**Core idea:** A fair division reflects each player's chance of winning from the current position. Counting equally likely future sequences turns that idea into a precise calculation. The imagined unused round keeps all sequences the same length without changing the contest's winner.

**Main lesson:** Intuition can be unreliable in probability. Precise definitions and explicit reasoning help us check it.

### Part 2 — Experiments, sample spaces, and events

#### Experiment

<div class="example-block" markdown="1">

<div class="ex-title">Experiment <span class="ex-pill pill-defn">Definition</span></div>

An **experiment** is any process with possible outcomes whose result is not known in advance. It need not be a laboratory experiment.

Examples include tossing a coin twice, rolling two dice, or selecting five cards.

</div>

#### Outcome and sample space

An **outcome** is one possible result. The **sample space**, written as $$S$$, is the set of all possible outcomes.

For two coin tosses:

$$
S=\{HH,HT,TH,TT\}.
$$

The positions represent the first and second tosses, so $$HT$$ and $$TH$$ are different outcomes.

For two distinguishable six-sided dice:

$$
S=\{(i,j):i,j\in\{1,2,3,4,5,6\}\},
\qquad \lvert S\rvert=6\times6=36.
$$

Here, $$\lvert S\rvert$$ means the number of elements in $$S$$. You can distinguish the dice by color, or distinguish the first roll from the second.

#### Event

<div class="example-block" markdown="1">

<div class="ex-title">Event <span class="ex-pill pill-defn">Definition</span></div>

An **event** is a subset of the sample space:

$$
A\subseteq S.
$$

An event occurs when the observed outcome belongs to that subset.

For two coin tosses:

| Event | Subset of the sample space |
|---|---|
| Both tosses are tails | $$\{TT\}$$ |
| Exactly one head | $$\{HT,TH\}$$ |
| At least one head | $$\{HH,HT,TH\}$$ |

</div>

#### Set notation refresher — supplementary

Unions, intersections, and complements translate statements about events into precise set notation:

| Notation | Meaning |
|---|---|
| $$A\cup B$$ | $$A$$ or $$B$$ occurs, including the possibility that both occur |
| $$A\cap B$$ | Both $$A$$ and $$B$$ occur |
| $$A^c$$ | $$A$$ does not occur; the outcomes in $$S$$ outside $$A$$ |
| $$\varnothing$$ | The empty event |
| $$A\subseteq B$$ | Every outcome in $$A$$ also belongs to $$B$$ |

### Part 3 — The naive definition of probability

<div class="result-box" markdown="1">

For a finite sample space whose outcomes are equally likely:

$$
\boxed{P(A)=\frac{\lvert A\rvert}{\lvert S\rvert}
=\frac{\text{number of favorable outcomes}}{\text{number of possible outcomes}}.}
$$

“Favorable” means that the outcome satisfies event $$A$$, whether or not that outcome is desirable.

</div>

#### The two essential conditions

<div class="warning-box" markdown="1">

1. **The sample space is finite.**
2. **Its individual outcomes are equally likely.**

Without these conditions, simply counting favorable and possible outcomes does not establish the probability.

</div>

#### Example: Two tails

If $$HH,HT,TH,TT$$ are equally likely, then:

$$
P(\text{two tails})=\frac{1}{4}.
$$

Only one of the four outcomes belongs to the event.

#### Fairness alone is not enough for a sequence

Equal chances of heads and tails on an individual toss do not, by themselves, guarantee that the four two-toss sequences are equally likely. Dependence between tosses can change their probabilities.

**Supplementary illustration:** Suppose the first toss is fair, but the second result always repeats the first. Each position individually has a 50% chance of heads, yet:

$$
P(HH)=P(TT)=\frac12,\qquad P(HT)=P(TH)=0.
$$

Independent fair tosses would make all four sequences equally likely. Independence is a concept developed more fully later in probability.

#### Two possibilities do not imply a 50–50 chance

<div class="misconception-block" markdown="1">

Consider the claim: “There either is life on Neptune or there is not, so the probability of life is 1/2.” This argument is invalid because listing two possibilities does not establish that they are equally likely.

**Key distinction:** Not knowing the probability is different from knowing that outcomes are equally likely.

Intelligent life is a more restrictive condition than life of any kind. If $$I$$ is the event of intelligent life and $$L$$ is the event of any life, then:

$$
I\subseteq L\quad\Longrightarrow\quad P(I)\le P(L).
$$

Strict inequality requires positive probability for life without intelligent life; it does not follow from subset inclusion alone.

</div>

#### Another common trap — supplementary

For two fair, independent dice, the 36 ordered pairs are equally likely. The possible sums $$2,3,\ldots,12$$ are not equally likely.

There is one pair giving sum 2, but six pairs giving sum 7. Therefore:

$$
P(\text{sum}=2)=\frac1{36},\qquad
P(\text{sum}=7)=\frac6{36}.
$$

### Part 4 — The multiplication rule for counting

Suppose a process has $$r$$ stages. There are $$n_1$$ choices at stage 1, $$n_2$$ choices at stage 2 for each possible first choice, and so on. If stage $$i$$ always has $$n_i$$ choices after any allowed preceding history, then:

$$
\boxed{\text{Number of complete outcomes}=n_1n_2\cdots n_r.}
$$

#### Example: Ice cream

<div class="example-block" markdown="1">

<div class="ex-title">Ice cream choices <span class="ex-pill pill-ex">Example</span></div>

There are two cone types and three flavors available with either cone:

```text
Choose a cone
├── Cake
│   ├── Chocolate
│   ├── Vanilla
│   └── Strawberry
└── Waffle
    ├── Chocolate
    ├── Vanilla
    └── Strawberry
```

Each complete path represents a different cone–flavor pair. There are:

$$
2\times3=6
$$

possible pairs. Choosing the flavor before the cone gives the same count: $$3\times2=6$$.

</div>

#### Why counting rules are useful

Ten stages with two choices each produce:

$$
2^{10}=1024
$$

outcomes. Listing every outcome quickly becomes impractical.

#### Clarifications — supplementary

- This is a **counting rule**, not a claim about multiplying probabilities of independent events. Counting does not require a probability model.
- The identities of available choices may change between branches, as long as the required number of choices at that stage stays the same.
- If branches have different numbers of continuations, count the separate branches and add. For example, three flavors for cake cones and two for waffle cones give $$3+2=5$$ possibilities.

### Part 5 — Factorials, ordered selections, and combinations

#### Factorial notation

For a positive integer $$n$$:

$$
n!=n(n-1)(n-2)\cdots2\cdot1
$$

For example, $$4!=24$$. The convention is $$0!=1$$.

#### Ordered selection without replacement

Select $$k$$ distinct objects from $$n$$, keeping track of selection order.

- The first selection has $$n$$ possibilities.
- The second has $$n-1$$ possibilities.
- The third has $$n-2$$ possibilities.
- The $$k$$th has $$n-k+1$$ possibilities.

The multiplication rule gives:

$$
n(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}.
$$

#### Unordered selection without replacement

If order does not matter, the ordered count counts each group repeatedly. Every group of $$k$$ distinct objects has exactly $$k!$$ orderings.

Divide by that common overcounting factor:

$$
\boxed{\binom nk=\frac{n!}{k!(n-k)!}.}
$$

This is a **binomial coefficient**, read as “$$n$$ choose $$k$$.” It counts subsets of size $$k$$ from $$n$$ distinct objects.

For $$0\le k\le n$$, use the formula above. For nonnegative integers with $$k>n$$, the count is zero because the selection is impossible.

#### Small example — supplementary

Choose two people from $$A,B,C$$.

Ordered selections:

```text
AB, BA, AC, CA, BC, CB
```

Unordered groups:

```text
{A,B}, {A,C}, {B,C}
```

Thus:

$$
\binom32=\frac{3\times2}{2!}=3.
$$

**Important:** Division by $$k!$$ works here because every selected object is distinct and every group was counted exactly $$k!$$ times.

<div class="example-block" markdown="1">

<div class="ex-title">Counting full houses <span class="ex-pill pill-ex">Worked example</span></div>

### Part 6 — Worked example: A full house in poker

#### Set up the model

A standard deck has 52 distinct cards: 13 ranks, each with four suits. A five-card hand is an unordered selection without replacement.

Assume every five-card hand is equally likely.

A **full house** contains exactly three cards of one rank and two cards of a different rank, such as three 7s and two 10s.

#### Step 1: Count all hands

$$
\lvert S\rvert=\binom{52}{5}=2,598,960.
$$

#### Step 2: Count full houses

| Choice | Number of possibilities | Explanation |
|---|---:|---|
| Rank of the three-card group | $$13$$ | Any rank is possible |
| Three suits for that rank | $$\binom43=4$$ | Choose three of its four cards |
| Rank of the two-card group | $$12$$ | It must differ from the first rank |
| Two suits for that rank | $$\binom42=6$$ | Choose two of its four cards |

By the multiplication rule:

$$
\lvert A\rvert=13\binom43\cdot12\binom42
=13\cdot4\cdot12\cdot6
=3744.
$$

Each full house has a unique triple rank, pair rank, and selection of suits. The procedure therefore counts every full house exactly once.

#### Step 3: Divide

$$
\boxed{
P(\text{full house})=
\frac{13\binom43\cdot12\binom42}{\binom{52}{5}}
=\frac{3744}{2,598,960}
\approx0.001440576.
}
$$

That is approximately **0.1441%**, or about one in 694 uniformly random five-card hands.

#### Common mistakes

- **Using 13 choices for the pair rank:** Only 12 remain after choosing the triple rank.
- **Dividing the numerator by $$2!$$:** The two ranks have different roles, so swapping them changes the hand's rank multiplicities.
- **Using only $$\binom{13}{2}$$ for the ranks:** After choosing two ranks, you must also choose which supplies the triple. An equivalent rank count is $$\binom{13}{2}\times2=13\times12$$.
- **Mixing an ordered denominator with an unordered numerator:** Both counts must describe outcomes using the same convention.
- **Forgetting suits:** Choosing ranks alone does not specify the actual five cards.

</div>

### Part 7 — The sampling table

Two questions determine the basic counting method:

1. **Does order matter?** Would selecting $$A$$ then $$B$$ differ from selecting $$B$$ then $$A$$?
2. **Is replacement allowed?** Can the same object be selected again?

For $$n$$ distinct available objects or types and a sample of size $$k$$:

| Sampling | Order matters | Order does not matter |
|---|---|---|
| With replacement | $$n^k$$ | $$\binom{n+k-1}{k}$$ |
| Without replacement | $$\frac{n!}{(n-k)!}$$ | $$\binom nk$$ |

Assume $$n\ge1$$ and $$k\ge0$$. Without replacement, the displayed factorial expressions apply when $$k\le n$$; the count is zero if $$k>n$$.

#### With replacement, ordered

Each of the $$k$$ positions has $$n$$ choices:

$$
n\times\cdots\times n=n^k.
$$

**Supplementary example:** A four-digit code, allowing leading zeros and repeated digits, has $$10^4=10,000$$ possibilities.

#### Without replacement, ordered

Each selection removes an object:

$$
n(n-1)\cdots(n-k+1)
$$

**Supplementary example:** Awarding gold, silver, and bronze to three of eight people, with no ties, gives $$8\times7\times6=336$$ possibilities.

#### Without replacement, unordered

Select a group, ignoring order:

$$
\binom nk.
$$

**Supplementary example:** A three-person committee from eight people can be chosen in $$\binom83=56$$ ways.

#### With replacement, unordered

Repetitions are allowed, but order is ignored. Such a selection is called a **multiset**.

The number of such selections is:

$$
\binom{n+k-1}{k}.
$$

A small case helps illustrate what the formula counts:

**Supplementary small-case check:** Choose two items from $$A,B,C$$, allowing repetition and ignoring order:

```text
AA, AB, AC, BB, BC, CC
```

There are six possibilities, agreeing with $$\binom{3+2-1}{2}=\binom42=6$$.

<div class="misconception-block" markdown="1">

**Why you cannot simply divide $$n^k$$ by $$k!$$ — supplementary**

With repetition, different unordered selections can have different numbers of ordered versions. For example, $$AB$$ corresponds to $$AB$$ and $$BA$$, but $$AA$$ has only one ordering.

There is no uniform $$k!$$ overcounting factor.

</div>

<div class="warning-box" markdown="1">

#### A probability warning — supplementary

The sampling table counts possibilities; it does not automatically make them equally likely.

For two independent uniform draws from $$A,B,C$$, there are nine equally likely ordered sequences. After ignoring order:

$$
P(AA)=\frac19,\qquad P(\{A,B\})=\frac29.
$$

Although there are six multisets, they are not equally likely under this sampling process. Consequently, dividing by six would give incorrect probabilities for this experiment.

</div>

### Part 8 — Original practice questions

Try these before reading the answers.

1. Two independent fair coins are tossed. Write the sample space and find the probability of exactly one head.
2. A cafe offers four drinks and three pastries, with every pairing available. How many drink–pastry pairs can you choose?
3. How many five-character strings can be formed from $$A,B,C,D$$ if repetition is allowed?
4. How many ways can a president and secretary be selected from seven people if one person cannot hold both roles?
5. How many three-person committees can be selected from seven people?
6. A bag contains five distinct red balls and three distinct blue balls. Two balls are selected uniformly without replacement. What is the probability that both are red?
7. How many unordered selections of three items can be made from four types if repetition is allowed?
8. Explain why “it happens or it does not happen” does not establish a probability of $$1/2$$.
9. In the full-house calculation, explain why the two rank factors are 13 and 12, and why there is no division by 2.

### Part 9 — Practice answers

#### 1. Exactly one head

$$
S=\{HH,HT,TH,TT\},\qquad A=\{HT,TH\}.
$$

The four sequences are equally likely, so $$P(A)=2/4=1/2$$.

#### 2. Cafe pairs

Each drink can be paired with any of three pastries, giving $$4\times3=12$$ pairs.

#### 3. Strings with repetition

There are four choices for each of five positions, giving $$4^5=1024$$ strings.

#### 4. Distinct officer roles

There are seven choices for president and six remaining choices for secretary, giving $$7\times6=42$$ assignments. The roles matter.

#### 5. Committee

Order does not matter, so the count is:

$$
\binom73=\frac{7\cdot6\cdot5}{3\cdot2\cdot1}=35.
$$

#### 6. Two red balls

All unordered pairs of distinct balls are equally likely under the stated sampling process. There are $$\binom82$$ total pairs and $$\binom52$$ red pairs:

$$
P(\text{both red})=\frac{\binom52}{\binom82}
=\frac{10}{28}=\frac5{14}.
$$

#### 7. Unordered selection with repetition

Use the formula for unordered selections with replacement:

$$
\binom{4+3-1}{3}=\binom63=20.
$$

This is a count, not a claim that those selections are equally likely under every drawing process.

#### 8. Two possibilities

The possibilities must also be equally likely before favorable-outcome counting gives $$1/2$$. The number of labels alone supplies no evidence of equal likelihood.

#### 9. Full-house ranks

Any of 13 ranks can supply the triple. The pair must use one of the other 12 ranks. There is no division by 2 because the triple and pair roles distinguish the two ranks; each full house is already counted once.

### Part 10 — Quick revision sheet

| Concept | Essential fact |
|---|---|
| Sample space | Set of possible outcomes, $$S$$ |
| Event | Subset $$A\subseteq S$$ |
| Naive probability | $$P(A)=\lvert A\rvert/\lvert S\rvert$$ for finite, equally likely outcomes |
| Multiplication rule | Multiply stage counts when each stage has the stated number of choices after every allowed history |
| Ordered, with replacement | $$n^k$$ |
| Ordered, without replacement | $$n!/(n-k)!$$ |
| Unordered, without replacement | $$\binom nk$$ |
| Unordered, with replacement | $$\binom{n+k-1}{k}$$ |
| Full house | $$13\binom43\cdot12\binom42/\binom{52}{5}\approx0.1441\%$$ |


### Term Glossary

<div class="glossary-entry" markdown="1">
<div class="gterm">Sample space <span class="gcat cat-defn">Definition</span></div>

The set of all possible outcomes of the experiment.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Event <span class="gcat cat-defn">Definition</span></div>

A subset of the sample space; it occurs when the observed outcome belongs to that subset.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Equally likely outcomes <span class="gcat cat-defn">Definition</span></div>

Outcomes assigned the same probability by the model. This assumption must be justified before applying the counting ratio.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Multiplication rule <span class="gcat cat-defn">Definition</span></div>

A counting principle that multiplies the numbers of choices at successive stages, provided each stage has the stated count after every allowed preceding history.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Combination <span class="gcat cat-defn">Definition</span></div>

An unordered selection of distinct objects, counted by a binomial coefficient.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Replacement <span class="gcat cat-defn">Definition</span></div>

Returning a selected object to the available pool so that it can be selected again.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Multiset <span class="gcat cat-defn">Definition</span></div>

An unordered selection that permits repeated objects or types.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Full house <span class="gcat cat-defn">Definition</span></div>

A five-card hand with three cards of one rank and two cards of a different rank.

</div>

<div class="ref-tags">
  <span class="ref-tag">Statistics 110</span>
  <span class="ref-tag">Lecture 1</span>
  <span class="ref-tag">Probability</span>
  <span class="ref-tag">Counting</span>
  <span class="ref-tag">Combinations</span>
</div>

  </div>
</div>

<!-- Future lectures: add a matching entry to the front-matter toc, then append
     a new H2 heading and chapter-block here. Use "Lecture 2 - Topic" (and so on),
     unique lecture-2-toggle/body/arrow IDs, and toggleLecture('lecture-2').
     Keep the shared styles and toggleLecture function defined only once. -->


## Lecture 2 - Story Proofs and Axioms of Probability

<div class="chapter-block">
  <button type="button" class="chapter-toggle" id="lecture-2-toggle" onclick="toggleLecture('lecture-2')" aria-expanded="true" aria-controls="lecture-2-body">
    <span class="chapter-toggle-left">
      <span class="chapter-badge">Lecture 2</span>
      <span>
        <span class="chapter-title">Lecture 2 - Story Proofs and Axioms of Probability</span>
        <span class="chapter-subtitle">Labeling, stars and bars, combinatorial identities, and probability spaces</span>
      </span>
    </span>
    <span class="chapter-arrow open" id="lecture-2-arrow" aria-hidden="true">▼</span>
  </button>
  <div class="chapter-body open" id="lecture-2-body" markdown="1">

<div class="note-abstract" markdown="1">

Counting becomes easier when a problem is represented in a useful way. Labeling clarifies which outcomes are distinct; stars and bars turns repeated selections into arrangements of symbols; story proofs establish identities by counting the same collection in two ways. Probability axioms then extend the framework to unequal probabilities and infinite sample spaces.

</div>

### Notation at a Glance

<div class="notation-panel" markdown="1">

| Symbol | Meaning |
|---|---|
| $$n$$ | Number of available types or labeled boxes in a stars-and-bars problem |
| $$k$$ | Number of selections or identical objects to distribute |
| $$x_i$$ | Number of selections of type $$i$$, or occupancy of box $$i$$ |
| $$\binom{n+k-1}{k}$$ | Number of unordered selections with replacement |
| $$m,n$$ | Sizes of two disjoint groups in Vandermonde's identity |
| $$j$$ | Number selected from the first group |
| $$S$$ | Sample space |
| $$P(A)$$ | Probability assigned to event $$A$$ |
| $$\varnothing$$ | Empty event |
| $$A_i\cap A_j=\varnothing$$ | Events $$A_i$$ and $$A_j$$ are disjoint |
| $$\bigcup_{j=1}^{\infty}A_j$$ | Event that at least one of the events $$A_1,A_2,\ldots$$ occurs |

</div>

### Learning objectives

After studying these notes, you should be able to:

- Distinguish labeled objects from unordered summaries of those objects.
- Explain when dividing by an overcounting factor is justified.
- Derive the stars-and-bars formula using a reversible encoding.
- Recognize equivalent problems involving repeated selections, box occupancies, and integer solutions.
- Prove three binomial identities by interpreting both sides as counts.
- Explain why a count of possible configurations does not specify their probabilities.
- State the probability axioms and apply additivity to disjoint events.

### Part 1 — Labeling and correcting overcounting

#### Objects can look identical and still represent different outcomes

Suppose a jar contains three red balls and one green ball, and each physical ball is equally likely to be drawn. Label them $$R_1,R_2,R_3,G_1$$. The sample space for one draw has four equally likely outcomes, so:

$$
P(\text{red})=\frac34.
$$

The color labels “red” and “green” describe only two possible observations, but those observations are not equally likely. Red combines three underlying outcomes, whereas green corresponds to one.

**Core idea:** Labels make the elementary outcomes explicit. Ignoring a distinction in the final observation does not erase its effect on probability.

#### Example: Splitting ten people into teams of four and six

Choose the four-person team. Everyone else belongs to the six-person team:

$$
\binom{10}{4}=210.
$$

Choosing the six-person team first gives the same partition, so:

$$
\binom{10}{4}=\binom{10}{6}.
$$

There is no division by two: each partition has exactly one four-person team, so choosing that team counts each partition once.

<div class="example-block" markdown="1">
<div class="ex-title">Two unnamed teams of five <span class="ex-pill pill-ex">Worked example</span></div>

Now split ten people into two five-person teams with no labels or different roles assigned to the teams.

Choosing five people gives $$\binom{10}{5}$$ possibilities, but it counts each partition twice. Selecting one team first or selecting its complement first produces the same pair of teams.

Therefore:

$$
\boxed{\text{Number of partitions}=\frac12\binom{10}{5}=126.}
$$

If the teams instead have distinct labels, such as Team A and Team B, assigning a group to Team A differs from assigning that group to Team B. The count is then $$\binom{10}{5}=252$$.

<div class="ex-lesson"><strong>Core idea:</strong> Decide what makes two completed results different before correcting for overcounting. Equal-sized, unnamed teams can be exchanged without changing a partition; labeled teams cannot.</div>
</div>

<div class="warning-box" markdown="1">

**When can you divide?** Divide by a number $$c$$ only after showing that every desired outcome was counted exactly $$c$$ times. A correction that varies from outcome to outcome cannot be applied as one common divisor.

</div>

### Part 2 — Unordered sampling with replacement

Choose $$k$$ times from $$n$$ available types, allowing repetition and ignoring selection order. Assume $$n\ge1$$ and $$k\ge0$$.

Instead of recording a sequence, record how often each type was chosen:

$$
(x_1,x_2,\ldots,x_n),\qquad x_i\ge0,\qquad x_1+\cdots+x_n=k.
$$

The entries are nonnegative integers. For example, choosing types $$A,A,C$$ gives counts $$(2,0,1)$$ for types $$A,B,C$$. Sequences $$AAC$$, $$ACA$$, and $$CAA$$ all give the same count vector.

<div class="example-block" markdown="1">
<div class="ex-title">Three equivalent counting problems <span class="ex-pill pill-defn">Interpretation</span></div>

The following descriptions refer to the same collection of possibilities:

| Description | What one outcome records |
|---|---|
| Unordered sampling with replacement | How many times each type was selected |
| Identical objects in labeled boxes | How many objects occupy each box |
| Nonnegative integer solutions | A vector $$(x_1,\ldots,x_n)$$ whose entries sum to $$k$$ |

Each type corresponds to a box, and each selection adds one identical tally mark to that box. The boxes remain distinct because they represent different types; the tally marks do not need identities because order is ignored.

</div>

#### Check simple cases

| Case | Direct reasoning | Formula check |
|---|---|---|
| $$k=0$$ | One empty selection | $$\binom{n-1}{0}=1$$ |
| $$k=1$$ | Choose any one of the $$n$$ types | $$\binom n1=n$$ |
| $$n=1$$ | Every selection is of the only type | $$\binom kk=1$$ |
| $$n=2$$ | The first count can be $$0,1,\ldots,k$$; the second is determined | $$\binom{k+1}{k}=k+1$$ |

These checks help interpret the formula. They do not replace a proof for arbitrary $$n$$ and $$k$$.

### Part 3 — Stars and bars: deriving the formula

<div class="example-block" markdown="1">
<div class="ex-title">Stars-and-bars formula <span class="ex-pill pill-thm">Theorem</span></div>

The number of ways to distribute $$k$$ identical objects among $$n$$ labeled boxes, allowing empty boxes, is:

$$
\boxed{\binom{n+k-1}{k}=\binom{n+k-1}{n-1}.}
$$

Equivalently, this counts nonnegative integer solutions of $$x_1+\cdots+x_n=k$$ and unordered selections of size $$k$$ with replacement from $$n$$ types.

</div>

#### Step 1: Encode the box counts

Use a star `*` for each object and a bar `|` between neighboring boxes.

For four boxes containing $$(3,0,2,1)$$ objects, the encoding is:

```text
Box 1   Box 2   Box 3   Box 4
  ***   |      |  **   |  *

Compact encoding: ***||**|*
```

There are six stars and three bars. The adjacent bars indicate an empty second box. A leading bar would indicate an empty first box, and a trailing bar would indicate an empty last box.

#### Visual example: From boxes to a symbol string

<figure>
  <img src="/assets/img/statistic-101/lecture-2-textbook-fig-1-5-box-encoding.png" alt="Four boxes containing one, two, three, and one particles, with the corresponding wall-and-particle encoding below." style="display: block; width: 100%; max-width: 640px; height: auto; margin: 0 auto;">
  <figcaption>Boxes and their symbol encoding. Reproduced from Joseph K. Blitzstein and Jessica Hwang, <em>Introduction to Probability</em>, Figure 1.5, p. 18.</figcaption>
</figure>

The four boxes contain $$(1,2,3,1)$$ particles, so $$n=4$$ and $$k=7$$. Reading from left to right, each dot becomes a star and each boundary between boxes becomes a bar:

```text
*|**|***|*
```

The lower row also shows an outer wall at each end. Those two walls are fixed; they are not extra separators to arrange. Removing them leaves seven stars and three internal bars, or ten positions. Thus all configurations of seven identical objects in four labeled boxes are counted by:

$$
\binom{10}{7}=\binom{10}{3}=120.
$$

**Core idea:** The box boundaries preserve the order of the labeled boxes, while the dots record only occupancies. The diagram uses seven particles; the earlier $$(3,0,2,1)$$ example uses six and shows how an empty box is encoded.

#### Step 2: Show that the encoding is reversible

Every occupancy vector produces exactly one string. Conversely, count the stars before the first bar, between successive bars, and after the last bar to recover every box count.

This is a **bijection**: a one-to-one correspondence between the two collections. Nothing is omitted and nothing is counted twice.

#### Step 3: Choose the star positions

A valid string contains:

- $$k$$ stars;
- $$n-1$$ bars;
- $$n+k-1$$ positions altogether.

Choose which $$k$$ positions contain stars. All remaining positions contain bars:

$$
\text{Number of strings}=\binom{n+k-1}{k}.
$$

Choosing the $$n-1$$ bar positions instead gives $$\binom{n+k-1}{n-1}$$. Both descriptions specify the same strings.

**For the example:** Six objects among four boxes give $$\binom96=\binom93=84$$ possible occupancy vectors.

<div class="misconception-block" markdown="1">

**Why not choose gaps only between the stars?** That would rule out adjacent bars and bars at the ends, excluding empty boxes. Stars and bars allows those arrangements because a type may be selected zero times.

**Why not divide $$n^k$$ by $$k!$$?** Different count vectors have different numbers of ordered versions. For example, $$AAA$$ has one ordering, while $$AAB$$ has three. There is no common $$k!$$ overcounting factor.

</div>

#### Supplementary example: Each box must be nonempty

Distribute seven identical objects into three labeled boxes, with at least one in each box.

First place one object in each box. Four objects remain, and they may be distributed with empty boxes allowed. Thus:

$$
\binom{3+4-1}{4}=\binom64=15.
$$

More generally, for $$k\ge n\ge1$$, positive integer solutions of $$x_1+\cdots+x_n=k$$ are counted by:

$$
\binom{k-1}{n-1}.
$$

If $$k<n$$, no such solution exists. The change of variables $$y_i=x_i-1$$ explains the result: the $$y_i$$ are nonnegative and sum to $$k-n$$.

### Part 4 — A count is not a probability model

The stars-and-bars count is also called the **Bose–Einstein value**, reflecting its connection to counting occupation configurations of indistinguishable particles. For ordinary sampling problems, however, counting configurations does not establish that those configurations are equally likely.

#### Example: Two independent fair coin tosses

The four equally likely ordered outcomes are:

$$
HH,\quad HT,\quad TH,\quad TT.
$$

Ignoring order leaves three head–tail count configurations:

| Configuration | Ordered outcomes represented | Probability |
|---|---|---|
| Two heads | $$HH$$ | $$1/4$$ |
| One head and one tail | $$HT,TH$$ | $$1/2$$ |
| Two tails | $$TT$$ | $$1/4$$ |

Stars and bars correctly counts the three configurations:

$$
\binom{2+2-1}{2}=3.
$$

It does **not** imply that each has probability $$1/3$$. A model assigning equal probabilities to the three configurations would describe a different random experiment.

**Core idea:** Whether we can visually distinguish objects is separate from how the experiment assigns probabilities. Identical-looking coins still have a first and second toss, or can be labeled coin 1 and coin 2.

<div class="warning-box" markdown="1">

**The physics connection has limits.** Bose–Einstein counting concerns indistinguishable particles and their occupation configurations. It does not make ordinary coin-toss configurations uniformly distributed, nor does the counting formula alone determine a physical system's probabilities.

</div>

#### Supplementary formula: Probability of a count vector

For $$k$$ independent draws, each uniformly choosing one of $$n$$ types, every ordered sequence has probability $$1/n^k$$.

A count vector $$(x_1,\ldots,x_n)$$ represents:

$$
\frac{k!}{x_1!x_2!\cdots x_n!}
$$

ordered sequences. To see why, arrange the $$k$$ selections and divide out the permutations within each repeated type. Therefore:

$$
P(\text{counts }(x_1,\ldots,x_n))
=\frac{k!}{x_1!\cdots x_n!}\frac1{n^k}.
$$

This explains precisely why different occupancy vectors generally receive different probabilities.

### Part 5 — Story proofs: counting the same collection twice

<div class="example-block" markdown="1">
<div class="ex-title">Story proof <span class="ex-pill pill-defn">Definition</span></div>

A **story proof** establishes a mathematical result through an interpretation. For a counting identity, interpret both sides as the number of objects in the same collection, then justify each count.

A story proof is a general argument. Verifying a few numerical examples provides checks, but does not prove an identity for all admissible values.

</div>

#### Identity 1: Choosing a group or its complement

For integers $$0\le k\le n$$:

$$
\boxed{\binom nk=\binom n{n-k}.}
$$

Choose a committee of $$k$$ people from $$n$$ people. Specifying the members uniquely determines the $$n-k$$ nonmembers, and specifying the nonmembers uniquely determines the members.

The two sides count the same committees through complementary descriptions.

**Core idea:** Choosing what to include is equivalent to choosing what to exclude.

#### Identity 2: A committee with a president

For integers $$1\le k\le n$$:

$$
\boxed{n\binom{n-1}{k-1}=k\binom nk.}
$$

Count committees of size $$k$$ with one committee member designated as president.

| Method | First choice | Second choice | Total |
|---|---|---|---|
| President first | One of $$n$$ people | Remaining $$k-1$$ members from the other $$n-1$$ | $$n\binom{n-1}{k-1}$$ |
| Committee first | A $$k$$-person committee from $$n$$ | President from its $$k$$ members | $$\binom nk\,k$$ |

Every committee–president pair is counted exactly once by each method, proving the identity.

For example, selecting a three-person committee with a president from five people gives:

$$
5\binom42=30=3\binom53.
$$

**Core idea:** Changing the order in which we specify a complete outcome can produce a useful identity without changing the outcomes being counted.

### Part 6 — Vandermonde's identity

<div class="example-block" markdown="1">
<div class="ex-title">Vandermonde's identity <span class="ex-pill pill-thm">Theorem</span></div>

For nonnegative integers $$m,n,k$$ with $$k\le m+n$$:

$$
\boxed{\binom{m+n}{k}
=\sum_{j=0}^{k}\binom mj\binom n{k-j}.}
$$

A binomial coefficient is zero when its lower argument exceeds its nonnegative upper argument. Impossible selections therefore contribute zero to the sum.

</div>

#### The story: Choose a committee from two groups

There are two disjoint groups: the first has $$m$$ people, and the second has $$n$$ people. Choose a committee of size $$k$$.

**Count directly:** Choose any $$k$$ of the total $$m+n$$ people:

$$
\binom{m+n}{k}.
$$

**Count by composition:** Suppose exactly $$j$$ committee members come from the first group. Then $$k-j$$ must come from the second group. For this fixed $$j$$, the multiplication rule gives:

$$
\binom mj\binom n{k-j}.
$$

Add over all possible $$j$$. The cases are disjoint because a committee has exactly one value of $$j$$, and they cover all committees. This proves the identity.

The feasible values are:

$$
\max(0,k-n)\le j\le\min(k,m).
$$

Using $$j=0,\ldots,k$$ is convenient because the infeasible terms are already zero.

#### Worked numerical example

Choose three people from a group of three and a separate group of four:

| Number from the first group, $$j$$ | Number from the second group | Number of committees |
|---|---:|---|
| 0 | 3 | $$\binom30\binom43=4$$ |
| 1 | 2 | $$\binom31\binom42=18$$ |
| 2 | 1 | $$\binom32\binom41=12$$ |
| 3 | 0 | $$\binom33\binom40=1$$ |

Hence:

$$
4+18+12+1=35=\binom73.
$$

**Core idea:** Multiply choices within a fixed case; add counts across disjoint cases.

#### Supplementary probability connection

If every $$k$$-person committee is equally likely, then:

$$
P(\text{exactly }j\text{ from the first group})
=\frac{\binom mj\binom n{k-j}}{\binom{m+n}{k}}.
$$

Vandermonde's identity guarantees that these probabilities sum to 1. It connects a combinatorial identity to the requirement that all possible cases account for the whole experiment.

### Part 7 — The general definition of probability

The formula $$P(A)=\lvert A\rvert/\lvert S\rvert$$ requires a finite sample space with equally likely outcomes. To handle unequal probabilities or infinitely many outcomes, assign probabilities to events through a function $$P$$.

<div class="example-block" markdown="1">
<div class="ex-title">Probability space <span class="ex-pill pill-defn">Definition</span></div>

At this introductory level, a **probability space** consists of:

- A sample space $$S$$ describing possible outcomes.
- A probability function $$P$$ that maps each event $$A$$ to a real number $$P(A)$$ in $$[0,1]$$ and satisfies the axioms below.

The input to $$P$$ is an event, which is a set of outcomes. Its output is a number.

</div>

#### Visual interpretation: Events are sets; probabilities are masses

<figure>
  <img src="/assets/img/statistic-101/lecture-2-textbook-fig-1-1-pebble-world.png" alt="Nine outcomes represented by pebbles. Event A encloses five pebbles, event B encloses four, and one pebble belongs to both events." style="display: block; width: 100%; max-width: 560px; height: auto; margin: 0 auto;">
  <figcaption>Pebble World: each pebble is an outcome, and each outlined region is an event. Reproduced from Joseph K. Blitzstein and Jessica Hwang, <em>Introduction to Probability</em>, Figure 1.1, p. 3; the mass interpretation is developed in Section 1.6.</figcaption>
</figure>

The outer rectangle is $$S$$. Event $$A$$ contains five of the nine outcomes; event $$B$$ contains four. One outcome belongs to both, so $$A$$ and $$B$$ are not disjoint.

If all nine outcomes are equally likely, each has probability $$1/9$$. Then:

$$
P(A)=\frac59,\qquad P(B)=\frac49,\qquad
P(A\cap B)=\frac19,\qquad P(A\cup B)=\frac89.
$$

Adding $$5/9$$ and $$4/9$$ counts the shared pebble twice. Their union contains eight distinct pebbles, so direct addition is invalid here.

For a general finite model, imagine giving the pebbles nonnegative masses totaling 1. The probability of an event is the sum of the masses inside it. Equal masses recover counting; unequal masses require adding the assigned probabilities instead. The picture specifies which outcomes belong to each event, but the size or number of drawn circles alone does not specify their probabilities.

**Core idea:** Combining disjoint events adds separate masses. When events overlap, their common outcomes must be accounted for only once.

#### Axiom 1: The empty event and the whole space

$$
\boxed{P(\varnothing)=0,\qquad P(S)=1.}
$$

The empty event contains no outcome, so it cannot occur. The full sample space contains every possible outcome, so it must occur.

#### Axiom 2: Countable additivity

If $$A_1,A_2,\ldots$$ are pairwise disjoint events, then:

$$
\boxed{P\left(\bigcup_{j=1}^{\infty}A_j\right)
=\sum_{j=1}^{\infty}P(A_j).}
$$

“Pairwise disjoint” means:

$$
A_i\cap A_j=\varnothing\qquad\text{whenever }i\ne j.
$$

No outcome belongs to two of the events. Their union therefore combines non-overlapping probability contributions.

Countable additivity also gives finite additivity: set all events after the last one to $$\varnothing$$. In particular, if $$A\cap B=\varnothing$$, then:

$$
P(A\cup B)=P(A)+P(B).
$$

<div class="misconception-block" markdown="1">

**Disjointness is essential.** For two independent fair coin tosses, let $$A$$ mean the first toss is heads and $$B$$ mean the second toss is heads. The outcome $$HH$$ belongs to both events. Adding $$P(A)+P(B)=1$$ counts it twice, whereas $$P(A\cup B)=3/4$$.

Independent events are not necessarily disjoint. Independence describes how probabilities relate; disjointness means that the events cannot occur together.

</div>

#### Supplementary example: Unequal masses on a finite sample space

Let $$S=\{a,b,c\}$$, with individual probabilities $$0.2,0.3,0.5$$. For any event, add the probabilities of its outcomes. Then:

$$
P(\{a,c\})=0.2+0.5=0.7.
$$

The empty set has total probability 0, the full space has total probability 1, and disjoint sets add without double counting. This is a valid probability model, although counting two favorable outcomes out of three would give the wrong answer.

Equal masses of $$1/N$$ on a finite sample space of size $$N$$ recover the naive formula. Thus the counting definition is a special case of the general framework.

#### Supplementary example: A countably infinite sample space

Let $$S=\{1,2,3,\ldots\}$$ and assign:

$$
P(\{j\})=2^{-j},\qquad j=1,2,\ldots.
$$

The total probability is the geometric series:

$$
\sum_{j=1}^{\infty}2^{-j}=1.
$$

For example, the probability of an even result is:

$$
P(\{2,4,6,\ldots\})=\sum_{r=1}^{\infty}4^{-r}=\frac13.
$$

The outcomes are not equally likely, but the model has a well-defined total probability. No division by an infinite number of outcomes is needed.

<div class="warning-box" markdown="1">

**Technical clarification for infinite spaces:** In a fully general treatment, probabilities are assigned to a specified collection of measurable events, and a probability space is written $$(S,\mathcal F,P)$$. For finite or countable spaces, we can take all subsets as events. For uncountable spaces, such as a continuous interval, additional care is needed; not every subset must be assigned a probability.

**Probability zero is not always impossibility.** The empty event always has probability zero, but in continuous models a particular point can also have probability zero. The reverse implication is not generally valid.

</div>

### Part 8 — Original practice questions

Try these before reading the answers.

1. How many ways can eight people be split into an unnamed team of three and a team of five? What changes for two unnamed teams of four? What if the two four-person teams are labeled A and B?
2. Encode $$(2,0,1,2)$$ using stars and bars. How many possible occupancy vectors are there for five identical objects in four labeled boxes?
3. How many nonnegative integer solutions satisfy $$x_1+x_2+x_3=6$$? How many satisfy the same equation with all entries positive?
4. Three independent draws select uniformly from types $$A$$ and $$B$$. How many unordered count configurations are possible? Find the probability of each configuration and explain why they are not uniform.
5. Prove $$6\binom52=3\binom63$$ by describing a committee and a president.
6. Choose three people from disjoint groups of four and five people. Use Vandermonde's identity to verify the total count. If all committees are equally likely, what is the probability that exactly two members come from the first group?
7. Suppose $$S=\{a,b,c\}$$ has individual probabilities $$0.1,0.4,0.5$$. Let $$A=\{a,b\}$$ and $$B=\{b,c\}$$. Find $$P(A)$$, $$P(B)$$, and $$P(A\cup B)$$. Why is direct addition invalid?
8. In the model $$P(\{j\})=2^{-j}$$ for positive integers $$j$$, find the probability of a result at least 3.

### Part 9 — Practice answers

#### 1. Splitting teams

For teams of three and five, choose the three-person team:

$$
\binom83=56.
$$

For two unnamed teams of four, each partition is counted twice by selecting a four-person team:

$$
\frac12\binom84=35.
$$

For labeled teams A and B, choosing Team A uniquely determines Team B, giving $$\binom84=70$$ assignments.

#### 2. Stars-and-bars encoding

The string is:

```text
**||*|**
```

There are five stars and three bars, so:

$$
\binom{4+5-1}{5}=\binom85=56.
$$

#### 3. Integer solutions

For nonnegative entries:

$$
\binom{3+6-1}{6}=\binom82=28.
$$

For positive entries, subtract one from each variable. The new nonnegative entries sum to 3, giving:

$$
\binom{3+3-1}{3}=\binom52=10.
$$

#### 4. Counts versus probabilities

There are $$\binom{2+3-1}{3}=4$$ configurations. The eight ordered sequences are equally likely:

| Counts $$(x_A,x_B)$$ | Number of ordered sequences | Probability |
|---|---:|---|
| $$(3,0)$$ | 1 | $$1/8$$ |
| $$(2,1)$$ | 3 | $$3/8$$ |
| $$(1,2)$$ | 3 | $$3/8$$ |
| $$(0,3)$$ | 1 | $$1/8$$ |

The configurations are not uniform because they represent different numbers of equally likely ordered outcomes.

#### 5. Committee and president

Choose the president from six people, then two other members from the remaining five: $$6\binom52$$.

Alternatively, choose three members from six, then select one of the three as president: $$3\binom63$$.

Both count the same committee–president pairs, and both equal 60.

#### 6. Vandermonde and a committee probability

Count by the number selected from the first group:

$$
\binom40\binom53+\binom41\binom52+
\binom42\binom51+\binom43\binom50
=10+40+30+4=84=\binom93.
$$

Exactly two from the first group gives $$\binom42\binom51=30$$ committees, so:

$$
P(\text{exactly two})=\frac{30}{84}=\frac5{14}.
$$

#### 7. Overlapping events

$$
P(A)=0.1+0.4=0.5,\qquad P(B)=0.4+0.5=0.9.
$$

Their union is $$S$$, so $$P(A\cup B)=1$$. Adding 0.5 and 0.9 counts outcome $$b$$ twice. Additivity in its direct form requires disjoint events.

#### 8. An infinite tail

By countable additivity:

$$
P(\{3,4,5,\ldots\})=\sum_{j=3}^{\infty}2^{-j}
=\frac{1/8}{1-1/2}=\frac14.
$$

### Part 10 — Quick revision sheet

| Concept | Essential fact |
|---|---|
| Labels | Identify elementary outcomes before grouping them into observations |
| Overcounting correction | Divide by $$c$$ only when every desired outcome is counted exactly $$c$$ times |
| Stars and bars | $$k$$ identical objects, $$n$$ labeled boxes, empty boxes allowed: $$\binom{n+k-1}{k}$$ |
| Positive occupancies | For $$k\ge n\ge1$$: $$\binom{k-1}{n-1}$$ |
| Complement identity | $$\binom nk=\binom n{n-k}$$ |
| Committee–president identity | $$n\binom{n-1}{k-1}=k\binom nk$$ |
| Vandermonde's identity | $$\binom{m+n}{k}=\sum_{j=0}^k\binom mj\binom n{k-j}$$ |
| Story proof | Justify two counts of the same collection |
| Probability function | Maps events to numbers in $$[0,1]$$ |
| Normalization | $$P(\varnothing)=0$$ and $$P(S)=1$$ |
| Countable additivity | For pairwise disjoint events, probability of the union equals the sum of probabilities |
| Main modeling warning | Equally likely sequences can produce unequally likely count configurations |

### Term Glossary

<div class="glossary-entry" markdown="1">
<div class="gterm">Occupancy vector <span class="gcat cat-notn">Notation</span></div>

A vector $$(x_1,\ldots,x_n)$$ recording the number of objects in each labeled box. For unordered repeated selections, it records how many times each type was chosen.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Bijection <span class="gcat cat-defn">Definition</span></div>

A one-to-one correspondence between two collections. Every element of either collection has exactly one partner in the other, so finite collections related by a bijection have the same size.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Stars and bars <span class="gcat cat-prop">Counting method</span></div>

An encoding of identical objects as stars and boundaries between labeled boxes as bars. Choosing the star or bar positions gives the number of nonnegative occupancy vectors.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Story proof <span class="gcat cat-defn">Definition</span></div>

A proof by interpretation. In combinatorics, it often establishes an identity by counting the same collection in two justified ways.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Vandermonde's identity <span class="gcat cat-thm">Identity</span></div>

An equality between choosing a committee from two combined groups and summing over all possible ways to split its membership between those groups.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Probability space <span class="gcat cat-defn">Definition</span></div>

A sample space together with a probability function on its events. In the fully general formulation, the collection of measurable events is also specified.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Pairwise disjoint events <span class="gcat cat-defn">Definition</span></div>

Events for which every pair of distinct events has empty intersection. At most one of them can occur in a single outcome.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Countable additivity <span class="gcat cat-prop">Axiom</span></div>

The probability of a union of countably many pairwise disjoint events equals the sum of their individual probabilities.

</div>

<div class="ref-tags">
  <span class="ref-tag">Statistics 110</span>
  <span class="ref-tag">Lecture 2</span>
  <span class="ref-tag">Stars and bars</span>
  <span class="ref-tag">Story proofs</span>
  <span class="ref-tag">Probability axioms</span>
</div>

  </div>
</div>


## Lecture 3 - Birthday Problem and Properties of Probability

<div class="chapter-block">
  <button type="button" class="chapter-toggle" id="lecture-3-toggle" onclick="toggleLecture('lecture-3')" aria-expanded="true" aria-controls="lecture-3-body">
    <span class="chapter-toggle-left">
      <span class="chapter-badge">Lecture 3</span>
      <span>
        <span class="chapter-title">Lecture 3 - Birthday Problem and Properties of Probability</span>
        <span class="chapter-subtitle">Complements, probability axioms, inclusion–exclusion, and de Montmort's matching problem</span>
      </span>
    </span>
    <span class="chapter-arrow open" id="lecture-3-arrow" aria-hidden="true">▼</span>
  </button>
  <div class="chapter-body open" id="lecture-3-body" markdown="1">

<div class="note-abstract" markdown="1">

A coincidence can become likely when there are many opportunities for it to occur. The birthday problem illustrates this through counting the complement. Probability axioms give general rules for complements, containment, and overlapping events. Inclusion–exclusion then handles the overlaps in a shuffled deck, giving a surprisingly stable probability of at least one matching card.

</div>

### Notation at a Glance

<div class="notation-panel" markdown="1">

| Symbol | Meaning |
|---|---|
| $$k$$ | Number of people in the birthday problem |
| $$M$$, $$M^c$$ | At least one birthday match, and no birthday matches |
| $$\prod_{j=0}^{k-1}(1-j/365)$$ | Product of the $$k$$ factors for distinct birthdays |
| $$A^c$$ | Complement of event $$A$$ within $$S$$ |
| $$B\cap A^c$$ | Outcomes in $$B$$ but outside $$A$$ |
| $$A\subseteq B$$ | Every outcome in $$A$$ belongs to $$B$$ |
| $$\bigcup_{i=1}^n A_i$$ | At least one of the events $$A_1,\ldots,A_n$$ occurs |
| $$\bigcap_{i\in I}A_i$$ | All events whose indices belong to $$I$$ occur |
| $$n$$ | Number of distinct cards in the matching problem |
| $$\pi(i)$$ | Label on the card in position $$i$$ of a shuffled deck |
| $$A_i=\{\pi(i)=i\}$$ | Card $$i$$ matches its position |
| $$D_n$$ | Number of permutations of $$n$$ objects with no fixed points |
| $$e$$ | Base of the natural logarithm; $$e\approx2.71828$$ |

</div>

### Learning objectives

After studying these notes, you should be able to:

- State the birthday model's assumptions and identify its equally likely outcomes.
- Derive the probability of at least one birthday match by counting the complement.
- Distinguish any matching pair from a match with one specified person's birthday.
- Prove the complement rule, monotonicity, and the two-event addition rule from the probability axioms.
- Explain the alternating signs in inclusion–exclusion.
- Calculate intersection probabilities for specified matching positions in a permutation.
- Derive the matching probability and explain its limit of $$1-e^{-1}$$.

### Part 1 — The birthday problem: defining the model

Suppose $$k$$ people are in a room. What is the probability that **at least two** have the same birthday?

Use the following idealized model:

- There are 365 possible birthdays; February 29 is excluded.
- Each person's birthday is equally likely to be any of those days.
- People's birthdays are mutually independent.
- People are distinguishable: person 1's birthday and person 2's birthday occupy different positions in an outcome.

An outcome is an ordered list of $$k$$ birthdays. Each position has 365 possibilities, so:

$$
\lvert S\rvert=365^k.
$$

The uniformity and independence assumptions make every such list equally likely, with probability $$365^{-k}$$.

Let $$M$$ be the event of at least one match. A match may involve one pair, several pairs, or three or more people on one day. All of these belong to $$M$$.

<div class="warning-box" markdown="1">

**Modeling clarification:** Real birthdays need not be uniformly distributed or independent. The formula below is exact for the stated model; it is not an exact description of every real group. Labeling people does not establish independence—it specifies which outcomes we are counting.

</div>

#### Boundary cases

With zero or one person, a match is impossible. With more than 365 people, a match is certain by the **pigeonhole principle**: assigning more than 365 people to 365 days forces some day to receive at least two people.

With exactly 365 people, a match is extremely likely but not certain: an assignment with one person on each day is still possible.

### Part 2 — Count no matches, then take the complement

Directly counting all possible kinds of matches is difficult because the cases overlap. The complement $$M^c$$ has a simple description: all birthdays are different.

For $$1\le k\le365$$:

| Person | Allowed birthdays if all birthdays must differ |
|---|---:|
| First | 365 |
| Second | 364 |
| Third | 363 |
| $$k$$th | $$365-k+1$$ |

Thus:

$$
\lvert M^c\rvert=365\cdot364\cdots(365-k+1).
$$

Divide by the number of equally likely birthday lists:

$$
P(M^c)=\frac{365\cdot364\cdots(365-k+1)}{365^k}
=\prod_{j=0}^{k-1}\left(1-\frac j{365}\right).
$$

<div class="result-box" markdown="1">

$$
\boxed{P(M)=1-\prod_{j=0}^{k-1}\left(1-\frac j{365}\right),\qquad1\le k\le365.}
$$

For $$k=0$$, the empty product is 1, giving probability 0. For $$k>365$$, use $$P(M)=1$$ rather than extending the product to negative factors.

</div>

**Core idea:** The experiment allows repeated birthdays, so the denominator counts sampling with replacement. The no-match event restricts birthdays to distinct days, so its numerator counts assignments without replacement. Both counts still describe ordered lists for the same labeled people.

#### Worked example: Why 23 people are enough

For 23 people:

$$
P(M)=1-\frac{365\cdot364\cdots343}{365^{23}}
\approx0.507297.
$$

The no-match probability is approximately $$0.492703$$. For 22 people, the match probability is approximately $$0.475695$$, so 23 is the smallest group size with a match probability above 50%.

| People, $$k$$ | Probability of at least one match |
|---:|---:|
| 2 | $$0.002740$$ |
| 10 | $$0.116948$$ |
| 22 | $$0.475695$$ |
| 23 | $$0.507297$$ |
| 30 | $$0.706316$$ |
| 50 | $$0.970374$$ |
| 57 | $$0.990122$$ |
| 100 | $$0.999999693$$ |

<figure>
  <img src="/assets/img/statistic-101/lecture-3-textbook-fig-1-4-birthday.png" alt="Birthday-match probability rises with group size, crossing one half at 23 people and approaching one by 100 people." style="display: block; width: 100%; max-width: 680px; height: auto; margin: 0 auto;">
  <figcaption>Birthday-match probability under the independent, uniform 365-day model. Reproduced from Joseph K. Blitzstein and Jessica Hwang, <em>Introduction to Probability</em>, Figure 1.4, p. 12.</figcaption>
</figure>

#### Why the result is less surprising after counting pairs

A group of 23 people contains:

$$
\binom{23}{2}=253
$$

pairs. The event concerns any of these pairs, not just the 22 comparisons involving one particular person. The number of pairs grows quadratically with group size.

<div class="misconception-block" markdown="1">

**Incorrect:** There are 253 pairs, each matching with probability $$1/365$$, so the probability of a match is $$253/365$$.

**Correction:** Pair-match events overlap. If three people share a birthday, all three pairs among them match. Adding their probabilities counts that outcome repeatedly. The ratio $$253/365\approx0.693151$$ is not the probability of at least one match.

</div>

#### Supplementary comparison: Someone shares your birthday

Fix your birthday and consider 22 other people under the same independent, uniform model. Each avoids your birthday with probability $$364/365$$. Therefore:

$$
P(\text{at least one shares your birthday})
=1-\left(\frac{364}{365}\right)^{22}
\approx0.058571.
$$

This is about 5.86%, compared with 50.73% for any match among all 23 people. The first event asks for a match with one specified birthday; the second allows any pair to match.

### Part 3 — Probability axioms and the complement rule

A probability function assigns every event a number in $$[0,1]$$. The axioms are:

$$
P(\varnothing)=0,\qquad P(S)=1,
$$

and, for pairwise disjoint events:

$$
P\left(\bigcup_{i=1}^{\infty}A_i\right)
=\sum_{i=1}^{\infty}P(A_i).
$$

These rules apply beyond finite, equally likely sample spaces. The following properties are consequences of the axioms, rather than additional assumptions.

#### Derive the complement rule

The events $$A$$ and $$A^c$$ are disjoint, and their union is $$S$$. By additivity:

$$
1=P(S)=P(A\cup A^c)=P(A)+P(A^c).
$$

Rearranging gives:

$$
\boxed{P(A^c)=1-P(A).}
$$

This justifies the final step in the birthday calculation. It also applies when individual outcomes have unequal probabilities or when the sample space is infinite.

**Core idea:** An event and its complement divide the entire experiment into two mutually exclusive possibilities, whose probabilities sum to 1.

### Part 4 — Monotonicity: a larger event cannot be less likely

<div class="example-block" markdown="1">
<div class="ex-title">Monotonicity <span class="ex-pill pill-thm">Theorem</span></div>

If $$A\subseteq B$$, then:

$$
\boxed{P(A)\le P(B).}
$$

</div>

#### Proof by disjoint decomposition

Separate $$B$$ into the outcomes in $$A$$ and the outcomes outside $$A$$:

$$
B=A\cup(B\cap A^c).
$$

These two pieces are disjoint. Hence:

$$
P(B)=P(A)+P(B\cap A^c)\ge P(A),
$$

because probabilities are nonnegative.

<figure>
  <img src="/assets/img/statistic-101/lecture-3-textbook-monotonicity.png" alt="Event A lies inside event B; the remainder of B is labeled B intersection A complement." style="display: block; width: 100%; max-width: 430px; height: auto; margin: 0 auto;">
  <figcaption>Decomposing a containing event into disjoint pieces. Reproduced from Blitzstein and Hwang, <em>Introduction to Probability</em>, diagram in the proof of Theorem 1.6.2, p. 22.</figcaption>
</figure>

#### Supplementary example: Nested dice events

Roll a fair six-sided die. Let $$A=\{6\}$$ and $$B=\{4,5,6\}$$. Since $$A\subseteq B$$:

$$
P(A)=\frac16\le\frac36=P(B).
$$

The extra outcomes $$B\cap A^c=\{4,5\}$$ contribute probability $$2/6$$.

<div class="warning-box" markdown="1">

**Containment need not give strict inequality.** Even if $$A$$ is a proper subset of $$B$$, it is possible that $$P(A)=P(B)$$. Strict inequality holds exactly when $$P(B\cap A^c)>0$$. A nonempty event need not have positive probability in every model.

</div>

### Part 5 — Two overlapping events: the addition rule

<div class="result-box" markdown="1">

For any two events $$A$$ and $$B$$:

$$
\boxed{P(A\cup B)=P(A)+P(B)-P(A\cap B).}
$$

</div>

The sum $$P(A)+P(B)$$ counts outcomes in the intersection twice. Subtracting $$P(A\cap B)$$ leaves each outcome in the union counted once.

<figure>
  <img src="/assets/img/statistic-101/lecture-3-textbook-two-event-union.png" alt="Two overlapping events A and B inside sample space S, with their shared region labeled A intersection B." style="display: block; width: 100%; max-width: 430px; height: auto; margin: 0 auto;">
  <figcaption>The intersection is included in both event probabilities. Reproduced from Blitzstein and Hwang, <em>Introduction to Probability</em>, diagram in the proof of Theorem 1.6.2, p. 22.</figcaption>
</figure>

#### Proof using the axioms

Write the union as two disjoint pieces:

$$
A\cup B=A\cup(B\cap A^c).
$$

Therefore:

$$
P(A\cup B)=P(A)+P(B\cap A^c).
$$

Also, $$B=(A\cap B)\cup(B\cap A^c)$$ is a disjoint union, so:

$$
P(B\cap A^c)=P(B)-P(A\cap B).
$$

Substitution gives the addition rule. No independence assumption is needed. For disjoint events, the intersection has probability zero and the rule reduces to direct addition.

#### Supplementary worked example: An even result or a result above 3

For a fair die, let $$A=\{2,4,6\}$$ and $$B=\{4,5,6\}$$. Their intersection is $$\{4,6\}$$. Hence:

$$
P(A\cup B)=\frac36+\frac36-\frac26=\frac46=\frac23.
$$

The union is $$\{2,4,5,6\}$$, confirming the result by direct counting.

**Core idea:** “Or” includes outcomes where both events occur, but each such outcome contributes only once to the union.

### Part 6 — Inclusion–exclusion for three or more events

#### Three events

$$
\boxed{\begin{aligned}
P(A\cup B\cup C)
={}&P(A)+P(B)+P(C)\\
&-P(A\cap B)-P(A\cap C)-P(B\cap C)\\
&+P(A\cap B\cap C).
\end{aligned}}
$$

<figure>
  <img src="/assets/img/statistic-101/lecture-3-textbook-three-event-union.png" alt="Three overlapping events A, B, and C, including pairwise overlaps and a central triple overlap." style="display: block; width: 100%; max-width: 400px; height: auto; margin: 0 auto;">
  <figcaption>Pairwise corrections remove the central overlap too many times, so the triple intersection is added back. Reproduced from Blitzstein and Hwang, <em>Introduction to Probability</em>, Section 1.6, p. 23.</figcaption>
</figure>

Track how often a particular outcome contributes:

| Events containing the outcome | Single-event additions | Pairwise subtractions | Triple addition | Net count |
|---|---:|---:|---:|---:|
| Exactly one | 1 | 0 | 0 | 1 |
| Exactly two | 2 | 1 | 0 | 1 |
| All three | 3 | 3 | 1 | 1 |

The pairwise intersections include the triple intersection. Subtracting all three pairwise terms removes a central outcome three times after adding it three times, leaving zero. The final addition restores its contribution to one.

#### General formula

For events $$A_1,\ldots,A_n$$:

$$
\boxed{
P\left(\bigcup_{i=1}^{n}A_i\right)
=\sum_{r=1}^{n}(-1)^{r+1}
\sum_{1\le i_1<\cdots<i_r\le n}
P(A_{i_1}\cap\cdots\cap A_{i_r}).
}
$$

Add single-event probabilities, subtract two-event intersections, add three-event intersections, and continue with alternating signs. Each unordered group of indices appears once; the condition $$i_1<\cdots<i_r$$ prevents repeated listings of the same intersection.

**Core idea:** Inclusion–exclusion corrects overlap systematically. Symmetry makes it especially useful when all intersections involving the same number of specified events have the same probability.

<div class="misconception-block" markdown="1">

**Incorrect:** For three events, subtracting the three pairwise intersections is enough.

**Correction:** The triple intersection must be added back. Pairwise intersections mean that both named events occur, whether or not a third event also occurs; they do not mean “exactly those two.”

</div>

### Part 7 — de Montmort's matching problem

Shuffle $$n\ge1$$ distinct cards labeled $$1,2,\ldots,n$$, with all $$n!$$ permutations equally likely. Reveal them in order while counting $$1,2,\ldots,n$$. Win if at least one revealed card matches the number called out.

A match is a **fixed point** of the permutation. If the deck is $$(3,2,1,4)$$, positions 2 and 4 match; positions 1 and 3 do not.

Let:

$$
A_i=\{\pi(i)=i\}.
$$

The event of winning is $$A_1\cup\cdots\cup A_n$$. The events overlap because several positions can match at once.

#### Step 1: One specified position matches

Fix card $$i$$ in position $$i$$. The remaining $$n-1$$ cards may be arranged freely, giving $$(n-1)!$$ favorable permutations:

$$
P(A_i)=\frac{(n-1)!}{n!}=\frac1n.
$$

#### Step 2: Several specified positions match

For distinct positions $$i_1,\ldots,i_r$$, fixing their cards leaves $$(n-r)!$$ arrangements:

$$
P(A_{i_1}\cap\cdots\cap A_{i_r})=\frac{(n-r)!}{n!}.
$$

For example:

$$
P(A_i\cap A_j)=\frac1{n(n-1)},\qquad
P(A_i\cap A_j\cap A_\ell)=\frac1{n(n-1)(n-2)}.
$$

Fixing the specified positions does **not** forbid additional matches among the remaining positions. That is exactly what an intersection requires: all named events occur, possibly along with others.

#### Step 3: Group the inclusion–exclusion terms

There are $$\binom nr$$ ways to choose the $$r$$ specified matching positions. Each intersection has the same probability, so the total at order $$r$$ is:

$$
\binom nr\frac{(n-r)!}{n!}
=\frac{n!}{r!(n-r)!}\frac{(n-r)!}{n!}
=\frac1{r!}.
$$

Therefore:

<div class="result-box" markdown="1">

$$
\boxed{P(\text{at least one match})
=\sum_{r=1}^{n}\frac{(-1)^{r+1}}{r!}
=1-\frac1{2!}+\frac1{3!}-\cdots+\frac{(-1)^{n+1}}{n!}.}
$$

</div>

**Core idea:** A complicated union becomes manageable because intersection probabilities depend only on how many positions are specified. The binomial coefficient counts the choices of positions; the factorial ratio counts decks satisfying those choices.

#### Worked example: Three cards

For $$n=3$$:

$$
P(\text{win})=1-\frac12+\frac16=\frac23.
$$

All six decks can be listed:

| Deck order | Matching positions | Result |
|---|---|---|
| $$(1,2,3)$$ | 1, 2, 3 | Win |
| $$(1,3,2)$$ | 1 | Win |
| $$(2,1,3)$$ | 3 | Win |
| $$(2,3,1)$$ | None | Lose |
| $$(3,1,2)$$ | None | Lose |
| $$(3,2,1)$$ | 2 | Win |

Four of six permutations win. No permutation has exactly two matching positions: if two cards are fixed, the remaining card is forced into its own position.

<div class="misconception-block" markdown="1">

**Incorrect:** Each position matches with probability $$1/n$$, so the probability of winning is $$n(1/n)=1$$.

**Correction:** The events are not disjoint. The fully ordered deck belongs to every $$A_i$$ and is counted $$n$$ times in that sum. Inclusion–exclusion corrects those repeated contributions.

**Another trap:** The match events are not independent. For $$n\ge2$$, $$P(A_i\cap A_j)=1/[n(n-1)]$$, whereas $$P(A_i)P(A_j)=1/n^2$$.

</div>

### Part 8 — Derangements and the large-deck limit

A **derangement** is a permutation with no fixed points. It is a losing deck in the matching game.

Taking the complement of the winning probability gives:

$$
P(\text{no matches})=\sum_{r=0}^{n}\frac{(-1)^r}{r!}.
$$

Multiply by the total number of permutations:

$$
\boxed{D_n=n!\sum_{r=0}^{n}\frac{(-1)^r}{r!}.}
$$

For example, $$D_3=6(1-1+1/2-1/6)=2$$, agreeing with the two losing decks above.

#### The limiting probability

The exponential series gives:

$$
e^{-1}=\sum_{r=0}^{\infty}\frac{(-1)^r}{r!}.
$$

Consequently:

$$
\boxed{P(\text{no matches})\longrightarrow e^{-1}\approx0.367879,}
$$

$$
\boxed{P(\text{at least one match})\longrightarrow1-e^{-1}\approx0.632121.}
$$

| Cards, $$n$$ | Exact winning probability | Decimal |
|---:|---|---:|
| 1 | $$1$$ | $$1.000000$$ |
| 2 | $$1-1/2!$$ | $$0.500000$$ |
| 3 | $$1-1/2!+1/3!$$ | $$0.666667$$ |
| 4 | $$1-1/2!+1/3!-1/4!$$ | $$0.625000$$ |
| 5 | $$1-1/2!+1/3!-1/4!+1/5!$$ | $$0.633333$$ |
| 6 | $$1-1/2!+1/3!-1/4!+1/5!-1/6!$$ | $$0.631944$$ |

The finite probabilities alternate around the limit; they do not increase monotonically with deck size. A larger deck provides more candidate matching positions, but each specified position matches with smaller probability $$1/n$$.

#### Supplementary clarification: Accuracy of the limit

The alternating-series remainder bounds the error by the first omitted term:

$$
\left|P(\text{win})-(1-e^{-1})\right|\le\frac1{(n+1)!}.
$$

For six cards, the error is at most $$1/7!\approx0.000198413$$. For 52 distinct numbered cards, the limiting value is an extraordinarily accurate approximation, although the finite alternating sum remains the exact probability.

### Part 9 — Original practice questions

Try these before reading the answers.

1. Under the birthday model, find the probability of at least one match among three people. Explain why there are two different counting rules in the calculation.
2. What is the smallest group size that guarantees a birthday match? Why does a group of 365 people not guarantee one?
3. Fix your birthday. Find the probability that at least one of ten other people shares it, under the independent, uniform model. Is this the same event as any birthday match among all eleven people?
4. Suppose $$A\subseteq B$$, $$P(A)=0.25$$, and $$P(B)=0.60$$. Find $$P(B\cap A^c)$$ and $$P(B^c)$$.
5. Suppose $$P(A)=0.60$$, $$P(B)=0.50$$, and $$P(A\cap B)=0.20$$. Find the probabilities of the union, neither event, and exactly one event.
6. Three events each have probability $$0.40$$. Each pairwise intersection has probability $$0.15$$, and the triple intersection has probability $$0.05$$. Find the probability of their union. What answer would omitting the triple correction give?
7. Shuffle five distinct numbered cards uniformly. Find the probability that positions 1 and 3 both match. How many permutations satisfy this condition? Does the condition forbid other matches?
8. For four distinct numbered cards, find the probability of winning the matching game and the number of derangements.
9. In a deck of four distinct numbered cards, explain why the probability that positions 1 and 2 both match is not $$1/16$$.

### Part 10 — Practice answers

#### 1. Three birthdays

The denominator counts all birthday assignments with repetition allowed. The no-match numerator counts only assignments of distinct birthdays:

$$
P(M)=1-\frac{365\cdot364\cdot363}{365^3}
=\frac{1093}{133225}\approx0.008204.
$$

The probability is about 0.8204%. Taking the complement includes every possible kind of match without counting overlapping match cases separately.

#### 2. A guaranteed match

The smallest size is 366. With 365 people, assigning exactly one person to each day produces no match. With 366 people, there are more people than available days, so at least two must share a day.

#### 3. A specified birthday

All ten people avoid your birthday with probability $$(364/365)^{10}$$, so:

$$
P(\text{at least one shares yours})
=1-\left(\frac{364}{365}\right)^{10}
\approx0.027062.
$$

This is about 2.7062%. Any match among eleven people also includes pairs among the other ten, so it is a different, larger event.

#### 4. Containment and complement

The disjoint decomposition of $$B$$ gives:

$$
P(B\cap A^c)=P(B)-P(A)=0.60-0.25=0.35.
$$

The complement rule gives $$P(B^c)=1-0.60=0.40$$.

#### 5. Union, neither, and exactly one

$$
P(A\cup B)=0.60+0.50-0.20=0.90.
$$

Neither event is the complement of the union, so its probability is $$0.10$$.

Exactly one consists of the disjoint events $$A\cap B^c$$ and $$B\cap A^c$$:

$$
P(\text{exactly one})=(0.60-0.20)+(0.50-0.20)=0.70.
$$

The union includes the both-events case; exactly one excludes it.

#### 6. Three-event correction

$$
P(A\cup B\cup C)=3(0.40)-3(0.15)+0.05=0.80.
$$

Omitting the triple correction gives $$0.75$$, undercounting the union by the probability $$0.05$$ of the triple intersection.

#### 7. Two specified matching positions

Fix cards 1 and 3 in positions 1 and 3. Arrange the remaining three cards in $$3!=6$$ ways. Thus:

$$
P(A_1\cap A_3)=\frac{3!}{5!}=\frac1{20}.
$$

Other positions may also match. The intersection requires at least the two specified matches, not exactly two matches.

#### 8. Four-card game

$$
P(\text{win})=1-\frac1{2!}+\frac1{3!}-\frac1{4!}
=\frac{15}{24}=\frac58.
$$

The no-match probability is $$3/8$$, so:

$$
D_4=4!\cdot\frac38=9.
$$

#### 9. Dependence between matching positions

Each specified position matches with probability $$1/4$$. But fixing two specified cards leaves $$2!$$ favorable permutations out of $$4!$$:

$$
P(A_1\cap A_2)=\frac{2!}{4!}=\frac1{12}.
$$

Multiplying $$1/4$$ by $$1/4$$ would require independence, which does not hold for these events.

### Part 11 — Quick revision sheet

| Concept | Essential fact |
|---|---|
| Birthday sample space | $$365^k$$ equally likely ordered assignments under uniformity and mutual independence |
| No birthday match | $$\prod_{j=0}^{k-1}(1-j/365)$$ for $$1\le k\le365$$ |
| At least one birthday match | One minus the no-match probability; exceeds 50% first at $$k=23$$ |
| Guaranteed birthday match | $$k>365$$ |
| Complement | $$P(A^c)=1-P(A)$$ |
| Monotonicity | $$A\subseteq B\Rightarrow P(A)\le P(B)$$ |
| Two-event addition | $$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$ |
| Inclusion–exclusion | Add singles, subtract pairs, add triples, and continue alternating |
| $$r$$ specified card matches | $$(n-r)!/n!$$ |
| Total order-$$r$$ contribution | $$\binom nr(n-r)!/n!=1/r!$$ |
| Matching-game win | $$\sum_{r=1}^n(-1)^{r+1}/r!$$ |
| Derangements | $$D_n=n!\sum_{r=0}^n(-1)^r/r!$$ |
| Large-deck win probability | $$1-e^{-1}\approx0.632121$$ |

### Term Glossary

<div class="glossary-entry" markdown="1">
<div class="gterm">Birthday match <span class="gcat cat-defn">Definition</span></div>

An event in which at least two people share a birthday. It includes several pairs or larger groups sharing a day, not only exactly one matching pair.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Pigeonhole principle <span class="gcat cat-prop">Counting principle</span></div>

Placing more objects than boxes into boxes forces at least one box to contain two or more objects.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Complement rule <span class="gcat cat-thm">Theorem</span></div>

The probability that an event does not occur is one minus the probability that it occurs.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Monotonicity <span class="gcat cat-thm">Theorem</span></div>

If one event is contained in another, its probability cannot exceed that of the containing event.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Inclusion–exclusion <span class="gcat cat-thm">Theorem</span></div>

A formula for the probability of a union that corrects repeated contributions from overlapping events using alternating sums of intersection probabilities.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Permutation <span class="gcat cat-defn">Definition</span></div>

An ordering of distinct objects. There are $$n!$$ permutations of $$n$$ distinct objects.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Fixed point <span class="gcat cat-defn">Definition</span></div>

A position $$i$$ at which a permutation leaves the label unchanged: $$\pi(i)=i$$. In the matching game, it is a card whose label equals its position.

</div>

<div class="glossary-entry" markdown="1">
<div class="gterm">Derangement <span class="gcat cat-defn">Definition</span></div>

A permutation with no fixed points. In the matching game, it corresponds to a deck with no matching positions.

</div>

<div class="ref-tags">
  <span class="ref-tag">Statistics 110</span>
  <span class="ref-tag">Lecture 3</span>
  <span class="ref-tag">Birthday problem</span>
  <span class="ref-tag">Probability properties</span>
  <span class="ref-tag">Inclusion–exclusion</span>
  <span class="ref-tag">Matching problem</span>
</div>

  </div>
</div>
