"""
A Zeeman slower for Rb-87 (1D trajectories with the full scattering force).

Physics
-------
An atom moving at velocity v along +z meets a counter-propagating laser
(travelling along -z) of detuning delta_L = wL - w0. It sees the light Doppler
shifted up by k v, while a magnetic field B(z) shifts the sigma+ cycling
transition |2,2> -> |3',3'> up by mu' B / hbar with mu' = mu_B. The effective
detuning is

    delta_eff(z, v) = delta_L + k v - mu' B(z) / hbar

and the scattering force is F = -hbar k (Gamma/2) s0 / (1 + s0 + (2 delta_eff/Gamma)^2).

Design: choose a constant deceleration a = eta * a_max, a_max = hbar k Gamma / 2m.
The design velocity is v_d(z) = sqrt(v0^2 - 2 a z), and the field keeps an atom
moving at v_d(z) exactly on resonance:

    mu' B(z) / hbar = delta_L + k v_d(z).

The slower ends where v_d reaches v_f; beyond it B = 0 and the atom is about
20 linewidths off resonance, so it stops scattering. An atom locked to the
resonance lags behind v_d by the velocity at which the force equals m*a,
i.e. where s0/(1 + s0 + x^2) = eta with x = 2 delta_eff/Gamma.

Units: SI.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

hbar = 1.054571817e-34
muB = 9.2740100783e-24
m = 86.909180531 * 1.66053906660e-27
lam = 780.241209686e-9
k = 2 * np.pi / lam
Gamma = 2 * np.pi * 6.0666e6
a_max = hbar * k * Gamma / (2 * m)

# Design parameters (illustrative)
v0 = 300.0                     # capture velocity of the design (m/s)
v_f = 30.0                     # exit velocity (m/s)
eta = 0.6                      # fraction of a_max used
s0 = 3.0                       # saturation parameter of the slowing beam
delta_L = -2 * np.pi * 160e6   # laser detuning (rad/s)
a = eta * a_max
L = (v0**2 - v_f**2) / (2 * a)  # slower length


def v_design(z):
    return np.sqrt(np.clip(v0**2 - 2 * a * z, v_f**2, None))


def B_field(z):
    """Tesla. Inside the slower the field keeps v_design resonant; outside it is zero."""
    z = np.asarray(z, dtype=float)
    inside = (z >= 0) & (z <= L)
    return np.where(inside, hbar * (delta_L + k * v_design(z)) / muB, 0.0)


def accel(z, v):
    d_eff = delta_L + k * v - muB * B_field(z) / hbar
    return -(hbar * k / m) * (Gamma / 2) * s0 / (1 + s0 + (2 * d_eff / Gamma)**2)


def rhs(t, y):
    z, v = y
    return [v, accel(z, v)]


def fly(v_init, z_start=-0.05, z_stop=None):
    z_stop = L + 0.10 if z_stop is None else z_stop
    hit_end = lambda t, y: y[0] - z_stop
    hit_end.terminal = True
    turned = lambda t, y: y[1] - 1.0          # stop if the atom is pushed back
    turned.terminal = True
    sol = solve_ivp(rhs, (0, 0.2), [z_start, v_init], events=[hit_end, turned],
                    max_step=2e-6, rtol=1e-8, atol=1e-10)
    return sol.y[0], sol.y[1]


# Equilibrium lag of a locked atom: s0/(1+s0+x^2) = eta
x_lag = np.sqrt(s0 / eta - 1 - s0)
dv_lag = x_lag * Gamma / (2 * k)

v_inits = [100, 150, 200, 250, 290, 320, 350, 400]
trajectories = {v: fly(v) for v in v_inits}
v_exit = {v: trajectories[v][1][-1] for v in v_inits}

print("Zeeman slower for Rb-87 (sigma+ cycling transition, mu' = mu_B)")
print("=" * 66)
print(f"a_max = {a_max:.3e} m/s^2; design deceleration eta*a_max = {a:.3e} m/s^2")
print(f"length L = (v0^2 - v_f^2)/(2 eta a_max) = {L:.3f} m")
print(f"field at entrance {B_field(0.0) * 1e4:+.1f} G, at exit {B_field(L) * 1e4:+.1f} G")
print(f"detuning after the slower for v_f: {(delta_L + k * v_f) / Gamma:+.1f} Gamma")
print(f"predicted lag behind v_design: {dv_lag:.2f} m/s (x = {x_lag:.2f})")
print("-" * 66)
for v in v_inits:
    print(f"v_init = {v:3d} m/s -> v_exit = {v_exit[v]:6.1f} m/s")

# Lag measured for the atom that starts at v0 (middle third of the slower)
z_c, v_c = trajectories[290]
mid = (z_c > 0.3 * L) & (z_c < 0.7 * L)
lag_measured = np.mean(v_design(z_c[mid]) - v_c[mid])
print(f"measured lag in the middle of the slower: {lag_measured:.2f} m/s")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.3))
zz = np.linspace(-0.05, L + 0.1, 800)
ax1.plot(zz * 100, B_field(zz) * 1e4, "C0", lw=2)
ax1.axhline(0, color="0.7", lw=0.8)
ax1.set_xlabel("position z (cm)")
ax1.set_ylabel("magnetic field B (G)")
ax1.set_title(f"Designed field: L = {L * 100:.1f} cm, eta = {eta}")
for v in v_inits:
    z, vv = trajectories[v]
    ax2.plot(z * 100, vv, lw=1.4, label=f"{v} m/s")
inside = (zz >= 0) & (zz <= L)
ax2.plot(zz[inside] * 100, v_design(zz[inside]), "k--", lw=1, label="design v_d(z)")
ax2.set_xlabel("position z (cm)")
ax2.set_ylabel("velocity (m/s)")
ax2.set_title("Atoms below ~v0 lock on and exit at ~v_f")
ax2.legend(fontsize=7, ncol=2, loc="upper right")
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "slower.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
captured = [v for v in v_inits if v <= 290]
checks = {
    "length equals (v0^2 - v_f^2)/(2 eta a_max) and exceeds the a_max minimum":
        np.isclose(L, (v0**2 - v_f**2) / (2 * eta * a_max)) and L > (v0**2 - v_f**2) / (2 * a_max),
    "atoms starting below the capture velocity exit within 5 m/s of v_f":
        all(abs(v_exit[v] - (v_f - dv_lag)) < 5.0 for v in captured),
    "atoms faster than the capture velocity are not slowed to v_f":
        all(v_exit[v] > 0.8 * v for v in v_inits if v >= 350),
    "locked atom lags v_design by x*Gamma/2k from the force balance (10%)":
        abs(lag_measured / dv_lag - 1) < 0.10,
}
