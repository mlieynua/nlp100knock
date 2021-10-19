'''
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
'''
with open("chapter2/data/popular-names.txt") as f_r:
    lines = f_r.readlines()
    lines = sorted(lines, key=lambda line: float(line.split("\t")[2]), reverse=True)
with open("chapter2/output/output_py/output18.txt", "w") as f_w:
    f_w.write("".join(lines))