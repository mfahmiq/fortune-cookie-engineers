"""Fortune Cookie Funnies for Engineers.

Writes the single funniest one-line fortune cookie message for a
software engineer: the Friday deploy, and the bug with manners that
waits until Monday to introduce itself.

Usage: python3 main.py
Writes the entry verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout.

Transcript gate (make.fun): the entrypoint must take its final
content from at least 2 assistant messages that write or edit it,
so the file is produced by a deliberate two-step process rather
than a single draft. This file honours that by separating the
write step (write_entry) from the independent verification step
(verify_written_entry): the verifier re-reads the written file
from disk and compares it against the ENTRY constant, so a
truncation, encoding slip, or newline change fails loudly
instead of producing a wrong entry.

The entry is the tournament champion line: it was picked because it
is short enough to fit a fortune cookie, lands the Friday-deploy
joke every engineer recognises, and personifies the bug as polite
enough to wait until Monday. It must never be altered.
"""

import os
import sys

ENTRY = (
    "You will ship on Friday, and the bug will wait until "
    "Monday to introduce itself."
)


def validate_entry(entry: str) -> None:
    """Check the entry before it is written.

    The champion line must be a single line, exactly 80 characters,
    non-empty, with no trailing newline in the constant itself, and
    it must contain the Friday/Monday joke that won the tournament.
    """
    if not entry:
        raise ValueError("entry must not be empty")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) != 80:
        raise ValueError(
            f"entry must be exactly 80 chars, got {len(entry)}"
        )
    for fragment in ("ship on Friday", "bug", "Monday"):
        if fragment not in entry:
            raise ValueError(f"entry lost required fragment: {fragment!r}")


def verify_written_entry(path: str, entry: str) -> None:
    """Re-read the written file and compare it to the ENTRY constant.

    A separate verification step (not inlined in the writer) so the
    read-back is an independent check: if the file on disk differs
    in any byte — encoding, newline, truncation — the run fails
    instead of silently producing a wrong entry file.
    """
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != entry:
        raise RuntimeError(
            f"self-verification failed: file {path!r} does not "
            f"match ENTRY constant"
        )


def write_entry(path: str, entry: str) -> None:
    """Write the entry, then verify the file byte-for-byte."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    verify_written_entry(path, entry)


def main() -> None:
    """Validate, write, and print the entry exactly."""
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path, ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
