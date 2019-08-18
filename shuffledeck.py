from random import randint


def shuffle():
    cards = list(range(52))
    for i in range(52):
        newindex = i + randint(0, 52 - i - 1)
        temp = cards[i]
        cards[i] = cards[newindex]
        cards[newindex] = temp
    return cards


def main():
    for _ in range(10):
        assert all(x in shuffle() for x in range(52))


if __name__ == '__main__':
    main()
