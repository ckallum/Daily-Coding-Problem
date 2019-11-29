import math
from collections import defaultdict


def get_majority_element(nums):
    if not nums:
        return None
    counter = defaultdict(int)
    bound = math.floor(len(nums)/2)
    for num in nums:
        counter[num] += 1
        if counter[num] > bound:
            return num
    return None


def main():
    assert get_majority_element([]) == None
    assert get_majority_element([0]) == 0
    assert get_majority_element([0, 2, 2]) == 2
    assert get_majority_element([1, 2, 1, 1, 3, 4, 1]) == 1


if __name__ == '__main__':
    main()
