def max_list_path(numbers):
    result = []
    i = 0
    j = 0
    current = numbers[i][j]
    while i < len(numbers)-1:
        result.append(current)
        current = max(numbers[i + 1][j], numbers[i + 1][j + 1])
        i += 1
    result.append(current)
    return result


def main():
    assert max_list_path([[1], [2, 3], [1, 5, 1]]) == [1, 3, 5]


if __name__ == '__main__':
    main()
