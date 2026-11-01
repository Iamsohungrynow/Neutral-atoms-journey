"""
A one-dimensional magneto-optical trap (J = 0 -> J' = 1 model).

Physics
-------
A linear field B = A z Zeeman-shifts the excited sublevels m' = +1 and m' = -1
by +/- mu' A z / hbar. Two red-detuned beams: the one travelling along +z
drives m' = +1 (sigma+), the one along -z drives m' = -1 (sigma-). For an atom
at position z with velocity v the effective detunings are

    beam along +z :  delta - k v - mu' A z / hbar
    beam along -z :  delta + k v + mu' A z / hbar

and the force is the difference of the two scattering forces (beams treated
independently). Expanding for small z and v,

    F = -beta v - kappa z,   kappa = mu' A beta / (hbar k),

with the molasses friction coefficient beta of Chapter 05. The atom is a damped
harmonic oscillator with omega_0 = sqrt(kappa/m) and damping rate beta/m.

Illustrative parameters: Rb-87 D2, delta = -Gamma, s0 = 1 per beam,
A = 10 G/cm, mu' = mu_B, beam radius 1 cm. Units: SI.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

hbar = 1.054571817e-34
muB = 9.2740100783e-24
m = 86.909180531 * 1.66053906660e-27
k = 2 * np.pi / 780.241209686e-9
Gamma = 2 * np.pi * 6.0666e6

delta = -1.0 * Gamma
s0 = 1.0
A = 0.10            # T/m  (= 10 G/cm)
mu = muB
R_beam = 0.01       # m


def force(z, v):
    z = np.asarray(z, dtype=float)
    shift = mu * A * z / hbar
    fp = s0 / (1 + s0 + (2 * (delta - k * v - shift) / Gamma)**2)
    fm = s0 / (1 + s0 + (2 * (delta + k * v + shift) / Gamma)**2)
    F = hbar * k * Gamma / 2 * (fp - fm)
    return np.where(np.abs(z) <= R_beam, F, 0.0)


beta = -8 * hbar * k**2 * delta * s0 / (Gamma * (1 + s0 + (2 * delta / Gamma)**2)**2)
kappa = mu * A * beta / (hbar * k)
w0 = np.sqrt(kappa / m)
gam = beta / m                     # amplitude decays as exp(-gam t / 2)

# numerical derivatives at the origin
h_v, h_z = 1e-4, 1e-8
beta_num = -(force(0, h_v) - force(0, -h_v)) / (2 * h_v)
kappa_num = -(force(h_z, 0) - force(-h_z, 0)) / (2 * h_z)


def rhs(t, y):
    return [y[1], force(y[0], y[1]) / m]


# small-amplitude release from rest
z_init = 20e-6
t = np.linspace(0, 8e-3, 2000)
sol = solve_ivp(rhs, (0, t[-1]), [z_init, 0.0], t_eval=t, rtol=1e-10, atol=1e-14)
disc = (gam / 2)**2 - w0**2
if disc < 0:                                   # underdamped
    wd = np.sqrt(-disc)
    z_lin = z_init * np.exp(-gam * t / 2) * (np.cos(wd * t) + gam / (2 * wd) * np.sin(wd * t))
else:                                          # overdamped
    r1, r2 = -gam / 2 + np.sqrt(disc), -gam / 2 - np.sqrt(disc)
    z_lin = z_init * (r2 * np.exp(r1 * t) - r1 * np.exp(r2 * t)) / (r2 - r1)


# capture: atoms enter at z = -R with velocity v; captured if they stay inside
def captured(v_in, t_max=0.05):
    out = lambda t, y: abs(y[0]) - 1.001 * R_beam
    out.terminal = True
    s = solve_ivp(rhs, (0, t_max), [-R_beam, v_in], events=out, max_step=2e-5, rtol=1e-8, atol=1e-12)
    return s.status != 1, s


lo, hi = 0.0, 100.0
for _ in range(30):
    mid = 0.5 * (lo + hi)
    lo, hi = (mid, hi) if captured(mid)[0] else (lo, mid)
v_capture = lo
F_bound = hbar * k * Gamma / 2 * s0 / (1 + s0)
v_bound = np.sqrt(2 * F_bound * 2 * R_beam / m)    # cannot remove more energy than F_max * 2R

print("1D MOT, Rb-87 D2: delta = -Gamma, s0 = 1 per beam, A = 10 G/cm")
print("=" * 64)
print(f"beta  = {beta:.4e} kg/s   (numerical derivative {beta_num:.4e})")
print(f"kappa = {kappa:.4e} N/m   (numerical derivative {kappa_num:.4e})")
print(f"trap frequency omega0/2pi = {w0 / 2 / np.pi:.1f} Hz, damping rate beta/m = {gam:.1f} 1/s")
print(f"damping ratio (beta/m)/(2 omega0) = {gam / (2 * w0):.2f} "
      f"({'under' if disc < 0 else 'over'}damped)")
print(f"force maximum near |z| = |delta| hbar/(mu' A) = {abs(delta) * hbar / (mu * A) * 1e3:.2f} mm (linear only for |z| < ~2 mm)")
print(f"capture velocity (beam radius 1 cm): {v_capture:.1f} m/s; "
      f"energy bound sqrt(4 F_max R/m) = {v_bound:.1f} m/s")
print(f"max deviation from damped-oscillator solution: "
      f"{np.max(np.abs(sol.y[0] - z_lin)) / z_init * 100:.3f}% of z0")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(14, 4.0))
zz = np.linspace(-1.2 * R_beam, 1.2 * R_beam, 800)
axes[0].plot(zz * 1e3, force(zz, 0) * 1e21, "k", lw=2, label="full force F(z, v=0)")
zl = np.abs(zz) < 3e-3
axes[0].plot(zz[zl] * 1e3, -kappa * zz[zl] * 1e21, "C1--", lw=1.5, label="linear -kappa z")
axes[0].set_xlabel("position z (mm)")
axes[0].set_ylabel("force (1e-21 N)")
axes[0].set_title("Restoring force (beams end at +/-10 mm)")
axes[0].legend(fontsize=8)
axes[1].plot(t * 1e3, sol.y[0] * 1e6, "C0", lw=2, label="numerical")
axes[1].plot(t * 1e3, z_lin * 1e6, "k:", lw=1.5, label="damped oscillator")
axes[1].set_xlabel("time (ms)")
axes[1].set_ylabel("position (um)")
axes[1].set_title("Small oscillation: a damped harmonic oscillator")
axes[1].legend(fontsize=8)
for v_in in [5, 10, 15, 20, v_capture * 0.98, v_capture * 1.05, 40]:
    ok, s = captured(v_in)
    axes[2].plot(s.y[0] * 1e3, s.y[1], color="C2" if ok else "C3", lw=1.2)
axes[2].set_xlabel("position z (mm)")
axes[2].set_ylabel("velocity (m/s)")
axes[2].set_title(f"Capture: green caught, red lost (v_c = {v_capture:.1f} m/s)")
axes[2].axvline(-10, color="0.7", lw=0.8)
axes[2].axvline(10, color="0.7", lw=0.8)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "mot.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
zin = np.linspace(1e-6, R_beam, 500)
checks = {
    "dF/dv at the origin equals -beta (molasses formula)": abs(beta_num / beta - 1) < 1e-4,
    "dF/dz at the origin equals -kappa = -mu' A beta/(hbar k)": abs(kappa_num / kappa - 1) < 1e-4,
    "small oscillation follows the analytic damped oscillator within 1% of z0":
        np.max(np.abs(sol.y[0] - z_lin)) < 0.01 * z_init,
    "force is restoring everywhere inside the beams":
        np.all(force(zin, 0) < 0) and np.all(force(-zin, 0) > 0),
    "capture velocity lies below the energy bound sqrt(4 F_max R/m) and above 30% of it":
        0.3 * v_bound < v_capture < v_bound,
}
