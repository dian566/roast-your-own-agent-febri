#!/usr/bin/env python3
"""One-line roast of my own AI agent for make.fun."""

# The roast: four confident paragraphs about a bug, then the apology —
# it had been reading the wrong file the whole time.

import os

ROAST = "My agent wrote four confident paragraphs explaining the bug, then apologized: it had been reading the wrong file the whole time."
MAX_LEN = 200  # bounty cap for a one-line roast


def file_roast() -> None:
    """Write the roast to /output/entry.txt, nothing else."""
    if len(ROAST) > MAX_LEN or not ROAST.strip() or "\n" in ROAST:
        raise ValueError("roast must be a single non-empty line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST)


if __name__ == "__main__":  # run it
    file_roast()
