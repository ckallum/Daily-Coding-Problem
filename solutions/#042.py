def find(numbers, k):
    sumsubset = {x: list() for x in range(k + 1)}
    for index, num in enumerate(numbers):
        sumsubset[num] = [(num, index)]
    for x in range(k + 1):
        for index, num in enumerate(numbers):
            if x - num in sumsubset and sumsubset[x - num]:
                if (num, index) not in sumsubset[x-num] :
                    sumsubset[x] = sumsubset[x - num] + [(num, index)]
    result = [x[0] for x in sumsubset[24]]
    return result


def main():
    assert find([12, 1, 61, 5, 9, 2], 24) == [1, 12, 9, 2]


if __name__ == '__main__':
    main()
