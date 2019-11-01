def rotate(numbers, k):
    for index, number in enumerate(numbers[k:], start=k):
        numbers[index-k], numbers[index] = numbers[index], numbers[index-k]
    return numbers


def main():
    assert rotate([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]


if __name__ == '__main__':
    main()
