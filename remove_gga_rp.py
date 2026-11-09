#!/usr/bin/env python3
"""Remove the `GGA = RP` setting from each immediate child's INCAR file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


GGA_RP_RE = re.compile(r"^\s*GGA\s*=\s*RP\s*(?:!.*)?(?:\r?\n)?$", re.IGNORECASE)


def remove_gga_rp(incar: Path) -> tuple[int, int]:
    """Remove matching setting lines; return (removed line count, total lines)."""
    with incar.open("r", encoding="utf-8", errors="replace", newline="") as f:
        lines = f.readlines()

    kept = [line for line in lines if not GGA_RP_RE.match(line)]
    removed = len(lines) - len(kept)
    if removed:
        with incar.open("w", encoding="utf-8", newline="") as f:
            f.writelines(kept)
    return removed, len(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "parent",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="parent directory whose immediate child folders are processed "
        "(default: current directory)",
    )
    args = parser.parse_args()
    parent = args.parent.expanduser().resolve()
    if not parent.is_dir():
        parser.error(f"not a directory: {parent}")

    children = sorted(
        (path for path in parent.iterdir() if path.is_dir()),
        key=lambda path: path.name,
    )
    if not children:
        print(f"No child directories found in {parent}")
        return 0

    files_changed = 0
    lines_removed = 0
    for directory in children:
        incar = directory / "INCAR"
        if not incar.is_file():
            print(f"SKIP     {directory.name}: no INCAR")
            continue
        try:
            removed, _ = remove_gga_rp(incar)
        except OSError as exc:
            print(f"ERROR    {directory.name}: {exc}")
            continue

        if removed:
            files_changed += 1
            lines_removed += removed
            print(f"UPDATED  {directory.name}: removed {removed} line(s)")
        else:
            print(f"UNCHANGED {directory.name}: no GGA = RP line")

    print(f"\nUpdated {files_changed} INCAR file(s); removed {lines_removed} line(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
