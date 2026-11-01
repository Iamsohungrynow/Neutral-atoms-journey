"""
Ramsey dephasing of a hyperfine qubit by thermal motion in a tweezer, and spin echo.

Physics
-------
The trap light shifts |1> = |F=2,mF=0> slightly more than |0> = |F=1,mF=0>:
the qubit frequency changes by a fraction eta of the local light shift. An
atom at the bottom of the trap sees the full depth; an atom with motional
energy E spends its time higher in the well, where the intensity is lower.
In a harmonic trap the time-averaged potential energy is E/2, so the atom's
qubit frequency is offset by

    delta(E) = eta * E / (2 hbar)        (relative to an atom at rest at the bottom)

For a thermal (Boltzmann) ensemble in 3D, E has the distribution
E^2 exp(-E/kT) and the Ramsey contrast is

    C(t) = | < exp(i delta(E) t) > | = [1 + (eta kB T t / 2 hbar)^2]^(-3/2)
         = [1 + 0.95 (t/T2*)^2]^(-3/2),   T2* = sqrt(e^(2/3) - 1) * 2 hbar / (eta kB T),

the result of Kuhr et al., PRA 72, 023406 (2005). Here we do NOT assume the
time average: each atom follows its exact classical harmonic trajectory, and
the accumulated phase (eta/hbar) * integral V(t) dt is computed in closed form.

Spin echo: a pi pulse at t/2 reverses the sign of the phase accumulated
afterwards, so any shift that is constant during the sequence cancels.

Parameters: Rb-87 in an 852 nm, 1 mK tweezer (f_r = 98.5 kHz, f_z = 18.9 kHz),
eta = 2.258e-4 from the two-line model of Chapter 07. Units: SI.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

hbar = 1.054571817e-34
kB = 1.380649e-23
eta = 2.258e-4
omegas = 2 * np.pi * np.array([98.5e3, 98.5e3, 18.9e3])
rng = np.random.default_rng(9)
N = 60000
Z = rng.standard_normal((2, 3, N))          # reused for every temperature


def energies_and_phases(T):
    """Energy per axis (J) and oscillation phase for thermal harmonic motion."""
    m = 86.909180531 * 1.66053906660e-27
    x = np.sqrt(kB * T / (m * omegas[:, None]**2)) * Z[0]
    v = np.sqrt(kB * T / m) * Z[1]
    E = 0.5 * m * v**2 + 0.5 * m * omegas[:, None]**2 * x**2
    phi = np.arctan2(-v, omegas[:, None] * x)        # x = A cos(w t + phi)
    return E, phi


def V_integral(E, phi, t0, t1):
    """Exact integral of V(t) = E cos^2(w t + phi) from t0 to t1, summed over axes."""
    w = omegas[:, None]
    F = lambda t: E * (t / 2 + (np.sin(2 * (w * t + phi))) / (4 * w))
    return (F(t1) - F(t0)).sum(axis=0)


def contrast(T, times, echo=False):
    E, phi = energies_and_phases(T)
    out = []
    for t in times:
        if echo:
            ph = eta / hbar * (V_integral(E, phi, 0, t / 2) - V_integral(E, phi, t / 2, t))
        else:
            ph = eta / hbar * V_integral(E, phi, 0, t)
        out.append(abs(np.mean(np.exp(1j * ph))))
    return np.array(out)


def T2star(T):
    return np.sqrt(np.exp(2 / 3) - 1) * 2 * hbar / (eta * kB * T)


def kuhr(t, T):
    return (1 + (np.exp(2 / 3) - 1) * (t / T2star(T))**2)**-1.5


temps = [5e-6, 10e-6, 20e-6]
times = np.linspace(0, 40e-3, 161)
ram = {T: contrast(T, times) for T in temps}
echo = contrast(10e-6, times, echo=True)


def one_over_e(t, c):
    i = np.where(c < np.exp(-1))[0][0]
    return np.interp(np.exp(-1), [c[i], c[i - 1]], [t[i], t[i - 1]])


T2_fit = {T: one_over_e(times, ram[T]) for T in temps}

print("Ramsey dephasing from thermal differential light shifts (852 nm, eta = 2.258e-4)")
print("=" * 72)
for T in temps:
    print(f"T = {T * 1e6:4.0f} uK: T2* from simulation = {T2_fit[T] * 1e3:6.2f} ms, "
          f"Kuhr formula 0.97 * 2 hbar/(eta kB T) = {T2star(T) * 1e3:6.2f} ms")
print(f"ratio T2*(5 uK)/T2*(20 uK) = {T2_fit[5e-6] / T2_fit[20e-6]:.3f} (expect 4)")
print(f"spin-echo contrast at t = 40 ms, 10 uK: {echo[-1]:.4f} (Ramsey: {ram[10e-6][-1]:.4f})")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
for T, col in zip(temps, ["C0", "C1", "C3"]):
    ax1.plot(times * 1e3, ram[T], color=col, lw=2, label=f"Ramsey, {T * 1e6:.0f} uK (simulation)")
    ax1.plot(times[::8] * 1e3, kuhr(times[::8], T), "o", color=col, ms=3)
ax1.plot(times * 1e3, echo, "k--", lw=1.5, label="spin echo, 10 uK")
ax1.set_xlabel("total free-evolution time (ms)")
ax1.set_ylabel("Ramsey contrast")
ax1.set_title("Thermal dephasing (dots: Kuhr et al. formula)", fontsize=9)
ax1.set_ylim(0, 1.05)
ax1.legend(fontsize=8)
Tg = np.linspace(2e-6, 40e-6, 200)
for lam, e, col in [(852, 2.258e-4, "C3"), (1064, 6.083e-5, "C0")]:
    ax2.loglog(Tg * 1e6, np.sqrt(np.exp(2 / 3) - 1) * 2 * hbar / (e * kB * Tg) * 1e3, color=col, lw=2,
               label=f"{lam} nm, eta = {e:.2e}")
ax2.loglog([T * 1e6 for T in temps], [T2_fit[T] * 1e3 for T in temps], "ko", ms=4, label="simulation (852 nm)")
ax2.set_xlabel("atom temperature (uK)")
ax2.set_ylabel("T2* (ms)")
ax2.set_title("T2* = 0.97 x 2 hbar / (eta kB T): colder and farther detuned is better", fontsize=9)
ax2.legend(fontsize=8)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "ramsey.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
se = 1 / np.sqrt(N)
checks = {
    "exact-trajectory Ramsey contrast matches [1 + 0.95 (t/T2*)^2]^-1.5 within 4/sqrt(N)":
        all(np.max(np.abs(ram[T] - kuhr(times, T))) < 4 * se for T in temps),
    "1/e time equals 0.97 * 2 hbar/(eta kB T) within 3%":
        all(abs(T2_fit[T] / T2star(T) - 1) < 0.03 for T in temps),
    "T2* scales as 1/T (ratio 4 between 5 and 20 uK, within 3%)":
        abs(T2_fit[5e-6] / T2_fit[20e-6] / 4 - 1) < 0.03,
    "spin echo removes the static thermal dephasing (contrast > 0.99 at 40 ms)":
        echo.min() > 0.99,
}
