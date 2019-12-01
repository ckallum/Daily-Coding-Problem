# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a positive integer n, find the smallest number of squared integers which sum to n.
#
# For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.
#
# Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
#
from cmath import inf


def count_recursive(n):
    if n == 0:
        return 0
    minimum = inf
    for i in range(1, n):
        if i ** 2 <= n:
            minimum = min(minimum, 1 + count_recursive(n - (i ** 2)))
    return minimum


def count_squares(n):
    squares = [x ** 2 for x in range(1, n) if x ** 2 <= n]
    count_dict = {x: inf for x in range(n + 1)}
    count_dict[0] = 0
    for square in squares:
        for num in range(square, n + 1):
            count_dict[num] = min(count_dict[n], 1 + count_dict[num - square])
    return count_dict[n]


def main():
    assert count_recursive(13) == 2
    assert count_recursive(27) == 3
    assert count_squares(13) == 2
    assert count_squares(27) == 3


if __name__ == '__main__':
    main()
