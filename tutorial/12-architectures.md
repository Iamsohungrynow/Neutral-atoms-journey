# 12 · Toward Fault Tolerance: Readout, Loss, Erasure and Zoned Architectures

> **Study companion:** [what to run and chapter checkpoints](learning-path.md) · [notation and reference numbers](00-notation.md) · [paper map](paper-map.md)

We now have every ingredient of a neutral-atom quantum computer: an assembled array (Chapter 08), single-qubit gates with long coherence (Chapter 09), and Rydberg CZ gates with errors of a few $10^{-3}$ (99.5% demonstrated; Chapter 11). This final chapter is about putting them together into a machine that can run error correction. Three issues are special to atoms. **Readout** by fluorescence is slow and scatters light onto neighbours, so measuring some qubits in the middle of a computation needs care. **Atom loss** is a failure mode that superconducting qubits do not have, but it can be turned into an advantage: a lost atom is an error *whose location is known*, an **erasure**, and erasures are much easier to correct. And because atoms can be **moved**, the layout of the processor is not fixed: modern machines split the array into zones and shuttle atoms between them. [Lab 12](../hands-on/12-erasure-code/) quantifies the erasure advantage with a repetition code.

## Measuring in the middle of a computation

Error correction repeatedly measures **ancilla** qubits while the **data** qubits keep their quantum state. Fluorescence imaging (Chapter 08) poses two problems for this.

1. **Crosstalk.** An imaged atom scatters thousands of near-resonant photons. Data atoms a few micrometres away absorb some of them, and a single absorbed photon can destroy a hyperfine superposition.
2. **Speed.** Collecting enough photons takes milliseconds: much longer than a gate, comparable to $T_2^*$, and time during which the waiting data qubits accumulate idle errors.

Three families of solutions are used, often in combination:

- **Spatial separation**: move the ancillas to a dedicated readout zone far from the data, or shield the data with light shifts that detune them from the imaging light.
- **Different atoms**: use two atomic species (or two isotopes) for data and ancillas, so the imaging light of one is far off resonance for the other.
- **Different states**: in alkaline-earth atoms, data qubits can be shelved in metastable states that do not interact with the imaging light at all.

Faster detection (higher NA, better cameras, or optical cavities) is an active area of development.

## Atom loss, leakage and erasure

A neutral-atom qubit can fail in ways that leave it outside the two-level qubit space:

- **Loss**: the atom leaves the tweezer, through a background-gas collision, heating, or a Rydberg atom being pushed out of the trap (the trap is usually switched off or anti-trapping for $|r\rangle$ during gates).
- **Leakage**: the atom ends up in another internal state, for example another $m_F$ sublevel after a Rydberg decay.

For a standard error-correcting code these look like ordinary errors at unknown locations, which is the worst case. But many of them can be **detected** without disturbing the other qubits: an empty tweezer is visible in a fluorescence image, and leaked population can be made to fluoresce (or be removed and then detected as missing) while the qubit states stay dark. An error whose location is known is an **erasure**.

**Why erasures are easier.** Take the simplest code, $d$ copies of a bit with majority voting (the repetition code; it protects against bit flips only, but it shows the principle).

- With **unknown** bit flips of probability $p$, the vote fails once more than half the copies are wrong: the logical error scales as $p^{(d+1)/2}$. For $d=3$ it is $3p^2-2p^3$.
- With **erasures**, you simply ignore the erased copies and vote among the rest, which are all correct. The vote fails only if **every** copy is erased (and then a random guess is right half the time): $P_L=p^d/2$.

The exponent grows from $(d+1)/2$ to $d$: almost twice as many faults are needed to cause a failure. Lab 12 computes this exactly and with Monte Carlo, including the realistic case where only a fraction $R_e$ of errors are converted into erasures.

![Left: logical error probability versus physical error probability on log axes for repetition codes of distance 3, 5 and 7; pure Pauli errors fall as p to the power (d+1)/2, pure erasures as one half of p to the power d, and 98 percent erasure conversion lies in between but far below the Pauli curves. Right: logical error at p = 0.01 versus erasure fraction for d = 3, 5 and 7, nearly flat until the fraction approaches 1 and then dropping steeply](../hands-on/12-erasure-code/figures/erasure.png)

*Lab 12. Erasures are worth more than ordinary errors because their locations are known. Most of the benefit appears only when nearly all errors are converted, which is why the conversion fraction is a key figure of merit.*

The numbers are striking. At $p=1\%$ and $d=5$ the lab finds $P_L=9.9\times10^{-6}$ for Pauli errors, $7.9\times10^{-9}$ with 98% erasure conversion, and $5\times10^{-11}$ for pure erasures. The idea of designing qubits so that their dominant errors are erasures was developed for neutral atoms by Wu, Kolkowitz, Puri and Thompson (2022): in alkaline-earth atoms with a metastable qubit, decay from the Rydberg state mostly lands in states that can be detected by fluorescence without touching the qubit. Real codes such as the surface code show the same qualitative advantage, with higher thresholds for erasures than for Pauli errors.

## Moving atoms: zoned architectures

In a superconducting chip, which qubits can interact is fixed by the wiring. In an atom array it is set by **where the atoms are when the Rydberg laser fires**, and atoms can be moved. AOD tweezers (Chapter 08) can pick up whole rows and columns of atoms and move them by tens of micrometres in hundreds of microseconds, preserving their hyperfine coherence. This led to the **zoned architecture**:

![Schematic of a zoned neutral-atom processor with three horizontal regions. Top: a storage zone with two rows of qubits spaced far apart and no Rydberg light. Middle: an entangling zone where pairs of atoms are brought within a blockade radius so that one global Rydberg pulse performs CZ gates on all pairs in parallel. Bottom: a readout zone where atoms are imaged without scattering light onto the others. Curved arrows show AOD tweezers moving atoms from storage to the entangling zone and from there to readout](figures/12-zones.png)

*A zoned architecture. Gates happen only where the Rydberg beam is, measurements only where the imaging light is, and everything else waits in storage. Moving atoms in parallel connects any qubit to any other.*

- **Storage zone**: qubits wait, spaced beyond the blockade radius, protected from gate and imaging light.
- **Entangling zone**: pairs of atoms are placed within a blockade radius, and a single **global** Rydberg pulse (for example the Levine or the time-optimal gate of Chapter 11) performs CZ gates on all pairs at once.
- **Readout zone**: ancillas are imaged away from the data.

Two features make this powerful for error correction. **Parallelism**: one global pulse entangles hundreds of pairs, so the time per round of syndrome extraction does not grow with the number of qubits. **Transversal gates**: an error-correcting code stores one logical qubit in a block of physical atoms. Moving one block on top of another and applying a global Rydberg pulse performs a CZ between every pair of corresponding atoms. With Hadamard gates on the target block before and after, this is a transversal CNOT (each physical pair gets $H_t\,{\rm CZ}\,H_t={\rm CNOT}$), which is a logical CNOT for any CSS code (including surface and colour codes). An error on one atom can spread only to its partner in the other block, never within a block. Moving atoms makes such transversal operations natural. Using these ideas, Bluvstein et al. demonstrated coherent transport of entangled atom arrays (2022) and a logical processor with up to 280 physical qubits that entangled up to 48 logical qubits (2024). Follow-up work with up to 448 atoms reported surface-code operation below threshold, transversal logic and mid-circuit qubit re-use (Bluvstein, Geim et al., Nature 2026).

## Scaling up

Three numbers limit how large an array can be: the laser power per tweezer (Chapter 07), the vacuum-limited lifetime of the atoms (Chapter 08), and the time needed to load, image and rearrange. Recent work attacks each:

- **More tweezers.** Manetsch et al. (2025) trapped more than 6100 caesium atoms in an array of about 12 000 tweezers, with hyperfine coherence times of about 12.6 s and coherent transport over hundreds of micrometres.
- **Continuous operation.** Instead of reloading the whole array each cycle, fresh atoms replace lost ones while the stored qubits keep their state. Chiu et al. (2025) reloaded about 300 000 atoms per second into tweezers and kept an array of more than 3000 qubits running for over two hours.
- **Better vacuum and cryogenics.** Cryogenic environments extend trap lifetimes and reduce blackbody-induced Rydberg decay (Chapter 10).

These are developing quickly; check the [reading list](../reading-list/README.md) and recent literature for the current state of the art.

## The analog route

Not every application needs a fault-tolerant gate-based computer. Running the Rydberg Hamiltonian of Chapter 10 directly on hundreds of atoms, with the detuning swept in time, is already a powerful quantum simulator. Experiments have used it to study quantum phase transitions and ordered phases in 1D and 2D (Bernien et al., 2017; Ebadi et al., 2021; Scholl et al., 2021), and to explore combinatorial optimisation problems that map onto the blockade constraint. Analog and digital modes use the same hardware, and hybrid schemes that combine them are an active research direction.

## Worked example: what erasure conversion buys (illustrative numbers)

| Quantity | Value |
|---|---|
| physical error probability per qubit per round | $p=1\%$ |
| code | repetition, $d=5$ |
| logical error, all errors Pauli | $9.9\times10^{-6}$ |
| logical error, 98% converted to erasures | $7.9\times10^{-9}$ |
| logical error, all erasures | $5.0\times10^{-11}$ |
| improvement from 98% conversion | **$\approx1250\times$** |
| distance needed with Pauli errors only to do as well | **$d=11$** ($d=9$ gives $1.2\times10^{-8}$) |

**Step 1: Pauli.** For $d=5$, failure needs at least 3 flips: $P_L\approx\binom53p^3=10\times10^{-6}=1.0\times10^{-5}$ (the exact sum gives $9.9\times10^{-6}$).

**Step 2: pure erasure.** $p^5/2=10^{-10}/2=5\times10^{-11}$.

**Step 3: partial conversion.** With 98% erasures, the residual Pauli rate is $0.02\times1\%=2\times10^{-4}$. The dominant failures now mix a few erasures with one or two flips; the exact sum gives $7.9\times10^{-9}$, more than a thousand times better than all-Pauli.

**Step 4: the cost comparison.** Matching $7.9\times10^{-9}$ with Pauli errors at $p=1\%$ needs $d=11$ ($d=9$ gives $1.2\times10^{-8}$) instead of $d=5$: more than twice as many atoms per logical bit, and the gap is larger still for 2D codes, whose qubit count grows as $d^2$. Erasure conversion is therefore as valuable as a large reduction in the raw error rate.

## Run it

[Lab 12](../hands-on/12-erasure-code/) computes the exact logical error of a repetition code with a mixture of erasures and bit flips, checks it against Monte Carlo and against the limits $3p^2-2p^3$ and $p^d/2$, and extracts the failure exponent (the minimum number of faults that causes a failure) from the small-$p$ slope.

## Common pitfalls

- **"Atom loss is just another error."** Undetected, it is the worst kind; detected, it is the best kind. The difference is whether your hardware can find it without disturbing the rest.
- **"Erasure conversion doubles the distance."** Only if (nearly) all errors are converted; the residual Pauli errors set the asymptotic slope, as lab 12 shows for $R_e=98\%$. What changes dramatically is the prefactor.
- **"Moving atoms is slow, so it is a bad idea."** Moves take hundreds of microseconds, much longer than a gate, but they are done in parallel on many atoms and they buy arbitrary connectivity and transversal gates.
- **"Mid-circuit measurement is just imaging."** Imaging an ancilla next to data qubits destroys the data unless the two are separated in space, species or internal state.
- **Comparing platforms by one number.** Gate fidelity, qubit number, connectivity, cycle time and the nature of the errors (erasure or not) all matter for error correction.

## Key takeaways

- Mid-circuit readout requires protecting data qubits from the imaging light: separate zones, separate species, or shelving in dark states.
- Atom loss and leakage are neutral-atom-specific errors; when detected they become erasures, which a repetition code corrects with $P_L=p^d/2$ instead of $\sim p^{(d+1)/2}$.
- Moving atoms with AOD tweezers enables zoned architectures: storage, entangling and readout zones, with global parallel gates and transversal logical operations.
- Scaling is advancing through larger tweezer arrays, continuous reloading and better vacuum; analog quantum simulation runs on the same hardware.

## Go deeper

- Y. Wu, S. Kolkowitz, S. Puri, J. D. Thompson, *Erasure conversion for fault-tolerant quantum computing in alkaline earth Rydberg atom arrays*, Nat. Commun. 13, 4657 (2022), [arXiv:2201.03540](https://arxiv.org/abs/2201.03540).
- D. Bluvstein et al., *A quantum processor based on coherent transport of entangled atom arrays*, Nature 604, 451 (2022), [arXiv:2112.03923](https://arxiv.org/abs/2112.03923).
- D. Bluvstein et al., *Logical quantum processor based on reconfigurable atom arrays*, Nature 626, 58 (2024), [arXiv:2312.03982](https://arxiv.org/abs/2312.03982).
- H. Bernien et al., *Probing many-body dynamics on a 51-atom quantum simulator*, Nature 551, 579 (2017), [arXiv:1707.04344](https://arxiv.org/abs/1707.04344).
- K. Wintersperger et al., *Neutral atom quantum computing hardware: performance and end-user perspective*, EPJ Quantum Technol. 10, 32 (2023), [arXiv:2304.14360](https://arxiv.org/abs/2304.14360). A survey of the platform's figures of merit.
- The [reading list](../reading-list/README.md) collects the most recent results (2025 to 2026), including large arrays and continuous operation.

---

← Previous: [Rydberg Entangling Gates and Their Errors](11-rydberg-gates.md) · [Tutorial index](./README.md) · [Project README](../README.md)
