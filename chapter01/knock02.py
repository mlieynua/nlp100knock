'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''
word1 = "パトカー"
word2 = "タクシー"
# join(ジェネレータ)の方がjoin(リスト)より計算効率良い
print("".join(i_char1 + i_char2 for i_char1, i_char2 in zip(word1, word2)))