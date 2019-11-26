import bisect
from random import randint


def get_num(probability, probabilities, nums):
    recalculated = []
    accumulated_prob = 0
    for p in probabilities:
        recalculated.append(p + accumulated_prob)
        accumulated_prob += p
    print(probability, recalculated, bisect.bisect_left(recalculated, probability))
    return nums[bisect.bisect_left(recalculated, probability)]


def main():
    nums = [1, 2, 3, 4]
    probabilities = [0.1, 0.5, 0.2, 0.2]
    num_dict = {x: 0 for x in nums}
    for i in range(10000):
        probability = randint(0, 100) / 100
        num_dict[get_num(probability, probabilities, nums)] += 1
    for x in num_dict:
        assert round(num_dict[x] / 10000, 1) == probabilities[x - 1]


if __name__ == '__main__':
    main()
