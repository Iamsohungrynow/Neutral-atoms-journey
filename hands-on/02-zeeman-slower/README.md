# Zeeman slower

Theory: [Chapter 05](../../tutorial/05-doppler-cooling.md)

## What you simulate

A Rb-87 atom flies along $+z$ into a counter-propagating, $\sigma^+$-polarized
slowing beam. Its effective detuning combines the laser detuning, the Doppler
shift and the Zeeman shift of the cycling transition ($\mu'=\mu_B$):

    delta_eff(z, v) = delta_L + k v - mu_B B(z) / hbar

and it feels the full Lorentzian scattering force (Chapter 04). You first
**design** a slower for constant deceleration $a=\eta\,a_{\max}$, from a capture
velocity $v_0=300$ m/s down to $v_f=30$ m/s, then integrate trajectories for atoms
entering at 100 to 400 m/s and see which ones are captured.

Design values (illustrative): $\eta=0.6$, $s_0=3$, $\delta_L/2\pi=-160$ MHz.

## Run it

Run these commands from the **repository root**, using the environment from the [shared setup](../README.md).

    python -m pip install -r hands-on/requirements.txt
    python hands-on/02-zeeman-slower/slower.py

## The code explained

The design velocity and the field that keeps it resonant are one line each:

    v_design(z) = sqrt(v0**2 - 2*a*z)
    B(z) = hbar * (delta_L + k * v_design(z)) / muB      # inside 0 <= z <= L, else 0

`solve_ivp` integrates $\dot z=v$, $\dot v=F(z,v)/m$ with a small maximum step
(the force changes over a few cm) and stops when the atom leaves the slower
region or is pushed backward.

The force balance predicts how far a locked atom lags behind the design
velocity: the force equals $m\,a$ when
$s_0/(1+s_0+x^2)=\eta$ with $x=2\delta_{\rm eff}/\Gamma$. With $s_0=3$ and
$\eta=0.6$ this gives $x=1$, a lag of $\Gamma/2k=2.37$ m/s. The script measures
the actual lag between 30% and 70% of the slower length, and the actual
deceleration from the slope of $v^2$ versus $z$, and compares both with the design.

## Expected output

    a_max = 1.122e+05 m/s^2; design deceleration eta*a_max = 6.729e+04 m/s^2
    length L = (v0^2 - v_f^2)/(2 eta a_max) = 0.662 m
    field at entrance +160.4 G, at exit -86.8 G
    detuning after the slower for v_f: -20.0 Gamma
    predicted lag behind v_design: 2.37 m/s (x = 1.00)
    v_init = 100 m/s -> v_exit =   26.4 m/s
    v_init = 150 m/s -> v_exit =   26.4 m/s
    v_init = 200 m/s -> v_exit =   26.4 m/s
    v_init = 250 m/s -> v_exit =   26.4 m/s
    v_init = 290 m/s -> v_exit =   26.4 m/s
    v_init = 320 m/s -> v_exit =  318.9 m/s
    v_init = 350 m/s -> v_exit =  349.7 m/s
    v_init = 400 m/s -> v_exit =  399.9 m/s
    measured lag in the middle of the slower: 2.43 m/s
    measured deceleration of the locked atom: 6.6529e+04 m/s^2 (design eta*a_max = 6.7291e+04)

![Zeeman slower field and trajectories](figures/slower.png)

Left: the designed field. It falls from $+160$ G, crosses zero, and ends at
$-87$ G, where it drops abruptly to zero. Right: every atom slower than about
300 m/s coasts until the resonance condition reaches it, locks on just below the
dashed design curve (on its slow, red-detuned side), and leaves at 26.4 m/s: $v_f$
minus the lag (which grows to about 2.8 m/s near the exit, where $v_d$ is small),
minus a further 0.7 m/s lost in the 10 cm after the slower, where the atom is
20 linewidths off resonance but still scatters a few times $10^4$ photons per
second. Atoms above the capture velocity are never resonant
and pass through almost unchanged.

The runner checks four things: that the deceleration the locked atom actually
experiences (the slope of $v^2$ versus $z$, which should be $-2\eta a_{\max}$; the
small lag makes it about 1% lower) matches the design within 2%; that atoms entering between $v_f$ and $v_0$ leave
within 2 m/s of $v_f$ minus the lag; that atoms above $v_0$ are not captured; and
that the measured lag matches the force balance (10%). The deceleration check
only confirms that the atom stays locked (any locked atom follows the designed
$B(z)$); the lag check is the one that tests the force law itself.

## Try this

1. Raise $\eta$ to 0.8, above $s_0/(1+s_0)=0.75$. The slower gets shorter, but
   atoms can no longer keep up with the resonance and fall out of lock. Find the
   largest $\eta$ that still works.
2. Lower $s_0$ to 1 while keeping $\eta=0.6$. Predict the new lag from the force
   balance first. (Is there a solution at all?)
3. Add a 5% error to $B(z)$ near the middle of the slower. How much does the
   exit velocity change? (Real coils never follow the design exactly.)
