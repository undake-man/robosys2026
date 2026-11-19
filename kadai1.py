#レポートや課題の文章の文字数や行数、段落数などを確認するコマンド
import argparse
import re
import sys
from pathlib import Path
def analyze_text(text: str) -> dict[str, int]:
    """Analyze the text and return statistics."""

    characters = len(text)

    characters_without_whitespace = sum(
        not char.isspace() for char in text
    )

    lines = len(text.splitlines())

    paragraphs = sum(
        1 for block in re.split(
            r"(?:\r?\n)[ \t]*(?:\r?\n)+", text
        )
        if block.strip()
    )

    sentences = len(
        re.findall(r"[。！？!?]+|(?<!\d)\.(?=\s|$)", text)
    )

    return {
        "characters": characters,
        "characters_without_whitespace": characters_without_whitespace,
        "lines": lines,
        "paragraphs": paragraphs,
        "sentences": sentences,
    }
def build_parser():
    parser = argparse.ArgumentParser(
        prog="text-counter",
        description="Count characters, lines, paragraphs, and sentences."
    )

    parser.add_argument(
        "file",
        help="Path to the UTF-8 text file"
    )

    parser.add_argument(
        "--target",
        type=int,
        default=None,
        help="Target character count"
    )

    return parser
def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.target is not None and args.target <= 0:
        print(
            "Error: --target must be a positive integer.",
            file=sys.stderr
        )
        return 2
