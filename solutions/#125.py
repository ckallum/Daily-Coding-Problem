from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bst_sum_target(root, k):
    cache = {}
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        if k - current.value in cache:
            return current.value, cache[k - current.value]
        else:
            cache[current.value] = current.value
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
    return None


def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(11)
    root.right.right = Node(15)
    assert (bst_sum_target(root, 20)) == 5, 15


if __name__ == '__main__':
    main()
