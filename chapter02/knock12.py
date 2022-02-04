'''
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
'''
import sys

input_path = sys.argv[1]
output_col1_path = sys.argv[2]
output_col2_path = sys.argv[3]

with open(input_path) as f:
    lines = f.readlines()
    vals1 = [line.split()[0] for line in lines]
    vals2 = [line.split()[1] for line in lines]
with open(output_col1_path, "w") as f:
    f.write("\n".join(vals1))
with open(output_col2_path, "w") as f:
    f.write("\n".join(vals2))