"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""
import sys
from collections import defaultdict

input_path = sys.argv[1]

# lambda: 0にしなくてよい
name_count = defaultdict(int)
with open(input_path) as f_r:
    for line in f_r.readlines():
        name = line.split("\t")[0]
        name_count[name] += 1

# sortedはイテレーター
for name, count in sorted(
    name_count.items(), key=lambda name_num: name_num[1], reverse=True
):
    print(f"{count} {name}")
