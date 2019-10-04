def find_longest_sequence(numbers):
    numbers_set = set(numbers)
    max_sequence = 0
    for number in numbers_set:
        if number - 1 not in numbers_set:
            current_num = number
            length = 1
            while current_num + 1 in numbers_set:
                length += 1
                current_num += 1
            max_sequence = max(max_sequence, length)

    return max_sequence


def main():
    assert find_longest_sequence([100, 4, 200, 1, 3, 2]) == 4


if __name__ == '__main__':
    main()
