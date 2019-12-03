def first_recurring(string):
    string_dict = set()
    for char in string:
        if char in string_dict:
            return char
        string_dict.add(char)
    return None


def main():
    assert first_recurring("acbbac") == 'b'
    assert not first_recurring("abc")


if __name__ == '__main__':
    main()