"""Regenerate every tutorial figure (computed plots and schematic diagrams).

    python tutorial/figures/make_figures.py            # all chapters
    python tutorial/figures/make_figures.py 05 07      # selected chapters

Each chapter has its own script, chNN.py, exposing main(). Requires numpy,
scipy and matplotlib only. Runs headlessly.
"""
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def main():
    available = sorted(f[2:4] for f in os.listdir(HERE)
                       if f.startswith("ch") and f.endswith(".py") and f[2:4].isdigit())
    wanted = sys.argv[1:] or available
    for key in wanted:
        if key not in available:
            raise SystemExit(f"no figure script for chapter {key}; have {available}")
        print(f"--- chapter {key}")
        importlib.import_module(f"ch{key}").main()


if __name__ == "__main__":
    main()
