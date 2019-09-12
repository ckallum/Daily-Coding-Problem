def remove_columns(matrix):
    if len(matrix) == 1:
        return 0

    count = 0
    for i in range(len(matrix[0])):
        for j in range(1, len(matrix)):
            if matrix[j][i] < matrix[j - 1][i]:
                count += 1
                break
    return count


def main():
    assert remove_columns([['c', 'b', 'a'],
                           ['d', 'a', 'f'],
                           ['g', 'h', 'i']]) == 1

    assert remove_columns([['a', 'b', 'c', 'd', 'e', 'f']]) == 0

    assert remove_columns([['z', 'y', 'x'],
                           ['w', 'v', 'u'],
                           ['t', 's', 'r']]) == 3


if __name__ == '__main__':
    main()
