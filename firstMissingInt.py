# List traversal/search ->  improved by using a hashTable for searching instead of list


def findMissingBrute(l):
    if len(l) == 0:
        return 1
    nextInt = 1
    found = False
    while not found:
        if nextInt in l:
            nextInt += 1
        else:
            found = True

    return nextInt


def main():
    nums = [3, 4, -1, 1, 0, 3, 4, 6, 7, 8, 3, 2, 10]
    print(findMissingBrute(nums))


if __name__ == '__main__':
    main()
