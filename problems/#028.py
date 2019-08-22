def justify(words, k):
    result = list()
    currentString = list()
    currentCharLen = 0
    for word in words:
        currentString.append(word)
        if currentCharLen + len(word) + len(currentString)-1 <= k:
            currentCharLen += len(word)
        else:
            currentString.pop()
            newString = insertSpaces(currentString, currentCharLen, k)
            result.append(newString)
            currentString = [word]
            currentCharLen = len(word)
    result.append(insertSpaces(currentString, currentCharLen, k))
    print(result)
    return result


def insertSpaces(currentString, currentCharLen, k):
    extraSpaces = k-(currentCharLen+len(currentString)-1)
    print("Extra spaces: ", extraSpaces)
    print(currentCharLen)
    index = 0
    if extraSpaces == 0:
        return " ".join(currentString)
    while extraSpaces != 0:
        currentString[index] += " "
        index = (index+1) % (len(currentString)-1)
        extraSpaces -= 1
    return " ".join(currentString)


def main():
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    assert justify(words, 16) == ["the  quick brown", "fox  jumps  over", "the   lazy   dog"]


if __name__ == '__main__':
    main()
