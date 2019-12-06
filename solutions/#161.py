def reverse_bits(number):
    low = 0
    high = len(number) - 1
    while high > low:
        number[low], number[high] = number[high], number[low]
        low += 1
        high -= 1
    return number


def main():
    assert reverse_bits([1111, 0000, 1111, 0000, 1111, 0000, 1111, 0000]) == [0000, 1111, 0000, 1111, 0000, 1111, 0000,
                                                                              1111]


if __name__ == '__main__':
    main()
