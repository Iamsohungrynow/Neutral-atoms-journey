"""
Release-and-recapture thermometry of a single atom in a tweezer (Monte Carlo).

Physics
-------
An atom at temperature T sits in a Gaussian tweezer of depth U0. The trap is
switched off for a time t; the atom flies ballistically (gravity included,
though it hardly matters on these time scales); the trap is switched back on.
The atom is recaptured if its total energy in the re-applied trap is negative:

    E = (1/2) m v^2 + U(r(t)) < 0,   U(r, z) = -U0 w0^2/w(z)^2 exp(-2 r^2 / w(z)^2).

Initial state: thermal phase-space distribution of the HARMONIC approximation
of the trap (Gaussian positions with sigma_i = sqrt(kT/(m omega_i^2)), Gaussian
velocities with sigma_v = sqrt(kT/m)). This is accurate when kT << U0; samples
with harmonic energy above U0 (which would not be trapped) are discarded and
the discarded fraction is reported. Because the Gaussian well lies below its
harmonic approximation, every kept atom is bound at t = 0.

Fitting the recapture curve P(t) to simulations at different T is how
experiments measure single-atom temperatures (Tuchendler et al., PRA 2008).

Tweezer: 1064 nm, w0 = 1 um, U0 = kB x 1 mK (f_r = 98.5 kHz, f_z = 23.6 kHz).
Units: SI.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

kB = 1.380649e-23
m = 86.909180531 * 1.66053906660e-27
g = 9.80665
lam, w0 = 1064e-9, 1.0e-6
U0 = kB * 1e-3
zR = np.pi * w0**2 / lam
wr = np.sqrt(4 * U0 / (m * w0**2))
wz = np.sqrt(2 * U0 / (m * zR**2))
rng = np.random.default_rng(11)

N = 40000
# Fixed standard normals: every temperature reuses them (common random numbers),
# so the simulated curves are smooth functions of T and can be fitted.
Z = rng.standard_normal((6, N))


def U(x, y, z):
    wz2 = w0**2 * (1 + (z / zR)**2)
    return -U0 * (w0**2 / wz2) * np.exp(-2 * (x**2 + y**2) / wz2)


def sample(T):
    sx, sz, sv = np.sqrt(kB * T / (m * wr**2)), np.sqrt(kB * T / (m * wz**2)), np.sqrt(kB * T / m)
    x, y, z = sx * Z[0], sx * Z[1], sz * Z[2]       # tweezer axis along z, gravity along x
    vx, vy, vz = sv * Z[3], sv * Z[4], sv * Z[5]
    E_harm = 0.5 * m * (vx**2 + vy**2 + vz**2) + 0.5 * m * (wr**2 * (x**2 + y**2) + wz**2 * z**2)
    keep = E_harm < U0
    return (x, y, z, vx, vy, vz), keep, E_harm


def recapture(T, times):
    (x, y, z, vx, vy, vz), keep, _ = sample(T)
    P = []
    for t in times:
        xt = x + vx * t - 0.5 * g * t**2
        vxt = vx - g * t
        yt, zt = y + vy * t, z + vz * t
        E = 0.5 * m * (vxt**2 + vy**2 + vz**2) + U(xt, yt, zt)
        P.append(np.mean(E[keep] < 0))
    return np.array(P), 1 - keep.mean()


times = np.linspace(0, 60e-6, 31)
temps = [5e-6, 20e-6, 50e-6]
curves = {T: recapture(T, times) for T in temps}

# mean harmonic energy with no truncation should be 3 kB T (equipartition, 6 quadratic terms)
_, _, E20 = sample(20e-6)
E_mean, E_err = E20.mean() / (kB * 20e-6), E20.std() / np.sqrt(N) / (kB * 20e-6)

# synthetic experiment: T_true = 20 uK, 200 shots per release time
T_true, shots = 20e-6, 200
P_true, _ = recapture(T_true, times)
data = rng.binomial(shots, P_true) / shots
T_grid = np.arange(14e-6, 28.001e-6, 0.05e-6)
chi2 = []
for T in T_grid:
    Pm, _ = recapture(T, times)
    var = np.clip(Pm * (1 - Pm), 1e-3, None) / shots
    chi2.append(np.sum((data - Pm)**2 / var))
chi2 = np.array(chi2)
T_fit = T_grid[np.argmin(chi2)]
inside = T_grid[chi2 < chi2.min() + 1]
T_lo, T_hi = inside.min(), inside.max()

print("Release and recapture: 1064 nm, w0 = 1 um, U0 = 1 mK")
print("=" * 62)
print(f"trap frequencies f_r = {wr / 2 / np.pi / 1e3:.1f} kHz, f_z = {wz / 2 / np.pi / 1e3:.1f} kHz")
for T in temps:
    P, lost = curves[T]
    print(f"T = {T * 1e6:4.0f} uK: P(0) = {P[0]:.3f}, P(20 us) = {np.interp(20e-6, times, P):.3f}, "
          f"P(40 us) = {np.interp(40e-6, times, P):.3f}  (harmonic samples above U0: {lost * 100:.2f}%)")
print(f"mean harmonic energy at 20 uK = {E_mean:.4f} +/- {E_err:.4f} kB T (expect 3)")
print(f"fit to synthetic data (T_true = 20 uK, {shots} shots/point): T = {T_fit * 1e6:.2f} uK, "
      f"1-sigma range {T_lo * 1e6:.2f}-{T_hi * 1e6:.2f} uK")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
for T, col in zip(temps, ["C0", "C1", "C3"]):
    ax1.plot(times * 1e6, curves[T][0], color=col, lw=2, label=f"T = {T * 1e6:.0f} uK")
ax1.errorbar(times * 1e6, data, yerr=np.sqrt(data * (1 - data) / shots + 1e-6), fmt="ko", ms=3,
             capsize=2, label=f"synthetic data, {T_true * 1e6:.0f} uK")
ax1.set_xlabel("release time t (us)")
ax1.set_ylabel("recapture probability")
ax1.set_title("Hotter atoms fly away faster")
ax1.legend(fontsize=8)
ax2.plot(T_grid * 1e6, chi2 - chi2.min(), "k", lw=1.5)
ax2.axhline(1, color="C3", ls=":", lw=1)
ax2.axvline(T_true * 1e6, color="C2", ls="--", lw=1, label="true T")
ax2.set_xlabel("model temperature (uK)")
ax2.set_ylabel("chi^2 - chi^2_min")
ax2.set_ylim(0, 30)
ax2.set_xlim(14, 28)
ax2.set_title(f"Fit: T = {T_fit * 1e6:.1f} uK ({T_lo * 1e6:.1f} to {T_hi * 1e6:.1f})")
ax2.legend(fontsize=8)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "recapture.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
checks = {
    "every kept atom is recaptured at t = 0 (Gaussian well below its harmonic approximation)":
        all(curves[T][0][0] == 1.0 for T in temps),
    "untruncated thermal samples have mean energy 3 kB T (equipartition) within 4 s.e.":
        abs(E_mean - 3) < 4 * E_err,
    "recapture falls with release time and with temperature":
        all(np.all(np.diff(curves[T][0]) <= 1e-12) for T in temps)
        and np.all(curves[5e-6][0] >= curves[20e-6][0]) and np.all(curves[20e-6][0] >= curves[50e-6][0]),
    "fit to synthetic data recovers the true temperature (within 3 sigma and 10%)":
        abs(T_fit - T_true) <= 3 * (T_hi - T_lo) / 2 and abs(T_fit / T_true - 1) < 0.10,
}
