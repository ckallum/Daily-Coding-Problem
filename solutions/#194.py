def get_intersections(y1, y2):
    segments = list(zip(y1, y2))
    print(segments)
    count = 0
    for i in range(len(segments)):
        for j in range(i):
            p, q = segments[i], segments[j]
            if (p[0] < q[0] and p[1] > q[1]) or (q[0] < p[0] and q[1] > p[1]):
                count += 1
    return count


def main():
    assert get_intersections([1, 4, 5], [4, 2, 3]) == 2
    assert get_intersections([1, 4, 5], [2, 3, 4]) == 0


if __name__ == '__main__':
    main()
