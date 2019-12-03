def count_paths(grid):
    count = 0
    return dfs(grid, 0, 0)


def isSafe(grid, param, param1):
    if 0 <= param < len(grid) and 0 <= param1 < len(grid[0]) and grid[param][param1] == 0:
        return True
    return False


def dfs(grid, x, y):
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        grid[x][y] = 0
        return 1
    down = 0
    right = 0
    if isSafe(grid, x, y):
        grid[x][y] = 1
        down = dfs(grid, x + 1, y)
        right = dfs(grid, x, y + 1)
        grid[x][y] = 0
    return down+right


def main():
    assert count_paths([[0, 0, 1],
                        [0, 0, 1],
                        [1, 0, 0]]) == 2


if __name__ == '__main__':
    main()
