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
    pass


def main():
    inp = '1212'
    print(decodeCount(inp))


if __name__ == '__main__':
    main()
