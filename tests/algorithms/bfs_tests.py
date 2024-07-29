from unittest import TestCase

from algorithms.bfs import bfs
from model.graph import Graph

class Test(TestCase):
    def test_correct_bfs(self):
        n = 8
        graph = Graph(n)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 5)
        graph.add_edge(1, 7)
        graph.add_edge(7, 6)
        graph.add_edge(6, 2)
        graph.add_edge(7, 2)
        graph.add_edge(7, 4)
        graph.add_edge(7, 5)

        expected_order = [0, 1, 2, 3, 5, 7, 6, 4]

        bfs_order = bfs(graph, 0, n)

        self.assertEqual(expected_order, bfs_order)
