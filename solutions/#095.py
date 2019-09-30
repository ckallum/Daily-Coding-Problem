def next_lexographic_number(numbers):
    for index in range(len(numbers) - 1, -1, -1):
        if index > 0 and numbers[index] > numbers[index - 1]:
            break

    if index == 0:
        numbers.reverse()
    else:
        for i in range(len(numbers) - 1, index - 1, -1):
            if numbers[i] > numbers[index - 1]:
                temp = numbers[i]
                numbers[i] = numbers[index - 1]
                numbers[index - 1] = temp
                break

        tail = numbers[index:]
        tail.reverse()
        numbers[index:] = tail

    return numbers


def main():
    assert next_lexographic_number([1, 2, 3]) == [1, 3, 2]
    assert next_lexographic_number([1, 3, 2]) == [2, 1, 3]
    assert next_lexographic_number([3, 2, 1]) == [1, 2, 3]


if __name__ == '__main__':
    main()
