

"""
Proof: Each element's final position from positions n-1 to 0 has a probability of 1/(it's index) =
1/n * 1/n-1 ... 1/1 = 1/(n!)
which means the total probability of a single permutation = 1/(n!) which is correct as there is a total of
n! permutations so each permutation should have equal probability/

"""


from random import randint


def shuffle():
    cards = list(range(52))
    for i in range(52, 0, -1):
        newindex = randint(0, i+1)
        temp = cards[i]
        cards[i] = cards[newindex]
        cards[newindex] = temp
    return cards


def main():
    for _ in range(10):
        assert all(x in shuffle() for x in range(52))


if __name__ == '__main__':
    main()
