"""
Rydberg CZ gates: the Levine et al. (2019) two-pulse phase gate, the Jaksch
et al. (2000) pi-2pi-pi gate, and the main error sources.

Model
-----
Two atoms, each with levels {|0>, |1>, |r>}; only |1> couples to |r>.
With hbar = 1, for each atom

    H_i = (Omega/2) (e^{-i xi} |r><1| + e^{+i xi} |1><r|) - Delta |r><r| - (i Gamma/2) |r><r|

plus V |rr><rr| for the pair. The imaginary term models Rydberg decay as
population loss (non-Hermitian evolution); Doppler shifts add a random
detuning delta_i to each atom. The 9 x 9 Hamiltonian is piecewise constant, so
each pulse is a matrix exponential.

Levine gate: two global pulses of equal length tau and detuning Delta, the
second with laser phase xi. The parameters are chosen so that |01>, |10> and
|11> all return to the qubit subspace and the conditional phase
phi_11 - phi_01 - phi_10 equals pi. (With the phase convention above the paper's
values Delta/Omega = 0.377, tau Omega = 4.29, xi = 3.90 are recovered.)

Gate quality: the 4 x 4 block M of the propagator on the qubit subspace is
compared with CZ up to single-qubit Z rotations using the average gate fidelity
F = (|Tr(U^dag M)|^2 + Tr(M^dag M)) / 20  (Pedersen et al. 2007).

Units: time in us, angular frequencies in rad/us.
"""

import os
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
from scipy.optimize import minimize

Omega = 2 * np.pi * 3.5            # Rydberg Rabi frequency (rad/us)
C6 = 2 * np.pi * 862.7e3           # rad/us um^6 (70S)
R = 4.0                            # um
V0 = C6 / R**6                     # 2pi x 210.6 MHz
tau_r = 146.2                      # us, 70S lifetime at 300 K (ARC)
# 'Ideal' blockade: much larger than Omega, but not so large that expm loses unitarity
V_INF = 1e7                        # rad/us
k_eff = 8.745                      # 1/um (420 nm and 1013 nm counter-propagating)
sigma_v_10uK = 0.03093             # um/us, 1D rms velocity at 10 uK

ket = np.eye(3)
P1, Pr = np.outer(ket[1], ket[1]), np.outer(ket[2], ket[2])
Sr1 = np.outer(ket[2], ket[1])     # |r><1|
I3 = np.eye(3)
two = lambda A, B: np.kron(A, B)
rr = two(Pr, Pr)
comp = [0, 1, 3, 4]                # |00>, |01>, |10>, |11> in the 9-dim basis


def H_pair(xi, Delta, V=V0, Gamma=0.0, d1=0.0, d2=0.0, addr=(1, 1)):
    def single(d, on):
        drive = on * 0.5 * Omega * (np.exp(-1j * xi) * Sr1 + np.exp(1j * xi) * Sr1.T)
        return drive - (Delta + d) * Pr - 0.5j * Gamma * Pr
    return two(single(d1, addr[0]), I3) + two(I3, single(d2, addr[1])) + V * rr


def levine_U(params, **kw):
    Delta_over_Omega, tauOmega, xi = params
    D, tau = Delta_over_Omega * Omega, tauOmega / Omega
    return expm(-1j * H_pair(xi, D, **kw) * tau) @ expm(-1j * H_pair(0.0, D, **kw) * tau)


def fidelity_cz(U):
    M = U[np.ix_(comp, comp)]
    th = np.angle(M[1, 1])                       # single-qubit Z phase from |01>
    th2 = np.angle(M[2, 2])
    ideal = np.diag([1, np.exp(1j * th), np.exp(1j * th2), -np.exp(1j * (th + th2))])
    return (abs(np.trace(ideal.conj().T @ M))**2 + np.real(np.trace(M.conj().T @ M))) / 20


# ---------------------------------------------------------------------------
# 1) find the Levine parameters (ideal blockade, no decay)
# ---------------------------------------------------------------------------
def cost(p):
    return 1 - fidelity_cz(levine_U(p, V=V_INF))


best = min((minimize(cost, x0, method="Nelder-Mead", options=dict(xatol=1e-9, fatol=1e-14, maxiter=6000))
            for x0 in ([0.38, 4.3, 3.9], [0.35, 4.2, 3.7])), key=lambda r: r.fun)
params = best.x % np.array([np.inf, np.inf, 2 * np.pi])
U_ideal = levine_U(params, V=V_INF)
M = U_ideal[np.ix_(comp, comp)]
cond_phase = (np.angle(M[3, 3]) - np.angle(M[1, 1]) - np.angle(M[2, 2])) % (2 * np.pi)
T_gate = 2 * params[1] / Omega

# time-integrated Rydberg population for each input state (ideal blockade)
def rydberg_time(params, n=4000):
    D, tau = params[0] * Omega, params[1] / Omega
    dt = tau / n
    out = []
    n_r = two(Pr, I3) + two(I3, Pr)
    for idx in comp:
        psi = np.zeros(9, complex)
        psi[idx] = 1
        total = 0.0
        for xi in (0.0, params[2]):
            Ustep = expm(-1j * H_pair(xi, D, V=V_INF) * dt)
            for _ in range(n):
                total += np.real(psi.conj() @ n_r @ psi) * dt
                psi = Ustep @ psi
        out.append(total)
    return np.array(out)


T_R = rydberg_time(params)

# ---------------------------------------------------------------------------
# 2) error sources
# ---------------------------------------------------------------------------
G = 1 / tau_r
inf_decay = 1 - fidelity_cz(levine_U(params, Gamma=G, V=V_INF))
inf_decay_pred = np.mean(G * T_R)

inf_V = {V: 1 - fidelity_cz(levine_U(params, V=V)) for V in (V0, 2 * V0)}

rng = np.random.default_rng(1)


def doppler_infidelity(sigma_v, n=600):
    s = k_eff * sigma_v
    d = rng.standard_normal((n, 2)) * s
    return 1 - np.mean([fidelity_cz(levine_U(params, V=V_INF, d1=a, d2=b)) for a, b in d])


inf_dopp = doppler_infidelity(sigma_v_10uK)
inf_dopp_half = doppler_infidelity(sigma_v_10uK / 2)

# Jaksch pi-2pi-pi with local addressing
def pulse(t, addr):
    return expm(-1j * H_pair(0.0, 0.0, V=V_INF, addr=addr) * t)


tpi = np.pi / Omega
U_j = pulse(tpi, (1, 0)) @ pulse(2 * tpi, (0, 1)) @ pulse(tpi, (1, 0))
phases_j = np.angle(np.diag(U_j[np.ix_(comp, comp)])) / np.pi

print("Rydberg CZ gates (Omega/2pi = 3.5 MHz, 70S at R = 4 um, V/h = 210.6 MHz)")
print("=" * 72)
print(f"Levine gate: Delta/Omega = {params[0]:.4f}, tau*Omega = {params[1]:.4f} per pulse, "
      f"xi = {params[2]:.4f} rad")
print(f"   conditional phase = {cond_phase / np.pi:.6f} pi, fidelity (ideal blockade) = {fidelity_cz(U_ideal):.10f}")
print(f"   total gate time 2 tau = {T_gate * 1e3:.0f} ns = {2 * params[1]:.3f} / Omega")
print(f"   time in |r> (us): 00 {T_R[0]:.3f}, 01 {T_R[1]:.3f}, 10 {T_R[2]:.3f}, 11 {T_R[3]:.3f}")
print(f"decay (tau = {tau_r} us): infidelity {inf_decay:.3e}; prediction mean(Gamma T_R) = {inf_decay_pred:.3e}")
print(f"finite blockade: infidelity at V = {V0 / 2 / np.pi:.0f} MHz: {inf_V[V0]:.2e}; "
      f"at 2V: {inf_V[2 * V0]:.2e} (ratio {inf_V[V0] / inf_V[2 * V0]:.2f})")
print(f"Doppler, 10 uK: infidelity {inf_dopp:.2e}; at T/4 (sigma_v/2): {inf_dopp_half:.2e} "
      f"(ratio {inf_dopp / inf_dopp_half:.2f})")
print(f"Jaksch pi-2pi-pi phases / pi for |00>,|01>,|10>,|11>: {np.round(phases_j, 6)}")

# ---------------------------------------------------------------------------
# Figure: trajectories and error budget versus Omega
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.3))
D, tau = params[0] * Omega, params[1] / Omega
ts = np.linspace(0, 2 * tau, 400)
for idx, lab, col in [(1, "|01>", "C0"), (4, "|11>", "C3")]:
    pops = []
    for t in ts:
        if t <= tau:
            U = expm(-1j * H_pair(0.0, D, V=V_INF) * t)
        else:
            U = expm(-1j * H_pair(params[2], D, V=V_INF) * (t - tau)) @ expm(-1j * H_pair(0.0, D, V=V_INF) * tau)
        psi = U[:, idx]
        pops.append(abs(psi[idx])**2)
    ax1.plot(ts * 1e3, pops, color=col, lw=2, label=f"return probability, start {lab}")
ax1.axvline(tau * 1e3, color="0.6", ls=":", lw=1)
ax1.text(tau * 1e3 + 5, 0.9, "phase jump xi", fontsize=8)
ax1.set_xlabel("time (ns)")
ax1.set_ylabel("population of the initial state")
ax1.set_title("Levine gate: |11> closes after pulse 1, |01> after pulse 2", fontsize=9)
ax1.set_ylim(-0.3, 1.05)
ax1.legend(fontsize=8, loc="lower center", ncol=2)
Om = np.linspace(0.5, 12, 60) * 2 * np.pi
e_decay = np.mean(T_R * Omega) / Om * G                    # T_R scales as 1/Omega
e_dopp = inf_dopp * (Omega / Om)**2
e_block = inf_V[V0] * (Om / Omega)**2
ax2.loglog(Om / 2 / np.pi, e_decay, "C0", lw=2, label="Rydberg decay (tau = 146 us)")
ax2.loglog(Om / 2 / np.pi, e_dopp, "C1", lw=2, label="Doppler, 10 uK")
ax2.loglog(Om / 2 / np.pi, e_block, "C2", lw=2, label="finite blockade, V/h = 211 MHz")
ax2.loglog(Om / 2 / np.pi, e_decay + e_dopp + e_block, "k--", lw=1.5, label="sum")
ax2.set_xlabel("Rydberg Rabi frequency Omega / 2pi (MHz)")
ax2.set_ylabel("gate infidelity")
ax2.set_title("Error budget: faster helps decay and Doppler, hurts blockade", fontsize=9)
ax2.legend(fontsize=8)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "cz_gate.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
checks = {
    "optimiser reproduces Levine et al.: Delta/Omega = 0.377, tau Omega = 4.29, xi = 3.90":
        abs(params[0] - 0.377) < 2e-3 and abs(params[1] - 4.29) < 1e-2 and abs(params[2] - 3.90) < 1e-2,
    "with ideal blockade the gate is CZ (conditional phase pi, fidelity 1 - 1e-9)":
        abs(cond_phase - np.pi) < 1e-5 and fidelity_cz(U_ideal) > 1 - 1e-9,
    "|11> completes a full detuned cycle in one pulse: sqrt(2 + (Delta/Omega)^2) tau Omega = 2 pi":
        abs(np.sqrt(2 + params[0]**2) * params[1] - 2 * np.pi) < 1e-3,
    "time in |r> for |11> equals the analytic 2 tau Omega^2/(2 Omega^2 + Delta^2) (one full cycle per pulse)":
        abs(T_R[3] - 2 * (params[1] / Omega) * Omega**2 / (2 * Omega**2 + (params[0] * Omega)**2)) < 1e-3,
    "decay infidelity equals Gamma times the mean time in |r> (first-order loss model, 5%)":
        abs(inf_decay / inf_decay_pred - 1) < 0.05,
    "Doppler infidelity scales as sigma_v^2 (ratio 4 within 25%, independent random draws)":
        abs(inf_dopp / inf_dopp_half / 4 - 1) < 0.25,
    "finite-blockade infidelity scales as 1/V^2 (ratio 4 within 15%)":
        abs(inf_V[V0] / inf_V[2 * V0] / 4 - 1) < 0.15,
    "Jaksch pi-2pi-pi gives phases (0, pi, pi, pi): CZ up to local Z":
        np.allclose(np.abs(phases_j), [0, 1, 1, 1], atol=1e-6),
}
