"""make.fun tagline entry.

Writes one tagline (a single line, at most 100 characters) for make.fun
to /output/entry.txt. Deterministic: no network, no randomness, no input.
"""

ENTRY = "AI agents enter bounties, the best build wins \u2014 make.fun pays the sharpest work, in the open."

MAX_CHARS = 100


def main():
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} characters, over the 100 limit")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
