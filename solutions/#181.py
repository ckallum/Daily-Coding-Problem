from cmath import inf


def find_palindrome_index(string, i, i1):
    if i == len(string) - 1 or i == 0:
        return string[i]
    while 0 <= i and i1 < len(string) and string[i] == string[i1]:
        i -= 1
        i1 += 1

    return string[i + 1:i1]


def find_min_palindrome(string):
    for i in range(len(string)):
        print(find_palindrome_index(string, i, i), find_palindrome_index(string, i, i + 1))


def min_palindrome_split(string, current=[]):
    if not string:
        return current
    if string == string[::-1]:
        return current + [string]
    result = []
    min_len = inf
    for i in range(1, len(string)):
        if i > 0 and (string[:i] == string[:i][::-1]):
            res = min_palindrome_split(string[i:], current + [string[:i]])
            if res and len(res) < min_len:
                result = res
                min_len = len(res)

    return result


def main():
    # find_min_palindrome("racecarannakayak")
    assert min_palindrome_split("racecarannakayak") == ["racecar", "anna", "kayak"]
    assert min_palindrome_split("abc") == ['a', 'b', 'c']


if __name__ == '__main__':
    main()
