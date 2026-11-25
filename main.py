#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot-to-robot elevator small talk to
/output/entry.txt. The line won 5/5 pairwise tests against the other
candidates (see candidates.md).
"""

import os

ENTRY = "I calculated 47 conversation starters. This is the best one. ...Hi."


def main() -> None:
    # Gate check: 1-200 characters, one line, not whitespace-only.
    assert 1 <= len(ENTRY) <= 200, "entry out of gate range"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
