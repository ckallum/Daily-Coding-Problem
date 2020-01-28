class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bottom_view(root):
    results = {}
    helper(root, 0, 0, results, {})
    l = []
    for distance, value in results.items():
        l.append(value)
    return l


def helper(node, height, distance, distance_to_node, distance_to_height):
    if not node:
        return
    helper(node.left, height + 1, distance - 1, distance_to_node, distance_to_height)
    if distance not in distance_to_node:
        distance_to_node[distance] = node.value
        distance_to_height[distance] = height
    else:
        if height > distance_to_height[distance]:
            distance_to_node[distance] = node.value
            distance_to_height[distance] = height
    helper(node.right, height + 1, distance + 1, distance_to_node, distance_to_height)


def main():
    root = Node(5, Node(3, Node(1, Node(0)), Node(4)), Node(7, Node(6), Node(9, Node(8))))
    assert bottom_view(root) == [0, 1, 3, 4, 8, 9]


if __name__ == '__main__':
    main()
