def expected_rounds(n):
    count = 0
    while n >= 1:
        count += 1
        n = n//2
    return count


def main():
    assert expected_rounds(1) == 1
    assert expected_rounds(2) == 2
    assert expected_rounds(100) == 7
    assert expected_rounds(200) == 8


if __name__ == '__main__':
    main()