def multiplication_table(n, x):
    if n == 1:
        return n
    if x // n > n:
        return 0
    tuples = list()
    for i in range(1, x + 1):
        if x % i == 0 and i < n:
            tuples.append((i, x // i))
    return len(tuples)


def main():
    assert multiplication_table(6, 12) == 4
    assert multiplication_table(4, 48) == 0
    assert multiplication_table(12, 6) == 4


if __name__ == '__main__':
    main()
