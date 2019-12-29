def rectangle_intersection(rec1, rec2):
    rec1["bottom_right"] = (rec1["top_left"][0] + rec1["dimensions"][0], rec1["top_left"][1] + rec1["dimensions"][1])
    rec2["bottom_right"] = (rec2["top_left"][0] + rec2["dimensions"][0], rec2["top_left"][1] + rec2["dimensions"][1])
    print(rec1, rec2)
    if rec1["top_left"][0] > rec2["bottom_right"][0] or rec1["top_left"][1] > rec2["bottom_right"][1] or rec2["top_left"][0] > rec1["bottom_right"][0] or rec2["top_left"][1] > rec1["bottom_right"][1]:
        return 0
    area = (min(rec1["bottom_right"][0], rec2["bottom_right"][0])-max(rec1["top_left"][0], rec2["top_left"][0])) * (min((rec1["bottom_right"][1], rec2["bottom_right"][1])) - max(rec1["top_left"][1], rec2["top_left"][1]))
    print(area)
    return area


def main():
    rec1 = {
        "top_left": (1, 4),
        "dimensions": (3, 3)  # width, height
    }
    rec2 = {
        "top_left": (0, 5),
        "dimensions": (4, 3)  # width, height
    }
    assert rectangle_intersection(rec1, rec2) == 6


if __name__ == '__main__':
    main()
