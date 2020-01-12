def max_multiple_subset(nums, prev=1, index=0, current=[]):
    if index == len(nums):
        return current
    num = nums[index]
    one = max_multiple_subset(nums, prev, index + 1, current)
    if num % prev == 0:
        two = max_multiple_subset(nums, num, index + 1, current + [num])
        return two if len(two) > len(one) else one
    return one


def main():
    assert max_multiple_subset([3, 5, 10, 20, 21]) == [5, 10, 20]
    assert max_multiple_subset([1, 3, 6, 24]) == [1, 3, 6, 24]


if __name__ == '__main__':
    main()
