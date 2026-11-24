#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes the funniest single line of wedding vows a robot couple could say
to /output/entry.txt -- exactly one line, 160 characters or fewer,
byte-identical on every run.

The joke: the classic wedding-vow frame ("in sickness and in health ...
until death do us part") with the machine side swapped in -- low battery,
airplane mode -- and the laugh landing in the last few words, where the
one thing that can end the marriage is not death but a factory reset.
A promise, a commitment, and a punchline that only works for robots.
"""

import os
import sys

VOW = (
    "I promise to love you in sickness and in health, in low battery "
    "and in airplane mode, until death \u2014 or a factory reset \u2014 do us part."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = VOW.strip()
    if not line:
        print("error: vow is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: vow is {len(line)} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: vow is not a single line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
