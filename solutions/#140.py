def find_duplicates(nums):
    xor = nums[0]
    x = 0
    y = 0
    for num in nums[1:]:
        xor ^= num

    bit = xor & ~(xor - 1)
    for num in nums:
        if num & bit:
            x ^= num
        else:
            y ^= num
    return x, y


def main():
    assert find_duplicates([2, 4, 6, 8, 10, 2, 6, 10]) == (4, 8)


if __name__ == '__main__':
    main()
