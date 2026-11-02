# Hands-On Track

Each lab is a short, self-contained NumPy/SciPy script (QuTiP for lab 01) that simulates the equations of one tutorial chapter on a laptop. It plots the result, lets you change the parameters, and checks itself against an independent analytic or statistical result. You need nothing beyond Python and the packages below.

## Setup (from the repository root)

Use Python 3.12 or newer. Create an isolated environment once:

```bash
python -m venv .venv
```

Activate it on macOS/Linux with `source .venv/bin/activate`, or on Windows
PowerShell with `.venv\Scripts\Activate.ps1`. Then install and run:

```bash
python -m pip install -r hands-on/requirements.txt
```

```bash
python hands-on/run_labs.py --list
```

```bash
python hands-on/run_labs.py --all --check
```

`--check` runs each lab in a separate process with a non-interactive plotting
backend, saves its figure, verifies its physics checks, and writes an ignored
`hands-on/run-report.json` with the results and installed versions. It exits
with a non-zero status if any check fails. Omit `--check` to open the plots
interactively (close each window to continue), or run any script directly.

**The check contract.** Every lab leaves a dictionary called `checks` that maps
a short description to `True` or `False`. Each entry compares a numerical result
with something computed independently: an analytic formula, a limiting case, or
an exact statistical expectation with its standard error. The runner fails a lab
if any entry is false.

Verified environment: Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1,
Matplotlib 3.11.2, QuTiP 5.3.1 (Linux). The requirements list supported API
bounds, not a claim that every combination has been tested. Only lab 01 uses
QuTiP; the others need NumPy, SciPy and Matplotlib. The ARC Rydberg library
(`pip install arc-alkali-rydberg-calculator`) is optional: no lab or figure
imports it, but it reproduces the Rydberg numbers stored in the code.

Follow the [learning path](../tutorial/learning-path.md) for predictions,
exercises and answers. Read the [notation page](../tutorial/00-notation.md) for
units and sign conventions before changing the code.

## Simulation labs

| Lab | Topic | Theory chapter |
| --- | --- | --- |
| [01-optical-bloch/](01-optical-bloch/) | Damped Rabi oscillations, saturation and power broadening (QuTiP) | [03](../tutorial/03-atom-light.md) |
| [02-zeeman-slower/](02-zeeman-slower/) | Designing a slower; capture velocity and exit velocity | [05](../tutorial/05-doppler-cooling.md) |
| [03-doppler-molasses/](03-doppler-molasses/) | Photon-by-photon molasses; friction and the Doppler limit | [05](../tutorial/05-doppler-cooling.md) |
| [04-mot/](04-mot/) | 1D MOT force, damped oscillation and capture | [06](../tutorial/06-sub-doppler-mot.md) |
| [05-tweezer-trap/](05-tweezer-trap/) | Polarizability, depth, trap frequencies and scattering | [07](../tutorial/07-optical-tweezers.md) |
| [06-release-recapture/](06-release-recapture/) | Single-atom thermometry by release and recapture | [07](../tutorial/07-optical-tweezers.md) |
| [07-rearrangement/](07-rearrangement/) | Collisional-blockade loading and atom-by-atom assembly | [08](../tutorial/08-arrays.md) |
| [08-imaging-fidelity/](08-imaging-fidelity/) | Photon-count histograms, threshold and fidelity | [08](../tutorial/08-arrays.md) |
| [09-ramsey-dephasing/](09-ramsey-dephasing/) | Thermal dephasing from differential light shifts; spin echo | [09](../tutorial/09-qubits-coherence.md) |
| [10-rydberg-blockade/](10-rydberg-blockade/) | Blockade, collective $\sqrt N$ enhancement, Rydberg scaling | [10](../tutorial/10-rydberg.md) |
| [11-cz-gate/](11-cz-gate/) | Levine and Jaksch CZ gates; decay, Doppler and blockade errors | [11](../tutorial/11-rydberg-gates.md) |
| [12-erasure-code/](12-erasure-code/) | Repetition code with erasures versus Pauli errors | [12](../tutorial/12-architectures.md) |
| [13-adiabatic-z2/](13-adiabatic-z2/) | Analog simulation: adiabatic preparation of a $Z_2$ Rydberg crystal | [10](../tutorial/10-rydberg.md) |

## Regenerate the tutorial figures

```bash
python tutorial/figures/make_figures.py
```

Pass chapter numbers, for example `python tutorial/figures/make_figures.py 05 07`,
to redraw only those chapters. Lab figures are regenerated whenever the lab
runs. All figures are teaching models, not measured data.

## See also

- [Repository overview](../README.md)
- [Tutorial chapters](../tutorial/README.md)
