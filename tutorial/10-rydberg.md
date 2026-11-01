# 10 · Rydberg Atoms and the Blockade

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

Everything so far has been about isolated atoms. Ground-state atoms a few micrometres apart are, for every practical purpose, non-interacting, which is wonderful for storing qubits and useless for entangling them. This chapter introduces the way neutral atoms are made to talk: excite one electron to a very high principal quantum number $n$ (a **Rydberg state**), where the atom becomes enormous, extremely polarizable and strongly interacting. Two Rydberg atoms 5 $\mu$m apart shift each other's energy by tens of MHz, enough that a laser can excite one of them but not both. That **Rydberg blockade** is the basis of the entangling gates in Chapter 11 and of analog quantum simulation. The theory follows Saffman, Walker and Mølmer's review and Browaeys and Lahaye's; the numbers come from the ARC library.

## Rydberg atoms

A Rydberg atom is the alkali atom of Chapter 02 with its valence electron promoted to large $n$, typically 50 to 100. The quantum-defect formula still holds,

$$E_{n\ell}=-\frac{\mathrm{Ry}}{(n-\delta_\ell)^2}=-\frac{\mathrm{Ry}}{n^{*2}},$$

with $\delta_0=3.131$ for Rb $nS$ states, so $70S_{1/2}$ has $n^*=66.87$. Almost every property is a power of $n^*$, because the electron's orbit grows as $n^{*2}$ and its speed falls as $1/n^*$:

| Property | Scaling | Rb $70S_{1/2}$ (ARC) |
|---|---|---|
| binding energy | $n^{*-2}$ | 3.04 meV $=h\times736$ GHz |
| spacing to neighbouring $n$ | $n^{*-3}$ | $\approx h\times22$ GHz |
| orbit radius $\langle r\rangle\approx\frac32n^{*2}a_0$ | $n^{*2}$ | 355 nm |
| dipole moment to neighbouring states | $n^{*2}$ | thousands of $ea_0$ |
| radiative lifetime (low $\ell$) | $n^{*3}$ | 374 $\mu$s at 0 K |
| blackbody-limited lifetime | $n^{*2}$ | 147 $\mu$s total at 300 K |
| static polarizability | $n^{*7}$ | $\approx520$ MHz/(V/cm)$^2$ |
| van der Waals coefficient $C_6$ | $n^{*11}$ | $h\times863$ GHz $\mu$m$^6$ |

Three entries matter most. **Lifetimes** of hundreds of microseconds are long compared with MHz-scale laser couplings, so a Rydberg state can be coherently driven. **Room-temperature blackbody radiation** (thermal photons at THz frequencies, resonant with transitions between neighbouring Rydberg levels) shortens the lifetime by more than a factor of two at $n=70$; cryogenic environments help. The **polarizability** grows as $n^{*7}$, so Rydberg atoms are very sensitive to stray electric fields: a field of only 10 mV/cm shifts $70S$ by tens of kHz. Experiments use electrodes to null stray fields and avoid charging their glass cells.

![Left: two-photon excitation ladder of Rb-87 from the 5S1/2 qubit state through the 6P3/2 intermediate state to the 70S1/2 Rydberg state, with a 420 nm laser of Rabi frequency Omega 1, a 1013 nm laser of Rabi frequency Omega 2, an intermediate detuning Delta i of order GHz, and an effective Rabi frequency Omega 1 Omega 2 over 2 Delta i of a few MHz. Right: a circle of radius 355 nm representing the size of a 70S Rydberg atom; a ground-state atom of radius 0.25 nm would be invisible at this scale](figures/10-excitation.png)

*How Rb-87 is excited to $70S$: two lasers, detuned from the short-lived intermediate state so that it is barely populated, act like a single laser with Rabi frequency $\Omega=\Omega_1\Omega_2/2\Delta_i$. The excited atom is about a thousand times larger than in its ground state.*

### Exciting a Rydberg state

A single photon cannot drive $5S\to70S$ at all ($\Delta\ell=0$ is dipole-forbidden); one ultraviolet photon near 297 nm reaches the $nP$ Rydberg states instead. Most Rb experiments use **two photons**, which reach $nS$ (and $nD$) states: 420 nm to $6P_{3/2}$ and 1013 nm onward to $70S$ (or 780 nm and 480 nm via $5P_{3/2}$). Detuning both by $\Delta_i$ from the intermediate state, the scheme behaves like the Raman transition of Chapter 09 with an effective Rabi frequency $\Omega=\Omega_1\Omega_2/2\Delta_i$, typically a few MHz. The intermediate state still scatters a little light; Chapter 11 includes that in the error budget. Alkaline-earth atoms such as strontium can be excited with a **single** UV photon from a long-lived metastable state, which avoids the intermediate state altogether.

Because the two beams are usually counter-propagating, the Doppler shift is set by the difference of their wavevectors, $k_{\rm eff}=2\pi(1/420.3\ {\rm nm}-1/1012.8\ {\rm nm})=8.75\times10^6\ {\rm m^{-1}}$. An atom at $10\ \mu$K (rms velocity 3.1 cm/s) sees a random detuning with an rms value of $k_{\rm eff}\sigma_v/2\pi=43$ kHz, which matters for gates (Chapter 11).

## Interactions between Rydberg atoms

Two atoms in $|r\rangle=|nS\rangle$ at distance $R$ interact through their electric dipoles. A single $nS$ state has no permanent dipole, so the interaction appears in **second order**: the pair state $|nS,nS\rangle$ is coupled by the dipole-dipole operator $\propto1/R^3$ to nearby pair states such as $|nP,(n-1)P\rangle$, which differ in energy by a small **Förster defect** $\Delta_F$. Second-order perturbation theory gives

$$V(R)=-\frac{|C_3|^2}{\Delta_F R^6}\equiv\frac{C_6}{R^6},$$

the **van der Waals** interaction. Its strength scales as $C_3^2/\Delta_F\propto(n^{*4})^2/n^{*-3}=n^{*11}$, which explains the enormous growth with $n$. For Rb $nS$ pairs $C_6>0$ (repulsive); for $70S$, $C_6/h=863$ GHz $\mu$m$^6$. At short distances, where $C_3/R^3$ becomes comparable with $\Delta_F$, perturbation theory fails and the interaction crosses over to the resonant dipole-dipole form $\propto1/R^3$.

How strong is it? At $R=5\ \mu$m,

$$\frac{V}{h}=\frac{863\times10^3\ {\rm MHz}\,\mu{\rm m}^6}{5^6\ \mu{\rm m}^6}=55\ {\rm MHz},$$

while two ground-state Rb atoms at the same distance interact by many orders of magnitude less than a hertz. Switching the interaction on and off by exciting and de-exciting $|r\rangle$ is the neutral-atom version of a tunable coupler.

## The Rydberg blockade

Drive two atoms resonantly from $|g\rangle$ to $|r\rangle$ with the same Rabi frequency $\Omega$. With $n_i=|r\rangle\langle r|_i$, the Hamiltonian is

$$\frac{H}{\hbar}=\frac{\Omega}{2}\big(\sigma^x_1+\sigma^x_2\big)+\frac{V(R)}{\hbar}\,n_1n_2 .$$

- If the atoms are **far apart** ($V\ll\hbar\Omega$), each Rabi-flops independently and the probability of finding both excited is $\sin^4(\Omega t/2)$.
- If they are **close** ($V\gg\hbar\Omega$), the doubly excited state $|rr\rangle$ is shifted out of resonance. Starting from $|gg\rangle$, the laser can only reach the symmetric singly excited state $|W\rangle=(|gr\rangle+|rg\rangle)/\sqrt2$. The matrix element $\langle W|H|gg\rangle=\sqrt2\,\hbar\Omega/2$, so the pair oscillates between $|gg\rangle$ and an **entangled** state at the enhanced frequency $\sqrt2\,\Omega$.

![Left: level diagram of two atoms; the ground state gg couples to the symmetric singly excited state W with matrix element root 2 Omega, while the doubly excited state rr is shifted up by V and is no longer resonant with the laser. Right: van der Waals interaction energy of two 70S atoms versus distance on a log scale, crossing the 2 MHz line of h-bar Omega at the blockade radius of 8.7 micrometres; at 5 micrometres it is 55 MHz. The region inside the blockade radius is shaded](figures/10-blockade.png)

*The blockade. Inside the blockade radius, $V\gg\hbar\Omega$ and at most one atom is excited; outside it, the atoms behave independently.*

The crossover defines the **blockade radius**

$$R_b=\Big(\frac{C_6}{\hbar\Omega}\Big)^{1/6},$$

which is $(863\ {\rm GHz}/2\ {\rm MHz})^{1/6}\ \mu{\rm m}=8.7\ \mu$m for $70S$ at $\Omega/2\pi=2$ MHz. Because of the sixth root, $R_b$ is forgiving: changing $\Omega$ by a factor of 2 changes $R_b$ by only 12%.

The blockade is not perfect. The doubly excited state is still weakly coupled, off resonance by $V$, so its population is of order $(\hbar\Omega/V)^2$: about $\frac12(2/55)^2\approx7\times10^{-4}$ at 5 $\mu$m. Lab 10 confirms that halving $V$ multiplies the residual double excitation by 4.

**Many atoms.** If $N$ atoms all lie within one blockade radius, only one excitation can be shared among them, and the ground state couples to the symmetric state $\frac1{\sqrt N}\sum_i|g\cdots r_i\cdots g\rangle$ with matrix element $\sqrt N\,\hbar\Omega/2$: a **collective Rabi frequency** $\sqrt N\,\Omega$. Observing the $\sqrt2$ enhancement for two atoms in separate tweezers was the first direct demonstration of the blockade between individual atoms (Gaëtan et al.; Urban et al., 2009).

> **Intuition aside.** The blockade is a quantum "one at a time" rule enforced by energy conservation. The laser supplies exactly enough energy to excite one atom. Exciting the second would cost an extra $V$ that the laser photon does not carry, so it simply does not happen, and quantum mechanics keeps both possibilities (which atom was excited) in superposition: that is the entanglement.

## From blockade to quantum simulation

Let many atoms in an array evolve under the same laser, now with a detuning $\Delta$:

$$\frac{H}{\hbar}=\sum_i\frac{\Omega}{2}\sigma^x_i-\Delta\sum_in_i+\sum_{i<j}\frac{V_{ij}}{\hbar}n_in_j .$$

This is an Ising-type spin model in a transverse field, with the "spin up" state being the Rydberg state. When the nearest neighbours are blockaded and farther atoms are not, sweeping $\Delta$ from negative to positive drives the array into ordered phases, for example a chain in which every other atom is excited. Programmable arrays of tens to hundreds of atoms have used this Hamiltonian to study quantum phase transitions and many-body dynamics (Bernien et al., 2017; Ebadi et al., 2021; Scholl et al., 2021). This "analog" mode uses the ground-Rydberg qubit directly, without the hyperfine qubit of Chapter 09.

## Worked example (Rb-87, 70S, illustrative numbers)

| Quantity | Formula | Value |
|---|---|---|
| effective quantum number | $70-3.131$ | 66.87 |
| orbit radius | $\frac32n^{*2}a_0$ | **355 nm** |
| lifetime at 300 K | ARC | **147 $\mu$s** |
| $C_6/h$ | ARC | 863 GHz $\mu$m$^6$ |
| interaction at 5 $\mu$m | $C_6/R^6$ | **55 MHz** |
| blockade radius at $\Omega/2\pi=2$ MHz | $(C_6/\hbar\Omega)^{1/6}$ | **8.7 $\mu$m** |
| residual double excitation at 5 $\mu$m | $\sim\frac12(\hbar\Omega/V)^2$ | **$7\times10^{-4}$** |
| time-to-entangle ($\pi$ pulse at $\sqrt2\Omega$) | $\pi/(\sqrt2\Omega)$ | **177 ns** |
| decay during it | $t/\tau$ | **$\approx1.2\times10^{-3}$** |

**Step 1: size.** $\frac32\times66.87^2\times0.0529\ {\rm nm}=355$ nm, about a third of a tweezer waist.

**Step 2: interaction and blockade.** $V/h=55$ MHz at 5 $\mu$m is 28 times $\Omega/2\pi=2$ MHz: deep in the blockade regime. At 10 $\mu$m it falls to 0.86 MHz, less than $\Omega$: no blockade. The array spacing must sit well inside $R_b=8.7\ \mu$m for the atoms that should interact, and well outside it for those that should not.

**Step 3: speed versus lifetime.** Starting from $|gg\rangle$, a pulse of length $\pi/(\sqrt2\Omega)=1/(2\sqrt2\times2\ {\rm MHz})=177$ ns creates $|W\rangle$. The pair spends on average about half of that time with one atom in $|r\rangle$, so the probability of a decay is roughly $0.5\times177\ {\rm ns}/147\ \mu{\rm s}\approx6\times10^{-4}$ (the table's $t/\tau$ is the pessimistic upper bound). Lifetime limits on gate fidelity are therefore at the $10^{-3}$ level; Chapter 11 does this budget properly.

## Run it

[Lab 10](../hands-on/10-rydberg-blockade/) simulates two atoms as a function of distance, extracts the $\sqrt2$ enhancement and the $(\Omega/V)^2$ residual double excitation, checks the collective $\sqrt N$ Rabi frequency for up to four atoms, and fits the Rydberg scaling laws to ARC data.

## Common pitfalls

- **"Blockade means the interaction is infinite."** The leakage into $|rr\rangle$ is of order $(\hbar\Omega/V)^2$; it is a gate error and a source of unwanted entanglement with distant atoms.
- **Mixing up $C_6$ conventions.** ARC prints $C_6$ with the opposite sign to the convention used here; some papers quote $C_6$ in units of $h$, others in angular units ($2\pi\times$GHz $\mu$m$^6$). Always check the sign and the factor of $2\pi$.
- **"Higher $n$ is always better."** $C_6$ grows as $n^{*11}$ and lifetimes as $n^{*3}$, but so do electric-field sensitivity ($n^{*7}$), blackbody transfer to neighbouring states and the difficulty of exciting the state (the coupling falls as $n^{*-3/2}$). Most experiments settle on $n\approx50$ to 80.
- **Forgetting the Doppler effect.** With counter-propagating 420 nm and 1013 nm beams, a 10 $\mu$K atom has a 43 kHz rms Doppler detuning; that limits ground-Rydberg coherence to microseconds.
- **"The ground-Rydberg qubit is a good memory."** With a lifetime of $\sim100\ \mu$s and laser-phase sensitivity it is not; information is stored in hyperfine states and only briefly mapped to $|r\rangle$ during gates.

## Key takeaways

- Rydberg atoms have $n\approx50$ to 100; their properties scale as powers of $n^*$: radius $n^{*2}$, lifetime $n^{*3}$, polarizability $n^{*7}$, $C_6$ $n^{*11}$.
- Two $70S$ Rb atoms interact with $C_6/h=863$ GHz $\mu$m$^6$: 55 MHz at 5 $\mu$m.
- When $V\gg\hbar\Omega$, double excitation is blocked; two atoms oscillate between $|gg\rangle$ and the entangled $|W\rangle$ at $\sqrt2\Omega$, and $N$ atoms at $\sqrt N\Omega$.
- The blockade radius $R_b=(C_6/\hbar\Omega)^{1/6}$ is 8.7 $\mu$m at $\Omega/2\pi=2$ MHz.
- The same Hamiltonian, run with a detuning sweep across an array, is a programmable quantum simulator of Ising-type models.

## Go deeper

- M. Saffman, T. G. Walker, K. Mølmer, *Quantum information with Rydberg atoms*, Rev. Mod. Phys. 82, 2313 (2010), [arXiv:0909.4777](https://arxiv.org/abs/0909.4777). The standard review: scaling laws, interactions, blockade and gate proposals.
- A. Browaeys and T. Lahaye, *Many-body physics with individually controlled Rydberg atoms*, Nat. Phys. 16, 132 (2020), [arXiv:2002.07413](https://arxiv.org/abs/2002.07413). The quantum-simulation side, very readable.
- N. Šibalić, J. D. Pritchard, C. S. Adams, K. J. Weatherill, *ARC: An open-source library for calculating properties of alkali Rydberg atoms*, Comput. Phys. Commun. 220, 319 (2017), [arXiv:1612.05529](https://arxiv.org/abs/1612.05529). The library behind every Rydberg number in this chapter.
- A. Gaëtan et al., *Observation of collective excitation of two individual atoms in the Rydberg blockade regime*, Nat. Phys. 5, 115 (2009), [arXiv:0810.2960](https://arxiv.org/abs/0810.2960); E. Urban et al., *Observation of Rydberg blockade between two atoms*, Nat. Phys. 5, 110 (2009), [arXiv:0805.0758](https://arxiv.org/abs/0805.0758).
- T. F. Gallagher, *Rydberg Atoms* (Cambridge University Press, 1994). The classic monograph on Rydberg physics.

---

← Back to [project README](../README.md) · [Tutorial index](./README.md)
