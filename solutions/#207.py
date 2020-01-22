class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)


class Graph:
    def __init__(self):
        self.nodes, self.edges = set(), dict()
        self.set_1, self.set_2 = set(), set()

    def check_bipartite_bfs(self):
        for node, _ in self.edges.items():
            if node not in self.set_2:
                self.set_1.add(node)
                if self.edges[node]:
                    for neighbour in self.edges[node]:
                        self.set_2.add(neighbour)
        for node in self.set_2:
            if self.edges[node]:
                for neighbour in self.edges[node]:
                    if neighbour in self.set_2:
                        return False
        return True


def main():
    g = Graph()
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g.nodes = set([a, b, c, d, e, f])

    g.edges[a] = set([d])
    g.edges[b] = set([d, e, f])
    g.edges[c] = set([f])
    g.edges[d] = set([a, b])
    g.edges[e] = set([b])
    g.edges[f] = set([b, c])
    assert g.check_bipartite_bfs()

    g.edges = dict()
    g.nodes = {a, b, c, d, e, f}
    g.edges[a] = set([d])
    g.edges[b] = set([d, e, f])
    g.edges[c] = set([f])
    g.edges[d] = set([a, b])
    g.edges[e] = set([b, f])
    g.edges[f] = set([b, c, e])
    assert not g.check_bipartite_bfs()


if __name__ == '__main__':
    main()
