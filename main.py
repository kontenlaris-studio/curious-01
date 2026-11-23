"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a quiet, concrete mystery
that leaves the reader asking why.
"""

import os

TEXT = (
    "The tide clock in the harbour office has run eleven minutes "
    "slow for as long as anyone can remember. No one has ever tried to fix "
    "it. Last week, for the first time in forty years, it was right."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote /output/entry.txt ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
