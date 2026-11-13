"""Chapter 09 figures: two-photon Raman transitions and Ramsey / spin-echo sequences."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import atomdata as A
from style import save


def raman():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4), gridspec_kw={"width_ratios": [1, 1.1]})
    ax1.axis("off")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(-0.6, 7)
    ax1.hlines(6.0, 2.5, 7.5, color="k", lw=2)
    ax1.text(7.6, 6.0, "5P (excited)", va="center", fontsize=9)
    ax1.hlines(5.0, 2.5, 7.5, color="C3", lw=1, ls="--")
    ax1.annotate("", xy=(8.2, 6.0), xytext=(8.2, 5.0), arrowprops=dict(arrowstyle="<->"))
    ax1.text(8.35, 5.5, "Delta", va="center", fontsize=9)
    ax1.hlines(0.9, 1.0, 3.5, color="k", lw=2)
    ax1.hlines(0.0, 6.5, 9.0, color="k", lw=2)
    ax1.text(1.0, 1.15, "|1> = |F=2, mF=0>", fontsize=8)
    ax1.text(6.5, -0.45, "|0> = |F=1, mF=0>", fontsize=8)
    ax1.annotate("", xy=(5.0, 5.0), xytext=(2.6, 0.9), arrowprops=dict(arrowstyle="<->", color="C3", lw=2))
    ax1.annotate("", xy=(5.0, 5.0), xytext=(7.4, 0.0), arrowprops=dict(arrowstyle="<->", color="C0", lw=2))
    ax1.text(3.0, 3.2, "beam 1\nOmega_1", color="C3", fontsize=9, ha="right")
    ax1.text(7.1, 3.2, "beam 2\nOmega_2", color="C0", fontsize=9)
    ax1.text(5.0, 0.45, "frequency difference\n= 6.834 GHz", ha="center", fontsize=8)
    ax1.set_title("Two-photon Raman transition: Omega_eff = Omega_1 Omega_2 / (2 Delta)", fontsize=9)

    G = A.GAMMA_D2
    d = np.logspace(np.log10(20e9), 12.5, 300)   # Delta / 2pi in Hz, well above the 6.8 GHz hyperfine splitting
    err = np.pi * (G / 2 / np.pi) / d
    ax2.loglog(d / 1e9, err, "C2", lw=2)
    ax2.set_xlabel("detuning Delta / 2pi (GHz)")
    ax2.set_ylabel("spontaneous-scattering probability per pi pulse")
    ax2.set_title("Single-level estimate: P_sc = pi Gamma / Delta", fontsize=9)
    ax2.axvline(7123, color="0.6", ls=":", lw=1)
    ax2.text(7123 * 0.9, 3e-4, "fine-structure\nsplitting 7.1 THz:\nboth P levels matter", fontsize=8, ha="right")
    ax2.plot(50, np.pi * 6.0666e6 / 50e9, "ko", ms=4)
    ax2.text(58, np.pi * 6.0666e6 / 50e9 * 1.2, "50 GHz: 3.8e-4", fontsize=8)
    save(fig, "09-raman.png")


def sequences():
    fig, axes = plt.subplots(2, 1, figsize=(10, 3.8), sharex=True)
    for ax, (title, pulses) in zip(axes, [
            ("Ramsey: measures T2* (all static and slow shifts dephase)", [(0, 0.06, "pi/2"), (0.94, 0.06, "pi/2")]),
            ("Spin echo: a pi pulse (twice the area, so twice as long) in the middle refocuses static shifts (measures T2_echo)",
             [(0, 0.06, "pi/2"), (0.44, 0.12, "pi"), (0.94, 0.06, "pi/2")])]):
        ax.axhline(0, color="k", lw=1)
        for t0, w, lab in pulses:
            h = 0.6
            ax.add_patch(Rectangle((t0, 0), w, h, fc="C0", ec="k"))
            ax.text(t0 + w / 2, h + 0.08, lab, ha="center", fontsize=9)
        ax.set_ylim(-0.2, 1.4)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_title(title, fontsize=9, loc="left")
        ax.text(1.03, 0.2, "image", fontsize=8)
    axes[1].annotate("", xy=(0.44, -0.12), xytext=(0.06, -0.12), arrowprops=dict(arrowstyle="<->", lw=0.8))
    axes[1].annotate("", xy=(0.94, -0.12), xytext=(0.56, -0.12), arrowprops=dict(arrowstyle="<->", lw=0.8))
    axes[1].text(0.265, 0.12, "phase +phi", ha="center", fontsize=8)
    axes[1].text(0.735, 0.12, "phase -phi", ha="center", fontsize=8)
    axes[1].set_xlabel("time (arbitrary units)")
    axes[1].set_xticks([])
    save(fig, "09-sequences.png")


def main():
    raman()
    sequences()


if __name__ == "__main__":
    main()
