from cmath import inf
from collections import deque


def longest_distinct_subarray(nums):
    current = deque()
    length = -inf
    for num in nums:
        while num in current:
            current.popleft()
        current.append(num)
        length = max(length, len(current))
    print(length)
    return length


def main():
    assert longest_distinct_subarray([5, 1, 3, 5, 2, 3, 4, 1]) == 5


if __name__ == '__main__':
    main()
