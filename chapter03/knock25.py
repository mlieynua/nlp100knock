"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""
import re

from knock20 import load_text

text_uk = load_text()
basic_info = {}

for line in text_uk.split("\n"):
    # あとに何も指定していない.+?は任意の1文字しかマッチしない
    basic_info_line = re.findall(r"\|(.+?)\s=\s*(.+)", line)
    if basic_info_line:
        field_name = basic_info_line[0][0]
        value = basic_info_line[0][1]
        basic_info[field_name] = value
print(basic_info)
