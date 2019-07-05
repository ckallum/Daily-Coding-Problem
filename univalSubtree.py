class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def getUnivalCount(root):
    if not root:
        return 0
    total = getUnivalCount(root.left) + getUnivalCount(root.right)
    if root.right or root.left:
        if root.right.data and root.left.data == root.data:
            return 1+total
        else:
            return total
    else:
        return 1

    return total


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


if __name__ == '__main__':
    main()

