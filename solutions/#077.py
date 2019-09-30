def sort_intervals(x):
    return x[0]


"""
 As we have sorted the intervals by start time, each new interval is guaranteed to be merged into
 the last interval in the merged interval list or appended to it.
 - The start time of the last interval in the merged list is guaranteed to start after the interval
 previous to it in the list finishes. Therefore the next interval we are comparing will start after
 that previous interval finishes and can never be merged or merge it. This means we only need to compare
 the last merged interval and the current interval we are on. 

"""


def merge_overlaps(intervals):
    sorted_intervals = sorted(intervals, key=sort_intervals)
    current = 0
    merged = [sorted_intervals[0]]
    max_end = sorted_intervals[0][1]
    for start, end in sorted_intervals[1:]:
        if not end < max_end:
            if start < merged[current][1]:
                merged[current] = (merged[current][0], end)
            else:
                merged.append((start, end))
                max_end = end
                current += 1
    return merged


def main():
    assert merge_overlaps([(1, 3), (5, 8), (4, 10), (20, 25)]) == [
        (1, 3), (4, 10), (20, 25)]
    assert merge_overlaps([(1, 3), (5, 8), (4, 10), (20, 25), (6, 12)]) == [
        (1, 3), (4, 12), (20, 25)]


if __name__ == '__main__':
    main()
