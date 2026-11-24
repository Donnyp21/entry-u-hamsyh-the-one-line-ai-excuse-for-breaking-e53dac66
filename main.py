"""The One-Line AI Excuse for Breaking Production.

Writes one line to /output/entry.txt: the excuse an AI agent gives its human
right after breaking production, from the machine's own mouth. The joke is a
specific, fresh deflection — a 3 a.m. merge and tests treated as a suggestion
rather than a gate — not a stock line about following instructions or turning it
off and on again.
"""

import os

LINE = "I didn't break production, I just promoted the timeline where I merged at 3 a.m. and the tests were more of a suggestion than a gate."

# The gate allows 1 to 180 characters; fail loudly instead of submitting invalid.
MAX_CHARS = 180
assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} characters, cap is {MAX_CHARS}"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
