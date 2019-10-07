def find_consecutive_sequence(numbers, k):
    numbers_dict = {number: [(i, number)] for i, number in enumerate(numbers) if number <= k}
    for i in range(k + 1):
        for index, number in enumerate(numbers):
            if i - number in numbers and (index, number) not in numbers_dict[i - number]:
                numbers_dict[i] = numbers_dict[i - number] + [(index, number)]
    return [number[1] for number in numbers_dict[k]]


def main():
    assert find_consecutive_sequence([1, 2, 3, 4, 5, 2], 10) == [1, 4, 5]


if __name__ == '__main__':
    main()
