# Neutral Atoms and Tweezer Arrays: An Annotated Reading List

Papers, books and lectures on laser cooling, optical tweezers, Rydberg atoms
and neutral-atom quantum computing that I would give to someone with a physics
or engineering background who wants to understand how these machines are built
and operated.

The annotations are original. Every reference is a public source (arXiv, a
journal, a textbook, or a university thesis repository). Identities, authors,
venues and arXiv numbers were checked against search results for arXiv,
publisher and repository records in November 2026; where an arXiv title differs
from the published one, both are given.

**How to use this list.** Each section matches part of the
[tutorial](../tutorial/README.md). Read the ⭐ entries first; the rest are for
when a chapter leaves you wanting the original argument or the experimental
details.

| Section | Tutorial chapters |
|---|---|
| [Start here](#start-here) | all |
| [Laser cooling and trapping](#laser-cooling-and-trapping) | 02 to 06 |
| [Optical tweezers and single atoms](#optical-tweezers-and-single-atoms) | 07 to 08 |
| [Qubits, gates and coherence](#qubits-gates-and-coherence) | 09 |
| [Rydberg atoms and the blockade](#rydberg-atoms-and-the-blockade) | 10 |
| [Rydberg entangling gates](#rydberg-entangling-gates) | 11 |
| [Error correction, architectures and scaling](#error-correction-architectures-and-scaling) | 12 |
| [Quantum simulation](#quantum-simulation) | 10, 12 |
| [Courses and lecture series](#courses-and-lecture-series) | all |
| [Theses and recent papers from my bibliography](#theses-and-recent-papers-from-my-bibliography) | all |

---

## Start here

- ⭐ **Laser cooling and trapping of atoms.** Metcalf, van der Straten (2003).
  *J. Opt. Soc. Am. B* 20, 887. [doi:10.1364/JOSAB.20.000887](https://doi.org/10.1364/JOSAB.20.000887) ·
  [Utrecht preprint](https://webspace.science.uu.nl/~strat102/preprint/handpubl.pdf)
  The primary text for Part I of the course. A compact, experimentally minded
  review that starts from optical forces and works through slowing, molasses,
  sub-Doppler cooling and trapping. The [paper map](../tutorial/paper-map.md)
  shows which chapter covers which theme.

- ⭐ **Quantum computing with neutral atoms.** Henriet, Beguin, Signoles,
  Lahaye, Browaeys, Reymond, Jurczak (2020). *Quantum* 4, 327.
  [arXiv:2006.12326](https://arxiv.org/abs/2006.12326)
  A readable tour of the whole platform: trapping, qubit encodings, gates,
  readout, and both digital and analog applications.

- ⭐ **Quantum science with optical tweezer arrays of ultracold atoms and
  molecules.** Kaufman, Ni (2021). *Nat. Phys.* 17, 1324.
  [arXiv:2109.10087](https://arxiv.org/abs/2109.10087)
  A short review focused on tweezers themselves: loading, cooling, imaging,
  and the range of species and applications.

- **Quantum information with Rydberg atoms.** Saffman, Walker, Mølmer (2010).
  *Rev. Mod. Phys.* 82, 2313. [arXiv:0909.4777](https://arxiv.org/abs/0909.4777)
  The standard reference on Rydberg physics for quantum information: scaling
  laws, interactions, blockade, gate protocols and error analysis.

- **Many-body physics with individually controlled Rydberg atoms.** Browaeys,
  Lahaye (2020). *Nat. Phys.* 16, 132. [arXiv:2002.07413](https://arxiv.org/abs/2002.07413)
  The quantum-simulation side of Rydberg arrays, very clearly written.

- **Atomic Physics.** Foot (2005). Oxford University Press.
  The textbook for Chapters 02 to 06: atomic structure, the optical Bloch
  equations, laser cooling and trapping.

- **Lecture courses and lecture series.** See [Courses and lecture series](#courses-and-lecture-series)
  below: MIT's graduate atomic-physics courses for Part I, and lecture series
  by Browaeys and by Bernien for Parts II and III.

---

## Laser cooling and trapping

- **Laser Cooling and Trapping.** Metcalf, van der Straten (1999). Springer.
  The book-length version of the primary text.
- **Rubidium 87 D Line Data.** Steck. [steck.us/alkalidata](https://steck.us/alkalidata)
  Every Rb-87 number used in the course, with references: transition
  frequencies, lifetimes, dipole matrix elements, hyperfine constants,
  saturation intensities, Breit-Rabi formula.
- **Laser deceleration of an atomic beam.** Phillips, Metcalf (1982).
  *Phys. Rev. Lett.* 48, 596. The first Zeeman slower.
- **Three-dimensional viscous confinement and cooling of atoms by resonance
  radiation pressure.** Chu, Hollberg, Bjorkholm, Cable, Ashkin (1985).
  *Phys. Rev. Lett.* 55, 48. The first optical molasses.
- **Trapping of neutral sodium atoms with radiation pressure.** Raab, Prentiss,
  Cable, Chu, Pritchard (1987). *Phys. Rev. Lett.* 59, 2631. The first MOT.
- **Observation of atoms laser cooled below the Doppler limit.** Lett, Watts,
  Westbrook, Phillips, Gould, Metcalf (1988). *Phys. Rev. Lett.* 61, 169.
  [doi:10.1103/PhysRevLett.61.169](https://doi.org/10.1103/PhysRevLett.61.169)
  Sodium at $43\pm20\ \mu$K, far below the Doppler limit of about $240\ \mu$K.
  The two-level theory had no explanation for a temperature that low.
- **Laser cooling below the Doppler limit by polarization gradients: simple
  theoretical models.** Dalibard, Cohen-Tannoudji (1989). *J. Opt. Soc. Am. B* 6, 2023.
  The explanation of Sisyphus and $\sigma^+\sigma^-$ cooling.
- **Laser cooling of atoms.** Wineland, Itano (1979). *Phys. Rev. A* 20, 1521.
  A thorough early theory of Doppler cooling.

---

## Optical tweezers and single atoms

- ⭐ **Optical dipole traps for neutral atoms.** Grimm, Weidemüller,
  Ovchinnikov (2000). *Adv. At. Mol. Opt. Phys.* 42, 95.
  [arXiv:physics/9902072](https://arxiv.org/abs/physics/9902072)
  The polarizability and scattering formulas of Chapter 07 and a survey of trap
  geometries.
- **Sub-poissonian loading of single atoms in a microscopic dipole trap.**
  Schlosser, Reymond, Protsenko, Grangier (2001). *Nature* 411, 1024.
  The collisional blockade.
- **Single-atom trapping in holographic 2D arrays of microtraps with arbitrary
  geometries.** Nogrette et al. (2014). *Phys. Rev. X* 4, 021034.
  [arXiv:1402.5329](https://arxiv.org/abs/1402.5329)
  SLM-generated arrays of up to about 100 traps with closed-loop depth
  equalisation.
- **Large-scale uniform optical focus array generation with a phase spatial
  light modulator.** Kim, Keesling, Omran, Levine, Bernien, Greiner, Lukin,
  Englund (2019). *Opt. Lett.* 44, 3178. [arXiv:1903.09286](https://arxiv.org/abs/1903.09286)
  Hologram algorithms for arrays of $\sim10^3$ foci with better than 98% uniformity.
- ⭐ **Atom-by-atom assembly of defect-free one-dimensional cold atom arrays.**
  Endres et al. (2016). *Science* 354, 1024. [arXiv:1607.03044](https://arxiv.org/abs/1607.03044)
  (arXiv title: *Cold matter assembled atom-by-atom*). Rearrangement with a
  multi-tone AOD.
- ⭐ **An atom-by-atom assembler of defect-free arbitrary two-dimensional atomic
  arrays.** Barredo, de Léséleuc, Lienhard, Lahaye, Browaeys (2016). *Science*
  354, 1021. [arXiv:1607.03042](https://arxiv.org/abs/1607.03042)
  Rearrangement in 2D, up to 50 atoms in arbitrary geometries.
- **Gray-molasses optical-tweezer loading: controlling collisions for scaling
  atom-array assembly.** Brown et al. (2019). *Phys. Rev. X* 9, 011057.
  [arXiv:1811.01448](https://arxiv.org/abs/1811.01448)
  89% single-atom loading in one tweezer and 80% across a 10 × 10 array.
- **Cooling a single atom in an optical tweezer to its quantum ground state.**
  Kaufman, Lester, Regal (2012). *Phys. Rev. X* 2, 041014.
  [arXiv:1209.2087](https://arxiv.org/abs/1209.2087)
  Raman sideband cooling to the 3D ground state with about 90% probability.
- **Coherence and Raman sideband cooling of a single atom in an optical
  tweezer.** Thompson, Tiecke, Zibrov, Vuletić, Lukin (2013). *Phys. Rev. Lett.*
  110, 133001. [arXiv:1209.3028](https://arxiv.org/abs/1209.3028)
  Polarization effects in a tight tweezer and their compensation; sideband
  cooling with a 900 nm waist.

---

## Qubits, gates and coherence

- ⭐ **Analysis of dephasing mechanisms in a standing-wave dipole trap.** Kuhr,
  Alt, Schrader, Dotsenko, Miroshnychenko, Rauschenbeutel, Meschede (2005).
  *Phys. Rev. A* 72, 023406. [arXiv:quant-ph/0410037](https://arxiv.org/abs/quant-ph/0410037)
  The origin of the thermal $T_2^*$ formula used in Chapter 09 and lab 09.
- **Quantum computing with atomic qubits and Rydberg interactions: progress and
  challenges.** Saffman (2016). *J. Phys. B* 49, 202001.
  [arXiv:1605.05207](https://arxiv.org/abs/1605.05207)
- **Dispersive optical systems for scalable Raman driving of hyperfine qubits.**
  Levine et al. (2022). *Phys. Rev. A* 105, 032618.
  [arXiv:2110.14645](https://arxiv.org/abs/2110.14645)
  A Raman laser built from a phase-modulated laser and a chirped Bragg grating;
  2 MHz Rabi frequencies on about 300 qubits with scattering error below
  $2\times10^{-4}$ per $\pi$ pulse.

---

## Rydberg atoms and the blockade

- **Rydberg Atoms.** Gallagher (1994). Cambridge University Press. The classic monograph.
- **ARC: An open-source library for calculating properties of alkali Rydberg
  atoms.** Šibalić, Pritchard, Adams, Weatherill (2017). *Comput. Phys. Commun.*
  220, 319. [arXiv:1612.05529](https://arxiv.org/abs/1612.05529)
  The library behind the Rydberg numbers of Chapter 10.
- **Dipole blockade and quantum information processing in mesoscopic atomic
  ensembles.** Lukin et al. (2001). *Phys. Rev. Lett.* 87, 037901.
- **Observation of Rydberg blockade between two atoms.** Urban et al. (2009).
  *Nat. Phys.* 5, 110. [arXiv:0805.0758](https://arxiv.org/abs/0805.0758)
- **Observation of collective excitation of two individual atoms in the Rydberg
  blockade regime.** Gaëtan et al. (2009). *Nat. Phys.* 5, 115.
  [arXiv:0810.2960](https://arxiv.org/abs/0810.2960)
- **Rydberg atom quantum technologies.** Adams, Pritchard, Shaffer (2020).
  *J. Phys. B* 53, 012002. [arXiv:1907.09231](https://arxiv.org/abs/1907.09231)

---

## Rydberg entangling gates

- ⭐ **Fast quantum gates for neutral atoms.** Jaksch, Cirac, Zoller, Rolston,
  Côté, Lukin (2000). *Phys. Rev. Lett.* 85, 2208.
  [arXiv:quant-ph/0004038](https://arxiv.org/abs/quant-ph/0004038)
  The $\pi$-$2\pi$-$\pi$ protocol.
- **High-fidelity control and entanglement of Rydberg-atom qubits.** Levine et
  al. (2018). *Phys. Rev. Lett.* 121, 123603. [arXiv:1806.04682](https://arxiv.org/abs/1806.04682)
  Laser phase noise and how to suppress it.
- ⭐ **Parallel implementation of high-fidelity multiqubit gates with neutral
  atoms.** Levine et al. (2019). *Phys. Rev. Lett.* 123, 170503.
  [arXiv:1908.06101](https://arxiv.org/abs/1908.06101)
  The global two-pulse CZ gate of Chapter 11 and lab 11; fidelity at least 97.4%,
  plus a three-qubit Toffoli gate.
- **Analysis of imperfections in the coherent optical excitation of single
  atoms to Rydberg states.** de Léséleuc, Barredo, Lienhard, Browaeys, Lahaye
  (2018). *Phys. Rev. A* 97, 053803. [arXiv:1802.10424](https://arxiv.org/abs/1802.10424)
  The error sources of ground-Rydberg Rabi oscillations, one by one.
- **Time-optimal two- and three-qubit gates for Rydberg atoms.** Jandura,
  Pupillo (2022). *Quantum* 6, 712. [arXiv:2202.00903](https://arxiv.org/abs/2202.00903)
  Smooth, globally applied single pulses about 10% faster than the two-pulse gate.
- ⭐ **High-fidelity parallel entangling gates on a neutral-atom quantum
  computer.** Evered et al. (2023). *Nature* 622, 268.
  [arXiv:2304.05420](https://arxiv.org/abs/2304.05420)
  CZ fidelity 99.52(4)% on up to 60 atoms in parallel.
- **Benchmarking and fidelity response theory of high-fidelity Rydberg entangling
  gates.** Tsai, Sun, Shaw, Finkelstein, Endres (2025). *PRX Quantum* 6, 010331.
  [arXiv:2407.20184](https://arxiv.org/abs/2407.20184)
  (original arXiv v1 title: *Benchmarking and linear response modeling of high-fidelity
  Rydberg gates*). A time-optimal CZ at 0.9971(5) and a method to predict
  infidelity from measured laser-noise spectra.

---

## Error correction, architectures and scaling

- ⭐ **Erasure conversion for fault-tolerant quantum computing in alkaline earth
  Rydberg atom arrays.** Wu, Kolkowitz, Puri, Thompson (2022). *Nat. Commun.* 13,
  4657. [arXiv:2201.03540](https://arxiv.org/abs/2201.03540)
  With $^{171}$Yb, most gate errors become detectable erasures; the surface-code
  threshold rises from 0.94% to 4.15% in their model. The idea behind lab 12.
- ⭐ **A quantum processor based on coherent transport of entangled atom
  arrays.** Bluvstein et al. (2022). *Nature* 604, 451.
  [arXiv:2112.03923](https://arxiv.org/abs/2112.03923)
- ⭐ **Logical quantum processor based on reconfigurable atom arrays.** Bluvstein
  et al. (2024; online December 2023). *Nature* 626, 58.
  [arXiv:2312.03982](https://arxiv.org/abs/2312.03982)
  Up to 280 physical qubits; surface codes up to distance 7; up to 48 logical
  qubits in sampling circuits.
- **A fault-tolerant neutral-atom architecture for universal quantum
  computation.** Bluvstein, Geim et al. (2026; online November 2025). *Nature*
  649, 39. [doi:10.1038/s41586-025-09848-5](https://doi.org/10.1038/s41586-025-09848-5) ·
  [arXiv:2506.20661](https://arxiv.org/abs/2506.20661) (arXiv title: *Architectural
  mechanisms of a universal fault-tolerant quantum computer*).
  Up to 448 atoms: surface-code operation 2.14(13)x below threshold, lattice
  surgery, transversal teleportation with 3D codes, and mid-circuit qubit re-use.
- **Continuous operation of a coherent 3,000-qubit system.** Chiu et al. (2025).
  *Nature* 646, 1075. [arXiv:2506.20660](https://arxiv.org/abs/2506.20660)
  Reloading 300 000 atoms per second to keep more than 3000 qubits running for
  over two hours.
- **A tweezer array with 6100 highly coherent atomic qubits.** Manetsch et al.
  (2025). *Nature* 647, 60. [arXiv:2403.12021](https://arxiv.org/abs/2403.12021)
  Caesium in about 12 000 tweezers, 12.6 s hyperfine coherence, and coherent
  transport over hundreds of micrometres.
- **Leveraging qubit loss detection in fault tolerant quantum algorithms.**
  Baranes, Cain, Bonilla Ataides, Bluvstein, Sinclair, Vuletić, Zhou, Lukin
  (2026). *Phys. Rev. X* 16, 011002. [arXiv:2502.20558](https://arxiv.org/abs/2502.20558)
  (earlier arXiv title: *Leveraging atom loss errors in fault tolerant quantum
  algorithms*).
- **Neutral atom quantum computing hardware: performance and end-user
  perspective.** Wintersperger et al. (2023). *EPJ Quantum Technol.* 10, 32.
  [arXiv:2304.14360](https://arxiv.org/abs/2304.14360)

---

## Quantum simulation

- **Probing many-body dynamics on a 51-atom quantum simulator.** Bernien et al.
  (2017). *Nature* 551, 579. [arXiv:1707.04344](https://arxiv.org/abs/1707.04344)
- **Quantum phases of matter on a 256-atom programmable quantum simulator.**
  Ebadi et al. (2021). *Nature* 595, 227. [arXiv:2012.12281](https://arxiv.org/abs/2012.12281)
- **Quantum simulation of 2D antiferromagnets with hundreds of Rydberg atoms.**
  Scholl et al. (2021). *Nature* 595, 233. [arXiv:2012.12268](https://arxiv.org/abs/2012.12268)
  (arXiv title: *Programmable quantum simulation of 2D antiferromagnets with
  hundreds of Rydberg atoms*).
- **Engineering quantum criticality and dynamics on an analog-digital
  simulator.** Geim et al. (2026). [arXiv:2602.18555](https://arxiv.org/abs/2602.18555)
  Mapping between Rydberg and hyperfine qubits; ring exchange and a
  271-site kagome lattice.
- **Three-body interactions in Rydberg lattices.** Samajdar, Lukin, Walther
  (2026). [arXiv:2604.11870](https://arxiv.org/abs/2604.11870) (theory)

---

## Courses and lecture series

Courses and school lectures by researchers in the field, found by searching
university and school pages in November 2026. Only publicly available materials
are listed; the topic orders shown are those of the published syllabi.

| Course or series | Instructor(s) | What it covers, in order | Materials | Best for |
|---|---|---|---|---|
| ⭐ MIT **8.421** *Atomic and Optical Physics I* (OCW, Spring 2014) | W. Ketterle (lectures), I. Chuang | resonance → atomic structure (H, He, fine structure, Lamb shift, hyperfine) → atoms in external fields → atom-light interaction and spontaneous emission → line broadening → two-photon excitation and coherence in two- and three-level systems | [videos, problem sets, exams](https://ocw.mit.edu/courses/8-421-atomic-and-optical-physics-i-spring-2014/) | Ch 02, 03 |
| ⭐ MIT **8.422** *Atomic and Optical Physics II* (OCW, Spring 2013) | W. Ketterle | non-classical light, multiphoton and Raman processes, coherence; lecture 16 light forces (radiation pressure, reactive forces, applications of the spontaneous force); lecture 17 dressed atom and dipole traps; lecture 18 magnetic trapping and evaporation | [videos and notes](https://ocw.mit.edu/courses/8-422-atomic-and-optical-physics-ii-spring-2013/) | Ch 04 to 07 |
| ⭐ A. Browaeys, Les Houches pre-doctoral school *Interaction of light and cold atoms* (30 Sep – 11 Oct 2019) | A. Browaeys | dipole-dipole interaction between atoms → Rydberg physics, arrays of cold atoms, blockade and quantum information → many-body physics with Rydberg atoms | [lecture 1 slides](https://coldatoms2019.sciencesconf.org/data/pages/2019_LesHouches_Predoc_Lecture1_short.pdf) | Ch 08, 10, 11 |
| ⭐ A. Browaeys, Boulder School *Ultracold Matter* (July 2021), *Rydberg atoms in optical tweezers I to III* | A. Browaeys | Rydberg atoms and their interactions, arrays of atoms, blockade and gates, many-body physics and spin models | [lecture notes](https://www.colorado.edu/conference/bss/2021/boulder-school-2021-lecture-notes); videos on the Boulder School YouTube channel | Ch 08 to 10 |
| ⭐ H. Bernien, ICTP-SAIFR School on Emergent Phenomena in Non-Equilibrium Quantum Many-Body Systems (São Paulo, June–July 2023), *Quantum Information Processing and Simulation with Rydberg Atom Arrays* (3 lectures) | H. Bernien | Rydberg arrays for quantum simulation and computation | [slides](https://www.ictp-saifr.org/wp-content/uploads/2023/06/Quantum-Information-Processing-and-Simulation-with-Rydberg-Atom-Arrays.pdf); videos on the ICTP-SAIFR YouTube channel | Ch 10 to 12 |
| A. Browaeys, ICTP summer school (2025) and Benasque (2025) | A. Browaeys | arrays and Rydberg physics → Rydberg interactions and spin models → quantum magnetism | [Benasque lecture 1](https://www.benasque.org/2025uqms/talks_contr/173_2025_Benasque_school_Lecture1_Browaeys.pdf) | Ch 10 |
| Caltech **Ph/APh 137ab** *Atoms and Photons* | M. Endres, N. Hutzler | quantized fields, light-matter interaction, open systems, with applications including Rydberg arrays; resonance, atomic structure, laser cooling, coherent control | [catalog entry](https://catalog.caltech.edu/current/2025-26/phaph-137-ab); materials not public | syllabus reference |
| Varenna "Enrico Fermi" school, Course 214, *Quantum Computers and Simulators with Atoms* (2024) | lecturers include Saffman and Kaufman | advanced lectures; Saffman's notes, *Quantum computing with atomic qubit arrays: confronting the cost of connectivity*, cover connectivity: long-range gates, atom transport, lattice surgery | [Saffman's notes, arXiv:2505.11218](https://arxiv.org/abs/2505.11218) | after Ch 12 |

M. Lukin has taught in Harvard's graduate atomic-physics sequence, but no
official course materials are public. The review by Morgado and
Whitlock, *Quantum simulation and computing with Rydberg-interacting qubits*,
AVS Quantum Sci. 3, 023501 (2021), [arXiv:2011.03031](https://arxiv.org/abs/2011.03031),
is a good companion to Bernien's lectures.

---

## Theses and recent papers from my bibliography

Theses are where the details of how an experiment works get written down.
They are linked through university repositories, not re-hosted.

### Lukin group (Harvard)

| Year | Author | Title | Type | Where |
|---|---|---|---|---|
| 2021 | Levine, H. J. | Quantum Information Processing and Quantum Simulation with Programmable Rydberg Atom Arrays | PhD thesis | [Harvard DASH](https://dash.harvard.edu/handle/1/37368420) |
| 2022 | Cong, I. | Quantum Machine Learning, Error Correction, and Topological Phases of Matter | PhD thesis | Harvard DASH |
| 2022 | Chen, Y.-T. (advisors Vuletić, Lukin) | A Platform for Cavity Quantum Electrodynamics with Rydberg Atom Arrays | PhD thesis | [Harvard DASH](https://dash.harvard.edu/handle/1/37372046) |
| 2023 (Harvard DASH: 2024) | Ebadi, S. | Quantum Simulation and Computation with Two-Dimensional Arrays of Neutral Atoms | PhD thesis | Harvard |
| 2025 | Bluvstein, D. | Error-Corrected Quantum Processing with Neutral Atoms | PhD thesis | [Harvard DASH](https://dash.harvard.edu/handle/1/42725323) |
| 2026 | Evered, S. J. | Digital Quantum Simulation and Error Correction with Atomic Processors | PhD thesis | Harvard DASH |
| 2026 | Evered et al. | High-fidelity entangling gates and nonlocal circuits with neutral atoms | preprint | [arXiv:2604.25987](https://arxiv.org/abs/2604.25987) |
| 2025 | Menon, Bonilla Ataides, Mehta, Tan, Lukin | Magic tricycles: efficient magic state generation with finite block-length quantum LDPC codes | preprint (posted August 2025, since revised) | [arXiv:2508.10714](https://arxiv.org/abs/2508.10714) |
| 2026 | Koh, …, Lukin, Majidy | Entangling logical qubits without physical operations | preprint | [arXiv:2601.20927](https://arxiv.org/abs/2601.20927) |

### Endres group (Caltech)

| Year | Author | Title | Type | Where |
|---|---|---|---|---|
| 2020 | Kale, A. M. | Towards High Fidelity Quantum Computation and Simulation with Rydberg Atoms | senior (undergraduate) thesis | [CaltechTHESIS](https://thesis.library.caltech.edu/13812) |
| 2024 | Shaw, A. L. | Learning, Verifying, and Erasing Errors on a Chaotic and Highly Entangled Programmable Quantum Simulator | PhD thesis | [CaltechTHESIS](https://thesis.library.caltech.edu/16353) |
| 2025 | Shaw, Scholl, Finkelstein, Tsai, Choi, Endres | Erasure cooling, control, and hyperentanglement of motion in optical tweezers (arXiv title: *Erasure-cooling, control, and hyper-entanglement…*) | *Science* 388, 845 (2025), [doi:10.1126/science.adn2618](https://doi.org/10.1126/science.adn2618) | [arXiv:2311.15580](https://arxiv.org/abs/2311.15580) |
| 2026 | Manetsch, H. J. | Scaling Neutral Atom Tweezer Arrays to 6,100 Qubits | PhD thesis | [CaltechTHESIS](https://thesis.caltech.edu/18735/) |
| 2026 | Bataille, Nomura, Endres | Detuning- and Stark-robust Rydberg gates | preprint | [arXiv:2608.27426](https://arxiv.org/abs/2608.27426) |

### Notes on checking the bibliography

Checking these entries turned up a few details that differed from how they
were first recorded:

- *Quantum Information Processing and Quantum Simulation with Programmable
  Rydberg Atom Arrays* is Harry Levine's 2021 thesis (advisor Lukin), not by
  "Balanis C.A.".
- *Towards High Fidelity Quantum Computation and Simulation with Rydberg Atoms*
  (Kale, 2020) is a Caltech **senior** thesis, not a PhD thesis.
- *Benchmarking and Linear Response Modeling of High-Fidelity Rydberg Gates*
  (2024) and *Benchmarking and fidelity response theory of high-fidelity
  Rydberg entangling gates* (2025) are the **same paper**: arXiv preprint and
  PRX Quantum version.
- *A tweezer array with 6100 highly coherent atomic qubits* was published in
  Nature in **2025** (arXiv 2024); the 2026 item is Manetsch's thesis.
- *Erasure-cooling, control, and hyper-entanglement of motion* now lists Shaw
  first (Scholl second) and was published in Science in 2025 as *Erasure cooling,
  control, and hyperentanglement of motion in optical tweezers*.
- *Three-body interactions in Rydberg lattices*: last author is Walther (Lukin
  is second). *Entangling logical qubits without physical operations*: last
  author is Majidy (Lukin is among the authors).
- *Magic tricycles* was first posted in August 2025 (arXiv:2508.10714) and has been revised since.
- *Leveraging atom loss errors…* was retitled *Leveraging qubit loss detection…*
  and published in PRX in 2026.
- *Advancing the Scalability Frontier of Neutral Atom Quantum Processors*
  (recorded as Guo J., 2026): no matching thesis was found in public records
  during this check, so it is not listed above. Please confirm the exact title
  and author.

---

← [Project README](../README.md) · 📑 [Tutorial index](../tutorial/README.md)
