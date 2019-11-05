def valid(guess, n):
    return guess - 10 ** 6 < n < guess + 10 ** 6


def helper(n, low, high):
    mid = low + ((high - low) / 2)
    if valid(mid * mid, n):
        return mid
    elif mid*mid > n:
        return helper(n, low, mid)
    else:
        return helper(n, mid, high)


def square_root(n):
    return helper(n, 0, n)


def main():
    assert valid(square_root(9),  3)
    assert valid(square_root(2), 1.41421356237)
    assert valid(square_root(10000), 100)


if __name__ == '__main__':
    main()
