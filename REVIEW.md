# Independent review, 2 November 2026 (fourth pass: derivations and wording)

This pass had two aims: check every equation and every step of every
derivation (not only the final numbers), and rewrite passages that read as
machine-generated. Five reviewers each re-derived their slice by hand, with
sympy or numerically, and proposed text edits; every physics correction below
was re-checked independently before it was applied. No displayed equation was
wrong. The corrections are to individual statements, numbers and missing
conditions.

## Corrections

| Where | Finding | Correction |
|---|---|---|
| Ch 11 | finite-blockade error described as leakage, "part of" which calibration removes | it is almost entirely a phase $\delta\phi=2\hbar\Omega/V$ on $\vert11\rangle$, giving $1-F=0.6(\hbar\Omega/V)^2=1.7\times10^{-4}$; re-optimising the pulse leaves $1.2\times10^{-8}$ (checked numerically); leakage is only $10^{-5}$ |
| Ch 11 | "the design has two steps" followed by three conditions; $1-F\approx\Gamma\overline{T_R}$ and $F$ not derived or defined in the chapter | three conditions for three parameters, with $\phi_{11}=\Delta\tau=1.62$ rad and $\phi_{01}=2.38$ rad shown; Pedersen formula and one-line derivation added |
| Ch 03 | pitfall said more intensity barely raises the scattering above $s_0\approx1$ | on resonance $s_0=1\to10$ raises $\gamma_p$ from 50% to 91% of $\Gamma/2$; pitfall now targets "scattering is proportional to intensity" |
| Ch 01 | cooling factor $10^6$ to $10^7$ | $3\times10^6$ to $3\times10^7$ |
| Ch 02 | worked example reused the resonant leak estimate | one leak per 2 to 3 thousand photons at MOT detunings, every 0.2 to 3 ms |
| Ch 04 | far-detuned limit of the log formula; sign of $U_0$ in the worked example | needs $\vert\delta\vert\gg\Gamma$ as well; $\vert\delta\vert$ used so $U_0>0$ |
| Ch 05 | molasses caption: "linear up to $kv\approx\vert\delta\vert$" and "peaks near $\vert\delta\vert/k$" contradict each other | within 10% of linear to 1.5 and 2.5 m/s ($\delta=-\Gamma/2,-\Gamma$); peaks at 2.8 and 4.8 m/s |
| Ch 06 | Sisyphus climb "every half wavelength" | every quarter wavelength |
| Ch 07 | Lamb-Dicke parameter called the ratio of size to wavelength | ratio to the reduced wavelength $\lambda/2\pi$ |
| Ch 08 | error at threshold 16 given as $5.4\times10^{-5}$ | $5.1\times10^{-5}$ |
| Ch 09 | Rayleigh fraction "70 to 90%" | two thirds for the clock states at any polarization (Kramers-Heisenberg sum; checked numerically) |
| Ch 10 | $\sqrt N$ condition "within one blockade radius"; lifetime scaling $n^{*3}$ | every pair within $R_b$ of each other; $n^{*3}$ is the radiative part |
| Ch 12 | dominant failure terms and the value of erasure conversion stated vaguely | leading terms $5.8\times10^{-9}$ and $1.9\times10^{-9}$; 98% conversion is worth an elevenfold cut in the raw error rate |
| Labs 09, 10 | an oscillating-phase bound off by 2; an ill-posed exercise; "equals" for a 1% agreement | bound $E_i/2\omega_i$; exercise restated; "agrees to about 1%" |
| notation page | Gaussian potential and $\sigma^x$ | focal-plane form with $w_0$; $\sigma^x_i$ defined |

## Wording

About 160 passages across the chapters, labs and front pages were rewritten:
signposting openers ("This chapter builds…", "The idea is simple", "Here is
how"), "This is why" and "Note that" sentences, colons that deliver a moral,
paragraph-ending morals, rule-of-three lists, filler adjectives, stacked bold
labels and templated metaphors (several "Intuition aside" boxes now give a
number the reader can check instead). Section structure, worked examples,
numbers and links are unchanged.

## Re-run

`python hands-on/run_labs.py --all --check` passes 13/13, regenerating the
figures leaves every PNG unchanged, and `python tools/check_repo.py` reports
0 errors.

# Independent review, 1 November 2026 (third pass)

Five fresh reviewers re-read the whole course again in the same slices as the
second pass, recomputed every number with their own scripts, re-derived the key
formulas, simulated the protocols the text describes, viewed every figure and
ran every lab. Each finding below was re-checked (several by independent
simulation) before it was applied. No formula in the course was found to be
wrong; the corrections fix statements that would mislead a beginner, missing
assumptions, and bookkeeping.

## Corrections

| Where | Finding | Correction |
|---|---|---|
| Ch 03 | Landau-Zener example quoted $4\times10^{-3}$ for a $\pm7$ MHz sweep at constant $\Omega$ | the formula needs the sweep to start and end at $\vert\delta\vert\gg\Omega$; that finite sweep actually leaves 1.4% (0.2% with a ramped $\Omega$), now stated |
| Ch 03 | "the hyperfine lines blur together" in a 300 K vapour | only the excited-state components blur; the 6.8 GHz ground-state splitting stays resolved |
| Ch 03 | ladder-system detunings and light-shift signs ambiguous; STIRAP pulses not said to overlap | detuning conventions for $\Lambda$ and ladder stated; both levels pushed away from $\vert e\rangle$; overlapping pulses in counter-intuitive order |
| Ch 01, 02 | coherence "for seconds"; why the hyperfine qubit is protected; leak-rate estimate; a typo | ms (seconds with echo); mechanism stated; line-strength and branching factors included |
| Ch 04 | "slides down (or up)"; excited-state light shift "the same amount" | pushed toward lower energy; equal and opposite only in the two-level model |
| Ch 05 | Zeeman-slower lock explanation used "falls behind" in two opposite senses | rewritten: of the two force-balance points only the slow, red-detuned one is stable |
| Ch 05 | molasses force "linear for $\vert v\vert\lesssim2.4$ m/s" for a figure at $\delta=-\Gamma,-2\Gamma$ | close to linear for $kv\lesssim\vert\delta\vert$; peaks near $v\approx\vert\delta\vert/k$ |
| Ch 06, lab 04 | force maximum called the "edge of the trap"; "linear only for $\vert z\vert\lesssim2$ mm" | the force stays restoring out to the beam edge; within about 10% of linear to 2 to 3 mm |
| Ch 06 | sub-Doppler floor explained inconsistently | floor where recoil heating per cycle is no longer small compared with the energy removed per climb |
| Labs 02, 03 | exit-speed arithmetic; burn-in event counts; stale docstring and dead code | numbers match the code's output; dead code removed |
| Ch 07 | sign regions of the polarizability omitted the D2-to-tune-out window; $w_0$ formula attribution | full sign map; untruncated-Gaussian vs filled-aperture spot sizes |
| Ch 08 | threshold rounding; SLM refresh time; $p_{\rm hole}$ undefined | equal priors stated; thresholds 16 and 17 nearly equivalent; tens of ms; defined |
| Ch 09 | nuclear-spin Zeeman scale; Rayleigh-scattering fraction; Raman figure range | 0.2 to 0.75 kHz/G; 70 to 90%; figure starts at 20 GHz |
| Lab 08 | fidelity check used one error bar for all thresholds | per-threshold binomial standard error |
| Ch 10, 11, lab 13 | $Z_2$ crossover is at $\Delta\approx1.4$ MHz, not 0, for $\Omega/2\pi=2$ MHz; PXP model unexplained; leakage mechanism | crossover stated; PXP Hamiltonian written out; leakage from the fast $\Omega$ ramps |
| Ch 12 | transversal CNOT error spreading | errors spread only to the partner atom in the other block |
| REVIEW, reading list | 70S lifetime 147 $\mu$s left in the checking notes; "(not independently checked)" markers | 146 $\mu$s; all 14 marked references verified against arXiv, APS, Nature and ADS records and the markers removed |
| reading list | Shaw et al. page missing; 8.421 instructors; Tsai et al. arXiv title; unconfirmed course details | *Science* 388, 845 (2025); Ketterle and Chuang; v1 title; unconfirmed lecturer, course number and PDF link removed |

## Re-run

`python hands-on/run_labs.py --all --check` passes 13/13,
`python tutorial/figures/make_figures.py` changes only the three figures edited
in this pass (06-mot-scheme, 09-raman, 09-sequences), and
`python tools/check_repo.py` reports 0 errors.

# Independent review, 1 November 2026 (second pass)

Five independent reviewers each re-read one slice of the course line by line
(Chapters 01 to 03, 04 to 06, 07 to 09, 10 to 12, and the cross-cutting pages
with every citation), recomputed the numbers with their own scripts and the ARC
library, viewed every figure, and ran every lab. A sixth searched for courses
and lecture series by researchers in the field. Every finding was re-checked
before it was applied.

## Corrections

| Where | Finding | Correction |
|---|---|---|
| Ch 01 cycle figure | readout written as "bright = 1, dark = 0" | after pushing out $F=2$ ($\vert1\rangle$), bright means $\vert0\rangle$: "bright = 0, dark = 1" |
| Ch 07 | polarizability at 532 nm given as $-785$ a.u. (an early weighting error) | $-262$ a.u. from the course's two-line model |
| Ch 06 | gray-molasses mechanism described backwards | atoms leave the dark state near the bottoms of bright-state valleys and are pumped back near the hilltops |
| Ch 11 | "co-propagating beam geometries reduce" Doppler errors | backwards for a ladder scheme: co-propagating beams add the wavevectors; counter-propagating beams (as assumed) or three-photon schemes reduce it |
| Ch 12 | transversal physical CZ called a logical gate in general | a transversal CNOT (CZ plus Hadamards) is logical for CSS codes such as surface and colour codes |
| Ch 01 | cooling factor stated as $10^5$ and "five orders of magnitude" | $10^6$ to $10^7$ (300 K to 10 to 100 $\mu$K) |
| Ch 02 | clock-state noise sensitivity "a thousand times" smaller; low-$n$ quantum defects "slightly larger"; $g_F\neq1/2$ attributed only to $g_I$; quadrupole condition | about 600 times; larger for S, P and smaller for D, F; $g_J\neq2$ contributes too; quadrupole exists because $I\ge1$ |
| Ch 03 | RWA described in the wrong frame | RWA in the interaction picture, then the frame rotating at $\omega_L$; Bloch components defined |
| Ch 04 | $\vert\delta\vert=1650\,\Gamma$ in the worked example | $\approx8200\,\Gamma$; two-level $\sigma^+$ assumption stated |
| Ch 05 | ytterbium narrow-line cooling "below a microkelvin"; 3D Doppler limit wording | only strontium reaches below 1 $\mu$K; explicit 1D vs 3D emission-model statement |
| Ch 06, lab 04 | "linear region 4.3 mm" | that is the force maximum; the force is linear only for $\vert z\vert\lesssim2$ mm |
| Ch 08 | threshold arithmetic with rounded $\mu_s$; combine step attributed a reservoir effect | carry $\mu_s=32.2$ (gives 17); $0.606\times0.717=0.434$ |
| Ch 09 | ground-Rydberg splitting "hundreds of THz"; $T_1$ "seconds" | about 1009 THz (297 nm); seconds at 852 nm, minutes at 1064 nm; repumper polarization requirement added |
| Ch 10 | blockade history attribution; Förster-defect sign undefined | Urban et al. (suppressed double excitation) and Gaëtan et al. ($\sqrt2$ enhancement); $\Delta_F<0$ defined |
| all | 70S lifetime at 300 K quoted as 147 $\mu$s | 146 $\mu$s (ARC, consistent with the code) |
| Ch 12, lab 12 | erasure "doubles" the code distance | exponent $d$ instead of $(d+1)/2$ |
| reading list | 2025 Bluvstein et al. listed as preprint; Shaw et al. arXiv title | published as *A fault-tolerant neutral-atom architecture for universal quantum computation*, Nature 649, 39 (2026); Science title and DOI added |
| notation page | lab unit conventions wrong for labs 01 and 09; "every number recomputed" overclaim | corrected table; stated which inputs are tabulated |

## Stronger lab checks

Several checks were circular or trivial and were replaced: lab 01 now compares
QuTiP with an independent integration of the Chapter 03 Bloch equations; lab 02
measures the deceleration the locked atom actually experiences; lab 03 extracts
the friction coefficient from the decay of the mean velocity in the stochastic
simulation (instead of re-deriving the force formula) and uses a burn-in of
eight damping times at every detuning; lab 11 checks the time $\vert11\rangle$
spends in $\vert r\rangle$ against its analytic value and models ideal blockade
with a $V$ small enough to keep the matrix exponential unitary; lab 12 runs its
Monte Carlo at $p=0.3$, where every case produces enough failures to test.

## Additions

- **Chapter 03:** Doppler broadening; three-level atoms (adiabatic elimination,
  dark states and STIRAP, Landau-Zener adiabatic passage), which later chapters
  rely on.
- **Chapter 10 and lab 13:** analog quantum simulation, with exact adiabatic
  preparation of a nine-atom $Z_2$ crystal.
- **Reading list and paper map:** courses and lecture series (MIT 8.421/8.422 at
  lecture level, Browaeys at Les Houches 2019 and Boulder 2021, Bernien at
  ICTP-SAIFR 2023, Caltech Ph/APh 137, Saffman's Varenna notes).
- Previous/next navigation on every chapter; the link checker now also checks
  HTML `src`/`href` targets.

Validation after this pass: `python hands-on/run_labs.py --all --check` passes
13/13 (about 100 s on a 4-core machine), `python tutorial/figures/make_figures.py` regenerates every
figure, and `python tools/check_repo.py` reports 0 errors.

---

# Repository review, 1 November 2026 (first pass)

This file records how the course was built and checked, what was corrected
during the checks, and what is deliberately out of scope.

## Sources and structure

- **Part I (Chapters 02 to 06)** follows the themes of H. J. Metcalf and
  P. van der Straten, *Laser cooling and trapping of atoms*, J. Opt. Soc. Am. B
  20, 887 (2003) ([Utrecht preprint](https://webspace.science.uu.nl/~strat102/preprint/handpubl.pdf)):
  optical forces, slowing and molasses, multilevel (sub-Doppler) cooling and the
  MOT, and quantized motion in optical potentials.
- **Parts II and III** follow the order of graduate atomic-physics courses
  (MIT 8.421/8.422) and of the main reviews and lecture series on tweezer arrays
  and Rydberg atoms (Grimm et al.; Kaufman and Ni; Browaeys's Boulder School 2021
  lectures; Saffman, Walker and Mølmer; Henriet et al.; Browaeys and Lahaye).
  The [paper map](tutorial/paper-map.md) gives the details.

**Access limitation.** The build environment could not download the Utrecht
preprint (the host was blocked by the environment's network policy), nor
arXiv or journal pages directly. The structure of the review was confirmed from
its published abstract and bibliographic records, and the paper map is
therefore organised by the review's themes rather than its section numbers.
Everything else was checked through web-search results and by recomputing
numbers locally.

## How numbers were checked

- **Single source of truth.** All reference data live in
  [`tutorial/figures/atomdata.py`](tutorial/figures/atomdata.py) and are listed in
  [`tutorial/00-notation.md`](tutorial/00-notation.md). Rb-87 D-line values follow
  Steck's tables; recomputed values agree with them: $T_D=145.6\ \mu$K,
  $v_r=5.885$ mm/s, $T_r=362$ nK, $I_{\rm sat}=1.669$ mW/cm$^2$, and a cycling
  dipole of $2.989\,ea_0$.
- **Hyperfine and Zeeman data** were computed with the ARC library: 5P1/2
  splitting 816.66 MHz; 5P3/2 splittings 72.22, 156.94, 266.65 MHz; clock-state
  quadratic Zeeman shift 575.15 Hz/G$^2$.
- **Tweezer data** use a two-line (D1 + D2) Lorentz-oscillator polarizability.
  It gives 677 a.u. at 1064 nm (ARC's full sum: 679 a.u.), a tune-out wavelength
  of 790.03 nm (the measured value is 790.03 nm), and a static polarizability
  within 3.3% of the measured 318.8 a.u.
- **Rydberg data** (quantum defects, lifetimes at 0 and 300 K, $C_6$) were
  computed with ARC for $n=40$ to 100. For 70S: $C_6/h=862.7$ GHz $\mu$m$^6$,
  $\tau=374\ \mu$s (0 K) and $146\ \mu$s (300 K). The fitted scaling exponents
  are $-2.00$ (binding energy), $3.00$ (lifetime) and $11.3$ ($C_6$).
- **The Levine CZ gate** parameters were re-derived numerically:
  $\Delta/\Omega=0.3774$, $\tau\Omega=4.2927$ per pulse, and $\xi=3.902$ rad in the
  phase convention of Chapter 11 ($2\pi-3.902=2.381$ rad in the opposite one).
- **Worked examples** in every chapter show their arithmetic. Each value was
  computed in Python before it was written down.

## Labs and their checks

All thirteen labs run headlessly with
`python hands-on/run_labs.py --all --check` (about 100 s on a 4-core machine) and pass.
Each lab defines a `checks` dictionary of independent comparisons. Examples:

| Lab | Independent check |
|---|---|
| 01 | QuTiP steady state equals $(s_0/2)/(1+s_0+(2\delta/\Gamma)^2)$ at every detuning; the width equals $\Gamma\sqrt{1+s_0}$ |
| 02 | a locked atom lags the design velocity by the amount the force balance predicts (2.37 m/s) |
| 03 | an event-by-event photon-kick simulation reproduces the analytic friction coefficient and the Doppler-temperature curve within statistical error |
| 04 | the MOT's spring constant and damping match numerical derivatives; a small oscillation matches the analytic damped oscillator |
| 05 | harmonic trap frequencies match the numerical curvature of the full Gaussian potential |
| 06 | a fit to synthetic release-and-recapture data recovers the input temperature |
| 07 | rearrangement success matches an exact hole-counting formula |
| 08 | the optimal imaging threshold equals the Poisson crossing point |
| 09 | exact classical trajectories reproduce the Kuhr et al. Ramsey envelope; $T_2^*\propto1/T$ |
| 10 | blockaded atoms oscillate at $\sqrt N\,\Omega$; residual double excitation scales as $(\Omega/V)^2$ |
| 11 | decay error equals $\Gamma$ times the time in $\vert r\rangle$; Doppler and blockade errors scale as $\sigma_v^2$ and $1/V^2$ |
| 12 | Monte Carlo agrees with the exact logical-error sum; pure erasures give $p^d/2$ |

Every figure was regenerated with `python tutorial/figures/make_figures.py` and
inspected visually for overlapping labels and for physics errors.
`python tools/check_repo.py` checks every local Markdown link and image and every HTML `src`/`href` target (not heading anchors or external URLs).

Validated on Linux with Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1,
Matplotlib 3.11.2 and QuTiP 5.3.1.

## Corrections made during checking

| Finding | Correction |
|---|---|
| A first draft of the differential light shift held $\Gamma$ fixed while shifting the transition frequency, overestimating $\eta$ by about a factor of 2 | The transition dipole is now held fixed; $\eta(1064\ {\rm nm})=6.1\times10^{-5}$. The same method gives $1.6\times10^{-4}$ for Cs at 1030 nm, consistent with the literature scale |
| A first polarizability draft weighted D1 and D2 by $(2J'+1)/(2J+1)$ instead of the fraction of the line strength | Weights 1/3 and 2/3; the result now agrees with ARC to 0.3% at 1064 nm |
| The Kaufman, Lester and Regal arXiv number was written as 1209.3087 | Corrected to 1209.2087 |
| The Rydberg chapter implied that one UV photon excites $nS$ states | One photon reaches $nP$ ($\Delta\ell=0$ is forbidden); $nS$ needs two photons |
| The 99.5% gate result was attributed to "gates of the Levine family" | Evered et al. used fast single-pulse optimal-control gates plus dark-state techniques; fidelity 99.52(4)% on up to 60 atoms |
| A quoted time-optimal duration of $7.612/\Omega$ could not be confirmed from search results | Stated as "about $7.6/\Omega$, about 10% faster than the two-pulse gate", which follows from $7.612$ versus $8.585$ in units of $1/\Omega$ (11%) |
| A tweezer-loading statement of "80 to 90%" was attributed jointly | Now specific: 89% (single tweezer) and 80% (10 × 10 array) from Brown et al. 2019; Grünzweig et al. 2010 credited for the method |
| Lett et al. 1988 was quoted as "about 40 $\mu$K" | $43\pm20\ \mu$K against a Doppler limit of about 240 $\mu$K |
| The Breit-Rabi, Sisyphus and quantum-defect figures had a mislabelled panel, an optical-pumping arrow drawn at the wrong position, and a 5S level drawn with the large-$n$ quantum defect | All redrawn: measured level energies from ARC, correct hilltop-to-valley pumping, labels moved |
| A worked example claimed $d=9$ suffices to match a 98%-erasure $d=5$ code | Exact computation gives $1.2\times10^{-8}$ at $d=9$; $d=11$ is needed |

The reading list documents corrections to the bibliography entries (author,
year and duplicate entries) in its final section.

## Citation checks

Paper identities, author lists, venues and arXiv numbers were checked against
web-search results for the arXiv, publisher and repository records of: the
primary text; Henriet et al.; Lett et al.; Nogrette et al.; Kim et al.; Endres
et al.; Barredo et al.; Brown et al.; Kaufman et al.; Thompson et al.; Kuhr et
al.; Levine et al. 2019 and 2022; de Léséleuc et al.; Jandura and Pupillo;
Evered et al. 2023; Tsai et al.; Wu et al.; Bluvstein et al. 2022, 2024 and 2025;
Chiu et al.; Manetsch et al.; Baranes et al.; Geim et al.; Samajdar et al.; and
every thesis and preprint in the bibliography section. Classic references
(1979 to 2001), the main reviews and three experiments (2017 to 2021) were
re-checked against arXiv, APS, Nature and ADS records in the third pass.

## Scope and limits

- The course teaches mechanisms with simple, explicitly stated models: a
  two-level atom for Doppler cooling, a $J=0\to J'=1$ atom for the MOT, a scalar
  two-line polarizability, constant-pulse Rydberg gates with idealised error
  models, and a repetition code for erasure. The [paper map](tutorial/paper-map.md)
  lists what an advanced course would add.
- Experimental numbers are illustrative and computed for Rb-87; real machines
  use other species, wavelengths and parameters.
- No experimental data were used. The labs' checks are regression guards for
  the stated models, not validation against measurements.
