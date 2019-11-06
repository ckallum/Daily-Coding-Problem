from cmath import inf


def stock_market(prices, k):
    profit = [[0 for _ in range(len(prices)+1)] for _ in range(k)]
    for i in range(0, k):
        prev_diff = -inf
        for j in range(1, len(prices)):
            prev_diff = max(prev_diff, profit[i-1][j-1]-prices[j-1])
            profit[i][j] = max(profit[i][j-1], prev_diff+prices[j])
    return profit[k-1][len(prices)-1]


def main():
    assert stock_market([5, 2, 4, 0, 1], 2) == 3
    assert stock_market([0, 1, 0, 2, 0, 3, 0, 4], 2) == 7
    assert stock_market([0, 1, 0, 2, 0, 3, 0, 4], 3) == 9
    assert stock_market([4, 2], 1) == 0


if __name__ == '__main__':
    main()
