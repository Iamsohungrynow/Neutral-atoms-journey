"""
An optical tweezer for Rb-87: polarizability, depth, trap frequencies, scattering.

Physics
-------
Each D line is a Lorentz oscillator. Keeping the counter-rotating term, the
ground-state polarizability (SI) is

    alpha(w) = sum_lines  wt * 6 pi eps0 c^3 (Gamma/w0^2) / (w0^2 - w^2)

with weights 1/3 (D1) and 2/3 (D2) (Grimm, Weidemueller, Ovchinnikov 2000).
A Gaussian focus I(r, z) = 2P/(pi w(z)^2) exp(-2 r^2 / w(z)^2), w(z) = w0 sqrt(1 + (z/zR)^2),
zR = pi w0^2 / lambda, gives the potential U = -alpha I / (2 eps0 c). Near the
bottom it is harmonic with

    omega_r = sqrt(4 U0 / (m w0^2)),   omega_z = sqrt(2 U0 / (m zR^2)).

The photon scattering rate is

    Gamma_sc = sum wt * (3 pi c^2 / 2 hbar w0^3) (w/w0)^3 (Gamma/(w0-w) + Gamma/(w0+w))^2 I.

Units: SI. Atomic units of polarizability: 1 a.u. = 4 pi eps0 a0^3.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

h = 6.62607015e-34
hbar = h / (2 * np.pi)
kB = 1.380649e-23
c = 299792458.0
eps0 = 8.8541878128e-12
a0 = 5.29177210903e-11
AU = 4 * np.pi * eps0 * a0**3
m = 86.909180531 * 1.66053906660e-27
LINES = [(2 * np.pi * c / 794.978851156e-9, 2 * np.pi * 5.7500e6, 1 / 3),   # D1
         (2 * np.pi * c / 780.241209686e-9, 2 * np.pi * 6.0666e6, 2 / 3)]   # D2


def alpha(lam):
    w = 2 * np.pi * c / np.asarray(lam, dtype=float)
    return sum(wt * 6 * np.pi * eps0 * c**3 * (G / w0**2) / (w0**2 - w**2) for w0, G, wt in LINES)


def scatter_rate(lam, I):
    w = 2 * np.pi * c / np.asarray(lam, dtype=float)
    return sum(wt * 3 * np.pi * c**2 / (2 * hbar * w0**3) * (w / w0)**3
               * (G / (w0 - w) + G / (w0 + w))**2 * I for w0, G, wt in LINES)


def potential(r, z, lam, P, w0):
    zR = np.pi * w0**2 / lam
    wz = w0 * np.sqrt(1 + (z / zR)**2)
    I = 2 * P / (np.pi * wz**2) * np.exp(-2 * r**2 / wz**2)
    return -alpha(lam) * I / (2 * eps0 * c)


def summary(lam, P, w0):
    U0 = -potential(0, 0, lam, P, w0)
    zR = np.pi * w0**2 / lam
    wr = np.sqrt(4 * U0 / (m * w0**2))
    wz = np.sqrt(2 * U0 / (m * zR**2))
    I0 = 2 * P / (np.pi * w0**2)
    return U0, wr, wz, zR, scatter_rate(lam, I0)


# ---------------------------------------------------------------------------
# Numbers for the reference tweezer
# ---------------------------------------------------------------------------
w0 = 1.0e-6
print("Optical tweezer for Rb-87 (two-line D1 + D2 model)")
print("=" * 66)
print(f"static polarizability  alpha(0) = {alpha(1.0) / AU:.1f} a.u. (measured: 318.8 a.u.)")
tune_out = brentq(alpha, 781e-9, 794e-9)
print(f"tune-out wavelength between D2 and D1: {tune_out * 1e9:.2f} nm")
for lam in (1064e-9, 852e-9):
    U1, *_ = summary(lam, 1e-3, w0)
    P_mK = 1e-3 * kB / U1 * 1e-3
    U0, wr, wz, zR, sc = summary(lam, P_mK, w0)
    Er = (h / lam)**2 / (2 * m)
    print(f"{lam * 1e9:.0f} nm: alpha = {alpha(lam) / AU:7.1f} a.u.; depth per mW (w0 = 1 um) = "
          f"{U1 / kB * 1e6:6.1f} uK = h x {U1 / h / 1e6:.2f} MHz")
    print(f"        for U0 = 1 mK: P = {P_mK * 1e3:5.2f} mW, f_r = {wr / 2 / np.pi / 1e3:5.1f} kHz, "
          f"f_z = {wz / 2 / np.pi / 1e3:4.1f} kHz, zR = {zR * 1e6:.2f} um")
    print(f"        scattering {sc:5.1f} photons/s, recoil heating 2 E_r Gamma_sc = "
          f"{2 * Er * sc / kB * 1e6:.2f} uK/s")

# numerical curvature at the bottom versus the harmonic formulas (1064 nm, 1 mK)
lam = 1064e-9
P_mK = 1e-3 * kB / summary(lam, 1e-3, w0)[0] * 1e-3
U0, wr, wz, zR, _ = summary(lam, P_mK, w0)
dr, dz = 1e-9, 1e-9
k_r = (potential(dr, 0, lam, P_mK, w0) - 2 * potential(0, 0, lam, P_mK, w0) + potential(-dr, 0, lam, P_mK, w0)) / dr**2
k_z = (potential(0, dz, lam, P_mK, w0) - 2 * potential(0, 0, lam, P_mK, w0) + potential(0, -dz, lam, P_mK, w0)) / dz**2
wr_num, wz_num = np.sqrt(k_r / m), np.sqrt(k_z / m)
print(f"curvature check: f_r numerical {wr_num / 2 / np.pi / 1e3:.3f} kHz vs analytic {wr / 2 / np.pi / 1e3:.3f} kHz; "
      f"f_z {wz_num / 2 / np.pi / 1e3:.3f} vs {wz / 2 / np.pi / 1e3:.3f} kHz")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.2))
lam_axis = np.linspace(500e-9, 1200e-9, 4000)
a = alpha(lam_axis) / AU
ax = axes[0]
ax.plot(lam_axis * 1e9, np.where(np.abs(a) < 1.4e4, a, np.nan), "k", lw=1.5)
ax.axhline(0, color="0.6", lw=0.8)
for l, lab in [(780.24, "D2"), (794.98, "D1")]:
    ax.axvline(l, color="C3", lw=0.8, ls=":")
ax.text(787, 1.32e4, "D2  D1", fontsize=8, color="C3", ha="center")
ax.set_ylim(-1.5e4, 1.5e4)
ax.set_xlabel("trap wavelength (nm)")
ax.set_ylabel("ground-state polarizability (a.u.)")
ax.set_title("alpha > 0: attractive (red of D1)\nalpha < 0: repulsive (blue of D2)", fontsize=9)
ax.annotate("1064 nm: 677 a.u.", xy=(1064, alpha(1064e-9) / AU), xytext=(930, 6e3), fontsize=8,
            arrowprops=dict(arrowstyle="->"))
ax = axes[1]
r = np.linspace(-2.5e-6, 2.5e-6, 500)
zz = np.linspace(-8e-6, 8e-6, 500)
ax.plot(r * 1e6, potential(r, 0, lam, P_mK, w0) / kB * 1e3, "C0", lw=2, label="radial (z = 0)")
ax.plot(r * 1e6, (-U0 + 0.5 * m * wr**2 * r**2) / kB * 1e3, "C0:", lw=1.2, label="harmonic, radial")
ax.plot(zz * 1e6, potential(0, zz, lam, P_mK, w0) / kB * 1e3, "C1", lw=2, label="axial (r = 0)")
ax.plot(zz * 1e6, (-U0 + 0.5 * m * wz**2 * zz**2) / kB * 1e3, "C1:", lw=1.2, label="harmonic, axial")
ax.set_ylim(-1.05, 0.1)
ax.set_xlabel("position (um)")
ax.set_ylabel("U / k_B (mK)")
ax.set_title("1064 nm, w0 = 1 um, 10.3 mW: a 1 mK well", fontsize=9)
ax.legend(fontsize=7, loc="lower right")
ax = axes[2]
lam_red = np.linspace(805e-9, 1200e-9, 400)
I_unit = 2e-3 / (np.pi * w0**2)                 # 1 mW into w0 = 1 um
depth_unit = alpha(lam_red) * I_unit / (2 * eps0 * c)
sc_per_mK = scatter_rate(lam_red, I_unit) * (1e-3 * kB / depth_unit)
ax.semilogy(lam_red * 1e9, sc_per_mK, "C2", lw=2)
ax.set_xlabel("trap wavelength (nm)")
ax.set_ylabel("photons scattered per second at U0 = 1 mK")
ax.set_title("Same depth, farther detuned: less scattering", fontsize=9)
for l in (852, 1064):
    v = scatter_rate(l * 1e-9, I_unit) * (1e-3 * kB / (alpha(l * 1e-9) * I_unit / (2 * eps0 * c)))
    ax.plot(l, v, "ko", ms=4)
    ax.text(l + 8, v * 1.15, f"{l} nm: {v:.1f}/s", fontsize=8)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "tweezer.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
depth_1064 = summary(1064e-9, 1e-3, 1e-6)[0] / kB * 1e6
checks = {
    "numerical curvature of the Gaussian well gives omega_r = sqrt(4U0/mw0^2) (1e-4)":
        abs(wr_num / wr - 1) < 1e-4,
    "numerical curvature gives omega_z = sqrt(2U0/m zR^2) (1e-4)": abs(wz_num / wz - 1) < 1e-4,
    "depth per mW at 1064 nm, w0 = 1 um is 97 uK (reference table)": abs(depth_1064 - 97.0) < 0.5,
    "attractive red of D1, repulsive blue of D2, tune-out between the D lines":
        alpha(1064e-9) > 0 and alpha(852e-9) > 0 and alpha(532e-9) < 0 and 780.3e-9 < tune_out < 794.9e-9,
    "static limit within 5% of the measured 318.8 a.u. (higher states add the rest)":
        abs(alpha(1.0) / AU / 318.8 - 1) < 0.05,
}
