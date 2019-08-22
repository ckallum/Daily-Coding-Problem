def palindrome(string):
    if string == string[::-1]:
        return string

    if string[0] == string[-1]:
        return string[0] + palindrome(string[1:-1]) + string[-1]
    else:
        p1 = string[0] + palindrome(string[1:]) + string[0]
        p2 = string[-1] + palindrome(string[:-1]) + string[-1]
        if len(p1) > len(p2):
            return p2
        elif len(p1) < len(p2):
            return p1
    if p1 < p2:
        return p1
    else:
        return p2


def main():
    assert palindrome("race") == "ecarace"
    assert palindrome("google") == "elgoogle"
    assert palindrome("gloog") == "gloolg"


if __name__ == '__main__':
    main()
