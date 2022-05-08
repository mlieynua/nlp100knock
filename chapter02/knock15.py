"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
"""
import sys

filename = sys.argv[1]
n = int(sys.argv[2])

with open(filename) as f_r:
    lines = f_r.readlines()
    for line in lines[len(lines) - n :]:
        print(line, end="")
