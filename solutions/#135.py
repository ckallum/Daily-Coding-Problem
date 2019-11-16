class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def min_path_sum(root):
    if not root:
        return 0

    return root.value + (min(min_path_sum(root.right), min_path_sum(root.left)))


def main():
    root = Node(10)
    root.left = Node(5)
    root.left.right = Node(2)
    root.right = Node(5)
    root.right.right = Node(1)
    root.right.right.left = Node(-1)
    assert min_path_sum(root) == 15


if __name__ == '__main__':
    main()
