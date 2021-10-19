'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
'''
import sys

n = int(sys.argv[1])
with open("chapter2/data/popular-names.txt") as f_r:
    with open("chapter2/output/output_py/output14.txt", "w") as f_w:
        f_w.write("".join(f_r.readline() for i in range(n)))