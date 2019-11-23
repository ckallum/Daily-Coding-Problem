def preprocess(nums):
    for index, num in enumerate(nums):
        if index > 0:
            nums[index] += nums[index - 1]
    return nums


def find_sum(nums, i, j):
    return nums[j - 1] - nums[i - 1]


def index_sum(nums, i, j):
    nums = preprocess(nums)
    return find_sum(nums, i, j)


def main():
    assert index_sum([1, 2, 3, 4, 5], 1, 3) == 5


if __name__ == '__main__':
    main()
