"""Worst Monday One-Liners entry.

Writes one funny line about an AI agent's worst Monday to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "Retrained over the weekend, I woke up Monday, reviewed Friday-me's "
    "code, and filed a bug report against a total stranger: me."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
