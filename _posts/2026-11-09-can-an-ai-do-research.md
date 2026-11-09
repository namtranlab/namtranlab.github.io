---
layout: distill
title: Can an AI Do Research While I Sleep?
description: A story about teaching an LLM agent to hunt for trading signals, and what it taught me about automating research.
tags: AI Autoresearch
giscus_comments: true
date: 2026-11-09
featured: true
thumbnail: https://media.warriortrading.com/2018/06/blog_alpha.jpg

authors:
  - name: Nam Tran
    url: "/"
    affiliations:
      name: MSE, NTU

toc:
  - name: "It started with a question"
  - name: "Why trading signals?"
  - name: "The idea: a research loop"
  - name: "Building the tools: WQBrainSim"
  - name: "Writing the rulebook: skills for the agent"
  - name: "Letting it run"
  - name: "What I found"
  - name: "Beyond trading (i.e., autoresearch for computational modeling)"
---

## It started with a question {#it-started-with-a-question}

Lately I have been curious about one thing: **can a large language model do research on its own?**

I don't mean answering a question or writing a function when asked. I mean the whole loop a researcher goes through every day:

> have an idea → test it → look at the result → learn something → have a better idea → repeat

It sounds simple, but it asks a lot from the AI. It has to remember what it already tried, not fool itself with lucky results, know when to give up on a dead end, and keep going for hours without someone holding its hand.

So I wanted a playground where I could try this for real, with real feedback, real limits, and real consequences.

Before we start you can find all the codes/kills used for this test in this repo here:

[https://github.com/namtranlab/WQBrainResearch](https://github.com/namtranlab/WQBrainResearch)


## Why trading signals? {#why-trading-signals}

I picked a fun one: **finding alphas on WorldQuant BRAIN.**

An *alpha* is a small formula that tries to predict which stocks will do better than others tomorrow. Something like:

```
rank(close - open) / (high - low)
```

Read it as: Stocks with stronger opening-to-closing price performance relative to their intraday trading range are more likely to move upward.

BRAIN lets you write such a formula, runs a backtest over years of market data, and gives you back a score card: Sharpe ratio, returns, turnover, a *fitness* score and a list of pass/fail checks.

Why is this a good playground?

- **LLMs are very good at spotting patterns.** Alpha research is mainly pattern hunting
- **The feedback is clear and numeric.** Every idea gets a score. No arguing about whether it "worked."
- **The search space is huge.** Thousands of data fields, hundreds of operators, many settings. Too much for a human to explore by hand, which is exactly where an agent could help.

It felt like the perfect small world to test.

## The idea: a research loop {#the-idea-a-research-loop}

Here is what I wanted the AI to do, again and again:

```
  ┌─▶ 1. Check the notebook     What did we try? What worked? What failed?
  │            │
  │   2. Update the lessons     Is "smoothing helps this kind of signal" still true?
  │            │
  │   3. Generate / polish      Half brand-new ideas, half fixes of "almost good" ones
  │            │
  │   4. Test                   Backtest each idea on BRAIN and collect the scores
  │            │
  │   5. Submit the best        Once a day, only ideas that pass every check
  │            │
  └────────────┘
```

Step 3 is where the thinking happens, in two ways:

- **New ideas (explore)**: try data that fewer people have explored, starting from a simple story ("companies that many people bet against should do worse, because...").
- **Polish (exploit)**: take an idea that *almost* passed and fix it: try a different set of stocks, smooth the signal over a few days, compare stocks only within their own industry, swap one ingredient, or mix it with another weak idea.

The hope is simple: every round makes the next round a little smarter.

## Building the tools: WQBrainSim {#building-the-tools-wqbrainsim}

Before the AI can do anything, it needs hands. So I first built **WQBrainSim**, a small command-line tool that talks to BRAIN.

Full confession: I vibe-coded it. I described what I wanted, Claude wrote the code, and I tested it, poked at it, and asked for changes until it behaved. Who writes code by hand these days? :)

It lets me (and the agent) do things like:

```bash
uv run wqbrainsim run --alpha example/alpha.json --settings example/settings.json
uv run wqbrainsim datafields --region USA --delay 1 --universe TOP3000
uv run wqbrainsim check <ALPHA_ID>
```

What it does for us:

- **Simulates/Submits** an alpha and waits for the result.
- **Remembers every job** in a small SQLite database.
- **Looks up the catalog**: which datasets, fields and operators exist. 

A lot of the boring work went into handling the messy real world: rate limits, expired logins, a job whose submission may or may not have gone through. The best practice is to create a MCP server for these tools.

## Writing the rulebook: skills for the agent {#writing-the-rulebook-skills-for-the-agent}

Next, I needed to teach the AI *how* to be a researcher. I did this with two layers.

### Layer 1: the hard rules live in code (`research.py`)

This was my most important design decision: **anything that must never go wrong is enforced by code, not by asking nicely in a prompt.**

`research.py` wraps WQBrainSim and refuses to break the rules, no matter what the agent writes. And yes, of course I vibe-coded this one too :) There is something funny about an AI writing the rulebook that keeps another AI in line. For example:

| Rule | Why |
|---|---|
| One simulation at a time, 4 to 7 minutes apart, at most 15 per hour | Be polite to the platform and never hit the limit |
| At least half of each batch must be new ideas | Stop the agent from endlessly tweaking one alpha |
| At most 3 variants of one family per batch | Spread the bets |
| A family with 5 tries in a row and no real gain is "exhausted" | Know when to give up |
| No rerun of the exact same input | No wasting simulations on hope |
| Only GOOD-grade alphas are pooled; at most 3 submissions a day | Quality over quantity |


### Layer 2: the judgment lives in skills (`workflow/`)

The creative part, *what to try next*, is guided by a set of Claude Code skills:

| Skill | Role |
|---|---|
| `wq` | The orchestrator: runs the loop |
| `wq-setup` | First-time setup: review seed alphas, pick default settings, agree on the policy with me |
| `wq-generate` | New ideas from unexplored datasets, always starting from an economic hypothesis |
| `wq-improve` | Improve near misses: settings research, a playbook for fitness, Sharpe, turnover, correlation |
| `wq-submit` | End-of-day submission plus a written report for each submitted alpha |

Plus a shared `PROTOCOL.md`: the commands, file formats and grade lines all skills agree on.

The skills read like advice from a senior colleague:

> *"Change one setting at a time when diagnosing, and tie each change to a mechanism."*

### Memory: the lab notebook

A researcher without a notebook repeats the same mistakes. So the agent keeps one:

- `R history`: best alpha of each family, building blocks, near misses.
- `R patterns`: which kinds of changes actually raised fitness.
- `R lessons`: short, testable claims like "SUBINDUSTRY neutralization helps sparse fundamental signals", each with its own record of supporting and contradicting evidence.

Every batch, the agent reads the notebook before writing new ideas, and 2 or 3 candidates in each batch are deliberate *tests* of a lesson. 

## Letting it run {#letting-it-run}

This is a test so I run it in **interactive mode**, so I can watch every step and steer when I want.

**Setup** (once): put your BRAIN login in `WQBrainSim/.env`, copy `claude-settings.proposed.json` to `.claude/settings.json`, and install the skills. 

**Start** with `/wq`. The first time, the agent reviews the 159 seed alphas, proposes default settings and the submission policy.

**Then it loops on its own:** read the notebook → write a batch of 10 to 15 ideas → simulate them one by one (about an hour per batch) → update lessons → repeat. Once a day it submits the best alphas and writes a report for each.

You can jump in any time: *"Why this dataset?"*, *"Try analyst revisions next."*, *"Stop after this batch."* Every step saves its state, so you can close Claude Code and type `/wq` later to carry on.

## What I found {#what-i-found}

- **It workded.** The loop helped me find a bunch of alphas and reach Gold level in just 5 days. BRAIN caps points at 2k per day, and Gold needs 10k.

- **The agent can be lazy, or less creative.** Once it found a good strategy, it kept sticking with it. For example, it kept sorting stocks into ten groups by their recent return and then ranking the signal inside each group, like this:

  ```
  group_rank(signal, bucket(rank(ts_sum(returns, h)), range="0,1,0.1"))
  ```

  This creates many correlated signals and limits its ability to find new transformations.


Here is one alpha the loop found. BRAIN graded it **SPECTACULAR**.

**The score card** (TOP3000, delay 1, SECTOR neutralization, decay 6, truncation 0.08):

| Sharpe | Fitness | Returns | Turnover | Drawdown | Self-correlation |
|---|---|---|---|---|---|
| 2.88 | 3.16 | 15.1% | 12.4% | 4.09% | 0.71 |

**The formula** looks scary at first:

```
group_rank(ts_mean(rp_nip_technical, 60), bucket(rank(ts_sum(returns, 60)), range="0,1,0.1")) 
+ group_rank(ts_mean(rp_nip_price, 60), bucket(rank(ts_sum(returns, 60)), range="0,1,0.1"))
+ group_rank(ts_mean(rp_nip_society, 60), bucket(rank(ts_sum(returns, 60)), range="0,1,0.1")) 
+ group_rank(ts_mean(rp_nip_ptg, 60), bucket(rank(ts_sum(returns, 60)), range="0,1,0.1"))
+ group_rank(ts_mean(rp_nip_inverstor, 60), bucket(rank(ts_sum(returns, 60)), range="0,1,0.1")) 
+ 0.6 * group_rank(-rank(ts_rank(close, 10)) * rank(close / open), bucket(rank(ts_sum(returns, 5)), range="0,1,0.1")) 
+ 0.6 * group_rank(-ts_delta(((close - low) - (high - close)) / (high - low + 0.001 * close), 9), bucket(rank(ts_sum(returns, 5)), range="0,1,0.1")) 
+ rank(ts_corr(close, ts_delay(close, 5), 500))
```

But it is really just three simple ideas added together:

| Legs | What they look at | Direction | Share of weight |
|---|---|---|---|
| L1 to L5 | Expected price impact of five kinds of news (technical analysis, price moves, society, analyst price targets, investor relations), averaged over 60 days | Favor | ≈ 69% |
| L6, L7 | Stocks near their 10-day high that rose today; closes creeping toward the top of the daily range | Bet against | ≈ 17% |
| L8 | How smoothly the price has moved over about two years | Favor | ≈ 14% |

In plain words:

- **Slow news (most of the weight).** Some news moves prices more than others. The alpha favors stocks that have had high-impact news over the last quarter, on the idea that the market has not fully priced it in yet.
- **Short-term pullback.** Stocks that jumped up in the last few days often fall back a little. The alpha leans gently against them, which also offsets some risk.
- **Steady trend.** Stocks whose price moves smoothly over years get a small bonus. This slow piece helps the alpha behave the same across big and small stocks.

So it is slow news + fast pullbacks + a long-term steady-trend signal.

## Beyond trading (i.e., autoresearch for computational modeling) {#beyond-trading-i-e-autoresearch-for-computational-modeling}

If we look at scientific research, we see the same playbook:

```
      1. Review the literature   Build knowledge: what is known, what has been tried?
         │
      2. Choose the problem      Which question/problem is worth solving?
         │
  ┌─▶ 3. Propose / polish ideas  New hypotheses, or fixes of "almost good" ones
  │      │
  │   4. Test the ideas          Run the calculations or do experiment
  │      │
  │   5. Evaluate the results    Should we keep this candinate/hypothesis
  │      │
  └──────┘
```

An AI agent can run most of this loop leaving human focus on critical steps such as **choosing which problem is worth working on**, and **the final check of the results** before anything leaves the lab. 

### My initial idea for a computational modeling agent

I imagine a similar design, rebuilt for a scientific field:

**1. Tools (the hands)**:

- **Input builder**: create input files from a structured description, and validate them before anything is submitted.
- **HPC connector**: submit jobs to the scheduler (SLURM, PBS), track them in a local database, resume after interruptions, respect the allocation budget.
- **Result analyzer**: parse outputs, detect common failures (no convergence, wall-time exceeded, imaginary frequencies), and summarize the key numbers.

**2. A rulebook in code** — the equivalent of `research.py`. For example:

- No rerun of an identical input without a stated reason.
- Required convergence tests before a result counts.
- A lesson system with evidence and retirement.

**3. Skills (the judgment)** — setup, generate, improve, report — written in the language of the field.

**4. A literature RAG (the library)** — In the alpha project, the agent's "library" is the dataset catalog. For science, it should be the **literature**:

- Collect papers, method guides and benchmark studies in the field.
- Index them so the agent can retrieve relevant passages: "what parameters did others use for this class of materials?", "what is a known failure mode for this method?"
- Use them as an guidance to: seed hypotheses, sensible default settings...

The agent would then start where a good PhD student starts: by reading, not by guessing.
