# 09 · Atomic Qubits, Single-Qubit Gates and Coherence

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

We now have a defect-free array of single, cold atoms, and each one has to become a qubit. That means picking two internal states to store it in (usually the hyperfine "clock" states of Chapter 02, though other encodings are gaining ground), rotating it with microwaves or two-photon Raman lasers, and addressing one atom without disturbing its neighbours. Most of the chapter, though, is about how long the qubit keeps its phase. The trap of Chapter 07 shifts the two qubit states by slightly different amounts, and an atom's thermal motion turns that into dephasing. Lab 09 reproduces the classic analytic result for that dephasing from exact atomic trajectories, and shows how a spin echo removes it.

## Where to store a qubit

| Encoding | States (example) | Splitting | Strengths | Caveats |
|---|---|---|---|---|
| **Hyperfine clock qubit** | Rb-87 $\vert F{=}1,m_F{=}0\rangle$, $\vert F{=}2,m_F{=}0\rangle$ | 6.83 GHz (microwave) | no linear Zeeman shift; long $T_1$ and $T_2$ | differential light shift in the trap |
| Zeeman qubit | two $m_F$ sublevels of one $F$ | MHz per gauss | simple to drive | linearly field sensitive (Chapter 02) |
| **Ground-Rydberg qubit** | $\vert g\rangle$, $\vert r\rangle=\vert70S\rangle$ | about 1009 THz (297 nm, UV; driven as two photons, 420 + 1013 nm) | directly interacting; used in analog simulators | Rydberg lifetime $\sim100\ \mu$s; laser phase noise |
| Nuclear-spin qubit | $^{87}$Sr ($I=9/2$) or $^{171}$Yb ($I=1/2$) in the $^1S_0$ ground state | about 0.2 to 0.75 kHz per gauss (kHz to about 100 kHz at typical bias fields) | no electronic angular momentum: tiny magnetic and light-shift sensitivity | needs two-electron atoms |
| Optical clock qubit | Sr $^1S_0$ and the metastable $^3P_0$ state | 429 THz (698 nm) | ultra-narrow line; magic-wavelength traps | ultrastable lasers needed |

This course keeps to the Rb-87 clock qubit, $|0\rangle=|F{=}1,m_F{=}0\rangle$ and $|1\rangle=|F{=}2,m_F{=}0\rangle$. The ground-Rydberg transition appears again in Chapters 10 and 11 as the mechanism for entangling gates.

**Initialisation.** Optical pumping prepares $|0\rangle$. With $\pi$-polarized light on $F=1\to F'=1$, every sublevel of $F=1$ can be excited except $m_F=0$: the $m_F=0\to m_F'=0$ transition is forbidden when $\Delta F=0$ (its Clebsch-Gordan coefficient vanishes). A repumper on $F=2\to F'=2$ returns atoms that decay to $F=2$; it must not be purely $\pi$-polarized, or $|F{=}2,m_F{=}0\rangle$ would be dark too and atoms would pile up there. The D1 line is often used for pumping because its two excited hyperfine levels are 817 MHz apart, which keeps the light cleanly on one transition. After a few scattering events every atom ends up in the dark state $|F{=}1,m_F{=}0\rangle$. Fidelities above 99% are routine; residual errors come from imperfect polarization and off-resonant excitation of other hyperfine levels.

## Single-qubit gates

### Microwaves

The qubit splitting is a microwave frequency, so the simplest way to drive $|0\rangle\leftrightarrow|1\rangle$ is a microwave horn or antenna at 6.834 GHz. The wavelength is $c/6.834\ {\rm GHz}=4.4$ cm, much larger than the array, so every atom sees the same field and a microwave pulse acts on the whole array at once (a **global** drive). Microwaves are clean (no spontaneous emission) but slow; Rabi frequencies of tens of kHz give $\pi$ pulses of tens of microseconds.

### Two-photon Raman transitions

Two laser beams detuned by $\Delta$ from the excited state, with frequencies differing by exactly the qubit splitting, drive the qubit through a virtual level. Adiabatically eliminating the excited state (it is barely populated when $|\Delta|\gg\Omega_1,\Omega_2,\Gamma$) gives an effective two-level system with

$$\Omega_{\rm eff}=\frac{\Omega_1\Omega_2}{2\Delta}.$$

Raman beams can be focused onto single atoms or steered with AODs, giving **local** gates with Rabi frequencies of MHz.

![Left: lambda-type Raman scheme; beam 1 couples the F = 2 clock state and beam 2 couples the F = 1 clock state to a virtual level detuned by Delta below the 5P excited state, with a frequency difference of 6.834 GHz. Right: the spontaneous-scattering probability per pi pulse, pi Gamma over the magnitude of Delta, versus detuning on log axes, falling from 1 times ten to the minus three at 20 GHz to 3.8 times ten to the minus four at 50 GHz; a dotted line at the 7.1 THz fine-structure splitting marks where both P levels must be included](figures/09-raman.png)

*Raman gates. Off-resonant light can scatter photons during the pulse. The plotted quantity counts scattering events; the resulting gate infidelity depends on the scattering channels and their effect on the qubit.*

**The cost: spontaneous scattering.** With $\Omega_1=\Omega_2=\Omega$, each beam excites the atom off-resonantly at rate $\Gamma\Omega^2/4\Delta^2$, so the total scattering rate is $R=\Gamma\Omega^2/2\Delta^2$ (this assumes $|\Delta|\gg\omega_{\rm hfs}$, so that both beams scatter from whichever qubit state is populated). A $\pi$ pulse lasts $\pi/\Omega_{\rm eff}=2\pi\Delta/\Omega^2$, so the probability of scattering a photon during it is

$$P_{\rm sc}=R\,\frac{\pi}{\Omega_{\rm eff}}=\frac{\pi\Gamma}{|\Delta|},$$

independent of laser power within this simplified model. $P_{\rm sc}$ is a scattering probability, not an average gate infidelity. Raman scattering changes the internal state; Rayleigh scattering returns it to the same state but can still dephase a superposition if the scattering amplitudes distinguish the qubit states. The error therefore requires the multilevel, polarization-dependent scattering amplitudes and branching channels. A useful D2-dominated clock-state limit has approximately two thirds Rayleigh and one third Raman scattering, but that fraction is not universal and does not apply to a closed stretched-state cycling transition. See [Ozeri et al. (2007)](https://doi.org/10.1103/PhysRevA.75.042329) and [Uys et al. (2010)](https://doi.org/10.1103/PhysRevLett.105.200401). At $\Delta/2\pi=50$ GHz, $P_{\rm sc}=\pi\times6.07/50\,000=3.8\times10^{-4}$. For comparison, a Raman system designed for large arrays (Levine et al., 2022) drove about 300 Rb-87 qubits at 2 MHz Rabi frequency with a scattering error below $2\times10^{-4}$ per $\pi$ pulse. Increasing $\Delta$ helps until it becomes comparable to the fine-structure splitting (7.1 THz for Rb); then the D1 and D2 contributions to $\Omega_{\rm eff}$ partially cancel and the simple estimate no longer applies.

### Addressing one atom in an array

Three strategies are common:

1. **Focused Raman beams** on the chosen atoms.
2. **Light-shift addressing**: a focused off-resonant beam shifts the qubit frequency of selected atoms (through the same differential light shift that causes the dephasing discussed below), so that a global microwave or Raman pulse is resonant only with the unshifted atoms. A global pulse plus a pattern of shifts implements a different rotation on each group.
3. **Moving atoms** to a separate zone where they receive the gate (Chapter 12).

Crosstalk, the fraction of the addressing light reaching neighbours a few micrometres away, is a key specification.

## Coherence: how long does the qubit last?

Two time scales describe a qubit's memory, as in any two-level system:

- $T_1$: how long populations survive. For hyperfine qubits the main mechanism is **Raman scattering of trap photons**, which can change the hyperfine state. For far-detuned traps it is slow: for a 1 mK trap the two-line model gives $T_1$ of a few seconds at 852 nm and minutes at 1064 nm, where the hyperfine-changing amplitudes from D1 and D2 nearly cancel (exact values depend on state and polarization, and the rate scales linearly with the depth).
- $T_2$: how long the phase of a superposition survives. This is the limiting time, and it has several contributions.

### Thermal dephasing from the differential light shift

Chapter 07 showed that the trap shifts $|1\rangle$ a little more than $|0\rangle$, by a fraction $\eta$ of the local light shift. If every atom felt the same intensity this would just be a constant frequency offset that can be calibrated away. But atoms have thermal energy, and an atom with motional energy $E$ spends its time higher in the well, where the light is less intense. In a harmonic trap the time-averaged potential energy is $E/2$, so that atom's qubit frequency is offset by

$$\delta(E)=\frac{\eta E}{2\hbar}$$

relative to an atom at rest at the bottom. A thermal ensemble has a spread of energies, so a Ramsey experiment (two $\pi/2$ pulses separated by a free evolution time $t$) sees a spread of phases. For a 3D harmonic trap the Boltzmann energy distribution is $P(E)\propto E^2e^{-E/k_BT}$, and averaging $e^{i\delta(E)t}$ over it gives

$$\boxed{\ C(t)=\Big[1+\Big(\frac{\eta k_BTt}{2\hbar}\Big)^2\Big]^{-3/2}=\Big[1+0.95\Big(\frac{t}{T_2^*}\Big)^2\Big]^{-3/2},\qquad T_2^*=0.97\,\frac{2\hbar}{\eta k_BT}\ }$$

where the numbers come from defining $T_2^*$ as the $1/e$ time: $0.95=e^{2/3}-1$ and $0.97=\sqrt{e^{2/3}-1}$. This is the result of Kuhr et al. (2005). The envelope is not exponential; it falls off as a power law at long times.

$T_2^*$ gets longer if the atoms are colder or if $\eta$ is smaller, which means a farther-detuned trap. For Rb at $10\ \mu$K, $T_2^*=6.6$ ms in an 852 nm trap ($\eta=2.3\times10^{-4}$) and 24 ms at 1064 nm ($\eta=6.1\times10^{-5}$). The trap depth does not appear. A deeper trap shifts the qubit more, but the spread of shifts is set by $k_BT$ alone. Depth enters indirectly, because lowering the trap adiabatically lowers the temperature ($T\propto\omega\propto\sqrt{U_0}$, valid while $k_BT\ll U_0$ and the ramp is slow compared with the oscillation period), so $T_2^*$ grows as $1/\sqrt{U_0}$ when an experiment ramps the trap down before a coherent operation.

![Left: Ramsey contrast versus free-evolution time from lab 09 for atoms at 5, 10 and 20 microkelvin in an 852 nm tweezer, falling to 1/e at 13.2, 6.6 and 3.3 ms; dots show the analytic formula of Kuhr et al. on top of the simulated curves; a dashed line at contrast 1 shows that spin echo removes the dephasing. Right: T2 star versus temperature on log axes for 852 nm and 1064 nm traps, both falling as one over temperature, with the simulated points on the 852 nm line](../hands-on/09-ramsey-dephasing/figures/ramsey.png)

*Lab 09. Each simulated atom follows its exact classical trajectory, and the phase it accumulates is integrated in closed form; the averaged contrast reproduces the analytic formula. A spin echo cancels the dephasing because each atom's energy, and with it the time average of its frequency offset, stays constant during the sequence.*

### Spin echo and dynamical decoupling

Thermal dephasing is **reversible**: each atom keeps a constant frequency offset as long as its motional energy does not change. A $\pi$ pulse halfway through the free evolution swaps $|0\rangle$ and $|1\rangle$, so the phase accumulated in the second half has the opposite sign and cancels the first half. This **spin echo** removes any static offset, whether thermal, site-to-site variations of trap depth across the array, or a constant magnetic-field gradient.

![Two pulse sequences on a time axis. Ramsey: a pi/2 pulse, free evolution, a second pi/2 pulse, then imaging. Spin echo: a pi/2 pulse, free evolution accumulating phase plus phi, a pi pulse, free evolution accumulating phase minus phi, a final pi/2 pulse, then imaging](figures/09-sequences.png)

*Ramsey measures an inhomogeneous coherence time $T_2^*$. Hahn echo refocuses static frequency offsets and filters time-dependent noise; its measured decay time is denoted $T_{2,\rm echo}$. It is specific to that pulse sequence and need not be an irreversible coherence limit.*

Echo does not generally cancel all time-dependent noise. Its suppression of trap-intensity fluctuations, changes in motional energy and magnetic-field noise depends on their spectra and the pulse timing; pulse imperfections and addressing-laser phase noise can add further errors. Trains of many $\pi$ pulses (dynamical decoupling sequences such as CPMG and XY-8) suppress slowly varying noise further, and have extended hyperfine coherence in tweezers to the scale of seconds.

### Other dephasing sources, in numbers

| Source | Mechanism | Example magnitude |
|---|---|---|
| thermal motion | spread of $\eta E/2\hbar$ | $T_2^*=6.6$ ms (852 nm, $10\ \mu$K) |
| trap-depth inhomogeneity across the array | site-to-site $\eta\,\delta U_0$ | 2% depth spread at 852 nm, 1 mK: $0.02\times4.7$ kHz $=94$ Hz rms, a Gaussian $1/e$ time of $\sqrt2/(2\pi\times94\ {\rm Hz})=2.4$ ms (removed by echo) |
| magnetic field noise | clock shift $2\times575\ {\rm Hz/G^2}\times B\,\delta B$ | 1 mG at $B=3$ G: 3.5 Hz (Chapter 02) |
| Raman scattering of trap light | hyperfine-changing photon scattering | sets $T_1$: seconds (852 nm) to minutes (1064 nm) |
| gate laser phase and intensity noise | errors during operations | depends on the laser system |

## Worked example (Rb-87, illustrative numbers)

| Quantity | Formula | Value |
|---|---|---|
| microwave wavelength | $c/\nu_{\rm hfs}$ | 4.4 cm (global drive) |
| Raman: $\Omega_1=\Omega_2=2\pi\times100$ MHz, $\Delta=2\pi\times50$ GHz | $\Omega_{\rm eff}=\Omega^2/2\Delta$ | $2\pi\times100$ kHz |
| Raman $\pi$ time | $\pi/\Omega_{\rm eff}$ | **5 $\mu$s** |
| scattering probability per $\pi$ pulse (simplified model) | $\pi\Gamma/\lvert\Delta\rvert$ | **$3.8\times10^{-4}$** |
| differential shift at 1 mK, 852 nm | $\eta U_0/h$ | 4.7 kHz |
| $T_2^*$ at 10 $\mu$K, 852 nm | $0.97\times2\hbar/(\eta k_BT)$ | **6.6 ms** |
| gates within $T_2^*$ | $T_2^*/t_\pi$ | **~1300** |

**Step 1: Raman Rabi frequency.** $\Omega_{\rm eff}/2\pi=(100\ {\rm MHz})^2/(2\times50\,000\ {\rm MHz})=0.1$ MHz, so a $\pi$ pulse takes $1/(2\times0.1\ {\rm MHz})=5\ \mu$s.

**Step 2: scattering.** $P_{\rm sc}=\pi\times6.07\ {\rm MHz}/50\ {\rm GHz}=3.8\times10^{-4}$ per $\pi$ pulse in this model; converting this probability into gate infidelity requires the scattering channels.

**Step 3: thermal dephasing.** $2\hbar/(k_B\times10\ \mu{\rm K})=1.53\ \mu$s, divided by $\eta=2.26\times10^{-4}$ gives 6.8 ms, times 0.97 gives $T_2^*=6.6$ ms.

**Step 4: what that buys.** About $6.6\ {\rm ms}/5\ \mu{\rm s}\approx1300$ Raman $\pi$ pulses fit into $T_2^*$, and with spin echo the usable time extends much further. Single-qubit operations are therefore in good shape; the entangling gates of Chapters 10 and 11 are the harder part.

## Run it

[Lab 09](../hands-on/09-ramsey-dephasing/) simulates thermal atoms on exact harmonic trajectories in an 852 nm tweezer, computes the Ramsey contrast at three temperatures, compares it with the formula of Kuhr et al., checks the $1/T$ scaling of $T_2^*$, and shows that a spin echo restores the contrast.

## Common pitfalls

- **"Deeper traps dephase faster."** Not directly: the spread of differential shifts is $\eta k_BT/2\hbar$, independent of depth. Deeper traps matter through the temperature the atoms end up with, and through site-to-site depth variations (which scale with depth).
- **"Ramsey decay is exponential."** Thermal dephasing gives a power law, $[1+0.95(t/T_2^*)^2]^{-3/2}$. Fitting an exponential gives a misleading $T_2^*$.
- **Confusing $T_2^*$ and $T_2$.** $T_2^*$ includes reversible inhomogeneity; $T_{2,\rm echo}$ is the decay time under a specified echo sequence and can still be improved by a different decoupling sequence. Quote the sequence and decay convention.
- **"Raman errors fall forever with detuning."** The $\pi\Gamma/\Delta$ estimate assumes one excited level. Near and beyond the fine-structure splitting, the two P levels interfere and the coupling falls faster than the scattering.
- **Forgetting the laser.** Two Raman beams must be phase-coherent at the qubit frequency; their relative phase noise appears directly as qubit phase noise.

## Key takeaways

- The standard neutral-atom qubit is the hyperfine clock pair $|F{=}1,0\rangle$, $|F{=}2,0\rangle$; ground-Rydberg, nuclear-spin and optical-clock qubits are important alternatives.
- Microwaves give clean global rotations; Raman beams ($\Omega_{\rm eff}=\Omega_1\Omega_2/2\Delta$) give fast local gates with a scattering probability of about $\pi\Gamma/|\Delta|$ per $\pi$ pulse in the simplified model; the gate error depends on the scattering channels.
- The trap shifts the qubit by $\eta U$; thermal motion spreads this shift and gives $T_2^*=0.97\times2\hbar/(\eta k_BT)$ with a power-law envelope.
- For Rb at 10 $\mu$K: $T_2^*\approx6.6$ ms at 852 nm and 24 ms at 1064 nm. Spin echo and dynamical decoupling remove static inhomogeneity and extend coherence much further.

## Go deeper

- S. Kuhr et al., *Analysis of dephasing mechanisms in a standing-wave dipole trap*, Phys. Rev. A 72, 023406 (2005), [arXiv:quant-ph/0410037](https://arxiv.org/abs/quant-ph/0410037). The origin of the $T_2^*$ formula and a careful catalogue of dephasing mechanisms.
- M. Saffman, *Quantum computing with atomic qubits and Rydberg interactions: progress and challenges*, J. Phys. B 49, 202001 (2016), [arXiv:1605.05207](https://arxiv.org/abs/1605.05207). Qubit encodings, single-qubit gate methods and their error budgets.
- L. Henriet et al., *Quantum computing with neutral atoms*, Quantum 4, 327 (2020), [arXiv:2006.12326](https://arxiv.org/abs/2006.12326). Encodings and gates from a computing perspective.
- H. Levine et al., *Dispersive optical systems for scalable Raman driving of hyperfine qubits*, Phys. Rev. A 105, 032618 (2022), [arXiv:2110.14645](https://arxiv.org/abs/2110.14645). A practical Raman laser system for hundreds of tweezer qubits.
- J. D. Thompson et al., *Coherence and Raman sideband cooling of a single atom in an optical tweezer*, Phys. Rev. Lett. 110, 133001 (2013), [arXiv:1209.3028](https://arxiv.org/abs/1209.3028). Coherence of a hyperfine qubit in a tweezer, including the role of motion.

---

← Previous: [Loading, Imaging and Assembling Atom Arrays](08-arrays.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [Rydberg Atoms and the Blockade](10-rydberg.md) →
