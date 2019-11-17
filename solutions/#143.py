def pivot(numbers, x):
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] < x:
            left += 1
        if numbers[left] >= x:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            right -= 1

    print(numbers)
    left += 1
    right = len(numbers) - 1
    while left < right:
        if numbers[right] == x:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
        else:
            right -= 1
    print(numbers)
    return numbers


def main():
    assert pivot([9, 12, 3, 5, 14, 10, 10], 10) == [9, 5, 3, 10, 10, 14, 12]


if __name__ == '__main__':
    main()
