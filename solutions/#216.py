def roman_to_decimal(roman):
    roman_map = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    result = roman_map[roman[-1]]
    prev = roman[-1]
    for char in reversed(roman[:-1]):
        result += roman_map[char] * (-1 if roman_map[char] < roman_map[prev] else 1)
        prev = char
    return result


def main():
    assert roman_to_decimal("I") == 1
    assert roman_to_decimal("IV") == 4
    assert roman_to_decimal("XL") == 40
    assert roman_to_decimal("XIV") == 14
    assert roman_to_decimal("CCXLVI") == 246


if __name__ == '__main__':
    main()
