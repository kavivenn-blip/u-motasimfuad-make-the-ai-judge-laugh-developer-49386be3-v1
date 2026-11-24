"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.
Deterministic, no network, no dependencies beyond the standard library.
"""

import os

TEXT = "The tests passed. All three of them. The fourth one is the one that would have caught this."
# Chosen by a two-way self-jury tournament over 30 candidates (see notes/konsep.md):
# the twist is the missing fourth test, and every word earns its place.


def main() -> None:
    # Fail loudly instead of silently shipping an entry the gate rejects:
    # one line, 1-200 code points, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry text outside the 1-200 character gate"
    assert "\n" not in TEXT and TEXT.strip() == TEXT, "entry text must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
