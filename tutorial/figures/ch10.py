"""Chapter 10 figures: Rydberg excitation scheme and the blockade level diagram / pair potential."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

import atomdata as A
from style import save


def excitation():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8), gridspec_kw={"width_ratios": [1.1, 1]})
    ax1.axis("off")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(-0.5, 10)
    ax1.hlines(0.0, 1, 4.5, lw=2, color="k")
    ax1.text(0.9, 0.0, "5S1/2 |1>", ha="right", va="center", fontsize=9)
    ax1.hlines(5.2, 1, 4.5, lw=2, color="k")
    ax1.text(0.9, 5.2, "6P3/2", ha="right", va="center", fontsize=9)
    ax1.hlines(4.6, 1.5, 4.0, lw=1, color="C0", ls="--")
    ax1.annotate("", xy=(4.3, 5.2), xytext=(4.3, 4.6), arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax1.text(4.45, 4.9, "intermediate detuning\nDelta_i (~ GHz)", fontsize=8, va="center")
    ax1.hlines(9.2, 1, 4.5, lw=2, color="k")
    ax1.text(0.9, 9.2, "70S1/2 |r>", ha="right", va="center", fontsize=9)
    ax1.annotate("", xy=(2.2, 4.6), xytext=(2.2, 0.0), arrowprops=dict(arrowstyle="<->", color="C0", lw=2.2))
    ax1.text(2.05, 2.3, "420 nm\nOmega_1", ha="right", color="C0", fontsize=9)
    ax1.annotate("", xy=(2.2, 9.2), xytext=(2.2, 4.6), arrowprops=dict(arrowstyle="<->", color="C3", lw=2.2))
    ax1.text(2.05, 7.0, "1013 nm\nOmega_2", ha="right", color="C3", fontsize=9)
    ax1.text(3.0, 7.0, "Omega = Omega_1 Omega_2 / (2 Delta_i)\n(a few MHz)", fontsize=8)
    ax1.text(4.7, 9.6, "ionisation limit 735.7 GHz above 70S; level spacing near n = 70: ~22 GHz", fontsize=8, va="bottom")
    ax1.set_title("Two-photon excitation of Rb-87 to a Rydberg state", fontsize=9)
    # orbit size comparison
    ax2.set_aspect("equal")
    ax2.axis("off")
    r70 = 1.5 * 66.869**2 * A.a0 * 1e9   # nm
    ax2.add_patch(Circle((0, 0), r70, fc="#fde0dd", ec="C3"))
    ax2.add_patch(Circle((0, 0), 0.25, fc="C0", ec="C0"))
    ax2.set_xlim(-1.3 * r70, 1.3 * r70)
    ax2.set_ylim(-1.3 * r70, 1.3 * r70)
    ax2.annotate("", xy=(r70, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="<->", lw=1))
    ax2.text(r70 / 2, 18, f"<r> = (3/2) n*^2 a0 = {r70:.0f} nm", ha="center", fontsize=8)
    ax2.text(0, -r70 - 50, "a ground-state Rb atom (radius ~0.25 nm) would be invisible at this scale", ha="center", fontsize=8)
    ax2.set_title("A 70S Rydberg atom is ~1000x larger than a ground-state atom", fontsize=9)
    save(fig, "10-excitation.png")


def blockade_levels():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4), gridspec_kw={"width_ratios": [1, 1.2]})
    ax1.axis("off")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(-0.5, 9)
    ax1.hlines(0, 3, 7, lw=2)
    ax1.text(7.2, 0, "|gg>", va="center", fontsize=10)
    ax1.hlines(3.5, 3, 7, lw=2)
    ax1.text(7.2, 3.5, "|W> = (|gr> + |rg>)/sqrt 2", va="center", fontsize=9)
    ax1.hlines(7.0, 3, 7, lw=1, ls="--", color="0.5")
    ax1.text(7.2, 7.0, "|rr> without interaction", va="center", fontsize=8, color="0.4")
    ax1.hlines(8.6, 3, 7, lw=2, color="C3")
    ax1.text(7.2, 8.6, "|rr>, shifted by V", va="center", fontsize=9, color="C3")
    ax1.annotate("", xy=(4.0, 3.5), xytext=(4.0, 0), arrowprops=dict(arrowstyle="<->", color="C0", lw=2))
    ax1.text(3.85, 1.75, "sqrt(2) Omega", ha="right", color="C0", fontsize=9)
    ax1.annotate("", xy=(5.0, 7.0), xytext=(5.0, 3.5), arrowprops=dict(arrowstyle="<->", color="C0", lw=1.2, ls="--"))
    ax1.text(5.15, 5.3, "laser now off\nresonance by V", fontsize=8, color="C0")
    ax1.annotate("", xy=(6.5, 8.6), xytext=(6.5, 7.0), arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax1.text(6.35, 7.8, "V", ha="right", fontsize=9)
    ax1.set_title("Two atoms: the doubly excited state is pushed away", fontsize=9)
    R = np.linspace(2.5, 16, 400)
    V = A.C6_70S_HZ_UM6 / R**6 / 1e6
    ax2.semilogy(R, V, "C3", lw=2, label="V/h = C6/(h R^6), 70S + 70S")
    ax2.axhline(2.0, color="C0", ls="--", lw=1.2, label="hbar Omega, Omega/2pi = 2 MHz")
    Rb = (A.C6_70S_HZ_UM6 / 2e6)**(1 / 6)
    ax2.axvline(Rb, color="k", ls=":", lw=1)
    ax2.text(Rb + 0.2, 300, f"R_b = {Rb:.1f} um", fontsize=8)
    ax2.axvspan(2.5, Rb, color="C3", alpha=0.07)
    ax2.text(3.0, 0.05, "blockaded:\nV >> hbar Omega", fontsize=8, color="C3")
    ax2.text(11.5, 0.05, "independent:\nV << hbar Omega", fontsize=8)
    ax2.plot([5], [A.C6_70S_HZ_UM6 / 5**6 / 1e6], "ko", ms=4)
    ax2.text(5.2, A.C6_70S_HZ_UM6 / 5**6 / 1e6 * 1.3, "5 um: 55 MHz", fontsize=8)
    ax2.set_xlabel("distance R (um)")
    ax2.set_ylabel("interaction energy / h (MHz)")
    ax2.set_ylim(0.01, 3e3)
    ax2.legend(fontsize=8, loc="upper right")
    ax2.set_title("van der Waals interaction and blockade radius", fontsize=9)
    save(fig, "10-blockade.png")


def main():
    excitation()
    blockade_levels()


if __name__ == "__main__":
    main()
