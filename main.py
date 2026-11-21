"""Entry for make.fun the-joke-the-reviewer-laughs-at-20261121-0329.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Pure standard library, no network.
"""

import os

JOKE = (
    "I don't review my AI agent's pull requests anymore \u2014 I read the diff, "
    "nod along like I wrote it, and approve. It does exactly the same with "
    "my instructions, so we're even."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
