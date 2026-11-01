"""Chapter 07 figures: tweezer geometry (objective, focus, w(z)) and the motional ladder
with resolved-sideband (Raman) cooling."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch

import atomdata as A
from style import save


def geometry():
    lam, w0 = 1064e-9, 1.0e-6
    zR = np.pi * w0**2 / lam
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4), gridspec_kw={"width_ratios": [1, 1.2]})
    # (a) schematic: collimated beam -> objective -> focus with atom
    ax1.axis("off")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(-3, 3.4)
    ax1.add_patch(Polygon([[0.3, 1.6], [3.5, 1.6], [7.0, 0.05], [7.0, -0.05], [3.5, -1.6], [0.3, -1.6]],
                          closed=True, fc="#f4c7c3", ec="none"))
    ax1.add_patch(Polygon([[7.0, 0.05], [9.7, 1.25], [9.7, -1.25], [7.0, -0.05]], closed=True, fc="#f4c7c3", ec="none"))
    ax1.add_patch(Polygon([[3.3, 2.0], [3.7, 2.0], [3.7, -2.0], [3.3, -2.0]], closed=True, fc="#a6c8e0", ec="k"))
    ax1.text(3.5, 2.25, "objective\n(NA ~ 0.5)", ha="center", fontsize=8)
    ax1.plot([7.0], [0], "o", color="C0", ms=7)
    ax1.text(7.0, -0.55, "atom at\nthe focus", ha="center", va="top", fontsize=8)
    ax1.text(1.8, 0, "1064 nm\nbeam", ha="center", va="center", fontsize=8)
    ax1.add_patch(FancyArrowPatch((0.3, -2.4), (2.5, -2.4), arrowstyle="-|>", mutation_scale=12, color="C3"))
    ax1.text(1.4, -2.75, "light", ha="center", fontsize=8, color="C3")
    ax1.text(5.2, 3.2, "the same lens collects the atom's fluorescence (Chapter 08)", ha="center", fontsize=8)
    # (b) beam waist w(z) and intensity map
    z = np.linspace(-3 * zR, 3 * zR, 400)
    r = np.linspace(-3.3e-6, 3.3e-6, 300)
    Z, R = np.meshgrid(z, r)
    wz = w0 * np.sqrt(1 + (Z / zR)**2)
    I = (w0 / wz)**2 * np.exp(-2 * R**2 / wz**2)
    ax2.pcolormesh(Z * 1e6, R * 1e6, I, cmap="Reds", shading="auto")
    wline = w0 * np.sqrt(1 + (z / zR)**2)
    ax2.plot(z * 1e6, wline * 1e6, "k--", lw=1)
    ax2.plot(z * 1e6, -wline * 1e6, "k--", lw=1)
    ax2.axvline(zR * 1e6, color="0.3", lw=0.8, ls=":")
    ax2.axvline(-zR * 1e6, color="0.3", lw=0.8, ls=":")
    ax2.text(-8.5, -2.9, "dotted lines: z = +/- z_R, z_R = pi w0^2 / lambda = 2.95 um", fontsize=8)
    ax2.annotate("", xy=(0, 1.0), xytext=(0, 0), arrowprops=dict(arrowstyle="<->", lw=1))
    ax2.text(0.15, 0.4, "w0 = 1 um", fontsize=8)
    ax2.set_xlabel("z along the beam (um)")
    ax2.set_ylabel("r (um)")
    ax2.set_title("Intensity near the focus: tight radially, long axially", fontsize=9)
    save(fig, "07-tweezer-geometry.png")


def ladder():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 9.5)
    nmax = 4
    for base, lab, x0 in [(0.0, "|F=1> (lower hyperfine state)", 1.0), (5.0, "|F=2> (upper hyperfine state)", 1.0)]:
        for n in range(nmax + 1):
            y = base + 0.75 * n
            ax.hlines(y, x0, x0 + 3.2, color="k", lw=1.6)
            ax.text(x0 + 3.3, y, f"n = {n}", va="center", fontsize=8)
        ax.text(x0 - 0.1, base + 1.5, lab, rotation=90, va="center", ha="right", fontsize=8)
    # red-sideband Raman transition |F=1, n> -> |F=2, n-1>
    for n in range(1, nmax + 1):
        x = 1.5 + 0.55 * n
        ax.annotate("", xy=(x, 5.0 + 0.75 * (n - 1)), xytext=(x, 0.75 * n),
                    arrowprops=dict(arrowstyle="->", color="C3", lw=1.6))
    ax.text(5.0, 4.1, "red-sideband Raman pulse:\n|F=1, n> -> |F=2, n-1>", color="C3", fontsize=8)
    # optical pumping back to F=1 without changing n (Lamb-Dicke regime)
    ax.annotate("", xy=(3.9, 0.75 * 0 + 0.02), xytext=(3.9, 5.0), arrowprops=dict(arrowstyle="->", color="C0", lw=1.4, ls="--"))
    ax.text(5.0, 2.0, "optical pumping back to F = 1,\nusually keeping n\n(Lamb-Dicke regime)", color="C0", fontsize=8)
    ax.text(1.0, -0.4, "Repeat: each cycle removes one vibrational quantum; n = 0 is dark to the red sideband.",
            fontsize=8)
    # right: numbers
    G = 2 * np.pi * 98.45e3
    x0 = np.sqrt(A.hbar / (2 * A.M_RB87 * G))
    rows = [("radial trap frequency", "98.5 kHz"),
            ("vibrational quantum h f / k_B", f"{A.hbar * G / A.kB * 1e6:.1f} uK"),
            ("ground-state size x0 = sqrt(hbar/2m omega)", f"{x0 * 1e9:.0f} nm"),
            ("Lamb-Dicke eta = k x0 (780 nm)", f"{A.K_D2 * x0:.2f}"),
            ("mean n at 10 uK (radial)", f"{1 / np.expm1(A.hbar * G / (A.kB * 10e-6)):.1f}")]
    ax.text(6.0, 8.8, "1064 nm, w0 = 1 um, U0 = 1 mK (Rb-87)", fontsize=9, weight="bold")
    for i, (k, v) in enumerate(rows):
        ax.text(6.0, 8.1 - 0.6 * i, k, fontsize=8)
        ax.text(9.9, 8.1 - 0.6 * i, v, fontsize=8, ha="right")
    save(fig, "07-sideband-cooling.png")


def main():
    geometry()
    ladder()


if __name__ == "__main__":
    main()
