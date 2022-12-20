# Topological Sort by Alessia Sarritzu
from queue import Queue
import unittest


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.outgoing = []
        self.incoming = 0

    def add_edge(self, node):
        self.outgoing.append(node)


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)


def topological_sort(graph):
    order = Queue()
    process_next = Queue()

    for node in graph.nodes:             # Iterate through each node
        for out in node.outgoing:       # Iterate through each node's edge
            out.incoming += 1

    # Therefore, the complexity is V + E, due to the fact that the number of edges is distributed
    # across each element of the outer loops.

    for node in graph.nodes:            # Iterate through each node
        if node.incoming == 0:
            process_next.put(node)

    while process_next.qsize() > 0:              # V + E
        node = process_next.get()
        for out in node.outgoing:
            out.incoming -= 1
            if out.incoming == 0:
                process_next.put(out)
        order.put(node)

    if order.qsize() == len(graph.nodes):
        return order
    else:
        return None


class Test(unittest.TestCase):
    def test_valid_graph(self):
        nodes = {"A": GraphNode("A"), "B": GraphNode("B"), "C": GraphNode("C"),
                 "D": GraphNode("D"), "E": GraphNode("E"), "F": GraphNode("F")}
        nodes["A"].add_edge(nodes["D"])
        nodes["B"].add_edge(nodes["D"])
        nodes["D"].add_edge(nodes["C"])
        nodes["F"].add_edge(nodes["A"])
        nodes["F"].add_edge(nodes["B"])
        g = Graph()
        for n in nodes.values():
            g.add_node(n)

        oq = topological_sort(g)
        self.assertEqual(", ".join([oq.get().value for _ in range(oq.qsize())]), "E, F, A, B, D, C")

    def test_graph_with_cycle(self):
        nodes = {"A": GraphNode("A"), "B": GraphNode("B"), "C": GraphNode("C"), "D": GraphNode("D")}
        nodes["A"].add_edge(nodes["B"])
        nodes["B"].add_edge(nodes["C"])
        nodes["C"].add_edge(nodes["D"])
        nodes["D"].add_edge(nodes["A"])
        g = Graph()
        for n in nodes.values():
            g.add_node(n)

        oq = topological_sort(g)
        self.assertIsNone(oq)


if __name__ == "__main__":
    unittest.main()
