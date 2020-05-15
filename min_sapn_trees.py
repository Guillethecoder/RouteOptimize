from heap import Min_Heap
from graph import Graph
from union_find import Set

def MST_Prim(graph):
    """
    Applies Prim's algorithm to compute a minimum spanning tree.
    """
    minSpanTree = Graph(numVertices = graph.numVertices(), numEdges = 0, weightRange = 0)
    queue = Min_Heap()
    parent = {}

    for vertex in graph.vertices():
        parent[vertex] = None
        queue.insert(float('inf'), vertex)

    while queue:
        key, vertex = queue.extract_min()

        predecessor = parent[vertex]
        if predecessor != None:
            weight = graph.weight[(predecessor, vertex)]
            minSpanTree.addUndirectedEdge(predecessor, vertex, weight)

        for neighbor in graph.adjacent[vertex]:
            if neighbor in queue:
                new_key = graph.weight[(vertex, neighbor)]
                if new_key < queue.key(neighbor):
                    queue.decrease_key(neighbor, new_key)
                    parent[neighbor] = vertex

    return minSpanTree


def MST_Kruskal(graph):
    """
    Applies Kruskal's algorithm to compute a minimum spanning tree.
    """

    component = tuple(Set(vertex) for vertex in graph.vertices())
    minSpanTree = Graph(numVertices = graph.numVertices(), numEdges = 0, weightRange = 0)

    for (u, v) in sorted(graph.edges(), key = lambda e: graph.weight[e]):
        if component[u].findSet() != component[v].findSet():
            component[u].union(component[v])
            minSpanTree.addUndirectedEdge(u, v, graph.weight[(u,v)])

    return minSpanTree


def test(numVertices, numEdges, weightRange):
    """
    Checks whether Prim's and Kruskal's algorithms
    produce spanning trees with the same weight
    """
    graph = Graph(numVertices = numVertices,
                  numEdges = numEdges,
                  weightRange = weightRange,
                  directed = False)

    mst = MST_Prim(graph)
    primsWeight = sum(graph.weight[e] for e in mst.edges())

    mst = MST_Kruskal(graph)
    kruskalsWeight = sum(graph.weight[e] for e in mst.edges())

    return primsWeight == kruskalsWeight


def runTests(numVertices, numEdges, weightRange, numTests):
    """
    Runs a sequence of test to check if Prim's and Kruskal's
    algorithms produce spanning trees with the same weight.
    """
    return all(test(numVertices, numEdges, weightRange) for t in range(numTests))
