---
layout: page
title: Accelerating Single-Atom Catalyst Design through Multiscale Modeling and Machine Learning
description: Combining grand-canonical DFT, kinetic Monte Carlo, and machine learning to understand and design single-atom catalysts for electrochemical reactions.
img: https://onlinelibrary.wiley.com/cms/asset/42906240-8917-4454-991d-6b8493fc047d/advs202102886-fig-0002-m.png
importance: 1
category: Research
---

Single-atom catalysts (SACs), such as isolated Fe atoms in nitrogen-doped carbon (Fe–N–C), use nearly every metal atom as an active site, which makes them attractive for electrochemical CO<sub>2</sub> reduction (CO<sub>2</sub>RR). Under working conditions, however, the active site is not static. It responds to the applied potential, to adsorbates, and to the surrounding electrolyte. Conventional constant-charge DFT models with a fixed active site often miss this behavior.

This project combines three methods to capture SACs under realistic conditions:

- **Grand-canonical DFT (GC-DFT)** treats the electrode at a constant potential, giving potential-dependent reaction energetics and barriers.
- **Kinetic Monte Carlo (KMC)** turns these energetics into activity, selectivity, and site coverages that can be compared directly with experiments.
- **Machine learning (ML)** learns from the computed data to screen large spaces of metal centers and coordination environments, so that only promising candidates go on to expensive simulations.

### Highlight: dynamic active sites in Fe–N–C

Experiments on Fe–N–C catalysts raise several puzzles. Which step limits the rate? Why do Fe sites stay active at high potentials even though CO should poison them? Why does the hydrogen evolution reaction outcompete CO<sub>2</sub>RR as the potential becomes more negative?

Using GC-DFT and KMC, we proposed a **dual-side adsorption mechanism**, inspired by dynamic active sites in enzymes. Species adsorb on both sides of the Fe center, and this changes the site's electronic structure during the reaction. A key result is that **the rate-determining step is not fixed; it changes with the applied potential**. This one picture explains the observed activity trends, the CO tolerance, and the competition with hydrogen evolution [1].

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.html path="assets/img/publication_preview/TOC_angewandte_2024.jpeg" title="Dual-side adsorption on Fe–N–C" alt="Dual-side adsorption mechanism on an Fe–N–C single-atom catalyst during CO2 electroreduction" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Fig. 1. Dynamic adaptation of the Fe active site driven by dual-side adsorption during CO<sub>2</sub> electroreduction [1].
</div>


### References

[1] N. V. Tran<sup>†</sup>, J. Liu<sup>†</sup>, S. Li, "Dynamic Adaptation of Active Site Driven by Dual-side Adsorption in Single-Atomic Catalysts During CO<sub>2</sub> Electroreduction," *Angew. Chem. Int. Ed.* **2024**, 63, e202411765.

[2] S. Liang, L. Huang, Y. Gao, Q. Wang, B. Liu, “Electrochemical Reduction of CO2 to CO over Transition Metal/N-Doped Carbon Catalysts: The Active Sites and Reaction Mechanism,” Adv. Sci. 2021, 8, 2102886.