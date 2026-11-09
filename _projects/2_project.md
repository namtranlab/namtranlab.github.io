---
layout: page
title: Role of Interfacial Water Structure in Electrocatalysis
description: Using ab initio molecular dynamics and machine-learning potentials to study how the electrode potential reshapes interfacial water and, in turn, catalysis on single-atom catalysts.
img: assets/img/publication_preview/water_interface.png
importance: 1
category: Research
---

Electrochemical reactions do not happen in a vacuum. They take place at the electrode/electrolyte interface, where the catalyst surface meets a dense, structured network of water molecules and hydrated cations. The applied potential charges the electrode and reorganizes this interfacial water: molecules reorient, hydrogen-bond networks rearrange, and cations such as K<sup>+</sup> accumulate near the surface. This microenvironment controls how reactants reach the active site, how protons are delivered, and how stable the catalyst remains [1].

Static models that leave out the solvent, or treat it only as an implicit continuum, cannot capture these effects. We use **ab initio molecular dynamics (AIMD)** to describe the interface explicitly at the electronic-structure level. We also train **machine-learning potentials (MLPs)** on AIMD data to reach the larger systems and longer time scales needed for converged structural and dynamical statistics.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.html path="assets/img/publication_preview/water_interface.png" title="Water structure at a charged SAC interface" alt="Schematic of a charged electrode with single-atom sites, an interfacial water layer, hydrated K+ cations, CO2 diffusing to an active site, and proton transfer through a hydrogen-bond chain converting *CO2 to *COOH" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Fig. 1. The electrode/electrolyte interface on a single-atom catalyst at potential U. CO<sub>2</sub> diffuses through the structured water layers to a metal site. Hydrated K<sup>+</sup> cations sit in the near-surface region, and protons are relayed through the hydrogen-bond network to convert *CO<sub>2</sub> into *COOH.
</div>

### Research focus

We focus on three questions about single-atom catalysts (SACs):

1. **Transport and adsorption.** How does the potential-dependent water structure affect the diffusion of reactants such as CO<sub>2</sub> to the active site and their adsorption on it?
2. **Reaction kinetics.** How do interfacial water and cations take part in electrochemical steps, for example as proton donors through hydrogen-bond chains, or by stabilizing charged intermediates?
3. **Catalyst stability.** How does the interfacial environment under operating conditions affect the stability of SACs, including degradation of the active site?

### References

[1] M. Schreier, P. Kenis, F. Che, A. S. Hall, "Trends in Electrocatalysis: The Microenvironment Moves to Center Stage," *ACS Energy Lett.* **2023**, 8, 3935–3940. [doi:10.1021/acsenergylett.3c01623](https://doi.org/10.1021/acsenergylett.3c01623)
