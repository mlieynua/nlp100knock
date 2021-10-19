'''
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
'''
import sys

n = int(sys.argv[1])
with open("chapter2/data/popular-names.txt") as f_r:
    lines = f_r.readlines()
with open("chapter2/output/output_py/output15.txt", "w") as f_w:
    f_w.write("".join(lines[-i] for i in range(n, 0, -1)))