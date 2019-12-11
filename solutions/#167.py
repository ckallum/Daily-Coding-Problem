def is_palindrome(w):
    return w == w[::-1]


def palindrome_indexes(strings):
    result = []
    for index, word in enumerate(strings):
        for j, w1 in enumerate(strings[index+1:], start=index+1):
            if is_palindrome(word+w1):
                result.append((index, j))
            if is_palindrome(w1+word):
                result.append((j, index))
    return result


def main():
    assert palindrome_indexes(["code", "edoc", "da", "d"]) == [(0, 1), (1, 0), (2, 3)]


if __name__ == '__main__':
    main()