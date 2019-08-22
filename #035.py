def rgb(rgbs):
    left = 0
    right = len(rgbs) - 1
    while True:
        while rgbs[left] == 'R' and left < right:
            left += 1
        while rgbs[right] != 'R' and left < right:
            right -= 1
        if left >= right:
            break
        rgbs[left], rgbs[right] = rgbs[right], rgbs[left]
    right = len(rgbs) - 1
    while True:
        while rgbs[left] == 'G' and left < right:
            left += 1
        while rgbs[right] != 'G' and left < right:
            right -= 1
        if left >= right:
            break
        rgbs[left], rgbs[right] = rgbs[right], rgbs[left]
    return rgbs


def main():
    rgbs = ['R', 'G', 'B', 'G', 'R', 'R', 'B']
    assert rgb(rgbs) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']


if __name__ == '__main__':
    main()
