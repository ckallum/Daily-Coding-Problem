from collections import deque

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    def left(a, b):
        return a
    return f(left)


def cdr(f):
    def right(a, b):
        return b
    return f(right)


def main():
    print(cons(2, 3))
    print(car(cons(2, 3)))
    print(cdr(cons(2, 3)))


if __name__ == '__main__':
    main()
