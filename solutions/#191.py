def overlapping_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    current = intervals[0]
    count = 0
    for interval in intervals[1:]:
        if interval[0] < current[1]:
            count += 1
        else:
            current = interval
    return count


def main():
    assert overlapping_intervals([(7, 9), (2, 4), (5, 8)]) == 1
    assert overlapping_intervals([(7, 9), (2, 4), (5, 8), (1, 3)]) == 2


if __name__ == '__main__':
    main()
