"""Chapter 08 figures: making many tweezers (AOD vs SLM) and collisional-blockade loading."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch
from scipy.stats import poisson

from style import save


def aod_slm():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4))
    for ax in (ax1, ax2):
        ax.axis("off")
        ax.set_xlim(0, 10)
        ax.set_ylim(-3.2, 3.2)
    # AOD
    ax1.add_patch(Rectangle((0.2, -0.3), 2.0, 0.6, fc="#f4c7c3", ec="none"))
    ax1.add_patch(Rectangle((2.2, -1.0), 1.2, 2.0, fc="#cfe2f3", ec="k"))
    ax1.text(2.8, 1.25, "AOD crystal", ha="center", fontsize=8)
    ax1.text(2.8, -1.55, "RF tones\nf1, f2, f3, f4", ha="center", va="top", fontsize=8)
    angles = np.linspace(-0.35, 0.35, 4)
    for a in angles:
        ax1.add_patch(Polygon([[3.4, -0.15], [3.4, 0.15], [7.6, 0.15 + 4.2 * np.tan(a)], [7.6, -0.15 + 4.2 * np.tan(a)]],
                              closed=True, fc="#f4c7c3", ec="none", alpha=0.9))
        ax1.plot([8.3], [4.2 * np.tan(a) * 1.0], "o", color="C0", ms=6)
    ax1.add_patch(Rectangle((7.6, -2.2), 0.3, 4.4, fc="#a6c8e0", ec="k"))
    ax1.text(7.75, 2.45, "objective", ha="center", fontsize=8)
    ax1.text(5.0, -2.7, "each RF frequency -> one deflection angle -> one tweezer\n"
             "change a frequency and the tweezer moves (used for rearrangement)", ha="center", fontsize=8)
    ax1.set_title("Acousto-optic deflector: dynamic 1D rows (2D with two crossed AODs)", fontsize=9)
    # SLM
    ax2.add_patch(Rectangle((0.2, -0.6), 2.4, 1.2, fc="#f4c7c3", ec="none"))
    ax2.add_patch(Rectangle((2.6, -1.4), 0.5, 2.8, fc="0.75", ec="k"))
    rng = np.random.default_rng(3)
    for i in range(14):
        ax2.add_patch(Rectangle((2.62, -1.38 + i * 0.2), 0.46, 0.18, fc=plt.cm.twilight(rng.random()), ec="none"))
    ax2.text(2.85, 1.65, "SLM (phase\nhologram)", ha="center", fontsize=8)
    ax2.add_patch(Polygon([[3.1, -1.4], [3.1, 1.4], [6.6, 1.0], [6.6, -1.0]], closed=True, fc="#f4c7c3", ec="none", alpha=0.6))
    ax2.add_patch(Rectangle((6.6, -2.2), 0.3, 4.4, fc="#a6c8e0", ec="k"))
    ax2.text(6.75, 2.45, "objective", ha="center", fontsize=8)
    pts = [(8.2 + 0.45 * (i % 4), -1.2 + 0.8 * (i // 4)) for i in range(16)]
    pts = [p for j, p in enumerate(pts) if j not in (5, 10)] + [(8.85, -0.0), (9.5, 1.6)]
    for x, y in pts:
        ax2.plot(x, y, "o", color="C0", ms=5)
    ax2.text(5.0, -2.7, "one hologram -> hundreds to thousands of static traps in any 2D pattern;\n"
             "iterative algorithms equalise the trap depths", ha="center", fontsize=8)
    ax2.set_title("Spatial light modulator: static arbitrary 2D patterns", fontsize=9)
    save(fig, "08-aod-slm.png")


def loading():
    nbar = np.linspace(0, 5, 300)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
    ax1.plot(nbar, 0.5 * (1 - np.exp(-2 * nbar)), "C0", lw=2, label="P(1) after pairwise loss")
    ax1.plot(nbar, 0.5 * (1 + np.exp(-2 * nbar)), "0.5", lw=2, label="P(0) after pairwise loss")
    ax1.plot(nbar, nbar * np.exp(-nbar), "C1--", lw=1.5, label="P(1) for plain Poisson loading")
    ax1.axhline(0.5, color="k", ls=":", lw=0.8)
    ax1.set_xlabel("mean number of atoms that enter the tweezer, nbar")
    ax1.set_ylabel("probability")
    ax1.set_title("Collisional blockade: occupancy = N mod 2 -> 1/2", fontsize=9)
    ax1.legend(fontsize=8)
    n = np.arange(0, 9)
    nb = 3.0
    w = 0.38
    ax2.bar(n - w / 2, poisson.pmf(n, nb), width=w, color="C1", alpha=0.8, label=f"Poisson, nbar = {nb:g}")
    par = np.zeros_like(n, dtype=float)
    par[0] = poisson.pmf(n[::2], nb).sum() + poisson.sf(8, nb) * 0.5
    par[1] = poisson.pmf(n[1::2], nb).sum() + poisson.sf(8, nb) * 0.5
    ax2.bar(n + w / 2, par, width=w, color="C0", alpha=0.8, label="after light-assisted collisions")
    ax2.set_xlabel("atoms in the tweezer")
    ax2.set_ylabel("probability")
    ax2.set_xticks(n)
    ax2.set_title("Pairs are expelled: 0 or 1 atom, never more", fontsize=9)
    ax2.legend(fontsize=8)
    save(fig, "08-loading.png")


def main():
    aod_slm()
    loading()


if __name__ == "__main__":
    main()
