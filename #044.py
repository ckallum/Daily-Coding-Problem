count = 0


def bruteinversion(numbers):
    c = 0
    for index, num in enumerate(numbers):
        for index2, num2 in enumerate(numbers):
            if num2 < num and index2 > index:
                c += 1
    return c


def inversionUsingMergeSort(numbers):
    if len(numbers) < 2:
        return numbers
    mid = int(len(numbers) / 2)
    left = inversionUsingMergeSort(numbers[:mid])
    right = inversionUsingMergeSort(numbers[mid:])
    return mergeSortUitl(left, right)


def mergeSortUitl(left, right):
    global count
    print(left, right)
    sortedArr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedArr.append(left[i])
            i += 1
        else:
            sortedArr.append(right[j])
            temp = i
            while i < len(left) and left[i] > right[j]:
                print(count)
                count += 1
                i += 1
            j += 1
            i = temp

    while i < len(left):
        sortedArr.append(left[i])
        i += 1
        count += 1
    while j < len(right):
        sortedArr.append(right[j])
        j += 1
    return sortedArr


def main():
    assert bruteinversion([2, 4, 1, 3, 5]) == 3
    assert bruteinversion([5, 4, 3, 2, 1]) == 10
    inversionUsingMergeSort([2, 4, 1, 3, 5])
    print("Count = ", count)


if __name__ == '__main__':
    main()
