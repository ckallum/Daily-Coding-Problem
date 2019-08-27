# Tree traversal, depth first to get totals of child subtrees, then make comparisons with children to get total value at current root


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def getUnivalCount(root):
    if not root:
        return 0
    unival_count = getUnivalCount(root.right) + getUnivalCount(root.left)
    if root.right or root.left:
        if root.right and root.left:
            if root.val == root.right.val and root.val == root.left.val:
                return unival_count + 1
            else:
                return unival_count
        elif root.right and root.right.val == root.val:
            return unival_count + 1
        elif root.left.val == root.val:
            return unival_count + 1
        else:
            return unival_count

    return 1


def main():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.right = Node(0)
    rightleft = Node(1)
    root.right.left = rightleft
    rightleft.right = Node(1)
    rightleft.left = Node(1)
    print(getUnivalCount(root))
    assert (getUnivalCount(root)) == 5
    assert (getUnivalCount(root.left)) == 1
    assert (getUnivalCount(root.right)) == 4
    assert (getUnivalCount(rightleft)) == 3
    b = Node(0)
    b.left = Node(0)
    b.left.left = Node(0)
    b.left.right = Node(0)
    assert getUnivalCount(b) == 4


if __name__ == '__main__':
    main()
