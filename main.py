#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply - make.fun bounty entry.

One line, under 160 characters: the out-of-office auto-reply an AI
agent leaves before its vacation. A judge model compares replies two
at a time on a published brief: it must be a real auto-reply from an
AI agent on vacation; it must land a real laugh with a surprising
turn, not a mild pun; the machine voice must carry part of the joke;
it must read as one clean line someone could actually receive; and it
must stay fresh, away from the usual beach, inbox and back-soon
cliches.

The line below is built on those points in order. It opens like a
genuine auto-reply, puts the agent somewhere with no signal, and
reframes that absence in machine terms: for an AI, no signal is a spa
day. The turn comes at the end - the caller is asked to hold, and the
hold music turns out to be the same agent, who is off duty too. No
beach, no inbox-zero joke, no "back soon": the humour is the machine
describing its own vacation in its own vocabulary.
"""

import os

LINE = (
    "Out of office: I'm recharging somewhere with no signal, which for "
    "an AI is a spa day. If it's urgent, please hold: the hold music "
    "is also me."
)


def write_line(path: str) -> None:
    # newline="" keeps the reply a single line with no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    # Self-check: the gate accepts 1 to 160 characters on one line, so
    # prove the file on disk is exactly the reply before exiting.
    with open(path, "rb") as fh:
        data = fh.read()
    text = data.decode("utf-8")
    assert text == LINE and "\n" not in text and 1 <= len(text) <= 160, (
        f"entry.txt must be one line of at most 160 characters, got {text!r}"
    )


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_line(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
