def minimally_connected(graph):
    for v in graph:
        for i, n in enumerate(graph[v]):
            graph[v].remove(n)
            graph[n].remove(v)
            if is_connected(graph, v, n):
                return False
            graph[n].add(v)
            graph[v].add(n)
    return True


def is_connected(graph, current, target, seen=[]):
    if current == target:
        return True
    return any(is_connected(graph, n, target, seen + [current]) for n in graph[current] if n not in seen)


def main():
    graph = {"a": {"b"}, "b": {"a"}}
    graph2 = {"a": {"b", "c"}, "b": {"a", "c"}, "c": {"b", "a"}}
    assert minimally_connected(graph)
    assert not minimally_connected(graph2)


if __name__ == '__main__':
    main()
