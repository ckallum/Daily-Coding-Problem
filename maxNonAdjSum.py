def findMax(l):
    maxCount = l[0]
    prevMaxCount = 0
    for x in l[1:]:
        nonAdjMax = prevMaxCount + x  # adds the max at i-2 to current value at array[i]
        prevMaxCount = maxCount  # set previous max to max value at i-1
        maxCount = max(nonAdjMax, maxCount, x)
        # Finds new max between max at i-2 + value at array[i], value at array[i] or max at previous index

    return maxCount


# [-3, -1, 4]


def main():
    l1 = [2, 4, 6, 2, 5]  # 13
    l2 = [5, 1, 1, 5]  # 10
    l3 = [5, -3, 2, 6, -1, -4]  # 11
    l4 = [-5, -3, -2, -6, -1, -4]
    print(findMax(l1))
    print(findMax(l2))
    print(findMax(l3))
    print(findMax(l4))


if __name__ == '__main__':
    main()
