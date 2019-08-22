class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def makeTree(preorder, inorder):
    if not (preorder and inorder):
        return None
    root = Node(preorder[0])
    if len(preorder) == 1:
        return root

    for i, value in enumerate(inorder):
        if value == root.val:
            root.left = makeTree(preorder[1:i + 1], inorder[:i])
            root.right = makeTree(preorder[i + 1:], inorder[i + 1:])

    return root


def main():
    tree = makeTree(preorder=['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                    inorder=['d', 'b', 'e', 'a', 'f', 'c', 'g'])
    assert tree.val == 'a'
    assert tree.left.val == 'b'
    assert tree.left.left.val == 'd'
    assert tree.left.right.val == 'e'
    assert tree.right.val == 'c'
    assert tree.right.left.val == 'f'
    assert tree.right.right.val == 'g'

    tree = makeTree(preorder=['a', 'b', 'd', 'e', 'c', 'g'],
                    inorder=['d', 'b', 'e', 'a', 'c', 'g'])
    assert tree.val == 'a'
    assert tree.left.val == 'b'
    assert tree.left.left.val == 'd'
    assert tree.left.right.val == 'e'
    assert tree.right.val == 'c'
    assert tree.right.right.val == 'g'
