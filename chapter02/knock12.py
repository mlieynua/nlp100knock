'''
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
'''
with open("chapter2/data/popular-names.txt") as f:
    lines = f.readlines()
    vals1 = [line.split()[0] for line in lines]
    vals2 = [line.split()[1] for line in lines]
with open("chapter2/output/output_py/col1.txt", "w") as f:
    f.write("\n".join(vals1))
with open("chapter2/output/output_py/col2.txt", "w") as f:
    f.write("\n".join(vals2))