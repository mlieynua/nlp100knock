'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
'''
import sys 

n = int(sys.argv[1])
with open("chapter2/data/popular-names.txt") as f_r:
    lines = f_r.readlines()
num_per_division = int(len(lines) / n)
idx_list = list(range(0, len(lines), num_per_division))

for count, (idx_begin, idx_end) in enumerate(zip(idx_list[:-1], idx_list[1:]), start=1):
    print(count)
    if count == n:
        with open(f"chapter2/output/output_py/output16-{count}.txt", "w") as f_w:
            f_w.write("".join(lines[idx_begin:]))
    else:
        with open(f"chapter2/output/output_py/output16-{count}.txt", "w") as f_w:
            f_w.write("".join(lines[idx_begin:idx_end]))