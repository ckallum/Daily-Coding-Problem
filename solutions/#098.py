def exists(board, word):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                val = board[row][col]
                board[row][col] = -1
                for r, c in [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]:
                    if -1 < r < len(board) and -1 < c < len(board[0]):
                        if exists_util(board, word[1:], (r, c)):
                            return True
                board[row][col] = val
    return False


def exists_util(board, word, coord):
    if not word:
        return True
    row, col = coord
    if board[row][col] == word[0]:
        board[row][col] = -1
        for r, c in [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]:
            if -1 < r < len(board) and -1 < c < len(board[0]):
                if exists_util(board, word[1:], (r, c)):
                    return True

    return False


def main():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert exists(board, "ABCCED")
    assert exists(board1, "SEE")
    assert not exists(board, "ABCB")


if __name__ == '__main__':
    main()
