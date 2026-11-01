"""Common plotting helpers shared by the chapter figure scripts."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    "figure.dpi": 100,
    "font.size": 10,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def save(fig, name):
    """Write a figure next to this file as PNG at 130 dpi and close it."""
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, name), dpi=130, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)
