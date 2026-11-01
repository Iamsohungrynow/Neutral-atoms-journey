# 03 · A Two-Level Atom in a Laser Field

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

Everything in Part I of this course, from slowing to trapping, comes from one question: what does a laser do to an atom? This chapter answers it for the simplest possible atom, one with only two levels. We derive the coupling, see the atom oscillate between its levels (**Rabi oscillations**), add spontaneous emission to get the **optical Bloch equations**, and solve them for the quantity that drives Chapters 04 to 06: the **photon scattering rate**. The model is not a toy. Chapter 02 showed that Rb-87 driven with $\sigma^+$ light on $|F{=}2,m_F{=}2\rangle\to|F'{=}3,m_F'{=}3\rangle$ really is a closed two-level system.

> **Conventions.** Laser frequency $\omega_L$, atomic frequency $\omega_0$, detuning $\delta=\omega_L-\omega_0$ (red: $\delta<0$). $\Gamma$ is the excited-state decay rate. $\Omega$ is the Rabi frequency, defined so that on resonance the excited population is $\sin^2(\Omega t/2)$. See the [notation page](00-notation.md).

![Two-level atom diagram: ground state g and excited state e; a red double arrow shows the laser at frequency omega L with coupling Omega, ending on a dashed line a distance delta below the excited state; a blue dashed arrow from e to g shows spontaneous emission at rate Gamma. A table lists the Rb-87 D2 cycling-transition numbers: 780.241 nm, Gamma over 2 pi = 6.0666 MHz, lifetime 26.2 ns, dipole 2.99 e a0, saturation intensity 1.669 mW per square centimetre, cross-section 0.291 square micrometres](figures/03-two-level.png)

*The model of this chapter and its three parameters: the coupling $\Omega$, the detuning $\delta$, and the decay rate $\Gamma$. The table gives their scale for Rb-87.*

## The classical picture first

Before any quantum mechanics, think of the electron as a mass on a spring, resonant at $\omega_0$, with a damping rate $\Gamma$, driven by the laser's electric field $E_0\cos\omega_Lt$. Two facts from the driven damped oscillator survive into the quantum treatment:

1. The response is large only within about $\Gamma$ of resonance (a **Lorentzian** line of full width $\Gamma$).
2. Below resonance the electron moves **in phase** with the field; above resonance it moves **out of phase**. This phase decides whether light attracts or repels an atom (Chapter 04).

What the classical oscillator cannot do is **saturate**. A spring can be stretched as far as you like, but a two-level atom can be at most fully excited. That is the new physics below.

## The coupling and the rotating-wave approximation

An atom is much smaller than an optical wavelength (0.5 nm versus 780 nm), so it sees a uniform but oscillating field. The interaction is that of an electric dipole,

$$\hat H_{\rm int}=-\hat{\mathbf d}\cdot\mathbf E_0\cos\omega_Lt .$$

The dipole operator only connects $|g\rangle$ and $|e\rangle$. Define the **Rabi frequency** through its matrix element,

$$\hbar\Omega=-\langle e|\hat{\mathbf d}\cdot\mathbf E_0|g\rangle,$$

taking $\Omega$ real. Write $\cos\omega_Lt=(e^{i\omega_Lt}+e^{-i\omega_Lt})/2$ and look at the coupling in the interaction picture, where the atom's own evolution at $\omega_0$ is removed. The coupling then contains two kinds of term. One oscillates at the small difference $\omega_L-\omega_0=\delta$; the other oscillates at the sum $\omega_L+\omega_0\approx2\pi\times768$ THz. The fast term averages to zero over any time we can resolve. Dropping it is the **rotating-wave approximation (RWA)**, valid when $\Omega,|\delta|\ll\omega_0$. For Rb that means MHz to GHz couplings against a 384 THz transition: an extremely good approximation.

Finally, moving to a frame that rotates at the laser frequency $\omega_L$ makes what remains time independent:

$$\frac{\hat H}{\hbar}=-\delta\,|e\rangle\langle e|+\frac{\Omega}{2}\big(|e\rangle\langle g|+|g\rangle\langle e|\big).$$

> **Intuition aside.** In the rotating frame the laser "stands still". The detuning becomes an energy offset of the excited state ($-\hbar\delta$: if the laser is red-detuned, the excited state sits *above* the laser's reach by $\hbar|\delta|$), and the laser field becomes a static coupling between the levels.

## Rabi oscillations and the Bloch sphere

Any pure state of two levels can be drawn as a point on a unit sphere: ground state at the south pole, excited state at the north pole. With the Pauli matrix $\sigma_z=|e\rangle\langle e|-|g\rangle\langle g|$, the Hamiltonian above is (up to a constant) $\frac{\hbar}{2}(\Omega\sigma_x-\delta\sigma_z)$, a spin in a magnetic field. The Bloch vector has components $u=\langle\sigma_x\rangle=2\,{\rm Re}\,\rho_{eg}$, $v=\langle\sigma_y\rangle=-2\,{\rm Im}\,\rho_{eg}$ and $w=\langle\sigma_z\rangle=\rho_{ee}-\rho_{gg}$. It therefore **precesses** about the axis $(\Omega,0,-\delta)$ at the **generalized Rabi frequency**

$$\Omega'=\sqrt{\Omega^2+\delta^2}.$$

Starting in $|g\rangle$, the excited population is

$$P_e(t)=\frac{\Omega^2}{\Omega'^2}\sin^2\!\Big(\frac{\Omega't}{2}\Big).$$

On resonance the atom is fully inverted after a **$\pi$ pulse** of duration $\pi/\Omega$. Off resonance it oscillates faster but never reaches the north pole.

![Three Bloch spheres. Left: resonant drive with no decay, a great circle through both poles about a horizontal rotation axis. Middle: detuning equal to the Rabi frequency, a tilted small circle that reaches only the equator. Right: resonant drive at three times the linewidth with decay, a spiral that ends at a point inside the sphere](figures/03-bloch.png)

*Bloch-vector trajectories from the optical Bloch equations ($\Omega=2\Gamma$ in the first two panels). Without decay the state circles forever about the rotation axis. With spontaneous emission it spirals into a **steady state** inside the sphere: a statistical mixture, not a pure state.*

## Spontaneous emission and the optical Bloch equations

A real excited state decays. For an electric-dipole transition the rate is

$$\Gamma=\frac{\omega_0^3|d|^2}{3\pi\varepsilon_0\hbar c^3},$$

where $d$ is the transition dipole matrix element. For Rb-87 D2, $\Gamma=2\pi\times6.0666$ MHz $=3.81\times10^7\ {\rm s^{-1}}$, a lifetime of 26.2 ns, and inverting the formula gives $|d|=2.99\,ea_0$ for the cycling transition.

Decay turns pure states into mixtures, so we describe the atom by a density matrix $\rho$ and add damping. Taking matrix elements of the master equation gives the **optical Bloch equations**:

$$\dot\rho_{ee}=-\Gamma\rho_{ee}+\Omega\,{\rm Im}\,\rho_{ge},$$

$$\dot\rho_{eg}=\Big(i\delta-\frac{\Gamma}{2}\Big)\rho_{eg}-\frac{i\Omega}{2}\big(\rho_{gg}-\rho_{ee}\big),$$

with $\rho_{gg}=1-\rho_{ee}$ and $\rho_{ge}=\rho_{eg}^*$. Populations decay at $\Gamma$; coherences decay at $\Gamma/2$.

### The steady state

After a few lifetimes the atom forgets its initial state. Setting the time derivatives to zero: the second equation gives $\rho_{eg}=\dfrac{i\Omega(\rho_{gg}-\rho_{ee})/2}{i\delta-\Gamma/2}$. Substituting into the first and solving for $\rho_{ee}$,

$$\boxed{\ \rho_{ee}=\frac{s_0/2}{1+s_0+(2\delta/\Gamma)^2},\qquad s_0=\frac{2\Omega^2}{\Gamma^2}=\frac{I}{I_{\rm sat}}\ }$$

The photons the atom scatters per second equal $\Gamma\rho_{ee}$:

$$\gamma_p=\frac{\Gamma}{2}\,\frac{s_0}{1+s_0+(2\delta/\Gamma)^2}.$$

This one formula is the engine of laser cooling. Read off its properties:

- **Low intensity** ($s_0\ll1$): a Lorentzian in $\delta$ with full width $\Gamma$, and $\gamma_p\propto I$.
- **Saturation**: $\gamma_p\to\Gamma/2$ as $s_0\to\infty$, at any detuning (far from resonance it just takes more intensity). At most half the atoms are excited, because stimulated emission balances absorption.
- **Power broadening**: the full width at half maximum is $\Gamma\sqrt{1+s_0}$.

### Saturation intensity and cross-section

With $I=\tfrac12c\varepsilon_0E_0^2$ and $\Omega=dE_0/\hbar$, the condition $s_0=1$ fixes $I_{\rm sat}=c\varepsilon_0\hbar^2\Gamma^2/(4d^2)$. Eliminating $d$ with the decay-rate formula,

$$I_{\rm sat}=\frac{\pi hc\,\Gamma}{3\lambda^3}=1.669\ \mathrm{mW/cm^2}\quad\text{(Rb-87 cycling transition)}.$$

At low intensity, the scattered power $\hbar\omega\gamma_p$ divided by the incident intensity is the resonant **cross-section** $\sigma_0=\hbar\omega\Gamma/(2I_{\rm sat})=3\lambda^2/2\pi=0.291\ \mu{\rm m}^2$: an atom a fraction of a nanometre across blocks light as if it were a disc about 0.6 $\mu$m in diameter.

![Left: log-log plot of scattering rate versus saturation parameter for detunings 0, minus half a linewidth and minus two linewidths; each curve rises linearly and flattens at Gamma over 2, 1.9 times ten to the seven photons per second. Right: full width at half maximum in units of Gamma, rising as the square root of one plus s0, with points marked at 8.6 MHz for s0 = 1, 20.1 MHz for s0 = 10 and 61.0 MHz for s0 = 100](figures/03-saturation.png)

*Saturation (left) and power broadening (right) for Rb-87 D2. Detuned light needs more intensity to saturate: the curve for $\delta=-2\Gamma$ reaches half of $\Gamma/2$ only at $s_0=1+(2\delta/\Gamma)^2=17$.*

## Doppler broadening: why cold atoms see a sharp line

The line shape above is for an atom at rest. An atom moving with velocity $v$ along the beam sees the laser Doppler-shifted by $kv$, so a gas with a spread of velocities absorbs over a spread of frequencies. For a thermal (Maxwell-Boltzmann) gas the velocity along the beam is Gaussian with rms value $\sigma_v=\sqrt{k_BT/m}$, which gives a Gaussian **Doppler profile** with rms width $k\sigma_v$, or $\sigma_v/\lambda$ in ordinary frequency units, and full width at half maximum $2\sqrt{2\ln2}\,\sigma_v/\lambda$:

| Rb-87 on the D2 line | $\sigma_v$ | Doppler FWHM | compared with $\Gamma/2\pi=6.07$ MHz |
|---|---|---|---|
| room-temperature vapour, 300 K | 169 m/s | **511 MHz** | 84 times wider: the hyperfine lines of Chapter 02 blur together |
| laser-cooled cloud, 100 $\mu$K | 9.8 cm/s | **0.30 MHz** | 20 times narrower: the natural line dominates |

This is why lasers are locked using **Doppler-free** techniques such as saturated-absorption spectroscopy in a vapour cell, and why cold atoms are such clean spectroscopic samples. The same physics returns twice later in the course: the Doppler shift is what makes laser *cooling* possible (Chapter 05), and the residual Doppler shift of a few-microkelvin atom is an error source for Rydberg gates (Chapter 11). Finite interaction time (transit-time broadening) and collisions also broaden lines, but they are small for atoms held in tweezers.

## Beyond two levels: three-level atoms

Several tools in later chapters use three levels: Raman transitions between the two qubit states (Chapter 09), two-photon excitation of Rydberg states (Chapter 10), and the dark states behind gray molasses (Chapter 06). Three ideas cover them all.

**1. Adiabatic elimination: two photons act like one.** Take levels $|a\rangle$, $|e\rangle$, $|b\rangle$, with a laser of Rabi frequency $\Omega_1$ on $|a\rangle\leftrightarrow|e\rangle$ and a second, $\Omega_2$, on $|e\rangle\leftrightarrow|b\rangle$, both detuned by the same large $\Delta$ from $|e\rangle$ so that the two-photon transition $|a\rangle\leftrightarrow|b\rangle$ is resonant. If $|\Delta|\gg\Omega_1,\Omega_2,\Gamma_e$, the intermediate state is barely populated (probability about $\Omega_1^2/4\Delta^2$) and can be eliminated. What remains is an effective two-level system with

$$\Omega_{\rm eff}=\frac{\Omega_1\Omega_2}{2\Delta},$$

plus a light shift of each level by $\Omega_i^2/4\Delta$ (the Chapter 04 formula, one laser at a time). The *difference* of the two light shifts moves the two-photon resonance and must be compensated. The small intermediate-state population still scatters photons at a rate of about $\Gamma_e\Omega_1^2/4\Delta^2$, which is the price of the scheme (Chapters 09 and 11 work out the numbers).

**2. Dark states.** In a $\Lambda$ system ($|a\rangle$ and $|b\rangle$ both below $|e\rangle$) on two-photon resonance, the superposition

$$|D\rangle\propto\Omega_2|a\rangle-\Omega_1|b\rangle$$

is not coupled to $|e\rangle$ at all: the two excitation amplitudes cancel. An atom in $|D\rangle$ never absorbs, never scatters, and stays there. This **coherent population trapping** makes a medium transparent at the two-photon resonance (electromagnetically induced transparency) and underlies gray molasses (Chapter 06). Slowly changing the ratio $\Omega_1/\Omega_2$ moves the dark state: applying $\Omega_2$ first and then $\Omega_1$ (the "counter-intuitive" order) carries an atom from $|a\rangle$ to $|b\rangle$ without ever populating $|e\rangle$. This is STIRAP (stimulated Raman adiabatic passage).

**3. Adiabatic passage and Landau-Zener.** Sweep the detuning of a two-level system through resonance, $\delta(t)=\alpha t$, with a constant coupling $\Omega$. Far from resonance the eigenstates are $|g\rangle$ and $|e\rangle$; at resonance they mix; on the other side they have swapped. If the sweep is slow, the atom follows its eigenstate and ends up transferred; if it is fast, it stays behind. The probability of being left behind is the **Landau-Zener** formula,

$$P_{\rm diabatic}=\exp\!\Big(-\frac{\pi\Omega^2}{2\alpha}\Big),$$

so the sweep must be slow compared with $\Omega^2$, the square of the minimum gap. Adiabatic transfer is robust against small errors in pulse area and detuning, which is why it is used for state transfer and, in many-body form, to prepare ordered phases of Rydberg arrays (Chapter 10 and lab 13). For example, $\Omega/2\pi=2$ MHz swept over 14 MHz in 2 $\mu$s gives $\alpha=2\pi\times7$ MHz/$\mu$s and $P_{\rm diabatic}=e^{-\pi(2\pi\times2)^2/(2\cdot2\pi\times7)}=e^{-5.6}\approx4\times10^{-3}$.

## Worked example (Rb-87 D2, illustrative numbers)

| Symbol | Meaning | Value |
|---|---|---|
| $I$ | laser intensity | 1.0 mW/cm$^2$ |
| $s_0=I/I_{\rm sat}$ | saturation parameter | **0.599** (computed) |
| $\Omega/2\pi=(\Gamma/2\pi)\sqrt{s_0/2}$ | Rabi frequency | **3.32 MHz** (computed) |
| $\gamma_p(\delta=0)$ | scattering rate on resonance | **$7.1\times10^6$ s$^{-1}$** (computed) |
| $\gamma_p(\delta=-\Gamma/2)$ | at the Doppler-cooling detuning | **$4.4\times10^6$ s$^{-1}$** (computed) |
| $\Gamma\sqrt{1+s_0}/2\pi$ at $s_0=10$ | power-broadened width | **20.1 MHz** (computed) |

**Step 1: saturation.** $s_0=1.0/1.669=0.599$.

**Step 2: Rabi frequency.** $\Omega=\Gamma\sqrt{s_0/2}=\Gamma\times0.547$, so $\Omega/2\pi=3.32$ MHz. Check from the field: $E_0=\sqrt{2I/(c\varepsilon_0)}=86.8$ V/m and $\Omega=dE_0/\hbar=2\pi\times3.32$ MHz with $d=2.99\,ea_0$. Both routes agree.

**Step 3: scattering on resonance.** $\gamma_p=(\Gamma/2)\,s_0/(1+s_0)=1.906\times10^7\times0.599/1.599=7.1\times10^6\ {\rm s^{-1}}$.

**Step 4: detuned by half a linewidth.** $(2\delta/\Gamma)^2=1$, so $\gamma_p=1.906\times10^7\times0.599/2.599=4.4\times10^6\ {\rm s^{-1}}$.

**Step 5: can we see coherent Rabi oscillations?** Only if they are faster than decay. Here $\Omega/\Gamma=0.55$, so the excited population is damped before it completes a cycle (lab 01 shows this case). Coherent control of an optical transition needs $\Omega\gg\Gamma$ or, much better, a long-lived excited state; that is why qubits are stored in ground hyperfine levels (Chapter 09) and why Rydberg states, with lifetimes of hundreds of microseconds, are used for gates (Chapter 10).

## Run it

[Lab 01](../hands-on/01-optical-bloch/) solves the optical Bloch equations with QuTiP, shows the damped Rabi oscillations, and checks the steady state, the saturation and the power-broadened width against the formulas above.

## Common pitfalls

- **$\Omega$ versus $\Omega/2$.** Some texts call $\Omega/2$ the Rabi frequency or write the coupling as $\hbar\Omega$ rather than $\hbar\Omega/2$. Then $s_0=2\Omega^2/\Gamma^2$ changes form. Fix a convention (ours: $P_e=\sin^2(\Omega t/2)$) and stay with it.
- **"Saturation intensity is a property of the atom."** It also depends on polarization and on which sublevels are involved. 1.669 mW/cm$^2$ is for the $\sigma^+$ cycling transition; for other polarizations the effective dipole is smaller and $I_{\rm sat}$ larger (Steck lists 3.58 mW/cm$^2$ for isotropic light).
- **"More intensity always means more scattering."** Above $s_0\approx1$ the rate barely grows; you only broaden the line.
- **"The steady state is reached instantly."** It takes several lifetimes ($\sim5/\Gamma\approx130$ ns for Rb). For pulses shorter than that, solve the time-dependent equations.
- **Angular versus ordinary frequency.** $\Gamma=3.81\times10^7\ {\rm s^{-1}}$ and $\Gamma/2\pi=6.07$ MHz are the same thing. Mixing them introduces errors of $2\pi$.

## Key takeaways

- In the rotating-wave approximation, a laser-driven two-level atom is a spin precessing about $(\Omega,0,-\delta)$ at $\Omega'=\sqrt{\Omega^2+\delta^2}$.
- Spontaneous emission damps populations at $\Gamma$ and coherences at $\Gamma/2$; the optical Bloch equations describe both.
- The steady-state scattering rate $\gamma_p=\frac{\Gamma}{2}\frac{s_0}{1+s_0+(2\delta/\Gamma)^2}$ saturates at $\Gamma/2$ and is power-broadened to width $\Gamma\sqrt{1+s_0}$.
- For Rb-87 D2: $\Gamma/2\pi=6.07$ MHz, $I_{\rm sat}=1.669$ mW/cm$^2$, maximum scattering rate $1.9\times10^7$ photons per second.
- Thermal motion Doppler-broadens a line (511 MHz FWHM for Rb vapour at 300 K, 0.3 MHz at 100 $\mu$K).
- Two detuned lasers act like one with $\Omega_{\rm eff}=\Omega_1\Omega_2/2\Delta$; $\Lambda$ systems have dark states; slow sweeps transfer population adiabatically (Landau-Zener).
- Each scattered photon delivers a momentum kick; Chapter 04 turns this rate into a force.

## Go deeper

- H. J. Metcalf and P. van der Straten, *Laser cooling and trapping of atoms*, J. Opt. Soc. Am. B 20, 887 (2003), [Utrecht preprint](https://webspace.science.uu.nl/~strat102/preprint/handpubl.pdf). Its introduction to optical forces starts from this scattering rate, in closely related notation ($\delta$, $s_0$, $\gamma_p$; the review writes $\gamma$ for the linewidth that this course calls $\Gamma$).
- C. J. Foot, *Atomic Physics* (Oxford University Press, 2005), chapter 7. A careful derivation of the optical Bloch equations and the steady state.
- D. A. Steck, *Rubidium 87 D Line Data*, [steck.us/alkalidata](https://steck.us/alkalidata). Dipole matrix elements and saturation intensities for every polarization.
- H. J. Metcalf and P. van der Straten, *Laser Cooling and Trapping* (Springer, 1999), chapters 2 and 3. The book-length version of the review, with the density-matrix derivation in full.

---

← Previous: [The Atom: Levels, Fine and Hyperfine Structure](02-atomic-structure.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [Optical Forces: Radiation Pressure and the Dipole Force](04-optical-forces.md) →
