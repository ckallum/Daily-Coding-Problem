def integer_palindrome(number):
    while number > 0:
        current = number
        size = 0
        right_digit = current % 10
        left_digit = 0
        while current > 0:
            left_digit = current % 10
            current //= 10
            size += 1
        if left_digit != right_digit:
            return False
        number -= left_digit * (10 ** size)
    return True


def main():
    assert integer_palindrome(121)
    assert integer_palindrome(888)
    assert not integer_palindrome(678)
    assert not integer_palindrome(1678)
    assert integer_palindrome(1661)


if __name__ == '__main__':
    main()
