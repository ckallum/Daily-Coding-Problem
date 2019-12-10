class TwoDIterator():
    def __init__(self, values=[]):
        self.values = values
        self.n = True
        self.row = 0
        self.col = 0
        self.rowLen = len(values)
        self.colLen = len(values[0])

    def hasNext(self):
        return self.n

    def next(self):
        if not self.n:
            return None
        if self.col == self.colLen:
            if self.row < self.rowLen - 1:
                self.row += 1
            while not self.values[self.row] and self.row < self.rowLen - 1:
                self.row += 1
            self.col = 0
            self.colLen = len(self.values[self.row])
        nextValue = self.values[self.row][self.col]
        if self.col < self.colLen-1:
            self.n = True
        else:
            self.n = False
            for r in range(self.row + 1, self.rowLen):
                if self.values[r]:
                    self.n = True
                    break
        self.col += 1

        return nextValue


def main():
    it = TwoDIterator([[1, 2], [3], [], [4, 5, 6]])
    assert it.hasNext()
    assert it.next() == 1
    assert it.next() == 2
    assert it.next() == 3
    assert it.next() == 4
    assert it.next() == 5
    assert it.hasNext()
    assert it.next() == 6
    assert not it.hasNext()


if __name__ == '__main__':
    main()
