class ListNode(object):
    def __init__(self, value, next=None):
        self.next = next
        self.value = value

    def ll_to_list(self):
        current = self
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result


def rotate_list(head, k):
    length = 1
    current = head
    while current.next:
        length += 1
        current = current.next
    current.next = head
    temp = current
    for i in range(abs(length - k)):
        temp = temp.next
    new_head = temp.next
    temp.next = None
    return new_head


def main():
    root = ListNode(7, ListNode(7, ListNode(3, ListNode(5))))
    assert rotate_list(root, 2).ll_to_list() == [3, 5, 7, 7]
    root2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert rotate_list(root2, 3).ll_to_list() == [3, 4, 5, 1, 2]
    root3 = ListNode(7, ListNode(7, ListNode(3, ListNode(5))))
    assert rotate_list(root3, 4).ll_to_list() == [7, 7, 3, 5]


if __name__ == '__main__':
    main()
