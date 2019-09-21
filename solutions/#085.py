def result(x, y, b):
    if x >= 2 ^ 32 or y >= 2 ^ 32:
        return None

    return (x * b) + (y * abs(b - 1))


def main():
    assert not result(2 ^ 32, 2 ^ 32, 0)
    assert result(4, 5, 0) == 5
    assert result(4, 5, 1) == 4


if __name__ == '__main__':
    main()
