from cmath import inf


def gcd(nums):
    current = 1
    for i in range(1, min(nums) + 1):
        if all([x % i == 0 for x in nums]) and i > current:
            current = i
    return current


def main():
    assert gcd([42, 56, 14]) == 14


if __name__ == '__main__':
    main()
