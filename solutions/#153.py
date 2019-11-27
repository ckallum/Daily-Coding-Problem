# Good morning! Here's your coding interview problem for today.
#
# Find an efficient algorithm to find the smallest distance (measured in number of words)
# between any two given words in a string.
#
# For example, given words "hello", and "world" and a text content of "dog cat hello cat
# dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.
from cmath import inf


def find_distance(words, w1, w2):
    last_word, last_index = None, None
    min_dist = inf
    for index, word in enumerate(words.split()):
        if word == w1 or word == w2:
            if (word == w1 and last_word == w2) or (word == w2 and last_word == w1):
                if index - last_index - 1 < min_dist:
                    min_dist = index - last_index - 1
            last_index = index
            last_word = word
    return min_dist


def main():
    assert find_distance("dog cat hello cat world dog dog hello cat dog cat world", "hello", "world") == 1
    assert find_distance("dog cat hello cat dog dog hello cat world", "dog", "world") == 2
    assert find_distance("dog cat hello cat dog dog hello cat world", "hello", "world") == 1
    assert find_distance("dog cat hello cat dog dog hello world", "hello", "world") == 0


if __name__ == '__main__':
    main()
