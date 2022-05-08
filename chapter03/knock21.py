"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""
import re
from knock20 import load_text

text_uk = load_text()
for line in text_uk.split('\n'):
    if re.match(r'\[\[Category:.+?\]\]', line):
        print(line)

# ab*：a・ab・aにいくつかのbにマッチ（*直前の文字はあってもなくてもよい、複数個あるなら全てマッチ）
# ab+：ab・aにいくつかのbにマッチ（*直前の文字は1以上は必要, 複数個あるなら全てマッチ）
# ab?：a・abにマッチ（直前  の文字はあってもなくてもよい、複数個あっても1つしかマッチしない）