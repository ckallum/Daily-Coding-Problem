def shortest_unique_prefix(strings):
    results = []
    for index, word in enumerate(strings):
        for i in range(len(word)):
            if word[:i] not in [w[:i] for w in strings[:index] + strings[index + 1:]]:
                results.append(word[:i])
                break
    return results


def main():
    assert shortest_unique_prefix(["dog",
                                   "cat",
                                   "apple",
                                   "apricot",
                                   "fish"]) == ["d",
                                                "c",
                                                "app",
                                                "apr",
                                                "f"]


if __name__ == '__main__':
    main()
