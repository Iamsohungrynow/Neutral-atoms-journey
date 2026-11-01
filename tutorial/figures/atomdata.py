"""Shared physical constants and reference atomic data for every figure script.

All numbers here are the single source of truth quoted in the chapters and in
tutorial/00-notation.md. Rb-87 D-line data follow D. A. Steck, "Rubidium 87 D
Line Data" (steck.us/alkalidata); Rydberg-state numbers were computed with the
ARC library (Sibalic et al., Comput. Phys. Commun. 220, 319 (2017)).
"""
import numpy as np
from scipy import constants as _C

h = _C.h
hbar = _C.hbar
kB = _C.k
c = _C.c
eps0 = _C.epsilon_0
amu = _C.atomic_mass
a0 = _C.physical_constants["Bohr radius"][0]
muB = _C.physical_constants["Bohr magneton"][0]
g0 = 9.80665
AU_POL = 4 * np.pi * eps0 * a0**3      # SI value of one atomic unit of polarizability

# ---- Rb-87 ---------------------------------------------------------------
M_RB87 = 86.909180531 * amu
LAMBDA_D1 = 794.978851156e-9           # 5S1/2 -> 5P1/2, vacuum wavelength
LAMBDA_D2 = 780.241209686e-9           # 5S1/2 -> 5P3/2, vacuum wavelength
GAMMA_D1 = 2 * np.pi * 5.7500e6        # natural linewidth (angular), D1
GAMMA_D2 = 2 * np.pi * 6.0666e6        # natural linewidth (angular), D2
OMEGA_D1 = 2 * np.pi * c / LAMBDA_D1
OMEGA_D2 = 2 * np.pi * c / LAMBDA_D2
F_HFS = 6.834682610904e9               # ground hyperfine splitting (Hz)
K_D2 = 2 * np.pi / LAMBDA_D2

# Derived D2 laser-cooling scales (checked against Steck's tables)
T_DOPPLER = hbar * GAMMA_D2 / (2 * kB)                 # 145.6 uK
V_RECOIL = hbar * K_D2 / M_RB87                        # 5.885 mm/s
T_RECOIL = (hbar * K_D2)**2 / (M_RB87 * kB)            # 362 nK (Steck's convention)
E_RECOIL = (hbar * K_D2)**2 / (2 * M_RB87)             # h x 3.771 kHz
I_SAT_CYCLING = np.pi * h * c * GAMMA_D2 / (3 * LAMBDA_D2**3)   # 16.69 W/m^2 = 1.669 mW/cm^2
A_MAX = hbar * K_D2 * GAMMA_D2 / (2 * M_RB87)          # 1.12e5 m/s^2

# Rydberg excitation (two-photon ladder via 6P3/2) and 70S1/2 numbers (ARC)
LAMBDA_420 = 420.299e-9                # 5S1/2 -> 6P3/2
LAMBDA_1013 = 1012.79e-9               # 6P3/2 -> 70S1/2
C6_70S_HZ_UM6 = 862.7e9                # C6/h for 70S1/2-70S1/2, Hz um^6 (repulsive)
TAU_70S_0K = 373.9e-6                  # radiative lifetime, 0 K
TAU_70S_300K = 146.5e-6                # including blackbody, 300 K


def alpha_ground(lam, hfs_shift=0.0):
    """Scalar ground-state polarizability of Rb-87 (SI) from the D1 and D2 lines.

    Each line is a damped Lorentz oscillator with its counter-rotating term,
    alpha = (2J'+1)/(3(2J+1)) * 6 pi eps0 c^3 Gamma/w0^2 / (w0^2 - w^2),
    i.e. weights 1/3 (D1) and 2/3 (D2). Higher states add ~1% at 1064 nm.
    hfs_shift (angular) is added to both transition frequencies.
    """
    w = 2 * np.pi * c / np.asarray(lam, dtype=float)
    a = 0.0
    for w0, G, wt in [(OMEGA_D1, GAMMA_D1, 1 / 3), (OMEGA_D2, GAMMA_D2, 2 / 3)]:
        dip = wt * 6 * np.pi * eps0 * c**3 * G / w0**3     # keep |d|^2 fixed
        w0s = w0 + hfs_shift
        a = a + dip * w0s / (w0s**2 - w**2)
    return a


def scatter_rate_ground(lam, intensity):
    """Photon scattering rate (1/s) of a ground-state Rb-87 atom in light of given intensity."""
    w = 2 * np.pi * c / np.asarray(lam, dtype=float)
    r = 0.0
    for w0, G, wt in [(OMEGA_D1, GAMMA_D1, 1 / 3), (OMEGA_D2, GAMMA_D2, 2 / 3)]:
        r = r + wt * 3 * np.pi * c**2 / (2 * hbar * w0**3) * (w / w0)**3 * (
            G / (w0 - w) + G / (w0 + w))**2 * intensity
    return r


def trap_depth(lam, power, waist):
    """Peak light shift U0 (J, positive = attractive) of a focused Gaussian beam."""
    I0 = 2 * power / (np.pi * waist**2)
    return alpha_ground(lam) * I0 / (2 * eps0 * c)


def eta_differential(lam):
    """Differential light shift between F=2 and F=1, as a fraction of the trap depth."""
    wh = 2 * np.pi * F_HFS
    return (alpha_ground(lam, -wh) - alpha_ground(lam)) / alpha_ground(lam)
