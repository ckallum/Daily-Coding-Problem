from math import log, inf

# arbitrage happens when product of exchange rates > 1 i.e not equivalent
""" to simulate the multiplying of rates as addition of a weight of an edge we -log(rate) for each rate
    as -log(rateA) + -log(rateB) = -log(rateA * rateB) < 0 iff rateA*rateB > 1. This is better than brute force
    as we don't have to go through all permutations as it will stop early once we reach a negative cycle.
    
    - We use the Bellman-Ford algorithm which can detect a negative cycle when evaluating the min distance between in
      a path. As for the first loop of vertices the loop invariant guarantees us the minimum path from source to 
      destination presuming all weights are positive
    - However, if there's a negative weight, after the first path we will get a minimum path, but during the second
      iteration we will find an even smaller path because the negative path + minimum path will create a smaller value
      than the previous value of minimum path.
    - Thus we have found a negative cycle where a path/edge returns a negative value which means there is a 
      sequence of product of rates which gives a > 1 result. 
    - We iterate V-1 times as largest cycle traverses through V-1 nodes

"""


def arbitrage(rates):
    graph = [[-log(rate) for rate in row] for row in rates]
    minpaths = [inf] * len(rates)
    # We can choose any source as all vertices are connected so the paths will be the same value no matter the source
    source = 0
    minpaths[source] = 0  # As source is 0, the path from source to any node will always be smaller than the current
    # min path to the node as nodes are set to inf
    # We know if a value of a node < inf then the node has been visited before by the source

    # First traversal, guarantees minimum path between source to vertex given all edge weights are positive
    for i in range(len(graph) - 1):  # V-1
        for v in range(len(graph)):  # All vertices
            for w in range(len(graph)):  # All vertices to all vertices
                if minpaths[w] > minpaths[v] + graph[v][w]:
                    minpaths[w] = minpaths[v] + graph[v][w]

    # Second traversal, should do nothing if no negative weight values, if a minpath to a vertex currently is negative
    # value then the next traversal(minpaths[v] + graph[v][w] will give an even smaller value,
    # which means break as we have found an arbitrage

    for i in range(len(graph) - 1):  # V-1
        for v in range(len(graph)):  # All vertices
            for w in range(len(graph)):  # All vertices to all vertices
                if minpaths[w] > minpaths[v] + graph[v][w]:
                    return True
    return False


def main():
    rates = [[1.0, 0.8, 1.3],
             [0.8, 1.0, 2.4],
             [1.3, 2.4, 1.0]]

    assert arbitrage(rates) == True


if __name__ == '__main__':
    main()
