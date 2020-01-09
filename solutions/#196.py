from collections import defaultdict


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def frequent_sum_subtree(root):
    sums = defaultdict()
    find(root, sums)
    return max(sums.items(), key=lambda x, y: y)[0]


def find(root, sums):
    if not root.left and not root.right:
        sums[root.value] += 1
        return
    if root.right:
        find(root.right, sums)
    if root.left:
        find(root.left, sums)
    for k, v in sums:
        sums[v + root.value] += 1
    return


def main():
    root = Node(5)
    root.left = Node(2)
    root.right = Node(-5)
    assert frequent_sum_subtree(root) == 2
