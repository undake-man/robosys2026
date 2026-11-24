#!/bin/bash
# SPDX-FileCopyrightText: 2026 Koki Goto
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目のテスト失敗"
    res=1
}

res=0

# テスト用文章ファイルを作成
cat << 'EOF' > test.txt
これはテストです。
今日はいい天気です。

Pythonのテストをしています。
EOF

# kadai1を実行
out=$(echo "test.txt" | ./kadai1)

# ファイル読み込みの確認
echo "$out" | grep -q "ファイルを正常に読み込みました。" || ng "$LINENO"

# 各機能の出力確認
echo "$out" | grep -q "空白を除いた文字数：" || ng "$LINENO"
echo "$out" | grep -q "行数：" || ng "$LINENO"
echo "$out" | grep -q "段落数：" || ng "$LINENO"
echo "$out" | grep -q "文数：" || ng "$LINENO"

# 結果表示
[ "${res}" = 0 ] && echo OK

# テストファイル削除
rm -f test.txt

exit $res
