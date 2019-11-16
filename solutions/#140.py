def find_duplicates(nums):
    xor = nums[0]
    x = 0
    y = 0
    for num in nums[1:]:
        xor ^= num
    """
    A xor A = 0 -> A xor B xor C xor A xor B xor D = C xor D
    """

    bit = xor & ~(xor - 1)
    """
        i.e xor(C xor D) = 110100-> 110100-1 = 110011-> ~110011 = 001100-> 110100 & 001100-> 000100 = right most 1.
        i.e xor(C xor D) = 110101-> 110101-1 = 110100 -> ~110100 = 001011 -> 110101 & 001011 = 000001 = right most 1
    
    """
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
