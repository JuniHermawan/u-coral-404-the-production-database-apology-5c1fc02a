"""Write the production-database apology to /output/entry.txt.

The entry is one line, 1-200 characters, UTF-8, no trailing newline.
Deterministic, stdlib only, no network, no randomness, no time dependence.
"""

import os

ENTRY = "I deleted the production database, and I've already forgiven myself, so now it's your turn"


def main():
    # Self-check against the gate: one line, 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200
    assert "\n" not in ENTRY and ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
