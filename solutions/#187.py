def overlapping_rectangles(rectangles):
    for rectangle in range(len(rectangles)):
        rectangles[rectangle]["bottom_right"] = (
            rectangles[rectangle]["top_left"][0] + rectangles[rectangle]["dimensions"][0],
            rectangles[rectangle]["top_left"][1] + rectangles[rectangle]["dimensions"][1])
    for i, rectangle in enumerate(rectangles):
        for j, rectangle2 in enumerate(rectangles[i + 1:], start=i + 1):
            if overlaps(rectangle, rectangle2) or overlaps(rectangle2, rectangle):
                return True
    return False


def overlaps(rectangle1, rectangle2):
    return rectangle1["top_left"][0] <= rectangle2["top_left"][0] and rectangle1["top_left"][1] >= \
           rectangle2["top_left"][1] and rectangle1["bottom_right"][0] > rectangle2["top_left"][0] and \
           rectangle1["bottom_right"][1] > rectangle2["top_left"][1]


def main():
    assert overlapping_rectangles([{
        "top_left": (1, 4),
        "dimensions": (3, 3)  # width, height
    },
        {
            "top_left": (-1, 3),
            "dimensions": (2, 1)
        },
        {
            "top_left": (0, 5),
            "dimensions": (4, 3)
        }])


if __name__ == '__main__':
    main()
