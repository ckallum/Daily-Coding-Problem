# intution is we want to be able to start a new task as soon as possible so it doesn't matter
# when we start the task as long as we finish as soon as possible->sort by finishing time
# even if a task starts earlier, we won't be able to add a new task if it finishes later
# which is why we don't want to sort/prioritise by start time.
# i.e. if the next task is feasible to be added on the earlier start time it will also be feasible for the later start
# time since the later start time has an earlier finish. -> added either way.


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
