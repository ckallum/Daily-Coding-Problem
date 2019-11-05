class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rand = None

    def __repr__(self):
        return self.val


def deep_clone(head):
    node_to_index = dict()
    node_index_to_random = dict()
    current = head
    i = 0
    while current:
        node_to_index[current] = i
        current = current.next
        i += 1

    current = head
    i = 0
    while current:
        node_index_to_random[i] = node_to_index[current.rand]
        current = current.next
        i += 1

    current = head
    i = 0
    head_pointer = Node(0)
    tail = head_pointer
    index_to_node = dict()
    while current:
        new = Node(current.val)
        tail.next = new
        tail = tail.next
        index_to_node[i] = new
        current = current.next
        i += 1

    i = 0
    current = head_pointer.next
    while current:
        random = node_index_to_random[i]
        current.rand = index_to_node[random]
        current = current.next
        i += 1
    return head_pointer.next


def main():
    a = Node('a')
    b = Node('b')
    a.next = b
    c = Node('c')
    b.next = c
    d = Node('d')
    c.next = d
    e = Node('e')
    d.next = e

    a.rand = a
    b.rand = a
    c.rand = e
    d.rand = c
    e.rand = c

    clone = deep_clone(a)
    assert clone.val == a.val
    assert clone.rand.val == a.rand.val
    assert clone.next.val == a.next.val
    assert clone.next.rand.val == a.next.rand.val


if __name__ == '__main__':
    main()

