# 08 · Loading, Imaging and Assembling Atom Arrays

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

Chapter 07 built one tweezer. A quantum computer needs hundreds or thousands of them, each holding exactly one atom, arranged in a pattern you choose. This chapter covers the four steps that get you there: **making** many tweezers from one laser, **loading** them (and the surprising physics that gives exactly zero or one atom per trap), **imaging** single atoms to find out which traps are full, and **rearranging** the atoms into a defect-free array. The labs simulate loading and rearrangement (lab 07) and single-atom detection (lab 08).

## Making many tweezers

Two devices dominate, and most experiments use both.

**Acousto-optic deflectors (AODs).** A radio-frequency sound wave in a crystal acts as a moving diffraction grating; the deflection angle is proportional to the RF frequency. Driving the AOD with several frequencies at once creates a row of beams, and the objective lens turns each angle into a tweezer at a different position. Two crossed AODs make a rectangular grid. AOD tweezers can be **moved** smoothly by sweeping a frequency, and switched on and off in microseconds, which makes them the tool for rearrangement and for moving atoms during a computation (Chapter 12). Their limitation is that a crossed pair can only make grids that are products of the $x$ and $y$ frequencies.

**Spatial light modulators (SLMs).** A liquid-crystal SLM imprints a programmable phase pattern (a hologram) on the beam; the objective's focal plane then contains the Fourier transform of that pattern. With a suitable hologram, one beam becomes hundreds or thousands of static tweezers in an arbitrary 2D pattern. Iterative algorithms adjust the hologram until all trap depths are equal to within a few percent. SLMs refresh slowly (milliseconds), so they are used for the static array, with AOD tweezers moving atoms between its sites.

![Left: an acousto-optic deflector crystal driven by four radio-frequency tones splits one laser beam into four deflected beams, which an objective focuses into four tweezers in a row. Right: a spatial light modulator imprints a phase hologram on a laser beam, and the objective turns it into an arbitrary two-dimensional pattern of tweezers](figures/08-aod-slm.png)

*Two ways to multiply tweezers. AODs are dynamic but limited to rows and grids; SLMs make arbitrary static patterns. Typical arrays combine a static SLM (or AOD) array with one or more moving AOD tweezers.*

## Loading: why every tweezer holds zero or one atom

Overlap the tweezer array with a cold cloud (a MOT or, better, a molasses) and atoms fall into the traps. You might expect a Poisson number of atoms per tweezer. Instead, in a sufficiently small trap you get **zero or one, with roughly equal probability**. This is the work of **light-assisted collisions**.

When two atoms share a micron-sized trap in the presence of near-resonant cooling light, the light can excite the pair to a molecular state in which the atoms strongly attract each other. They accelerate toward each other and, after the excitation decays, often carry enough kinetic energy to leave the trap together. In a tiny tweezer this happens within milliseconds, much faster than new atoms arrive. So atoms are lost **in pairs**, and the trap can never hold more than one atom for long. This is the **collisional blockade** regime (Schlosser et al., 2001).

A simple model makes the 50% precise. If $N$ atoms enter, with $N$ Poisson-distributed with mean $\bar n$, and every pair is removed, the trap ends with $N\bmod2$ atoms. The probability of one atom is the probability that $N$ is odd:

$$P_1=\sum_{N\ \rm odd}\frac{\bar n^Ne^{-\bar n}}{N!}=e^{-\bar n}\sinh\bar n=\frac{1-e^{-2\bar n}}{2}\ \xrightarrow{\ \bar n\gg1\ }\ \frac12 .$$

![Left: probability of finding one atom after pairwise loss, (1 - exp(-2 nbar))/2, rising to one half, together with the probability of zero atoms falling to one half and, for comparison, the plain Poisson probability of one atom which peaks at 0.37. Right: bar charts of a Poisson distribution with mean 3 and of the same distribution after light-assisted collisions, which leaves only zero or one atom with almost equal probability](figures/08-loading.png)

*Collisional blockade. Removing atoms in pairs turns any Poisson distribution into a coin toss between zero and one atom. Without it, the best you could do is $P_1=1/e=0.37$, and many traps would hold two or more atoms.*

The occupancy is **sub-Poissonian**: the variance of the atom number per trap, $p(1-p)=0.25$ at $p=1/2$, is half the variance $0.5$ that a Poisson distribution with the same mean of 0.5 atoms would have. That is useful, but a 50% filling is still a problem: the probability that all $N$ traps are full is $2^{-N}$, about $10^{-15}$ for $N=50$.

**Beating 50%.** If the collisions are tuned so that only **one** atom of a pair escapes, the trap ends with one atom far more often. Blue-detuned light-assisted collisions do this by giving the pair just enough energy for one atom to leave; gray-molasses loading on the D1 line achieves the same with little light scattering. Grünzweig et al. (2010) pioneered this with blue-detuned light-assisted collisions; with gray-molasses loading, Brown et al. (2019) reached 89% in a single tweezer and 80% across a 10 × 10 array. Rearrangement then fills the rest.

## Imaging single atoms

To know which traps are full, you photograph the atoms by their fluorescence: shine near-resonant light, collect scattered photons with the same high-NA objective, and image them onto a sensitive camera.

**Photon budget.** An atom emitting into all directions sends a fraction

$$\eta_{\rm coll}=\frac{1-\cos\theta}{2},\qquad\sin\theta={\rm NA},$$

of its photons into the lens (for isotropic emission). For NA $=0.5$, $\theta=30°$ and $\eta_{\rm coll}=(1-0.866)/2=6.7\%$; for NA $=0.7$ it is 14.3%. After optical losses and the camera's quantum efficiency, only a few percent of the scattered photons are detected.

**Heating during imaging.** At $6\times10^4$ scattered photons per second, a 20 ms exposure scatters about 1200 photons. Each adds about $2E_r=k_B\times0.36\ \mu$K, so an uncooled atom would gain $1200\times0.36\ \mu{\rm K}\approx0.43$ mK, close to the trap depth. Imaging therefore uses **cooling light** (molasses or a similar configuration) so that the atom is laser-cooled while it fluoresces. The tweezer's light shift also detunes the imaging transition (Chapter 07), which is why imaging light and trap depth are chosen together.

**Fidelity and survival.** Two numbers characterise imaging:

- **Detection (assignment) fidelity**: the probability of correctly calling a trap full or empty. Photon counts from an empty trap (background) and a full trap (signal plus background) are both Poisson distributed; a threshold separates them. Lab 08 shows that with 32 signal and 5 background photons the two distributions are so well separated that the error is $5\times10^{-5}$.
- **Survival**: the probability that the atom is still there afterwards. Imaging heats and occasionally loses atoms; an atom lost early in the exposure produces too few photons and may be miscounted. In lab 08, a 1% loss during imaging raises the assignment error from $5\times10^{-5}$ to $1.6\times10^{-3}$.

State-resolved readout of a qubit uses the same imaging. First, light resonant with $F=2\to F'=3$ and no repumper **pushes out** every atom in $F=2$; then all remaining atoms are imaged. A bright trap means the atom was in $F=1$, a dark trap that it was in $F=2$ (or was lost). Chapter 12 discusses how readout is done in the middle of a computation.

## Rearrangement: atom-by-atom assembly

With a 50% filled array and a single-atom image in hand, the computer finds the empty target sites and sends a moving AOD tweezer to fix them: ramp up the moving tweezer on top of a reservoir atom, drag it to the empty site, ramp down. This idea, demonstrated in one dimension by Endres et al. and in two dimensions by Barredo et al. (both 2016), made defect-free arrays of tens of atoms possible and is now standard.

**Algorithms.** In 1D, sliding atoms together ("compaction") is enough. In 2D, a common approach assigns each empty target site to a reservoir atom so as to minimise the total travel distance (the Hungarian algorithm, used in lab 07), then moves atoms one by one or several at a time with multiple AOD tones. Practical algorithms avoid collisions between moving and static atoms and minimise the total time.

**Success probability.** Each move can lose the atom (probability $\varepsilon$), and every atom can be lost to background-gas collisions during the cycle (lifetime $\tau$, cycle time $t$). If each empty target site costs one move, the probability that a target block of $N$ sites ends up defect free is

$$P_{\rm success}=\sum_h\binom{N}{h}(1-p)^hp^{N-h}\;(1-\varepsilon)^h\;e^{-Nt/\tau}$$

(assuming enough reservoir atoms; lab 07 includes the reservoir exactly). The two loss factors set the scaling: with $p=1/2$, $\varepsilon=1\%$, $\tau=60$ s and $t=0.2$ s, a 100-site block succeeds about 43% of the time, compared with $2^{-100}\approx10^{-30}$ without rearrangement. For 1000 sites the vacuum factor alone is $e^{-1000\times0.2/60}=e^{-3.3}=0.036$. Scaling to thousands of qubits therefore pushes toward better vacuum (cryogenic setups reach lifetimes of many minutes), faster cycles, repeated rearrangement rounds, and continuous reloading of fresh atoms (Chapter 12).

![Three panels from lab 07. Left: a 16 by 16 array after loading, with 125 atoms scattered randomly and a red 10 by 10 target square. Middle: the same array after 51 moves, with the target square completely filled and leftover atoms outside. Right: probability of a defect-free array versus number of target sites on a log scale: without rearrangement it falls as one half to the N; with rearrangement it falls exponentially but slowly; three curves compare move loss 1 percent with a 60 s vacuum lifetime, 0.3 percent with 60 s, and 0.3 percent with 600 s; Monte Carlo points agree with the curves](../hands-on/07-rearrangement/figures/rearrange.png)

*Lab 07. Rearrangement turns a hopeless $2^{-N}$ into a slowly decaying exponential set by move losses and vacuum lifetime.*

## Worked example: assembling a 10 × 10 array (illustrative numbers)

| Quantity | Value |
|---|---|
| traps, target | 256 (16 × 16), central 100 (10 × 10) |
| loading probability | $p=0.5$ |
| move loss, vacuum lifetime, cycle time | 1%, 60 s, 0.2 s |
| expected empty target sites | $100\times0.5=$ **50 moves** |
| move survival factor | $0.99^{50}=$ **0.61** (on average) |
| vacuum survival factor | $e^{-100\times0.2/60}=$ **0.72** |
| defect-free probability | **0.43** (exact formula, lab 07) |
| imaging: NA, collection, detection | 0.5, 6.7%, 2.7% |
| imaging: signal, background, error | 32, 5 photons, $5\times10^{-5}$ |

**Step 1: loading.** About 128 of 256 traps fill; on average 50 of the 100 target sites are empty, and 78 reservoir atoms are available, enough with high probability.

**Step 2: moves.** Each of the roughly 50 moves survives with 99%. The average of $0.99^h$ over the binomial distribution of $h$ is $(1-0.01\times0.5)^{100}=0.995^{100}=0.61$.

**Step 3: vacuum.** All 100 target atoms must survive 0.2 s: $e^{-100\times0.2/60}=e^{-0.333}=0.72$.

**Step 4: combine.** $0.606\times0.717=0.434$. Including the small probability that the reservoir runs short (lab 07) changes nothing at this size. In more than half the cycles at least one site is empty after one round. Experiments then image again and repair the remaining holes in a second round.

**Step 5: imaging.** With $\mu_s=0.0268\times6\times10^4\times0.02=32.2$ detected signal photons and $\mu_b=5$, the optimal threshold is the first count at which a full site becomes more likely than an empty one, where the two Poisson distributions cross: $\mu_s/\ln(1+\mu_s/\mu_b)=32.2/\ln7.44=16.03$, which rounds up to 17 photons (with $\mu_s$ rounded to 32 you would get 16, so carry the digits), and the assignment error is $5\times10^{-5}$.

## Run it

- [Lab 07](../hands-on/07-rearrangement/) simulates collisional-blockade loading, 2D rearrangement with the Hungarian algorithm, and the success probability versus array size, and compares everything with the exact formulas above.
- [Lab 08](../hands-on/08-imaging-fidelity/) simulates photon-count histograms, chooses the threshold, and shows how loss during imaging degrades fidelity.
- [Lab 06](../hands-on/06-release-recapture/) (from Chapter 07) shows how the same images measure the temperature of a single atom.

## Common pitfalls

- **"50% loading means half the atoms are lost."** Pairs are lost; the occupancy of each trap becomes a fair coin, independent of the cloud density once $\bar n\gtrsim2$.
- **Detection fidelity versus survival.** A perfect image of an atom that is then lost is useless for the next step. Quote both numbers.
- **"Imaging only needs a good camera."** The limit is usually photon budget and heating: NA, imaging time, cooling during imaging, and loss all matter.
- **Ignoring vacuum lifetime.** A 60 s lifetime sounds long, but a 1000-atom array loses one atom every 60 ms on average.
- **Thinking rearrangement is free.** Each move costs time and a small loss probability, and the moving tweezer can heat the atom; experiments re-cool after rearrangement.

## Key takeaways

- AODs make dynamic rows and grids and move atoms; SLMs make static arbitrary patterns. Most arrays use both.
- Light-assisted collisions remove atoms in pairs, so each tweezer ends with $N\bmod2$ atoms: $P_1=(1-e^{-2\bar n})/2\to1/2$. Tailored collisions raise this to about 80 to 90%.
- Fluorescence imaging collects $(1-\cos\theta)/2$ of the photons (6.7% at NA 0.5) and must cool the atom while imaging; assignment errors of $10^{-4}$ and below are possible, and survival is a separate figure of merit.
- Rearrangement fills empty sites atom by atom; success then decays as $(1-\varepsilon p_{\rm hole})^N e^{-Nt/\tau}$ instead of $p^N$.

## Go deeper

- N. Schlosser, G. Reymond, I. Protsenko, P. Grangier, *Sub-poissonian loading of single atoms in a microscopic dipole trap*, Nature 411, 1024 (2001). The collisional blockade.
- M. Endres et al., *Atom-by-atom assembly of defect-free one-dimensional cold atom arrays*, Science 354, 1024 (2016), [arXiv:1607.03044](https://arxiv.org/abs/1607.03044).
- D. Barredo, S. de Léséleuc, V. Lienhard, T. Lahaye, A. Browaeys, *An atom-by-atom assembler of defect-free arbitrary two-dimensional atomic arrays*, Science 354, 1021 (2016), [arXiv:1607.03042](https://arxiv.org/abs/1607.03042).
- F. Nogrette et al., *Single-atom trapping in holographic 2D arrays of microtraps with arbitrary geometries*, Phys. Rev. X 4, 021034 (2014), [arXiv:1402.5329](https://arxiv.org/abs/1402.5329).
- M. O. Brown et al., *Gray-molasses optical-tweezer loading: controlling collisions for scaling atom-array assembly*, Phys. Rev. X 9, 011057 (2019), [arXiv:1811.01448](https://arxiv.org/abs/1811.01448).
- A. M. Kaufman and K.-K. Ni, *Quantum science with optical tweezer arrays of ultracold atoms and molecules*, Nat. Phys. 17, 1324 (2021), [arXiv:2109.10087](https://arxiv.org/abs/2109.10087).

---

← Previous: [Optical Dipole Traps and Tweezers](07-optical-tweezers.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [Atomic Qubits, Single-Qubit Gates and Coherence](09-qubits-coherence.md) →
