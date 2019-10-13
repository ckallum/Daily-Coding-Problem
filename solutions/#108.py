def is_rotation(a, b):
    # for _ in range(len(a)):
    #     if a == b:
    #         return True
    #     b = b[-1] + b[:-1]
    #
    # return False

    return a in b*2


def main():
    assert is_rotation("abcde", "cdeab")
    assert not is_rotation("abc", "cba")


if __name__ == '__main__':
    main()