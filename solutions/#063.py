def word_search(grid, word):
    found_in_col = False
    found_in_row = False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == word[0]:
                if len(grid)-row >= len(word):
                    found_in_col = find_in_col(grid, row, col, word)
                if len(grid[0]) - col >= len(word):
                    found_in_row = find_in_row(grid,row,col,word)
            if found_in_col or found_in_row:
                return True
    return False


def find_in_row(grid, row, col, word):
    if "".join(grid[row][col:col + len(word)]) == word:
        return True
    return False


def find_in_col(grid, row, col, word):
    assemble = ""
    for i in range(row, row + len(word)):
        assemble += grid[i][col]
    if assemble == word:
        return True
    return False


def main():
    grid = [['F', 'A', 'C', 'I'],
            ['O', 'B', 'Q', 'P'],
            ['A', 'N', 'O', 'B'],
            ['M', 'A', 'S', 'S']]

    assert word_search(grid, "FOAM")
    assert word_search(grid, "MASS")


if __name__ == '__main__':
    main()
