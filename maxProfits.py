from math import inf


def maxProfits(prices):
    maxprof = -inf
    left = 0
    for index, price in enumerate(prices):
        if price - prices[left] > maxprof:
            maxprof = price - prices[left]
        elif price < prices[left]:
            left = index

    return maxprof


def main():
    prices = [9, 11, 8, 12, 5, 7, 10]
    assert maxProfits(prices) == 5


if __name__ == '__main__':
    main()
