class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        result = self.value
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


# DFS -> look at how it should behave on last level/leaves and how the second last level processes the result of the
# leaves.
def invert_bst(root):
    if not root:
        return None
    if not (root.left or root.right):
        return root
    temp_left = root.left
    root.left = invert_bst(root.right)
    root.right = invert_bst(temp_left)

    return root


def main():
    root = Node("a")
    root.left = Node("b")
    root.left.left = Node("d")
    root.left.right = Node("e")
    root.right = Node("c")
    root.right.right = Node("f")
    assert str(invert_bst(root)) == "acfbed"


if __name__ == '__main__':
    main()
