from collections import Counter


class Graph(object):
    def __init__(self, nodes, neighbour_map):
        self.nodes = nodes
        self.neighbour_map = neighbour_map


class Path(object):
    def __init__(self, nodes=set(), counts=dict()):
        self.nodes = nodes
        self.letter_count = counts


def find_max_path_string(graph_path, start_node, neighbour_map):
    # If there is a cycle return the current path as it's the furthest we can go
    if start_node in graph_path.nodes:
        return [graph_path]

    # Adding current node to the current path and letter count of path
    new_nodes = graph_path.nodes
    new_nodes.add(start_node)
    new_letter_count = graph_path.letter_count
    # Getting the letter from the node as each node is a letter and its number
    if start_node[0] not in new_letter_count:
        new_letter_count[start_node[0]] = 0
    new_letter_count[start_node[0]] += 1
    new_graph_path = Path(new_nodes, new_letter_count)

    # if the current node has no neighbours
    if start_node not in neighbour_map:
        return [new_graph_path]

    paths = list()
    for neighbour in neighbour_map[start_node]:
        paths.extend(find_max_path_string(new_graph_path, neighbour, neighbour_map))
    return paths


def max_graph_path(graph_string, edge_list):
    graph = Graph(build_graph(graph_string, edge_list)[0], build_graph(graph_string, edge_list)[1])
    paths = list()
    graph_path = Path()
    for start_node in graph.nodes:
        paths.extend(find_max_path_string(graph_path, start_node, graph.neighbour_map))

    max_path_value = 0
    for path in paths:
        if max(path.letter_count.values()) > max_path_value:
            max_path_value = max(path.letter_count.values())
    return max_path_value if max_path_value > 0 else None


def build_graph(graph_string, edge_list):
    nodes = list()
    letter_counts = dict()
    neighbour_map = dict()
    for letter in graph_string:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1
        # Differentiating between nodes with same letters i.e A1, A2, A3
        nodes.append("{}{}".format(letter, letter_counts[letter]))

    for edge in edge_list:
        if nodes[edge[0]] not in neighbour_map:
            neighbour_map[nodes[edge[0]]] = set()
        if nodes[edge[0]] != nodes[edge[1]]:
            neighbour_map[nodes[edge[0]]].add(nodes[edge[1]])
    return nodes, neighbour_map


def main():
    assert max_graph_path("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]) == 3
    assert not max_graph_path("D", [(0, 0)])


if __name__ == '__main__':
    main()
