def decode(num):
    if 0 < int(num) <= 26:
        return 1
    else:
        return 0


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


def dpDecodeCount(num):
    parseDict = dict()
    parseDict[num[0]] = 1
    for i in range(1, len(num)):
        if i > 1:
            if decode(num[i-1:i+1]) == 0:
                parseDict[num[:i + 1]] = parseDict[num[:i]]
            else:
                parseDict[num[:i + 1]] = parseDict[num[:i - 1]] + parseDict[num[:i]]
        else:
            parseDict[num[:i + 1]] = decode(num[:i+1]) + 1

    return parseDict[num]


def main():
    inp = '12221221344511221213'
    print(decodeCount(inp))
    print(dpDecodeCount(inp))


if __name__ == '__main__':
    main()
