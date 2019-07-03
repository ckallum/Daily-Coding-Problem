
class Node:
    def __init__(self, value):
        self.data = value
        self.both = id(value)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

addressMap = dict()
addressMap[id("a")] = a
addressMap[id("b")] = b
addressMap[id("c")] = c
addressMap[id("d")] = d
addressMap[id("e")] = e
addressMap[id("f")] = f

class xorList:
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.head.both = 0
        self.tail.both = 0

    def add(self, element):
        self.tail.both ^= element.both
        element.both = self.tail.both
        self.tail = element

    def get(self, index):
        result = self.head
        previousAddress = 0
        for i in range(index):
            nextAddress = previousAddress ^ result.both
            previousAddress = result.both
            result = addressMap[nextAddress]
        return result.data


def main():
    l = xorList(a)
    l.add(b)
    l.add(c)
    l.add(d)
    assert l.get(0) == 'a'
    assert l.get(1) == 'b'
    assert l.get(2) == 'c'
    assert l.get(3) == 'd'



if __name__ == '__main__':
    main()
