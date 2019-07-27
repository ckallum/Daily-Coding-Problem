def fill(levels):
    leftpillar = 0
    rightpillar = len(levels) - 1
    leftmax = 0
    rightmax = 0
    res = 0
    if len(levels) < 3:
        return 0
    while leftpillar <= rightpillar:
        if levels[leftpillar] < levels[rightpillar]:
            if levels[leftpillar] > leftmax:
                leftmax = levels[leftpillar]
            else:
                res += leftmax - levels[leftpillar]
            leftpillar += 1
        else:
            if levels[rightpillar] > rightmax:
                rightmax = levels[rightpillar]
            else:
                res += rightmax - levels[rightpillar]
            rightpillar -= 1
    return res


def main():
    assert fill([3, 0, 1, 3, 0, 5]) == 8


if __name__ == '__main__':
    main()
