# Function is broken because each new call of the function lambda get's passed in the current local value
# of i which is fixed at 9.


def faulty_function():
    functions = []
    result = []
    for i in range(10):
        functions.append(lambda: i)

    for f in functions:
        result.append(f())
    return result


def fixed_function():
    functions = []
    result = []
    for i in range(10):
        functions.append(lambda: i)
    i = 0
    for f in functions:
        result.append(f())
        i += 1
    return result


def main():
    assert faulty_function() == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    assert fixed_function() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    main()
