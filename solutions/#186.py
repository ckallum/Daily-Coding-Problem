from cmath import inf


def helper(current_sum, seen, nums):
    if current_sum < 0:
        return seen, abs(current_sum)
    min_diff = current_sum
    indexes = seen
    for i, n in enumerate(nums):
        if i not in seen:
            r, d = helper(current_sum - nums[i], seen+[i], nums)
            if d < min_diff:
                min_diff = d
                indexes = r
    return indexes, min_diff


def smallest_difference_subset(nums):
    s = sum(nums)//2
    indexes = None
    min_diff = s
    for i, num in enumerate(nums):
        r, d = helper(s - num, [i], nums)
        if d <= min_diff:
            indexes = r
            min_diff = d
    result = [[], []]
    print(indexes, min_diff)
    for i, num in enumerate(nums):
        if i in indexes:
            result[0].append(num)
        else:
            result[1].append(num)
    print(result)
    return result


def main():
    assert smallest_difference_subset([5, 10, 15, 20, 25]) == [[10, 25], [5, 15, 20]]


if __name__ == '__main__':
    main()
