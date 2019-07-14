# Tree evaluation and string traversal/creating a tree from a string -> list -> list of nodes


class Node(object):
    def __init__(self, string, t, depth):
        self.string = string
        self.type = t
        self.children = list()
        self.depth = depth
        self.childrenLen = 0
        self.size = len(string)

    def __repr__(self):
        return "(name={}, type={}, len={})".format(
            self.string, self.type, self.size)


def traverseTree(nodeList):
    if not nodeList:
        return None

    parent = nodeList[0]
    for i, node in enumerate(nodeList[1:]):
        if node.depth <= parent.depth:
            break
        if node.depth == parent.depth + 1:
            child = traverseTree(nodeList[i + 1:])
            parent.children.append(child)
            if child.children or child.type == 'file':
                if child.size + child.childrenLen > parent.childrenLen:
                    parent.childrenLen = child.size + child.childrenLen
    return parent


def absolutePath(string):
    if not string:
        return 0
    stringSplit = [x.split('\t') for x in string.split('\n')]
    nodeList = [Node(x[-1], findType(x[-1]), len(x) - 1) for x in stringSplit]
    print(stringSplit)
    print(nodeList)
    parent = traverseTree(nodeList)
    return parent.size + parent.childrenLen


def findType(s):
    if '.' in s:
        return 'file'
    return 'directory'


def main():
    root = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(absolutePath(root))


if __name__ == '__main__':
    main()
