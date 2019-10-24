def find_set(intervals):
    start_set = []
    end_set = []
    for start, end in intervals:
        if start not in start_set and start not in end_set:
            start_set.append(start)
            end_set.append(end)
        elif start in start_set and end not in end_set:
            end_set.append(end)
        elif start not in start_set and end in end_set:
            start_set.append(start)
    return set(start_set) if len(start_set) < len(end_set)else set(end_set)


def main():
    assert find_set([[0, 3], [2, 6], [3, 4], [6, 9]]) == {3, 6}
    assert find_set([[0, 3], [2, 6], [2, 4], [2, 9]]) == {0, 2}


if __name__ == '__main__':
    main()
