"""Chapter 05 figures: Zeeman slower layout and field, molasses force, Doppler temperature."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle

import atomdata as A
from style import save

G = A.GAMMA_D2
k = A.K_D2


def zeeman_slower():
    # same design as hands-on lab 02
    v0, vf, eta, dL = 300.0, 30.0, 0.6, -2 * np.pi * 160e6
    a = eta * A.A_MAX
    L = (v0**2 - vf**2) / (2 * a)
    z = np.linspace(0, L, 400)
    vd = np.sqrt(v0**2 - 2 * a * z)
    B = A.hbar * (dL + k * vd) / A.muB * 1e4   # gauss

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_axes([0.06, 0.55, 0.9, 0.40])
    ax.axis("off")
    ax.set_xlim(-25, 95)
    ax.set_ylim(-7, 8)
    ax.add_patch(Rectangle((-22, -2.5), 10, 5, fc="0.75", ec="k"))
    ax.text(-17, 0, "oven\n~400 K", ha="center", va="center", fontsize=8)
    # coil windings: thicker where the field is larger in magnitude
    zz = np.linspace(0, L * 100, 40)
    for zi in zz:
        bi = np.interp(zi / 100, z, np.abs(B))
        h = 1.0 + 3.0 * bi / np.abs(B).max()
        ax.add_patch(Rectangle((zi - 0.7, 1.2), 1.4, h, fc="#d9a066", ec="none"))
        ax.add_patch(Rectangle((zi - 0.7, -1.2 - h), 1.4, h, fc="#d9a066", ec="none"))
    ax.text(L * 50, 5.9, "tapered solenoid: field decreases, crosses zero, ends abruptly", ha="center", fontsize=8)
    ax.add_patch(Circle((83, 0), 3.2, fc="#f4c7c3", ec="C3"))
    ax.text(83, -4.8, "MOT", ha="center", fontsize=9)
    ax.add_patch(FancyArrowPatch((-12, 0), (78, 0), arrowstyle="-|>", mutation_scale=14, color="k", lw=1.5))
    ax.text(30, 0.45, "atoms, 300 m/s -> 30 m/s", ha="center", fontsize=8)
    ax.add_patch(FancyArrowPatch((93, -0.9), (-10, -0.9), arrowstyle="-|>", mutation_scale=14, color="C3", lw=2))
    ax.text(30, -5.6, "<- slowing laser (sigma+, red detuned by 160 MHz), counter-propagating", ha="center", va="top", fontsize=8, color="C3")
    ax2 = fig.add_axes([0.06 + 0.9 * 25 / 120, 0.09, 0.9 * (L * 100) / 120, 0.40])
    ax2.plot(z * 100, B, "C0", lw=2)
    ax2.axhline(0, color="0.7", lw=0.8)
    ax2.set_xlim(0, L * 100)
    ax2.set_xlabel("position along the slower (cm)")
    ax2.set_ylabel("B (G)")
    ax2.set_title(f"field that keeps v_d(z) resonant (L = {L * 100:.0f} cm, eta = 0.6); dashed: v_d(z), same shape", fontsize=9)
    ax3 = ax2.twinx()
    ax3.plot(z * 100, vd, "k--", lw=1)
    ax3.set_ylabel("design velocity (m/s)", fontsize=9)
    ax3.spines["right"].set_visible(True)
    save(fig, "05-zeeman-slower.png")


def molasses_force():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
    s0 = 1.0
    v = np.linspace(-15, 15, 800)
    for dl, col in [(-0.5, "C1"), (-1.0, "C3"), (-2.0, "C0")]:
        d = dl * G
        Fp = A.hbar * k * G / 2 * s0 / (1 + s0 + (2 * (d - k * v) / G)**2)
        Fm = -A.hbar * k * G / 2 * s0 / (1 + s0 + (2 * (d + k * v) / G)**2)
        ax2.plot(v, (Fp + Fm) * 1e21, color=col, lw=2, label=f"delta = {dl} Gamma")
        if dl == -1.0:
            ax1.plot(v, Fp * 1e21, "C3--", lw=1.2, label="beam along +z")
            ax1.plot(v, Fm * 1e21, "C0--", lw=1.2, label="beam along -z")
            ax1.plot(v, (Fp + Fm) * 1e21, "k", lw=2, label="sum")
    for ax in (ax1, ax2):
        ax.axhline(0, color="0.7", lw=0.8)
        ax.axvline(0, color="0.7", lw=0.8)
        ax.set_xlabel("atom velocity v (m/s)")
        ax.set_ylabel("force (1e-21 N)")
    ax1.set_title("delta = -Gamma, s0 = 1 per beam: each beam pushes,\nthe one the atom moves toward pushes harder", fontsize=9)
    ax1.legend(fontsize=8)
    ax2.set_title("Total force: friction near v = 0,\ncapture range of a few Gamma/k = few x 4.7 m/s", fontsize=9)
    ax2.legend(fontsize=8)
    save(fig, "05-molasses-force.png")


def doppler_temperature():
    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    x = np.linspace(0.08, 6, 500)          # 2|delta|/Gamma
    TD = A.T_DOPPLER
    for s0, col in [(0.0, "k"), (0.5, "C1"), (2.0, "C3")]:
        T = A.hbar * G / 4 * (1 + s0 + x**2) / x / A.kB
        ax.plot(-x / 2, T * 1e6, color=col, lw=2, label=f"s0 = {s0} (per beam)")
    ax.axhline(TD * 1e6, color="0.5", ls=":", lw=1)
    ax.plot([-0.5], [TD * 1e6], "ko")
    ax.annotate("Doppler limit: delta = -Gamma/2,\nT_D = hbar Gamma / 2 k_B = 145.6 uK", xy=(-0.5, TD * 1e6),
                xytext=(-2.6, 60), fontsize=9, arrowprops=dict(arrowstyle="->"))
    ax.set_xlim(-3, 0)
    ax.set_ylim(0, 800)
    ax.set_xlabel("detuning delta / Gamma")
    ax.set_ylabel("Doppler temperature (uK)")
    ax.set_title("Doppler-cooling theory for Rb-87: k_B T = (hbar Gamma/4)(1 + s0 + x^2)/x")
    ax.legend(fontsize=8, loc="upper left")
    save(fig, "05-doppler-temperature.png")


def main():
    zeeman_slower()
    molasses_force()
    doppler_temperature()


if __name__ == "__main__":
    main()
