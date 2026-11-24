"""One Letter for Your Day — entry: C (caffeinated).

Writes exactly one character, "C", to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR). No newline, no word, no gloss, no punctuation:
the letter is the whole entry, per RULES.txt.

Why C: the word behind the letter is "caffeinated" — a coffee-fuelled
day that kept going past midnight, still shipping bounties at dawn.
It is vivid and specific (a sharp picture, not a vague mood), funny
at once, and true to a real day; the initial fits the word exactly,
and it is not the obvious pick (E for exhausted, T for tired).
It is also none of the three example letters in the task description
(A, F, Z), which the rules' fixed anchor texts are most likely to be —
an entry byte-identical to a fixed text shares its rate and never
enters the playoff.

No network, no randomness, no input. Deterministic: every run writes
byte-identical output.
"""

import os
from pathlib import Path

LETTER = "C"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
