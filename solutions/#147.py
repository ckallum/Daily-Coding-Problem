def reverse(lst, i, j):
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst


def reverse_sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                reverse(nums, i, j)
    return nums


def main():
    assert reverse_sort([1, 4, 3, 5, 6, 1, 2, 4]) == [1, 1, 2, 3, 4, 4, 5, 6]


if __name__ == '__main__':
    main()
