def max_profit_with_fees(prices, fee):
    i = 0
    profit = 0
    while i < len(prices) - 1:
        while prices[i] > prices[i + 1]:
            i += 1
        if i == len(prices) - 1:
            break
        buy = prices[i]
        i += 1
        while i < len(prices) - 1 and prices[i]-fee < prices[i + 1]:
            i += 1
        sell = prices[i]
        i += 1
        print(buy, sell)
        if sell - fee - buy > 0:
            profit += sell - fee - buy
    print(profit)
    return profit


def main():
    assert max_profit_with_fees([1, 3, 2, 8, 4, 10], 2) == 9


if __name__ == '__main__':
    main()
