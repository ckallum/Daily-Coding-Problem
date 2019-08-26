def findindex(numbers, element):
    return bst(numbers, 0, len(numbers) - 1, element)


def bst(numbers, low, high, element):
    if high < low:
        return None

    mid = (high+low)//2
    if numbers[mid] == element:
        return mid

    if numbers[mid] >= numbers[low]:
        if numbers[low] <= element <= numbers[mid]:
            return bst(numbers, low, mid-1, element)
        else:
            return bst(numbers, mid+1, high, element)

    else:
        if numbers[mid] >= element:
            return bst(numbers, low+1, mid-1, element)
        return bst(numbers, mid + 1, high, element)


def main():
    assert findindex([13, 18, 25, 2, 8, 10], 8) == 4


if __name__ == '__main__':
    main()
