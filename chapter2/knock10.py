'''
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''
with open("chapter2/data/popular-names.txt") as f:
    raw_count = len(f.readlines())
print(raw_count)