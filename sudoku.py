# Backtracking Sudoku algorithm
from random import choice


def sudoku(board):
    if complete(board):
        return board
    emptySpaces = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
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
    for j in range(len(board[0])):
        if duplicates([board[i][j] for i in range(len(board))]):
            return False
    return True


def validRow(board):
    for row in board:
        if duplicates(row):
            return False
    return True


def validBox(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(board[i + k][j + l])
            if duplicates(block):
                return False
    return True


def duplicates(arr):
    c = {}
    for val in arr:
        if val in c and val != 0:
            return True
        c[val] = True
    return False


def complete(board):
    for row in range(1, 10):
        for col in range(1, 10):
            if board[row][col] == 0:
                return False
    return True


def main():
    board = [[0 for _ in range(9)] for _ in range(9)]
    print(sudoku(board))


if __name__ == '__main__':
    main()
