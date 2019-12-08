def find_duplicate(numbers):
    for num in numbers:
        n = abs(num)
        numbers[n-1] = -numbers[n-1]
    for index, num in enumerate(numbers):
        if abs(num) == num:
            return index+1


def main():
    assert find_duplicate([1, 2, 3, 4, 5, 5]) == 5
    assert find_duplicate([1, 2, 3, 3, 4, 5]) == 3


if __name__ == '__main__':
    main()
