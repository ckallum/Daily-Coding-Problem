import string


def solution(string, k):
    charCountDict = dict.fromkeys(string.ascii_lowercase, 0)
    distinctChars = 0
    returnString = ''
    maxLength = 0

    for x in string:
        if charCountDict[x] == 0:
            distinctChars += 1
        charCountDict[x] += 1

        if k > distinctChars:
            print('Not enough distinct chararcters')
            return

        # Algorithmic window problem

    return returnString, maxLength


def main():
    x, y = solution('abcbbbadadadadada', 3)
    print('Result:', x, 'Length:', y)


if __name__ == '__main__':
    main()
