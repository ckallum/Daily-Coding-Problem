from collections import Counter


def is_palindrome_recursive(string, low):
    if string == string[::-1]:
        return True
    string = list(string)
    for i in range(low, len(string)):
        string[i], string[len(string) - 1] = string[len(string) - 1], string[i]
        if is_palindrome_recursive("".join(string), i + 1):
            return True
        string[i], string[len(string) - 1] = string[len(string) - 1], string[i]
    return False


def is_palindrome(string):
    chars = Counter(string)
    odd_count = 0
    for char in chars:
        if chars[char] % 2:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


def main():
    assert is_palindrome_recursive("racecar", 0)
    assert not is_palindrome_recursive("daily", 0)
    assert is_palindrome_recursive("rcarace", 0)
    assert is_palindrome("racecar")
    assert not is_palindrome("daily")
    assert is_palindrome("rcarace")


if __name__ == '__main__':
    main()
