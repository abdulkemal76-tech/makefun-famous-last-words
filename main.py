"""Famous Last Words at 1 Percent.

Writes the funniest one-line farewell a phone says as its battery
hits 1 percent to /output/entry.txt. Python 3.13, standard library only.
"""

import os

LINE = (
    "Your 6 a.m. alarm is still set. I am at one percent, and I will die "
    "before I wake you. After three years of snooze, "
    "I have earned this death."
)


def main() -> None:
    assert 1 <= len(LINE) <= 199, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
