import unittest
import os

from algorithms.lex_bfs_plus import lex_bfs_plus
from algorithms.simple_lex_bfs_plus import simple_lex_bfs_plus
from model.graph import Graph
from tests.helpers.create_graph_from_file import create_graph_from_file
from tests.helpers.shuffle_helper import shuffle_adj_lists


def build_test_graph(graph: Graph) -> None:
    graph.add_edge(0, 5)
    graph.add_edge(0, 8)
    graph.add_edge(0, 3)
    graph.add_edge(5, 8)
    graph.add_edge(5, 9)
    graph.add_edge(5, 6)
    graph.add_edge(8, 6)
    graph.add_edge(8, 1)
    graph.add_edge(3, 9)
    graph.add_edge(6, 2)
    graph.add_edge(9, 2)
    graph.add_edge(9, 1)
    graph.add_edge(2, 4)
    graph.add_edge(2, 7)
    graph.add_edge(7, 4)


def build_small_test_graph(graph: Graph) -> None:
    graph.add_edge(4, 3)
    graph.add_edge(4, 2)
    graph.add_edge(4, 1)
    graph.add_edge(3, 1)
    graph.add_edge(1, 0)


class Test(unittest.TestCase):
    def test_singleton_graph(self):
        tie_breaking_order = [0]
        correct_order = [0]
        n = 1
        graph = Graph(n)
        order = lex_bfs_plus(graph, tie_breaking_order)
        self.assertEqual(correct_order, order)

    def test_lex_bfs_plus_with_small_graph(self):
        tie_breaking_order = [0, 1, 2, 3, 4]
        correct_order = [4, 3, 1, 2, 0]
        n = 5
        graph = Graph(n)
        build_small_test_graph(graph)
        for i in range(10):
            shuffle_adj_lists(graph)
            order = lex_bfs_plus(graph, tie_breaking_order)
            self.assertEqual(correct_order, order)

    def test_lex_bfs_plus(self):
        tie_breaking_order = [5, 6, 3, 8, 1, 9, 4, 7, 2, 0]
        correct_order = [0, 8, 5, 3, 6, 1, 9, 2, 7, 4]
        n = 10
        graph = Graph(n)
        build_test_graph(graph)
        for i in range(10):
            shuffle_adj_lists(graph)
            order = lex_bfs_plus(graph, tie_breaking_order)
            self.assertEqual(correct_order, order)

    def test_lex_bfs_plus_5_nodes(self):
        self.__run_test_on_n_nodes(5)

    def test_lex_bfs_plus_10_nodes(self):
        self.__run_test_on_n_nodes(10)

    def test_lex_bfs_plus_20_nodes(self):
        self.__run_test_on_n_nodes(20)

    def test_lex_bfs_plus_30_nodes(self):
        self.__run_test_on_n_nodes(30)

    def test_lex_bfs_plus_50_nodes(self):
        self.__run_test_on_n_nodes(50)

    def test_lex_bfs_plus_100_nodes(self):
        self.__run_test_on_n_nodes(100)

    def test_lex_bfs_plus_250_nodes(self):
        self.__run_test_on_n_nodes(250)

    def __run_test_on_n_nodes(self, n: int):
        test_dir = os.path.dirname(__file__)
        input_dir = os.path.join(test_dir, '..', 'connected_graph_inputs')
        input_file_path = os.path.join(input_dir, f'{n}_nodes.txt')
        graph = create_graph_from_file(input_file_path)
        tie_breaking_order = list(range(n))
        for i in range(10):
            shuffle_adj_lists(graph)
            order = lex_bfs_plus(graph, tie_breaking_order)
            correct_order = simple_lex_bfs_plus(graph, tie_breaking_order)
            self.assertEqual(correct_order, order)


if __name__ == '__main__':
    unittest.main()
