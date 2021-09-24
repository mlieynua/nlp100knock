'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''
with open("chapter2/data/popular-names.txt") as f:
    lines = [line.replace("\t", " ") for line in f.readlines()]
with open("chapter2/output/output_py/output11.txt", "w") as f:
    f.write("".join(lines))