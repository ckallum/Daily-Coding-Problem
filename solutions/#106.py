class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_bst_bfs(root):
    if not root:
        return None
    queue = list()
    result = list()
    queue.append(root)
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def main():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)
    root.right.right = Node(4)
    assert print_bst_bfs(root) == [0, 1, 2, 3, 4]


if __name__ == '__main__':
    main()
