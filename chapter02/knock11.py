'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''
with open("chapter2/data/popular-names.txt") as f_r:
    lines = f_r.readlines()
with open("chapter2/output/output_py/output11.txt", "w") as f_w:
    f_w.write("".join(line.replace("\t", " ") for line in lines))