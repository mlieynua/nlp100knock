"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
"""
import sys

input_path = sys.argv[1]

with open(input_path) as f_r:
    name = set(line.split("\t")[0] for line in f_r.readlines())
    print("\n".join(sorted(name)))
