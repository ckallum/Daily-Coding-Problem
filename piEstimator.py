from random import randrange


def estimate():
    sigFigs = 1000
    inCircle = 0
    inSquare = 0
    for _ in range(sigFigs * sigFigs):
        randomX = randrange(sigFigs) / sigFigs
        randomY = randrange(sigFigs) / sigFigs
        rSquared = (randomX ** 2) + (randomY ** 2)
        if rSquared <= 1:
            inCircle += 1
        inSquare += 1

    pi = 4 * (inCircle / inSquare)
    print(pi)


def main():
    estimate()


if __name__ == '__main__':
    main()
