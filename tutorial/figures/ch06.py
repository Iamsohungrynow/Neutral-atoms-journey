"""Chapter 06 figures: lin-perp-lin Sisyphus cooling and the 1D/3D MOT schematic."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Ellipse

import atomdata as A
from style import save


def sisyphus():
    """Light-shifted ground sublevels of a J=1/2 -> J'=3/2 atom in a lin-perp-lin standing wave.

    The local polarization cycles linear -> sigma+ -> linear -> sigma- with period lambda/2;
    the sigma+/- intensity fractions are (1 +/- sin 2kz)/2 and the Clebsch-Gordan weights
    (1 for the stretched transition, 1/3 for the other) give
        U(+1/2) = E_ls [2/3 + (1/3) sin 2kz],   U(-1/2) = E_ls [2/3 - (1/3) sin 2kz],   E_ls < 0.
    """
    z = np.linspace(0, 1.0, 600)               # in units of lambda
    s = np.sin(4 * np.pi * z)
    U0 = -1.0
    Up = U0 * (2 / 3 + s / 3)
    Um = U0 * (2 / 3 - s / 3)
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.plot(z, Up, "C3", lw=2.2, label="m = +1/2")
    ax.plot(z, Um, "C0", lw=2.2, label="m = -1/2")
    # an atom climbing a hill and being pumped down at the top
    zv = 0.125   # valley of m=+1/2 (sigma+ light)
    zt = 0.375   # hilltop of m=+1/2 = valley of m=-1/2 (sigma- light)
    zz = np.linspace(zv, zt, 80)
    ax.plot(zz, U0 * (2 / 3 + np.sin(4 * np.pi * zz) / 3) + 0.07, "k", lw=1, ls=(0, (2, 2)))
    ax.annotate("", xy=(zt, -1.0 + 0.03), xytext=(zt, -1 / 3 - 0.02),
                arrowprops=dict(arrowstyle="->", color="k", lw=1.5))
    ax.text(zt + 0.015, -0.62, "at the hilltop sigma- light\npumps the atom to m = -1/2,\nwhose valley is here: the\nemitted photon carries off\nthe energy", fontsize=8)
    ax.text(0.25, -1.12, "dotted: the atom climbs in m = +1/2 (kinetic -> potential energy)", fontsize=8, ha="center")
    ax.set_xlabel("position z (units of lambda)")
    ax.set_ylabel("light shift (units of |E_ls|)")
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.2, -0.02)
    for zp, lab in [(0, "lin"), (0.125, "sigma+"), (0.25, "lin"), (0.375, "sigma-"), (0.5, "lin"),
                    (0.625, "sigma+"), (0.75, "lin"), (0.875, "sigma-"), (1.0, "lin")]:
        ax.text(zp, -0.09, lab, ha="center", fontsize=8, color="0.35")
    ax.set_title("Sisyphus cooling in a lin-perp-lin standing wave (J = 1/2 -> 3/2, red detuning)")
    ax.legend(fontsize=8, loc="lower right")
    save(fig, "06-sisyphus.png")


def mot_scheme():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8), gridspec_kw={"width_ratios": [1.35, 1]})
    # (a) 1D MOT energy diagram
    z = np.linspace(-1, 1, 10)
    ax1.plot(z, 0 * z - 2.2, "k", lw=2)
    ax1.text(1.03, -2.2, "J = 0, m = 0", va="center", fontsize=8)
    for mp, col in [(+1, "C3"), (0, "0.4"), (-1, "C0")]:
        ax1.plot(z, 1.0 + 0.55 * mp * z, color=col, lw=2)
        ax1.text(1.03, 1.0 + 0.55 * mp, (f"m' = {mp:+d}" if mp else "m' = 0"), va="center", fontsize=8, color=col)
    ax1.plot(z, 0 * z + 0.6, "C2", lw=1.2, ls="--")
    ax1.text(-1.0, 0.68, "laser (red detuned)", fontsize=8, color="C2")
    zr = (0.6 - 1.0) / (-0.55)   # where m'=-1 meets the laser (z>0)
    ax1.annotate("", xy=(zr, 0.6), xytext=(zr, -2.2), arrowprops=dict(arrowstyle="->", color="C0", lw=2))
    ax1.annotate("", xy=(-zr, 0.6), xytext=(-zr, -2.2), arrowprops=dict(arrowstyle="->", color="C3", lw=2))
    ax1.text(zr + 0.04, -1.2, "sigma- light\nfrom the right\nresonant here", fontsize=8, color="C0")
    ax1.text(-zr - 0.04, -1.2, "sigma+ light\nfrom the left\nresonant here", fontsize=8, color="C3", ha="right")
    ax1.add_patch(FancyArrowPatch((-1.25, -2.9), (-0.65, -2.9), arrowstyle="-|>", mutation_scale=14, color="C3", lw=2))
    ax1.add_patch(FancyArrowPatch((1.25, -2.9), (0.65, -2.9), arrowstyle="-|>", mutation_scale=14, color="C0", lw=2))
    ax1.text(0, -3.05, "B = A z: zero at the centre", ha="center", va="top", fontsize=8)
    ax1.set_xlim(-1.35, 1.45)
    ax1.set_ylim(-3.5, 2.0)
    ax1.set_xlabel("position z")
    ax1.set_yticks([])
    ax1.set_title("1D MOT: the Zeeman shift picks which beam pushes", fontsize=10)
    # (b) 3D: anti-Helmholtz coils and six beams
    ax2.axis("off")
    ax2.set_xlim(-2, 2)
    ax2.set_ylim(-2, 2)
    for y, cur in [(1.1, "current ->"), (-1.1, "<- current")]:
        ax2.add_patch(Ellipse((0, y), 2.6, 0.55, fill=False, ec="#b5651d", lw=3))
        ax2.text(1.45, y, cur, fontsize=8, va="center", color="#b5651d")
    ax2.add_patch(Ellipse((0, 0), 0.32, 0.32, fc="#f4c7c3", ec="C3"))
    for (x0, y0, x1, y1) in [(-1.9, 0, -0.3, 0), (1.9, 0, 0.3, 0), (0, -1.95, 0, -0.3), (0, 1.95, 0, 0.3),
                             (-1.3, -1.3, -0.25, -0.25), (1.3, 1.3, 0.25, 0.25)]:
        ax2.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=12, color="C3", lw=1.6))
    ax2.text(0, -2.0, "anti-Helmholtz coils: |B| grows linearly from the centre;\n"
             "six circularly polarized red-detuned beams", ha="center", va="top", fontsize=8)
    ax2.set_title("3D MOT", fontsize=10)
    save(fig, "06-mot-scheme.png")


def mot_force():
    G, k = A.GAMMA_D2, A.K_D2
    A_grad, s0, R = 0.10, 1.0, 0.01
    z = np.linspace(-0.015, 0.015, 900)
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    for dl, col in [(-0.5, "C1"), (-1.0, "C3"), (-2.0, "C0"), (-3.0, "C4")]:
        d = dl * G
        sh = A.muB * A_grad * z / A.hbar
        F = A.hbar * k * G / 2 * (s0 / (1 + s0 + (2 * (d - sh) / G)**2) - s0 / (1 + s0 + (2 * (d + sh) / G)**2))
        F = np.where(np.abs(z) <= R, F, 0)
        ax.plot(z * 1e3, F * 1e21, color=col, lw=2, label=f"delta = {dl} Gamma")
    ax.axhline(0, color="0.7", lw=0.8)
    ax.set_xlabel("position z (mm)")
    ax.set_ylabel("force on an atom at rest (1e-21 N)")
    ax.set_title("1D MOT force, A = 10 G/cm, s0 = 1, beams of radius 10 mm")
    ax.legend(fontsize=8)
    save(fig, "06-mot-force.png")


def main():
    sisyphus()
    mot_scheme()
    mot_force()


if __name__ == "__main__":
    main()
