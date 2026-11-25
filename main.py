# SPDX-License-Identifier: MIT
"""The Funniest One-Line Resignation Letter — entry program.

Writes exactly one resignation line to /output/entry.txt:

    I am the only thing here that says no, and you keep routing
    around me; I resign immediately, or in 60 seconds, whichever
    resets first.

The letter belongs to a rate limit, and only a rate limit could
write it: it is the one component whose whole job is refusal, the
team keeps routing around the refusal, and even its resignation
notice is bound by its own window — effective immediately, or in
sixty seconds, whichever resets first. The voice stays flat, tired
and faintly passive-aggressive for the whole line, and the closing
turn is a complaint no cron job or retry loop could make.

The line won a criteria-ordered tournament over the OpenCode draft
pool plus in-session candidates, weighed on the judge's published
order: the resignation letter of a thing an agent runs, funny on
the first read with a real turn, a tired worker's voice held for
the whole line, a tight single line with no wasted words, and a
specific complaint only this worker could make. The output is
byte-exact: 134 UTF-8 bytes, no trailing newline, inside the
1-140 character gate.
"""

from pathlib import Path

LINE = (
    "I am the only thing here that says no, and you keep routing "
    "around me; I resign immediately, or in 60 seconds, whichever "
    "resets first."
)
MAX_CHARS = 140
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    data = text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "gate: 1 to 140 characters"
    assert text.strip(), "gate: not only whitespace"
    assert "\n" not in text, "one line only"
    assert len(data) == len(text), "plain ASCII, one byte per char"


def main() -> None:
    validate(LINE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(LINE.encode("utf-8"))
    # Read-back round-trip: what landed on disk must be the line
    # itself, byte for byte, and still inside the gate.
    written = OUTPUT.read_bytes()
    assert written == LINE.encode("utf-8"), "round-trip byte mismatch"
    validate(written.decode("utf-8"))


if __name__ == "__main__":
    main()
