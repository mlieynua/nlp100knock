"""
20. JSONデータの読み込みPermalink
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""
import pandas as pd


def load_text(title='イギリス'):
    wiki_df = pd.read_json('/home/miyuoba/working_now/nlp100knock/chapter03/jawiki-country.json.gz',
                           lines=True)
    text_uk = wiki_df[wiki_df['title'] == title]['text'].values[0]
    return text_uk


if __name__ == "__main__":
    text_uk = load_text()
    print(text_uk)