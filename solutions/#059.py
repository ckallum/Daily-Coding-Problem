"""
Implementation of a Merkle Tree, a hash-based tree data structure where all leaf nodes
are files and the other nodes are directories.
Each file is a hash of its contents, each directory is a hash of all its children.

This allows us to compare file's and verify data is the same/allows us to sync data
efficiently by comparing its hashes instead of having to store and read the full file
system.

This protocol is mostly used during file transfers and checking if there has been a
a change made in a distributed file system. If there has been a change in computer A,
computer A sends a hash of the file to computer B. Computer B then checks the hash of
the root of the file to the hash of the root of the received file. If there is a
difference computer B will want to see the hashes of the children directories of the root
to see which directory has been and changed, this is repeated until we get to the piece
of data that been changed and is thus updated.

This is commonly used in version control and any transactional based operations
"""
from hashlib import md5


class MerkerFile(object):
    def __init__(self):
        self.content = ""
        self.children = []
        self.hash = ""
        self.is_dir = False
        self.parent = None

    def add_content(self, content):
        if self.is_dir:
            raise Exception("Directory can't have contents")

        self.content = content
        self.hash = md5(content.encode()).hexdigest()
        self.rehash_directory()

    def rehash_directory(self):
        dir_node = self.parent

        while dir_node:
            children = dir_node.children
            childhashes = ""
            for child in children:
                childhashes += child.hash
            dir_node.hash = md5(childhashes.encode()).hexdigest()
            dir_node = dir_node.parent

    def add_to_directory(self, directory):
        directory.children.append(self)
        self.parent = directory
        self.rehash_directory()

    def getFileHashes(self):
        childHashes = []
        if self.is_dir and not self.children:
            return None
        if not self.is_dir:
            return [self.hash]
        for child in self.children:
            childHashes.extend(child.getFileHashes())

        return childHashes


def findDifferencesBetweenSystems(root1, root2):
    if not (root1 or root2):
        return None

    return list(set(root1.getFileHashes())-set(root2.getFileHashes()))


def main():
    # create a directory structure on the first computer
    computer1_root = MerkerFile()
    computer1_root.is_dir = True
    file1 = MerkerFile()
    file1.add_to_directory(computer1_root)
    file1.add_content("File 1 Content")

    computer2_root = MerkerFile()
    computer2_root.is_dir = True
    file1_clone = MerkerFile()
    file1_clone.add_to_directory(computer2_root)
    file1_clone.add_content("File 1 Content")
    file2 = MerkerFile()
    file2.add_to_directory(computer1_root)
    file2.add_content("File 2 Content")
    print(findDifferencesBetweenSystems(computer1_root, computer2_root))

    assert findDifferencesBetweenSystems(computer1_root, computer2_root) == [file2.hash]


if __name__ == '__main__':
    main()
