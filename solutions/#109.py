from itertools import chain


def swap_even_with_odd(numbers):
    return list(
        chain(*[(numbers[x], numbers[x - 1]) for x in range(1, len(numbers), 2)])) if not len(
        numbers) % 2 else list(
        chain(*[(numbers[x], numbers[x - 1]) for x in range(1, len(numbers), 2)])) + [numbers[
                                                                                          len(
                                                                                              numbers) - 1]]


def main():
    assert swap_even_with_odd([1, 0, 1, 0, 1, 0, 1]) == [0, 1, 0, 1, 0, 1, 1]
    assert swap_even_with_odd([1, 1, 1, 0, 0, 0, 1, 0]) == [1, 1, 0, 1, 0, 0, 0, 1]


if __name__ == '__main__':
    main()
