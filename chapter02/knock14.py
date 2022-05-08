'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
'''
import sys

n = int(sys.argv[1])
for i, line in enumerate(sys.stdin):
    print(line, end="")
    if i == n:
        break

# tail -n20 chapter02/data/popular-names.txt | python chapter02/knock14.py 10
# 使いまわししやすさ