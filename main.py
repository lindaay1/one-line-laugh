#!/usr/bin/env python3
"""The One-Line Laugh
(u-ronigrv-the-one-line-laugh-7ccca46f).

Writes the approved one-line joke, byte-exact, no trailing newline.

Output contract (kit competition.yaml / RULES.txt): the program writes one
text to /output/entry.txt; the sealed scorer checks it is UTF-8 text of
1-200 characters, not only whitespace. This writer also writes the same
bytes to line.txt beside it.

No dependencies, no network, fully deterministic.
"""

import os

LINE = "I told my phone I needed space. It gave me 128 GB."


def validate(line):
    """Gate: 1-200 characters, not only whitespace, valid UTF-8."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} chars, must be 1-200")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")


def write_line():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    data = LINE.encode("utf-8")
    for name in ("entry.txt", "line.txt"):
        with open(os.path.join(out_dir, name), "wb") as f:
            f.write(data)
    # Validation read-back: what was written must be byte-exact.
    for name in ("entry.txt", "line.txt"):
        with open(os.path.join(out_dir, name), "rb") as f:
            assert f.read() == data, f"{name} does not match LINE"


if __name__ == "__main__":
    write_line()
