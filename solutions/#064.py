def knights_tour(n, visited, current_row, current_col):
    count = 0
    if is_complete(visited, n):
        return 1

    possible_moves = [(current_row - 1, current_col - 2), (current_row - 1, current_col + 2),
                      (current_row - 2, current_col - 1), (current_row - 2, current_col + 1),
                      (current_row + 1, current_col - 2), (current_row + 1, current_col + 2),
                      (current_row + 2, current_col - 1), (current_row + 2, current_col + 1)]
    for move in possible_moves:
        if is_valid(move[0], move[1], visited, n):
            visited.append(move)
            count += knights_tour(n, visited, move[0], move[1])
            visited.pop()
    return count


def knights_tour_start(n):
    count = 0
    visited = []
    for row in range(n):
        for col in range(n):
            visited.append((row, col)
                           )
            count += knights_tour(n, visited, row, col)
            visited.pop()
    return count


def is_complete(visited, n):
    return n * n == len(visited)


def is_valid(row, col, visited, n):
    if row < 0 or col < 0:
        return False
    elif row >= n or col >= n:
        return False
    else:
        return not ((row, col) in visited)


def main():
    assert knights_tour_start(1) == 1
    assert knights_tour_start(2) == 0
    assert knights_tour_start(3) == 0
    assert knights_tour_start(4) == 0


if __name__ == '__main__':
    main()
