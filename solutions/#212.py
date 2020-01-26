def int_to_column(n):
    result = ""
    while n > 0:
        modulus = n % 26
        if modulus == 0:
            modulus = 26
            n -= 1
        result += chr(ord('A') + modulus - 1)
        n //= 26
    return result[::-1]


def main():
    assert int_to_column(27) == 'AA'
    assert int_to_column(1) == 'A'
    assert int_to_column(26) == 'Z'
    assert int_to_column(51) == 'AY'


if __name__ == '__main__':
    main()
