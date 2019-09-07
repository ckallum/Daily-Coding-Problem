from collections import Counter
from random import randint


def rand7():
    return randint(1, 7)


"""
Each result of rand7() has a probability of 1/7. This also means that if you trim the results to only be valid 
if in the range 1-5, each value (1,2,3,4,5) also has the probability of 1/7 to occur and therefore all of them
have uniform probability of happening. 

As each new test is independent of each other, we can just treat every experiment as a new one as they are 
unconditional of each other. This means we can continuously retry the experiment by calling it recursively if the 
result is outside the range 1-5 where each result between 1-5 has uniform probability of occurring.
"""


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
