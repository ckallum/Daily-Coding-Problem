from collections import deque
from copy import copy


def get_len(x):
    return len(x)


def longest_subsequence(numbers):
    subsequences = [[numbers[0]]]
    for num in numbers[1:]:
        additional_sequences = []
        for index, subsequence in enumerate(subsequences):
            if num > max(subsequence):
                subsequences[index].append(num)
            else:
                temp = copy(subsequence)
                while num <= temp[len(temp) - 1]:
                    temp.pop()
                temp.append(num)
                if temp not in (subsequences and additional_sequences):
                    additional_sequences.append(temp)
        subsequences.extend(additional_sequences)
    subsequences = list(sorted(subsequences, key=get_len))[::-1]

    return len(subsequences[0])


def main():
    assert longest_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6


if __name__ == '__main__':
    main()
