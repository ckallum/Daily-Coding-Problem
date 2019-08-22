def buildSentence(wordsLeft, stringLeft):
    if not wordsLeft and stringLeft:
        return None
    if not stringLeft:
        return []
    res = []
    for index, x in enumerate(wordsLeft):
        if stringLeft[:len(x)] == x:
            res.append(wordsLeft.pop(index))
            remainingString = stringLeft[len(x):]
            remaining = buildSentence(wordsLeft, remainingString)
            if remaining is not None:
                return res+remaining
            wordsLeft.append(x)
    return res


def main():
    wordsDict = ['quick', 'brown', 'the', 'fox']
    string1 = 'thequickbrownfox'

    assert buildSentence(wordsDict, string1) == ['the', 'quick', 'brown', 'fox']


if __name__ == '__main__':
    main()