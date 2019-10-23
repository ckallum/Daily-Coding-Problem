def square_and_sort(numbers):
    numbers = sorted(list(map(lambda x: x*x, numbers)))
    return numbers


def main():
    assert square_and_sort([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]


if __name__ == '__main__':
    main()