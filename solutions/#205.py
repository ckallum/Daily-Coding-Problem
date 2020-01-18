from bisect import bisect


def next_lexographic_permutation(number):
    number = str(number)
    i = 0
    right = []
    replaced = None
    for i in range(len(number) - 2, 0, -1):
        right.append(number[i + 1])
        if number[i] < number[i + 1]:
            replaced = number[i]
            break
    replaced_index = bisect(right, replaced)
    replacement = right[replaced_index]
    right[replaced_index] = replaced
    return int(number[:i]+replacement+"".join(sorted(right)))



def main():
    assert next_lexographic_permutation(48975) == 49578


if __name__ == '__main__':
    main()
