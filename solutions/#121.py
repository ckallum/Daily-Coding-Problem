def possible_palindrome(string, k):
    if string and string == string[::-1]:
        return True
    if not k:
        return False
    if string[0] == string[-1]:
        return possible_palindrome(string[1:-1], k)

    for i, _ in enumerate(string):
        new = string[:i]+string[i+1:]
        if possible_palindrome(new, k-1):
            return True
    return False


def main():
    assert possible_palindrome("waterrfetawx", 2)


if __name__ == '__main__':
    main()
