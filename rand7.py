from random import randint


def rand7():
    result = (5 * rand5()) + rand5() - 5
    if result < 22:
        return result % 7 + 1
    return rand7()


def rand5():
    return randint(1, 5)


def main():
    experiments = 10000
    resultdict = {x: 0 for x in range(1, 8)}
    for _ in range(experiments):
        number = rand7()
        resultdict[number] += 1

    for num in resultdict:
        resultdict[num] = resultdict[num] / experiments
        print(round(resultdict[num], 2))
        print(round(1 / 7, 2))
        assert round(resultdict[num], 2) == round(1 / 7, 2)


if __name__ == '__main__':
    main()
