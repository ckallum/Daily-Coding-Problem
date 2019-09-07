from collections import Counter
from random import randint

"""
The goal is to use rand5() to get equal chances of resulting in values between 1 - 21 
inclusive so that the results of: ((1 - 21) mod 7) + 1 have uniform probability of 
happening which also means the values between 1-7 have uniform probability.

The probability of the results of the equation: ((1- 21) mod 7) + 1:
1((mod7) + 1): 7, 14, 21 = 3/21 = 1/7
2((mod7) + 1): 1, 8, 15 = 3/21 = 1/7 etc...

5*rand5(): result has 1/5 chance
rand5(): result has 1/5 chance

5*rand5() + rand5() = 1/5*1/5 = 1/25 chance for each result. 
-5: brings result in range where the result is guaranteed to be between 1 - 25

if the result is larger than 22 we disregard it and roll again by calling it recursively, this doesn't effect
the probability as each experiment is unconditional on each other so each new experiment
is treated as the first one.

"""


def rand7():
    result = (5 * rand5()) + rand5() - 5
    if result < 22:
        return result % 7 + 1
    return rand7()


def rand5():
    return randint(1, 5)


def main():
    experiments = 10000
    result_dict = Counter(rand7() for _ in range(experiments))

    for num in result_dict:
        result_dict[num] = result_dict[num] / experiments
        print(round(result_dict[num], 2))
        print(round(1 / 7, 2))
        assert round(result_dict[num], 2) == round(1 / 7, 2)


if __name__ == '__main__':
    main()
