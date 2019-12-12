def rotate_matrix(matrix):
    for i in range((len(matrix)+1)//2):
        for j in range(i, len(matrix)-i-1):
            matrix[i][j], matrix[-j-1][i], matrix[-i-1][-j-1], matrix[j][-i-1] = matrix[-j-1][i], matrix[-i-1][-j-1],  matrix[j][-i-1],matrix[i][j]

    print(matrix)
    return matrix


def main():
    assert rotate_matrix([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]]) == [[7, 4, 1],
                                          [8, 5, 2],
                                          [9, 6, 3]]


if __name__ == '__main__':
    main()
