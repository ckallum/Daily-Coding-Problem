from functools import reduce


def find_perfect_number(n):
    remaining = 10-int(reduce(lambda x, y: int(x)+int(y), list(str(n))))
    return int(str(n) + str(remaining))


def main():
    assert find_perfect_number(1) == 19
    assert find_perfect_number(2) == 28
    assert find_perfect_number(3) == 37
    assert find_perfect_number(4) == 46
    assert find_perfect_number(5) == 55
    assert find_perfect_number(6) == 64
    assert find_perfect_number(7) == 73
    assert find_perfect_number(8) == 82
    assert find_perfect_number(9) == 91
    assert find_perfect_number(10) == 109
    assert find_perfect_number(11) == 118
    assert find_perfect_number(200) == 2008
    assert find_perfect_number(201) == 2017


if __name__ == '__main__':
    main()
