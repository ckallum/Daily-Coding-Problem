class ListNode:
    def __init__(self, value, n=None):
        self.value = value
        self.n = n


def partition_linked_list(head, k):
    pass


def main():
    list = ListNode(5, ListNode(1, ListNode(8, ListNode(0, ListNode(3)))))
    assert partition_linked_list(list, 3) == [1, 0, 5, 8, 3]


if __name__ == '__main__':
    main()
