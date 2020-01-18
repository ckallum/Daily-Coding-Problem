from bisect import bisect


def next_lexographic_permutation(number):
    number = list(str(number))
    i = 0
    replaced = None
    for i in range(len(number) - 2, 0, -1):
        if number[i] < number[i + 1]:
            replaced = number[i]
            break
    for j in range(len(number) - 1, i, -1):
        if number[j] > replaced:
            number[i], number[j] = number[j], number[i]
            break
    number[i + 1:] = reversed(number[i + 1:])
    return int("".join(number))


def main():
    assert next_lexographic_permutation(48975) == 49578


if __name__ == '__main__':
    main()
