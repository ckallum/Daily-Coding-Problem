class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def root_to_leaves(root):
    if not root:
        return []
    if not (root.left or root.right):
        return [[root.value]]
    result = list()
    right_res = root_to_leaves(root.right)
    for r in right_res:
        result.append([root.value] + r)
    left_res = root_to_leaves(root.left)
    for l in left_res:
        result.append([root.value] + l)
    return result


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(5)
    root.right.left = Node(4)
    assert root_to_leaves(root) == [[1, 3, 5], [1, 3, 4], [1, 2]]


if __name__ == '__main__':
    main()
