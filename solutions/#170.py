from cmath import inf
from copy import copy

characters = set("abcdefghijklmnopqrstuvwxyz")


def shortest_transformation(start, end, dictionary):
    result = helper(start, end, [start], [], dictionary)
    return result


def helper(word, end, current_result, seen, dictionary):
    if word == end:
        return current_result
    possible_words = list()
    seen.append(word)
    for i in range(len(word)):
        for char in characters:
            possible = word[:i] + char + word[i + 1:]
            if possible in dictionary and possible not in seen:
                possible_words.append(possible)
    min_len = inf
    result = None
    for possible in possible_words:
        r = helper(possible, end, current_result + [possible], seen, dictionary)
        if r and len(r) < min_len:
            result = r
            min_len = len(result)
    return result


def main():
    assert shortest_transformation("dog", "cat", {"dot", "dop", "dat", "cat"}) == ["dog", "dot", "dat", "cat"]
    assert not shortest_transformation("dog", "cat", {"dot", "dop", "dat", "car"})


if __name__ == '__main__':
    main()
