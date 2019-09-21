def count_unclosed_parentheses(parentheses):
    current_parentheses = []
    for p in parentheses:
        if current_parentheses:
            if p == ')' and current_parentheses[-1] == '(':
                current_parentheses.pop()
            else:
                current_parentheses.append(p)

        else:
            current_parentheses.append(p)
    return len(current_parentheses)


def main():
    assert count_unclosed_parentheses("())()") == 1
    assert count_unclosed_parentheses(")(") == 2


if __name__ == '__main__':
    main()