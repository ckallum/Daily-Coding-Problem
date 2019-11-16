def increment_row(grid, x, y, y_bound):
    return all(grid[x][y:y_bound])


def increment_col(grid, x, x_bound, y):
    for i in range(x, x_bound):
        if not grid[i][y]:
            return False
    return True


def area_helper(grid, x, x_bound, y, y_bound):
    current_area = (x_bound - x) * (y_bound - y)
    row_inc, col_inc = 0, 0
    r_inc = x_bound < len(grid) and increment_row(grid, x_bound, y, y_bound)
    if r_inc:
        row_inc = area_helper(grid, x, x_bound + 1, y, y_bound)
    c_inc = y_bound < len(grid[0]) and increment_col(grid, x, x_bound, y_bound)
    if c_inc:
        col_inc = area_helper(grid, x, x_bound, y, y_bound + 1)
    return max(current_area, row_inc, col_inc)


def find_rectangle(grid):
    max_area = 0
    num_cols = len(grid[0])
    num_rows = len(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            area_bound = (num_rows - x) * (num_cols - y)
            if area_bound > max_area and grid[x][y]:
                possible_area = area_helper(grid, x, x + 1, y, y + 1)
            max_area = possible_area if possible_area > max_area else max_area
    print(max_area)
    return max_area


def main():
    assert find_rectangle([[1, 0, 0, 0],
                           [1, 0, 1, 1],
                           [1, 0, 1, 1],
                           [0, 1, 0, 0]]) == 4


if __name__ == '__main__':
    main()
