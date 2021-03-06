from collections import defaultdict
# Dynamic programming string partitioning -> fibonacci-> problem solving and edge cases with multiple step values


def twosteps(n):
    stepsDict = defaultdict()
    stepsDict[0], stepsDict[1] = 1, 1
    for x in range(2, n + 1):
        stepsDict[x] = stepsDict[x - 1] + stepsDict[x - 2]

    return stepsDict[n]


def variedSteps(n, possiblesteps):
    stepsDict = dict()
    stepsDict[0] = 1
    if n < min(lst):
        return 0
    for x in range(1, n + 1):
        stepsDict[x] = 0
        for step in possiblesteps:
            if x - step in stepsDict:
                stepsDict[x] += stepsDict[x - step]
        print("Number of ways to get to step", x, " ", stepsDict[x])
    return stepsDict[n]


def main():
    assert variedSteps(4, [1, 2]) == 5
    # assert variedSteps(5, [1, 2, 3]) == 13
    assert twosteps(4) == 5


if __name__ == '__main__':
    main()
