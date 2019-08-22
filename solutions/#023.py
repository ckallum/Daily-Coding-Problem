from sys import maxsize


def findSteps(mat, start, goal):

    if start == goal:
        return 0

    minSteps = maxsize
    currentRow = start[0]
    currentCol = start[1]
    mat[currentRow][currentCol] = True
    neighbours = [(currentRow - 1, currentCol), (currentRow, currentCol - 1), (currentRow, currentCol + 1),
                  (currentRow + 1, currentCol)]
    for neighbour in neighbours:
        if validCoord(neighbour, mat):
            step = findSteps(mat, (neighbour[0], neighbour[1]), goal) + 1
            if step < minSteps:
                minSteps = step
    return minSteps


def validCoord(coord, mat):
    if 0 <= coord[0] < len(mat) and 0 <= coord[1] < len(mat[0]):
        if not mat[coord[0]][coord[1]]:
            return True
    return False


def main():
    mat = [[False, False, False, False],
           [True, True, False, True],
           [False, False, False, False],
           [False, False, False, False]]
    start = (3, 0)
    goal = (0, 0)
    assert findSteps(mat, start, goal) == 7


if __name__ == '__main__':
    main()
