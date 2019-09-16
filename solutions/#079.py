def convert_to_non_decreasing(numbers):
    count = 0
    for index, number in enumerate(numbers):
        if index + 1 < len(numbers):
            if number > numbers[index + 1]:
                count += 1
        if count > 1:
            return False

    return True


def main():
    assert convert_to_non_decreasing([10, 5, 7])
    assert not convert_to_non_decreasing([10, 7, 5])


if __name__ == '__main__':
    main()
