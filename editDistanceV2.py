def recursiveSolution(string1, string2):
    if not string1 and string2:
        return len(string2)
    elif not string2 and string1:
        return len(string1)
    elif not(string1 or string2):
        return 0

    if string1[-1] == string2[-1]:
        return recursiveSolution(string1[:-1], string2[:-1])
    else:
        return 1 + min(recursiveSolution(string1, string2[:-1]), recursiveSolution(string1[:-1], string2[:-1]),
                       recursiveSolution(string1[:-1], string2))


def dpSolution(string1, string2):
    matrix = [[0 for _ in range(len(string1)+1)] for _ in range(len(string2)+1)]
    for i in range(len(matrix)):  # i = current row = current substring in string 2
        for j in range(len(matrix[0])):  # j = current column = current substring in string 1
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif string2[i-1] == string1[j-1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
    return matrix[len(string2) - 1][len(string1) - 1]


def main():
    assert dpSolution("kitten", "sitting") == 3
    assert recursiveSolution("kitten", "sitting") == 3


if __name__ == '__main__':
    main()
