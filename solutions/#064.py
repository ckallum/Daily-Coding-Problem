from copy import copy


def knights_tour(n, visited, current_row, current_col):
    count = 0
    if is_complete(visited, n):
        return 1

    possible_moves = [(current_row - 1, current_col - 2), (current_row - 1, current_col + 2),
                      (current_row - 2, current_col - 1), (current_row - 2, current_col + 1),
                      (current_row + 1, current_col - 2), (current_row + 1, current_col + 2),
                      (current_row + 2, current_col - 1), (current_row + 2, current_col + 1)]
    valid_moves = [pos for pos in possible_moves if 0 <= pos[0] < n and 0 <= pos[1] < n and pos not in visited]
    for move in valid_moves:
        temp_visited = copy(visited)
        temp_visited.append(move)
        count += knights_tour(n, temp_visited, move[0], move[1])

    return count


def knights_tour_start(n):
    count = 0
    visited = []
    for row in range(n):
        for col in range(n):
            temp_visited = copy(visited)
            temp_visited.append((row, col))
            count += knights_tour(n, temp_visited, row, col)
    return count


def is_complete(visited, n):
    return n * n == len(visited)


def main():
    assert knights_tour_start(1) == 1
    assert knights_tour_start(2) == 0
    assert knights_tour_start(3) == 0
    assert knights_tour_start(4) == 0
    assert knights_tour_start(5) == 1728


if __name__ == '__main__':
    main()
