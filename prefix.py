from collections import defaultdict

def prefixFuncShort(l, pre):
    return list(filter(lambda x: x[:len(pre)] == pre, l))


class TrieNode(object):
    def __init__(self, char):
        self.value = char
        self.children = defaultdict(TrieNode)
        self.finished = False


def add(node, word):
    current = node
    for char in word:
        if char in current.children:
            current = current.children[char]
        else:
            newNode = TrieNode(char)
            current.children[char] = newNode
            current = newNode
    current.finished = True


def findSuf(node):
    if node.finished:
        return [node.value]

    s = []
    for key, trieNode in node.children.items():
        s.extend(findSuf(trieNode))
    s = [node.value + substring for substring in s]
    return s



def search(node, pre):
    current = node
    resultStrings = list()
    for char in pre:
        if char in current.children:
            current = current.children[char]
        else:
            return []
    suffix = findSuf(current)

    for suf in suffix:
        resultStrings.append(pre[:-1]+str(suf))
    return resultStrings



def prefixFuncTrie(l, pre):
    t = TrieNode('*')
    for word in l:
        add(t, word)
    result = search(t, pre)
    return result



def main():
    l = ['dog', 'deer', 'deal', 'd']
    print(prefixFuncShort(l, 'de'))
    print(prefixFuncTrie(l, 'de'))


if __name__ == '__main__':
    main()
