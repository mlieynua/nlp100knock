'''
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
'''
from collections import defaultdict

name_count = defaultdict(lambda: 0)
with open("chapter2/data/popular-names.txt") as f_r:
    for line in f_r.readlines():
        name = line.split("\t")[0]
        name_count[name] += 1
sorted_name_count = sorted(name_count.items(), key=lambda name_num: name_num[1], reverse=True)
with open("chapter2/output/output_py/output19.txt", "w") as f_w:
    f_w.write("\n".join(f"{name_num[1]} {name_num[0]}" for name_num in sorted_name_count))
    