def interval_stab(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    result = set()
    for start, end in intervals:
        if not result or start not in result:
            result.add(end)
    return list(result)


def main():
    assert interval_stab([(1, 4), (4, 5), (7, 9), (9, 12)]) == [9, 4]


if __name__ == '__main__':
    main()
