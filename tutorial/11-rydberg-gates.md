# 11 · Rydberg Entangling Gates and Their Errors

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

Chapter 10 showed that two nearby atoms cannot both be excited to a Rydberg state. This chapter turns that "one at a time" rule into a **controlled-Z (CZ) gate** between hyperfine qubits. The idea is simple: a state that makes a full $2\pi$ round trip to $|r\rangle$ and back picks up a phase of $-1$, and the blockade decides which round trips are allowed. We work through the original **$\pi$-$2\pi$-$\pi$ protocol** of Jaksch et al., then the **global two-pulse phase gate** of Levine et al. that underlies today's parallel gates, and finally the **error budget**: Rydberg decay, Doppler dephasing, finite blockade strength, and the imperfections of real lasers. [Lab 11](../hands-on/11-cz-gate/) reproduces the published gate parameters and checks each error scaling.

> **Conventions.** Qubit states $|0\rangle=|F{=}1,m_F{=}0\rangle$ and $|1\rangle=|F{=}2,m_F{=}0\rangle$; only $|1\rangle$ is coupled to $|r\rangle$. The single-atom Hamiltonian is $\frac{\hbar\Omega}{2}(e^{-i\xi}|r\rangle\langle1|+{\rm h.c.})-\hbar\Delta|r\rangle\langle r|$ with laser phase $\xi$, as in the [notation page](00-notation.md).

## The key fact: a $2\pi$ rotation gives a minus sign

Drive a two-level system $|1\rangle\leftrightarrow|r\rangle$ resonantly for a time $2\pi/\Omega$. The population returns completely to $|1\rangle$, but the state has rotated by $2\pi$ about an axis on the Bloch sphere, and a spin-1/2 rotated by $2\pi$ changes sign:

$$e^{-i(\Omega t/2)\sigma_x}\Big|_{t=2\pi/\Omega}=\cos\pi\;\mathbb 1-i\sin\pi\;\sigma_x=-\mathbb 1 .$$

So "excite to $|r\rangle$ and come back" is a phase gate on $|1\rangle$. The blockade can switch it off: if the other atom is already in $|r\rangle$, the round trip cannot happen and no sign is picked up. Conditional phase is exactly what a CZ gate is.

## The $\pi$-$2\pi$-$\pi$ gate

The protocol of Jaksch et al. (2000), with light addressed separately to the control and target atoms:

1. a $\pi$ pulse on the control atom ($|1\rangle\to|r\rangle$),
2. a $2\pi$ pulse on the target atom,
3. a $\pi$ pulse on the control atom ($|r\rangle\to|1\rangle$).

Go through the four inputs:

| Input $\vert c\,t\rangle$ | What happens | Phase |
|---|---|---|
| $\vert00\rangle$ | no atom is coupled | $+1$ |
| $\vert01\rangle$ | target makes a $2\pi$ loop | $-1$ |
| $\vert10\rangle$ | control makes $\pi+\pi=2\pi$ loop; target uncoupled | $-1$ |
| $\vert11\rangle$ | control in $\vert r\rangle$ blocks the target; control completes $2\pi$ | $-1$ |

The result is ${\rm diag}(1,-1,-1,-1)$, which equals ${\rm CZ}$ followed by a $Z$ gate on each qubit. Single-qubit $Z$ rotations are cheap (they are just phase bookkeeping), so this *is* a CZ gate.

![Left: pulse sequence of the Jaksch gate with a pi pulse on the control, a 2 pi pulse on the target, and a second pi pulse on the control, with a table showing phases +1, -1, -1, -1 for inputs 00, 01, 10 and 11. Right: the Levine gate with two global pulses of equal length and detuning, the second with a laser phase xi; tau Omega = 4.29, Delta over Omega = 0.377, xi = 3.90, total duration 8.58 over Omega](figures/11-protocols.png)

*Two ways to make a CZ gate from the blockade. The Jaksch protocol needs individually addressed pulses; the Levine protocol uses the same global pulses on both atoms, so it can run on many pairs in parallel.*

## The global two-pulse gate

Addressing each atom separately with Rydberg lasers is technically hard. Levine et al. (2019) found a gate that uses the **same** pulse on both atoms. Apply two pulses of equal duration $\tau$ and detuning $\Delta$, the second with its laser phase shifted by $\xi$. Thanks to the blockade, each computational input evolves in a small, independent subspace:

- $|00\rangle$: nothing couples; no phase.
- $|01\rangle$ and $|10\rangle$: one atom is a two-level system $\{|1\rangle,|r\rangle\}$ with Rabi frequency $\Omega$ and detuning $\Delta$.
- $|11\rangle$: couples only to $|W\rangle=(|1r\rangle+|r1\rangle)/\sqrt2$, a two-level system with coupling $\sqrt2\Omega$ and detuning $\Delta$.

The design has two steps. First choose $\tau$ so that the $|11\rangle$ system completes **one full detuned cycle in each pulse**, $\sqrt{2\Omega^2+\Delta^2}\,\tau=2\pi$; then $|11\rangle$ returns home after each pulse, regardless of $\xi$. The single-atom system has not closed after the first pulse; choose $\xi$ so that the second pulse brings it back. Finally choose $\Delta$ so that the accumulated phases satisfy

$$\phi_{11}-\phi_{01}-\phi_{10}=\pi .$$

The solution is

$$\frac{\Delta}{\Omega}=0.377,\qquad\tau\Omega=4.29,\qquad\xi=3.90\ {\rm rad},$$

with a total duration $2\tau=8.58/\Omega$: 390 ns at $\Omega/2\pi=3.5$ MHz. Check the first condition: $\sqrt{2+0.377^2}\times4.29=1.464\times4.29=6.28\approx2\pi$. Lab 11 finds these values by numerical optimisation and confirms that the result is a CZ up to single-qubit phases. (With the opposite sign convention for the laser phase, the same gate has $\xi=2\pi-3.90=2.38$; both describe the same physics.)

**Faster gates.** Optimal-control methods find a single smooth, phase-modulated global pulse that does the same job about 10% faster; the time-optimal CZ gate takes about $7.6/\Omega$ (Jandura and Pupillo, 2022). Using such fast single-pulse gates, together with dark-state techniques to reduce intermediate-state scattering and improved Rydberg excitation and atom cooling, Evered et al. (2023) reached a CZ fidelity of 99.52(4)% on up to 60 atoms in parallel. The first global two-pulse gate (Levine et al., 2019) had a fidelity of at least 97.4%.

## The error budget

A gate fidelity is limited by everything that happens while atoms are in $|r\rangle$. Lab 11 adds each error source to the two-atom simulation and compares with a simple formula. The **average gate fidelity** $F$ compares the simulated 4 × 4 propagator with an ideal CZ (up to single-qubit $Z$ phases); $1-F$ is the infidelity.

### 1. Rydberg decay

While an atom is in $|r\rangle$ it can decay (radiatively or by blackbody transfer) at rate $\Gamma=1/\tau_r$. To first order the infidelity is $\Gamma$ times the time spent in $|r\rangle$, averaged over the four inputs:

$$1-F\approx\Gamma\,\overline{T_R},\qquad\overline{T_R}=\tfrac14\big(T_R^{00}+T_R^{01}+T_R^{10}+T_R^{11}\big).$$

For the Levine gate at $\Omega/2\pi=3.5$ MHz the lab finds $T_R=0,\ 0.208,\ 0.208,\ 0.182\ \mu$s, so $\overline{T_R}=0.150\ \mu$s. With $\tau_r=146\ \mu$s (70S at 300 K), $1-F=0.150/146=1.0\times10^{-3}$. Since $T_R\propto1/\Omega$, faster gates reduce this error; colder surroundings (smaller blackbody rate) and higher $n$ (longer lifetime) do too.

### 2. Doppler dephasing

A moving atom sees the two-photon Rydberg light shifted by $k_{\rm eff}v$ (Chapter 10). Over a gate lasting a few hundred nanoseconds the velocity is effectively constant, so this is a random static detuning, rms $k_{\rm eff}\sigma_v=2\pi\times43$ kHz at $10\ \mu$K. A detuning error $\delta$ causes an infidelity of order $(\delta/\Omega)^2$: the lab finds $5.6\times10^{-4}$ at $10\ \mu$K, scaling as $\sigma_v^2\propto T$. Colder atoms and faster gates reduce it. The usual counter-propagating 420/1013 nm arrangement already removes most of it (co-propagating beams would add the wavevectors, multiplying the Doppler detuning by 2.4 and the infidelity by about six), and three-photon schemes whose wavevectors cancel can remove it entirely.

### 3. Finite blockade

With $V$ finite, $|11\rangle$ couples weakly to $|rr\rangle$, which shifts its phase and leaks population. The infidelity scales as $(\hbar\Omega/V)^2$: $1.7\times10^{-4}$ at $V/h=211$ MHz (two 70S atoms 4 $\mu$m apart), four times smaller at twice the interaction. Faster gates make it worse.

![Left: population of the initial state during the Levine gate; the 11 state returns to 1 at the end of the first pulse, the 01 state only at the end of the second pulse after the phase jump. Right: gate infidelity versus Rydberg Rabi frequency on log axes for Rydberg decay (falling as one over Omega), Doppler dephasing at 10 microkelvin (falling as one over Omega squared), finite blockade at 211 MHz (rising as Omega squared), and their sum, which has a minimum of about 1.3 times ten to the minus three near 6 MHz](../hands-on/11-cz-gate/figures/cz_gate.png)

*Lab 11. Left: the two pulses of the Levine gate. Right: the three intrinsic errors scale differently with $\Omega$, so there is an optimal Rabi frequency. Real experiments add laser and control errors on top.*

### 4. Technical errors

The intrinsic budget above totals about $1.7\times10^{-3}$ (worked example below). In experiments other errors usually dominate:

- **Laser phase noise.** The Rydberg lasers' phase directly enters the gate; noise at frequencies near $\Omega$ is especially harmful. Narrow-linewidth lasers locked to high-finesse cavities, with filtered "servo bumps", are essential.
- **Intensity noise and inhomogeneity.** A 1% error in $\Omega$ shifts the pulse areas; across a large array the beams must be uniform, and robust pulse designs tolerate small errors.
- **Intermediate-state scattering.** In two-photon schemes the atom briefly occupies $6P_{3/2}$ (lifetime 118 ns) with probability $\sim\Omega_1^2/4\Delta_i^2$. The resulting error per gate is of order $\pi\Gamma_i/\Delta_i$: about $2\times10^{-3}$ for $\Gamma_i/2\pi=1.35$ MHz and $\Delta_i/2\pi=2$ GHz (a rough estimate for a single $2\pi$-area pulse with $\Omega_1=\Omega_2$; the Levine gate has about 1.4 times that area per atom, and the result depends on the ratio $\Omega_1/\Omega_2$).
- **Atomic motion and position.** Thermal motion also changes $V$ (if not deep in the blockade regime) and the local intensity.
- **Leakage and loss.** Atoms that decay from $|r\rangle$ may end up outside the qubit subspace or be lost from the trap. Chapter 12 shows that such errors, if detected, can be easier to correct than ordinary errors.

## Worked example: a CZ gate on Rb-87 70S (illustrative numbers)

| Quantity | Value |
|---|---|
| $\Omega/2\pi$, $R$, $V/h$ | 3.5 MHz, 4.0 $\mu$m, 211 MHz (asymptotic $C_6/R^6$; Chapter 10) |
| gate parameters | $\Delta/\Omega=0.377$, $\tau\Omega=4.29$, $\xi=3.90$ |
| gate duration | $8.58/\Omega=$ **390 ns** |
| mean time in $\vert r\rangle$ | **0.150 $\mu$s** |
| decay error ($\tau_r=146\ \mu$s) | **$1.0\times10^{-3}$** |
| Doppler error (10 $\mu$K) | **$5.6\times10^{-4}$** |
| finite-blockade error | **$1.7\times10^{-4}$** |
| intrinsic total | **$\approx1.7\times10^{-3}$** ($F\approx99.8\%$) |

**Step 1: duration.** $2\times4.29/(2\pi\times3.5\ {\rm MHz})=8.58/(22.0\ \mu{\rm s}^{-1})=0.390\ \mu$s.

**Step 2: decay.** $0.150\ \mu{\rm s}/146\ \mu{\rm s}=1.0\times10^{-3}$. This is the largest intrinsic term.

**Step 3: Doppler.** $k_{\rm eff}\sigma_v/\Omega=2\pi\times43\ {\rm kHz}/(2\pi\times3.5\ {\rm MHz})=0.012$; the infidelity is a few times $0.012^2$, and the lab gives $5.6\times10^{-4}$.

**Step 4: blockade.** $\Omega/V=3.5/211=0.017$; the infidelity is of order $(\Omega/V)^2/2$, and the lab gives $1.7\times10^{-4}$.

**Step 5: verdict.** About $1.7\times10^{-3}$ from decay, motion and finite interaction (part of the blockade error is a deterministic phase that recalibrating $\Delta$ and $\xi$ can absorb; fluctuations of the atom positions cannot be), before laser noise and intermediate-state scattering. This is why the 99.5% demonstration of 2023 was a milestone, and why cryogenic environments, higher Rydberg states, faster robust pulses and colder atoms are all active research directions.

## Run it

[Lab 11](../hands-on/11-cz-gate/) simulates two three-level atoms with the full $9\times9$ Hamiltonian, recovers the Levine gate parameters by optimisation, verifies the conditional phase, checks the decay, Doppler and blockade error scalings, and confirms the $\pi$-$2\pi$-$\pi$ truth table.

## Common pitfalls

- **"The phases in the table are the whole story."** Population must also return to the qubit subspace; a gate with the right phases but leakage to $|r\rangle$ is not a CZ. The lab's fidelity measure checks both.
- **Single-qubit phases.** Both protocols produce CZ only up to local $Z$ rotations, which must be tracked or corrected. Comparing with a bare CZ underestimates the fidelity.
- **Laser-phase conventions.** The sign of $\xi$ depends on how the Hamiltonian is written; 3.90 and 2.38 rad are the same gate in opposite conventions.
- **"More power is always better."** Faster gates reduce decay and Doppler errors but increase the finite-blockade error and can increase intermediate-state scattering.
- **Ignoring spectator atoms.** In a dense array, atoms that should not take part may be within a blockade radius of an excited atom. Gate layouts space pairs so that only the intended partners interact.

## Key takeaways

- A $2\pi$ excursion to $|r\rangle$ multiplies a state by $-1$; the blockade makes that phase conditional.
- The $\pi$-$2\pi$-$\pi$ gate gives ${\rm diag}(1,-1,-1,-1)$ = CZ up to local $Z$, but needs individual addressing.
- The global Levine gate uses two identical pulses with a phase jump: $\Delta/\Omega=0.377$, $\tau\Omega=4.29$, $\xi=3.90$, total $8.58/\Omega$; time-optimal single pulses take about $7.6/\Omega$.
- Intrinsic errors: decay $\Gamma\overline{T_R}\propto1/\Omega$, Doppler $\propto T/\Omega^2$, finite blockade $\propto(\Omega/V)^2$. For Rb 70S at 3.5 MHz they total about $1.7\times10^{-3}$.
- Laser phase noise, intensity errors and intermediate-state scattering add to this; fidelities of 99.5% have been demonstrated in parallel on many pairs.

## Go deeper

- D. Jaksch, J. I. Cirac, P. Zoller, S. L. Rolston, R. Côté, M. D. Lukin, *Fast quantum gates for neutral atoms*, Phys. Rev. Lett. 85, 2208 (2000), [arXiv:quant-ph/0004038](https://arxiv.org/abs/quant-ph/0004038). The original proposal.
- H. Levine et al., *Parallel implementation of high-fidelity multiqubit gates with neutral atoms*, Phys. Rev. Lett. 123, 170503 (2019), [arXiv:1908.06101](https://arxiv.org/abs/1908.06101). The global two-pulse gate.
- S. Jandura and G. Pupillo, *Time-optimal two- and three-qubit gates for Rydberg atoms*, Quantum 6, 712 (2022), [arXiv:2202.00903](https://arxiv.org/abs/2202.00903).
- S. J. Evered et al., *High-fidelity parallel entangling gates on a neutral-atom quantum computer*, Nature 622, 268 (2023), [arXiv:2304.05420](https://arxiv.org/abs/2304.05420).
- S. de Léséleuc, D. Barredo, V. Lienhard, A. Browaeys, T. Lahaye, *Analysis of imperfections in the coherent optical excitation of single atoms to Rydberg states*, Phys. Rev. A 97, 053803 (2018), [arXiv:1802.10424](https://arxiv.org/abs/1802.10424). A careful experimental error analysis: Doppler, laser noise, intermediate-state scattering.
- M. Saffman, T. G. Walker, K. Mølmer, *Quantum information with Rydberg atoms*, Rev. Mod. Phys. 82, 2313 (2010), [arXiv:0909.4777](https://arxiv.org/abs/0909.4777).

---

← Previous: [Rydberg Atoms and the Blockade](10-rydberg.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [Toward Fault Tolerance: Readout, Loss, Erasure and Zoned Architectures](12-architectures.md) →
