"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""
import re
from knock20 import load_text

text_uk = load_text()
basic_info = {}


def get_basic_info():
    for line in text_uk.split('\n'):
        basic_info_line = re.findall(r'\|(.+)\s=\s*(.+)', line)
        if basic_info_line:
            field_name = basic_info_line[0][0]
            value = basic_info_line[0][1]

            value = re.sub(r"'", "", value)
            # \2：かっこの2つ目のみ残す
            value = re.sub(r'\[\[(.+\||)(.+?)\]\]', r'\2', value)
            value = re.sub(r"\{\{(.+\||)(.+?)\}\}", r"\2", value)
            value = re.sub(r"\[\[(.+?)\}\}", r"\1", value)
            value = re.sub(r"\[.+?\]", "", value)
            value = re.sub(r"<ref\s.+?>", "", value)
            value = re.sub(r"<br />", "", value)
            value = re.sub(r"</ref>", "", value)
            value = re.sub(r"<ref>.+", "", value)
            value = re.sub(r"<ref>.+?</ref>", "", value)
            basic_info[field_name] = value
    return basic_info


if __name__ == "__main__":
    basic_info = get_basic_info()
    print(basic_info)
