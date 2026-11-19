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

