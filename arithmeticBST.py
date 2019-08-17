class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def parseTree(root):
    if not root:
        return None
    if root.left is None and root.right is None:
        return root.value
    else:
        opdict = {"*": parseTree(root.left) * parseTree(root.right), "+": parseTree(root.left) + parseTree(root.right),
                  "-": parseTree(root.left) - parseTree(root.right), "/": parseTree(root.left) / parseTree(root.right)}
        value = opdict[root.value]
        return value


def createBST(numbers):
    if len(numbers) == 1:
        return Node(numbers[0])
    root = Node(numbers[0])
    root.left = createBST(numbers[1:int(len(numbers) / 2) + 1])
    root.right = createBST(numbers[int(len(numbers) / 2) + 1:])

    return root


def main():
    root = createBST(["*", "+", 3, 2, "+", 4, 5])
    assert parseTree(root) == 45


if __name__ == '__main__':
    main()