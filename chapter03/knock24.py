"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""
import re

from knock20 import load_text

text_uk = load_text()
media_files = re.findall(r"\[\[ファイル:(.+?)\]\]", text_uk)
for text in media_files:
    print(re.sub(r"\|.+", "", text))
