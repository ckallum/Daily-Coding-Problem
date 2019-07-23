class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "Node value = {}, next node = {}".format(self.val, self.next)


def remove(head, k):
    temp = ListNode(None)
    temp.next = head
    lookahead = temp
    for _ in range(k):
        lookahead = lookahead.next
    removedItem = head
    prev = temp
    while lookahead:
        lookahead = lookahead.next
        if lookahead:
            prev = removedItem
            removedItem = removedItem.next
    prev.next = removedItem.next

    return temp.next


def createLinkedList(l):
    head = ListNode(l[0])
    node = head
    for x in l[1:]:
        n = ListNode(x)
        node.next = n
        node = n
    return head


def convertToList(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


def main():
    head = createLinkedList([0, 1, 2, 3, 4, 5])
    assert convertToList(remove(head, 6)) == [1, 2, 3, 4, 5]
    h = createLinkedList([0, 1, 2, 3, 4, 5])
    assert convertToList(remove(h, 2)) == [0, 1, 2, 3, 5]


if __name__ == '__main__':
    main()
