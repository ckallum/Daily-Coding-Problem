from collections import deque


def count_smaller_elements_naive(numbers):
    for i in range(len(numbers)):
        temp = numbers[i]
        numbers[i] = 0
        for j in range(i + 1, len(numbers)):
            if numbers[j] < temp:
                numbers[i] += 1
    print(numbers)
    return numbers

#
# def count_smaller_elements(numbers):
#     numbers = list(sorted([(n, i) for i, n in enumerate(numbers)]))
#     result = [0] * len(numbers)
#     for index, tup in enumerate(numbers):
#         result[tup[1]] = index
#     print(result)
#     return result


def main():
    assert count_smaller_elements_naive([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
    # assert count_smaller_elements([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]


if __name__ == '__main__':
    main()
