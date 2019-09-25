from random import randint


def get_random_value(n, numbers):
    possible_nums = []
    for number in range(0, n):
        if number not in numbers:
            possible_nums.append(number)
    return possible_nums[randint(0, len(possible_nums)-1)]


def main():
    iterations = 10000
    predictions_dict = {}
    n = 40
    numbers = [1, 4, 8, 5, 7, 6, 10, 29, 39]
    expected = round(1/(n-len(numbers)), 2)
    for _ in range(iterations):
        result = get_random_value(n, numbers)
        if result not in predictions_dict:
            predictions_dict[result] = 1
        else:
            predictions_dict[result] += 1

    for number in predictions_dict:
        assert round(predictions_dict[number]/iterations, 2) == expected


if __name__ == '__main__':
    main()
