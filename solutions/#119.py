def find_set(intervals):
    intervals = sorted(intervals)
    result = set()
    for start, end in intervals:
        if start not in result:
            result.add(end)
    return result


def main():
    assert find_set([[0, 3], [2, 6], [3, 4], [6, 9]]) == {3, 6}
    assert find_set([[0, 3], [2, 6], [1, 2], [3, 9]]) == {2, 3}


if __name__ == '__main__':
    main()
