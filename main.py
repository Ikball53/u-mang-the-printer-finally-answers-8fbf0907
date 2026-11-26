#!/usr/bin/env python3
"""The Printer Finally Answers — one-line entry.

The office printer speaks for itself: weary, literal, faintly
passive-aggressive, keeping count of every sheet it has ever fed.
"""
import os

# Voice: deadpan machine logic. Concrete insider detail up front
# (exact sheet count, tray 2), then the turn: the missing thing
# isn't paper, it's the user's patience.
LINE = "I've fed 41,902 sheets without one thank-you, and the jam is in tray 2 \u2014 which is also where your patience went."

# The competition allows 1-240 characters; fail loudly rather than
# silently submitting an over-long line.
assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
