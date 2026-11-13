# Read → predict → run → explain

Use this page as your laboratory notebook. For each chapter: read it, work the
checkpoint on paper, run the linked lab, then change one parameter and explain
what happens before you look at the plot. A session takes 45 to 90 minutes; the
whole course takes a dozen sessions.

Start with the [notation and reference numbers](00-notation.md), the
[paper map](paper-map.md) and the [Python setup](../hands-on/README.md). All
commands run from the repository root.

| Chapter | By the end you should be able to… | Run and investigate |
|---|---|---|
| [01](01-introduction.md) | Explain the experimental cycle and estimate how many photons it takes to stop an atom | `python tutorial/figures/make_figures.py 01`; read the frequency-scale figure |
| [02](02-atomic-structure.md) | Read the Rb-87 level diagram and explain why the clock states are the standard qubit choice | `python tutorial/figures/make_figures.py 02`; change the plotted field range in `breit_rabi()` of `tutorial/figures/ch02.py` |
| [03](03-atom-light.md) | Solve the optical Bloch equations and use the scattering-rate formula | `python hands-on/01-optical-bloch/obe.py`; add a detuning |
| [04](04-optical-forces.md) | Distinguish the scattering and dipole forces and explain why traps are far detuned | `python tutorial/figures/make_figures.py 04` |
| [05](05-doppler-cooling.md) | Design a Zeeman slower and derive the Doppler limit | `python hands-on/run_labs.py 02 03`; change $\eta$ and the emission model |
| [06](06-sub-doppler-mot.md) | Explain Sisyphus cooling and compute the MOT spring constant | `python hands-on/04-mot/mot.py`; flip the field gradient |
| [07](07-optical-tweezers.md) | Compute tweezer depth, frequencies and scattering at any wavelength | `python hands-on/run_labs.py 05 06`; change the waist |
| [08](08-arrays.md) | Explain collisional blockade, imaging fidelity and rearrangement statistics | `python hands-on/run_labs.py 07 08`; raise the loading probability |
| [09](09-qubits-coherence.md) | Estimate Raman gate errors and the thermal $T_2^*$, and explain spin echo | `python hands-on/09-ramsey-dephasing/ramsey.py`; switch to 1064 nm (change both `eta` and the axial frequency in `omegas`) |
| [10](10-rydberg.md) | Use Rydberg scaling laws, compute the blockade radius, and explain adiabatic state preparation | `python hands-on/run_labs.py 10 13`; change the sweep time and the spacing |
| [11](11-rydberg-gates.md) | Explain how the blockade makes a CZ gate and build an error budget | `python hands-on/11-cz-gate/cz_gate.py`; change $\Omega$ and the lifetime |
| [12](12-architectures.md) | Explain erasure conversion and zoned architectures | `python hands-on/12-erasure-code/erasure.py` |

## Checkpoints: try before revealing the answers

1. **Stopping an atom (Ch 01):** How many 780 nm photons does it take to stop a
   Rb-87 atom moving at 300 m/s, and what is the shortest possible stopping time?
2. **Clock states (Ch 02):** At a bias field of 3 G, by how much is the clock
   transition shifted, and how sensitive is it to field noise (in Hz per mG)?
   Why can an atom on $F=2\to F'=3$ never decay to $F=1$?
3. **Scattering (Ch 03):** For $I=1$ mW/cm$^2$ on the cycling transition, find
   $s_0$ and the scattering rate at $\delta=-\Gamma/2$. What is the full width at
   half maximum at $s_0=10$?
4. **Forces (Ch 04):** 1 mW focused to a 10 $\mu$m waist, 50 GHz red of D2, treating the atom as the two-level cycling transition driven with $\sigma^+$ light: how
   deep is the trap and how fast does the atom scatter? Why is this a poor qubit
   trap?
5. **Doppler limit (Ch 05):** What is the Doppler limit for Cs
   ($\Gamma/2\pi=5.234$ MHz), and at which detuning is it reached?
6. **MOT (Ch 06):** For $A=10$ G/cm, $\delta=-\Gamma$, $s_0=1$ per beam, compute the
   spring constant and trap frequency. Is the motion over- or underdamped?
7. **Tweezer (Ch 07):** How much 1064 nm power gives a 1 mK trap with
   $w_0=0.8\ \mu$m, and what is the radial trap frequency?
8. **Arrays (Ch 08):** What is the probability that a 100-site array is
   defect-free *without* rearrangement (loading probability $p=0.5$, vacuum
   lifetime $\tau=60$ s, cycle time $t=0.2$ s)? With rearrangement, the same
   $\tau$ and $t$, and 1% loss per move, sorting a 16 × 16 array loaded at $p=0.5$
   into a central 10 × 10 block (the geometry of lab 07)?
9. **Coherence (Ch 09):** Find $T_2^*$ for a Rb atom at 10 $\mu$K in a 1064 nm
   tweezer. Would a spin echo remove dephasing caused by magnetic-field noise at
   1 kHz?
10. **Blockade (Ch 10):** For $70S$, what is the blockade radius at
    $\Omega/2\pi=1$ MHz? What is $V/h$ at 6 $\mu$m?
11. **Gates (Ch 11):** How long is a Levine CZ gate at $\Omega/2\pi=5$ MHz, and
    what is its decay error with $\tau_r=146\ \mu$s?
12. **Erasure (Ch 12):** For a $d=3$ repetition code at $p=5\%$, compare the
    logical error with bit-flip errors and with all-erasure errors.

<details>
<summary>Answers and interpretation</summary>

1. $N=v_0/v_r=300/(5.885\times10^{-3})\approx5.1\times10^4$ photons; at most
   $\Gamma/2=1.9\times10^7$ photons per second, so at least 2.7 ms (and 0.40 m).
2. $575.15\times3^2=5.2$ kHz; $d\nu/dB=2\times575.15\times3=3.45$ kHz/G
   $=3.5$ Hz/mG. $F'=3\to F=1$ would need $\Delta F=-2$, which an electric-dipole
   transition cannot do.
3. $s_0=1/1.669=0.599$; $\gamma_p=\frac\Gamma2\frac{0.599}{1+0.599+1}=4.4\times10^6\ {\rm s^{-1}}$;
   FWHM $=6.07\sqrt{11}=20.1$ MHz.
4. $U_0=h\times35$ MHz $=k_B\times1.7$ mK and $\gamma_p=2.7\times10^4\ {\rm s^{-1}}$:
   recoil heating is about $2E_r\gamma_p/k_B=9.8$ mK/s, giving the rough energy-budget time $U_0/(2E_r\gamma_p)\approx0.17$ s. This is a heating estimate, not a measured trap lifetime. In the ideal stretched-state cycling model with pure $\sigma^+$ light, spontaneous emission returns the atom to $|F=2,m_F=2\rangle$; it does not change the hyperfine state. A clock-qubit trap needs a separate multilevel calculation of both qubit states, polarization-dependent shifts and scattering. The one-third Raman fraction discussed for clock states cannot be applied to this closed transition.
5. $T_D=\hbar\Gamma/2k_B=125.6\ \mu$K, at $\delta=-\Gamma/2$ and low intensity.
6. $\kappa=\mu_BA\beta/\hbar k=1.66\times10^{-18}$ N/m, $f=540$ Hz; damping rate
   $\beta/m=1.05\times10^4\ {\rm s^{-1}}>2\omega_0=6.8\times10^3\ {\rm s^{-1}}$, so it is
   overdamped (lab 04).
7. Depth per mW scales as $1/w_0^2$: $P=10.3\times0.64=6.6$ mW. At fixed depth
   $f_r\propto1/w_0$: $98.5/0.8=123$ kHz.
8. $0.5^{100}e^{-100\times0.2/60}=5.7\times10^{-31}$. With rearrangement,
   averaging $0.99^h$ over the binomial number of holes $h$ gives
   $0.995^{100}=0.606$, and $0.606\times e^{-1/3}=0.606\times0.717=0.43$, because
   the reservoir almost never runs short. Lab 07's Monte Carlo gives
   $0.411\pm0.013$. Fewer than half the cycles succeed in one round.
9. $T_2^*=0.97\times2\hbar/(\eta k_BT)$ with $\eta=6.08\times10^{-5}$: 24 ms. Echo suppression of 1 kHz noise depends on the total free-evolution time and noise spectrum. For ideal instantaneous pulses and sinusoidal frequency noise, the Hahn-echo response is $|Y(\omega)|^2=16\sin^4(\omega T/4)/\omega^2$. A 1 kHz tone is exactly cancelled at $T=2$ ms (and integer multiples), but not generally at other durations. Short sequences suppress slowly varying noise; multiple-pulse sequences can provide broader or better-targeted suppression.
10. $R_b=(863\times10^3)^{1/6}\ \mu{\rm m}=9.8\ \mu$m; $V/h=863\times10^3/6^6=18.5$ MHz.
11. $8.585/\Omega=273$ ns. Chapter 11 (lab 11) gives a mean time in $|r\rangle$,
    averaged over the four input states, of $0.150\ \mu$s at $\Omega/2\pi=3.5$ MHz.
    It scales as $1/\Omega$: $0.150\times3.5/5=0.105\ \mu$s, so the decay error is
    $0.105/146=7\times10^{-4}$.
12. Bit flips: $3p^2-2p^3=7.25\times10^{-3}$. Erasure: $p^3/2=6.3\times10^{-5}$,
    more than a hundred times smaller.

</details>

## Capstone: design a two-qubit gate experiment

Choose an atom (Rb-87 unless you prefer otherwise), a tweezer wavelength and
waist, and a Rydberg state. Using the labs:

1. Find the tweezer power for a 1 mK trap and the trap frequencies (lab 05).
2. Assume the atoms are cooled to 10 $\mu$K; compute $T_2^*$ (lab 09) and the
   Doppler error of the Rydberg gate (lab 11).
3. Choose the atom spacing so that the pair is deep in the blockade regime but
   neighbouring pairs 3 spacings away are not (lab 10).
4. Choose $\Omega$ to minimise the intrinsic error budget (lab 11), then state
   which technical error (laser phase noise, intensity noise, intermediate-state
   scattering) you would expect to dominate and why.

Finish with a one-page table of assumptions, computed numbers and the
additional models you would need before building the experiment.

[Chapter index](README.md) · [Run all numerical checks](../hands-on/README.md)
