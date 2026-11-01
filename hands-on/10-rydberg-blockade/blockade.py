"""
Rydberg blockade: two atoms versus distance, collective sqrt(N) enhancement,
and Rydberg scaling laws.

Physics
-------
Each atom is a two-level system {|g>, |r>} driven resonantly with Rabi
frequency Omega. Two atoms at distance R in |r>|r> interact with the van der
Waals energy V(R) = C6 / R^6. With hbar = 1 and n_i = |r><r|_i:

    H = (Omega/2) (sigma_x^(1) + sigma_x^(2)) + V(R) n_1 n_2

* V = 0 (far apart): independent Rabi flopping, P(rr) = sin^4(Omega t / 2).
* V >> Omega (blockade): |rr> is shifted out of resonance; |gg> couples only
  to |W> = (|gr> + |rg>)/sqrt(2) with matrix element sqrt(2) Omega/2, so the
  pair oscillates at sqrt(2) Omega. The residual double-excitation probability
  scales as (Omega/V)^2. With N mutually blockaded atoms the collective Rabi
  frequency is sqrt(N) Omega.
* Blockade radius R_b = (C6 / hbar Omega)^(1/6): where V(R_b) = hbar Omega.

C6/h = 862.7 GHz um^6 for Rb-87 70S1/2 (repulsive), computed with ARC.
Units: time in us, frequencies in MHz, angular quantities in rad/us, R in um.
"""

import os
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

C6 = 2 * np.pi * 862.7e3          # rad/us * um^6
Omega = 2 * np.pi * 2.0           # rad/us
R_b = (C6 / Omega)**(1 / 6)

sx = np.array([[0, 1], [1, 0]], complex)
nr = np.array([[0, 0], [0, 1]], complex)
I2 = np.eye(2)


def op(single, i, N):
    return reduce(np.kron, [single if k == i else I2 for k in range(N)])


def H_chain(N, V):
    """N atoms, all pairs interacting with the same V (fully blockaded cluster)."""
    H = sum(0.5 * Omega * op(sx, i, N) for i in range(N))
    for i in range(N):
        for j in range(i + 1, N):
            H = H + V * op(nr, i, N) @ op(nr, j, N)
    return H


def evolve(H, times):
    psi0 = np.zeros(H.shape[0], complex)
    psi0[0] = 1.0
    w, U = np.linalg.eigh(H)
    c = U.conj().T @ psi0
    return np.array([U @ (np.exp(-1j * w * t) * c) for t in times])


times = np.linspace(0, 1.5, 1501)
nrr = op(nr, 0, 2) @ op(nr, 1, 2)
n_tot = op(nr, 0, 2) + op(nr, 1, 2)


def pair_traces(R):
    V = C6 / R**6
    psi = evolve(H_chain(2, V), times)
    P_rr = np.real(np.einsum("ti,ij,tj->t", psi.conj(), nrr, psi))
    N_r = np.real(np.einsum("ti,ij,tj->t", psi.conj(), n_tot, psi))
    return P_rr, N_r, V


def dominant_freq(signal, t):
    """Fit A sin^2(w t / 2) and return the angular frequency w."""
    d = np.diff(signal)
    first_max = np.where((d[:-1] > 0) & (d[1:] <= 0) & (signal[1:-1] > 0.5 * signal.max()))[0][0] + 1
    guess = np.pi / t[first_max]                    # first maximum where w t = pi
    (A, w), _ = curve_fit(lambda t, A, w: A * np.sin(w * t / 2)**2, t, signal, p0=[signal.max(), guess])
    return abs(w)


P_far, N_far, _ = pair_traces(1e3)
P_4, N_4, V4 = pair_traces(4.0)
R2 = 4.0 * 2**(1 / 6)                      # interaction halved
P_4b, _, V4b = pair_traces(R2)
w_blockade = dominant_freq(N_4, times)

# collective enhancement for N = 1..4 strongly blockaded atoms
coll = {}
for N in (1, 2, 3, 4):
    H = H_chain(N, 2 * np.pi * 5000.0)    # V/h = 5 GHz >> Omega
    psi = evolve(H, times)
    ntot = sum(op(nr, i, N) for i in range(N))
    Nr = np.real(np.einsum("ti,ij,tj->t", psi.conj(), ntot, psi))
    coll[N] = dominant_freq(Nr, times) / Omega

# Rydberg scaling from ARC (Rb-87 nS1/2): n, n*, binding (meV), tau0 (us), tau300 (us), C6/h (GHz um^6)
ARC = np.array([
    (40, 36.8687, -10.00927, 62.65, 34.48, 0.9984),
    (50, 46.8687, -6.19372, 128.71, 62.35, 15.44),
    (60, 56.8688, -4.20698, 229.95, 99.52, 138.9),
    (70, 66.8688, -3.04278, 373.87, 146.25, 862.7),
    (80, 76.8688, -2.30260, 567.98, 202.71, 4162),
    (90, 86.8688, -1.80298, 819.79, 269.03, 1.65e4),
    (100, 96.8688, -1.44994, 1136.80, 345.30, 5.617e4)])
nstar = ARC[:, 1]
slope = lambda y: np.polyfit(np.log(nstar), np.log(np.abs(y)), 1)[0]
exp_bind, exp_tau, exp_c6 = slope(ARC[:, 2]), slope(ARC[:, 3]), slope(ARC[:, 5])

print("Rydberg blockade, Rb-87 70S, Omega/2pi = 2 MHz")
print("=" * 64)
print(f"blockade radius R_b = (C6/hbar Omega)^(1/6) = {R_b:.2f} um")
print(f"R = 4.00 um: V/h = {V4 / 2 / np.pi:8.1f} MHz, max P(rr) = {P_4.max():.2e}")
print(f"R = {R2:.2f} um: V/h = {V4b / 2 / np.pi:8.1f} MHz, max P(rr) = {P_4b.max():.2e} "
      f"(ratio {P_4b.max() / P_4.max():.2f}, expect 4)")
print(f"blockaded pair oscillates at {w_blockade / Omega:.4f} Omega (expect sqrt 2 = {np.sqrt(2):.4f})")
print("collective Rabi frequency / Omega: " + ", ".join(f"N={N}: {v:.3f}" for N, v in coll.items()))
print(f"ARC scaling exponents vs n*: binding {exp_bind:.2f} (theory -2), "
      f"tau0 {exp_tau:.2f} (theory 3), C6 {exp_c6:.2f} (theory 11)")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.2))
ax = axes[0]
ax.plot(times, N_far / 2, "C0", lw=1.5, label="R = 1 mm: <n> per atom (independent)")
ax.plot(times, N_4, "C3", lw=2, label="R = 4 um: total Rydberg number (blockaded)")
ax.plot(times, P_4 * 1000, "k:", lw=1, label="R = 4 um: P(rr) x 1000")
ax.set_xlabel("time (us)")
ax.set_ylabel("Rydberg population")
ax.set_title("Blockade: one shared excitation, sqrt(2) faster", fontsize=9)
ax.legend(fontsize=7, loc="upper right")
ax.set_ylim(0, 1.25)
ax = axes[1]
Rs = np.linspace(3, 16, 200)
Pmax = [pair_traces(R)[0].max() for R in Rs]
ax.semilogy(Rs, Pmax, "C2", lw=2)
ax.axvline(R_b, color="k", ls="--", lw=1)
ax.text(R_b + 0.2, 2e-4, f"R_b = {R_b:.1f} um", fontsize=8)
ax.set_xlabel("interatomic distance R (um)")
ax.set_ylabel("maximum P(rr) during 1.5 us")
ax.set_title("Double excitation is suppressed inside R_b", fontsize=9)
ax = axes[2]
ax.loglog(nstar, ARC[:, 5], "o-", color="C3", label="C6/h (GHz um^6)")
ax.loglog(nstar, ARC[:, 3], "s-", color="C0", label="lifetime at 0 K (us)")
ax.loglog(nstar, ARC[:, 4], "s--", color="C0", alpha=0.6, label="lifetime at 300 K (us)")
ax.loglog(nstar, -ARC[:, 2], "^-", color="C2", label="binding energy (meV)")
ax.set_xlabel("effective principal quantum number n*")
ax.set_title(f"Scaling (ARC): C6 ~ n*^{exp_c6:.1f}, tau ~ n*^{exp_tau:.1f}", fontsize=9)
ax.legend(fontsize=7)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "blockade.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
checks = {
    "far-apart atoms flop independently: P(rr) = sin^4(Omega t/2)":
        np.allclose(P_far, np.sin(Omega * times / 2)**4, atol=1e-6),
    "blockaded pair oscillates at sqrt(2) Omega (0.5%)": abs(w_blockade / Omega / np.sqrt(2) - 1) < 5e-3,
    "residual double excitation scales as (Omega/V)^2 (halving V gives x4 within 10%)":
        abs(P_4b.max() / P_4.max() / 4 - 1) < 0.10,
    "N blockaded atoms oscillate at sqrt(N) Omega (1%)":
        all(abs(v / np.sqrt(N) - 1) < 0.01 for N, v in coll.items()),
    "ARC data follow binding ~ n*^-2, tau0 ~ n*^3, C6 ~ n*^11 (C6 exponent within 10.5-12)":
        abs(exp_bind + 2) < 0.01 and abs(exp_tau - 3) < 0.05 and 10.5 < exp_c6 < 12,
}
