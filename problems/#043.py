from math import inf


class Stack(object):
    def __init__(self, s):
        self.size = s
        self.stack = []
        self.max = 0

    def push(self, val):
        if len(self.stack) < self.size:
            if val >= self.max:
                self.stack.append(2 * val - self.max)
                self.max = val
            else:
                self.stack.append(val)
        else:
            print("Invalid")
            return None

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val > self.max:
                self.max = 2 * self.max - val
            return val
        else:
            print("Invalid")
            return None

    def maxvalue(self):
        if not self.stack:
            return None
        return self.max


def main():
    s = Stack(10)
    for x in range(10):
        s.push(x)
    for x in range(9, -1, -1):
        assert s.maxvalue() == x
        s.pop()


if __name__ == '__main__':
    main()
