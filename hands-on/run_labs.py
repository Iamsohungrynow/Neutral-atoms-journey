"""Run the labs in separate processes and verify their physics checks.

python hands-on/run_labs.py --list
python hands-on/run_labs.py --all --check
python hands-on/run_labs.py 03 09 --check
Without --check, plots open interactively; close each window to continue.

Contract: every lab script leaves a dictionary named `checks` in its module
namespace, mapping a short description to a boolean. Each entry compares a
numerical result with an independent analytic or statistical expectation.
--check fails a lab if `checks` is missing, has fewer than two entries, or
contains any False value.
"""
import argparse
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent


def labs():
    return {p.parent.name[:2]: p for p in sorted(ROOT.glob("[0-9][0-9]-*/*.py"))}


def verify(values):
    checks = values.get("checks")
    if not isinstance(checks, dict) or len(checks) < 2:
        raise AssertionError("lab must define a `checks` dict with at least two entries")
    failed = [name for name, ok in checks.items() if not bool(ok)]
    for name, ok in checks.items():
        print(f"  [{'ok' if ok else 'FAIL'}] {name}")
    if failed:
        raise AssertionError(f"failed checks: {failed}")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("lab", nargs="*", help="Two-digit lab numbers")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--check", action="store_true", help="Headless execution with physics checks")
    parser.add_argument("--worker", help=argparse.SUPPRESS)
    args = parser.parse_args()
    available = labs()
    if args.worker:
        os.environ["MPLBACKEND"] = "Agg"
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        plt.show = lambda *a, **k: None
        values = runpy.run_path(str(available[args.worker]), run_name="__main__")
        verify(values)
        print("PASS: numerical physics checks")
        return
    if args.list:
        for key, path in available.items():
            print(f"{key}: {path.relative_to(ROOT)}")
        return
    selected = list(available) if args.all else args.lab
    if not selected or any(key not in available for key in selected):
        parser.error("Choose valid lab numbers (see --list) or --all")
    report = []
    for key in selected:
        start = time.monotonic()
        cmd = ([sys.executable, str(Path(__file__).resolve()), "--worker", key] if args.check
               else [sys.executable, str(available[key])])
        print(f"\nRunning {available[key].parent.name}", flush=True)
        try:
            result = subprocess.run(cmd, cwd=ROOT.parent, capture_output=args.check,
                                    text=True, timeout=600 if args.check else None)
            if args.check:
                print(result.stdout, end="")
                if result.returncode and result.stderr:
                    print(result.stderr, file=sys.stderr, end="")
            entry = {"lab": key, "passed": result.returncode == 0,
                     "seconds": round(time.monotonic() - start, 2)}
        except subprocess.TimeoutExpired:
            entry = {"lab": key, "passed": False, "error": "Timed out after 600 seconds"}
        report.append(entry)
    if args.check:
        import importlib.metadata
        versions = {}
        for name in ("numpy", "scipy", "matplotlib", "qutip"):
            try:
                versions[name] = importlib.metadata.version(name)
            except importlib.metadata.PackageNotFoundError:
                versions[name] = None
        (ROOT / "run-report.json").write_text(json.dumps(
            {"python": sys.version, "dependencies": versions, "results": report}, indent=2),
            encoding="utf-8")
    failures = sum(not item["passed"] for item in report)
    print(f"\n{len(report) - failures}/{len(report)} labs passed")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
