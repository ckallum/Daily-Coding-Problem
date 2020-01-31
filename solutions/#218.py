def reverse_graph(graph):
    new = {x: [] for x in graph}
    for v in graph:
        for v2 in graph[v]:
            new[v2].append(v)
    print(new)
    return new


def main():
    graph = {"a": ["b", "c"],
             "b": ["c", "d"],
             "c": ["d"],
             "d": ["a"]}
    assert reverse_graph(graph) == {"a": ["d"],
                                    "b": ["a"],
                                    "c": ["a", "b"],
                                    "d": ["b", "c"]}


if __name__ == '__main__':
    main()
