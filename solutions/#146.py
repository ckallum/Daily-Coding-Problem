class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preorder(self):
        result = list()
        result.append(self.value)
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result


def prune_zeros(root):
    if not root:
        return None
    left = prune_zeros(root.left)
    right = prune_zeros(root.right)
    root.left = left
    root.right = right
    if root.value == 1:
        return root
    else:
        if not (root.left or root.right):
            return None
    return root


def main():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.right = Node(0)
    root.right.left = Node(1)
    root.right.left.right = Node(0)
    root.right.left.left = Node(0)
    print(root.preorder())
    print(prune_zeros(root).preorder())
    assert prune_zeros(root).preorder() == [0, 1, 0, 1]


if __name__ == '__main__':
    main()
