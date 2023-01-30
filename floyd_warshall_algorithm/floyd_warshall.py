# Floyd-Warshall's Algorithm by Alessia Sarritzu
from math import inf
import unittest


class Vertex:
    def __init__(self, data, v_id):
        self.v_id = v_id
        self.data = data
        self.edges = []

    def add_edges(self, edges):
        for data in edges:
            self.edges.append(data)


class AdjacencyMatrix:
    def __init__(self, n):
        self.weight = [[inf for _ in range(n)] for _ in range(n)]
        for i in range(n):
            self.weight[i][i] = 0
        self.vertices = n

    def set_edge(self, i, j, w):
        self.weight[i][j] = w


def floyd_warshall(adj):
    paths = [[inf for _ in range(adj.vertices)] for _ in range(adj.vertices)]

    for k in range(adj.vertices):
        for i in range(adj.vertices):
            for j in range(adj.vertices):
                through_k = adj.weight[i][k] + adj.weight[k][j]
                if through_k < adj.weight[i][j]:
                    adj.weight[i][j] = through_k
                    paths[i][j] = k
                if paths[i][j] == inf and adj.weight[i][j] != inf:
                    paths[i][j] = i

    return paths


def get_path(i, j, paths):
    if paths[i][j] == inf:
        return None

    path = [i]
    while paths[i][j] != i:
        path.append(paths[i][j])
        i = paths[i][j]
    path.append(j)

    return path


class Test(unittest.TestCase):
    def test_floyd_warshall(self):
        vertices = {0: Vertex('A', 0), 1: Vertex('B', 1), 2: Vertex('C', 2),
                    3: Vertex('D', 3), 4: Vertex('E', 4), 5: Vertex('F', 5),
                    6: Vertex('G', 6)}

        vertices[0].add_edges([(1, 10), (3, 75), (4, 14)])
        vertices[1].add_edges([(2, 45), (3, 12), (5, 80)])
        vertices[2].add_edges([(0, 20), (4, 1), (5, 67)])
        vertices[3].add_edges([(1, 30), (2, 19), (4, 6)])
        vertices[4].add_edges([(2, 45), (3, 50)])
        vertices[5].add_edges([(0, 22), (1, 49)])
        vertices[6].add_edges([(0, 105), (3, 70)])

        adj = AdjacencyMatrix(len(vertices))

        for i in vertices.keys():
            for e in vertices[i].edges:
                adj.set_edge(i=i, j=e[0], w=e[1])

        paths = floyd_warshall(adj)
        self.assertEqual(get_path(0, 3, paths), [0, 1, 3])
        self.assertEqual(get_path(3, 4, paths), [3, 4])
        self.assertIsNone(get_path(2, 6, paths))


if __name__ == '__main__':
    unittest.main()
