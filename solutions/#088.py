def find_quotient(number1, number2):
    res = 0
    temp1 = number1
    while temp1 > 0:
        temp1 -= number2
        if temp1 > -1:
            res += 1
    return res


def main():
    assert find_quotient(20, 5) == 4
    assert find_quotient(21, 3) == 7
    assert find_quotient(3, 5) == 0


if __name__ == '__main__':
    main()
