# 04 · Optical Forces: Radiation Pressure and the Dipole Force

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

Light pushes on atoms in two quite different ways. The **scattering force** (radiation pressure) comes from absorbing photons out of a beam and re-emitting them in random directions; every absorption is a kick along the beam. The **dipole force** comes from the energy shift the light field imprints on the atom. The shift grows with the intensity, so the atom is pushed toward lower energy, into the light if the shift is negative and out of it if positive. The scattering force is dissipative, and laser *cooling* (Chapters 05 and 06) relies on it. The dipole force is conservative and is what holds atoms in optical traps (Chapter 07). Both follow from the two-level atom of Chapter 03, and comparing their sizes tells us why a tweezer is tuned far from resonance.

## Photon momentum and recoil

A photon of wavelength $\lambda$ carries momentum $\hbar k=h/\lambda$. When a Rb-87 atom absorbs a 780 nm photon its velocity changes by the **recoil velocity**

$$v_r=\frac{\hbar k}{m}=\frac{6.626\times10^{-34}\ {\rm J\,s}}{(780.24\times10^{-9}\ {\rm m})(1.443\times10^{-25}\ {\rm kg})}=5.885\ {\rm mm/s},$$

and gains the **recoil energy** $E_r=\hbar^2k^2/2m=h\times3.771$ kHz. Both are tiny. An atom from a room-temperature vapour moves 50 000 times faster than $v_r$. What makes the force large is the *rate*, since an atom can repeat the absorption-emission cycle up to $\Gamma/2\approx1.9\times10^7$ times per second.

## The scattering force

Put an atom in a single travelling-wave beam along $+z$. Each absorbed photon gives $+\hbar k$ along $z$. Each spontaneously emitted photon gives a kick of the same size in a random direction, which **averages to zero** over many cycles. The mean force is therefore momentum per photon times photons per second:

$$\boxed{\ F_{\rm sp}=\hbar k\,\gamma_p=\hbar k\,\frac{\Gamma}{2}\,\frac{s_0}{1+s_0+(2\delta/\Gamma)^2}\ }$$

using the scattering rate from Chapter 03. Its maximum, at high intensity on resonance, is

$$F_{\max}=\frac{\hbar k\Gamma}{2}=1.62\times10^{-20}\ {\rm N},\qquad a_{\max}=\frac{F_{\max}}{m}=1.12\times10^5\ {\rm m/s^2}\approx1.1\times10^4\,g .$$

A beam of a few milliwatts can therefore push with ten thousand times the force of gravity, enough to stop a thermal atomic beam in well under a metre (Chapter 05).

![Left: scattering force in units of hbar k Gamma over 2 versus detuning for saturation parameters 0.1, 1 and 10; Lorentzian peaks of height 0.09, 0.5 and 0.91 that broaden with intensity, below a dashed line at the maximum 1.6e-20 newton. Right: rotating-frame energies versus detuning in units of Omega; the bare ground (zero) and excited (minus hbar delta) lines cross at zero detuning, the exact dressed states avoid each other, and for red detuning the ground-like state is pushed down by Omega squared over four times the magnitude of delta](figures/04-forces.png)

*Left: the scattering force has the Lorentzian shape of the scattering rate and always points along the beam. Right: the origin of the dipole force. In the rotating frame the laser couples $|g\rangle$ (energy 0) and $|e\rangle$ (energy $-\hbar\delta$); the coupled "dressed" states repel. For red detuning the ground-like state is pushed down.*

### The cost: heating from random kicks

The emitted photons do not cancel exactly in any one realisation. Their kicks add like a **random walk**: after $N$ emissions along random directions the spread in momentum along $z$ grows as $\hbar k\sqrt{N/3}$ (the $1/3$ is $\langle\cos^2\theta\rangle$ for isotropic emission). The absorptions are random in time too. Both effects heat the atom. As a rule of thumb, each scattering event raises the atom's random (thermal) kinetic energy by about $2E_r$, one $E_r$ from the absorption kick and one from the emission kick. Chapter 05 shows that Doppler cooling is a competition between the mean force (cooling) and this random walk (heating), and the balance sets the lowest temperature.

![Left: six simulated momentum trajectories, each the momentum along the beam minus N hbar k, wandering randomly for up to 2000 scattered photons; dashed curves mark the rms spread plus or minus root N over 3. Right: the mean momentum of 400 simulated atoms follows the line N hbar k](figures/04-random-walk.png)

*Simulation of 400 atoms scattering 2000 photons each from a beam along $+z$. The mean momentum (right) grows by $\hbar k$ per photon, which is the scattering force. Individual atoms wander about that mean by $\sim\hbar k\sqrt{N/3}$ (left), and this spread is the heating.*

## The dipole force

Now tune the laser far from resonance, $|\delta|\gg\Gamma$. Absorption becomes rare, but the atom's energy levels are still shifted by the light. The rotating-frame Hamiltonian of Chapter 03,

$$\frac{\hat H}{\hbar}=\begin{pmatrix}0&\Omega/2\\ \Omega/2&-\delta\end{pmatrix},$$

has eigenvalues $E_\pm/\hbar=-\delta/2\pm\frac12\sqrt{\delta^2+\Omega^2}$. For $|\delta|\gg\Omega$ the state that connects to $|g\rangle$ is shifted by

$$\boxed{\ \Delta E_g=\frac{\hbar\Omega^2}{4\delta}\ }$$

the **light shift** (or AC Stark shift). It has the sign of $\delta$: red-detuned light ($\delta<0$) **lowers** the ground state, blue-detuned light raises it. Because $\Omega^2\propto I$, the shift is proportional to the local intensity. An atom in a beam whose intensity varies in space therefore sees a potential $U(\mathbf r)=\Delta E_g(\mathbf r)$ and feels a force

$$\mathbf F_{\rm dip}=-\nabla U=-\frac{\hbar}{4\delta}\nabla\Omega^2(\mathbf r).$$

- **Red detuning**: $U<0$ where the light is bright, so atoms are pulled toward intensity maxima. A focused red-detuned beam therefore traps atoms at its focus; an optical tweezer is such a beam.
- **Blue detuning**: atoms are pushed out of the light, toward intensity minima.

For a two-level atom at rest in steady state there is a formula valid at all intensities, $U=\frac{\hbar\delta}{2}\ln\!\big[1+\frac{s_0}{1+(2\delta/\Gamma)^2}\big]$. It reduces to $\hbar\Omega^2/4\delta$ when $|\delta|\gg\Gamma$ and $s_0\ll(2\delta/\Gamma)^2$.

> **Intuition aside.** Go back to the classical electron on a spring. Driven below resonance it oscillates in phase with the field, so its induced dipole lines up with the field and the energy $-\frac12\mathbf d\cdot\mathbf E$ is negative. The atom is then drawn toward strong fields, for the same reason that scraps of paper are pulled toward a charged comb. Above resonance the dipole oscillates out of phase and the atom is pushed away.

## Why traps are tuned far off resonance

Compare the two effects at large detuning. The potential and the scattering rate are

$$U\simeq\frac{\hbar\Omega^2}{4\delta}\propto\frac{I}{\delta},\qquad \gamma_p\simeq\frac{\Gamma\Omega^2}{4\delta^2}\propto\frac{I}{\delta^2},\qquad\text{so}\qquad \hbar\gamma_p=\frac{\Gamma}{|\delta|}\,|U| .$$

At a fixed trap depth, the scattering rate falls as $1/|\delta|$. Tweezers are therefore tuned far from resonance, and the depth lost by detuning is made up with more laser power.

![Left: dipole potential across a 1 milliwatt beam focused to a 10 micrometre waist, at plus and minus 50 GHz detuning; red detuning gives a well 1.68 millikelvin deep at the centre, blue detuning a hill of the same height. Right: the photon scattering rate for the red-detuned case, a Gaussian peaking at 2.7e4 photons per second](figures/04-dipole-potential.png)

*A near-resonant dipole trap: 1 mW at 50 GHz red detuning makes a 1.7 mK well, but the atom scatters $2.7\times10^4$ photons per second and is heated out in a fraction of a second. Chapter 07 shows that moving to 1064 nm (about 100 THz from resonance) brings the scattering at the same depth down to a few photons per second.*

## Worked example: a near-resonant dipole trap (illustrative numbers)

This example treats the atom as the two-level cycling transition driven with $\sigma^+$ light, so it uses $I_{\rm sat}=1.669$ mW/cm$^2$. For linearly polarized light the effective coupling is weaker and the depth and scattering rate come out about $2/3$ as large.

| Symbol | Meaning | Value |
|---|---|---|
| $P$, $w_0$ | beam power and waist | 1.0 mW, 10 $\mu$m |
| $I_0=2P/\pi w_0^2$ | peak intensity | 637 W/cm$^2$ (computed) |
| $s_0=I_0/I_{\rm sat}$ | peak saturation parameter | $3.8\times10^5$ (computed) |
| $\Omega/2\pi$ | peak Rabi frequency | 2.65 GHz (computed) |
| $\delta/2\pi$ | detuning from D2 | $-50$ GHz |
| $U_0$ | trap depth | **$h\times35.1$ MHz $=k_B\times1.68$ mK** (computed) |
| $\gamma_p$ | scattering rate at the centre | **$2.7\times10^4$ s$^{-1}$** (computed) |
| $t_{\rm heat}$ | time to heat by $U_0$ | **$\approx0.17$ s** (computed) |

**Step 1: intensity.** $I_0=2(10^{-3})/(\pi\times10^{-10})=6.37\times10^6\ {\rm W/m^2}=637\ {\rm W/cm^2}$, so $s_0=637/(1.669\times10^{-3})=3.8\times10^5$. A huge saturation parameter, but at $|\delta|\approx8200\,\Gamma$ the atom is barely excited.

**Step 2: Rabi frequency.** $\Omega=\Gamma\sqrt{s_0/2}=2\pi\times6.0666\ {\rm MHz}\times437=2\pi\times2.65$ GHz. Check that $\Omega\ll|\delta|$: $2.65/50=0.053$, fine.

**Step 3: depth.** $U_0/h=\Omega^2/(4|\delta|)/2\pi=(2.65\ {\rm GHz})^2/(4\times50\ {\rm GHz})=35.1$ MHz. In temperature units, $U_0/k_B=h(35.1\times10^6)/k_B=1.68$ mK. The exact dressed-state energy gives 35.06 MHz, confirming the perturbative formula.

**Step 4: scattering.** $\gamma_p=(\Gamma/|\delta|)(U_0/\hbar)=(6.0666/50\,000)\times2\pi\times35.1\times10^6\ {\rm s^{-1}}=2.7\times10^4\ {\rm s^{-1}}$.

**Step 5: heating time.** At $2E_r=k_B\times362$ nK per photon, the atom gains $k_B\times9.7$ mK per second, so it climbs out of the 1.68 mK well in about 0.17 s. A qubit has to be held for seconds, so this is far too fast, and it is why real tweezers are detuned by many terahertz (Chapter 07).

## Comparing the two forces

| | Scattering force | Dipole force |
|---|---|---|
| Origin | absorption followed by spontaneous emission | energy shift of the dressed ground state |
| Direction | along the beam | along the intensity gradient |
| Scales as | $\gamma_p$, maximal near resonance, saturates at $\hbar k\Gamma/2$ | $I/\delta$, does not saturate in the same way |
| Conservative? | no: dissipative (cooling is possible) | yes: a potential (trapping is possible) |
| Heating | intrinsic to the force | only via residual scattering $\propto I/\delta^2$ |
| Used for | slowing, molasses, MOT, imaging | tweezers, lattices, dipole traps |

## Common pitfalls

- **"A tweezer holds atoms with radiation pressure."** A single focused beam pushes atoms *along* the beam through scattering; the tweezer holds them through the dipole force, and works best where scattering is negligible.
- **"Blue light can't trap."** Blue-detuned light repels atoms, but a dark spot surrounded by light (a "bottle beam") or a blue-detuned lattice can trap them at intensity minima, where they also scatter less.
- **Sign of the light shift.** With $\delta=\omega_L-\omega_0$, the ground state shifts by $+\hbar\Omega^2/4\delta$: negative for red. In the two-level model the excited state shifts by the same amount in the opposite direction. In a real Rb tweezer the $5P_{3/2}$ shift has its own size, set by its couplings to other states (Chapter 07), which matters for imaging atoms in a tweezer (Chapter 08).
- **Two-level formulas at large detuning.** Once $|\delta|$ approaches the fine-structure splitting (7 THz for Rb) the D1 and D2 lines both contribute, and at still larger detuning (for example a 1064 nm tweezer, 100 THz away) the counter-rotating terms matter too. Chapter 07 uses the full two-line polarizability.
- **"Emission kicks cancel, so they don't matter."** Their mean is zero, but their *variance* grows with every photon, and this random walk is the heating that limits Doppler cooling.

## Key takeaways

- Each photon changes a Rb atom's velocity by $v_r=5.9$ mm/s; scattering at up to $\Gamma/2$ gives forces up to $\hbar k\Gamma/2$, about $10^4\,g$.
- The scattering force $F=\hbar k\gamma_p$ is dissipative and points along the beam; the random emission kicks heat the atom by about $2E_r$ per photon.
- The dipole force comes from the light shift $\hbar\Omega^2/4\delta$: red detuning attracts atoms to intense light, blue detuning repels them.
- At large detuning, $U\propto I/\delta$ while $\gamma_p\propto I/\delta^2$, so $\hbar\gamma_p=(\Gamma/|\delta|)U$: traps are made far off resonance.

## Go deeper

- H. J. Metcalf and P. van der Straten, *Laser cooling and trapping of atoms*, J. Opt. Soc. Am. B 20, 887 (2003), [Utrecht preprint](https://webspace.science.uu.nl/~strat102/preprint/handpubl.pdf). Its opening section on optical forces derives the radiative and dipole forces in closely related notation (it writes $\gamma$ for $\Gamma$).
- R. Grimm, M. Weidemüller, Yu. B. Ovchinnikov, *Optical dipole traps for neutral atoms*, Adv. At. Mol. Opt. Phys. 42, 95 (2000), [arXiv:physics/9902072](https://arxiv.org/abs/physics/9902072). The standard reference for the dipole potential and the $\Gamma/\delta$ scattering argument; Chapter 07 follows it.
- A. Ashkin, *Trapping of atoms by resonance radiation pressure*, Phys. Rev. Lett. 40, 729 (1978). An early proposal to trap atoms with light forces.
- C. J. Foot, *Atomic Physics* (Oxford University Press, 2005), chapter 9. A textbook treatment of both forces.

---

← Previous: [A Two-Level Atom in a Laser Field](03-atom-light.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [Slowing and Doppler Cooling](05-doppler-cooling.md) →
