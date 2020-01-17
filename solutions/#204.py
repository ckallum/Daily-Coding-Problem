class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_nodes(root):
    level = 0
    result = 0
    while root:
        result += 2 ** level
        level += 1
        root = root.left

    return result


def main():
    root = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
    assert count_nodes(root) == 7

