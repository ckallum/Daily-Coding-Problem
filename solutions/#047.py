from math import inf


def maxProfits(prices):  # Each time their is a new low buy in price, we shift the buy in point to see if there is
                         # better buy, sell window after that time as we always want to buy at it lowest price.
    maxprof = -inf
    buy = 0
    sell = 0
    for index, price in enumerate(prices):
        if price - prices[buy] > maxprof:
            maxprof = price - prices[buy]
            sell = index
        elif price < prices[buy]:
            buy = index

    return "Buy at: " + str(prices[buy]) + ", Sell at: " + str(prices[sell])


def main():
    prices = [9, 11, 8, 12, 5, 7, 10]
    assert maxProfits(prices) == "Buy at: 5, Sell at: 10"


if __name__ == '__main__':
    main()
