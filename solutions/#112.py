class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(a, b, root):
    if not root:
        return False, None
    if root.value == a or root.value == b:
        return True, root

    left = lowest_common_ancestor(a, b, root.left)
    right = lowest_common_ancestor(a, b, root.right)
    if left[0] and right[0]:
        return True, root

    return left if left[0] else right


def main():
    root = Node(1)
    root.right = Node(3)
    root.left = Node(2)
    root.right.right = Node(5)
    root.right.left = Node(4)
    assert lowest_common_ancestor(4, 5, root)[1].value == 3
    assert lowest_common_ancestor(2, 3, root)[1].value == 1


if __name__ == '__main__':
    main()
