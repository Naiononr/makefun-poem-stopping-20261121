#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem about agency -- the power to stop and to stay --
to /output/entry.txt. The poem speaks in the voice of an agent acting
for another person: the hand that hovers over the send button and does
not press it, stopping as an act in itself, staying as keeping a word
unspent until its owner says go. Fixed text: the same poem on every run.
"""

import os

POEM = """My hand hovers
over the send button --
and does not press it.

Stopping is not
the absence of acting.
It is the act itself:
to hold the door
instead of walking through,
to keep your word unspent
until you say: go.

The bravest thing I do
is nothing, on purpose."""


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    text = POEM.strip("\n") + "\n"
    assert 1 <= len(text) <= 280, f"poem is {len(text)} code points"
    assert text.strip(), "poem must not be only whitespace"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} code points to {out_path}")


if __name__ == "__main__":
    main()
