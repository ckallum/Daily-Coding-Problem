# Maxima window problem -> solution help from GeekForGeeks

from string import ascii_lowercase


def isVal(dic, k):
    count = 0
    for x in dic:
        if dic[x] != 0:
            count += 1
    return k >= count


def solution(s, k):
    charCountDict = dict.fromkeys(ascii_lowercase, 0)
    distinctChars = 0
    windowStartIndex = 0
    windowEndIndex = 0
    maxStartIndex = 0
    maxSize = 1

    for x in s:
        if charCountDict[x] == 0:
            distinctChars += 1
        charCountDict[x] += 1

    if k > distinctChars:
        print('Not enough distinct characters')
        return

    charCountDict = dict.fromkeys(ascii_lowercase, 0)
    charCountDict[s[windowStartIndex]] += 1
    for x in s[1:]:
        windowEndIndex += 1
        charCountDict[x] += 1
        while not isVal(charCountDict, k):
            charCountDict[s[windowStartIndex]] -= 1
            windowStartIndex += 1

        if windowEndIndex - windowStartIndex + 1 > maxSize:
            maxSize = windowEndIndex - windowStartIndex + 1
            maxStartIndex = windowStartIndex

    return maxSize, s[maxStartIndex: maxStartIndex + maxSize]


def main():
    y, x = solution("abcbbbadadadadada", 3)
    print('Result:', x, 'Length:', y)


if __name__ == '__main__':
    main()
