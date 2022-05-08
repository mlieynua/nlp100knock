'''
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
'''
import sys

input_col1_path = sys.argv[1]
input_col2_path = sys.argv[2]
output_path = sys.argv[3]

with open(input_col1_path) as f_r1,\
     open(input_col2_path) as f_r2,\
     open(output_path, "w") as f_w:
    for line1, line2 in zip(f_r1, f_r2):
        f_w.write(line1.strip() + "\t" + line2)