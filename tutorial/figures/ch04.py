"""Chapter 04 figures: scattering force, light shift / dressed states, Gaussian-beam
dipole potentials, and the momentum random walk of spontaneous emission."""
import numpy as np
import matplotlib.pyplot as plt

import atomdata as A
from style import save


def force_and_lightshift():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.3))
    d = np.linspace(-6, 6, 600)              # delta / Gamma
    for s0, col in [(0.1, "C0"), (1, "C1"), (10, "C3")]:
        F = s0 / (1 + s0 + (2 * d)**2)       # in units of hbar k Gamma / 2
        ax1.plot(d, F, color=col, lw=2, label=f"s0 = {s0}")
    ax1.axhline(1, color="k", ls="--", lw=0.8)
    ax1.text(-5.9, 1.02, "maximum hbar k Gamma/2 = 1.6e-20 N  (1.1e4 g for Rb)", fontsize=8)
    ax1.set_xlabel("detuning delta / Gamma")
    ax1.set_ylabel("scattering force / (hbar k Gamma / 2)")
    ax1.set_title("Radiation-pressure force: always along the beam")
    ax1.set_ylim(0, 1.12)
    ax1.legend(fontsize=8)

    # exact dressed-state energies in the rotating frame vs detuning, fixed Omega
    Om = 1.0
    dd = np.linspace(-5, 5, 800)
    Ep = -dd / 2 + 0.5 * np.sqrt(dd**2 + Om**2)
    Em = -dd / 2 - 0.5 * np.sqrt(dd**2 + Om**2)
    ax2.plot(dd, Ep, "C3", lw=2, label="dressed states (exact)")
    ax2.plot(dd, Em, "C3", lw=2)
    ax2.plot(dd, 0 * dd, "k:", lw=1, label="bare |g>, energy 0")
    ax2.plot(dd, -dd, "k--", lw=1, label="bare |e>, energy -hbar delta")
    mask = np.abs(dd) > 1.2
    gshift = np.where(mask, Om**2 / (4 * dd), np.nan)
    ax2.plot(dd, gshift, "C0", lw=1.5, ls="-.", label="perturbative shift of |g>: Omega^2/(4 delta)")
    ax2.set_xlabel("detuning delta / Omega")
    ax2.set_ylabel("energy / (hbar Omega)")
    ax2.set_title("Light shift: red light lowers |g>, blue light raises it")
    ax2.set_ylim(-3, 3)
    ax2.legend(fontsize=7.5, loc="upper right")
    ax2.annotate("red detuned:\n|g> pushed down", xy=(-3, Om**2 / (4 * -3)), xytext=(-4.9, -1.9),
                 fontsize=8, arrowprops=dict(arrowstyle="->"))
    save(fig, "04-forces.png")


def gaussian_potentials():
    """Two-level dipole potential across a 1 mW, w0 = 10 um beam at +/- 50 GHz detuning."""
    G = A.GAMMA_D2
    P, w0 = 1e-3, 10e-6
    r = np.linspace(-25e-6, 25e-6, 600)
    I = 2 * P / (np.pi * w0**2) * np.exp(-2 * r**2 / w0**2)
    s = I / A.I_SAT_CYCLING
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.0))
    for de_GHz, col, lab in [(-50, "C3", "red, delta = -2pi x 50 GHz"), (50, "C0", "blue, delta = +2pi x 50 GHz")]:
        de = 2 * np.pi * de_GHz * 1e9
        U = A.hbar * de / 2 * np.log(1 + s / (1 + (2 * de / G)**2))
        ax1.plot(r * 1e6, U / A.kB * 1e3, color=col, lw=2, label=lab)
        gam = G / 2 * s / (1 + s + (2 * de / G)**2)
        if de_GHz < 0:
            ax2.plot(r * 1e6, gam, "k", lw=2)
    ax1.axhline(0, color="0.6", lw=0.8)
    ax1.set_xlabel("radial position r (um)")
    ax1.set_ylabel("dipole potential U / k_B (mK)")
    ax1.set_title("1 mW focused to w0 = 10 um (Rb D2, two-level)")
    ax1.legend(fontsize=8, loc="upper left")
    ax1.annotate("atom attracted\nto the focus", xy=(0, -1.68), xytext=(8, -1.3), fontsize=8,
                 arrowprops=dict(arrowstyle="->"))
    ax2.set_xlabel("radial position r (um)")
    ax2.set_ylabel("photon scattering rate (1/s)")
    ax2.set_title("...but it scatters 2.7e4 photons/s at the centre")
    ax2.text(7, 2.0e4, "each photon heats by\n~2 E_r; 1.7 mK of\ndepth is gone in ~0.2 s", fontsize=8)
    save(fig, "04-dipole-potential.png")


def random_walk():
    rng = np.random.default_rng(7)
    N, walkers = 2000, 400
    absorb = np.ones((walkers, N))                       # +hbar k each absorption (beam along +z)
    cos_t = rng.uniform(-1, 1, (walkers, N))             # isotropic emission: z-component = cos(theta)
    p = np.cumsum(absorb - cos_t, axis=1)                # momentum along z in units of hbar k
    n = np.arange(1, N + 1)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.0))
    for k in range(6):
        ax1.plot(n, p[k] - n, lw=0.8)
    ax1.plot(n, np.sqrt(n / 3), "k--", lw=1.2, label="+/- sqrt(N/3) (isotropic emission)")
    ax1.plot(n, -np.sqrt(n / 3), "k--", lw=1.2)
    ax1.set_xlabel("number of scattered photons N")
    ax1.set_ylabel("p_z - N hbar k   (units of hbar k)")
    ax1.set_title("Emission kicks: a random walk about the mean push")
    ax1.legend(fontsize=8, loc="lower left")
    ax2.plot(n, p.mean(axis=0), "C3", lw=2, label="mean momentum (simulated)")
    ax2.plot(n, n, "k:", lw=1, label="N hbar k")
    ax2.set_xlabel("number of scattered photons N")
    ax2.set_ylabel("mean p_z (units of hbar k)")
    ax2.set_title("Absorption kicks add up: the scattering force")
    ax2.legend(fontsize=8)
    save(fig, "04-random-walk.png")
    return p[:, -1].std(), np.sqrt(N / 3)


def main():
    force_and_lightshift()
    gaussian_potentials()
    random_walk()


if __name__ == "__main__":
    main()
