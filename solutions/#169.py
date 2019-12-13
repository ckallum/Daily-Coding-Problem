class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def p(self):
        result = []
        current = self
        while current:
            result.append(current.value)
            current = current.next
        return result


def sort(head):
    if not head.next:
        return head
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    temp = ListNode(None)
    temp.next = head
    for i in range((count-1) // 2):
        head = head.next
    l2 = head.next
    head.next = None
    left = sort(temp.next)
    right = sort(l2)
    return merge(left, right)


def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    head = ListNode(None)
    temp = ListNode(None)
    temp.next = head
    while l1 and l2:
        if l1.value < l2.value:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next

    if not l1:
        head.next = l2
    if not l2:
        head.next = l1
    return temp.next.next


def main():
    head = ListNode(4)
    head.next = ListNode(1)
    head.next.next = ListNode(-3)
    head.next.next.next = ListNode(99)
    res = sort(head)
    assert res.p() == [-3, 1, 4, 99]


if __name__ == '__main__':
    main()
