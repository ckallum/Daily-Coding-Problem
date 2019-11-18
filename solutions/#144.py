def nearest_largest_number(numbers, index):
    numbers = [tup[0] for tup in enumerate(numbers) if tup[1] > numbers[index]]
    if not numbers:
        return None
    return min(numbers)


def main():
    assert nearest_largest_number([4, 1, 3, 5, 6], 0) == 3
    assert nearest_largest_number([4, 1, 3, 5, 6], 1) == 2
    assert nearest_largest_number([4, 1, 3, 5, 6], 2) == 0
    assert not nearest_largest_number([4, 1, 3, 5, 6], 4)


if __name__ == '__main__':
    main()
