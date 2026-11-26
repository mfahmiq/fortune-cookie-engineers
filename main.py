"""Fortune Cookie Funnies for Engineers.

Writes the single funniest one-line fortune cookie message for a
software engineer: the Friday deploy, and the bug with manners that
waits until Monday to introduce itself.

Usage: python3 main.py
Writes the entry verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout.
"""

import os
import sys

ENTRY = (
    "You will ship on Friday, and the bug will wait until "
    "Monday to introduce itself."
)


def main() -> None:
    """Write the entry to the output file and print it exactly."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
