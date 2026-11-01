"""
Stochastic loading and atom-by-atom rearrangement of a tweezer array.

Physics / model
---------------
1. Loading. Light-assisted collisions remove atoms in pairs, so a tweezer that
   received a Poisson number N of atoms ends up with N mod 2 atoms. The
   probability of one atom is

       p1 = exp(-nbar) sinh(nbar) = (1 - exp(-2 nbar)) / 2  -> 1/2  for nbar >> 1.

   Each site of the array is then filled independently with probability p.

2. Rearrangement. A target block of N sites is to be filled. Every empty
   target site ("hole") is filled by moving one reservoir atom into it, chosen
   by a minimum-total-distance assignment (Hungarian algorithm). Each move
   succeeds with probability 1 - eps_move. During the whole cycle (duration
   t_cycle) every target atom can also be lost to background-gas collisions with
   lifetime tau_vac.

   Because each hole costs exactly one move, the success probability is
   independent of which reservoir atom is chosen:

       P_success = sum_h  Binom(h; N, 1-p) * Prob(reservoir >= h) * (1-eps)^h * exp(-N t/tau)

   with the reservoir a Binomial(M - N, p) number of atoms. Without
   rearrangement, P_success = p^N exp(-N t/tau).
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment
from scipy.stats import binom

rng = np.random.default_rng(5)

# ---------------------------------------------------------------------------
# 1) Loading: Poisson arrivals followed by pairwise loss
# ---------------------------------------------------------------------------
nbar_values = np.array([0.25, 0.5, 1.0, 2.0, 4.0])
n_sites_load = 200000
p1_mc = np.array([np.mean(rng.poisson(nb, n_sites_load) % 2) for nb in nbar_values])
p1_th = 0.5 * (1 - np.exp(-2 * nbar_values))

p = 0.5                            # single-atom loading probability per site
occ = rng.random(n_sites_load) < p
load_mean, load_var = occ.mean(), occ.var()

# ---------------------------------------------------------------------------
# 2) 2D rearrangement with the Hungarian algorithm
# ---------------------------------------------------------------------------
eps_move = 0.01        # loss probability per move
tau_vac = 60.0         # s, vacuum-limited lifetime
t_cycle = 0.20         # s, time from loading image to final image


def rearrange_2d(L, n_target):
    """One realisation on an L x L grid with a central n_target x n_target block."""
    grid = rng.random((L, L)) < p
    start = (L - n_target) // 2
    tgt = np.zeros((L, L), bool)
    tgt[start:start + n_target, start:start + n_target] = True
    holes = np.argwhere(tgt & ~grid)
    reservoir = np.argwhere(~tgt & grid)
    if len(reservoir) < len(holes):
        return False, grid, None, len(holes)
    final = grid.copy()
    if len(holes):
        cost = np.linalg.norm(holes[:, None, :] - reservoir[None, :, :], axis=2)
        rows, cols = linear_sum_assignment(cost)
        for hi, ri in zip(rows, cols):
            final[tuple(reservoir[ri])] = False
            final[tuple(holes[hi])] = rng.random() > eps_move     # move may fail
    survive = rng.random((L, L)) < np.exp(-t_cycle / tau_vac)
    final &= survive
    return bool(np.all(final[tgt])), grid, final, len(holes)


def p_success_analytic(N, M):
    h = np.arange(N + 1)
    return np.sum(binom.pmf(h, N, 1 - p) * binom.sf(h - 1, M - N, p)
                  * (1 - eps_move)**h) * np.exp(-N * t_cycle / tau_vac)


cases = [(8, 5), (12, 8), (16, 10), (20, 13)]        # (L, side of target)
n_trials = 1500
results = []
for L, nt in cases:
    succ = np.array([rearrange_2d(L, nt)[0] for _ in range(n_trials)])
    P_mc = succ.mean()
    err = np.sqrt(max(P_mc * (1 - P_mc), 1 / n_trials) / n_trials)
    P_th = p_success_analytic(nt * nt, L * L)
    results.append((L, nt, P_mc, err, P_th, p**(nt * nt) * np.exp(-nt * nt * t_cycle / tau_vac)))

print("Loading and rearrangement")
print("=" * 70)
for nb, a, b in zip(nbar_values, p1_mc, p1_th):
    print(f"nbar = {nb:4.2f}: P(single atom) MC = {a:.4f}, (1 - exp(-2 nbar))/2 = {b:.4f}")
print(f"site occupation: mean {load_mean:.4f} (p = {p}), variance {load_var:.4f} (p(1-p) = {p * (1 - p):.4f})")
print(f"move loss {eps_move}, vacuum lifetime {tau_vac:.0f} s, cycle {t_cycle} s")
print(" grid   target   N    P_success MC       analytic   no rearrangement")
for L, nt, a, e, b, c in results:
    print(f" {L:2d}x{L:<2d}  {nt:2d}x{nt:<2d}  {nt * nt:3d}   {a:.3f} +/- {e:.3f}    {b:.3f}      {c:.1e}")

# ---------------------------------------------------------------------------
# Figure: one example before/after, and success versus N
# ---------------------------------------------------------------------------
ok, before, after, nh = rearrange_2d(16, 10)
while after is None:
    ok, before, after, nh = rearrange_2d(16, 10)
fig, axes = plt.subplots(1, 3, figsize=(14, 4.3))
for ax, g, title in [(axes[0], before, f"after loading: {before.sum()} atoms in 256 traps"),
                     (axes[1], after, f"after rearrangement ({nh} moves)")]:
    yy, xx = np.nonzero(g)
    ax.scatter(xx, yy, s=28, c="C0")
    ax.add_patch(plt.Rectangle((2.5, 2.5), 10, 10, fill=False, ec="C3", lw=1.5))
    ax.set_xlim(-1, 16)
    ax.set_ylim(-1, 16)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=9)
N_axis = np.arange(1, 1001)
axes[2].semilogy(N_axis, p**N_axis, "k--", lw=1.2, label="no rearrangement, p^N")
for eps, tau, col in [(0.01, 60, "C0"), (0.003, 60, "C2"), (0.003, 600, "C1")]:
    Pr = np.array([np.sum(binom.pmf(np.arange(n + 1), n, 1 - p) * (1 - eps)**np.arange(n + 1))
                   * np.exp(-n * t_cycle / tau) for n in N_axis[::10]])
    axes[2].semilogy(N_axis[::10], Pr, color=col, lw=2, label=f"rearranged: eps = {eps}, tau = {tau} s")
axes[2].plot([nt * nt for _, nt, *_ in results], [r[2] for r in results], "ko", ms=4, label="Monte Carlo (lab)")
axes[2].set_ylim(1e-6, 1.5)
axes[2].set_xlabel("number of target sites N")
axes[2].set_ylabel("probability of a defect-free array")
axes[2].set_title("Rearrangement beats p^N, but losses still compound", fontsize=9)
axes[2].legend(fontsize=7, loc="lower left")
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "rearrange.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
se_p1 = np.sqrt(p1_th * (1 - p1_th) / n_sites_load)
checks = {
    "parity of a Poisson number reproduces (1 - exp(-2 nbar))/2 within 4 s.e.":
        np.all(np.abs(p1_mc - p1_th) < 4 * se_p1),
    "site occupation has binomial mean p and variance p(1-p)":
        abs(load_mean - p) < 4 * np.sqrt(p * (1 - p) / n_sites_load) and abs(load_var - p * (1 - p)) < 0.002,
    "Monte Carlo success matches the exact hole-counting formula within 4 s.e.":
        all(abs(a - b) < 4 * e for _, _, a, e, b, _ in results),
    "rearrangement beats p^N by many orders of magnitude for N >= 25":
        all(b > 1e6 * c for _, nt, _, _, b, c in results if nt * nt >= 25),
}
