def find_perfect_number(n):
    n = list(str(n))
    remaining = 10
    for number in n:
        remaining -= int(number)
    return int(str("".join(n)) + str(remaining))


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
