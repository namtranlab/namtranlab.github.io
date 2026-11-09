---
layout: page
title: Tribochemistry and Superlubricity of Carbon-Based Materials
description: First-principles simulations of how sliding, stress, and the surrounding environment drive chemical reactions that decide friction and wear at diamond and carbon interfaces.
img: https://ars.els-cdn.com/content/image/1-s2.0-S0008622322005905-ga1.jpg
importance: 1
category: Research
---

Friction and wear cause a large share of the energy losses and component failures in mechanical systems. Diamond and other carbon-based coatings are promising solutions because they can reach superlubricity, a state with nearly vanishing friction. This behavior is fragile, however. The same coating can slide almost without resistance in one environment and wear quickly in another. The difference comes from **tribochemistry**: chemical reactions at the sliding interface that are driven by mechanical stress, temperature, and molecules from the surroundings.

These reactions happen at buried interfaces over very short times, so they are hard to observe directly in experiments. We use **density functional theory (DFT)** to describe how molecules bind to surfaces and how surfaces bond to each other, **ab initio molecular dynamics (AIMD)** to follow reactions under load and shear in real time, and **machine-learning potentials** to extend these simulations to larger systems and longer sliding times. Our work focuses on three questions.

### How does the environment passivate diamond surfaces?

Molecules such as H<sub>2</sub>, H<sub>2</sub>O, and O<sub>2</sub> are present in most working environments. We studied how each of them interacts with diamond surfaces and how the resulting surface terminations reduce adhesion between contacting surfaces, which leads to low friction [1].

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.html path="https://ars.els-cdn.com/content/image/1-s2.0-S0008622322005905-ga1.jpg" title="Molecules interacting with diamond surfaces" alt="Interaction of H2, H2O and O2 molecules with diamond surfaces" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Fig. 1. Interaction of H<sub>2</sub>, H<sub>2</sub>O, and O<sub>2</sub> molecules with diamond surfaces [1].
</div>

### What controls wear at the atomic scale?

When passivation breaks down, covalent bonds can form across the interface, and atoms can be pulled out of the surface. Using AIMD, we examined how surface orientation, applied stress, and adsorbed molecules affect these atomistic wear processes in diamond [2]. We also studied oxidized diamond sliding against silica, a contact that is common in real devices, to show how interfacial chemistry governs both wear and friction there [3].

### Can natural molecules enable green lubrication?

Many conventional lubricant additives raise environmental concerns. In collaboration with experimental groups, we helped show that aromatic molecules of natural origin, once activated by mechanochemistry at the sliding interface, can produce superlubricity. This points to a new route toward environmentally friendly lubrication [4].

### References

[1] N. V. Tran, M. C. Righi, "Ab initio insights into the interaction mechanisms between H<sub>2</sub>, H<sub>2</sub>O, and O<sub>2</sub> molecules with diamond surfaces," *Carbon* **2022**, 199, 497–507. [doi:10.1016/j.carbon.2022.07.056](https://doi.org/10.1016/j.carbon.2022.07.056)

[2] H. T. T. Ta, N. V. Tran, M. C. Righi, "Atomistic Wear Mechanisms in Diamond: Effects of Surface Orientation, Stress, and Interaction with Adsorbed Molecules," *Langmuir* **2023**, 39, 14396–14403. [doi:10.1021/acs.langmuir.3c01800](https://doi.org/10.1021/acs.langmuir.3c01800)

[3] H. T. T. Ta, N. V. Tran, M. C. Righi, "Nanotribological Properties of Oxidized Diamond/Silica Interfaces: Insights into the Atomistic Mechanisms of Wear and Friction by Ab Initio Molecular Dynamics Simulations," *ACS Appl. Nano Mater.* **2023**, 6, 16674–16683. [doi:10.1021/acsanm.3c02881](https://doi.org/10.1021/acsanm.3c02881)

[4] Y. Long, A. Pacini, M. Ferrario, N. V. Tran, S. Peeters, B. Thiebaut, S. Loehlé, J. M. Martin, M. C. Righi, M. I. De Barros Bouchet, "Superlubricity from mechanochemically activated aromatic molecules of natural origin: A new concept for green lubrication," *Carbon* **2024**, 228, 119365. [doi:10.1016/j.carbon.2024.119365](https://doi.org/10.1016/j.carbon.2024.119365)
