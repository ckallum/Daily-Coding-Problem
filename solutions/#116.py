from random import randint, random


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left_ = None
        self.right_ = None

    def __repr__(self):
        string = "{"
        string += "{}: ".format(self.value)
        string += "{"
        string += "l: {}, ".format(self.left_ if self.left_ else -1)
        string += "r: {}".format(self.right_ if self.right_ else -1)
        string += "}"
        string += "}"

        return string

    @classmethod
    def generate(cls):
        return cls(randint(1, 100000))

    @property
    def left(self):
        if not self.left_:
            self.left_ = self.generate()
        return self.left_

    @property
    def right(self):
        if not self.right_:
            self.right_ = self.generate()
        return self.right_


def main():
    size = 100
    root = Node.generate()
    temp = root
    all_generated_nodes = []
    while len(all_generated_nodes) < size:
        temp = temp.left if random() < 0.5 else temp.right
        all_generated_nodes.append(temp)
    assert len(all_generated_nodes) == size
    print(root)


if __name__ == '__main__':
    main()
