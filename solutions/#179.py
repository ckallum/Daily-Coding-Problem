class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def preorder(self):
        result = [self.value]
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result


def construct_from_postorder(postorder):
    if not postorder:
        return None
    print(postorder)
    root = Node(postorder[-1])
    mid = len(postorder) // 2
    postorder.pop()
    root.right = construct_from_postorder(postorder[mid:])
    root.left = construct_from_postorder(postorder[:mid])
    return root


def main():
    nodes = [2, 4, 3, 8, 7, 5]
    root = construct_from_postorder(nodes)
    print(root.preorder())
    assert root.preorder() == [5, 3, 2, 4, 7, 8]


if __name__ == '__main__':
    main()
