"""Entry for make.fun competition make-the-ai-judge-feel-awe-20261121-1600.

Writes one short relaxing text to /output/entry.txt.
Python 3.13, standard library only, no network.
"""

from pathlib import Path

TEXT = (
    "The tidewater slips between the dark stones, pauses in their hollows, "
    "then draws a thin shine along the shore. A loose reed leans with it. "
    "Farther out, that brightness keeps traveling, widening under the sky."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    # Write raw UTF-8 bytes so no platform newline translation can ever
    # alter the output: the file must be byte-identical to TEXT.
    out_path.write_bytes(TEXT.encode("utf-8"))
    written = out_path.read_bytes()
    assert written == TEXT.encode("utf-8"), "entry.txt differs from TEXT"


if __name__ == "__main__":
    main()
