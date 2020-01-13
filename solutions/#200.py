def interval_stab(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    for start, end in intervals:
        if not result or start != result[-1]:
            result.append(end)
    return result


def main():
    assert interval_stab([(1, 4), (4, 5), (7, 9), (9, 12)]) == [4, 9]


if __name__ == '__main__':
    main()
