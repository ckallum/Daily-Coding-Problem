def count_islands(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                is_island = True
                neighbours = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col), (row - 1, col - 1),
                              (row + 1, col + 1), (row - 1, col + 1), (row + 1, col - 1)]
                for r, c in neighbours:
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        if grid[r][c] == 1:
                            grid[r][c] = -1
                        elif grid[r][c] == -1:
                            is_island = False
                if is_island:
                    count += 1
            print_grid(grid)
    return count


def print_grid(grid):
    for row in range(len(grid)):
        print(grid[row], end="\n")
    print("\n")


def main():
    assert count_islands([[1, 0, 0, 0, 0],
                          [0, 0, 1, 1, 0],
                          [0, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0],
                          [1, 1, 0, 0, 1],
                          [1, 1, 0, 0, 1]]) == 4


if __name__ == '__main__':
    main()
