"""
Optical Bloch equations for a driven, decaying two-level atom (QuTiP).

Physics
-------
Rotating frame, rotating-wave approximation, laser detuning delta = wL - w0:

    H/hbar = -delta |e><e| + (Omega/2) (|e><g| + |g><e|)

Spontaneous emission at rate Gamma enters through the collapse operator
sqrt(Gamma) |g><e|. The steady-state excited population is

    rho_ee = (s0/2) / (1 + s0 + (2 delta/Gamma)^2),   s0 = 2 Omega^2 / Gamma^2,

so the photon scattering rate Gamma*rho_ee saturates at Gamma/2 and the
line (full width at half maximum) is power broadened to Gamma*sqrt(1 + s0).

We use the Rb-87 D2 line, Gamma/2pi = 6.0666 MHz. Units: time in us,
angular frequencies in rad/us (so 2*pi*6.0666 rad/us is Gamma).

Convention: |g> = basis(2, 0), |e> = basis(2, 1).
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from qutip import basis, mesolve, sesolve, steadystate, expect

GAMMA = 2 * np.pi * 6.0666          # rad/us, Rb-87 D2 natural linewidth
g, e = basis(2, 0), basis(2, 1)
Pe = e * e.dag()                     # excited-state projector
sig = g * e.dag()                    # lowering operator |g><e|


def hamiltonian(Omega, delta):
    return -delta * Pe + 0.5 * Omega * (e * g.dag() + g * e.dag())


def rho_ee_analytic(Omega, delta, Gamma=GAMMA):
    s0 = 2 * Omega**2 / Gamma**2
    return 0.5 * s0 / (1 + s0 + (2 * delta / Gamma)**2)


# ---------------------------------------------------------------------------
# Part 1: damped Rabi oscillations on resonance
# ---------------------------------------------------------------------------
tlist = np.linspace(0, 0.30, 1501)            # 0 to 300 ns
rabi_cases = [0.5, 2.0, 5.0]                  # Omega in units of Gamma
traces = {}
for r in rabi_cases:
    Omega = r * GAMMA
    res = mesolve(hamiltonian(Omega, 0.0), g * g.dag(), tlist,
                  c_ops=[np.sqrt(GAMMA) * sig], e_ops=[Pe],
                  options={"atol": 1e-10, "rtol": 1e-8})
    traces[r] = np.real(res.expect[0])

# Undamped reference: Gamma -> 0 must give sin^2(Omega t / 2)
Omega_ref = 2.0 * GAMMA
undamped = np.real(sesolve(hamiltonian(Omega_ref, 0.0), g, tlist, e_ops=[Pe],
                           options={"atol": 1e-10, "rtol": 1e-8}).expect[0])

# ---------------------------------------------------------------------------
# Part 2: steady-state line shape versus detuning and saturation
# ---------------------------------------------------------------------------
deltas = np.linspace(-6, 6, 481) * GAMMA
s0_values = [0.1, 1.0, 10.0]
lines = {}
for s0 in s0_values:
    Omega = GAMMA * np.sqrt(s0 / 2)
    lines[s0] = np.array([np.real(expect(Pe, steadystate(hamiltonian(Omega, d),
                                                            [np.sqrt(GAMMA) * sig])))
                          for d in deltas])


def fwhm(x, y):
    """Full width at half maximum by linear interpolation on each side."""
    half = y.max() / 2
    i = np.where(y >= half)[0]
    lo, hi = i[0], i[-1]
    xl = np.interp(half, [y[lo - 1], y[lo]], [x[lo - 1], x[lo]])
    xr = np.interp(half, [y[hi + 1], y[hi]], [x[hi + 1], x[hi]])
    return xr - xl


# ---------------------------------------------------------------------------
# Print results
# ---------------------------------------------------------------------------
print("Optical Bloch equations, Rb-87 D2 (Gamma/2pi = 6.0666 MHz)")
print("=" * 64)
for r in rabi_cases:
    ss = rho_ee_analytic(r * GAMMA, 0.0)
    print(f"Omega = {r:3.1f} Gamma: first maximum rho_ee = {traces[r].max():.4f}, "
          f"value at 300 ns = {traces[r][-1]:.4f}, analytic steady state = {ss:.4f}")
print("-" * 64)
widths = {}
for s0 in s0_values:
    w_num = fwhm(deltas, lines[s0]) / (2 * np.pi)
    w_th = GAMMA * np.sqrt(1 + s0) / (2 * np.pi)
    widths[s0] = (w_num, w_th)
    print(f"s0 = {s0:5.1f}: peak rho_ee = {lines[s0].max():.4f} "
          f"(analytic {s0 / 2 / (1 + s0):.4f}); FWHM = {w_num:.3f} MHz "
          f"(Gamma*sqrt(1+s0)/2pi = {w_th:.3f} MHz)")
rate_max = GAMMA * 1e6 * lines[10.0].max()
print(f"Scattering rate at s0 = 10 on resonance: {rate_max:.3e} photons/s "
      f"(limit Gamma/2 = {GAMMA * 1e6 / 2:.3e})")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.3))
for r, col in zip(rabi_cases, ["C0", "C1", "C2"]):
    ax1.plot(tlist * 1e3, traces[r], color=col, label=f"Omega = {r} Gamma")
    ax1.axhline(rho_ee_analytic(r * GAMMA, 0), color=col, ls=":", lw=1)
ax1.plot(tlist * 1e3, undamped, "k--", lw=0.8, alpha=0.6, label="Omega = 2 Gamma, no decay")
ax1.set_xlabel("time (ns)")
ax1.set_ylabel("excited population rho_ee")
ax1.set_title("Damped Rabi oscillations (dotted: steady state)")
ax1.set_ylim(0, 1.05)
ax1.legend(fontsize=8, loc="upper right")
for s0, col in zip(s0_values, ["C0", "C1", "C2"]):
    ax2.plot(deltas / GAMMA, lines[s0], color=col, label=f"s0 = {s0}")
    ax2.plot(deltas[::24] / GAMMA, rho_ee_analytic(GAMMA * np.sqrt(s0 / 2), deltas[::24]),
             "o", color=col, ms=3)
ax2.set_xlabel("detuning delta / Gamma")
ax2.set_ylabel("steady-state rho_ee")
ax2.set_title("Saturation and power broadening (dots: analytic)")
ax2.legend(fontsize=8)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "obe.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks (read by hands-on/run_labs.py --check)
# ---------------------------------------------------------------------------
analytic_lines = {s0: rho_ee_analytic(GAMMA * np.sqrt(s0 / 2), deltas) for s0 in s0_values}
checks = {
    "no-decay limit equals sin^2(Omega t/2)":
        np.allclose(undamped, np.sin(Omega_ref * tlist / 2)**2, atol=1e-6),
    "steady state equals (s0/2)/(1+s0+(2delta/Gamma)^2) for all detunings":
        all(np.allclose(lines[s0], analytic_lines[s0], atol=1e-9) for s0 in s0_values),
    "time evolution relaxes to the steady state after ~50 lifetimes":
        all(abs(traces[r][-1] - rho_ee_analytic(r * GAMMA, 0)) < 2e-3 for r in rabi_cases),
    "FWHM equals Gamma*sqrt(1+s0) within 0.5%":
        all(abs(w / t - 1) < 5e-3 for w, t in widths.values()),
    "scattering never exceeds Gamma/2":
        max(l.max() for l in lines.values()) < 0.5 and max(t.max() for t in traces.values()) <= 1.0,
}
