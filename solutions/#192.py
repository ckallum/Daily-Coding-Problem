def reachable(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == 0:
            return False
        else:
            i += nums[i]
            if i == len(nums) - 1:
                return True
    return False


def main():
    assert reachable([1, 3, 1, 2, 0.1])
    assert not reachable([1, 2, 1, 0, 0])


if __name__ == '__main__':
    main()
