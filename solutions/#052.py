class Node(object):
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRU(object):
    def __init__(self, cache_size):
        self.size = cache_size
        self.head = Node(None, None)
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = self.head
        self.head.prev = self.tail
        self.nodes = dict()

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def set(self, key, value):
        if key in self.nodes:
            node = self.nodes[key]
            self.remove(node)
        new = Node(value, key)
        self.add(new)
        self.nodes[key] = new
        if len(self.nodes) > self.size:
            deleted = self.head.next
            self.remove(deleted)
            del self.nodes[deleted.key]

    def get(self, key):
        if key in self.nodes:
            node = self.nodes[key]
            self.remove(node)
            self.add(node)
            return node.value
        return None


def main():
    lru = LRU(3)
    assert not lru.get("a")
    lru.set("a", 1)
    assert lru.get("a") == 1
    lru.set("b", 2)
    lru.set("c", 3)
    lru.set("d", 4)
    lru.set("e", 5)
    lru.set("a", 1)
    assert lru.get("a") == 1
    assert not lru.get("b")
    assert lru.get("e") == 5
    assert not lru.get("c")


if __name__ == '__main__':
    main()
