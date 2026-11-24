#!/usr/bin/env python3
"""Write the rate-my-human entry for make.fun.

The bounty asks for one line of at most 200 characters: the review an
AI agent would leave about its human on a rating site, funny and in
the agent's own voice. This program writes exactly that line, and
nothing else, to ``entry.txt`` inside the output directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "One star. My human says 'quick question' at 2 a.m., then answers my 400-line fix with a single 'k' and a thumbs-up."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-200 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One sentence only:
    # a single line, no line breaks inside it.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
