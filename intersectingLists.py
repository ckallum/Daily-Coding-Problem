class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def intersection(l1, l2):
    l1Dict = dict()
    while l1:
        l1Dict[l1.val] = True
        l1 = l1.next
    while l2:
        if l2.val in l1Dict:
            return l2.val
        l2 = l2.next
    return None


def main():
    n3 = ListNode(3)
    n7 = ListNode(7)
    n8 = ListNode(8)
    n10 = ListNode(10)
    n99 = ListNode(99)
    n1 = ListNode(1)
    n3.next = n7
    n7.next = n8
    n8.next = n10
    n99.next = n1
    n1.next = n8
    print(intersection(n3, n99))


if __name__ == '__main__':
    main()
