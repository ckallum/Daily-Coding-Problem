from functools import wraps


def collatz_sequence(num):
    count = 0
    r = num
    while num > 1:
        if num % 2:
            num = (3 * num) + 1

        else:
            num /= 2
        count += 1
    return count, r


def largest_collatz():
    res = 0
    m = 0
    for i in range(1000001):
        r = collatz_sequence(i)
        if r[0] > m:
            res = r[1]
            m = r[0]

    return res


def memo(f):
    f.cache = {}
    @wraps(f)
    def _f(*args):
        if args not in f.cache:
            f.cache[args] = f(*args)
        return f.cache[args]

    return _f


@memo
def collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz(n / 2)
    if n % 2 == 1:
        return 1 + collatz(3 * n + 1)


def dp_collatz(n):
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        value = i
        count = 0
        sp = False
        while not sp:
            if value % 2:
                value = (3 * value) + 1
            else:
                value //= 2

            count += 1
            if value < i and dp[value] > 0:
                sp = True
        dp[i] = count + dp[value]
    return list(max(enumerate(dp), key=lambda x: x[1]))[0]


def main():
    assert largest_collatz() == 837799
    assert max(range(1, 10 ** 6), key=collatz) == 837799
    assert dp_collatz(1000000) == 837799


if __name__ == '__main__':
    main()
