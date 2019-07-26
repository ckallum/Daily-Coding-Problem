from collections import deque


def evaluate(parentheses):
    lst = list(parentheses)
    stack = deque()
    leftDict = ['[', '(', '{']
    rightDict = [']', ')', '}']
    for p in lst:
        if p in leftDict:
            stack.append(p)
        else:
            index = rightDict.index(p)
            if not stack or index != leftDict.index(stack.pop()):
                return False
    if stack:
        return False
    return True


def main():
    assert evaluate("([])[]({})") == True
    assert evaluate("([)]") == False
    assert evaluate("((()") == False


if __name__ == '__main__':
    main()

