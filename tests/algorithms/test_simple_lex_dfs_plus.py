import unittest

from algorithms.simple_lex_dfs_plus import simple_lex_dfs_plus
from model.graph import Graph
from tests.helpers.shuffle_helper import shuffle_adj_lists


def build_small_test_graph(graph: Graph) -> None:
    graph.add_edge(4, 3)
    graph.add_edge(4, 2)
    graph.add_edge(4, 1)
    graph.add_edge(3, 1)
    graph.add_edge(1, 0)


def build_test_graph(graph: Graph) -> None:
    graph.add_edge(0, 1)    # s
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)    # a
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)    # b
    graph.add_edge(3, 4)    # c
    graph.add_edge(3, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    graph.add_edge(3, 8)
    graph.add_edge(4, 8)    # d
    graph.add_edge(5, 7)    # e
    graph.add_edge(6, 7)    # f
    graph.add_edge(7, 8)    # g
    graph.add_edge(7, 9)
    graph.add_edge(7, 10)
    graph.add_edge(8, 10)   # h
    graph.add_edge(9, 10)   # i

class Test(unittest.TestCase):
    def test_singleton_graph(self):
        tie_breaking_order = [0]
        correct_order = [0]
        n = 1
        graph = Graph(n)
        order = simple_lex_dfs_plus(graph, tie_breaking_order)
        self.assertEqual(correct_order, order)

    def test_simple_lex_dfs_plus_with_small_graph(self):
        tie_breaking_order = [0, 1, 2, 3, 4]
        correct_order = [4, 3, 1, 0, 2]
        n = 5
        graph = Graph(n)
        build_small_test_graph(graph)
        for i in range(10):
            shuffle_adj_lists(graph)
            order = simple_lex_dfs_plus(graph, tie_breaking_order)
            self.assertEqual(correct_order, order)

    def test_simple_lex_dfs_plus(self):
        tie_breaking_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        correct_order = [0, 4, 3, 8, 7, 10, 9, 6, 5, 2, 1]
        n = 11
        graph = Graph(n)
        build_test_graph(graph)
        for i in range(10):
            shuffle_adj_lists(graph)
            order = simple_lex_dfs_plus(graph, tie_breaking_order)
            self.assertEqual(correct_order, order)


if __name__ == '__main__':
    unittest.main()
