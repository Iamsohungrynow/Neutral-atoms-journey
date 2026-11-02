# 07 · Optical Dipole Traps and Tweezers

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

An optical tweezer is a single laser beam focused to a spot about a micrometre wide. Tuned to the red of the atomic resonance, it attracts atoms to its focus through the dipole force of Chapter 04, making a potential well about a millikelvin deep. Here we put numbers on it. Far from resonance the polarizability needs both D lines and the counter-rotating terms. The Gaussian-beam optics then fix the depth and the trap frequencies, the scattering rate tells us how fast the atom heats, and a small difference between the light shifts of the two qubit states comes back in Chapter 09 as dephasing. The last part treats the atom's motion in the well as quantized. For the trap physics the standard reference is the review by Grimm, Weidemüller and Ovchinnikov; for quantized motion, Metcalf and van der Straten.

## From the two-level light shift to a real atom

Chapter 04 found the light shift $\hbar\Omega^2/4\delta$ for a two-level atom near resonance. A tweezer is detuned by tens to hundreds of terahertz, which changes two things.

**The counter-rotating term returns.** The rotating-wave approximation dropped terms oscillating at $\omega_0+\omega$. Near resonance they are negligible; at 1064 nm, where $\omega$ is only 27% below $\omega_0$, they are not. The classical Lorentz oscillator keeps both terms automatically. For a transition with linewidth $\Gamma$ at frequency $\omega_0$ the polarizability is

$$\alpha(\omega)=6\pi\varepsilon_0c^3\,\frac{\Gamma/\omega_0^2}{\omega_0^2-\omega^2},$$

and the potential and the scattering rate in light of intensity $I$ are

$$U=-\frac{\alpha I}{2\varepsilon_0c},\qquad \Gamma_{\rm sc}=\frac{3\pi c^2}{2\hbar\omega_0^3}\Big(\frac{\omega}{\omega_0}\Big)^3\Big(\frac{\Gamma}{\omega_0-\omega}+\frac{\Gamma}{\omega_0+\omega}\Big)^2I .$$

Near resonance these reduce to $U=\hbar\Omega^2/4\delta$ and $\hbar\Gamma_{\rm sc}=(\Gamma/|\delta|)|U|$ of Chapter 04.

**Both D lines contribute.** The $5S_{1/2}$ ground state couples to both $5P_{1/2}$ (D1) and $5P_{3/2}$ (D2). For linearly polarized light the contributions add with weights $1/3$ and $2/3$, the fractions of the total line strength in each line. The result for Rb-87, computed in [lab 05](../hands-on/05-tweezer-trap/), is:

| Wavelength | Polarizability | Note |
|---|---|---|
| static ($\lambda\to\infty$) | 308 a.u. | the measured 318.8 a.u. includes higher states and the core |
| 1064 nm | **677 a.u.** | attractive |
| 852 nm | **2070 a.u.** | attractive, three times stronger |
| 790.03 nm | **0** | "tune-out" wavelength between the D lines: D1 and D2 cancel |
| 532 nm | $-$262 a.u. | repulsive |

(One atomic unit of polarizability is $4\pi\varepsilon_0a_0^3=1.649\times10^{-41}$ C m$^2$/V.)

![Three panels from lab 05. Left: ground-state polarizability of Rb-87 versus trap wavelength from 500 to 1200 nm, with poles at the D2 (780 nm) and D1 (795 nm) lines, positive (attractive) to the red of D1 and between D2 and the 790 nm tune-out wavelength, negative (repulsive) between the tune-out and D1 and to the blue of D2, and 677 atomic units at 1064 nm. Middle: radial and axial cuts through a 1 millikelvin tweezer at 1064 nm with a 1 micrometre waist and their harmonic approximations; the radial well has a full width at half depth of about 1.2 micrometres and the axial well about 5.9 micrometres. Right: photons scattered per second at a fixed depth of 1 millikelvin versus wavelength, falling from about 100 per second near 805 nm to 21.8 at 852 nm and 3.6 at 1064 nm](../hands-on/05-tweezer-trap/figures/tweezer.png)

*Lab 05's tweezer. Left: the polarizability changes sign at each resonance; any wavelength red of D1 traps ground-state atoms. Middle: a 1 mK tweezer is a narrow radial well and a long axial one. Right: at fixed depth, farther detuning means less scattering (the $\Gamma/\delta$ rule of Chapter 04).*

## The Gaussian focus

A laser focused by a lens of numerical aperture NA forms, to a good approximation, a Gaussian beam:

$$I(r,z)=\frac{2P}{\pi w(z)^2}\exp\!\Big(-\frac{2r^2}{w(z)^2}\Big),\qquad w(z)=w_0\sqrt{1+(z/z_R)^2},\qquad z_R=\frac{\pi w_0^2}{\lambda}.$$

The waist $w_0$ is the $1/e^2$ intensity radius at the focus; a lens of numerical aperture NA, uniformly filled, produces a diffraction-limited spot that is well approximated by a Gaussian with $w_0\approx0.42\,\lambda/{\rm NA}$, about $0.9\ \mu$m for 1064 nm and NA $=0.5$. (The often-quoted $\lambda/(\pi\,{\rm NA})$ assumes an untruncated Gaussian beam whose $1/e^2$ divergence half-angle equals the NA; a uniformly filled aperture gives the larger $0.42\,\lambda/{\rm NA}$ at any NA, and at NA $\gtrsim0.5$ non-paraxial effects enlarge the spot a little further.) Real tweezers have waists of about $0.7$ to $1\ \mu$m. The **Rayleigh range** $z_R$ is the distance over which the beam stays focused; for $w_0=1\ \mu$m at 1064 nm it is $2.95\ \mu$m, about three waists, so the radial and axial trap frequencies (and thermal cloud sizes) differ by a factor $\sqrt2\,z_R/w_0\approx4$.

![Left: schematic of a collimated 1064 nm beam focused by a high numerical aperture objective onto an atom at the focus; the same lens collects fluorescence. Right: colour map of intensity near the focus versus radial position and position along the beam, with dashed lines showing the beam radius w(z) growing from 1 micrometre at the waist, and dotted lines at the Rayleigh range of 2.95 micrometres](figures/07-tweezer-geometry.png)

*Tweezer geometry. The intensity, and therefore the trap, is tightly confined in the focal plane and elongated along the beam.*

### Depth and trap frequencies

The trap depth is the potential at the centre, $U_0=\alpha I_0/(2\varepsilon_0c)$ with $I_0=2P/\pi w_0^2$. Near the bottom, expand the exponential and the $1/w(z)^2$ factor to second order:

$$U(r,z)\approx-U_0+\tfrac12m\omega_r^2r^2+\tfrac12m\omega_z^2z^2,\qquad \omega_r=\sqrt{\frac{4U_0}{mw_0^2}},\qquad \omega_z=\sqrt{\frac{2U_0}{mz_R^2}}.$$

The ratio $\omega_r/\omega_z=\sqrt2\,z_R/w_0=\sqrt2\,\pi w_0/\lambda$ is about 4 for a 1 $\mu$m waist. At a given depth the radial frequency depends only on $U_0$ and $w_0$; the wavelength enters through $z_R$ and so affects only the axial frequency. Away from the bottom the Gaussian well is softer than the parabola, so hot atoms, which reach the outer parts of the well, oscillate more slowly than $\omega_r$ and $\omega_z$ suggest.

### Scattering and heating

Each scattered trap photon gives the atom about $2E_r$ of energy (Chapter 04), now with $E_r$ evaluated at the trap wavelength. At fixed depth $\Gamma_{\rm sc}$ falls roughly as $1/|\delta|$, which is the reason tweezers use far-detuned light. Lab 05 gives, for a 1 mK trap:

| | 1064 nm | 852 nm |
|---|---|---|
| power for $U_0=1$ mK ($w_0=1\ \mu$m) | 10.3 mW | 3.4 mW |
| scattering rate | 3.6 s$^{-1}$ | 21.8 s$^{-1}$ |
| recoil heating $2E_r\Gamma_{\rm sc}$ (energy) | $k_B\times0.7\ \mu$K/s | $k_B\times6.6\ \mu$K/s |

Over the second or so that an experiment lasts, both are negligible against a 1 mK depth. Scattering does more damage to coherence, because a single Raman-scattered photon can flip the qubit (Chapter 09). In practice other heating sources usually dominate. Intensity noise at twice the trap frequency heats the atom parametrically, and pointing noise at the trap frequency shakes it. Collisions with background gas in the vacuum cell knock atoms out entirely, setting a trap lifetime of seconds to minutes depending on the vacuum.

## Light shifts of the qubit states

The trap shifts every level of the atom, and not all by the same amount.

**Differential shift of the hyperfine states.** The $F=2$ level sits 6.8 GHz above $F=1$, so its detuning from the D lines is slightly smaller and its light shift slightly larger. Writing the difference as a fraction $\eta$ of the trap depth, the two-line model gives $\eta=6.1\times10^{-5}$ at 1064 nm and $2.3\times10^{-4}$ at 852 nm. At $U_0/h=20.8$ MHz (1 mK) the qubit frequency is lowered by $\eta U_0/h=1.3$ kHz (1064 nm) or $4.7$ kHz (852 nm), because the upper state $|1\rangle$ is pulled down more. (The simpler rotating-wave estimate $\eta\approx\omega_{\rm hfs}/\Delta_{\rm eff}$, common in the literature, gives about 12% more at 1064 nm and 4% more at 852 nm; the counter-rotating terms included here reduce $\eta$.) That would be harmless if every atom felt the same intensity, but a warm atom samples different intensities as it moves, and atoms in different tweezers sit in slightly different depths. Chapter 09 shows that this sets the inhomogeneous coherence time $T_2^*$.

**Excited-state and vector shifts.** The $5P_{3/2}$ excited state couples to other states and is shifted differently from the ground state, so the cooling and imaging transitions of an atom in a tweezer are shifted by an amount comparable to the depth. Circular or elliptical polarization adds a **vector light shift** that acts like a magnetic field along the beam, splitting $m_F$ levels. Tweezers are therefore usually linearly polarized, and imaging is often done with the trap modulated or at carefully chosen detunings (Chapter 08).

**Magic wavelengths.** For some transitions there are wavelengths at which both levels shift equally, so the transition frequency is independent of the trap intensity. The best known example is the strontium clock transition, magic at 813.4 nm; optical-clock qubits trapped at that wavelength keep their coherence for a long time. Nuclear-spin qubits are insensitive for a different reason: their ground state has no electronic angular momentum ($J=0$; Chapter 09).

## Quantized motion

At microkelvin temperatures the atom's motion in the well is quantum mechanical. In the harmonic approximation each direction is a ladder of states $|n\rangle$ with energies $\hbar\omega(n+\tfrac12)$.

For the reference tweezer, $\hbar\omega_r/k_B=4.7\ \mu$K. An atom at $10\ \mu$K has a thermal mean occupation $\bar n=1/(e^{\hbar\omega/k_BT}-1)=1.7$ radially and $8.3$ axially, so only the lowest few levels are occupied. The ground-state wavefunction has an rms width $x_0=\sqrt{\hbar/2m\omega_r}=24$ nm radially, and the thermal cloud has an rms size of about 50 nm radially and 210 nm axially, all much smaller than the trap.

The ratio of the ground-state size $x_0$ to the reduced wavelength $\lambda/2\pi$ of the light is the **Lamb-Dicke parameter** $\eta_{LD}=kx_0$, which is 0.20 radially for one 780 nm photon. (For a two-photon Raman transition the relevant wavevector is the difference $\Delta k$ of the two beams, so $\eta_{LD}$ ranges from nearly 0 for co-propagating beams to about 0.39 for counter-propagating ones.) When $\eta_{LD}^2(2\bar n+1)\ll1$ (the **Lamb-Dicke regime**), absorbing or emitting a photon rarely changes $n$. Then a laser tuned one trap frequency below a narrow transition (the red sideband) drives $|n\rangle\to|n-1\rangle$, and optical pumping back to the start state usually keeps the new $n$. Each cycle removes one quantum, and $|n=0\rangle$ is dark to the red sideband, so the atom accumulates in the motional ground state. In tweezers this **Raman sideband cooling** uses a two-photon Raman transition between the hyperfine states as the narrow line.

![Two harmonic ladders of vibrational states labelled n = 0 to 4, one for the lower hyperfine state F = 1 and one for the upper state F = 2. Red arrows show red-sideband Raman pulses from F = 1, n to F = 2, n - 1, and a blue dashed arrow shows optical pumping back to F = 1 without changing n. A table lists the radial trap frequency 98.5 kHz, vibrational quantum 4.7 microkelvin, ground-state size 24 nm, Lamb-Dicke parameter 0.20 and mean n of 1.7 at 10 microkelvin](figures/07-sideband-cooling.png)

*Resolved-sideband cooling in a tweezer. Each cycle of a red-sideband pulse plus optical pumping removes one vibrational quantum. The motional ground state does not absorb on the red sideband, so population piles up there.*

Raman sideband cooling of single atoms in tweezers was demonstrated in 2012 to 2013: Kaufman, Lester and Regal prepared a Rb-87 atom in its three-dimensional vibrational ground state with about 90% probability, and Thompson et al. reached the radial ground state (mean occupation about 0.01) with a mean axial occupation of about 8 in a tweezer with a 900 nm waist. Ground-state cooling matters for Rydberg gates, whose errors grow with atomic motion (Chapter 11), and for experiments that use motion itself as a resource.

### Measuring the temperature: release and recapture

How do you take the temperature of *one* atom? Switch the tweezer off for some microseconds (tens of microseconds for a 1 mK trap), let the atom fly, switch it back on, and image it. Hot atoms move farther and are recaptured less often. Repeating many times gives a recapture probability versus release time, which is fitted with a Monte Carlo simulation of thermal atoms. [Lab 06](../hands-on/06-release-recapture/) simulates the measurement and fits a synthetic data set, recovering the input temperature within its statistical error.

## Worked example: designing a tweezer (illustrative numbers)

| Quantity | Formula | Value |
|---|---|---|
| wavelength, waist | | 1064 nm, 1.0 $\mu$m |
| polarizability | two-line model | 677 a.u. |
| depth per mW | $\alpha(2P/\pi w_0^2)/(2\varepsilon_0c)$ | **$k_B\times97\ \mu$K $=h\times2.02$ MHz** |
| power for 1 mK | | **10.3 mW** |
| Rayleigh range | $\pi w_0^2/\lambda$ | **2.95 $\mu$m** |
| trap frequencies at 1 mK | $\sqrt{4U_0/mw_0^2}$, $\sqrt{2U_0/mz_R^2}$ | **98.5 kHz, 23.6 kHz** |
| scattering at 1 mK | Grimm formula | **3.6 s$^{-1}$** |
| qubit differential shift at 1 mK | $\eta U_0/h$ | **1.3 kHz** |

**Step 1: intensity per mW.** $I_0=2(10^{-3})/(\pi\times10^{-12})=6.37\times10^8$ W/m$^2$.

**Step 2: depth.** $U_0=\alpha I_0/2\varepsilon_0c$ with $\alpha=677\times1.649\times10^{-41}=1.117\times10^{-38}$ C m$^2$/V gives $U_0=1.117\times10^{-38}\times6.37\times10^8/(2\times8.854\times10^{-12}\times2.998\times10^8)=1.34\times10^{-27}$ J, which is $k_B\times97\ \mu$K. A 1 mK trap needs $1000/97=10.3$ mW. Arrays of hundreds of such tweezers need watts of laser power, and high-power 1064 nm fibre amplifiers are the usual source.

**Step 3: frequencies.** $\omega_r=\sqrt{4\times1.381\times10^{-26}/(1.443\times10^{-25}\times10^{-12})}=6.19\times10^5$ rad/s, so $f_r=98.5$ kHz. With $z_R=2.95\ \mu$m, $f_z=f_r\,w_0/(\sqrt2z_R)=23.6$ kHz.

**Step 4: is it a good trap?** For an atom cooled to 10 to 15 $\mu$K by the sub-Doppler molasses of Chapter 06, $U_0/k_BT\approx70$ to 100; the recoil heating is below $k_B\times1\ \mu$K per second, and the scattering rate is a few per second. The weak point is the 1.3 kHz differential shift, which Chapter 09 turns into a coherence time.

## Run it

- [Lab 05](../hands-on/05-tweezer-trap/) computes the polarizability from 500 to 1200 nm, the depth, trap frequencies and scattering for 1064 and 852 nm tweezers, and checks the harmonic frequencies against the numerical curvature of the Gaussian well.
- [Lab 06](../hands-on/06-release-recapture/) simulates release-and-recapture thermometry and fits a synthetic data set.

## Common pitfalls

- **"Closer to resonance is always worse."** At fixed *power*, closer detuning gives a deeper trap; at fixed *depth*, it gives more scattering. Which matters depends on whether you are limited by laser power or by heating and coherence.
- **Ignoring the counter-rotating term.** At 1064 nm the counter-rotating term adds about 15% to the Rb polarizability ($1+(\omega_0-\omega)/(\omega_0+\omega)\approx1.15$). Use the full Lorentz form.
- **"$\omega_z=\omega_r$."** A single-beam tweezer is three to five times weaker axially. In many experiments the weak axial confinement is the bottleneck for cooling and for gate errors caused by motion.
- **Using the harmonic approximation for hot atoms.** It overestimates the restoring force away from the bottom and ignores that atoms with energy above $U_0$ escape.
- **"The qubit doesn't care about the trap."** Both hyperfine states shift by almost the same amount, but the small difference $\eta U_0$ is the leading dephasing mechanism for thermal atoms (Chapter 09).

## Key takeaways

- The ground-state polarizability of Rb-87 is positive (attractive) to the red of D1 and between D2 and the 790.03 nm tune-out wavelength, negative between the tune-out and D1 and to the blue of D2; at 1064 nm it is 677 a.u.
- A Gaussian focus with waist $w_0$ gives a well of depth $U_0=\alpha I_0/2\varepsilon_0c$ with $\omega_r=\sqrt{4U_0/mw_0^2}$ and $\omega_z=\sqrt{2U_0/mz_R^2}$.
- For 1064 nm and $w_0=1\ \mu$m: 97 $\mu$K per mW; at 1 mK, 98.5 kHz radially, 23.6 kHz axially, 3.6 scattered photons per second.
- The qubit states shift by slightly different amounts, $\eta U_0$ with $\eta\sim10^{-4}$, which limits coherence for warm atoms.
- Atomic motion in a tweezer is quantized; Raman sideband cooling in the Lamb-Dicke regime prepares the motional ground state, and release-and-recapture measures temperature.

## Go deeper

- R. Grimm, M. Weidemüller, Yu. B. Ovchinnikov, *Optical dipole traps for neutral atoms*, Adv. At. Mol. Opt. Phys. 42, 95 (2000), [arXiv:physics/9902072](https://arxiv.org/abs/physics/9902072). The polarizability, scattering and multilevel formulas of this chapter, and a survey of trap geometries.
- H. J. Metcalf and P. van der Straten, *Laser cooling and trapping of atoms*, J. Opt. Soc. Am. B 20, 887 (2003), [Utrecht preprint](https://webspace.science.uu.nl/~strat102/preprint/handpubl.pdf). Its discussion of quantized atomic motion in optical potentials and of dipole traps.
- A. M. Kaufman, B. J. Lester, C. A. Regal, *Cooling a single atom in an optical tweezer to its quantum ground state*, Phys. Rev. X 2, 041014 (2012), [arXiv:1209.2087](https://arxiv.org/abs/1209.2087).
- J. D. Thompson, T. G. Tiecke, A. S. Zibrov, V. Vuletić, M. D. Lukin, *Coherence and Raman sideband cooling of a single atom in an optical tweezer*, Phys. Rev. Lett. 110, 133001 (2013), [arXiv:1209.3028](https://arxiv.org/abs/1209.3028).
- A. M. Kaufman and K.-K. Ni, *Quantum science with optical tweezer arrays of ultracold atoms and molecules*, Nat. Phys. 17, 1324 (2021), [arXiv:2109.10087](https://arxiv.org/abs/2109.10087).

---

← Previous: [Sub-Doppler Cooling and the Magneto-Optical Trap](06-sub-doppler-mot.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [Loading, Imaging and Assembling Atom Arrays](08-arrays.md) →
