class Node(object):
    def __init__(self, value):
        self.next = None
        self.value = value


def removeLookahead(head, k):
    headPointer = Node(None)
    headPointer.next = head
    lookahead = headPointer
    for _ in range(k):
        lookahead = lookahead.next
    node = headPointer
    while lookahead:
        lookahead = lookahead.next
        if lookahead:
            node = node.next
        else:
            node.next = node.next.next
    return headPointer.next


def convertToLL(nums):
    head = Node(nums[0])
    current = head
    for num in nums[1:]:
        next = Node(num)
        current.next = next
        current = current.next
    return head


def convertToList(head):
    ret = list()
    node = head
    while node:
        ret.append(node.value)
        node = node.next
    return ret


def main():
    assert convertToList(removeLookahead(convertToLL([0, 1, 2, 3, 4]), 2)) == [0, 1, 2, 4]
    assert convertToList(removeLookahead(convertToLL([0, 1, 2, 3, 4]), 5)) == [1, 2, 3, 4]


if __name__ == '__main__':
    main()