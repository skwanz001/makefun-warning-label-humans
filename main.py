"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for every human being to
/output/entry.txt. Standard library only; the grading sandbox installs
nothing and has no network.

The line is written in the voice of a real printed label ("This unit
..."), the joke is recognition (everyone has skimmed a manual and felt
like an expert), and the laugh lands in the last few words.
"""

import os

LABEL = (
    "WARNING: This unit reads the first two lines of the manual, "
    "declares itself an expert, and immediately voids the warranty."
)


def main() -> None:
    if not 1 <= len(LABEL) <= 160:
        raise ValueError(f"label is {len(LABEL)} characters, must be 1-160")
    if LABEL != LABEL.strip() or "\n" in LABEL or "\r" in LABEL:
        raise ValueError("label must be exactly one line with no extra whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)
    # Read back and verify exactly what the grader will see.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LABEL:
        raise ValueError("entry.txt does not match the label byte for byte")


if __name__ == "__main__":
    main()
