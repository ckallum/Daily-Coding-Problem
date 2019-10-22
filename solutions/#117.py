from cmath import inf


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_minimum(root, level=0):
    if not root:
        return level, inf
    if not (root.left or root.right):
        return level, inf

    left = find_minimum(root.left, level + 1)
    right = find_minimum(root.right, level + 1)
    current_sum = root.value + root.left.value + root.right.value
    if current_sum < left[1] and current_sum < right[1]:
        return level, current_sum
    elif right[1] < current_sum or left[1] < current_sum:
        if right[1] < left[1]:
            return right
        else:
            return left


def main():
    root = Node(3)
    root.left = Node(2)
    root.right = Node(1)
    root.right.right = Node(0)
    root.right.left = Node(-1)
    root.left.left = Node(1)
    root.left.right = Node(4)
    assert find_minimum(root) == (1, 0)


if __name__ == '__main__':
    main()

