class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(root):
    if not (root.left or root.right):
        return root.value, True

    left = is_valid_bst(root.left)
    right = is_valid_bst(root.right)

    if left[1] and right[1]:
        if left[0] < root.value < right[0]:
            return root.value, True

    return root.value, False


def main():
    root = Node(2)
    left = Node(1)
    right = Node(3)
    root.left = left
    root.right = right
    assert is_valid_bst(root)[1]

    root1 = Node(2)
    root1.left = right
    root1.right = left
    assert not is_valid_bst(root1)[1]
    root2 = Node(5)
    l = Node(3)
    l.left = Node(1)
    l.right = Node(4)
    r = Node(7)
    r.right = Node(8)
    r.left = Node(6)
    root2.left = l
    root2.right = r
    assert is_valid_bst(root2)[1]
    root2.left.right = Node(2)
    assert not is_valid_bst(root2)[1]


if __name__ == '__main__':
    main()
