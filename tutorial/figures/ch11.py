"""Chapter 11 figures: pulse protocols of the Jaksch pi-2pi-pi gate and the Levine phase gate."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from style import save


def protocols():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.2))
    # (a) Jaksch: control pi, target 2pi, control pi
    for ax in (ax1, ax2):
        ax.set_xlim(0, 10)
        ax.set_ylim(-0.5, 5.2)
        ax.axis("off")
    for y, lab in [(3.2, "control"), (1.2, "target")]:
        ax1.hlines(y, 0.8, 7.2, color="k", lw=1)
        ax1.text(0.7, y, lab, ha="right", va="center", fontsize=9)
    for (x, w, y, txt) in [(1.0, 1.2, 3.2, "pi"), (2.5, 2.4, 1.2, "2 pi"), (5.2, 1.2, 3.2, "pi")]:
        ax1.add_patch(Rectangle((x, y), w, 0.9, fc="C3", ec="k", alpha=0.85))
        ax1.text(x + w / 2, y + 1.05, txt, ha="center", fontsize=9)
    rows = [("|00>", "nothing happens", "+1"), ("|01>", "target 2pi loop", "-1"),
            ("|10>", "control pi + pi = 2pi loop", "-1"), ("|11>", "target blocked; control 2pi", "-1")]
    ax1.text(7.5, 4.6, "input    what happens               phase", fontsize=8, family="monospace")
    for i, (a, b, c) in enumerate(rows):
        ax1.text(7.5, 4.0 - 0.6 * i, f"{a:6s} {b:27s} {c}", fontsize=7.5, family="monospace")
    ax1.text(7.5, 1.3, "diag(1,-1,-1,-1) = CZ x (Z (x) Z):\nCZ up to single-qubit Z gates", fontsize=8)
    ax1.text(0.2, -0.3, "needs light addressed to each atom separately", fontsize=8, color="0.35")
    ax1.set_title("(a) Jaksch et al. (2000): pi - 2pi - pi", fontsize=10, loc="left")
    # (b) Levine: two global pulses with phase jump
    ax2.hlines(2.2, 0.5, 6.5, color="k", lw=1)
    ax2.text(0.4, 2.2, "both\natoms", ha="right", va="center", fontsize=9)
    ax2.add_patch(Rectangle((0.8, 2.2), 2.5, 0.9, fc="C0", ec="k", alpha=0.85))
    ax2.add_patch(Rectangle((3.4, 2.2), 2.5, 0.9, fc="C2", ec="k", alpha=0.85))
    ax2.text(2.05, 3.25, "tau, Delta, phase 0", ha="center", fontsize=8)
    ax2.text(4.65, 3.25, "tau, Delta, phase xi", ha="center", fontsize=8)
    ax2.text(3.35, 1.5, "tau Omega = 4.29,  Delta/Omega = 0.377,  xi = 3.90\n"
             "total 8.58 / Omega (390 ns at Omega/2pi = 3.5 MHz)", ha="center", fontsize=8)
    ax2.text(6.8, 4.4, "|11> drives |11> <-> |W> at\nsqrt(2 Omega^2 + Delta^2): one full\ncycle per pulse", fontsize=8)
    ax2.text(6.8, 2.6, "|01>, |10> drive at\nsqrt(Omega^2 + Delta^2): closed\nonly after the phase jump", fontsize=8)
    ax2.text(6.8, 1.0, "phases: phi11 = 2 phi01 + pi", fontsize=8)
    ax2.text(0.2, -0.3, "one global laser for all atoms: parallel gates on many pairs", fontsize=8, color="0.35")
    ax2.set_title("(b) Levine et al. (2019): two global pulses", fontsize=10, loc="left")
    save(fig, "11-protocols.png")


def main():
    protocols()


if __name__ == "__main__":
    main()
