from unittest import TestCase

from algorithms.dfs_plus import dfs_plus
from model.graph import Graph
from tests.helpers.shuffle_helper import shuffle_adj_lists


class Test(TestCase):
    def test_correct_dfs_plus(self):
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

        expected_order = [7, 6, 2, 1, 5, 3, 0, 4]
        order = [0, 1, 2, 3, 4, 5, 6, 7]

        for i in range(10):
            shuffle_adj_lists(graph)
            dfs_plus_order = dfs_plus(graph, order)
            self.assertEqual(expected_order, dfs_plus_order)
