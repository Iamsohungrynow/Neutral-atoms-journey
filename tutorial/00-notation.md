# Before you start: notation, units and reference numbers

This course uses one reference atom, **rubidium-87**, all the way through, so
the numbers in different chapters can be compared directly. Read this page once
and keep it open beside your editor. Every number in the table below is
recomputed by [`tutorial/figures/atomdata.py`](figures/atomdata.py); if a chapter
and this page ever disagree, this page and that script win.

## Sign conventions

| Symbol | Definition | Note |
|---|---|---|
| $\delta=\omega_L-\omega_0$ | laser detuning from an optical transition | **red** detuning means $\delta<0$ (laser below resonance). Same convention as Metcalf and van der Straten |
| $\Gamma$ | natural linewidth = spontaneous decay rate of the excited state, in rad/s | quoted as $\Gamma/2\pi$ in Hz. Lifetime $\tau=1/\Gamma$ |
| $\Omega$ | Rabi frequency (angular), $\hbar\Omega=-\langle e\vert\hat{\mathbf d}\cdot\mathbf E_0\vert g\rangle$ | the population oscillates as $\sin^2(\Omega t/2)$ on resonance |
| $s_0=I/I_{\rm sat}=2\Omega^2/\Gamma^2$ | on-resonance saturation parameter | $I_{\rm sat}=\pi hc\Gamma/(3\lambda^3)$ for a cycling transition |
| $\gamma_p=\dfrac{\Gamma}{2}\dfrac{s_0}{1+s_0+(2\delta/\Gamma)^2}$ | photon scattering rate | saturates at $\Gamma/2$ |
| $U_0>0$ | depth of an optical trap (a positive energy) | the potential itself is $U(\mathbf r)=-U_0\,e^{-2r^2/w^2}$ for a red-detuned Gaussian focus |
| $\Delta=\omega_L-\omega_{gr}$ | detuning of the Rydberg laser(s) from the ground-Rydberg transition | the Rydberg Hamiltonian is $H/\hbar=\sum_i\frac{\Omega}{2}\sigma^x_i-\Delta\sum_i n_i+\sum_{i<j}\frac{V_{ij}}{\hbar}n_in_j$ with $n_i=\vert r\rangle\langle r\vert_i$ |
| $V(R)=C_6/R^6$ | van der Waals interaction of two Rydberg atoms | $C_6>0$ means repulsive. (The ARC library prints the opposite sign; we convert) |
| $\vert0\rangle,\vert1\rangle$ | hyperfine "clock" qubit $\vert F{=}1,m_F{=}0\rangle$, $\vert F{=}2,m_F{=}0\rangle$ | in the gate chapter only $\vert1\rangle$ couples to the Rydberg state $\vert r\rangle$ |

Two traps for the unwary:

- **Recoil temperature.** We follow Steck and define $T_r=\hbar^2k^2/(m k_B)$.
  Some books use half of that, $\hbar^2k^2/(2mk_B)=E_r/k_B$. Always check which.
- **"Linewidth" and "Rabi frequency".** Both are angular frequencies in formulas
  and are quoted in ordinary frequency units in text: "$\Gamma=2\pi\times6.07$ MHz"
  means $\Gamma=3.81\times10^7\ \mathrm{s^{-1}}$.

## Units in the code

| Context | Units |
|---|---|
| Laser cooling, trapping, imaging labs (01 to 08) | SI throughout (m, s, kg, J, K), printed in convenient multiples |
| Coherent dynamics labs (09 to 12) | time in microseconds, frequency in MHz, angular quantities in rad/us, e.g. `Omega = 2*np.pi*2.0` means $\Omega/2\pi=2$ MHz |
| Hamiltonians in the dynamics scripts | actually $H/\hbar$ in rad/us |
| Temperatures | printed in uK; stored in K |

## Reference data: rubidium-87

D-line data follow D. A. Steck, *Rubidium 87 D Line Data*
([steck.us/alkalidata](https://steck.us/alkalidata)). Rydberg numbers were
computed with the open-source [ARC](https://github.com/nikolasibalic/ARC-Alkali-Rydberg-Calculator)
library. Tweezer numbers use the simple two-line (D1 + D2) polarizability of
Chapter 07, which agrees with ARC's full sum over states to about 1% at 1064 nm.

### Atom and laser cooling

| Quantity | Value |
|---|---|
| mass $m$ | 86.909 u $=1.443\times10^{-25}$ kg |
| D2 line $5S_{1/2}\to5P_{3/2}$ | $\lambda=780.241$ nm, $\Gamma/2\pi=6.0666$ MHz, $\tau=26.24$ ns |
| D1 line $5S_{1/2}\to5P_{1/2}$ | $\lambda=794.979$ nm, $\Gamma/2\pi=5.750$ MHz, $\tau=27.68$ ns |
| ground hyperfine splitting | $6.834\,682\,611$ GHz |
| saturation intensity (cycling $F{=}2\to F'{=}3$, $\sigma^\pm$) | $1.669$ mW/cm$^2$ |
| Doppler temperature $T_D=\hbar\Gamma/2k_B$ | $145.6\ \mu$K |
| recoil velocity $v_r=\hbar k/m$ | $5.885$ mm/s |
| recoil temperature $T_r=\hbar^2k^2/mk_B$ | $362$ nK |
| recoil energy $E_r=\hbar^2k^2/2m$ | $h\times3.771$ kHz |
| maximum scattering deceleration $a_{\max}=\hbar k\Gamma/2m$ | $1.12\times10^5$ m/s$^2$ $\approx1.1\times10^4\,g$ |
| shortest stopping distance from 300 m/s, $v^2/2a_{\max}$ | 0.40 m |

### A single optical tweezer (illustrative design)

| Quantity | Value |
|---|---|
| ground-state polarizability at 1064 nm / 852 nm | $\approx677$ / $\approx2070$ atomic units |
| depth per mW, 1064 nm, waist $w_0=1.0\ \mu$m | $k_B\times97\ \mu$K $=h\times2.0$ MHz |
| power for $U_0=k_B\times1$ mK at 1064 nm, $w_0=1\ \mu$m | 10.3 mW |
| trap frequencies at that depth | radial 98 kHz, axial 24 kHz (Rayleigh range 2.95 $\mu$m) |
| photon scattering rate at that depth | $\approx3.6\ \mathrm{s^{-1}}$ |
| Lamb-Dicke parameter, 780 nm light, radial | 0.20 |
| mean radial vibrational number at 10 $\mu$K | $\approx1.7$ |
| differential light shift $\eta$ (fraction of depth) | $6.1\times10^{-5}$ at 1064 nm, $2.3\times10^{-4}$ at 852 nm |

### Rydberg excitation

| Quantity | Value |
|---|---|
| two-photon ladder | $5S_{1/2}\xrightarrow{420.30\,\rm nm}6P_{3/2}\xrightarrow{1012.8\,\rm nm}nS_{1/2}$ (here $n=70$) |
| $70S_{1/2}$ effective quantum number $n^*=n-\delta_\ell$ | 66.87 |
| $70S_{1/2}$ lifetime at 0 K / 300 K | 374 $\mu$s / 147 $\mu$s |
| van der Waals coefficient $C_6/h$ ($70S+70S$) | $+863$ GHz $\mu$m$^6$ (repulsive) |
| blockade radius $R_b=(C_6/\hbar\Omega)^{1/6}$ at $\Omega/2\pi=2$ MHz | 8.7 $\mu$m |

The tweezer and Rydberg tables are **teaching values**, chosen to be typical.
Real experiments use other wavelengths, waists, powers and Rydberg states;
always recompute for your own parameters.

## What makes a simulation trustworthy?

1. Predict a limiting case before running: no light, no interaction, zero temperature.
2. Compare a numerical result with an independent analytic formula.
3. For Monte Carlo results, compare with the expected value **within its
   statistical error** ($\sigma/\sqrt N$), not to many digits.
4. Separate numerical convergence from physical validity. A perfectly converged
   two-level model cannot predict sub-Doppler cooling, which needs several
   ground sublevels.
5. Check that the observable answers the question. A Rydberg gate that returns
   every atom to the qubit subspace is not yet a CZ gate; its conditional phase
   must also be $\pi$.

Every lab encodes checks of these kinds; the [lab runner](../hands-on/README.md)
fails if any of them do not hold.

[Start the learning path](learning-path.md) · [Chapter index](README.md)
