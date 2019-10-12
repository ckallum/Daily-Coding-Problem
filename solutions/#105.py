import time


def debounce(s):
    """
    Decorator ensures function that can only be called once every `s` seconds.
    """
    interval = s * (10 ** (-3))

    def decorate(f):
        current_time = None

        # A decorator allows us to take in a function f and wrap it in another function i.e. changing its behaviour
        # without modifying the function f itself.
        def wrapped(*args, **kwargs):
            # nonlocal changes the current_time in the outer function as long as it isn't global
            nonlocal current_time
            start_time = time.time()
            if current_time is None or start_time - current_time >= interval:
                result = f(*args, **kwargs)
                current_time = time.time()
                return result

        return wrapped

    return decorate


@debounce(3000)
# '@' function is used to decorate a function, i.e. wrap it into something else when it is called.
def add_nums(x, y):
    return x + y


def main():
    assert add_nums(1, 1) == 2
    time.sleep(1)
    assert not add_nums(1, 2)
    time.sleep(1)
    assert not add_nums(1, 3)
    time.sleep(1)
    assert add_nums(1, 4) == 5


if __name__ == '__main__':
    main()
