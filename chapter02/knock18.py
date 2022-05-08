"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""
import sys

input_path = sys.argv[1]

with open(input_path) as f_r:
    lines = f_r.readlines()
    lines = sorted(lines, key=lambda line: float(line.split("\t")[2]), reverse=True)
    print("".join(lines))
