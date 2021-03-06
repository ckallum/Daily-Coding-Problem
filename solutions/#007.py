# Dynamic programming string traversal -> Fibonacci ish


def decode(num):
    if 0 < int(num) <= 26:
        return 1
    else:
        return 0


# Recursive Method
def decodeCount(num):
    if len(num) == 1:
        return 1
    elif len(num) == 2:
        return 1 + decode(num)
    else:
        count = decodeCount(num[1:])
        if decode(num[:2]) == 1:
            count += decodeCount(num[2:])

    return count


# Dynamic Programming method bottom up
def dpDecodeCount(num):
    parseDict = dict()
    parseDict[num[0]] = 1
    for i in range(1, len(num)):
        if i > 1:
            if decode(num[i - 1:i + 1]) == 0:
                parseDict[num[:i + 1]] = parseDict[num[:i]]
            else:
                parseDict[num[:i + 1]] = parseDict[num[:i - 1]] + parseDict[num[:i]]
        else:
            parseDict[num[:i + 1]] = decode(num[:i + 1]) + 1

    return parseDict[num]


def main():
    inp = '12221221344511221213'
    assert decodeCount(inp) == 1870
    assert dpDecodeCount(inp) == 1870


if __name__ == '__main__':
    main()
