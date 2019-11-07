class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current


def in_order_successor(root):
    if root.right:
        return find_min(root.right)
    parent = root.parent
    while parent:
        if parent.right.value != root.value:
            return parent
        root = parent
        parent = parent.parent
    return parent


def main():
    root = Node(20, None)
    root.left = Node(8,root)
    root.right = Node(22, root)
    root.left.left = Node(4, root.left)
    root.left.right = Node(12, root.left)
    root.left.right.left = Node(10, root.left.right)
    root.left.right.right = Node(14, root.left.right)
    assert in_order_successor(root.left.right.left).value == 12
    assert in_order_successor(root.left.right.right).value == 20


if __name__ == '__main__':
    main()
