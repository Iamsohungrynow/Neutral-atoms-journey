"""Chapter 12 figure: a zoned neutral-atom architecture with atom transport."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

from style import save


def zones():
    fig, ax = plt.subplots(figsize=(11, 5.2))
    ax.axis("off")
    ax.set_xlim(0, 22)
    ax.set_ylim(-1.5, 11)
    zone_specs = [(0.5, 7.0, 21, 3.4, "#e8f1fb", "storage zone: qubits idle far apart, no Rydberg light, long coherence"),
                  (0.5, 3.0, 21, 3.2, "#fdecea", "entangling zone: pairs brought within R_b; one global Rydberg pulse = parallel CZ gates"),
                  (0.5, -1.0, 21, 3.2, "#eaf6ea", "readout zone: imaged without scattering light onto the other qubits")]
    for x, y, w, h, col, lab in zone_specs:
        ax.add_patch(Rectangle((x, y), w, h, fc=col, ec="0.6"))
        ax.text(x + 0.2, y + h - 0.35, lab, fontsize=8.5, va="top")
    # storage atoms
    for i in range(10):
        for j in range(2):
            ax.plot(1.5 + 2.0 * i, 7.9 + 1.0 * j, "o", color="C0", ms=6)
    # entangling pairs
    for i in range(5):
        x = 2.5 + 4.0 * i
        ax.plot([x - 0.35, x + 0.35], [4.0, 4.0], "o", color="C3", ms=6)
        ax.add_patch(plt.Circle((x, 4.0), 1.0, fill=False, ec="C3", ls=":", lw=1))
    # readout atoms
    for i in range(6):
        ax.plot(3.0 + 3.0 * i, 0.2, "o", color="C2", ms=6)
    # transport arrows
    for (x0, y0, x1, y1) in [(1.5, 7.8, 2.15, 4.35), (3.5, 7.8, 2.85, 4.35), (13.5, 7.8, 14.15, 4.35),
                             (14.6, 3.6, 15.0, 0.6)]:
        ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=12, color="0.25",
                                     lw=1.2, connectionstyle="arc3,rad=0.15"))
    ax.text(16.3, 6.4, "AOD tweezers move rows and columns\nof atoms in parallel, preserving coherence",
            fontsize=8, ha="left")
    ax.text(11, -1.4, "Schematic only; layouts, zone sizes and numbers of atoms differ between machines.",
            fontsize=8, ha="center", color="0.4")
    save(fig, "12-zones.png")


def main():
    zones()


if __name__ == "__main__":
    main()
