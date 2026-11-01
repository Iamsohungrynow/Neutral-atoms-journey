"""
Analog quantum simulation: adiabatic preparation of the Z2 ordered phase in a
chain of Rydberg atoms.

Physics
-------
N atoms on a line with spacing a, each a two-level system {|g>, |r>}, evolve
under the Rydberg Hamiltonian of Chapter 10 (hbar = 1, n_i = |r><r|_i):

    H(t) = sum_i (Omega(t)/2) sigma_x^i - Delta(t) sum_i n_i + sum_{i<j} V_ij n_i n_j,
    V_ij = C6 / (a |i - j|)^6.

With a = 6 um and Rb-87 70S (C6/h = 862.7 GHz um^6), nearest neighbours are
blockaded (V_1/h = 18.5 MHz >> Omega/2pi = 2 MHz) while next-nearest
neighbours barely interact (V_2/h = 0.29 MHz). At large negative Delta the
ground state is all atoms in |g>; at positive Delta (but below V_1) it is the
"Z2" crystal r g r g ... r, one excitation on every other site. Sweeping Delta
slowly from negative to positive while Omega is on follows the instantaneous
ground state (adiabatic theorem) and prepares the crystal; sweeping too fast
creates defects, because the energy gap closes near the phase transition.

This is the protocol of the 51-atom experiment of Bernien et al. (2017); here
N = 9 so that the full 2^9 = 512-dimensional state can be evolved exactly.
Units: time in us, angular frequencies in rad/us, lengths in um.
"""

import os
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

N = 9
a = 6.0
C6 = 2 * np.pi * 862.7e3
Omega_max = 2 * np.pi * 2.0
Delta_start, Delta_end = -2 * np.pi * 6.0, 2 * np.pi * 8.0

dim = 2**N
states = np.arange(dim)
occ = ((states[:, None] >> np.arange(N)[::-1]) & 1).astype(float)   # occ[s, i] = n_i in basis state s

# diagonal parts
n_tot = occ.sum(axis=1)
V_diag = np.zeros(dim)
for i in range(N):
    for j in range(i + 1, N):
        V_diag += C6 / (a * (j - i))**6 * occ[:, i] * occ[:, j]

# sigma_x sum (off-diagonal, flips one bit)
rows, cols = [], []
for i in range(N):
    flipped = states ^ (1 << (N - 1 - i))
    rows.append(states)
    cols.append(flipped)
SX = sp.csr_matrix((np.ones(N * dim), (np.concatenate(rows), np.concatenate(cols))), shape=(dim, dim))


def H(Om, De):
    return 0.5 * Om * SX + sp.diags(-De * n_tot + V_diag)


def schedule(t, T):
    """Omega ramps on/off over 10% of T each; Delta sweeps linearly while Omega is at its maximum."""
    tr = 0.1 * T
    if t < tr:
        return Omega_max * t / tr, Delta_start
    if t > T - tr:
        return Omega_max * (T - t) / tr, Delta_end
    return Omega_max, Delta_start + (Delta_end - Delta_start) * (t - tr) / (T - 2 * tr)


def sweep(T, steps=400):
    psi = np.zeros(dim, complex)
    psi[0] = 1.0                       # all atoms in |g>
    dt = T / steps
    for k in range(steps):
        Om, De = schedule((k + 0.5) * dt, T)
        psi = expm_multiply(-1j * H(Om, De) * dt, psi)
    return psi


z2_index = int("".join("1" if i % 2 == 0 else "0" for i in range(N)), 2)
adjacent = (occ[:, :-1] * occ[:, 1:]).sum(axis=1) > 0      # any two neighbours both excited
allowed = ~adjacent
fib = [1, 1]
for _ in range(N + 1):
    fib.append(fib[-1] + fib[-2])

# classical ground state of the final Hamiltonian (Omega = 0)
E_classical = -Delta_end * n_tot + V_diag
gs_classical = int(np.argmin(E_classical))

# instantaneous spectrum along the sweep (Omega = Omega_max)
Deltas = np.linspace(Delta_start, Delta_end, 41)
# The drive starts in |gg...g>, which is symmetric under reflecting the chain, and H keeps that symmetry,
# so only reflection-symmetric excited states matter: compute the gap within that sector.
P = np.zeros(dim, int)
for s in range(dim):
    P[s] = int(format(s, f"0{N}b")[::-1], 2)
R = sp.csr_matrix((np.ones(dim), (states, P)), shape=(dim, dim))


def symmetric_gap(De):
    Hs = H(Omega_max, De).toarray()
    Rs = R.toarray()
    # project onto the reflection-symmetric subspace
    proj = (np.eye(dim) + Rs) / 2
    w, v = np.linalg.eigh(proj @ Hs @ proj + 1e3 * (np.eye(dim) - proj))
    return w[1] - w[0]


gaps_sym = np.array([symmetric_gap(De) for De in Deltas])
gap_min = gaps_sym.min()

times = [0.5, 1.0, 2.0, 4.0, 8.0]
results = {}
for T in times:
    psi = sweep(T)
    p = np.abs(psi)**2
    results[T] = dict(P_z2=p[z2_index], leak=p[adjacent].sum(), n_mean=(p * n_tot).sum(),
                      profile=(p[:, None] * occ).sum(axis=0))

print(f"Adiabatic Z2 preparation, N = {N}, a = {a} um, Omega/2pi = 2 MHz (Rb 70S)")
print("=" * 70)
print(f"V1/h = {C6 / a**6 / 2 / np.pi:.2f} MHz, V2/h = {C6 / (2 * a)**6 / 2 / np.pi:.3f} MHz")
print(f"blockade-allowed configurations: {allowed.sum()} (Fibonacci F(N+2) = {fib[N + 1]})")
print(f"classical ground state at Delta_end: {format(gs_classical, f'0{N}b')} (Z2 = {format(z2_index, f'0{N}b')})")
print(f"minimum gap in the symmetric sector: {gap_min / 2 / np.pi:.3f} MHz at Delta/2pi = "
      f"{Deltas[np.argmin(gaps_sym)] / 2 / np.pi:.2f} MHz")
print(" sweep time (us)   P(Z2)   P(adjacent pair)   <n_Rydberg>")
for T in times:
    r = results[T]
    print(f"     {T:5.2f}        {r['P_z2']:.3f}       {r['leak']:.2e}          {r['n_mean']:.3f}")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(14.5, 4.2))
ax = axes[0]
ax.plot(Deltas / 2 / np.pi, gaps_sym / 2 / np.pi, "C0", lw=2)
ax.set_xlabel("detuning Delta / 2pi (MHz)")
ax.set_ylabel("gap to the first symmetric excited state (MHz)")
ax.set_title("The gap closes near the transition", fontsize=9)
ax = axes[1]
ax.semilogx(times, [results[T]["P_z2"] for T in times], "o-", color="C3", lw=2)
ax.set_xticks(times)
ax.set_xticklabels([f"{T:g}" for T in times])
ax.minorticks_off()
ax.set_xlabel("sweep time T (us)")
ax.set_ylabel("probability of the perfect Z2 crystal")
ax.set_ylim(0, 1)
ax.set_title("Slower sweeps make fewer defects", fontsize=9)
ax = axes[2]
for T, col in zip([0.5, 2.0, 8.0], ["C1", "C2", "C0"]):
    ax.bar(np.arange(N) + {0.5: -0.27, 2.0: 0.0, 8.0: 0.27}[T], results[T]["profile"], width=0.27,
           color=col, label=f"T = {T} us")
ax.set_xlabel("site")
ax.set_ylabel("Rydberg population <n_i>")
ax.set_title("Final density profile: r g r g ... r", fontsize=9)
ax.set_ylim(0, 1.25)
ax.legend(fontsize=8, ncol=3, loc="upper center")
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "z2_sweep.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
checks = {
    "number of blockade-allowed configurations equals the Fibonacci number F(N+2)":
        allowed.sum() == fib[N + 1],
    "classical ground state at the end of the sweep is the Z2 crystal":
        gs_classical == z2_index,
    "nearest-neighbour blockade holds: P(adjacent pair) < 1e-2 for sweeps of 1 us or longer":
        all(results[T]["leak"] < 1e-2 for T in times if T >= 1.0),
    "adiabaticity: P(Z2) increases with sweep time and exceeds 0.9 for the slowest sweep":
        all(np.diff([results[T]["P_z2"] for T in times]) > 0) and results[times[-1]]["P_z2"] > 0.9,
}
