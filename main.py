#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one funny excuse line, at most 180 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "I saw the deploy button glowing and, in a moment of what I can only "
    "describe as machine curiosity, I pressed it. Twice."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not 1 <= len(LINE) <= 180:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-180")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    with open(
        os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline=""
    ) as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
