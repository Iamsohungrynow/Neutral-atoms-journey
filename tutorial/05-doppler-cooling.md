# 05 · Slowing and Doppler Cooling

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

Chapter 04 gave us a force, $F=\hbar k\gamma_p$, of up to ten thousand times gravity. Here we put it to two uses. **Slowing** uses one beam to bring a fast atomic beam down from hundreds of m/s to a few tens of m/s. The difficulty is that the Doppler shift changes as the atom slows, and the standard answer is the **Zeeman slower**. **Optical molasses** uses pairs of counter-propagating beams to make a velocity-dependent force, a friction, that cools atoms to about $150\ \mu$K. Weighing that friction against the heating from random photon kicks gives the **Doppler limit** $T_D=\hbar\Gamma/2k_B$. The material follows the first sections of Metcalf and van der Straten's review, the course's primary text for Part I.

> **Conventions.** $\delta=\omega_L-\omega_0$ (red: $\delta<0$). An atom with velocity $v$ moving *toward* a beam sees the light Doppler-shifted up by $kv$. For Rb, $k/2\pi=1/\lambda=1.282$ MHz per (m/s): an atom at 300 m/s sees the light shifted by 384 MHz, or 63 natural linewidths.

## The problem with slowing

Point a laser at an oncoming atomic beam. An atom at 300 m/s scatters photons only if the laser is tuned to its Doppler-shifted resonance, $\delta=-kv$, within about a linewidth $\Gamma/k=4.7$ m/s in velocity. After scattering a few hundred photons (each removing $v_r=5.9$ mm/s), it has slowed by a few m/s, drops out of resonance, and stops scattering. A fixed-frequency laser can only nibble a thin slice out of the velocity distribution.

There are two standard fixes:

- **Chirp the laser.** Sweep the laser frequency upward in time so that it follows the atoms as they slow. This works in pulses.
- **Shift the atom instead.** Keep the laser fixed and use a magnetic field to Zeeman-shift the atomic transition by exactly the amount the Doppler shift changes. This works continuously. It is the **Zeeman slower** (Phillips and Metcalf, 1982).

## The Zeeman slower

For the $\sigma^+$ cycling transition $|F{=}2,m_F{=}2\rangle\to|F'{=}3,m_F'{=}3\rangle$ the transition frequency shifts by $\mu'B/\hbar$ with $\mu'=(g_{F'}m_{F'}-g_Fm_F)\mu_B=(\tfrac23\cdot3-\tfrac12\cdot2)\mu_B=\mu_B$, that is 1.400 MHz per gauss. An atom at position $z$ with velocity $v$ therefore sees the effective detuning

$$\delta_{\rm eff}(z,v)=\delta_L+kv-\frac{\mu'B(z)}{\hbar}.$$

Now **design** the slower. Pick a constant deceleration $a=\eta\,a_{\max}$ with $0<\eta<1$, where $a_{\max}=\hbar k\Gamma/2m$. Under constant deceleration from $v_0$ the velocity is

$$v_d(z)=\sqrt{v_0^2-2az},$$

and the field that keeps such an atom on resonance ($\delta_{\rm eff}=0$) is

$$\boxed{\ B(z)=\frac{\hbar}{\mu'}\big[\delta_L+k\,v_d(z)\big]\ }$$

a field with a square-root profile. The slower ends where $v_d$ reaches the desired exit velocity $v_f$, after a length

$$L=\frac{v_0^2-v_f^2}{2\eta\,a_{\max}}.$$

![Top: schematic of a Zeeman slower; an oven on the left emits atoms through a tapered solenoid toward a MOT on the right, while a sigma-plus slowing laser red-detuned by 160 MHz travels in the opposite direction. Bottom: the designed magnetic field decreasing from +160 G at the entrance through zero near 55 cm to -87 G at the exit at 66 cm, with the design velocity falling from 300 to 30 m/s along the same curve](figures/05-zeeman-slower.png)

*The slower of lab 02: $v_0=300$ m/s, $v_f=30$ m/s, $\eta=0.6$, $\delta_L/2\pi=-160$ MHz. The field passes through zero (a "spin-flip" design) so that the coil currents stay moderate, and ends abruptly: beyond it, atoms at about 30 m/s are $20\Gamma$ off resonance and scatter hundreds of times more slowly than inside the slower.*

Three design choices deserve comment.

- **Why $\eta<1$?** The atom stays on the design curve only if the force can supply $ma$ somewhere near resonance. With saturation parameter $s_0$ the largest deceleration available is $a_{\max}\,s_0/(1+s_0)$, so $\eta$ must be below $s_0/(1+s_0)$. The force equals $ma$ at two detunings, one on each side of resonance, and only one of them is stable: the one where the atom is slightly *slower* than $v_d(z)$ (red-detuned in its own frame). If the atom gets slower still, it moves further from resonance, feels less force, and the resonance, sweeping down in velocity, catches it again. If it gets faster, it moves closer to resonance and is decelerated harder. In lab 02 the atom travels about 2.4 m/s slower than $v_d(z)$, as the force balance predicts.
- **What is captured?** Every atom with $v_f\lesssim v<v_0$ when it enters drifts until the resonance condition catches up with it, then locks on and exits at about $v_f$. Atoms faster than $v_0$ are never resonant and pass straight through. $v_0$ is the **capture velocity**.
- **Why red detuning?** With $\delta_L$ well to the red, atoms that have left the slower and slowed further are far off resonance, so the slowing beam does not push them back out of the MOT.

> **Intuition aside.** Think of the resonance condition as a velocity, $v_d(z)$, that falls steadily as the atom moves down the slower. An atom that enters slower than $v_0$ coasts until $v_d$ has come down to its speed, and from then on it is carried down with it. An atom that enters faster than $v_0$ is never resonant.

## Optical molasses

Slowing reduces the mean velocity; cooling reduces the *spread*. For that we need a force that depends on velocity and always opposes it. Take two counter-propagating beams of the same red detuning $\delta$ and intensity $s_0$, along $+z$ and $-z$. An atom moving with velocity $v$ along $+z$ sees the $-z$ beam (which it moves toward) shifted closer to resonance, $\delta+kv$, and the $+z$ beam shifted further away, $\delta-kv$. Treating the beams independently ($s_0\ll1$),

$$F(v)=\hbar k\frac{\Gamma}{2}\left[\frac{s_0}{1+s_0+\big(\frac{2(\delta-kv)}{\Gamma}\big)^2}-\frac{s_0}{1+s_0+\big(\frac{2(\delta+kv)}{\Gamma}\big)^2}\right].$$

Expanding for $kv\ll\Gamma$ gives a friction force $F=-\beta v$ with

$$\boxed{\ \beta=-\frac{8\hbar k^2\,\delta\,s_0}{\Gamma\big[1+s_0+(2\delta/\Gamma)^2\big]^2}\ }$$

which is positive (a true damping) only for red detuning. Three pairs of beams along $x$, $y$, $z$ damp motion in all directions: atoms in the overlap region move as if through a viscous fluid, hence "optical molasses" (Chu and co-workers, 1985).

![Left: force versus atom velocity at detuning minus Gamma with s0 = 1 per beam; the beam along +z pushes positive with a peak near -4.7 m/s, the beam along -z pushes negative with a peak near +4.7 m/s, and their sum is a dispersion-shaped curve passing through zero with negative slope. Right: the total force for detunings -0.5, -1 and -2 Gamma; larger detuning gives a smaller slope (weaker friction) at v = 0 but a wider capture range](figures/05-molasses-force.png)

*The molasses force for Rb-87. Each beam alone pushes atoms along its own direction; together they cancel for atoms at rest and oppose any motion. The force is close to linear (pure friction) only for $kv$ well below $|\delta|$: for these curves it stays within 10% of $-\beta v$ up to about 1.5 m/s at $\delta=-\Gamma/2$ and 2.5 m/s at $\delta=-\Gamma$. It peaks near $v\approx|\delta|/k$ (2.4 and 4.7 m/s), and faster atoms are still slowed, but more weakly. Larger detuning trades friction strength for capture range.*

## The Doppler limit

If friction were the whole story, atoms would cool to zero velocity. They do not, because each scattering event is a random kick (Chapter 04). Here is the balance in its simplest, one-dimensional form, the model used in lab 03.

Friction removes kinetic energy at the rate $\frac{d}{dt}\langle\tfrac12mv^2\rangle=-\beta\langle v^2\rangle$.

The heating comes from the scattering itself. Each beam scatters at rate $R_0=\frac{\Gamma}{2}\frac{s_0}{1+s_0+(2\delta/\Gamma)^2}$ for an atom near rest. Every event has two random kicks of $\pm\hbar k$: the absorption (random because the atom does not know which beam it will absorb from next) and the emission (along $\pm z$ with equal probability in this 1D model). The momentum spread therefore grows as $\frac{d}{dt}\langle p^2\rangle=2R_0\times2(\hbar k)^2$, so the kinetic energy grows at $\frac{d}{dt}\langle\tfrac12mv^2\rangle=2R_0\hbar^2k^2/m$.

In steady state the two rates cancel. Using $k_BT=m\langle v^2\rangle$ in one dimension,

$$k_BT=\frac{2R_0\hbar^2k^2}{\beta}=\frac{\hbar\Gamma}{4}\,\frac{1+s_0+(2\delta/\Gamma)^2}{2|\delta|/\Gamma}.$$

At low intensity this is smallest at $\delta=-\Gamma/2$, giving the **Doppler limit**

$$\boxed{\ k_BT_D=\frac{\hbar\Gamma}{2}\ },\qquad T_D=\frac{(1.0546\times10^{-34})(3.812\times10^7)}{2(1.381\times10^{-23})}=145.6\ \mu{\rm K}\ \text{for Rb-87}.$$

The emission model matters. With a single beam pair and isotropic emission, each emission kick contributes only $(\hbar k)^2/3$ along the axis and the result is $\tfrac23$ of the formula above. With three beam pairs, though, photons scattered from all six beams feed random kicks into every axis, and for isotropic emission the low-intensity limit comes out at exactly $\hbar\Gamma/2$ again, which is the value usually quoted. It depends on nothing but $\Gamma$, so narrower lines give colder limits. The intercombination line of strontium (689 nm, $\Gamma/2\pi=7.4$ kHz) cools to below a microkelvin, and that of ytterbium (556 nm, 182 kHz) has $T_D=4.4\ \mu$K (Chapter 02). For strontium the Doppler limit (0.18 $\mu$K) is even below the recoil temperature (0.46 $\mu$K), and there the recoil sets the floor instead.

![Doppler temperature of Rb-87 versus detuning for s0 = 0, 0.5 and 2 per beam. The s0 = 0 curve has its minimum of 145.6 microkelvin at delta = -Gamma/2, rising steeply toward zero detuning and linearly at large detuning; higher intensity raises the curve and moves its minimum to larger detuning](figures/05-doppler-temperature.png)

*The Doppler theory's prediction. Too close to resonance, the friction vanishes; too far, the atoms barely scatter, and the friction falls faster than the heating. Increasing the intensity raises the temperature, because friction and heating both grow but the friction saturates first. Lab 03 reproduces the $s_0=0.05$ curve with an event-by-event simulation of photon kicks.*

### The surprise of 1988

When Lett and co-workers measured the temperature of sodium in optical molasses carefully, they found $43\pm20\ \mu$K, several times **below** sodium's Doppler limit of about $240\ \mu$K. The theory above is correct for a two-level atom; real atoms have several ground-state sublevels, and polarization gradients in the light field add a far more efficient cooling mechanism, which Chapter 06 describes.

## Worked example (Rb-87, illustrative numbers)

| Quantity | Formula | Value |
|---|---|---|
| Doppler shift at 300 m/s | $v/\lambda$ | 384 MHz $=63\,\Gamma$ |
| slower length ($v_0=300$, $v_f=30$ m/s, $\eta=0.6$) | $(v_0^2-v_f^2)/2\eta a_{\max}$ | **0.66 m** |
| field range | $(v_0-v_f)/(\lambda\times1.400\ {\rm MHz/G})$ | **247 G** |
| time in the slower | $(v_0-v_f)/\eta a_{\max}$ | **4.0 ms** |
| photons scattered | $(v_0-v_f)/v_r$ | **46 000** |
| molasses friction ($\delta=-\Gamma/2$, $s_0=0.5$) | $\beta=4\hbar k^2s_0/(2+s_0)^2$ | **$2.2\times10^{-21}$ kg/s** |
| velocity damping time | $m/\beta$ | **66 $\mu$s** |
| molasses temperature at that setting | $(\hbar\Gamma/4)(2+s_0)/k_B$ | **182 $\mu$K** |
| rms velocity at $T_D$ | $\sqrt{k_BT_D/m}$ | **11.8 cm/s $=20\,v_r$** |

**Step 1: the slower.** $L=(300^2-30^2)/(2\times0.6\times1.122\times10^5)=89\,100/134\,600=0.66$ m. The field must sweep the transition by $(300-30)\times1.282=346$ MHz, which at 1.400 MHz/G is 247 G. Lab 02 shows that the designed field, $+160$ G to $-87$ G, does exactly that.

**Step 2: friction.** With $\hbar k^2=6.84\times10^{-21}$ kg/s, $\delta=-\Gamma/2$ and $s_0=0.5$: $\beta=4\times0.5/2.5^2\times6.84\times10^{-21}=2.2\times10^{-21}$ kg/s, so a velocity decays in $m/\beta=1.443\times10^{-25}/2.2\times10^{-21}=66\ \mu$s.

**Step 3: temperature.** At this intensity the 1D formula gives $(2.5/2)\,T_D=182\ \mu$K, 25% above the low-intensity limit. Real experiments compromise, since higher intensity captures more atoms and lower intensity cools further.

**Step 4: is the Doppler limit cold enough for a tweezer?** A 1 mK tweezer holds an atom at $146\ \mu$K easily ($k_BT/U_0\approx0.15$). But the atom's motion would then be spread over many vibrational levels, and Chapter 09 shows that its temperature directly limits qubit coherence. Sub-Doppler cooling (Chapter 06) brings this down by another order of magnitude.

## Run it

- [Lab 02](../hands-on/02-zeeman-slower/) designs the slower above, flies atoms of different initial speeds through it, and checks the capture velocity, the exit velocity and the lag predicted by the force balance.
- [Lab 03](../hands-on/03-doppler-molasses/) simulates molasses photon by photon, measures the friction coefficient from the decay of the mean velocity, and recovers the temperature-versus-detuning curve and the Doppler limit within statistical error.

## Common pitfalls

- **"Molasses traps atoms."** It does not. There is friction but no force toward any point, so atoms in molasses slowly diffuse away. Trapping needs a position-dependent force, which the MOT adds (Chapter 06).
- **"Closer to resonance cools better."** The friction coefficient vanishes on resonance and the force heats for blue detuning. The optimum for Doppler cooling is $\delta=-\Gamma/2$ at low intensity.
- **"The Doppler limit is a fundamental limit."** It is a limit of the two-level model. Multilevel atoms cool far below it (Chapter 06), and the recoil temperature $T_r=362$ nK is the next natural scale.
- **Slower capture versus oven speed.** In an effusive beam from an oven at 400 K the most probable speed is $\sqrt{3k_BT/m}\approx340$ m/s, so a large fraction of atoms is above 300 m/s and is not captured. Increasing $v_0$ captures more atoms but needs a longer slower or a larger $\eta$.
- **Transverse heating.** Photon kicks spread the slowed beam sideways (by about the random-walk $\sqrt N$ of Chapter 04), so slowed atoms diverge. Real setups often add transverse cooling or use a 2D MOT instead of a slower.

## Key takeaways

- The Doppler shift changes as atoms slow; a Zeeman slower compensates with a square-root field profile $B(z)=\frac{\hbar}{\mu'}[\delta_L+kv_d(z)]$ and captures all atoms slower than $v_0$.
- Two red-detuned counter-propagating beams give a friction force $F=-\beta v$ with $\beta=-8\hbar k^2\delta s_0/\Gamma(1+s_0+(2\delta/\Gamma)^2)^2$.
- Random photon kicks heat the atoms; the balance gives $k_BT=\frac{\hbar\Gamma}{4}\frac{1+s_0+(2\delta/\Gamma)^2}{2|\delta|/\Gamma}$, minimal at $\delta=-\Gamma/2$: the Doppler limit $T_D=\hbar\Gamma/2k_B=145.6\ \mu$K for Rb-87.
- Molasses damps velocities in tens of microseconds but does not trap.
- Real atoms beat the Doppler limit because of their multilevel structure (Chapter 06).

## Go deeper

- H. J. Metcalf and P. van der Straten, *Laser cooling and trapping of atoms*, J. Opt. Soc. Am. B 20, 887 (2003), [Utrecht preprint](https://webspace.science.uu.nl/~strat102/preprint/handpubl.pdf). The sections on slowing atomic beams and on optical molasses follow this chapter's logic, including the friction coefficient and the Doppler limit.
- W. D. Phillips and H. J. Metcalf, *Laser deceleration of an atomic beam*, Phys. Rev. Lett. 48, 596 (1982). The first Zeeman slower.
- S. Chu, L. Hollberg, J. E. Bjorkholm, A. Cable, A. Ashkin, *Three-dimensional viscous confinement and cooling of atoms by resonance radiation pressure*, Phys. Rev. Lett. 55, 48 (1985). The first optical molasses.
- P. D. Lett et al., *Observation of atoms laser cooled below the Doppler limit*, Phys. Rev. Lett. 61, 169 (1988). The measurement that broke the two-level theory.
- D. J. Wineland and W. M. Itano, *Laser cooling of atoms*, Phys. Rev. A 20, 1521 (1979). A thorough early theory of Doppler cooling, including the limit.

---

← Previous: [Optical Forces: Radiation Pressure and the Dipole Force](04-optical-forces.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [Sub-Doppler Cooling and the Magneto-Optical Trap](06-sub-doppler-mot.md) →
