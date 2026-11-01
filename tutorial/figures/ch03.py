"""Chapter 03 figures: two-level atom schematic, Bloch-sphere dynamics, saturation."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

import atomdata as A
from style import save


def two_level():
    fig, ax = plt.subplots(figsize=(8.2, 4.4))
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.6, 6)
    ax.hlines(0.5, 1, 4.5, lw=2.5, color="k")
    ax.hlines(5.0, 1, 4.5, lw=2.5, color="k")
    ax.hlines(4.3, 1.2, 4.3, lw=1, color="C3", ls="--")
    ax.text(0.85, 0.5, "|g>", ha="right", va="center", fontsize=13)
    ax.text(0.85, 5.0, "|e>", ha="right", va="center", fontsize=13)
    ax.annotate("", xy=(2.2, 4.3), xytext=(2.2, 0.5),
                arrowprops=dict(arrowstyle="<->", color="C3", lw=2.2))
    ax.text(2.0, 2.6, "laser\nomega_L\ncoupling Omega", ha="right", va="center", color="C3", fontsize=9)
    ax.annotate("", xy=(3.0, 5.0), xytext=(3.0, 4.3), arrowprops=dict(arrowstyle="<->", lw=1))
    ax.text(3.1, 4.65, "|delta| (red: delta < 0)", va="center", fontsize=9)
    ax.annotate("", xy=(3.6, 0.5), xytext=(3.6, 5.0),
                arrowprops=dict(arrowstyle="->", color="C0", lw=1.8, ls=(0, (4, 2))))
    ax.text(3.7, 1.6, "spontaneous\nemission,\nrate Gamma", color="C0", fontsize=9)
    ax.text(5.3, 5.3, "Rb-87 D2 cycling transition", fontsize=10, weight="bold")
    rows = [("|g> = |F=2, m_F=2>", ""), ("|e> = |F'=3, m_F'=3>", ""),
            ("wavelength", "780.241 nm"), ("Gamma / 2pi", "6.0666 MHz"),
            ("lifetime 1/Gamma", "26.2 ns"), ("dipole (cycling)", "2.99 e a0"),
            ("I_sat", "1.669 mW/cm^2"), ("cross-section 3 lambda^2/2pi", "0.291 um^2")]
    for i, (k, v) in enumerate(rows):
        ax.text(5.3, 4.6 - 0.55 * i, k, fontsize=9)
        ax.text(9.9, 4.6 - 0.55 * i, v, fontsize=9, ha="right")
    save(fig, "03-two-level.png")


def bloch_rhs(t, r, Om, de, G):
    u, v, w = r
    bx, by, bz = Om, 0.0, -de
    du = by * w - bz * v - G / 2 * u
    dv = bz * u - bx * w - G / 2 * v
    dw = bx * v - by * u - G * (w + 1)
    return [du, dv, dw]


def bloch():
    fig = plt.figure(figsize=(11, 4.6))
    G = A.GAMMA_D2
    cases = [("resonant, no decay", 2 * G, 0.0, 0.0, 3.0),
             ("detuned delta = Omega, no decay", 2 * G, 2 * G, 0.0, 3.0),
             ("resonant with decay (Omega = 3 Gamma)", 3 * G, 0.0, G, 8.0)]
    for k, (title, Om, de, Gm, tmax_over_G) in enumerate(cases):
        ax = fig.add_subplot(1, 3, k + 1, projection="3d")
        uu, vv = np.mgrid[0:2 * np.pi:40j, 0:np.pi:20j]
        ax.plot_wireframe(np.cos(uu) * np.sin(vv), np.sin(uu) * np.sin(vv), np.cos(vv),
                          color="0.85", lw=0.4)
        t = np.linspace(0, tmax_over_G / G, 1500)
        sol = solve_ivp(bloch_rhs, (0, t[-1]), [0, 0, -1], t_eval=t, args=(Om, de, Gm),
                        rtol=1e-9, atol=1e-11)
        ax.plot(*sol.y, color="C3", lw=1.6)
        ax.scatter(*sol.y[:, -1], color="C3", s=20)
        b = np.array([Om, 0, -de]) / np.hypot(Om, de)
        ax.quiver(0, 0, 0, *b, color="C0", lw=1.5, arrow_length_ratio=0.12)
        ax.text(*(1.15 * b), "rotation\naxis", color="C0", fontsize=7)
        ax.text(0, 0, 1.25, "|e>", ha="center", fontsize=9)
        ax.text(0, 0, -1.35, "|g>", ha="center", fontsize=9)
        ax.set_box_aspect((1, 1, 1))
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-1, 1)
        ax.set_axis_off()
        ax.view_init(elev=18, azim=-60)
        ax.set_title(title, fontsize=9)
    save(fig, "03-bloch.png")


def saturation():
    G = A.GAMMA_D2
    s0 = np.logspace(-2, 2.5, 300)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0))
    for dl, col in [(0.0, "C3"), (-0.5, "C1"), (-2.0, "C0")]:
        rate = G / 2 * s0 / (1 + s0 + (2 * dl)**2)
        ax1.loglog(s0, rate, color=col, lw=2, label=f"delta = {dl:g} Gamma")
    ax1.axhline(G / 2, color="k", ls="--", lw=0.8)
    ax1.text(0.012, G / 2 * 1.15, "Gamma/2 = 1.9e7 photons/s", fontsize=8)
    ax1.axvline(1, color="0.8", lw=0.8)
    ax1.set_xlabel("saturation parameter s0 = I / I_sat")
    ax1.set_ylabel("scattering rate (photons/s)")
    ax1.set_title("Scattering saturates at Gamma/2")
    ax1.legend(fontsize=8, loc="lower right")
    ax2.plot(s0, np.sqrt(1 + s0), "C2", lw=2)
    ax2.set_xscale("log")
    ax2.set_xlabel("s0")
    ax2.set_ylabel("FWHM / Gamma")
    ax2.set_title("Power broadening: FWHM = Gamma sqrt(1 + s0)")
    for s in [1, 10, 100]:
        ax2.plot(s, np.sqrt(1 + s), "ko", ms=4)
        ax2.text(s * 0.6, np.sqrt(1 + s) + 0.5, f"{np.sqrt(1 + s) * 6.0666:.1f} MHz", fontsize=8)
    save(fig, "03-saturation.png")


def main():
    two_level()
    bloch()
    saturation()


if __name__ == "__main__":
    main()
