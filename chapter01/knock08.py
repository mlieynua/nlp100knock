"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(string):
    ans = ""
    for idx, char in enumerate(string):
        if char.islower():
            ans += chr(219 - ord(char))
        else:
            ans += char
    return ans


print(cipher(string="HoGe FugA"))
print(cipher(cipher(string="HoGe FugA")))
