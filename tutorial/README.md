# 📑 Tutorial Index: Neutral Atoms and Tweezer Arrays from Scratch

Welcome! This is a self-contained, beginner-friendly course on neutral-atom quantum hardware, written for anyone with undergraduate physics and a little linear algebra. It starts from a single atom and a laser beam, builds up laser cooling and trapping following Metcalf and van der Straten's review *Laser cooling and trapping of atoms*, zooms in on a single atom in an optical tweezer, assembles defect-free arrays, and ends with Rydberg entangling gates and the architectures being built for quantum error correction. Every chapter teaches standard, publicly known physics in plain language, works at least one example with numbers, and ends with common pitfalls, key takeaways and pointers to the literature. One reference atom, rubidium-87, is used throughout so that numbers can be compared across chapters.

Start with the [guided learning path and exercises](learning-path.md), the [notation and reference numbers](00-notation.md), and the [paper map](paper-map.md), which shows how the course follows the primary text and the courses and reviews used to structure it.

## Part I: atoms and light

| # | Chapter | Key ideas | Lab |
|---|---------|-----------|-----|
| 01 | [**Introduction: Why Neutral Atoms**](01-introduction.md) | the experimental cycle, energy scales, DiVincenzo criteria, platform comparison, history | figures |
| 02 | [**The Atom: Levels, Fine and Hyperfine Structure**](02-atomic-structure.md) | quantum defects, D1/D2, hyperfine structure, cycling transition and repumper, Breit-Rabi, clock states | figures |
| 03 | [**A Two-Level Atom in a Laser Field**](03-atom-light.md) | rotating-wave approximation, Rabi oscillations, optical Bloch equations, saturation, scattering rate, Doppler broadening, three-level atoms and adiabatic passage | [01](../hands-on/01-optical-bloch/) |
| 04 | [**Optical Forces: Radiation Pressure and the Dipole Force**](04-optical-forces.md) | photon recoil, scattering force, light shift and dipole force, why traps are far detuned | figures |
| 05 | [**Slowing and Doppler Cooling**](05-doppler-cooling.md) | Zeeman slower, optical molasses, friction coefficient, Doppler limit | [02](../hands-on/02-zeeman-slower/), [03](../hands-on/03-doppler-molasses/) |
| 06 | [**Sub-Doppler Cooling and the Magneto-Optical Trap**](06-sub-doppler-mot.md) | polarization gradients, Sisyphus cooling, gray molasses, magneto-optical trap | [04](../hands-on/04-mot/) |

## Part II: single atoms in tweezers

| # | Chapter | Key ideas | Lab |
|---|---------|-----------|-----|
| 07 | [**Optical Dipole Traps and Tweezers**](07-optical-tweezers.md) | polarizability, Gaussian focus, depth and trap frequencies, scattering, differential light shift, quantized motion, sideband cooling | [05](../hands-on/05-tweezer-trap/), [06](../hands-on/06-release-recapture/) |
| 08 | [**Loading, Imaging and Assembling Atom Arrays**](08-arrays.md) | AODs and SLMs, collisional blockade, fluorescence imaging, rearrangement | [07](../hands-on/07-rearrangement/), [08](../hands-on/08-imaging-fidelity/) |
| 09 | [**Atomic Qubits, Single-Qubit Gates and Coherence**](09-qubits-coherence.md) | qubit encodings, microwave and Raman gates, thermal $T_2^*$, spin echo | [09](../hands-on/09-ramsey-dephasing/) |

## Part III: computing with Rydberg atoms

| # | Chapter | Key ideas | Lab |
|---|---------|-----------|-----|
| 10 | [**Rydberg Atoms and the Blockade**](10-rydberg.md) | scaling laws, van der Waals interaction, blockade radius, collective excitation, analog simulation and adiabatic state preparation | [10](../hands-on/10-rydberg-blockade/), [13](../hands-on/13-adiabatic-z2/) |
| 11 | [**Rydberg Entangling Gates and Their Errors**](11-rydberg-gates.md) | $\pi$-$2\pi$-$\pi$ gate, global phase gate, decay, Doppler and blockade errors | [11](../hands-on/11-cz-gate/) |
| 12 | [**Toward Fault Tolerance: Readout, Loss, Erasure and Zoned Architectures**](12-architectures.md) | mid-circuit readout, atom loss and erasure conversion, zoned architectures, scaling | [12](../hands-on/12-erasure-code/) |

## How to use this tutorial

Read the chapters in order; each builds on the previous ones. Before running a lab, predict its result on paper, then use the [learning path](learning-path.md) checkpoints to test yourself. The "Go deeper" references at the end of each chapter, and the [reading list](../reading-list/README.md), are the fastest way to reach research-level depth.

## About the figures

Every figure is original. Each chapter has its own script in [`figures/`](figures/) (`ch01.py` to `ch12.py`), and [`make_figures.py`](figures/make_figures.py) runs them all. Numbers that appear in figures, such as level splittings, trap depths or interaction energies, are computed from the shared reference data in [`atomdata.py`](figures/atomdata.py), not drawn by hand. Several chapters also embed the figures produced by their labs. Each image carries descriptive alt text.

---

← [Project README](../README.md) · 📚 [Annotated reading list](../reading-list/README.md)
