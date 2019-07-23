from sys import maxsize


class OverFlowException(Exception):
    def __init__(self):
        self.message = "Stack overflow"

    def __str__(self):
        return self.message


class UnderFlowException(Exception):
    def __init__(self):
        self.message = "Stack underflow"

    def __str__(self):
        return self.message


class MaxStack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.max = -maxsize

    def push(self, val):
        if self.size == len(self.stack):
            try:
                raise OverFlowException()
            except OverFlowException as e:
                print(e)
        if val > self.max:
            self.stack.append(2 * val - self.max)
            self.max = val

    def pop(self):
        if self.size == 0:
            try:
                raise UnderFlowException()
            except UnderFlowException as e:
                print(e)
        val = self.stack.pop(self.size-1)
        if val == self.max:
            self.max = 2*self.max - val

    def max(self):
        return self.max


def main():
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print(s.max())
    # 3
    s.pop()
    s.pop()
    print(s.max())


if __name__ == '__main__':
    main()
