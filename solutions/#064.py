def knights_tour(n, board, current_row, current_col):
    count = 0
    if is_complete(board, n):
        return 1

    possible_moves = [(current_row - 1, current_col - 2), (current_row - 1, current_col + 2),
                      (current_row - 2, current_col - 1), (current_row - 2, current_col + 1),
                      (current_row + 1, current_col - 2), (current_row + 1, current_col + 2),
                      (current_row + 2, current_col - 1), (current_row + 2, current_col + 1)]
    for move in possible_moves:
        if is_valid(move[0], move[1], board, n):
            board[move[0]][move[1]] = True
            count += knights_tour(n, board, move[0], move[1])
            board[move[0]][move[1]] = False

    return count


def knights_tour_start(n):
    count = 0
    board = [[False for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            board[row][col] = True
            count += knights_tour(n, board, row, col)
            board[row][col] = False
    return count


def is_complete(board, n):
    return n * n == len([(x, y) for x in range(n) for y in range(n) if board[x][y]])


def is_valid(row, col, board, n):
    if row < 0 or col < 0:
        return False
    elif row >= n or col >= n:
        return False
    else:
        return not board[row][col]


def main():
    print(knights_tour_start(5))


if __name__ == '__main__':
    main()
