from unittest import TestCase

from algorithms.last_in_tree import last_in_tree
from model.graph import Graph


class Test(TestCase):
    def test_correct_last_in_tree(self):
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

        order = [0, 1, 7, 5, 6, 2, 4, 3]

        tree = last_in_tree(graph, order, n)

        expected_tree = Graph(n)
        expected_tree.add_edge(0, 1)
        expected_tree.add_edge(1, 3)
        expected_tree.add_edge(1, 7)
        expected_tree.add_edge(7, 4)
        expected_tree.add_edge(7, 5)
        expected_tree.add_edge(2, 6)
        expected_tree.add_edge(6, 7)

        self.assertEqual(expected_tree, tree)