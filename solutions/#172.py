"""
Given a string s and a list of words words, where each word is the same length,
find all starting indices of substrings in s that is a concatenation of every
word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return
[0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are
no substrings composed of "dog" and "cat" in s.


"""


def helper(string, words, word_len):
    if not words:
        return True
    if not string:
        return False
    res = False
    if string[: word_len] in words:
        words.remove(string[:word_len])
        res = res or helper(string[word_len:], words, word_len)
        words.add(string[:word_len])
    return res


def find_indices(string, words):
    results = list()
    word_len = len(words[0])
    words = set(list(words))
    for i in range(len(string)):
        if helper(string[i:], words, word_len):
            results.append(i)
    return results


def main():
    assert find_indices("dogcatcatcodecatdog", ["cat", "dog"]) == [0, 13]
    assert not find_indices("barfoobazbitbyte", ["dog", "cat"])


if __name__ == '__main__':
    main()
