class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_deepest_node(root):
    if not root:
        return None, 0
    if not (root.left or root.right):
        return root.value, 1
    left_result = find_deepest_node(root.left)
    right_result = find_deepest_node(root.right)
    print(left_result, right_result)
    return (left_result[0], left_result[1]+1) if left_result[1] > right_result[1] else (right_result[0], right_result[1]+1)


def main():
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    assert find_deepest_node(root)[0] == 'd'


if __name__ == '__main__':
    main()
