# 06 · Sub-Doppler Cooling and the Magneto-Optical Trap

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

Chapter 05 treated the atom as a two-level system and found a temperature floor, the Doppler limit. Real atoms have several ground-state sublevels, and that changes everything twice. First, sublevels that are light-shifted by different amounts at different points of a polarization-varying light field make possible **Sisyphus cooling**, which reaches a few microkelvin, far below the Doppler limit. Second, sublevels that are Zeeman-shifted by a magnetic field gradient make the scattering force depend on position, which turns molasses into a **trap**: the magneto-optical trap, or MOT. These two ideas are the "multilevel atom" part of Metcalf and van der Straten's review, and together they produce the cold, dense clouds from which tweezers are loaded.

## Why the Doppler theory fails

The Doppler model has one ground state. Its only handle on the atom's velocity is the Doppler shift, which is smaller than the linewidth for slow atoms, so the friction is weak and the random kicks win at $T_D=\hbar\Gamma/2k_B$. In a multilevel atom there is a second, much slower internal time scale: the **optical pumping time** $\tau_p$ it takes for scattered photons to move the atom from one ground sublevel to another. When $\tau_p$ is long compared with $1/\Gamma$, the atom's internal state lags behind its motion, and that lag can be turned into a friction force much stronger than the Doppler one for slow atoms. The price is a small velocity capture range: sub-Doppler cooling only works on atoms that Doppler cooling has already slowed.

## Polarization gradients and Sisyphus cooling

Take two counter-propagating beams with **orthogonal linear polarizations** (the "lin$\perp$lin" configuration). The total field has constant intensity but its polarization changes along $z$ with period $\lambda/2$: linear at $z=0$, circular $\sigma^+$ at $\lambda/8$, linear (rotated by $90°$) at $\lambda/4$, $\sigma^-$ at $3\lambda/8$, and so on. The $\sigma^\pm$ fractions of the intensity are $(1\pm\sin2kz)/2$.

Now take the simplest atom with ground-state structure: $J=1/2\to J'=3/2$. Its two ground sublevels $m=\pm1/2$ couple to $\sigma^+$ and $\sigma^-$ light with different strengths: the stretched transition $m=+1/2\to m'=+3/2$ is three times stronger than $m=-1/2\to m'=+1/2$ (squared Clebsch-Gordan coefficients 1 and 1/3). With red detuning both sublevels are light-shifted down, but by different, position-dependent amounts:

$$U_{\pm1/2}(z)=E_{\rm ls}\Big[\tfrac23\pm\tfrac13\sin2kz\Big],\qquad E_{\rm ls}<0 ,$$

where $E_{\rm ls}$ is the light shift the stretched transition would have in pure circular light.

Where the light is $\sigma^+$, the $m=+1/2$ level is lowest; where it is $\sigma^-$, the $m=-1/2$ level is lowest. Optical pumping follows the polarization: $\sigma^+$ light pumps atoms into $m=+1/2$ and $\sigma^-$ into $m=-1/2$. So optical pumping **always moves the atom into the lower of the two levels**.

![Light shifts of the m = +1/2 and m = -1/2 ground sublevels along one wavelength of a lin-perp-lin standing wave; the two curves oscillate in antiphase between -1 and -1/3 of the maximum light shift, with the local polarization labelled lin, sigma+, lin, sigma-, repeating every half wavelength. A dotted path shows an atom climbing a hill in m = +1/2 from z = lambda/8 to 3 lambda/8, and an arrow shows it being optically pumped down to the valley of m = -1/2 at the hilltop](figures/06-sisyphus.png)

*Sisyphus cooling. A moving atom climbs a potential hill, converting kinetic energy into potential energy. Near the hilltop the light is $\sigma^-$ and the atom is pumped into the other sublevel, which is at the bottom of its own valley. The spontaneously emitted photon is bluer than the absorbed one by the height of the hill, and that energy is gone for good.*

The name comes from the Greek myth: the atom is forever climbing hills. Each climb removes the height of a hill, $\tfrac23|E_{\rm ls}|$, so the temperature reached scales with the light shift,

$$k_BT\sim|E_{\rm ls}|\propto\frac{\hbar\Omega^2}{|\delta|}\propto\frac{I}{|\delta|}\qquad(|\delta|\gg\Gamma),$$

with a numerical prefactor of order one that depends on the atomic structure. Lower intensity and larger detuning make colder atoms, until the hills become so shallow that a single photon recoil is enough to climb out of a valley. That sets a floor at a few tens of recoil energies $E_r$: a few microkelvin for Rb and Cs, compared with Doppler limits of about $125$ to $150\ \mu$K.

> **Intuition aside.** Doppler cooling asks the atom to notice a frequency shift smaller than its linewidth: it's like trying to feel a gentle breeze. Sisyphus cooling instead makes the atom pay a toll in potential energy every half wavelength. Even a very slow atom has to pay it, so the friction stays strong down to very low velocities.

**Other configurations.** With circularly polarized counter-propagating beams ($\sigma^+\sigma^-$) the polarization is linear everywhere but rotates along $z$, so there are no potential hills. A moving atom still sees the polarization rotate, which creates an imbalance of ground-state populations that makes it scatter more from the beam it moves toward. This "motion-induced orientation" also cools far below the Doppler limit; it needs a ground state with $J\ge1$ (or $F\ge1$). Six-beam molasses and the MOT contain both kinds of gradient.

**Gray molasses.** A modern variant tunes the cooling light slightly to the **blue** of a transition with dark states (for alkalis, usually D1, $F\to F'=F$). Atoms at rest are pumped into a dark state that does not scatter. The bright states are light-shifted upward by the blue-detuned light, by an amount that varies in space. A moving atom is coupled non-adiabatically from the dark state into a bright state, most likely near the bottom of a bright-state valley, where the two are closest in energy; it then climbs a hill and is optically pumped back into the dark state near the hilltop, losing energy as in Sisyphus cooling. Gray molasses reaches very low temperatures at high density with little light scattering, which is why it is popular for loading tweezers (Chapter 08).

## The magneto-optical trap

Molasses cools but does not confine. To trap, the force must also depend on position. The MOT does this by adding a magnetic field that is zero at the centre and grows linearly outward, $B=Az$, produced by a pair of coils with opposite currents (anti-Helmholtz).

**The 1D model.** Take an atom with a $J=0$ ground state and a $J'=1$ excited state with sublevels $m'=-1,0,+1$. The field shifts $m'=\pm1$ by $\pm\mu'Az$, with $\mu'=g'\mu_B$. Shine a red-detuned $\sigma^+$ beam from the left and a $\sigma^-$ beam from the right. At $z>0$ the $m'=-1$ level is shifted down toward the laser frequency, so the atom scatters more from the $\sigma^-$ beam, which pushes it back toward $z=0$. At $z<0$ the roles reverse.

![Left: one-dimensional MOT energy diagram versus position; the m' = +1 excited level tilts up and m' = -1 tilts down with z, crossing at the centre; a red-detuned laser line meets m' = +1 at negative z and m' = -1 at positive z, so sigma-plus light from the left is resonant on the left and sigma-minus light from the right is resonant on the right. Right: a 3D MOT with a pair of anti-Helmholtz coils carrying opposite currents and six circularly polarized red-detuned beams meeting at the centre](figures/06-mot-scheme.png)

*The MOT mechanism. Zeeman shifts make the beam that pushes toward the centre the one closer to resonance. In 3D, three orthogonal pairs of beams with the right circular polarizations do the same in every direction.*

The force from each beam has the same Lorentzian form as in molasses, with the Zeeman shift added to the Doppler shift:

$$F_\pm=\pm\hbar k\frac{\Gamma}{2}\frac{s_0}{1+s_0+\big(2\delta_\pm/\Gamma\big)^2},\qquad\delta_\pm=\delta\mp kv\mp\frac{\mu'Az}{\hbar}.$$

Because $v$ and $\mu'Az/\hbar k$ enter in the same way, the small-$z$, small-$v$ expansion is immediate:

$$\boxed{\ F=-\beta v-\kappa z,\qquad\kappa=\frac{\mu'A}{\hbar k}\,\beta\ }$$

with $\beta$ the molasses friction coefficient of Chapter 05. The atom is a **damped harmonic oscillator** with frequency $\omega_0=\sqrt{\kappa/m}$ and damping rate $\beta/m$.

![Force on an atom at rest versus position in a 1D MOT with a 10 G/cm gradient, saturation parameter 1 and beams of radius 10 mm, for detunings -0.5, -1, -2 and -3 Gamma. Each curve is restoring, linear near the centre and peaked where the Zeeman shift roughly equals the detuning (for -3 Gamma that point lies outside the beams); larger detuning gives a smaller spring constant but a longer-range force](figures/06-mot-force.png)

*The 1D MOT force for Rb-87 at rest. The force peaks where the Zeeman shift compensates the detuning, $z\approx\hbar|\delta|/\mu'A$; beyond that it falls off. Large detuning makes a larger, softer trap with a bigger capture range, which is why MOTs typically load at $\delta\approx-2\Gamma$ to $-3\Gamma$.*

### The MOT in practice

- **Gradient**: typically 10 to 20 G/cm along the coil axis; Maxwell's equation $\nabla\cdot\mathbf B=0$ makes the radial gradients half as large.
- **Source**: atoms are captured from a Zeeman-slowed beam (Chapter 05), from a 2D MOT that produces a cold atomic beam, or directly from the slow tail of a room-temperature vapour in a glass cell (the "vapour-cell MOT").
- **Repumper**: the $F=2\to F'=3$ cooling light must be accompanied by $F=1\to F'=2$ light (Chapter 02).
- **What you get**: millions to billions of atoms at tens to a hundred microkelvin in a cloud about a millimetre across. Sub-Doppler mechanisms work near the field zero, so MOTs are often colder than $T_D$; switching off the field and lowering the intensity (a molasses stage) then cools further, to about $10\ \mu$K.
- **Density limit**: atoms in the cloud reabsorb each other's scattered photons, which pushes them apart, so MOT densities saturate around $10^{10}$ to $10^{11}$ atoms per cm$^3$.

## Worked example: a 1D MOT for Rb-87 (illustrative numbers)

These are the parameters of [lab 04](../hands-on/04-mot/).

| Quantity | Formula | Value |
|---|---|---|
| detuning, intensity, gradient | | $\delta=-\Gamma$, $s_0=1$ per beam, $A=10$ G/cm, $\mu'=\mu_B$ |
| friction | $\beta=-8\hbar k^2\delta s_0/\Gamma(1+s_0+(2\delta/\Gamma)^2)^2$ | **$1.52\times10^{-21}$ kg/s** |
| spring constant | $\kappa=\mu'A\beta/\hbar k$ | **$1.66\times10^{-18}$ N/m** |
| trap frequency | $\sqrt{\kappa/m}/2\pi$ | **540 Hz** |
| damping rate | $\beta/m$ | **$1.05\times10^4\ {\rm s^{-1}}$** |
| force maximum (edge of the trap) | $z\approx\hbar\vert\delta\vert/\mu'A$ | **4.3 mm** (linear only for $\vert z\vert\lesssim2$ mm) |
| capture velocity (beams of 1 cm radius) | numerical (lab 04) | **20 m/s** |

**Step 1: friction.** Substitute $\delta=-\Gamma$ (so $2\delta/\Gamma=-2$) and $s_0=1$: $\beta=8\hbar k^2\,\Gamma\times1/[\Gamma\,(1+1+4)^2]=\frac{8}{36}\hbar k^2=0.222\times6.84\times10^{-21}=1.52\times10^{-21}$ kg/s. (A common slip is to use $|\delta|=\Gamma/2$ from the Doppler-limit discussion; substitute the detuning you actually chose.)

**Step 2: spring constant.** $\mu'A/\hbar k=(9.274\times10^{-24})(0.10)/(8.49\times10^{-28})=1092$ s$^{-1}$, so $\kappa=1092\times1.52\times10^{-21}=1.66\times10^{-18}$ N/m.

**Step 3: oscillation versus damping.** $\omega_0=\sqrt{1.66\times10^{-18}/1.443\times10^{-25}}=3390$ rad/s ($f=540$ Hz). The damping rate $\beta/m=1.05\times10^4\ {\rm s^{-1}}$ exceeds $2\omega_0=6780\ {\rm s^{-1}}$, so the motion is **overdamped**: a displaced atom creeps back to the centre in about a millisecond without oscillating, as lab 04 shows.

**Step 4: capture.** An atom entering beams of 1 cm radius is captured in lab 04 if it is slower than 20 m/s. Within this 1D model an upper bound is set by energy: the force can never exceed $\hbar k\frac{\Gamma}{2}\frac{s_0}{1+s_0}$, which over the 2 cm beam diameter removes at most the kinetic energy of an atom at 47 m/s. The atoms leaving the slower of Chapter 05 at about 26 m/s need larger beams or more detuning; this is why real MOT beams are 1 to 3 cm across and detuned by $2\Gamma$ to $3\Gamma$ during loading.

## From the MOT to a tweezer

The MOT is a reservoir. A typical tweezer experiment loads the MOT for 50 to 500 ms, then switches the gradient off and applies molasses (often gray molasses) at about $10\ \mu$K while the tweezers are on. Atoms falling into the tweezers are cooled by the same molasses light, and light-assisted collisions leave zero or one atom per tweezer. Chapter 07 describes the tweezers themselves; Chapter 08 describes the loading.

## Run it

[Lab 04](../hands-on/04-mot/) computes the 1D MOT force, checks $\beta$ and $\kappa$ against numerical derivatives, compares a small oscillation with the analytic damped-oscillator solution, and finds the capture velocity by bisection.

## Common pitfalls

- **"The MOT works because atoms are attracted to the field zero."** The field by itself exerts only a tiny force on the atom's magnetic moment. The MOT force is a scattering force; the field only decides which beam is closer to resonance.
- **Wrong circular polarizations.** With the opposite handedness, or the opposite coil current, the "restoring" force pushes atoms out. When a new MOT does not work, flipping the coil current is the first test.
- **"Sub-Doppler cooling needs special beams."** Ordinary six-beam molasses already contains polarization gradients. What it needs is a multilevel ground state, low intensity, larger detuning, and a small magnetic field (stray fields of a fraction of a gauss shift the sublevels and destroy the mechanism).
- **"Lower intensity is always colder."** Only down to the recoil-limited floor; below it the hills cannot hold atoms and the temperature rises again. The capture velocity also shrinks with intensity.
- **"The MOT is the coldest stage."** The MOT trades temperature for capture and confinement; the molasses that follows is colder.

## Key takeaways

- Multilevel atoms in polarization gradients undergo Sisyphus cooling: optical pumping moves them from hilltops to valleys, and the emitted photons carry away the energy. Temperatures scale as $I/|\delta|$ and reach a few microkelvin.
- Sub-Doppler mechanisms have small capture ranges; they work after Doppler cooling.
- A MOT combines molasses with a quadrupole field: Zeeman shifts make the scattering force restoring, $F=-\beta v-\kappa z$ with $\kappa=\mu'A\beta/\hbar k$.
- For Rb with 10 G/cm and $\delta=-\Gamma$, the 1D model gives a 540 Hz, overdamped trap with a capture velocity of about 20 m/s for beams of 1 cm radius.
- MOTs deliver millions of atoms at tens of microkelvin, the reservoir from which tweezers are loaded.

## Go deeper

- H. J. Metcalf and P. van der Straten, *Laser cooling and trapping of atoms*, J. Opt. Soc. Am. B 20, 887 (2003), [Utrecht preprint](https://webspace.science.uu.nl/~strat102/preprint/handpubl.pdf). Its sections on cooling below the Doppler limit and on magneto-optical trapping use the same models, including the MOT spring constant $\kappa=\mu'A\beta/\hbar k$.
- J. Dalibard and C. Cohen-Tannoudji, *Laser cooling below the Doppler limit by polarization gradients: simple theoretical models*, J. Opt. Soc. Am. B 6, 2023 (1989). The original explanation of Sisyphus and $\sigma^+\sigma^-$ cooling.
- E. L. Raab, M. Prentiss, A. Cable, S. Chu, D. E. Pritchard, *Trapping of neutral sodium atoms with radiation pressure*, Phys. Rev. Lett. 59, 2631 (1987). The first MOT.
- C. J. Foot, *Atomic Physics* (Oxford University Press, 2005), chapter 9. A clear textbook treatment of the MOT and of Sisyphus cooling.

---

← Previous: [Slowing and Doppler Cooling](05-doppler-cooling.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [Optical Dipole Traps and Tweezers](07-optical-tweezers.md) →
