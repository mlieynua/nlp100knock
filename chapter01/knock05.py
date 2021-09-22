'''
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
'''
def create_word_ngram(sequence, n=1):
    ngram = []
    if type(sequence) == str:
        sequence = sequence.split()
    for idx in range(len(sequence)-(n-1)):
        ngram.append(sequence[idx:idx+n])
    return ngram

def create_char_ngram(sequence, n=1):
    ngram = []
    if type(sequence) == str:
        sequence = sequence.replace(" ", "")
    elif type(sequence) == list:
        sequence = "".join(sequence)
    for i in range(len(sequence)-(n-1)):
        ngram.append(sequence[i:i+n])
    return ngram

if __name__ == "__main__":
    sample_str = "I am an NLPer"
    sample_list = ["I", "am", "an", "NLPer"]
    for i in range(1, 5):
        print(f"{i}-gram", "word ngram", create_word_ngram(sequence=sample_str, n=i))
        print(f"{i}-gram", "word ngram", create_word_ngram(sequence=sample_list, n=i))
        print(f"{i}-gram", "char ngram", create_char_ngram(sequence=sample_str, n=i))
        print(f"{i}-gram", "char ngram", create_char_ngram(sequence=sample_list, n=i))