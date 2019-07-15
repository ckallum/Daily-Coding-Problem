# Backtracking Sudoku algorithm
from random import choice


def sudoku(board):
    if complete(board):
        return board
    emptySpaces = [(i, j) for i in range(1,10) for j in range(1,10) if board[i][j] == 0]
    row, col = choice(emptySpaces)
    for i in range(1, 10):
        board[row][col] = i
        if validBoard(board):
            res = sudoku(board)
            if complete(res):
                return res
        board[row][col] = 0
    return board


def validBoard(board):
    if not validCol(board) or not validRow(board) or not validBox(board):
        return False
    return True


def validCol(board):
    pass


def validRow(board):
    pass


def validBox(board):
    pass


def complete(board):
    for row in range(1, 10):
        for col in range(1, 10):
            if board[row][col] == 0:
                return False
    return True


def main():
    board = [[0 for _ in range(1, 10)] for _ in range(1, 10)]
    sudoku(board)


if __name__ == '__main__':
    main()
