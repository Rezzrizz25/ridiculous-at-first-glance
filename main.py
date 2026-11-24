#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 characters) pitching a bizarre startup idea
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The pitch: retired grandmothers, hired out to scold teams into hitting
deadlines. Managers pay $200 a session, because nothing motivates like
a stranger's nana's disappointment. Absurd on first glance; on the
second, it is just accountability coaching with a guilt engine.
"""

import os
import sys

PITCH = (
    "We rent out retired grandmothers to scold your team into hitting "
    "deadlines \u2014 managers pay $200 a session, because no deadline "
    "motivates like a stranger's nana's disappointment."
)


def main() -> int:
    # The gate: UTF-8 text, 1 to 200 characters, not only whitespace,
    # exactly one sentence.
    text = PITCH.strip()
    if not text or text.isspace():
        print("error: pitch is blank", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: pitch is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("error: pitch must be exactly one sentence", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        print("error: pitch holds a control character", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
