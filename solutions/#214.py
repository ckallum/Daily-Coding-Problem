def consecutive_bits(number):
    result = 0
    count = 0
    while number > 0:
        modulus = number % 2
        if modulus == 1:
            count += 1
        else:
            count = 0
        if count > result:
            result = count
        number //= 2
    return result


def main():
    assert consecutive_bits(156) == 3


if __name__ == '__main__':
    main()
