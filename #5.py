# Understanding python function returns


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    return f(lambda x, y: x)


def cdr(f):
    return f(lambda x, y: y)


def main():
    assert (car(cons(2, 3))) == 2
    assert (cdr(cons(2, 3))) == 3


if __name__ == '__main__':
    main()
