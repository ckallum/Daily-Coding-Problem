import heapq
from cmath import inf


def n_logn_min_count(n):
    if not n:
        return 0
    count = 0
    coins = [1, 25, 10, 5]
    heapq._heapify_max(coins)
    current = inf
    while n > 0:
        print(n)
        while current > n:
            if not coins:
                return 0
            current = heapq._heappop_max(coins)
        n -= current
        count += 1
    return count


def min_count(n):
    coin_dict = [inf for _ in range(n + 1)]
    coin_dict[0] = 0
    coins = [1, 25, 10, 5]
    for i in range(1, n + 1):
        for j in range(len(coins)):
            if coins[j] <= i and coin_dict[i-coins[j]] != inf:
                coin_dict[i] = min(1 + coin_dict[i-coins[j]], coin_dict[i])
    print(coin_dict[n])
    return coin_dict[n]


def main():
    assert min_count(16) == 3
    assert min_count(25) == 1
    assert min_count(126) == 6


if __name__ == '__main__':
    main()
