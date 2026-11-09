---
layout: page
title: AI-Agent Autoresearch for Catalyst Design
description: A new project building an AI research agent that runs the hypothesis–simulation–analysis loop on its own, starting with single-atom catalysts for the hydrogen evolution reaction.
img: assets/img/publication_preview/ai_autoresearch.png
importance: 1
category: Research
---

Computational catalysis follows a familiar loop: read what others have done, propose a candidate, build and run the calculations, analyze the results, learn from them, and try again. Most of a researcher's time goes into the repetitive middle of this loop, such as preparing inputs, babysitting HPC jobs, and parsing outputs, rather than into the decisions that matter.

In this new project, we are building an **AI research agent** that runs this loop on its own. The idea grew out of an experiment where an LLM agent searched for trading signals around the clock, guided by a rulebook in code and a lab notebook of lessons (see the blog post [Can an AI Do Research While I Sleep?](/blog/2026/can-an-ai-do-research/)). I am now bringing the same design to computational modeling.

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/img/publication_preview/ai_autoresearch.png" title="AI-agent autoresearch loop" alt="The researcher sets the problem, rules and budget and checks the final results; an AI agent runs a loop of reading the literature, proposing candidates, building and running GC-DFT jobs on HPC, analyzing results, and updating lessons. The first target is the hydrogen evolution reaction on single-atom catalysts, aiming for a hydrogen adsorption free energy near zero." class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Fig. 1. The autoresearch loop. The researcher chooses the problem, sets the rules, and checks the final results. The agent reads the literature, proposes candidates, runs the calculations, and learns from each round.
</div>

### How the agent is built

- **Tools (the hands):** an input builder that creates and validates calculation inputs, an HPC connector that submits and tracks jobs on the scheduler and can resume after interruptions, and a result parser that catches common failures such as non-convergence or exceeded wall time.
- **A rulebook in code:** hard limits that the agent cannot override, such as no identical reruns, required convergence tests before a result counts, and a fixed HPC budget.
- **Skills (the judgment):** step-by-step guidance for generating ideas, improving near misses, and writing reports, in the language of the field.
- **A literature library:** retrieval over papers and benchmark studies, so the agent starts like a good PhD student, by reading rather than guessing.
- **A lab notebook:** short, testable lessons with supporting and contradicting evidence, which the agent reads before each new round.

### First target: single-atom catalysts for HER

As a first test case, the agent will search for **single-atom catalysts (SACs) for the hydrogen evolution reaction (HER)**. HER is a good starting point because it has a simple, well-established activity descriptor: the hydrogen adsorption free energy, ΔG<sub>H*</sub>, should be close to zero. At the same time, the design space is large, covering the choice of metal center, coordinating atoms, and carbon support, which is too much to explore by hand.

The agent will combine this descriptor with the potential-dependent, grand-canonical DFT methods from our [single-atom catalyst work](/projects/1_project/), and check candidates for stability as well as activity. As always, the researcher stays in charge of choosing the problem and of the final check before any result leaves the lab.

We will share progress and results here as the project develops.
