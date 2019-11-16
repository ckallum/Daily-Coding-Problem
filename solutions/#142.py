def regex_parenthesis(string, current_stack=[]):
    for index, char in enumerate(string):
        if char == "*":
            return regex_parenthesis(string[index+1:], current_stack) or regex_parenthesis(")"+string[index+1:], current_stack) or regex_parenthesis("("+string[index+1:], current_stack)
        elif char == "(":
            current_stack.append(char)
        else:
            if not current_stack:
                return False
            current_stack.pop()
    if current_stack:
        return False
    return True


def main():
    assert regex_parenthesis("(()*")
    assert regex_parenthesis("()")
    assert not regex_parenthesis(")*(")


if __name__ == '__main__':
    main()