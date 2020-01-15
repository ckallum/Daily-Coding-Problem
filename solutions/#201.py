def max_list_path(numbers):
    return helper(numbers, 0, 1, [numbers[0][0]], numbers[0][0])[0]


def helper(numbers, index, level, path, path_val):
    if level == len(numbers):
        return path, path_val
    left = helper(numbers, index, level+1, path+[numbers[level][index]], path_val+numbers[level][index])
    right = helper(numbers, index+1, level+1, path+[numbers[level][index+1]], path_val+numbers[level][index+1])
    if left[1] > right[1]:
        return left
    else:
        return right


def main():
    assert max_list_path([[1], [2, 3], [1, 5, 1]]) == [1, 3, 5]
    assert max_list_path([[1], [2, 3], [7, 5, 1]]) == [1, 2, 7]


if __name__ == '__main__':
    main()
