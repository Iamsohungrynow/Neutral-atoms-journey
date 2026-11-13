# 10 · Rydberg Atoms and the Blockade

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

Up to now every atom has been on its own. Two ground-state atoms a few micrometres apart interact so weakly that we can ignore it, which suits a qubit memory but gives us no way to entangle them. The standard fix is to excite one electron to a very high principal quantum number $n$ (a **Rydberg state**). The atom then becomes huge and very easy to polarize, and two Rydberg atoms 5 $\mu$m apart shift each other's energy by tens of MHz. A laser tuned to excite one of them then cannot excite both. This **Rydberg blockade** underlies the entangling gates of Chapter 11 and analog quantum simulation. The theory follows Saffman, Walker and Mølmer's review and Browaeys and Lahaye's; the numbers come from the ARC library.

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
| blackbody-limited lifetime | $n^{*2}$ | 240 $\mu$s from blackbody alone; 146 $\mu$s total at 300 K |
| static polarizability | $n^{*7}$ | $\approx520$ MHz/(V/cm)$^2$ (shift $=-\frac12\alpha F^2$) |
| van der Waals coefficient $C_6$ | $n^{*11}$ | $h\times863$ GHz $\mu$m$^6$ |

For what follows, the lifetimes and the polarizability matter most. Lifetimes of hundreds of microseconds are long compared with MHz-scale laser couplings, so a Rydberg state can be driven coherently. At room temperature, thermal photons at THz frequencies drive transitions to neighbouring Rydberg levels and cut the $70S$ lifetime to less than half its 0 K value, one reason some groups move to cryogenic set-ups. The $n^{*7}$ polarizability makes Rydberg atoms very sensitive to stray electric fields; 10 mV/cm already shifts $70S$ by tens of kHz. Experiments therefore null stray fields with electrodes and try to keep their glass cells from charging up.

![Left: two-photon excitation ladder of Rb-87 from the 5S1/2 qubit state through the 6P3/2 intermediate state to the 70S1/2 Rydberg state, with a 420 nm laser of Rabi frequency Omega 1, a 1013 nm laser of Rabi frequency Omega 2, an intermediate detuning Delta i of order GHz, and an effective Rabi frequency Omega 1 Omega 2 over 2 Delta i of a few MHz. Right: a circle of radius 355 nm representing the size of a 70S Rydberg atom; a ground-state atom of radius 0.25 nm would be invisible at this scale](figures/10-excitation.png)

*How Rb-87 is excited to $70S$: two lasers, detuned from the short-lived intermediate state so that it is barely populated, act like a single laser with Rabi frequency $\Omega=\Omega_1\Omega_2/2\Delta_i$. The excited atom is about a thousand times larger than in its ground state.*

### Exciting a Rydberg state

A single photon cannot drive $5S\to70S$ at all ($\Delta\ell=0$ is dipole-forbidden); one ultraviolet photon near 297 nm reaches the $nP$ Rydberg states instead. Most Rb experiments use **two photons**, which reach $nS$ (and $nD$) states: 420 nm to $6P_{3/2}$ and 1013 nm onward to $70S$ (or 780 nm and 480 nm via $5P_{3/2}$). Define each one-photon detuning as laser frequency minus its own atomic transition frequency. Then $\delta_{420}=\Delta_i$ and, on bare two-photon resonance, $\delta_{1013}=-\Delta_i$: the detunings have opposite signs in this absorption ladder. Their sum sets the bare two-photon detuning and must be adjusted to compensate differential light shifts. Eliminating the intermediate state gives an effective Rabi-frequency magnitude $|\Omega|=|\Omega_1\Omega_2/(2\Delta_i)|$, typically a few MHz. The intermediate state still scatters a little light; Chapter 11 includes that in the error budget. Alkaline-earth atoms such as strontium can be excited with a **single** UV photon from a long-lived metastable state, which avoids the intermediate state altogether.

Because the two beams are usually counter-propagating, the Doppler shift is set by the difference of their wavevectors, $k_{\rm eff}=2\pi(1/420.3\ {\rm nm}-1/1012.8\ {\rm nm})=8.75\times10^6\ {\rm m^{-1}}$. An atom at $10\ \mu$K (one-dimensional rms velocity along $k_{\rm eff}$, $\sigma_v=\sqrt{k_BT/m}=3.1$ cm/s) sees a random detuning with an rms value of $k_{\rm eff}\sigma_v/2\pi=43$ kHz, which limits ground-Rydberg coherence to $T_2^*=\sqrt2/(k_{\rm eff}\sigma_v)\approx5\ \mu$s and matters for gates (Chapter 11).

## Interactions between Rydberg atoms

Two atoms in $|r\rangle=|nS\rangle$ at distance $R$ interact through their electric dipoles. A single $nS$ state has no permanent dipole, so the interaction appears in **second order**: the pair state $|nS,nS\rangle$ is coupled by the dipole-dipole operator $\propto1/R^3$ to nearby pair states such as $|nP,(n-1)P\rangle$, which differ in energy by a small **Förster defect** $\Delta_F=E_{\rm pair'}-E_{nS,nS}$. Second-order perturbation theory gives

$$V(R)=-\frac{|C_3|^2}{\Delta_F R^6}\equiv\frac{C_6}{R^6},$$

the **van der Waals** interaction. Its strength scales as $C_3^2/\Delta_F\propto(n^{*4})^2/n^{*-3}=n^{*11}$, which explains the enormous growth with $n$. For Rb $nS$ pairs the nearby pair states lie *below* $|nS,nS\rangle$ ($\Delta_F<0$; for $70S$ the closest, $|70P_{3/2},69P_{3/2}\rangle$, is about 0.7 GHz below), so $C_6>0$ (repulsive); for $70S$, $C_6/h=863$ GHz $\mu$m$^6$. At short distances, where $C_3/R^3$ becomes comparable with $|\Delta_F|$ (below roughly 3 to 4 $\mu$m for $70S$), perturbation theory fails and the interaction crosses over to the resonant dipole-dipole form $\propto1/R^3$; $C_6/R^6$ values quoted at 4 $\mu$m are therefore asymptotic estimates, about 10% too large.

How strong is it? At $R=5\ \mu$m,

$$\frac{V}{h}=\frac{863\times10^3\ {\rm MHz}\,\mu{\rm m}^6}{5^6\ \mu{\rm m}^6}=55\ {\rm MHz},$$

while two ground-state Rb atoms at the same distance interact by many orders of magnitude less than a hertz. Switching the interaction on and off by exciting and de-exciting $|r\rangle$ is the neutral-atom version of a tunable coupler.

## The Rydberg blockade

Drive two atoms resonantly from $|g\rangle$ to $|r\rangle$ with the same Rabi frequency $\Omega$. With $n_i=|r\rangle\langle r|_i$, the Hamiltonian is

$$\frac{H}{\hbar}=\frac{\Omega}{2}\big(\sigma^x_1+\sigma^x_2\big)+\frac{V(R)}{\hbar}\,n_1n_2 .$$

- If the atoms are **far apart** ($V\ll\hbar\Omega$), each Rabi-flops independently and the probability of finding both excited is $\sin^4(\Omega t/2)$.
- If they are **close** ($V\gg\hbar\Omega$), the doubly excited state $|rr\rangle$ is shifted out of resonance. Starting from $|gg\rangle$, the laser can only reach the symmetric singly excited state $|W\rangle=(|gr\rangle+|rg\rangle)/\sqrt2$. The matrix element $\langle W|H|gg\rangle=\sqrt2\,\hbar\Omega/2$, so the pair oscillates between $|gg\rangle$ and an **entangled** state at the enhanced frequency $\sqrt2\,\Omega$.

![Left: level diagram of two atoms; the ground state gg couples to the symmetric singly excited state W with Rabi frequency root 2 Omega, while the doubly excited state rr is shifted up by V and is no longer resonant with the laser. Right: van der Waals interaction energy of two 70S atoms versus distance on a log scale, crossing the 2 MHz line of h-bar Omega at the blockade radius of 8.7 micrometres; at 5 micrometres it is 55 MHz. The region inside the blockade radius is shaded](figures/10-blockade.png)

*The blockade radius marks the crossover $V=\hbar\Omega$. Deep inside it, $V\gg\hbar\Omega$ and double excitation is strongly suppressed; far outside it, $V\ll\hbar\Omega$ and the atoms approach independent dynamics. Neither limit is a sharp boundary at $R_b$.*

The crossover defines the **blockade radius**

$$R_b=\Big(\frac{C_6}{\hbar\Omega}\Big)^{1/6},$$

which is $(863\ {\rm GHz}/2\ {\rm MHz})^{1/6}\ \mu{\rm m}=8.7\ \mu$m for $70S$ at $\Omega/2\pi=2$ MHz. The sixth root makes $R_b$ insensitive to the drive strength. A factor of 2 in $\Omega$ moves $R_b$ by a factor of only $2^{1/6}=1.12$.

The blockade is not perfect. The doubly excited state is still weakly coupled, off resonance by $V$, so its population is of order $(\hbar\Omega/V)^2$: at most about $\frac12(2/55)^2\approx7\times10^{-4}$ at 5 $\mu$m (that is the peak value, reached when the pair is in $|W\rangle$; the time average is about half of it). Lab 10 confirms that halving $V$ multiplies the residual double excitation by 4.

**Many atoms.** If all relevant pair interactions are sufficiently large compared with the collective drive couplings, the ensemble approximately remains in the zero- and one-excitation subspace. Being just inside the single-atom $R_b$ is not sufficient; a useful strong-blockade scale for a uniform cluster is $|V_{ij}|\gg\hbar\sqrt{N}\,\Omega$. With uniform drive amplitudes and phases, only one excitation can be shared among them, and the ground state couples to the symmetric state $\frac1{\sqrt N}\sum_i|g\cdots r_i\cdots g\rangle$ with matrix element $\sqrt N\,\hbar\Omega/2$: a **collective Rabi frequency** $\sqrt N\,\Omega$. Blockade between two individual atoms was first observed in 2009, as suppressed double excitation (Urban et al.) and as the $\sqrt2$-enhanced collective Rabi oscillation (Gaëtan et al.).

> **Intuition aside.** Think of it as energy bookkeeping. The laser is tuned to supply the energy of one excitation. A second excitation would need an extra $V$ that no photon in the beam provides, so it does not happen. Which of the two atoms took the excitation is left undecided, and that undecided superposition is the entangled state $|W\rangle$.

## From blockade to quantum simulation

Let many atoms in an array evolve under the same laser, now with a detuning $\Delta$:

$$\frac{H}{\hbar}=\sum_i\frac{\Omega}{2}\sigma^x_i-\Delta\sum_in_i+\sum_{i<j}\frac{V_{ij}}{\hbar}n_in_j .$$

This is an Ising-type spin model in a transverse field, with the "spin up" state being the Rydberg state: $\Omega$ plays the role of a transverse field, $\Delta$ of a longitudinal field (a chemical potential for Rydberg excitations), and $V_{ij}$ of an interaction that penalises nearby excitations (writing $n_i=(1+\sigma^z_i)/2$ turns $V_{ij}n_in_j$ into an Ising coupling $\sigma^z_i\sigma^z_j$ plus extra longitudinal fields). Running this Hamiltonian directly, rather than breaking it into gates, is called **analog quantum simulation**. It works with the ground-Rydberg two-level system itself; the hyperfine qubit of Chapter 09 plays no part.

**Ordered phases in a chain.** Consider atoms on a line with spacing $a$ such that nearest neighbours are blockaded ($V(a)\gg\hbar\Omega$) but next-nearest neighbours are not ($V(2a)=V(a)/64\ll\hbar\Omega$). With $\Omega\to0$ and $V(2a)$ neglected, the energy of a configuration is $-\hbar\Delta$ per excitation plus the interactions:

- For $\Delta<0$, every excitation costs energy, so the ground state has all atoms in $|g\rangle$.
- For $0<\Delta<V(a)/\hbar$, every excitation lowers the energy, but exciting the second atom of a neighbouring pair costs $V(a)$ and gains only $\hbar\Delta$, a net cost of $V(a)-\hbar\Delta>0$. The ground state therefore packs in as many excitations as the blockade allows, $|r\,g\,r\,g\cdots\rangle$. This crystal repeats only every two sites, so it breaks the chain's translation symmetry. In a long chain the two patterns $r\,g\,r\,g\ldots$ and $g\,r\,g\,r\ldots$ have the same energy, hence the name **$Z_2$ phase**; in an odd chain with open ends, $r$ on both ends makes one pattern the unique ground state. (Adding an excitation between two excited atoms would cost $2V(a)-\hbar\Delta$, so the condition $\Delta<V(a)/\hbar$ is sufficient but not tight.)

Between the two lies a quantum phase transition; with $\Omega>0$, quantum fluctuations shift it to positive $\Delta$ (in lab 13, near $\Delta/2\pi\approx1.4$ MHz, where the gap is smallest). A chain of $N$ atoms has only $F(N+2)$ configurations without neighbouring excitations (a Fibonacci number, with $F(1)=F(2)=1$: 89 for nine atoms, instead of $2^9=512$). In the limit of perfect nearest-neighbour blockade and $\Delta=0$ the Hamiltonian becomes $H/\hbar=\frac{\Omega}{2}\sum_iP_{i-1}\sigma^x_iP_{i+1}$ with $P=|g\rangle\langle g|$: an atom can flip only if both of its neighbours are in $|g\rangle$. That form is why the blockaded chain is called the "PXP model".

**Adiabatic preparation.** To reach the crystal, start with all atoms in $|g\rangle$ at large negative $\Delta$ (the ground state there), switch on $\Omega$, and sweep $\Delta$ slowly to positive values. Adiabatic following requires $|\langle m|\partial_t(H/\hbar)|0\rangle|\ll[(E_m-E_0)/\hbar]^2$ for coupled excited states throughout the protocol, including the ramps of $\Omega$. Comparing $d\Delta/dt$ with the squared gap alone is a scale estimate that omits the transition matrix elements. In a finite chain the gap typically reaches a nonzero minimum near the crossover associated with the thermodynamic phase transition. [Lab 13](../hands-on/13-adiabatic-z2/) does this for nine atoms 6 $\mu$m apart: the minimum gap in angular units is $2\pi\times0.79$ MHz, and the probability of the perfect crystal rises from 3% for a 0.5 $\mu$s sweep to 96% for an 8 $\mu$s sweep.

![Three panels from lab 13. Left: the energy gap to the first reflection-symmetric excited state of a nine-atom Rydberg chain versus detuning, falling from about 6 MHz to a minimum of 0.79 MHz near 1.4 MHz detuning and rising again. Middle: probability of the perfect Z2 crystal versus sweep time, rising from 3 percent at 0.5 microseconds to 96 percent at 8 microseconds. Right: Rydberg population on each of the nine sites at the end of the sweep for sweep times of 0.5, 2 and 8 microseconds; the slow sweep shows the alternating pattern r g r g with populations near 1 and 0](../hands-on/13-adiabatic-z2/figures/z2_sweep.png)

*Lab 13: adiabatic preparation of a $Z_2$ crystal. The slower the sweep, the fewer defects.*

**What experiments do with it.** Programmable arrays of tens to hundreds of atoms have used this Hamiltonian to prepare such ordered phases and study the transitions between them, to watch non-equilibrium many-body dynamics (including unexpectedly long-lived oscillations from the $Z_2$ state, known as quantum many-body scars), and to explore two-dimensional phases on square and triangular lattices (Bernien et al., 2017, in one dimension; Ebadi et al., 2021; Scholl et al., 2021). Other interactions are available too: atoms in two *different* Rydberg states exchange excitations through the resonant dipole-dipole interaction $\propto1/R^3$, which realises XY spin models, and weakly admixing Rydberg character into ground states ("Rydberg dressing") gives a weak, soft-core interaction between ground-state atoms: flat at short distance and falling as $1/R^6$ beyond a radius of a few micrometres set by the dressing detuning.

## Worked example (Rb-87, 70S, illustrative numbers)

| Quantity | Formula | Value |
|---|---|---|
| effective quantum number | $70-3.131$ | 66.87 |
| orbit radius | $\frac32n^{*2}a_0$ | **355 nm** |
| lifetime at 300 K | ARC | **146 $\mu$s** |
| $C_6/h$ | ARC | 863 GHz $\mu$m$^6$ |
| interaction frequency at 5 $\mu$m | $V/h=C_6/(hR^6)$ | **55 MHz** |
| blockade radius at $\Omega/2\pi=2$ MHz | $(C_6/\hbar\Omega)^{1/6}$ | **8.7 $\mu$m** |
| residual double excitation at 5 $\mu$m | $\sim\frac12(\hbar\Omega/V)^2$ | **$7\times10^{-4}$** |
| time-to-entangle ($\pi$ pulse at $\sqrt2\Omega$) | $\pi/(\sqrt2\Omega)$ | **177 ns** |
| decay during it | $\approx\frac12t/\tau$ (upper bound $t/\tau$) | **$\approx6\times10^{-4}$** ($1.2\times10^{-3}$) |

**Step 1: size.** $\frac32\times66.87^2\times0.0529\ {\rm nm}=355$ nm, about a third of a tweezer waist.

**Step 2: interaction and blockade.** $V/h=55$ MHz at 5 $\mu$m is 28 times $\Omega/2\pi=2$ MHz, well inside the blockade regime. At 10 $\mu$m it falls to 0.86 MHz, below $\Omega/2\pi$, and the blockade is only partial. The array spacing must sit well inside $R_b=8.7\ \mu$m for the atoms that should interact, and well outside it for those that should not.

**Step 3: speed versus lifetime.** Starting from $|gg\rangle$, a pulse of length $\pi/(\sqrt2\Omega)=1/(2\sqrt2\times2\ {\rm MHz})=177$ ns creates $|W\rangle$. The pair spends on average about half of that time with one atom in $|r\rangle$, so the probability of a decay is roughly $0.5\times177\ {\rm ns}/146\ \mu{\rm s}\approx6\times10^{-4}$ (the table's $t/\tau$ is the pessimistic upper bound). Lifetime limits on gate fidelity are therefore at the $10^{-3}$ level; Chapter 11 does this budget properly.

## Run it

[Lab 13](../hands-on/13-adiabatic-z2/) prepares a nine-atom $Z_2$ crystal by an adiabatic detuning sweep. [Lab 10](../hands-on/10-rydberg-blockade/) simulates two atoms as a function of distance, extracts the $\sqrt2$ enhancement and the $(\Omega/V)^2$ residual double excitation, checks the collective $\sqrt N$ Rabi frequency for up to four atoms, and fits the Rydberg scaling laws to ARC data.

## Common pitfalls

- **"Blockade means the interaction is infinite."** The leakage into $|rr\rangle$ is of order $(\hbar\Omega/V)^2$; it is a gate error and a source of unwanted entanglement with distant atoms.
- **Mixing up $C_6$ conventions.** ARC prints $C_6$ with the opposite sign to the convention used here; some papers quote $C_6$ in units of $h$, others in angular units ($2\pi\times$GHz $\mu$m$^6$). Always check the sign and the factor of $2\pi$.
- **"Higher $n$ is always better."** $C_6$ grows as $n^{*11}$ and lifetimes as $n^{*3}$, but so do electric-field sensitivity ($n^{*7}$) and the difficulty of exciting the state (the coupling falls as $n^{*-3/2}$), and blackbody transfer to neighbouring Rydberg states becomes the dominant decay channel. Most experiments settle on $n\approx50$ to 80.
- **Forgetting the Doppler effect.** With counter-propagating 420 nm and 1013 nm beams, a 10 $\mu$K atom has a 43 kHz rms Doppler detuning; that limits ground-Rydberg coherence to microseconds.
- **"The ground-Rydberg qubit is a good memory."** With a lifetime of $\sim100\ \mu$s and laser-phase sensitivity it is not; information is stored in hyperfine states and only briefly mapped to $|r\rangle$ during gates.

## Key takeaways

- Rydberg atoms have $n\approx50$ to 100; their properties scale as powers of $n^*$: radius $n^{*2}$, radiative lifetime $n^{*3}$, polarizability $n^{*7}$, $C_6$ $n^{*11}$.
- Two $70S$ Rb atoms interact with $C_6/h=863$ GHz $\mu$m$^6$: 55 MHz at 5 $\mu$m.
- When $V\gg\hbar\Omega$, double excitation is blocked; two atoms oscillate between $|gg\rangle$ and the entangled $|W\rangle$ at $\sqrt2\Omega$, and $N$ atoms at $\sqrt N\Omega$.
- The blockade radius $R_b=(C_6/\hbar\Omega)^{1/6}$ is 8.7 $\mu$m at $\Omega/2\pi=2$ MHz.
- The same Hamiltonian, run with a detuning sweep across an array, is a programmable quantum simulator of Ising-type models; in lab 13 a slow sweep prepares the $Z_2$ crystal of a blockaded chain.

## Go deeper

- M. Saffman, T. G. Walker, K. Mølmer, *Quantum information with Rydberg atoms*, Rev. Mod. Phys. 82, 2313 (2010), [arXiv:0909.4777](https://arxiv.org/abs/0909.4777). The standard review: scaling laws, interactions, blockade and gate proposals.
- A. Browaeys and T. Lahaye, *Many-body physics with individually controlled Rydberg atoms*, Nat. Phys. 16, 132 (2020), [arXiv:2002.07413](https://arxiv.org/abs/2002.07413). The quantum-simulation side, very readable.
- N. Šibalić, J. D. Pritchard, C. S. Adams, K. J. Weatherill, *ARC: An open-source library for calculating properties of alkali Rydberg atoms*, Comput. Phys. Commun. 220, 319 (2017), [arXiv:1612.05529](https://arxiv.org/abs/1612.05529). The library behind every Rydberg number in this chapter.
- A. Gaëtan et al., *Observation of collective excitation of two individual atoms in the Rydberg blockade regime*, Nat. Phys. 5, 115 (2009), [arXiv:0810.2960](https://arxiv.org/abs/0810.2960); E. Urban et al., *Observation of Rydberg blockade between two atoms*, Nat. Phys. 5, 110 (2009), [arXiv:0805.0758](https://arxiv.org/abs/0805.0758).
- T. F. Gallagher, *Rydberg Atoms* (Cambridge University Press, 1994). The classic monograph on Rydberg physics.

---

← Previous: [Atomic Qubits, Single-Qubit Gates and Coherence](09-qubits-coherence.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [Rydberg Entangling Gates and Their Errors](11-rydberg-gates.md) →
