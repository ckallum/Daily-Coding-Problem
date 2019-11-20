class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.value)
            current = current.next
        return result


def rotate_linked_list(head):
    if not head:
        return None
    current = head
    new_head = current.next
    n = new_head.next
    new_head.next = current
    current.next = rotate_linked_list(n)

    return new_head


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    assert rotate_linked_list(head).to_list() == [2, 1, 4, 3]


if __name__ == '__main__':
    main()
