import heapq
from cmath import inf


def min_count(n):
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


def main():
    assert min_count(16) == 3
    assert min_count(25) == 1
    assert min_count(126) == 6


if __name__ == '__main__':
    main()
