def reverse_polish(equation):
    num_stack = list()
    operations = {"*": lambda x, y: x * y,
                  "/": lambda x, y: x / y,
                  "-": lambda x, y: x - y,
                  "+": lambda x, y: x + y}

    for char in equation:
        if char in operations:
            if len(num_stack) < 2:
                return None
            res = operations[char](num_stack.pop(), num_stack.pop())
            num_stack.append(res)
        else:
            num_stack.append(char)
    return num_stack.pop()


def main():
    assert reverse_polish([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5


if __name__ == '__main__':
    main()
