class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return Node(key)
    elif node.value < key:
        node.right = insert(node.right, key)
    elif node.value > key:
        node.left = insert(node.left, key)
    return node


def find(node):
    if not node:
        return None
    if node.right:
        if node.right.right:
            return find(node.right)
        elif node.right.left:
            return find(node.right.left)
        else:
            return node
    elif node.left:
        return find(node.left)
    else:
        return node


def main():
    root = None
    root = insert(root, 30)
    insert(root, 40)
    insert(root, 50)
    insert(root, 20)
    insert(root, 45)
    insert(root, 15)
    insert(root, 25)
    assert find(root).value == 45


if __name__ == '__main__':
    main()