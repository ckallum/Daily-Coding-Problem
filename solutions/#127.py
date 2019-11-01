class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def to_list(self):
        res = []
        current = self
        while current:
            res.append(current.value)
            current = current.next
        return res


def add_nodes(n1, n2):
    current = Node(0)
    head = Node(None)
    head.next = current
    while n1 or n2:
        if n1 and n2:
            total = n1.value + n2.value + current.value
        elif n1:
            total = n1.value + current.value
        else:
            total = n2.value + current.value
        current.value = total % 10
        if total > 9:
            current.next = Node(1)
            current = current.next
        if n1:
            n1 = n1.next
        if n2:
            n2 = n2.next

    return head.next


def main():
    n1 = Node(9)
    n1.next = Node(9)
    n2 = Node(5)
    n2.next = Node(2)
    n2.next.next = Node(1)
    print(add_nodes(n1, n2).to_list())
    assert add_nodes(n1, n2).to_list() == [4, 2, 2]


if __name__ == '__main__':
    main()
