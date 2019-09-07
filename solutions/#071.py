from collections import Counter
from random import randint


def rand7():
    return randint(1, 7)


def rand5():
    result = rand7()
    while result > 5:
        result = rand7()
    return result


def main():
    experiments = 10000
    result_dict = Counter(rand5() for _ in range(experiments))
    probability = 0.2

    for number in result_dict:
        result_dict[number] /= experiments
        assert round(result_dict[number], 1) == probability


if __name__ == '__main__':
    main()
