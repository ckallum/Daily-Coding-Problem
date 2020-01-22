class ListNode:
    def __init__(self, value, n=None):
        self.value = value
        self.next = n

    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.value)
            current = current.next
        return result


def partition_linked_list(head, k):
    upper = ListNode(None)
    lower = ListNode(None)
    upper_pointer = ListNode(None, upper)
    lower_pointer = ListNode(None, lower)
    while head:
        if head.value < k:
            lower.next = head
            lower = lower.next
        else:
            upper.next = head
            upper = upper.next
        head = head.next
    lower.next = upper_pointer.next.next
    return lower_pointer.next.next


def main():
    list = ListNode(5, ListNode(1, ListNode(8, ListNode(0, ListNode(3)))))
    assert partition_linked_list(list, 3).to_list() == [1, 0, 5, 8, 3]


if __name__ == '__main__':
    main()
