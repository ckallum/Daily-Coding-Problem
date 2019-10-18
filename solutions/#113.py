def reverse_string(string):
    return " ".join(reversed(string.split()))


def main():
    assert reverse_string("hello world here") == "here world hello"


if __name__ == '__main__':
    main()
