def colour_fill(grid, coord, colour):
    c = grid[coord[0]][coord[1]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                dfs(grid, i, j, colour, c)
    return grid


def dfs(grid, x, y, colour, target):
    grid[x][y] = colour
    x_neighbours = [-1, -1, 0, 0, 1, 1, 1, -1]
    y_neighbours = [-1, 1, 1, -1, 1, -1, 0, 0]
    for i in range(8):
        new_x = x + x_neighbours[i]
        new_y = y + y_neighbours[i]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == target:
            dfs(grid, new_x, new_y, colour, target)


def main():
    grid = [["B", "B", "W"], ["W", "W", "W"], ["W", "W", "W"], ["B", "B", "B"]]
    assert colour_fill(grid, (2, 2), 'G') == [["B", "B", "G"], ["G", "G", "G"], ["G", "G", "G"], ["B", "B", "B"]]


if __name__ == '__main__':
    main()
