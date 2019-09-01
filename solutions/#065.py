def naive_spiral(matrix, n, m):
    result_list = []
    right = True
    down = False
    left = False
    up = False
    current = (0, 0)
    count = 0
    while count != n * m:
        result_list.append(matrix[current[0]][current[1]])
        print(result_list)
        matrix[current[0]][current[1]] = True
        count += 1
        if right:
            if current[1] + 1 < m:
                if matrix[current[0]][current[1] + 1] != True:
                    current = current[0], current[1] + 1
                else:
                    current = current[0] + 1, current[1]
                    right = False
                    down = True
            else:
                current = current[0] + 1, current[1]
                right = False
                down = True
        elif down:
            if current[0] + 1 < n:
                if matrix[current[0] + 1][current[1]] != True:
                    current = current[0] + 1, current[1]
                else:
                    current = current[0], current[1] - 1
                    down = False
                    left = True
            else:
                current = current[0], current[1] - 1
                down = False
                left = True
        elif left:
            if current[1] - 1 >= 0:
                if matrix[current[0]][current[1] - 1] != True:
                    current = current[0], current[1] - 1
                else:
                    current = current[0] - 1, current[1]
                    left = False
                    up = True
            else:
                current = current[0] - 1, current[1]
                left = False
                up = True
        else:
            if current[0] - 1 >= 0:
                if matrix[current[0] - 1][current[1]] != True:
                    current = current[0] - 1, current[1]
                else:
                    current = current[0], current[1] + 1
                    right = True
                    up = False
            else:
                current = current[0], current[1] + 1
                right = True
                up = False
    return result_list


def shorter_spiral_helper(matrix, current_row, current_col, row_boundary, col_boundary):
    numbers = []
    for i in range(current_col, col_boundary + 1):
        numbers.append(matrix[current_row][i])

    for i in range(current_row+1, row_boundary + 1):
        numbers.append(matrix[i][col_boundary])

    if row_boundary > current_row:
        for i in range(col_boundary-1, current_col-1, -1):
            numbers.append(matrix[row_boundary][i])

    if col_boundary > current_col:
        for i in range(row_boundary-1, current_row, -1):
            numbers.append(matrix[i][current_col])
    return numbers


def shorter_spiral(matrix, n, m):
    current_row, current_col, row_boundary, col_boundary = 0, 0, n - 1, m - 1
    result_list = []
    while current_row < row_boundary or current_col < col_boundary:
        result_list.extend(shorter_spiral_helper(matrix, current_row, current_col, row_boundary, col_boundary))
        if current_row < row_boundary:
            current_row += 1
            row_boundary -= 1
        if current_col < col_boundary:
            current_col += 1
            col_boundary -= 1

    print(result_list)
    return result_list


def main():
    assert naive_spiral([[1, 2, 3, 4, 5],
                         [6, 7, 8, 9, 10],
                         [11, 12, 13, 14, 15],
                         [16, 17, 18, 19, 20]], 4, 5) == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14,
                                                          13, 12]
    assert shorter_spiral([[1, 2, 3, 4, 5],
                         [6, 7, 8, 9, 10],
                         [11, 12, 13, 14, 15],
                         [16, 17, 18, 19, 20]], 4, 5)== [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14,
                                                          13, 12]


if __name__ == '__main__':
    main()
