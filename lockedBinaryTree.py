class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.locked = False

    def is_locked(self):
        return self.locked

    def lock(self):
        if not self.locked:
            if not (self.parent.lock or self.right.lock or self.left.lock):
                self.locked = True
                return True
        return False

    def unlock(self):
        if self.locked:
            if not (self.parent.lock or self.right.lock or self.left.lock):
                self.locked = True
                return True
        return False

