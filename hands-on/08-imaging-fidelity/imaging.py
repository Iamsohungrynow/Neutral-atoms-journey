"""
Single-atom fluorescence imaging: photon histograms, threshold and fidelity.

Model
-----
During an exposure of length t_exp an atom scatters photons at rate R_sc; a
fraction eta_det of them is detected. The camera region of one tweezer also
collects a Poisson background of mean mu_b. So the detected count is

    empty site :  n ~ Poisson(mu_b)
    full site  :  n ~ Poisson(mu_b + eta_det R_sc t_on),

where t_on = min(t_loss, t_exp) and the atom may be lost during imaging after
an exponentially distributed time t_loss with mean tau_loss. A site is called
"full" if n >= threshold. The assignment fidelity is

    F = 1 - [P(n >= th | empty) + P(n < th | full)] / 2

(equal prior probabilities, as for 50% loading).

Without loss, the optimal threshold is where the two Poisson pmfs cross,
th* = ceil( mu_s / ln(1 + mu_s/mu_b) ),  with mu_s = eta_det R_sc t_exp.

The collection efficiency of a lens of numerical aperture NA for isotropic
emission is the solid-angle fraction (1 - cos theta)/2 with sin theta = NA.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

rng = np.random.default_rng(8)

NA = 0.5
coll = (1 - np.sqrt(1 - NA**2)) / 2          # solid-angle fraction
transmission, qe = 0.5, 0.8
eta_det = coll * transmission * qe
R_sc = 6.0e4        # photons/s scattered during (cooled) imaging
t_exp = 20e-3       # s
mu_b = 5.0          # background counts per site per exposure
tau_loss = 2.0      # s, loss time constant during imaging
mu_s = eta_det * R_sc * t_exp

n_shots = 200000


def counts(full, with_loss):
    n = rng.poisson(mu_b, n_shots)
    if full:
        t_on = np.minimum(rng.exponential(tau_loss, n_shots), t_exp) if with_loss else np.full(n_shots, t_exp)
        n = n + rng.poisson(eta_det * R_sc * t_on)
    return n


def fidelity_mc(n0, n1, th):
    return 1 - 0.5 * (np.mean(n0 >= th) + np.mean(n1 < th))


def fidelity_analytic(th):          # no loss
    return 1 - 0.5 * (poisson.sf(th - 1, mu_b) + poisson.cdf(th - 1, mu_b + mu_s))


n_empty = counts(False, False)
n_full = counts(True, False)
n_full_loss = counts(True, True)

ths = np.arange(1, 40)
F_mc = np.array([fidelity_mc(n_empty, n_full, t) for t in ths])
F_th = np.array([fidelity_analytic(t) for t in ths])
F_loss = np.array([fidelity_mc(n_empty, n_full_loss, t) for t in ths])
th_best = ths[np.argmax(F_th)]
th_cross = int(np.ceil(mu_s / np.log(1 + mu_s / mu_b)))
survival = np.exp(-t_exp / tau_loss)

print("Fluorescence imaging of single atoms")
print("=" * 64)
print(f"NA = {NA}: collection {coll * 100:.2f}% -> detection efficiency {eta_det * 100:.2f}%")
print(f"signal mu_s = eta R t = {mu_s:.1f} photons, background mu_b = {mu_b}")
print(f"empty: mean {n_empty.mean():.3f}, var {n_empty.var():.3f}; "
      f"full: mean {n_full.mean():.2f}, var {n_full.var():.2f} (Poisson: mean = var)")
print(f"best threshold {th_best} (pmf crossing formula {th_cross}); "
      f"fidelity analytic {F_th.max():.6f}, MC {F_mc[th_best - 1]:.6f}")
print(f"with loss during imaging (tau = {tau_loss} s, survival {survival:.4f}): "
      f"best fidelity {F_loss.max():.5f}")
for na in (0.3, 0.5, 0.7, 0.9):
    print(f"   NA = {na}: collection fraction {(1 - np.sqrt(1 - na**2)) / 2 * 100:5.2f}%")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(14, 4.0))
bins = np.arange(0, 80) - 0.5
k = np.arange(0, 80)
ax = axes[0]
ax.hist(n_empty, bins=bins, density=True, color="0.6", alpha=0.7, label="empty site")
ax.hist(n_full_loss, bins=bins, density=True, color="C0", alpha=0.6, label="atom (with loss)")
ax.plot(k, poisson.pmf(k, mu_b), "k-", lw=1)
ax.plot(k, poisson.pmf(k, mu_b + mu_s), "k-", lw=1, label="Poisson (no loss)")
ax.axvline(th_best - 0.5, color="C3", ls="--", lw=1.2, label=f"threshold {th_best}")
ax.set_yscale("log")
ax.set_ylim(1e-6, 0.3)
ax.set_xlabel("detected photons per exposure")
ax.set_ylabel("probability")
ax.set_title(f"Histograms: {mu_s:.0f} signal vs {mu_b:.0f} background photons", fontsize=9)
ax.legend(fontsize=7)
ax = axes[1]
ax.plot(ths, 1 - F_th, "k", lw=1.5, label="analytic, no loss")
ax.plot(ths, 1 - F_mc, "C0o", ms=3, label="Monte Carlo, no loss")
ax.plot(ths, 1 - F_loss, "C1", lw=1.5, label=f"with loss (tau = {tau_loss:.0f} s)")
ax.set_yscale("log")
ax.set_xlabel("threshold (photons)")
ax.set_ylabel("assignment error 1 - F")
ax.set_title("Choosing the threshold", fontsize=9)
ax.legend(fontsize=7)
ax = axes[2]
na = np.linspace(0.05, 0.95, 200)
ax.plot(na, (1 - np.sqrt(1 - na**2)) / 2 * 100, "C2", lw=2)
ax.set_xlabel("numerical aperture NA")
ax.set_ylabel("fraction of photons collected (%)")
ax.set_title("Collection: (1 - cos theta)/2, isotropic emission", fontsize=9)
for v in (0.5, 0.7):
    ax.plot(v, (1 - np.sqrt(1 - v**2)) / 2 * 100, "ko", ms=4)
    ax.text(v - 0.02, (1 - np.sqrt(1 - v**2)) / 2 * 100 + 1.5, f"{(1 - np.sqrt(1 - v**2)) / 2 * 100:.1f}%",
            fontsize=8, ha="right")
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "imaging.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
se = lambda mu: np.sqrt(mu / n_shots)
checks = {
    "simulated counts have Poisson mean and variance (empty and full)":
        abs(n_empty.mean() - mu_b) < 4 * se(mu_b) and abs(n_full.mean() - mu_b - mu_s) < 4 * se(mu_b + mu_s)
        and abs(n_empty.var() / mu_b - 1) < 0.02 and abs(n_full.var() / (mu_b + mu_s) - 1) < 0.02,
    "Monte Carlo fidelity equals the Poisson-CDF formula at every threshold (within 4 s.e.)":
        np.all(np.abs(F_mc - F_th) < 4 * 0.5 * np.sqrt(
            (1 - poisson.cdf(ths - 1, mu_b)) * poisson.cdf(ths - 1, mu_b) / n_shots
            + poisson.cdf(ths - 1, mu_b + mu_s) * (1 - poisson.cdf(ths - 1, mu_b + mu_s)) / n_shots) + 1e-6),
    "best threshold equals the pmf crossing point ceil(mu_s / ln(1 + mu_s/mu_b))":
        th_best == th_cross,
    "loss during imaging lowers the best fidelity":
        F_loss.max() < F_th.max(),
}
