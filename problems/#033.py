def median(stream):
    medians = []
    values = []
    for value in stream:
        values.append(value)
        values.sort()
        if len(values) % 2 == 0:
            mid = int(len(values)/2)
            medians.append((values[mid]+values[mid-1])/2)
        else:
            medians.append(values[int(len(values)/2)])
    print(medians)
    return medians


def main():
    stream = [2, 1, 5, 7, 2, 0, 5]
    assert median(stream) == [2, 1.5, 2, 3.5, 2, 2, 2]


if __name__ == '__main__':
    main()
