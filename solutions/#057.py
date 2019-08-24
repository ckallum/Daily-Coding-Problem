from collections import deque


def stringtolist(string, k):
    words = string.split()
    currentlen = 0
    currentstr = deque()
    final = list()
    for word in words:
        wordlen = len(word)
        if wordlen > k:
            return None
        if currentlen + wordlen <= k:
            currentstr.append(word)
            currentlen = currentlen + wordlen + 1
        else:
            final.append(" ".join(list(currentstr)))
            currentstr = deque([word])
            currentlen = wordlen+1
    final.append(" ".join(list(currentstr)))
    return final


def main():
    assert stringtolist("the quick brown fox jumps over the lazy dog", 10) == ["the quick", "brown fox", "jumps over",
                                                                               "the lazy", "dog"]


if __name__ == '__main__':
    main()
