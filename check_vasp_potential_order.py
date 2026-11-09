#!/usr/bin/env python3
"""Check that POSCAR element order matches concatenated POTCAR order.

By default, checks each immediate child directory of the current directory.
Pass a parent directory to check its immediate child directories instead.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TITLE_RE = re.compile(r"^\s*TITEL\s*=\s*(.*?)\s*$", re.IGNORECASE)


def read_poscar_elements(path: Path) -> list[str]:
    lines = path.read_text(errors="replace").splitlines()
    if len(lines) < 7:
        raise ValueError("POSCAR is too short to contain element and count lines")

    # VASP 5+ format: line 6 contains symbols, line 7 contains atom counts.
    symbols = lines[5].split()
    counts = lines[6].split()
    if not symbols or not all(re.fullmatch(r"[A-Z][a-z]?", s) for s in symbols):
        raise ValueError(
            "POSCAR appears to use the VASP 4 format (no element symbols); "
            "cannot verify element order from POSCAR alone"
        )
    if len(counts) != len(symbols) or not all(x.isdigit() for x in counts):
        raise ValueError("POSCAR element and count lines are inconsistent")
    return symbols


def read_potcar_elements(path: Path) -> list[str]:
    elements: list[str] = []
    for line in path.read_text(errors="replace").splitlines():
        match = TITLE_RE.match(line)
        if not match:
            continue
        fields = match.group(1).split()
        if len(fields) < 2:
            raise ValueError(f"cannot parse POTCAR title: {line.strip()}")
        # Titles commonly look like "PAW_PBE Fe_pv ...". The suffix names
        # a potential variant, while POSCAR lists the chemical element.
        symbol = fields[1].split("_")[0]
        if not re.fullmatch(r"[A-Z][a-z]?", symbol):
            raise ValueError(f"cannot identify element in POTCAR title: {line.strip()}")
        elements.append(symbol)
    if not elements:
        raise ValueError("no TITEL entries found in POTCAR")
    return elements


def check_directory(directory: Path) -> tuple[str, str]:
    poscar = directory / "POSCAR"
    potcar = directory / "POTCAR"
    if not poscar.is_file() or not potcar.is_file():
        missing = [name for name, path in (("POSCAR", poscar), ("POTCAR", potcar)) if not path.is_file()]
        return "SKIP", f"missing {', '.join(missing)}"

    try:
        poscar_elements = read_poscar_elements(poscar)
        potcar_elements = read_potcar_elements(potcar)
    except (OSError, ValueError) as exc:
        return "ERROR", str(exc)

    if poscar_elements == potcar_elements:
        return "OK", "order matches: " + " ".join(poscar_elements)
    return (
        "MISMATCH",
        f"POSCAR: {' '.join(poscar_elements)} | POTCAR: {' '.join(potcar_elements)}",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "parent",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="parent directory whose immediate child directories are checked (default: current directory)",
    )
    args = parser.parse_args()
    parent = args.parent.expanduser().resolve()
    if not parent.is_dir():
        parser.error(f"not a directory: {parent}")

    children = sorted((p for p in parent.iterdir() if p.is_dir()), key=lambda p: p.name)
    if not children:
        print(f"No child directories found in {parent}")
        return 0

    failures = 0
    for directory in children:
        status, detail = check_directory(directory)
        print(f"{status:8} {directory.name}: {detail}")
        if status in {"MISMATCH", "ERROR"}:
            failures += 1

    print(f"\nChecked {len(children)} child directories; {failures} mismatch/error(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
