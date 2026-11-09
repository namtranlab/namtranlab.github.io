---
layout: page
title: Machine-Learning Potentials for High-Entropy Alloys
description: Combining DFT, AIMD, and active-learning ML potentials to understand short-range order, mechanical strength, and oxidation in refractory high- and medium-entropy alloys.
img: assets/img/publication_preview/ml_hea.png
importance: 1
category: Research
---

Refractory high- and medium-entropy alloys, made of several principal elements, are promising for structural and corrosion-resistant parts that must work at temperatures beyond the limits of today's Ni-based superalloys. Their properties depend on how the atoms are arranged locally. **Chemical short-range order (CSRO)**, the preference of certain elements to sit next to each other, can strongly change strength, deformation, and oxidation behavior. Capturing CSRO requires large simulation cells and long sampling, which is far beyond what DFT alone can handle.

We address this with **machine-learning interatomic potentials (MLIPs)** trained through an active-learning loop. An ensemble of Deep Potential models explores new configurations with MD, MC/MD, and strain. Uncertain structures are selected and labeled with DFT, and the models are retrained until they converge to near-DFT accuracy. Using these potentials together with DFT and AIMD, we study:

- **Short-range order and mechanics:** how CSRO affects hardness, dislocation behavior, and deformation in FeCrV-based [1] and CrTaTiMo [2] refractory alloys, compared with experiments.
- **Oxidation:** how oxygen is taken up and diffuses in CrTaTiMo alloys, which reveals their oxidation mechanism [3].

<div class="row justify-content-sm-center">
    <div class="col-sm-12 mt-3 mt-md-0">
        {% include figure.html path="assets/img/publication_preview/ml_hea.png" title="ML potentials for high-entropy materials" alt="Workflow: multi-principal-element alloy configurations feed an active-learning loop (train, explore, select, label) that produces a converged ML potential used to study oxidation and hardness/deformation" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Fig. 1. Workflow: alloy configurations with chemical short-range order feed an active-learning loop that produces a converged ML potential, which is then used to simulate oxidation and mechanical behavior.
</div>

### References

[1] A. Hobhaydar, X. Wang, H. Li, Z. Qiu, N. V. Tran\*, H. Zhu\*, "Influence of short-range ordering on mechanical properties of FeCrV-based refractory medium entropy alloys via deep neural network potentials," *J. Mater. Sci. Technol.* **2026**, 248, 155–164. [doi:10.1016/j.jmst.2025.05.049](https://doi.org/10.1016/j.jmst.2025.05.049)

[2] X. Wang, A. Hobhaydar, H. Li, L. Su, S. Moricca, N. V. Tran\*, H. Zhu\*, "Deciphering Short-Range Order-Driven Mechanical Enhancement in CrTaTiMo Refractory Alloys via Machine-Learning Potentials and Experimental Validation," submitted, 2025.

[3] X. Wang, A. Hobhaydar, Y. Wang, D. Wexler, H. Li, N. V. Tran\*, H. Zhu\*, "Unveiling the oxidation mechanism of CrTaTiMo refractory medium-entropy alloys: A synergy of density functional theory and ab initio molecular dynamics," *Mater. Des.* **2024**, 240, 112832. [doi:10.1016/j.matdes.2024.112832](https://doi.org/10.1016/j.matdes.2024.112832)
