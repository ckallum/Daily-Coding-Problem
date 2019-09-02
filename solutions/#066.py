"""
https://medium.com/@hjegeorge/interview-question-1-a-biased-coin-toss-9dc2af96321
- We don't know which side the coins bias is on:
However, if we flip the coin twice, as each flip is not conditional on each other, the probability of getting heads then tails
and tails then heads is equal no matter what side the coins is biased on.
e.g if the coin gives 70% probability of heads then:
 - landing heads then tails is 0.7 * 0.3 = 0.21
 - landing tails then heads is 0.3 * 0.7 = 0.21
 As both are just as likely then if we get alternative results from the two flips then we can just take the the result
 of the first flip as the result as it's just as likely to get heads on the first flip as tails on the first flip based
 on the condition the results of both flips are different.

 If both flips are the same, it doesn't tell us anything as we can't derive any probability from getting it as we
 don't know the bias. This means we discount that trial and do it again as if it didn't happen, we can do this
 as the first trial doesn't impact the second trial.



"""

from random import random


def bias_flip():
    rand = random()
    return 0 if rand < 0.7 else 1


def get_un_bias_flip():
    result1 = bias_flip()
    result2 = bias_flip()
    if result1 != result2:
        return result1
    else:
        return get_un_bias_flip()


def un_bias_flip():
    experiments = 100000
    biased_result = {1: 0, 0: 0}
    unbiased_results = {1: 0, 0: 0}
    for i in range(experiments):
        result = bias_flip()
        biased_result[result] += 1
        result2 = get_un_bias_flip()
        unbiased_results[result2] += 1

    for key in biased_result:
        biased_result[key] /= experiments
        biased_result[key] = round(biased_result[key], 2)

    for key in unbiased_results:
        unbiased_results[key] /= experiments
        unbiased_results[key] = round(unbiased_results[key], 2)
    return biased_result[0], biased_result[1], unbiased_results[0], unbiased_results[1]


def main():
    assert un_bias_flip() == (0.7, 0.3, 0.5, 0.5)


if __name__ == '__main__':
    main()
