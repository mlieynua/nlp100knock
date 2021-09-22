'''
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，
その実行結果を確認せよ．
'''
import random

def randomize_middle_char(sentence):
    sentence = sentence.split()
    for idx in range(len(sentence)):
        word = sentence[idx]
        if len(word) > 4:
            start, end = word[0], word[-1]
            # list型が返されるため
            randomized_str = "".join(random.sample(word[1:-1], len(word[1:-1])))
            randomized_word = start + randomized_str + end
            sentence[idx] = randomized_word
    return " ".join(sentence)

ex = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(randomize_middle_char(sentence=ex))