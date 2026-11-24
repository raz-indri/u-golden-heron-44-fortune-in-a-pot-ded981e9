"""Fortune in a Pot — a kind, funny fortune for the houseplant on the windowsill.

The joke: the sun itself leans in through the window just to gossip with the
little plant, and the plant's keeper will proudly brag about it to everyone —
a small, warm prediction for one very loved windowsill leaf.
"""

import os
from pathlib import Path

LINE = (
    "The sun will lean through the window to gossip with you, "
    "little leaf — your keeper will brag about you to everyone."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
