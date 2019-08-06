# Backtracking, if it's valid we carry going down branch following that move, else we prune the branch and try another move
# each index of the board is a new row, the number of the queen appended is the column in the row.


def nQueens(n, board=[]):
    if n == len(board):  # All rows are filled by a queen
        return 1
    count = 0
    for i in range(n):
        board.append(i)
        if valid(board):
            count += nQueens(n, board)
        board.pop()
    return count


def valid(board):
    rows = len(board) - 1  # Current number of rows being occupied
    col = board[-1]  # Column of last queen put down ->if it was put down that column must be valid
    for row, column in enumerate(board[:-1]): # Don't count last element as that's the element we are examining
        diff = abs(col - column)
        if diff == 0 or diff == rows - row:
            return False
    return True


def main():
    assert nQueens(0) == 1
    assert nQueens(1) == 1
    assert nQueens(2) == 0
    assert nQueens(3) == 0
    assert nQueens(4) == 2


if __name__ == '__main__':
    main()
