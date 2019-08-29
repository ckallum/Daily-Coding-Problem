def pow(x, y):
    if y == 0:
        return 1

    recursed = pow(x, int(y/2))
    if y % 2 == 0:
        return recursed * recursed
    else:
        return x * recursed * recursed


def main():
    assert pow(2, 4) == 16
    assert pow(3, 3) == 27


if __name__ == '__main__':
    main()