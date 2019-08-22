def encode(s1):
    count = 1
    ret = ""
    ch = s1[0]
    for x in s1[1:]:
        if x == ch:
            count += 1
        else:
            ret += str(count)+ch
            ch = x
            count = 1
    ret += str(count) + ch
    return ret


def main():
    s1 = "AAAABBBCCDAA"
    assert encode(s1) == "4A3B2C1D2A"


if __name__ == '__main__':
    main()