"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""
import re
from knock20 import load_text

text_uk = load_text()
for category_name in re.findall(r"\[\[Category:(.+?)\]\]", text_uk):
    print(category_name)