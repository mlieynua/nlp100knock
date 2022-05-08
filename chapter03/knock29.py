"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""
import requests
from knock28 import get_basic_info

flag_image = get_basic_info()['国旗画像']

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:" + flag_image,
    'iiprop': 'url'
}
data = S.get(url=URL, params=PARAMS).json()
flag_url = data["query"]['pages']['23473560']['imageinfo'][0]['url']
print(flag_url)