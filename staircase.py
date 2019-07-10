from collections import defaultdict
# Dynamic programming string partitioning -> fibonacci-> problem solving and edge cases with multiple step values


def steps(n):
    stepsDict = defaultdict()
    stepsDict[0], stepsDict[1] = 1, 1
    for x in range(2, n + 1):
        stepsDict[x] = stepsDict[x - 1] + stepsDict[x - 2]

    return stepsDict[n]


def variedSteps(n, lst):
    stepsDict = [0 for _ in range(n + 1)]
    stepsDict[0] = 1
    for x in range(1, n + 1):
        if x < min(lst):
            stepsDict[x] = 0
        else:
            for step in lst:
                if x >= step and stepsDict[x - step] != 0:
                    stepsDict[x] += stepsDict[x - step]
    return stepsDict[n]


def main():
    i = input('How many steps')
    print(steps(i))
    print(variedSteps(i, [1, 2, 3]))


if __name__ == '__main__':
    main()
