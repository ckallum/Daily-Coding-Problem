import heapq


def k_closest(points, centre, k):
    values = [(((x[0] - centre[0]) ** 2 + (x[1] - centre[1]) ** 2), x) for x in points]
    results = []
    for _ in range(k):
        min_d = heapq.heappop(values)
        results.append(min_d[1])
    print(results)
    return results


def main():
    assert k_closest([(0, 0), (5, 4), (3, 1)], (1, 2), 2) == [(0, 0), (3, 1)]


if __name__ == '__main__':
    main()
