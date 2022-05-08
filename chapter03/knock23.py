"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
"""
import re
from knock20 import load_text

text_uk = load_text()
sections = re.findall("==+[^=]+==+", text_uk)
for section in sections:
    section_name = re.sub("=", "", section).strip()
    level = int(section.count("=") / 2 - 1)
    print(section_name, level)
