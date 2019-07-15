# Backtracking, if it's valid we carry going down branch following that move, else we prune the branch and try another move


def nQueens(n, board=[]):
    if n == len(board):
        return 1
    count = 0
    for i in range(n):
        board.append(i)
        if isVal(board):
            count += nQueens(n, board)
        board.pop()
    return count


def isVal(board):
    row = len(board) - 1
    col = board[-1]

    for i, j in enumerate(board[:-1]):
        d = abs(col - j)
        if d == 0 or d == row - i:
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
