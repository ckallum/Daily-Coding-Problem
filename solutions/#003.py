# Tree traversal, problem solving with deserialising a string into relevant search


from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialise(node):
    if not node:
        return 'None' + '-'
    serialised = node.val + '-' + serialise(node.left) + serialise(node.right)
    return serialised


def deserialise(string):
    nodes = string.split('-')

    deserialised = deserialisedNode(deque(nodes), 'root')

    return deserialised


def deserialisedNode(q, find):
    print(q)
    if q:
        next_node = q.popleft()
        if next_node == 'None':
            return None
        else:
            if find in deque(next_node.split('.')):
                return Node(next_node, deserialisedNode(q, 'left'), deserialisedNode(q, 'right'))
    return None


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialise(node))
    n = deserialise(serialise(node))
    assert deserialise(serialise(node)).left.left.val == 'left.left'
    print(n.left.left.val)


if __name__ == '__main__':
    main()
