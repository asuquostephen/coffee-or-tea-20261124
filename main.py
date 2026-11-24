#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one character — the letter A — to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The gate allows exactly one
character: A for coffee, B for tea, and nothing else. This entry
answers A: coffee.
Python 3 standard library only. No network.
"""
import os
import sys

LETTER = "A"


def main() -> int:
    data = LETTER.encode("utf-8")
    if len(LETTER) != 1 or LETTER not in ("A", "B"):
        print(f"entry must be exactly one letter, A or B, got {LETTER!r}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
