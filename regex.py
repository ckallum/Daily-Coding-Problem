# String iteration and matching with recursive call on substrings

def evaluate(regex, string):
    # if no pattern and no text, return True
    if not regex:
        return not string

    # first character will not be a Kleene star
    firstEquals = bool(string) and regex[0] in {string[0], '.'}
    if len(regex) >= 2 and regex[1] == "*":
        return firstEquals and evaluate(regex, string[1:]) or evaluate(regex[2:], string)

    else:
        return firstEquals and evaluate(regex[1:], string[1:])


def main():
    regex1 = ".*at"
    regex2 = "ab*cd*.*"
    regex3 = ".*"
    assert evaluate(regex1, "cat") == True
    assert evaluate(regex2, "abbcd") == True
    assert evaluate(regex2, "abbcdddeeeee") == True
    assert evaluate(regex3, "") == True


if __name__ == '__main__':
    main()
