"""Chapter 02 figures: alkali levels vs hydrogen, the Rb-87 D-line diagram, Breit-Rabi."""
import numpy as np
import matplotlib.pyplot as plt

import atomdata as A
from style import save


# Rb-87 hyperfine data (A, B constants from ARC / Steck)
HFS_5P12 = 816.656e6           # F'=1 <-> F'=2 (Hz)
HFS_5P32 = [72.2180e6, 156.9470e6, 266.6500e6]   # F'=0-1, 1-2, 2-3 (Hz), measured (Steck)


# Measured-quality Rb level energies (eV below ionisation) from the ARC library,
# fine-structure centroids ignored (S1/2, P3/2, D5/2, F7/2 shown).
LEVELS_EV = {
    "S": [(5, -4.1771), (6, -1.6810), (7, -0.9149), (8, -0.5757), (9, -0.3957), (10, -0.2887)],
    "P": [(5, -2.5881), (6, -1.2272), (7, -0.7217), (8, -0.4757), (9, -0.3373), (10, -0.2517)],
    "D": [(4, -1.7774), (5, -0.9903), (6, -0.6201), (7, -0.4227), (8, -0.3061), (9, -0.2317), (10, -0.1814)],
    "F": [(4, -0.8553), (5, -0.5471), (6, -0.3797), (7, -0.2789), (8, -0.2134), (9, -0.1685), (10, -0.1365)],
}
RY_EV = 13.6057 * (1 - 5.4858e-4 / 86.909)   # Rydberg energy with Rb-87 reduced mass


def quantum_defect_levels():
    fig, ax = plt.subplots(figsize=(8.5, 5.4))
    cols = {"S": "C0", "P": "C3", "D": "C2", "F": "C4"}
    for i, L in enumerate("SPDF"):
        for n, E in LEVELS_EV[L]:
            ax.hlines(E, i - 0.3, i + 0.3, color=cols[L], lw=2)
            if n <= 7:
                ax.text(i + 0.33, E, f"{n}{L}", va="center", fontsize=8)
    for n in range(2, 11):
        E = -RY_EV / n**2
        ax.hlines(E, 4 - 0.3, 4 + 0.3, color="k", lw=2)
        if n <= 6:
            ax.text(4.33, E, f"n={n}", va="center", fontsize=8)
    ax.axhline(0, color="0.5", ls="--", lw=0.8)
    ax.text(4.75, 0.06, "ionisation limit", fontsize=8, color="0.4", ha="right")
    ax.set_xticks(range(5))
    ax.set_xticklabels(["S (l=0)\ndefect 3.13", "P (l=1)\ndefect 2.64", "D (l=2)\ndefect 1.35",
                        "F (l=3)\ndefect 0.02", "hydrogen\n(n=1 at -13.6 eV)"])
    ax.set_ylabel("energy below ionisation (eV)")
    ax.set_ylim(-4.5, 0.3)
    ax.set_xlim(-0.6, 4.85)
    ax.set_title("Rb levels: E = -Ry/(n - delta_l)^2, and low-l electrons dive into the core")
    ax.annotate("5S ground state, 4.18 eV deep\n(n* = 1.80, so delta = 3.20 at n = 5)", xy=(0.1, -4.1771),
                xytext=(0.75, -3.75), fontsize=8, va="center", arrowprops=dict(arrowstyle="->"))
    ax.text(2.5, -3.2, "defects quoted are the high-n (Rydberg) limits; at low n\nthey differ (larger for S and P, smaller for D and F)",
            fontsize=8, color="0.35", ha="center")
    save(fig, "02-quantum-defects.png")


def level_diagram():
    """Schematic (not to scale) Rb-87 D1/D2 hyperfine diagram with cooling and repump lines."""
    fig, ax = plt.subplots(figsize=(9.5, 6.4))
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.4, 10.4)

    def level(x0, x1, y, label, right=True, fs=8.5, col="k"):
        ax.hlines(y, x0, x1, color=col, lw=2)
        if right:
            ax.text(x1 + 0.1, y, label, va="center", fontsize=fs)
        else:
            ax.text(x0 - 0.1, y, label, va="center", ha="right", fontsize=fs)

    # ground state 5S1/2
    level(1.0, 9.0, 0.9, "")
    level(1.0, 9.0, 0.0, "")
    ax.text(9.1, 0.9, "F = 2", va="center", fontsize=9)
    ax.text(9.1, 0.0, "F = 1", va="center", fontsize=9)
    ax.text(0.9, 0.45, "5S$_{1/2}$", ha="right", va="center", fontsize=11)
    ax.annotate("", xy=(3.0, 0.9), xytext=(3.0, 0.0), arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax.text(3.1, 0.45, "6.834 682 611 GHz (hyperfine qubit)", ha="left", va="center", fontsize=8)

    # 5P1/2 (D1)
    y12 = 5.2
    level(1.0, 3.6, y12 + 0.5, "F' = 2")
    level(1.0, 3.6, y12, "F' = 1")
    ax.text(0.9, y12 + 0.25, "5P$_{1/2}$", ha="right", va="center", fontsize=11)
    ax.text(2.3, y12 + 0.25, "816.7 MHz", ha="center", va="center", fontsize=7.5)

    # 5P3/2 (D2)
    base = 7.6
    gaps = [0.36, 0.62, 0.95]  # visual, proportional-ish to 72, 157, 267 MHz
    ys = [base]
    for g in gaps:
        ys.append(ys[-1] + g)
    for F, y in enumerate(ys):
        level(5.0, 9.0, y, f"F' = {F}")
    ax.text(9.95, base + 1.0, "5P$_{3/2}$", ha="left", va="center", fontsize=11)
    for (ya, yb), lab in zip(zip(ys[:-1], ys[1:]), ["72.2", "156.9", "266.7 MHz"]):
        ax.text(4.9, (ya + yb) / 2, lab, ha="right", va="center", fontsize=7.5)

    # D1 / D2 labels
    ax.annotate("", xy=(1.6, y12), xytext=(1.6, 0.0),
                arrowprops=dict(arrowstyle="->", color="0.6", lw=1, ls="--"))
    ax.text(1.5, 2.7, "D1\n794.98 nm\n$\\Gamma/2\\pi$ = 5.75 MHz", ha="right", fontsize=8, color="0.35")

    # cooling transition F=2 -> F'=3 and repumper F=1 -> F'=2
    ax.annotate("", xy=(7.6, ys[3]), xytext=(7.6, 0.9),
                arrowprops=dict(arrowstyle="<->", color="C3", lw=2))
    ax.text(7.7, 4.0, "cooling / imaging\nF=2 -> F'=3 (cycling)\nD2, 780.24 nm\n$\\Gamma/2\\pi$ = 6.07 MHz",
            fontsize=8, color="C3")
    ax.annotate("", xy=(5.8, ys[2]), xytext=(5.8, 0.0),
                arrowprops=dict(arrowstyle="->", color="C0", lw=2))
    ax.text(5.9, 2.4, "repumper\nF=1 -> F'=2", fontsize=8, color="C0")
    # forbidden decay from F'=3 to F=1
    ax.annotate("", xy=(7.0, 0.0), xytext=(7.0, ys[3]),
                arrowprops=dict(arrowstyle="->", color="0.5", lw=0.8, ls=":"))
    ax.text(6.2, 6.3, "F'=3 -> F=1\nforbidden\n(Delta F = 2)", fontsize=7.5, color="0.4")
    ax.text(0.1, 10.1, "Rb-87, nuclear spin I = 3/2 (energies not to scale)", fontsize=10, weight="bold")
    save(fig, "02-rb87-levels.png")


def breit_rabi():
    I = 1.5
    dE = A.h * A.F_HFS
    gJ, gI = 2.00233113, -0.0009951414
    B = np.linspace(0, 0.5, 600)      # tesla
    x = (gJ - gI) * A.muB * B / dE
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.5))
    for F, sign, col in [(2, +1, "C3"), (1, -1, "C0")]:
        for m in range(-F, F + 1):
            if F == 2 and m == -2:
                root = 1 - x            # analytic continuation for the stretched state
            else:
                root = np.sqrt(1 + 4 * m * x / (2 * I + 1) + x**2)
            E = -dE / (2 * (2 * I + 1)) + gI * A.muB * m * B + sign * dE / 2 * root
            ax1.plot(B * 1e4, E / A.h / 1e9, color=col, lw=1.3)
            if B[-1] > 0:
                ax1.text(B[-1] * 1e4 * 1.01, E[-1] / A.h / 1e9, f"{m:+d}", fontsize=7, va="center", color=col)
    ax1.set_xlabel("magnetic field B (G)")
    ax1.set_ylabel("energy / h (GHz)")
    ax1.set_title("Breit-Rabi: Rb-87 5S$_{1/2}$ ground state")
    ax1.text(300, 5.0, "F = 2", color="C3")
    ax1.text(300, -5.6, "F = 1", color="C0")
    ax1.set_xlim(0, 5400)
    # clock vs magnetically sensitive transitions at low field
    b = np.linspace(0, 2.0, 200)  # gauss
    quad = 575.15 * b**2
    ax2.plot(b, quad, "C2", lw=2, label="clock |1,0> -> |2,0>: +575 Hz/G$^2$ x B$^2$")
    ax2.plot(b, 0.70e6 * b, "C1", lw=2, label="|1,0> -> |2,1>: about +0.70 MHz/G x B")
    ax2.set_yscale("log")
    ax2.set_ylim(1, 6e6)
    ax2.set_xlabel("magnetic field B (G)")
    ax2.set_ylabel("transition shift (Hz)")
    ax2.set_title("Why the clock states make the best qubit")
    ax2.legend(fontsize=8, loc="center right")
    ax2.axvline(1.0, color="0.8", lw=0.8)
    ax2.text(1.03, 1.6e6 , "at 1 G: 575 Hz vs 700 kHz", fontsize=8, va="bottom")
    save(fig, "02-breit-rabi.png")


def main():
    quantum_defect_levels()
    level_diagram()
    breit_rabi()


if __name__ == "__main__":
    main()
