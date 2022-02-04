'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''
import sys

filename = sys.argv[1]

with open(filename) as f_r:
    print("".join(line.replace("\t", " ") for line in f_r))