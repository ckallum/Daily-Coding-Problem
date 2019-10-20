class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_exact_subtree(s, t):
    if not (s or t):
        return True
    if (s and not t) or (t and not s):
        return False
    if s.value == t.value:
        return is_exact_subtree(s.left, t.left) and is_exact_subtree(s.right, t.right)

    return False


def is_subtree(s, t):
    if is_exact_subtree(s, t):
        return True
    result = False
    if s.left:
        result = result or is_subtree(s.left, t)
    if s.right:
        result = result or is_subtree(s.right, t)
    return result


def main():
    s = Node(1)
    s.left = Node(2)
    s.right = Node(3)
    s.right.right = Node(5)
    s.right.left = Node(4)
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.right.right = Node(5)
    r.right.left = Node(4)
    assert is_exact_subtree(s, r)

    t = Node(3)
    t.right = Node(5)
    t.left = Node(4)
    assert is_subtree(s, t)
    s.right.right.value = 6
    s.right.right.value = 7
    assert not is_subtree(s, t)


if __name__ == '__main__':
    main()
