from random import randint


def evolve(board):
    for row, val in enumerate(board):
        for col, val2 in enumerate(val):
            count = getNeighbours((col, row), board)
            if board[row][col] and (count > 3 or count < 2):
                board[row][col] = False
            elif not board[row][col] and count == 3:
                board[row][col] = True


def initialise(alive=[]):
    board = [[False for _ in range(50)] for _ in range(50)]
    if alive:
        for col, row in alive:
            try:
                board[col][row] = True
            except:
                pass
    else:
        for _ in range(5):
            x, y = randint(0, 49), randint(0, 49)
            board[x][y] = True
    return board


def printAliveCoords(board):
    alive = [(x, y) for x in range(len(board[0])) for y in range(len(board)) if board[y][x]]
    print(alive)


def getNeighbours(coordinate, board):
    x, y = coordinate
    count = 0
    neighbours = [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1),
                  (x, y + 1)]
    for neighbour in neighbours:
        col, row = neighbour
        try:
            if board[row][col]:
                count += 1
        except:
            pass
    return count


def main():
    board = initialise([(1, 1), (1, 2),(2, 1),(2, 3),(2, 1)])
    for _ in range(1000):
        printAliveCoords(board)
        evolve(board)


if __name__ == '__main__':
    main()
