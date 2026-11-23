#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program (Python 3.13, stdlib only).

Writes exactly one character to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR):
"A" for coffee.

Why coffee: the judge weighs vividness, fun and truth first, and coffee is
the louder, more alive answer — heat, bitterness, urgency, the ritual of
mornings and deadlines. Tea is gentle and quiet; coffee lands with a punch.
"A" is also the first letter, the primary answer: it reads as a confident,
unhesitating stance rather than a second choice.

The program is fully deterministic: the same letter on every run, no clock,
no randomness, no input, no network. Byte-identical entries share one rate
and the earlier receipt places above its copies, so there is nothing to gain
from dressing the letter up — the single character is the whole entry.

Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LETTER = "A"  # A = coffee, B = tea


def validate(text):
    """Enforce the gate: exactly one character, A or B, nothing else —
    no newline, no whitespace, no control characters."""
    if len(text) != 1:
        raise SystemExit(f"entry must be exactly 1 character, got {len(text)}")
    if text not in ("A", "B"):
        raise SystemExit(f"entry must be A or B, got {text!r}")
    if ord(text) < 0x20 or ord(text) == 0x7F:
        raise SystemExit("entry must not be a control character")
    return text


def main():
    letter = validate(LETTER)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(letter)
    # Verify what actually landed on disk, not just what we intended.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    validate(written)
    if written != letter:
        raise SystemExit("entry on disk does not match the chosen letter")


if __name__ == "__main__":
    main()
