"""
Why erasures are easier: a repetition code with Pauli errors versus erasures.

Model
-----
A logical bit is stored in d physical bits (d odd). Each bit independently
suffers, with total probability p,

  * an erasure with probability R_e * p: the bit is lost and we KNOW which one
    (in neutral atoms: an atom found missing, or a decay detected by a
    fluorescence check);
  * a Pauli (bit-flip) error with probability (1 - R_e) * p: the bit is wrong
    and we do NOT know it.

Decoder: majority vote over the non-erased bits; a tie, or all bits erased,
is decided by a coin toss (counted as failure with probability 1/2).

Exact logical error, summing over the numbers of erasures e and flips f:

  P_L = sum_{e,f} Multinomial(e, f) * [ 1 if f > (d-e)/2, 1/2 if f = (d-e)/2, else 0 ]

Limits:  pure Pauli (R_e = 0), d = 3:  P_L = 3p^2 - 2p^3      (~ p^((d+1)/2))
         pure erasure (R_e = 1):        P_L = p^d / 2            (~ p^d)
so converting errors into erasures roughly doubles the effective code distance.
"""

import os
from math import comb, factorial
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(12)


def p_logical(d, p, Re):
    pe, pf, pk = Re * p, (1 - Re) * p, 1 - p
    total = 0.0
    for e in range(d + 1):
        for f in range(d - e + 1):
            k = d - e - f
            w = factorial(d) / (factorial(e) * factorial(f) * factorial(k)) * pe**e * pf**f * pk**k
            n = d - e
            if 2 * f > n:
                total += w
            elif 2 * f == n:
                total += 0.5 * w
    return total


def p_logical_mc(d, p, Re, shots):
    u = rng.random((shots, d))
    erased = u < Re * p
    flipped = (u >= Re * p) & (u < p)
    n = d - erased.sum(axis=1)
    f = flipped.sum(axis=1)
    fail = (2 * f > n).astype(float)
    tie = 2 * f == n
    fail[tie] = rng.random(tie.sum()) < 0.5
    return fail.mean()


ps = np.logspace(-3, -0.3, 40)
ds = [3, 5, 7]
models = {"Pauli only (R_e = 0)": 0.0, "98% erasures (R_e = 0.98)": 0.98, "erasure only (R_e = 1)": 1.0}

# Monte Carlo spot checks
shots = 400000
spot = []
for d in ds:
    for name, Re in models.items():
        p = 0.1
        mc = p_logical_mc(d, p, Re, shots)
        th = p_logical(d, p, Re)
        se = np.sqrt(max(th * (1 - th), 1 / shots) / shots)
        spot.append((d, name, mc, th, se))


def slope(d, Re, p1=1e-3, p2=2e-3):
    return np.log(p_logical(d, p2, Re) / p_logical(d, p1, Re)) / np.log(p2 / p1)


print("Repetition code: Pauli errors versus erasures")
print("=" * 70)
print(" d   model                         P_L MC (p = 0.1)      exact")
for d, name, mc, th, se in spot:
    print(f" {d}   {name:28s}  {mc:.3e} +/- {se:.1e}   {th:.3e}")
print("small-p slope d ln P_L / d ln p (effective distance):")
for d in ds:
    print(f"   d = {d}: Pauli {slope(d, 0.0):.2f} (expect {(d + 1) / 2}), erasure {slope(d, 1.0):.2f} "
          f"(expect {d}), 98% erasure {slope(d, 0.98):.2f}")
print(f"at p = 1e-2, d = 5: Pauli {p_logical(5, 1e-2, 0):.2e}, 98% erasure {p_logical(5, 1e-2, 0.98):.2e}, "
      f"erasure {p_logical(5, 1e-2, 1):.2e}")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.3))
styles = {0.0: "-", 0.98: "--", 1.0: ":"}
for d, col in zip(ds, ["C0", "C1", "C3"]):
    for name, Re in models.items():
        ax1.loglog(ps, [p_logical(d, p, Re) for p in ps], styles[Re], color=col, lw=1.8,
                   label=f"d = {d}, {name}" if d == 5 or Re == 0.0 else None)
ax1.loglog(ps, ps, "k", lw=0.8, alpha=0.5, label="unencoded bit")
ax1.set_xlabel("physical error probability p")
ax1.set_ylabel("logical error probability")
ax1.set_ylim(1e-14, 1)
ax1.set_title("Solid: Pauli; dashed: 98% erasure; dotted: pure erasure", fontsize=9)
ax1.legend(fontsize=7, loc="lower right")
Re_axis = np.linspace(0, 1, 101)
for d, col in zip(ds, ["C0", "C1", "C3"]):
    ax2.semilogy(Re_axis, [p_logical(d, 1e-2, r) for r in Re_axis], color=col, lw=2, label=f"d = {d}")
ax2.set_xlabel("erasure fraction R_e")
ax2.set_ylabel("logical error at p = 0.01")
ax2.set_title("Converting errors into erasures pays off steeply near R_e = 1", fontsize=9)
ax2.legend(fontsize=8)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "erasure.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
pp = np.linspace(0.001, 0.5, 50)
checks = {
    "Monte Carlo agrees with the exact sum for every d and model (4 s.e.)":
        all(abs(mc - th) < 4 * se for _, _, mc, th, se in spot),
    "pure Pauli, d = 3, equals 3p^2 - 2p^3":
        np.allclose([p_logical(3, p, 0.0) for p in pp], 3 * pp**2 - 2 * pp**3, atol=1e-14),
    "pure erasure equals p^d / 2 for d = 3, 5, 7":
        all(np.allclose([p_logical(d, p, 1.0) for p in pp], pp**d / 2, rtol=1e-12) for d in ds),
    "effective distance: slope (d+1)/2 for Pauli and d for erasure (5%)":
        all(abs(slope(d, 0.0) / ((d + 1) / 2) - 1) < 0.05 and abs(slope(d, 1.0) / d - 1) < 0.05 for d in ds),
}
