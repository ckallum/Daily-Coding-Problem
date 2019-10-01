from copy import copy


def get_permutations(numbers, low, high):
    result = []
    if low == high:
        return [numbers]
    for i in range(low, high + 1):
        numbers[low], numbers[i] = numbers[i], numbers[low]
        temp = copy(numbers)
        result.extend(get_permutations(temp, low + 1, high))
        numbers[low], numbers[i] = numbers[i], numbers[low]

    print(result)
    return result


def main():
    assert get_permutations([1, 2, 3], 0, 2) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]


if __name__ == '__main__':
    main()
