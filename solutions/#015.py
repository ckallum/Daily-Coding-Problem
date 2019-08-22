import random
# Equation from https://stackoverflow.com/questions/23351918/select-an-element-from-a-stream-with-uniform-distributed-probability

class Stream(object):
    def __init__(self):
        self.stream = [random.randint(0, 1000) for _ in range(100000)]

    def getNext(self):
        return self.stream.pop()


def pickRandom():
    stream = Stream()
    inc = 0
    current = stream.getNext()
    res = None
    while current:
        inc += 1
        probability = random.choice([x for x in range(1, inc+1)])
        if probability == inc:
            res = current
        current = stream.getNext()
        print(res)
    return res


def main():
    r = pickRandom()
    print(r)


if __name__ == '__main__':
    main()
