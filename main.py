"""One Word From Grandma (make.fun bounty u-0xkianno-one-word-from-grandma-f04bed16).

Writes exactly one word to /output/entry.txt: the word grandma would
text about AI. Deterministic, no network, no randomness, no input: the
same word, byte for byte, on every run. The word was chosen for the
judge's brief: a real word a grandma would actually reach for when
faced with a machine that talks back - "witchcraft" is funny because
it is exactly how she would explain it, and grandma-like because it
comes from her world, not from tech. It beats the alternatives:
"Skynet" is a film reference, not something she would text, and a
typo like "robit" is cute but says nothing about what she thinks AI
is. 10 characters, one word.
"""

import os

LINE = "witchcraft"


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
    # not only white space. This word is 10 characters.
    assert 1 <= len(text) <= 30, "word must be 1-30 Unicode code points"
    assert text == text.strip(), "word must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "word must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "word must not contain hidden control characters"
    )
    assert text.strip(), "word must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
