# Easy Window problem

class Log(object):
    def __init__(self, size):
        self.log = list()
        self.size = size

    def __repr__(self):
        return str(self.log)

    def record(self, order_id):
        self.log.append(order_id)
        if len(self.log) > self.size:
            self.log.pop(0)

    def getLast(self, i):
        return self.log[-i]


def main():
    log = Log(5)
    for x in range(10):
        log.record(x)
        print(repr(log))

    assert log.getLast(1) == 9
    assert log.getLast(2) == 8
    assert log.getLast(3) == 7
    assert log.getLast(4) == 6
    assert log.getLast(5) == 5


if __name__ == '__main__':
    main()
