"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
（参考: マークアップ早見表）．
"""
import re
from knock20 import load_text

text_uk = load_text()
basic_info = {}

for line in text_uk.split("\n"):
    basic_info_line = re.findall(r"\|(.+?)\s=\s*(.+)", line)
    if basic_info_line:
        field_name = basic_info_line[0][0]
        value = basic_info_line[0][1]
        value = re.sub(r"'", "", value)
        basic_info[field_name] = value
print(basic_info)
