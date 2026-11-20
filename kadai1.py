#レポートや課題の文章の文字数（空白を除く）や行数、段落数などを確認するコマンド
import re
# ファイルの読み込み
def read_file():
    filename = input("読み込むファイル名を入力してください：")
    try:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                text = file.read()
        except UnicodeDecodeError:
            with open(filename, "r", encoding="cp932") as file:
                text = file.read()
        print("\nファイルを正常に読み込みました。")
        return text
    except FileNotFoundError:
        print("エラー：指定されたファイルが見つかりません。")
    except PermissionError:
        print("エラー：ファイルを読み込む権限がありません。")
    except UnicodeDecodeError:
        print("エラー：ファイルの文字コードを読み取れません。")
    except OSError as e:
        print(f"エラー：ファイルの読み込みに失敗しました。{e}")
    return None
# 文字数カウント（空白を除く）
def count_characters(text):
    return len(re.sub(r"\s", "", text))
# 行数カウント
def count_lines(text):
    return len(text.splitlines())
# 段落数カウント
def count_paragraphs(text):
    paragraphs = re.split(r"\n\s*\n", text.strip())
    return len([p for p in paragraphs if p.strip()])
# 文数カウント
def count_sentences(text):
    sentences = re.findall(r"[^。！？.!?]+[。！？.!?]", text)
    return len(sentences)
# メイン処理
def main():
    text = read_file()
    if text is None:
        return
    print("\n===== 文章解析結果 =====")
    print("空白を除いた文字数：", count_characters(text))
    print("行数：", count_lines(text))
    print("段落数：", count_paragraphs(text))
    print("文数：", count_sentences(text))
if __name__ == "__main__":
    main()
