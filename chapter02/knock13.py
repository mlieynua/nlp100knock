'''
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
'''
with open("chapter2/output/output_py/col1.txt") as f_r1:
    vals1 = [val1.strip() for val1 in f_r1.readlines()]
with open("chapter2/output/output_py/col2.txt") as f_r2:
    vals2 = [val2.strip() for val2 in f_r2.readlines()]
with open("chapter2/output/output_py/output13.txt", "w") as f_w:
    f_w.write("\n".join(f"{val1}\t{val2}" for val1, val2 in zip(vals1, vals2)))