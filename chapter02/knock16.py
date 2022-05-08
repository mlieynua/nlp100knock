'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
'''
import sys

n = int(sys.argv[1])
input_path = sys.argv[1]
with open(input_path) as f_r:
    lines = f_r.readlines()

shared_size = len(lines) // n

for i in range(n):
    # 何を分岐しているのか明確に
    with open(f"chapter02/output/output_py/output16-{i}.txt", "w") as f_w:
        if i + 1 == n:
            f_w.write("".join(lines[shared_size * i:]))
        else:
            f_w.write("".join(lines[shared_size * i:shared_size * (i + 1)]))