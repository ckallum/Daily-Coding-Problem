def find_minimum_steps(points):
    x, y = points[0]
    return find_minimum_steps_helper(points[1:], (x, y),0)


def get_min_distance(current, next_point, total_distance):
    x1, y1 = current
    x2, y2 = next_point

    x_diff = x2 - x1
    y_diff = y2 - y1
    if x_diff == 0:
        return total_distance + abs(y_diff)
    if y_diff == 0:
        return total_distance + abs(x_diff)

    new_current = ((x1 + (int(x_diff / abs(x_diff)))), (y1 + (int(y_diff / abs(y_diff)))))
    return get_min_distance(new_current, next_point,
                            1 + total_distance)


def find_minimum_steps_helper(points, current, total):
    if not points:
        return total
    next_point = points[0]
    min_distance = get_min_distance(current, next_point, 0)

    return find_minimum_steps_helper(points[1:], next_point, total + min_distance)


def main():
    assert find_minimum_steps([(0, 0), (1, 1), (1, 2)]) == 2
    assert find_minimum_steps([(0, 0), (2, 2), (2, 3)]) == 3


if __name__ == '__main__':
    main()
