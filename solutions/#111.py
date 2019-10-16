def anagram_indexes(word, string):
    current = set(word)
    indexes = []
    for index, char in enumerate(string):
        if char in current:
            current.remove(char)
            for i in range(1, len(word)):
                if index + i < len(string) and string[index + i] in current:
                    current.remove(string[index + i])
                    if not current:
                        indexes.append(index)
                        current = set(word)
                        break
                else:
                    current = set(word)
                    break
    print(indexes)
    return indexes


def main():
    assert anagram_indexes("ab", "abxaba") == [0, 3, 4]


if __name__ == '__main__':
    main()
