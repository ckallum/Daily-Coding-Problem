from functools import reduce
from itertools import chain


def count_bishop_pairings(coords, m):
    count = 0
    visited = []
    for row, col in coords:
        d_coords = list(chain(zip(range(row - 1, -1, -1), range(col - 1, -1, -1)),
                              zip(range(row + 1, m, 1), range(col + 1, m, 1)),
                              zip(range(row + 1, m, 1), range(col - 1, -1, -1)),
                              zip(range(row - 1, -1, -1), range(col + 1, m, 1)),
                              ))
        # d_coords = list(reduce(lambda x, y: x + y, [list(zip(range(row - 1, -1, -1), range(col - 1, -1, -1))),
        #                                             list(zip(range(row + 1, m, 1), range(col + 1, m, 1))),
        #                                             list(zip(range(row + 1, m, 1), range(col - 1, -1, -1))),
        #                                             list(zip(range(row - 1, -1, -1), range(col + 1, m, 1)))]
        #                        ))
        # diagonal_coords = [[(row - i, col - i), (row - i, col + i), (row + i, col - i),
        #                     (row + i, col + i)] for i in range(1, m)]
        # diagonal_coords = list(reduce(lambda x, y: x + y, diagonal_coords))

        for diag in d_coords:
            if diag in coords and diag not in visited:
                count += 1
        visited.append((row, col))
    return count


def main():
    assert count_bishop_pairings([(0, 0), (1, 2), (2, 2), (4, 0)], 5) == 2
    assert count_bishop_pairings([(0, 0), (0, 4), (1, 1), (4, 0), (2, 2)], 5) == 6
    assert count_bishop_pairings([(0, 0), (0, 4), (2, 2), (4, 0), (4, 4)], 5) == 6


"""
    board1 = [b 0 0 0 0]
             [0 0 b 0 0]
             [0 0 b 0 0]  = 2
             [0 0 0 0 0]
             [b 0 0 0 0]

    board2 = [b 0 0 0 b]
             [0 b 0 0 0]
             [0 0 b 0 0]  = 6
             [0 0 0 0 0]
             [b 0 0 0 0]

    board3 = [b 0 0 0 b]
             [0 0 0 0 0]
             [0 0 b 0 0]  = 6
             [0 0 0 0 0]
             [b 0 0 0 b]

"""

if __name__ == '__main__':
    main()
