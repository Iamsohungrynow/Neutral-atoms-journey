# How this course connects to its sources

## The primary text for Part I

H. J. Metcalf and P. van der Straten, **Laser cooling and trapping of atoms**,
J. Opt. Soc. Am. B 20, 887 (2003), [doi:10.1364/JOSAB.20.000887](https://doi.org/10.1364/JOSAB.20.000887).
A preprint is hosted by Utrecht University:
[handpubl.pdf](https://webspace.science.uu.nl/~strat102/preprint/handpubl.pdf).

The review opens with a simplified introduction to the optical forces that cool
and trap atoms, then discusses three themes: the effects of the **multilevel
structure** of real atoms, the **quantization of atomic motion**, and the
effects of **polychromatic light**. The map below is organised by these themes
rather than by section numbers. Use the PDF's own table of contents when
reading alongside the course.

| Theme of the review | Course chapters | Numerical work |
|---|---|---|
| optical forces: radiative (scattering) force and dipole force | 03, 04 | lab 01 (optical Bloch equations); chapter 04 figures |
| slowing atomic beams (Zeeman slower, chirped cooling) | 05 | lab 02 |
| optical molasses and the Doppler limit | 05 | lab 03 |
| multilevel atoms: optical pumping, polarization-gradient (Sisyphus) cooling, the sub-Doppler surprise | 02, 06 | chapter 06 figures |
| magneto-optical trapping | 06 | lab 04 |
| dipole traps and quantized motion in optical potentials | 07 | labs 05, 06 |
| polychromatic light (for example bichromatic forces) | not covered | an advanced topic outside the needs of tweezer experiments |

Metcalf and van der Straten's book, *Laser Cooling and Trapping* (Springer,
1999), develops the same material at book length and is the best next step
for Part I.

## Sources used to structure Parts II and III

No single text covers tweezer arrays and Rydberg gates for beginners, so the
order of Parts II and III follows the standard progression of graduate atomic
physics courses and of the main reviews:

| Source | Used for |
|---|---|
| MIT 8.421 / 8.422, *Atomic and Optical Physics I and II* ([MIT OpenCourseWare](https://ocw.mit.edu/courses/8-422-atomic-and-optical-physics-ii-spring-2013/)) | the order two-level systems → light forces → cooling and trapping (Chapters 03 to 07) |
| R. Grimm, M. Weidemüller, Yu. B. Ovchinnikov, *Optical dipole traps for neutral atoms* (2000), [arXiv:physics/9902072](https://arxiv.org/abs/physics/9902072) | polarizability, trap depth, scattering (Chapter 07) |
| A. M. Kaufman and K.-K. Ni, *Quantum science with optical tweezer arrays* (2021), [arXiv:2109.10087](https://arxiv.org/abs/2109.10087) | tweezer arrays, loading, imaging, cooling (Chapters 07 to 08) |
| A. Browaeys, lectures *Rydberg atoms in optical tweezers*, Boulder School 2021 (lecture notes on the [Boulder School website](https://boulderschool.yale.edu/)) | arrays → Rydberg basics → interactions → many-body physics (Chapters 08 to 10) |
| M. Saffman, T. G. Walker, K. Mølmer, *Quantum information with Rydberg atoms* (2010), [arXiv:0909.4777](https://arxiv.org/abs/0909.4777) | Rydberg scaling, blockade, gate protocols and errors (Chapters 10 to 11) |
| L. Henriet et al., *Quantum computing with neutral atoms* (2020), [arXiv:2006.12326](https://arxiv.org/abs/2006.12326) | qubit encodings, gates, digital and analog modes (Chapters 09 to 12) |
| A. Browaeys and T. Lahaye, *Many-body physics with individually controlled Rydberg atoms* (2020), [arXiv:2002.07413](https://arxiv.org/abs/2002.07413) | quantum simulation (Chapters 10, 12) |

This is an original, Rb-87-focused course built on these sources, not a
reproduction of any of them.

## What deserves a separate, advanced course?

- **Full multilevel laser-cooling theory**: semiclassical and quantum Monte
  Carlo treatments of polarization-gradient cooling in real hyperfine structure;
  lab 03 treats only the two-level Doppler model.
- **Tensor and vector light shifts, magic wavelengths and trap-induced
  dephasing beyond the scalar two-line model** of Chapter 07.
- **Realistic Rydberg physics**: full pair-potential calculations (Förster
  resonances, angular dependence, molecular resonances), blackbody
  redistribution, and electric-field control. ARC can do much of this.
- **Optimal-control and robust Rydberg pulses**, laser phase-noise modelling and
  intermediate-state dynamics; lab 11 uses the constant-pulse Levine gate with
  simplified error models.
- **Mid-circuit measurement, dual-species arrays and cavity-assisted readout.**
- **Surface-code and qLDPC decoding with erasures and atom loss**; lab 12 uses a
  repetition code to illustrate the principle only.
- **Molecules in tweezers, optical clocks, and quantum networking with atoms in
  cavities**, all of which use the same toolbox.

These boundaries matter: a teaching simulation can establish a mechanism
without being an experiment-design package.

[Learning path and exercises](learning-path.md) · [Notation](00-notation.md)
