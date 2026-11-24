"""One-Line Office Joke: 24-Hour Sprint (make.fun).

Writes exactly one line -- a single-sentence joke about office life,
at most 200 characters -- to <output_dir>/entry.txt.

Pure standard library (os only). Fully deterministic: the same line,
byte for byte, on every run.
"""

import os

LINE = (
    "We passed Dave's birthday card around the office for so long that "
    "by the time it reached his desk, it was his next birthday."
)

MAX_CHARS = 200


def validate(text):
    """Gate: 1-200 chars, UTF-8, a single line, not only whitespace."""
    if not text or not text.strip():
        raise SystemExit("line must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit("line exceeds %d chars: %d" % (MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise SystemExit("line must not contain a newline")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    text = validate(LINE.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back what was written: the file on disk must be exactly the
    # validated line plus its trailing newline, byte for byte.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != (text + "\n").encode("utf-8"):
        raise SystemExit("entry.txt on disk does not match the validated line")
    print("wrote %s (%d chars)" % (path, len(text)))


if __name__ == "__main__":
    main()
