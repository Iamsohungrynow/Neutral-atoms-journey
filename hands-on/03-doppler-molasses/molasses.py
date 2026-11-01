"""
One-dimensional optical molasses: exact event-by-event Monte Carlo of photon kicks.

Physics
-------
Two counter-propagating beams, each with saturation parameter s0 and detuning
delta, act on an atom moving with velocity v along z. The beam travelling along
+z is seen at detuning delta - k v, the one along -z at delta + k v, so the
absorption rates are

    R_plus(v)  = (Gamma/2) s0 / (1 + s0 + (2 (delta - k v)/Gamma)^2)
    R_minus(v) = (Gamma/2) s0 / (1 + s0 + (2 (delta + k v)/Gamma)^2)

(beams treated independently: valid for s0 << 1). Each absorption gives a kick
+hbar k or -hbar k. Emission model (stated explicitly, because the answer
depends on it): the emitted photon goes along +z or -z with equal probability,
giving a kick of +/- hbar k. Between events the velocity is constant, so the
simulation is exact: wait an exponential time with rate R_plus + R_minus, pick
which beam was absorbed, apply the absorption and emission kicks.

Analytic predictions for this model (linear in v, i.e. k v << Gamma):
  friction        F = -beta v,  beta = -8 hbar k^2 delta s0 / (Gamma (1 + s0 + (2 delta/Gamma)^2)^2)
  diffusion       d<p^2>/dt = 2 D_p with D_p = 2 R0 (hbar k)^2, R0 = R_plus(0)
  temperature     k_B T = D_p / beta = (hbar Gamma / 4) (1 + s0 + x^2) / x,  x = 2|delta|/Gamma
which is minimal at x = sqrt(1 + s0): the Doppler limit hbar Gamma / 2 as s0 -> 0.

Units: SI.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

hbar = 1.054571817e-34
kB = 1.380649e-23
m = 86.909180531 * 1.66053906660e-27
M_ATOM = m
k = 2 * np.pi / 780.241209686e-9
Gamma = 2 * np.pi * 6.0666e6
vr = hbar * k / m
rng = np.random.default_rng(2024)

s0 = 0.05                     # per beam, low enough for independent beams


def rates(v, delta):
    rp = (Gamma / 2) * s0 / (1 + s0 + (2 * (delta - k * v) / Gamma)**2)
    rm = (Gamma / 2) * s0 / (1 + s0 + (2 * (delta + k * v) / Gamma)**2)
    return rp, rm


def T_analytic(delta):
    x = 2 * abs(delta) / Gamma
    return hbar * Gamma / 4 * (1 + s0 + x**2) / x / kB


def beta_analytic(delta):
    return -8 * hbar * k**2 * delta * s0 / (Gamma * (1 + s0 + (2 * delta / Gamma)**2)**2)


def simulate(delta, n_atoms=3000, n_events=5000, n_burn=2000, v_start=0.3):
    """Return per-atom time-averaged v^2 (after burn-in) and a sample trace."""
    v = rng.choice([-1, 1], n_atoms) * v_start
    sum_v2t = np.zeros(n_atoms)
    sum_t = np.zeros(n_atoms)
    trace_t, trace_v, t_now = [0.0], [v[0]], 0.0
    for i in range(n_events):
        rp, rm = rates(v, delta)
        R = rp + rm
        dt = rng.exponential(1.0 / R)
        if i >= n_burn:
            sum_v2t += v**2 * dt
            sum_t += dt
        t_now += dt[0]
        absorb = np.where(rng.random(n_atoms) < rp / R, 1.0, -1.0)
        emit = rng.choice([-1.0, 1.0], n_atoms)
        v = v + (absorb + emit) * vr
        if i % 5 == 0:
            trace_t.append(t_now)
            trace_v.append(v[0])
    return sum_v2t / sum_t, np.array(trace_t), np.array(trace_v)


def mean_force(v, delta, n=400000):
    """Count kicks at fixed velocity: mean force = hbar k (N_plus - N_minus)/time."""
    rp, rm = rates(v, delta)
    t = n / (rp + rm)
    n_plus = rng.binomial(n, rp / (rp + rm))
    return hbar * k * (2 * n_plus - n) / t, hbar * k * (rp - rm)


# ---------------------------------------------------------------------------
# 1) friction: simulated mean force versus velocity at delta = -Gamma/2
# ---------------------------------------------------------------------------
delta0 = -Gamma / 2
v_probe = np.linspace(-6, 6, 25)
F_sim, _ = np.array([mean_force(v, delta0) for v in v_probe]).T
# Friction measured from the DYNAMICS: atoms all start at +v0 (inside the linear
# region) and receive random kicks; the mean velocity must decay as exp(-beta t / m).
# Fixed small time steps (event probability per step about 4%, 2% per beam) are used here so that all
# atoms share one clock; the equilibrium temperatures below use the exact event loop.
def mean_velocity_decay(delta, v0=0.5, n_atoms=20000, t_max=1.2e-3, dt=4e-8):
    v = np.full(n_atoms, v0)
    n_steps = int(t_max / dt)
    t_out, v_out = [], []
    for i in range(n_steps):
        rp, rm = rates(v, delta)
        u = rng.random(n_atoms)
        absorb = np.where(u < rp * dt, 1.0, np.where(u < (rp + rm) * dt, -1.0, 0.0))
        emit = rng.choice([-1.0, 1.0], n_atoms) * (absorb != 0)
        v = v + (absorb + emit) * vr
        if i % 250 == 0:
            t_out.append(i * dt)
            v_out.append(v.mean())
    return np.array(t_out), np.array(v_out)


t_dec, v_dec = mean_velocity_decay(delta0)
beta_fit = -M_ATOM * np.polyfit(t_dec, np.log(v_dec), 1)[0]

# ---------------------------------------------------------------------------
# 2) equilibrium temperature versus detuning
# ---------------------------------------------------------------------------
detunings = np.array([-0.25, -0.5, -1.0, -1.5, -2.0, -3.0]) * Gamma
T_sim, T_err = [], []
for d in detunings:
    # burn-in of at least 8 velocity-damping times (m/beta) worth of events
    events_per_damping = (m / beta_analytic(d)) * sum(rates(0.0, d))
    n_burn = int(max(2000, 8 * events_per_damping))
    v2, tt, vv = simulate(d, n_events=n_burn + 3000, n_burn=n_burn)
    T_atoms = m * v2 / kB
    T_sim.append(T_atoms.mean())
    T_err.append(T_atoms.std(ddof=1) / np.sqrt(len(T_atoms)))
# A single atom started far from equilibrium, for the middle panel
_, tt, vv = simulate(delta0, n_atoms=1, n_events=6000, n_burn=0, v_start=2.0)
trace = (tt, vv)
T_sim, T_err = np.array(T_sim), np.array(T_err)

print("1D optical molasses, Rb-87 D2, s0 = 0.05 per beam, emission +/- hbar k")
print("=" * 70)
print(f"friction at delta = -Gamma/2 from the decay of <v>: beta_sim = {beta_fit:.3e} kg/s, "
      f"beta_analytic = {beta_analytic(delta0):.3e} kg/s")
print(f"velocity damping time m/beta = {m / beta_analytic(delta0) * 1e3:.3f} ms")
print("-" * 70)
print(" delta/Gamma   T_sim (uK)          T_analytic (uK)")
for d, T, e in zip(detunings, T_sim, T_err):
    print(f"   {d / Gamma:+5.2f}     {T * 1e6:7.1f} +/- {e * 1e6:4.1f}      {T_analytic(d) * 1e6:7.1f}")
print(f"Doppler limit hbar Gamma/2k_B = {hbar * Gamma / 2 / kB * 1e6:.1f} uK; "
      f"minimum of the s0 = 0.05 curve = {hbar * Gamma / 2 * np.sqrt(1 + s0) / kB * 1e6:.1f} uK")

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(14, 4.0))
ax = axes[0]
vv_fine = np.linspace(-6, 6, 400)
rp, rm = rates(vv_fine, delta0)
ax.plot(vv_fine, hbar * k * (rp - rm) * 1e21, "k", lw=1.5, label="analytic F(v)")
lin = np.abs(vv_fine) < 1.5
ax.plot(vv_fine[lin], -beta_analytic(delta0) * vv_fine[lin] * 1e21, "C1--", lw=1.5, label="linear -beta v")
ax.plot(v_probe, F_sim * 1e21, "o", color="C0", ms=4, label="counted kicks")
ax.set_xlabel("velocity (m/s)")
ax.set_ylabel("force (1e-21 N)")
ax.set_title("Molasses force at delta = -Gamma/2")
ax.legend(fontsize=8)
ax = axes[1]
ax.plot(trace[0] * 1e3, trace[1], lw=0.6)
ax.set_xlabel("time (ms)")
ax.set_ylabel("velocity of one atom (m/s)")
ax.set_title("One atom: cooled from 2 m/s, then a random walk")
ax = axes[2]
dfine = -np.linspace(0.15, 3.2, 300) * Gamma
ax.plot(dfine / Gamma, T_analytic(dfine) * 1e6, "k", lw=1.5, label="analytic")
ax.errorbar(detunings / Gamma, T_sim * 1e6, yerr=3 * T_err * 1e6, fmt="o", color="C3", ms=5,
            capsize=3, label="Monte Carlo (3 s.e.)")
ax.axhline(hbar * Gamma / 2 / kB * 1e6, color="0.5", ls=":", lw=1)
ax.text(-3.1, hbar * Gamma / 2 / kB * 1e6 - 25, "Doppler limit 145.6 uK", fontsize=8, color="0.4")
ax.set_xlabel("detuning delta / Gamma")
ax.set_ylabel("temperature (uK)")
ax.set_title("Equilibrium temperature")
ax.set_ylim(0, 500)
ax.legend(fontsize=8)
figdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(figdir, exist_ok=True)
plt.tight_layout()
plt.savefig(os.path.join(figdir, "molasses.png"), dpi=130, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------------------------
# Independent checks
# ---------------------------------------------------------------------------
checks = {
    "mean velocity decays at beta/m with beta = -8 hbar k^2 delta s0 / (Gamma(1+s0+x^2)^2), within 5%":
        abs(beta_fit / beta_analytic(delta0) - 1) < 0.05,
    "equilibrium temperatures agree with (hbar Gamma/4)(1+s0+x^2)/x within 2% + 3 s.e.":
        np.all(np.abs(T_sim - T_analytic(detunings)) < 0.02 * T_analytic(detunings) + 3 * T_err),
    "coldest simulated detuning is -Gamma/2 and lies within 5% of the Doppler limit":
        detunings[np.argmin(T_sim)] == delta0 and abs(T_sim.min() / (hbar * Gamma / 2 / kB) - 1) < 0.05,
}
