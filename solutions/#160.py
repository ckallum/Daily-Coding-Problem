from cmath import inf


def find_max_path(graph):
    max_path = -inf
    for node in graph:
        for neighbour in graph[node]:
            current = bfs(graph, neighbour, graph[node][neighbour], [node])
            max_path = max(current, max_path)
    print(max_path)
    return max_path


def bfs(graph, current, current_sum, visited):
    if current not in graph:
        return current_sum
    visited.append(current)
    max_path = current_sum
    for neighbour in graph[current]:
        if neighbour not in visited:
            max_path = max(max_path, bfs(graph, neighbour, current_sum + graph[current][neighbour], visited))
    return max_path


def getGraph(weights):
    graph = {}
    for k, v in weights.items():
        nodes = k.split("-")
        if nodes[0] not in graph:
            graph[nodes[0]] = dict()
        if nodes[1] not in graph:
            graph[nodes[1]] = dict()
        graph[nodes[0]][nodes[1]] = v
        graph[nodes[1]][nodes[0]] = v

    return graph


def main():
    weights = {"a-b": 3, "a-c": 5, "a-d": 8, "d-e": 2, "d-f": 4, "e-g": 1, "e-h": 1}
    graph = getGraph(weights)
    assert find_max_path(graph) == 17


if __name__ == '__main__':
    main()
