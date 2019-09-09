class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(node):
    current = node
    value_list = list()
    while current:
        value_list.append(current.value)
        current = current.next
    return value_list


def recursive_reverse_linked_list(head):
    if not head:
        return None
    if not head.next:
        return head
    next_node = recursive_reverse_linked_list(head.next)
    next_node.next = head
    head.next = None
    return next_node.next


def iterative_reverse_linked_list(head):
    if not head.next:
        return head
    head_next = head.next
    head.next = None
    next_next = head_next.next
    while head_next:
        head_next.next = head
        head = head_next
        head_next = next_next
        if head_next:
            next_next = head_next.next
    return head


def main():
    root = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    root.next = two
    two.next = three
    three.next = four
    recursive_reverse_linked_list(root)
    assert print_list(four) == [4, 3, 2, 1]
    root = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    root.next = two
    two.next = three
    three.next = four
    head = iterative_reverse_linked_list(root)
    assert print_list(head) == [4, 3, 2, 1]


if __name__ == '__main__':
    main()
