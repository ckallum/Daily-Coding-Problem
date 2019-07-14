from collections import deque


def parentheses(s):
    leftDict = ['{', '[', '(']
    rightDict = ['}', ']', ')']
    parStack = deque()
    if len(s) % 2 != 0:
        return False
    for x in s:
        print(parStack)
        if x in leftDict:
            parStack.append(x)
        elif x != rightDict[leftDict.index(parStack.pop())]:
            return False
    return True


def main():
    assert parentheses("((()))") == True
    assert parentheses("[()]{}") == True
    assert parentheses("({[)]") == False


if __name__ == '__main__':
    main()
