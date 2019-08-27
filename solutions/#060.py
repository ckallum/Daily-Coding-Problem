def can_partition(numbers):
    if sum(numbers) % 2 != 0:
        return None
    else:
        subset_sum = sum(numbers) // 2
        sum_partition = [[True for _ in range(len(numbers) + 1)] for _ in range(subset_sum + 1)]
        for i in range(1, subset_sum + 1):
            sum_partition[i][0] = False

        for i in range(1, subset_sum + 1):
            for j in range(1, len(numbers) + 1):
                sum_partition[i][j] = sum_partition[i][j - 1]
                if i >= numbers[j - 1]:
                    sum_partition[i][j] = sum_partition[i][j] or sum_partition[i - numbers[j - 1]][j - 1]

        return sum_partition[subset_sum][len(numbers)]


def main():
    assert can_partition([15, 5, 20, 10, 35, 15, 10])
    assert not can_partition([15, 5, 20, 10, 35])


if __name__ == '__main__':
    main()
