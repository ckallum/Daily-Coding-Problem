def find_shortest_substring(string, chars, current=""):
    if not chars:
        return current
    min_res = ""
    for index, char in enumerate(string):
        if char in chars:
            temp = ""
            if not current:
                temp += char
            else:
                temp = current + string[0:index + 1]
            new_list = list(set(chars) - {char})
            res = find_shortest_substring(string[index + 1:], new_list, temp)
            if res:
                if not new_list:
                    return res
                elif len(res) < len(min_res) or not min_res:
                    min_res = res
    return min_res


def main():
    assert find_shortest_substring("ddcebaecde", ["a", "c", "d"]) == "aecd"
    assert find_shortest_substring("figehaeci", ["a", "e", "i"]) == "aeci"


if __name__ == '__main__':
    main()
