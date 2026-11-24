"""One-Line Laugh entry: writes a single funny one-liner to /output/entry.txt.

Deterministic: the same line is written on every run. No network access,
no reading of other files, no randomness, no time dependence.
"""

import os

ONE_LINER = (
    "I finally organized my passwords, and now I can't get into "
    "anything \u2014 including the app that stores them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ONE_LINER + "\n")


if __name__ == "__main__":
    main()
