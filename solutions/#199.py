def correct_braces(string):
    i = 0
    while i < len(string) and string[i] == ')':
        i += 1
    string = string[i:]
    if not string:
        return ""
    open = 0
    for index, p in enumerate(string):
        if p == '(':
            open += 1
        elif p == ')':
            open -= 1
        if not open:
            break
    return string[open:] if open else string[:index + 1] + correct_braces(string[index + 1:])


def main():
    assert correct_braces("()(()") == "()()"
    assert correct_braces("()(()))") == "()(())"
    assert correct_braces(")(())") == "(())"
    assert correct_braces("())(") == "()"


if __name__ == '__main__':
    main()
