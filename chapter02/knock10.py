'''
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''
import sys

filename = sys.argv[1]
with open(filename) as f:
    raw_count = len(f.readlines())
print(raw_count)