# 02 · The Atom: Levels, Fine and Hyperfine Structure

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

Before we can cool, trap or compute with an atom, we need to know its energy levels, because every laser in the experiment is tuned to one particular transition. We build up the levels of rubidium-87 one energy scale at a time. Which shell the outer electron occupies sets the **gross structure**, in electron-volts. Spin-orbit coupling splits the $5p$ level (but not the $5s$ ground state) into two **fine-structure** components 7 THz apart, and the nuclear spin splits every level again into **hyperfine** levels separated by gigahertz down to megahertz. Finally an external magnetic field shifts the sublevels by about a megahertz per gauss (the **Zeeman effect**), and that last step explains why the qubit is stored in the two "clock" states.

## Step 1: one electron outside a closed shell

Rubidium has 37 electrons: 36 fill closed shells exactly like the noble gas krypton, and one valence electron sits in the $5s$ orbital. For most purposes an alkali atom is therefore **a hydrogen atom with a fat nucleus**: one electron moving around a compact, spherically symmetric core of charge $+e$.

For hydrogen, the energy depends only on the principal quantum number,

$$E_n=-\frac{\mathrm{Ry}}{n^2},\qquad \mathrm{Ry}=13.606\ \mathrm{eV}.$$

For an alkali, an electron with low orbital angular momentum $\ell$ has an elliptical orbit that **penetrates the core**. Inside the core the nuclear charge is less screened, so the electron is more tightly bound than in hydrogen. The standard way to write this is with a **quantum defect** $\delta_\ell$:

$$E_{n\ell}=-\frac{\mathrm{Ry}}{(n-\delta_\ell)^2}=-\frac{\mathrm{Ry}}{n^{*2}},\qquad n^*=n-\delta_\ell .$$

For Rb the defects are large for S states ($\delta_0\approx3.13$), smaller for P ($\approx2.64$ for $P_{3/2}$, 2.65 for $P_{1/2}$) and D ($\approx1.35$), and almost zero for F states ($\approx0.02$), whose orbits never get close to the core. The defects depend weakly on $n$; the values above are the high-$n$ limits computed with the ARC library, and they will matter again in Chapter 10 for Rydberg states.

![Energy-level diagram of rubidium S, P, D and F levels next to hydrogen, all measured downward from the ionisation limit. The 5S ground state lies 4.18 eV below the limit, far deeper than any hydrogen level with n of 2 or more; S levels are pushed down the most, F levels almost coincide with hydrogen](figures/02-quantum-defects.png)

*Rubidium levels (energies from ARC) compared with hydrogen. The lower the angular momentum, the deeper the core penetration and the larger the shift. The $5S$ ground state is bound by 4.18 eV, corresponding to $n^*=\sqrt{13.6/4.18}=1.80$.*

> **Intuition aside.** In hydrogen the $n=4$ levels lie below $n=5$, so why is the Rb ground state $5s$ rather than $4d$ or $4f$? The $5s$ electron spends much more time inside the core. It is bound by 4.18 eV, against 1.78 eV for $4d$ and 0.86 eV for $4f$, which is almost exactly hydrogen's $n=4$ value of 0.85 eV.

The first excited state is $5p$. Every Rb experiment uses the $5s\to5p$ transition, at 780 to 795 nm. It is a strong transition in a range where cheap diode lasers exist, and the $5p$ state decays back to the ground state in about 26 ns.

## Step 2: fine structure, D1 and D2

The valence electron has spin $s=1/2$. Its orbital motion creates a magnetic field in the electron's rest frame, and the spin's magnetic moment couples to it (**spin-orbit coupling**). Only the total electronic angular momentum $\mathbf J=\mathbf L+\mathbf S$ is conserved. For the $5p$ level ($\ell=1$), $J$ can be $1/2$ or $3/2$, giving two levels:

| Level | Transition from $5S_{1/2}$ | Vacuum wavelength | Frequency | $\Gamma/2\pi$ |
|---|---|---|---|---|
| $5P_{1/2}$ | **D1** | 794.979 nm | 377.107 THz | 5.750 MHz |
| $5P_{3/2}$ | **D2** | 780.241 nm | 384.230 THz | 6.0666 MHz |

The fine-structure splitting is $384.230-377.107=7.123$ THz, about 2% of the optical frequency. The S ground state has $\ell=0$, so it has no spin-orbit splitting: it is just $5S_{1/2}$.

The notation $n\,^{2S+1}L_J$ is standard: in $5\,^2P_{3/2}$ the "2" is the spin multiplicity $2s+1$, which is always 2 for one-electron atoms, so it is usually dropped.

## Step 3: hyperfine structure

The Rb-87 nucleus has spin $I=3/2$ and a magnetic dipole moment (plus, because $I\ge1$, an electric quadrupole moment, which shifts only levels with $J\ge1$). Coupling it to the electron gives the total angular momentum

$$\mathbf F=\mathbf J+\mathbf I,\qquad F=|J-I|,\dots,J+I .$$

For a level with only the magnetic-dipole interaction, the energy shift is

$$\Delta E_F=\frac{A}{2}K,\qquad K=F(F+1)-I(I+1)-J(J+1),$$

where $A$ is the **hyperfine constant** of that level. Neighbouring $F$ levels are split by $A\,F_{\rm upper}$ (the Landé interval rule). Levels with $J\ge1$ have a small extra quadrupole term with constant $B$.

Apply this to Rb-87:

| Level | $F$ values | Hyperfine constants | Splittings |
|---|---|---|---|
| $5S_{1/2}$ | 1, 2 | $A/h=3417.34$ MHz | $2A/h=6834.68$ MHz |
| $5P_{1/2}$ | 1, 2 | $A/h=408.33$ MHz | 816.66 MHz |
| $5P_{3/2}$ | 0, 1, 2, 3 | $A/h=84.72$ MHz, $B/h=12.50$ MHz | 72.22, 156.95, 266.65 MHz |

The ground-state splitting, $6.834\,682\,610\,904$ GHz, is one of the most precisely measured numbers in physics. It is our **qubit frequency**.

Count states as a check: $5S_{1/2}$ has $(2I+1)(2J+1)=4\times2=8$ states, and $F=1$ plus $F=2$ give $3+5=8$ sublevels $m_F$.

![Rubidium-87 level diagram, not to scale. The 5S1/2 ground state splits into F = 1 and F = 2 separated by 6.834 682 611 GHz. The 5P1/2 level (D1, 794.98 nm) splits into F' = 1 and 2, 816.7 MHz apart. The 5P3/2 level (D2, 780.24 nm) splits into F' = 0, 1, 2 and 3 with gaps 72.2, 156.9 and 266.7 MHz. A red double arrow marks the cooling and imaging transition F = 2 to F' = 3; a blue arrow marks the repumper F = 1 to F' = 2; a dotted arrow marks the forbidden decay from F' = 3 to F = 1](figures/02-rb87-levels.png)

*The diagram every Rb experiment is built around. The red **cooling transition** $F=2\to F'=3$ is closed: $F'=3$ can only decay to $F=2$. Off-resonant excitation of $F'=2$ occasionally sends the atom to $F=1$, so a **repumper** laser on $F=1\to F'=2$ returns it to the cycle.*

### Selection rules and the closed cycle

Electric-dipole transitions obey

- $\Delta\ell=\pm1$ (S to P, P to S or D),
- $\Delta F=0,\pm1$, but not $F=0\to F'=0$,
- $\Delta m_F=0$ for $\pi$-polarized light (electric field along the quantisation axis set by the bias field, not along the beam), $\Delta m_F=\pm1$ for $\sigma^\pm$ light.

These rules explain the two lasers in the diagram. An atom excited to $F'=3$ cannot decay to $F=1$, because that would need $\Delta F=-2$. So $F=2\leftrightarrow F'=3$ is a **cycling transition**: in principle the atom can scatter photons forever. If in addition the light is $\sigma^+$ polarized, the atom is optically pumped into the stretched state $|F{=}2,m_F{=}2\rangle$, which couples only to $|F'{=}3,m_F'{=}3\rangle$. That pair is an almost perfect **two-level atom**, the model of Chapter 03.

In practice the cooling laser is also slightly off-resonant with $F'=2$, which is only 266.65 MHz away and can decay to either ground level. The relative probability of exciting the wrong level scales as $(\Gamma/2\Delta)^2$. With $\Gamma/2\pi=6.07$ MHz and $\Delta/2\pi=266.65$ MHz,

$$\left(\frac{6.07}{2\times266.65}\right)^2=1.3\times10^{-4},$$

so after very roughly $10^4$ photons the atom lands in $F=1$ and goes dark. This estimate assumes resonant light and ignores line-strength and branching factors; in a MOT the cooling light is red-detuned by about $2\Gamma$, which makes $F'=2$ relatively more likely. Including the weaker $F=2\to F'=2$ line strength and the 50% chance that $F'=2$ decays to $F=1$, that gives a dark atom every two to three thousand photons (on resonance the same factors stretch the estimate above to a few $10^4$). A perfect $\sigma^+$ beam on $|2,2\rangle$ could not excite $F'=2$ at all (there is no $m_F'=3$ in $F'=2$); the leak happens because real beams and MOTs have mixed polarizations. Laser cooling needs about $5\times10^4$ photons (Chapter 01), so at MOT detunings an atom without the repumper would be lost from the cycle long before it was cold.

## Step 4: the Zeeman effect and the clock states

In a weak magnetic field $B$ along $z$, each hyperfine sublevel shifts linearly:

$$\Delta E=g_F\,m_F\,\mu_BB,\qquad \frac{\mu_B}{h}=1.400\ \mathrm{MHz/G}.$$

For the Rb-87 ground state $g_F\approx+1/2$ for $F=2$ and $g_F\approx-1/2$ for $F=1$, so the sublevels shift by about $\pm0.70$ MHz per gauss per unit of $m_F$. Experiments therefore apply a small, well-controlled **bias field** (a few gauss), which defines the quantisation axis and separates the sublevels.

When the Zeeman energy becomes comparable with the hyperfine splitting, $F$ is no longer a good quantum number. The exact energies for a $J=1/2$ ground state are given by the **Breit-Rabi formula**,

$$E_{F=I\pm1/2,\,m}=-\frac{\Delta E_{\rm hfs}}{2(2I+1)}+g_I\mu_Bm\,B\pm\frac{\Delta E_{\rm hfs}}{2}\sqrt{1+\frac{4m\,x}{2I+1}+x^2},\qquad x=\frac{(g_J-g_I)\mu_BB}{\Delta E_{\rm hfs}},$$

with $g_J=2.00233$ and $g_I=-0.000995$ (Steck's sign convention, in which the Zeeman Hamiltonian is $\mu_B(g_JJ_z+g_II_z)B/\hbar$). For the stretched state $m=-(I+1/2)=-2$ the square root equals $|1-x|$ and must be read as $1-x$ so that the energy stays a smooth function of $B$ through $x=1$. The crossover field $x=1$ is $B=6834.68\ \mathrm{MHz}/(2.0033\times1.400\ \mathrm{MHz/G})\approx2440$ G, far above anything used in a tweezer experiment.

![Left: Breit-Rabi diagram of the Rb-87 ground state from 0 to 5000 gauss; five F = 2 sublevels start at +2.56 GHz and three F = 1 sublevels at -4.27 GHz, fanning out linearly at low field, curving at intermediate field and becoming linear again (Paschen-Back regime) at high field. Right: on a log scale, the shift of the clock transition grows as 575 Hz per gauss squared and reaches 575 Hz at 1 gauss, while the magnetically sensitive transition from 1,0 to 2,1 shifts by 0.70 MHz per gauss](figures/02-breit-rabi.png)

*Left: the exact ground-state energies (Breit-Rabi). Right: why the qubit lives in the $m_F=0$ "clock" states. Their transition has no linear Zeeman shift, only a quadratic one. At 1 G it shifts by 575 Hz instead of 700 kHz, and its sensitivity to field fluctuations is about 600 times smaller ($d\nu/dB=1.15$ kHz/G instead of 0.70 MHz/G).*

The two $m_F=0$ states have no linear shift at all. Expanding the Breit-Rabi formula to second order in $x$ for $m=0$ gives the **clock-transition shift**

$$\Delta\nu_{\rm clock}=\frac{(g_J-g_I)^2\mu_B^2}{2h^2\,\nu_{\rm hfs}}B^2=575.15\ \mathrm{Hz/G^2}\times B^2 .$$

The standard neutral-atom qubit therefore uses the two clock states,

$$|0\rangle=|F{=}1,m_F{=}0\rangle,\qquad |1\rangle=|F{=}2,m_F{=}0\rangle .$$

(The same states make the caesium and rubidium atomic clocks; caesium's $9.192\,631\,770$ GHz clock transition defines the SI second.)

## Beyond rubidium

| Atom | Why people use it | Note |
|---|---|---|
| Rb-87, Rb-85 | cheap 780/795 nm diode lasers; mature technology | Rb-85 has $I=5/2$ and a 3.04 GHz ground splitting |
| Cs-133 | largest hyperfine splitting of the stable alkalis (9.19 GHz); heavy, so small recoil | $I=7/2$, D2 line at 852 nm |
| Na, K, Li | lighter alkalis, popular for quantum gases | sub-Doppler cooling is harder for some isotopes |
| Sr, Yb (alkaline-earth and alkaline-earth-like) | two valence electrons give narrow "intercombination" and ultra-narrow "clock" lines; the fermionic isotopes have a nuclear spin with no electronic spin in the ground state | Sr-87 has $I=9/2$; Yb-171 has $I=1/2$, a natural nuclear-spin qubit |

Two-electron atoms have singlet and triplet families. A broad singlet line (for Sr, 461 nm, $\Gamma/2\pi\approx30$ MHz) is used for imaging, while the spin-forbidden singlet-triplet line (for Sr, 689 nm, $\Gamma/2\pi\approx7$ kHz) allows cooling to below a microkelvin. Chapter 09 returns to the qubit encodings these atoms make possible. For the rest of the course we stay with Rb-87.

## Worked example (Rb-87, values from the reference table)

| Quantity | Formula | Value |
|---|---|---|
| fine-structure splitting | $c/\lambda_{D2}-c/\lambda_{D1}$ | **7.123 THz** |
| ground hyperfine constant | $A/h=\nu_{\rm hfs}/2$ | **3417.34 MHz** |
| Zeeman shift of $\vert2,2\rangle$ at 3 G | $g_Fm_F\mu_BB/h=\tfrac12\cdot2\cdot1.400\cdot3$ | **4.2 MHz** |
| clock shift at 3 G | $575.15\times3^2$ | **5.18 kHz** |
| clock sensitivity at 3 G | $d\nu/dB=2\times575.15\times3$ | **3.45 kHz/G** |
| sensitivity of $\vert1,0\rangle\to\vert2,1\rangle$ | $\approx\tfrac12\mu_B/h$ | **0.70 MHz/G** |

**Step 1: fine structure.** $384.230-377.107=7.123$ THz. Two lasers 15 nm apart address completely different excited levels.

**Step 2: field noise.** Suppose the bias field fluctuates by 1 mG from shot to shot. The clock qubit frequency then fluctuates by $3.45\ \mathrm{kHz/G}\times10^{-3}\ \mathrm{G}=3.5$ Hz; a $\Delta m_F=1$ qubit would fluctuate by $0.70\ \mathrm{MHz/G}\times10^{-3}\ \mathrm{G}=700$ Hz. A phase error of one radian accumulates after $1/(2\pi\times3.5\ \mathrm{Hz})\approx45$ ms for the clock qubit but after only $1/(2\pi\times700\ \mathrm{Hz})\approx0.23$ ms for the other. That factor of 200 is why the clock states are used.

**Step 3: repumping.** At MOT detunings the estimate above gives one leak to $F=1$ every two to three thousand photons. At a scattering rate of $10^6$ to $10^7$ photons per second that happens every 0.2 to 3 ms, so the repumper must be on whenever the cooling light is.

## Common pitfalls

- **"The D2 line is a single frequency."** The $5S_{1/2}\to5P_{3/2}$ line has six allowed hyperfine components ($F=1\to F'=0,1,2$ and $F=2\to F'=1,2,3$) spread over 7 GHz. The quoted 780.241 nm refers to the centre of gravity of the line; lasers are locked to a specific hyperfine component.
- **"Hyperfine splittings follow $A\,F$."** The interval rule gives the splitting between $F$ and $F-1$ as $A\,F$ only when there is no quadrupole term. For $5P_{3/2}$ the $B$ term is needed to reproduce the measured splittings, 72.22, 156.95 and 266.65 MHz (to within 0.01 MHz).
- **"Clock states are immune to magnetic fields."** They have no *linear* shift; the quadratic shift (575 Hz/G$^2$) is still there and must be included when the bias field is several gauss.
- **"$g_F=1/2$ exactly."** It is $0.4998$ for $F=2$ and $-0.5018$ for $F=1$, because $g_J=2.00233$ is not exactly 2 and because of the small nuclear term $g_I$. The difference matters for precision work.
- **Primed and unprimed $F$.** By convention $F'$ refers to the excited state and $F$ to the ground state; mixing them up sends lasers to the wrong transition.

## Key takeaways

- Alkali atoms are hydrogen-like; the core penetration of low-$\ell$ orbits is captured by quantum defects, $E=-\mathrm{Ry}/(n-\delta_\ell)^2$.
- Spin-orbit coupling splits $5P$ into $5P_{1/2}$ (D1, 795 nm) and $5P_{3/2}$ (D2, 780 nm).
- Coupling to the $I=3/2$ nucleus splits the ground state into $F=1$ and $F=2$, 6.834682611 GHz apart; this splitting is the qubit frequency.
- $F=2\to F'=3$ is a closed cycling transition used for cooling and imaging; a repumper on $F=1\to F'=2$ recovers atoms that leak out.
- The $m_F=0$ clock states have only a quadratic Zeeman shift, 575 Hz/G$^2$, which makes them the standard qubit.

## Go deeper

- C. J. Foot, *Atomic Physics* (Oxford University Press, 2005), chapters 4 to 6. The clearest textbook treatment of alkali structure, fine and hyperfine structure, and the Zeeman effect.
- D. A. Steck, *Rubidium 87 D Line Data*, [steck.us/alkalidata](https://steck.us/alkalidata). The Rb-87 numbers in this chapter (wavelengths, linewidths, hyperfine constants, $g$-factors), with references and the Breit-Rabi formula in this chapter's form.
- N. Šibalić, J. D. Pritchard, C. S. Adams, K. J. Weatherill, *ARC: An open-source library for calculating properties of alkali Rydberg atoms*, Comput. Phys. Commun. 220, 319 (2017), [arXiv:1612.05529](https://arxiv.org/abs/1612.05529). The library used here for quantum defects and level energies; install it with `pip install arc-alkali-rydberg-calculator` and reproduce the first figure.
- H. J. Metcalf and P. van der Straten, *Laser cooling and trapping of atoms*, J. Opt. Soc. Am. B 20, 887 (2003), [Utrecht preprint](https://webspace.science.uu.nl/~strat102/preprint/handpubl.pdf). Its discussion of multilevel atoms, optical pumping and repumping builds directly on this chapter.

---

← Previous: [Introduction: Why Neutral Atoms](01-introduction.md) · [Tutorial index](./README.md) · [Project README](../README.md) · Next: [A Two-Level Atom in a Laser Field](03-atom-light.md) →
