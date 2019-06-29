from functools import reduce

def solution(l):
    ret = []
    total = int(reduce(lambda x, y:x*y, l))
    for x in l:
        ret.append(total//x)
    return ret


def main():
    l = [2,3,4,1,3,4,6,7]
    ret = solution(l)
    print(ret)


if __name__ == '__main__':
    main()
