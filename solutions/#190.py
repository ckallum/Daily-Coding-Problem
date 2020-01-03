def max_subarray_sum(array):
    current = 0
    for num in array:
        current = max(current, current + num)
    return current


def main():
    assert max_subarray_sum([8, -1, 3, 4]) == 15
    assert max_subarray_sum([-4, 5, 1, 0]) == 6


if __name__ == '__main__':
    main()
