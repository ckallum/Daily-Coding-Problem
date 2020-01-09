def matrix_smaller_and_bigger_elements(coord1, coord2, matrix):
    smaller = matrix[coord1[0]][coord1[1]]
    larger = matrix[coord2[0]][coord2[1]]
    count = 0
    seen = []
    count += smaller_than(smaller, matrix, coord1[0], coord1[1] - 1, seen)
    count += smaller_than(smaller, matrix, coord1[0] - 1, coord1[1], seen)
    count += larger_than(larger, matrix, coord2[0] + 1, coord2[1], seen)
    count += larger_than(larger, matrix, coord2[0], coord2[1] + 1, seen)
    print(count)
    return count


def smaller_than(value, matrix, x, y, seen):
    if x < 0 or x > len(matrix) - 1 or y < 0 or y > len(matrix[0]) - 1 or matrix[x][y] >= value or (x, y) in seen:
        return 0
    print(matrix[x][y], value, seen)
    seen.append((x, y))
    count = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x + i, y + j) not in seen:
                count += smaller_than(value, matrix, x + i, y + j, seen)
    return count


def larger_than(value, matrix, x, y, seen):
    if x < 0 or x > len(matrix) - 1 or y < 0 or y > len(matrix[0]) - 1 or matrix[x][y] <= value:
        return 0
    seen.append((x, y))
    count = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x + i, y + j) not in seen:
                count += larger_than(value, matrix, x + i, y + j, seen)
    return count


def main():
    assert matrix_smaller_and_bigger_elements((1, 1), (3, 3), [[1, 3, 7, 10, 15, 20],
                                                               [2, 6, 9, 14, 22, 25],
                                                               [3, 8, 10, 15, 25, 30],
                                                               [10, 11, 12, 23, 30, 35],
                                                               [20, 25, 30, 35, 40, 45]]) == 15


if __name__ == '__main__':
    main()
