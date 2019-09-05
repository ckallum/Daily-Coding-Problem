def find_largest_three_number_product(numbers):
    numbers = sorted(numbers)
    return max((numbers[0] * numbers[1] * numbers[len(numbers) - 1]),
               (numbers[len(numbers) - 1] * numbers[len(numbers) - 2] * numbers[len(numbers) - 3]))


def main():
    assert find_largest_three_number_product([-10, -10, 5, 2]) == 500
    assert find_largest_three_number_product([-10, -10, -1, 10, 10]) == 1000
    assert find_largest_three_number_product([-10, -10, -1, 5, 10, 10, 15, 20]) == 3000


if __name__ == '__main__':
    main()
