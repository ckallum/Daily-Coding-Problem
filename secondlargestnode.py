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


def findlargest(node):
    current = node
    while current:
        if not current.right:
            return current
        current = current.right

def find(node):
    if not node or (not node.left and not node.right):
        return False
    current = node
    while current:
        if current.right and not current.right.left and not current.right.right:
            return current
        elif not current.right and current.left:
            return findlargest(current.left)
        current = current.right

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
