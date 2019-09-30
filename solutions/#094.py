from cmath import inf


class Node(object):
    def __init__(self, value):
        self.value = value

        self.left = None
        self.right = None


def max_path_sum(root):
    if not root:
        return -inf
    if not(root.left or root.right):
        return root.value

    right_sum = max_path_sum(root.right)
    left_sum = max_path_sum(root.left)
    return max(root.value+root.right.value, root.value+root.left.value, right_sum, left_sum)


def main():
    root = Node(8)
    root.left = Node(9)
    root.right = Node(10)
    root.left.right = Node(20)
    root.left.left = Node(12)
    root.right.right = Node(10)
    root.right.left = Node(15)
    assert max_path_sum(root) == 29
    root.left.right = Node(0)
    assert max_path_sum(root) == 25


if __name__ == '__main__':
    main()
