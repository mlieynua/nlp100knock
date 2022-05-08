"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
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

        value_deleted_bold = re.sub(r"'", "", value)
        # \2：かっこの2つ目のみ残す
        value_deleted_bold_and_link = re.sub(
            r"\[\[(.+\||)(.+?)\]\]", r"\2", value_deleted_bold
        )
        basic_info[field_name] = value_deleted_bold_and_link
print(basic_info)
