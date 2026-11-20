#レポートや課題の文章の文字数や行数、段落数などを確認するコマンド
#ライブラリの読み込み
import argparse
import re
import sys
from pathlib import Path
#文章の分析
def analyze_text(text: str) -> dict[str, int]:
    """Analyze the text and return statistics."""

    characters = len(text)

    characters_without_whitespace = sum(not char.isspace() for char in text)

    lines = len(text.splitlines())

    paragraphs = sum(1 for block in re.split(r"(?:\r?\n)[ \t]*(?:\r?\n)+", text)if block.strip())

    sentences = len(re.findall(r"[。！？!?]+|(?<!\d)\.(?=\s|$)", text))

    return {"characters": characters,"characters_without_whitespace": characters_without_whitespace,"lines": lines,"paragraphs": paragraphs,"sentences": sentences,}
#コマンドの入力設定
def build_parser():
    parser = argparse.ArgumentParser(prog="text-counter",description="Count characters, lines, paragraphs, and sentences.")

    parser.add_argument("file",help="Path to the UTF-8 text file")

    parser.add_argument("--target",type=int,default=None,help="Target character count")

    return parser
#入力の確認
def main(argv=None):
    parser = build_parser(),
    args = parser.parse_args(argv)

    if args.target is not None and args.target <= 0:
        print("Error: --target must be a positive integer.",file=sys.stderr)
        return 2
#ファイルの読み込み・エラー処理
    path = Path(args.file)

    try:text = path.read_text(encoding="utf-8")

    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        return 1
    except UnicodeDecodeError:
        print(f"Error: {path} is not a valid UTF-8 text file.",file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Error: cannot read {path}: {exc}", file=sys.stderr)
        return 1
#分析結果の表示
    result = analyze_text(text)

    print("Text Counter")
    print("-------------------------")
    print(f"Characters: {result['characters']}")
    print("Characters (without whitespace): "f"{result['characters_without_whitespace']}")
    print(f"Lines: {result['lines']}")
    print(f"Paragraphs: {result['paragraphs']}")
    print(f"Sentences: {result['sentences']}")
#目標文字数の判定
    if args.target is not None:

        progress = result["characters"] / args.target * 100

        print()
        print(f"Target: {args.target} characters")
        print(f"Progress: {progress:.2f}%")
        if result["characters"] >= args.target:
            print("Status: Target achieved!")
        else:remaining = args.target - result["characters"]
            print(f"Status: {remaining} characters remaining.")

    return 0
