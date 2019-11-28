import heapq


class HeapStack():
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, item):
        self.size += 1
        heapq.heappush(self.heap, (-self.size, item))

    def pop(self):
        if self.size > 0:
            item = heapq.heappop(self.heap)
            self.size -= 1
            return item[1]
        else:
            return None


def main():
    heap = HeapStack()
    heap.push(5)
    heap.push(1)
    heap.push(4)
    heap.push(3)
    assert heap.pop() == 3
    assert heap.pop() == 4
    assert heap.pop() == 1
    assert heap.pop() == 5
    assert not heap.pop()


if __name__ == '__main__':
    main()
