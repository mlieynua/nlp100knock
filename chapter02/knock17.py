'''
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
'''
with open("chapter2/data/popular-names.txt") as f_r:
    name = set(line.split("\t")[0] for line in f_r.readlines())
with open("chapter2/output/output_py/output17.txt", "w") as f_w:
    f_w.write("\n".join(sorted(name)))