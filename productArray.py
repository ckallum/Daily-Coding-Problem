# List traversal brain teaser


from functools import reduce


def solution(l):
    ret = []
    total = int(reduce(lambda x, y: x*y, l))
    for x in l:
        ret.append(total//x)
    return ret


def noDivideSolution(l):
    prod = 1
    fromLeft = []
    for x in l:
        prod *= x
        fromLeft.append(prod)

    prod = 1
    fromRight = []
    for x in l[::-1]:
        prod *= x
        fromRight.append(prod)

    fromRight = fromRight[::-1]

    out = []
    for x in range(len(l)):
        if x == 0:
            num = fromRight[x+1]
        elif x == len(l)-1:
            num = fromLeft[x-1]
        else:
            num = fromRight[x+1] * fromLeft[x-1]

        out.append(num)
    return out


def minSpaceSol(l):
    temp = 1
    arr = [1 for x in l]

    for i in range(len(l)):
        arr[i] = temp
        temp *= l[i]

    temp = 1

    for i in range(len(l)-1, -1, -1):
        arr[i] *= temp
        temp *= l[i]

    return arr


def main():
    ls = [2, 3, 4, 1, 3, 4, 6, 7]
    ret = solution(ls)
    r = noDivideSolution(ls)
    eff = minSpaceSol(ls)
    print(ret)
    print(r)
    print(eff)


if __name__ == '__main__':
    main()
