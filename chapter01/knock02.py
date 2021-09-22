'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''
word1 = "パトカー"
word2 = "タクシー"
ans = ""
for i_char1, i_char2 in zip(word1, word2):
    ans += i_char1
    ans += i_char2
print(ans)