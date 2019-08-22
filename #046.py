"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than
one with the maximum length,return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""


def findPalindromeRecursive(string):
    if not string:
        return ""
    if string == string[::-1]:
        return string
    else:
        return findPalindromeRecursive(string[1:]) if len(findPalindromeRecursive(string[1:])) > len(
                findPalindromeRecursive(string[:-1])) else findPalindromeRecursive(string[:-1])


def main():
    assert findPalindromeRecursive("aabcdcb") == "bcdcb"
    assert findPalindromeRecursive("bananas") == "anana"


if __name__ == '__main__':
    main()
