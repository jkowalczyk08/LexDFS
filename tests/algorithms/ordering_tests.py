from unittest import TestCase

from algorithms.dfs_plus import dfs_plus
from algorithms.last_in_tree import last_in_tree
from algorithms.ordering import ordering
from model.graph import Graph


class Test(TestCase):
    def test_correct_ordering(self):
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

        s = 0
        dfs_plus_tiebreaking_order = [i for i in range(n)]
        order = dfs_plus(graph, dfs_plus_tiebreaking_order)
        tree = last_in_tree(graph, order)
        result = ordering(graph, tree, s, dfs_plus_tiebreaking_order[::-1])

        self.assertEqual(result, [0, 1, 7, 4, 6, 2, 5, 3])
