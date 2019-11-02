def towers_of_hanoi(source, helper, target, n):
    if n > 0:
        towers_of_hanoi(source, target, helper, n - 1)
        if source:
            target.append(source.pop())
        towers_of_hanoi(helper, source, target, n - 1)
    return target


def main():
    print(towers_of_hanoi([4, 3, 2, 1], [], [], 4))


if __name__ == '__main__':
    main()
