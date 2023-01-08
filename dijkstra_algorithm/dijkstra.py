# Dijkstra's Algorithm by Alessia Sarritzu
import unittest
from math import inf
from heapdict import heapdict


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, vertex, weight):
        self.edges.append(Edge(vertex, weight))


class Edge:
    def __init__(self, vertex, weight):
        self.weight = weight
        self.vertex = vertex


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertices(self, vertices):
        for vertex in vertices:
            self.vertices.append(vertex)


def dijkstra(graph, start_vertex, end_vertex):
    path_weight = {}
    previous = {}
    remaining = heapdict()

    for vertex in graph.vertices:
        if vertex == start_vertex:
            path_weight[vertex] = 0
        else:
            path_weight[vertex] = inf
        previous[vertex] = None
        remaining[vertex] = path_weight[vertex]

    while len(remaining) > 0:
        v = remaining.popitem()[0]
        for edge in v.edges:
            if path_weight[v] + edge.weight < path_weight[edge.vertex]:
                path_weight[edge.vertex] = path_weight[v] + edge.weight
                remaining[edge.vertex] = path_weight[edge.vertex]
                previous[edge.vertex] = v

    shortest_path = [end_vertex]
    prev = end_vertex
    end = False
    while end is False and prev in previous:
        shortest_path.append(previous[prev])
        prev = previous[prev]
        if prev == start_vertex:
            end = True

    if end:
        return "->".join(reversed([v.value for v in shortest_path]))
    else:
        return "Path not found."


class Test(unittest.TestCase):
    def test_valid_path(self):
        a = Vertex("A")
        b = Vertex("B")
        c = Vertex("C")
        d = Vertex("D")
        e = Vertex("E")

        a.add_edge(d, 60)
        a.add_edge(c, 12)
        b.add_edge(a, 10)
        c.add_edge(b, 20)
        c.add_edge(d, 32)
        e.add_edge(a, 7)

        graph = Graph()
        graph.add_vertices([a, b, c, d, e])
        self.assertEqual(dijkstra(graph, b, d), "B->A->C->D")

    def test_invalid_path(self):
        f = Vertex("F")
        g = Vertex("G")
        h = Vertex("H")
        i = Vertex("I")

        f.add_edge(h, 8)
        g.add_edge(f, 45)
        g.add_edge(h, 82)
        i.add_edge(f, 10)
        i.add_edge(g, 13)

        graph = Graph()
        graph.add_vertices([f, g, h, i])
        self.assertEqual(dijkstra(graph, h, i), "Path not found.")


if __name__ == '__main__':
    unittest.main()
