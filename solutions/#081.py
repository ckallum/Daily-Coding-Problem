def find_possible_combinations(mappings, string):
    combination_dict = {"": [""]}

    for index, value in enumerate(string):
        combination_dict[string[:index + 1]] = []
        if value in mappings:
            combination_dict[string[:index + 1]] = [x + v for x in combination_dict[string[:index]] for v in
                                                    mappings[value]]
        else:
            combination_dict[string[:index + 1]] = combination_dict[string[:index]]
    if string in mappings:
        if combination_dict[string] == [""]:
            combination_dict[string] = mappings[string]
        else:
            combination_dict[string].extend(mappings[string])

    return combination_dict[string]


def main():
    assert find_possible_combinations({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "23") == ["ad", "ae", "af", "bd",
                                                                                              "be", "bf", "cd", "ce",
                                                                                              "cf"]

    assert find_possible_combinations({"2": ["a", "b", "c"], "3": ["d", "e", "f"], "23": ["g", "h", "i"]}, "23") == [
        "ad", "ae", "af", "bd",
        "be", "bf", "cd", "ce",
        "cf", "g", "h", "i"]

    assert find_possible_combinations({"23": ["g", "h", "i"]}, "23") == ["g", "h", "i"]


if __name__ == '__main__':
    main()
