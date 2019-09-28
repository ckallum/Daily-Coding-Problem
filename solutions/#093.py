class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        res = str(self.value)
        if self.left:
            res += str(self.left)
        if self.right:
            res += str(self.right)
        return res


def largest_bst(root):
    if not root:
        return False, None, 0

    if not (root.left or root.right):
        return True, root, 1

    left_bst, left_node, left_count = largest_bst(root.left)
    right_bst, right_node, right_count = largest_bst(root.right)

    if left_bst or right_bst:
        if left_node.value < root.value < right_node.value:
            return True, root, 1 + left_count + right_count
        elif right_count > left_count:
            return False, right_node, right_count
        elif left_count > right_count:
            return False, left_node, left_count

    return False, root, 0


def main():
    root = Node(5)
    left = Node(3)
    left.left = Node(0)
    left.right = Node(4)
    right = Node(2)
    root.left = left
    root.right = right
    is_bst, node, count = largest_bst(root)
    print(is_bst, node.value, count)
    assert count == 3
    assert str(node) == "304"


if __name__ == '__main__':
    main()
