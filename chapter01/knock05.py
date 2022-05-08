"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def bigram(seq):
    return list(zip(seq[:-1], seq[1:]))


def ngram(seq, n=2):
    """
    n=2
    I  am [0:-2]
    am an [1:-1]
    an NLPer [2:]
    """
    subseq = []
    for i in range(n - 1):
        begin = i
        end = -n + i + 1
        subseq.append(seq[begin:end])
    subseq.append(seq[n - 1 :])
    # *：リストのアンパック
    return list(zip(*subseq))


if __name__ == "__main__":
    sample_str = "I am an NLPer"
    sample_list = ["I", "am", "an", "NLPer"]
    for i in range(1, 5):
        print(f"{i}-gram", "word ngram", ngram(seq=sample_str, n=i))
        print(f"{i}-gram", "word ngram", ngram(seq=sample_list, n=i))
        print(f"{i}-gram", "char ngram", ngram(seq=sample_str, n=i))
        print(f"{i}-gram", "char ngram", ngram(seq=sample_list, n=i))
