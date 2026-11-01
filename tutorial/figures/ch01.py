"""Chapter 01 figures: the experimental cycle and the ladder of frequency scales."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

import atomdata as A
from style import save


def cycle():
    steps = [
        ("1  Hot vapour", "Rb atoms at room\ntemperature, ~300 m/s"),
        ("2  MOT", "laser cooling +\nmagnetic gradient\n~100 uK, ~1e7 atoms"),
        ("3  Load tweezers", "light-assisted collisions\nleave 0 or 1 atom\n(~50% each)"),
        ("4  Image", "fluorescence picture:\nwhich sites are full?"),
        ("5  Rearrange", "moving tweezers drag\natoms into a\ndefect-free array"),
        ("6  Cool + initialise", "sub-Doppler / sideband\ncooling, optical\npumping to |0>"),
        ("7  Compute", "single-qubit gates +\nRydberg entangling\ngates"),
        ("8  Read out", "push out one state,\nimage again:\nbright = 1, dark = 0"),
    ]
    n = len(steps)
    fig, ax = plt.subplots(figsize=(10, 6.2))
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.45, 1.45)
    ax.set_aspect("equal")
    ax.axis("off")
    R = 1.08
    colors = ["#9e9e9e", "#e57373", "#ffb74d", "#4fc3f7", "#81c784", "#ba68c8", "#7986cb", "#4dd0e1"]
    pos = []
    for i, ((title, body), col) in enumerate(zip(steps, colors)):
        ang = np.pi / 2 - 2 * np.pi * i / n
        x, y = R * np.cos(ang), R * np.sin(ang)
        pos.append((x, y))
        box = FancyBboxPatch((x - 0.36, y - 0.22), 0.72, 0.44, boxstyle="round,pad=0.02",
                             fc=col, ec="k", lw=0.8, alpha=0.35)
        ax.add_patch(box)
        ax.text(x, y + 0.12, title, ha="center", va="center", fontsize=9.5, weight="bold")
        ax.text(x, y - 0.06, body, ha="center", va="center", fontsize=7.4)
    for i in range(n):
        a0 = np.pi / 2 - 2 * np.pi * (i + 0.30) / n
        a1 = np.pi / 2 - 2 * np.pi * (i + 0.70) / n
        p0 = (0.80 * np.cos(a0), 0.80 * np.sin(a0))
        p1 = (0.80 * np.cos(a1), 0.80 * np.sin(a1))
        ax.add_patch(FancyArrowPatch(p0, p1, connectionstyle="arc3,rad=-0.25",
                                     arrowstyle="-|>", mutation_scale=12, color="0.3", lw=1.2))
    ax.text(0, 0.08, "one experimental cycle", ha="center", fontsize=11, weight="bold")
    ax.text(0, -0.12, "repeated ~1 time per second;\nsteps 4-8 can repeat while\nthe MOT reloads",
            ha="center", fontsize=8.5, color="0.25")
    save(fig, "01-experimental-cycle.png")


def scales():
    """Characteristic frequencies of a Rb-87 tweezer experiment on one log axis."""
    items = [
        ("optical transition (D2)", A.c / A.LAMBDA_D2, "C3"),
        ("tweezer light, 1064 nm", A.c / 1064e-9, "C3"),
        ("ground hyperfine splitting", A.F_HFS, "C0"),
        ("Zeeman shift per m_F at 1 G (F=2)", 0.5 * A.muB * 1e-4 / A.h, "C0"),
        ("natural linewidth Gamma/2pi", A.GAMMA_D2 / (2 * np.pi), "C1"),
        ("Rydberg Rabi frequency (typ.)", 2e6, "C2"),
        ("interaction at 5 um, 70S", A.C6_70S_HZ_UM6 / 5.0**6, "C2"),
        ("tweezer depth, 1 mK", A.kB * 1e-3 / A.h, "C4"),
        ("radial trap frequency (typ.)", 98e3, "C4"),
        ("recoil energy E_r/h", A.E_RECOIL / A.h, "C4"),
        ("experimental cycle rate", 1.0, "0.4"),
    ]
    items.sort(key=lambda t: t[1])
    fig, ax = plt.subplots(figsize=(9, 5.6))
    for i, (label, f, col) in enumerate(items):
        ax.plot([f], [i], "o", color=col, ms=8)
        ax.hlines(i, 0.3, f, color=col, lw=1, alpha=0.4)
        if f > 1e9:
            ax.text(f / 1.8, i, f"{label}   ", va="center", ha="right", fontsize=9)
        else:
            ax.text(f * 1.8, i, f"  {label}", va="center", ha="left", fontsize=9)
    ax.set_xscale("log")
    ax.set_xlim(0.3, 3e16)
    ax.set_yticks([])
    ax.set_ylim(-1.3, len(items) - 0.4)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("frequency (Hz)   [energies converted with E = h f]")
    ax.set_title("Fourteen orders of magnitude in one experiment (Rb-87, illustrative values)")
    for f, lab in [(1e3, "kHz"), (1e6, "MHz"), (1e9, "GHz"), (1e12, "THz"), (1e15, "PHz")]:
        ax.axvline(f, color="0.85", lw=0.8, zorder=0)
        ax.text(f, -0.9, lab, ha="center", fontsize=8, color="0.5")
    save(fig, "01-frequency-scales.png")


def main():
    cycle()
    scales()


if __name__ == "__main__":
    main()
