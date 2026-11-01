# Repository review, 1 November 2026

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
  $\tau=374\ \mu$s (0 K) and $147\ \mu$s (300 K). The fitted scaling exponents
  are $-2.00$ (binding energy), $3.00$ (lifetime) and $11.3$ ($C_6$).
- **The Levine CZ gate** parameters were re-derived numerically:
  $\Delta/\Omega=0.3774$, $\tau\Omega=4.2927$ per pulse, and $\xi=3.902$ rad in the
  phase convention of Chapter 11 ($2\pi-3.902=2.381$ rad in the opposite one).
- **Worked examples** in every chapter show their arithmetic. Each value was
  computed in Python before it was written down.

## Labs and their checks

All twelve labs run headlessly with
`python hands-on/run_labs.py --all --check` (about 75 s on one core) and pass.
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
`python tools/check_repo.py` checks every local link and image.

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
| A quoted time-optimal duration of $7.612/\Omega$ could not be confirmed from search results | Stated as "about $7.6/\Omega$, about 10% faster than the two-pulse gate", which the abstract supports |
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
(1975 to 2010) and the main reviews were cited from standard records and are
marked *(not independently checked)* in the reading list.

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
