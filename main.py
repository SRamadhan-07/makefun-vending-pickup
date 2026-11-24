#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Entry program: writes the vending machine's pickup line to
/output/entry.txt as a single line of UTF-8 text, with no trailing
newline appended. The contest gate is 1 to 200 characters.
"""

import os
from pathlib import Path

PICKUP_LINE = (
    "Are you exact change? Because I've been waiting all day for "
    "someone who doesn't make me give something back."
)


def main() -> None:
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "entry.txt"
    path.write_text(PICKUP_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
