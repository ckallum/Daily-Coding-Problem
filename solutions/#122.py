def strip_neg(num):
    if num[0] != '-':
        return num
    else:
        return num[1:]


def is_valid_number_helper(string, dec):
    if not string:
        return True
    current = string[0]
    if (current == '.' and dec) or (not current.isdigit() and current != '.'):
        return False
    if current == '.':
        dec = True
    return is_valid_number_helper(string[1:], dec)


def is_valid_number(string):
    if not string:
        return False

    e_split = string.split("e")
    if len(e_split) > 2:
        return False
    elif len(e_split) == 2:
        left = strip_neg(e_split[0])
        right = strip_neg(e_split[1])
        return left and right and is_valid_number_helper(left, False) and is_valid_number_helper(right, False)
    else:
        string = strip_neg(string)
        return string and is_valid_number_helper(string, False)


def main():
    assert is_valid_number("10")
    assert is_valid_number("-10")
    assert is_valid_number("10.1")
    assert is_valid_number("-10.1")
    assert is_valid_number("1e5")
    assert is_valid_number("-5")
    assert is_valid_number("1e-5")
    assert is_valid_number("1e-5.2")
    assert not is_valid_number("a")
    assert not is_valid_number("x 1")
    assert not is_valid_number("a -2")
    assert not is_valid_number("-")


if __name__ == '__main__':
    main()
