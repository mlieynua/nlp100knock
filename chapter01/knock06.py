'''
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
XとYの和集合，積集合，差集合を求めよ．
さらに，"se"というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''
import knock05
sample1 = "paraparaparadise"
sample2 = "paragraph"

X = set(knock05.ngram(sample1, n=2))
Y = set(knock05.ngram(sample2, n=2))

print("和集合", X|Y)
print("積集合", X&Y)
print("差集合", X-Y, Y-X)
print("'se' in X", "se" in X)
print("'se' in Y", "se" in Y)