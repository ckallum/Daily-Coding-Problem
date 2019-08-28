def colourgraph(graph, k, coloured={}):
    if len(coloured) == len(graph):
        return True

    notcoloured = [row for row in range(len(graph)) if row not in coloured]
    for vertex in notcoloured:
        for colour in range(k):
            coloured[vertex] = colour
            if isvalid(graph, coloured, vertex, colour):
                if colourgraph(graph, k, coloured):
                    return True
            del coloured[vertex]
    return False


def isvalid(graph, coloured, row, colour):
    adjacent = [x for x in range(len(graph[row])) if graph[row][x] == 1]
    for coord in adjacent:
        if coord in coloured:
            if coloured[coord] == colour:
                return False
    return True


def colourgraph2(graph, k, coloured=[]):
    if len(graph) == len(coloured):
        return True

    for colour in range(k):
        coloured.append(colour)
        if isvalid2(graph, coloured, colour):
            if colourgraph2(graph, k, coloured):
                return True
        coloured.pop()
    return False


def isvalid2(graph, coloured, pre):
    colouredadjacent = [x for x, edge in enumerate(graph[len(coloured)-1]) if
                        edge and x < len(coloured)-1]
    for vertex in colouredadjacent:
        if coloured[vertex] == pre:
            return False
    return True


def main():
    adjmat1 = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
    ]
    adjmat2 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    assert not colourgraph(adjmat1, 3)
    assert colourgraph(adjmat1, 4)
    assert colourgraph(adjmat1, 1)
    assert colourgraph(adjmat2, 1)

    assert not colourgraph2(adjmat1, 3)
    assert colourgraph2(adjmat1, 4)
    assert colourgraph2(adjmat1, 1)
    assert colourgraph2(adjmat2, 1)


if __name__ == '__main__':
    main()
