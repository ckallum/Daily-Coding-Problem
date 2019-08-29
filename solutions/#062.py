def find_traversals(n, m):
    grid = [[0 for _ in range(m)] for _ in range(n)]
    grid[0][0] = 1
    for row in range(n):
        for col in range(m):
            if row - 1 >= 0:
                grid[row][col] += grid[row - 1][col]
            if col - 1 >= 0:
                grid[row][col] += grid[row][col - 1]

    return grid[n - 1][m - 1]


def main():
    assert find_traversals(2, 2) == 2
    assert find_traversals(5, 5) == 70


if __name__ == '__main__':
    main()
