import unittest
import os

from algorithms.lex_dfs_plus_on_chordal import lex_dfs_plus_on_chordal
from algorithms.simple_lex_dfs_plus import simple_lex_dfs_plus
from model.graph import Graph
from tests.helpers.create_graph_from_file import create_graph_from_file
from tests.helpers.shuffle_helper import shuffle_adj_lists


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
    def test_lex_dfs_plus_from_paper(self):
        tie_breaking_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        n = 11
        graph = Graph(n)
        build_test_graph(graph)
        for i in range(10):
            shuffle_adj_lists(graph)
            order = lex_dfs_plus_on_chordal(graph, tie_breaking_order)
            correct_order = simple_lex_dfs_plus(graph, tie_breaking_order)
            self.assertEqual(correct_order, order)

    def test_lex_dfs_plus_5_nodes(self):
        self.__run_test_on_n_nodes(5)

    def test_lex_dfs_plus_10_nodes(self):
        self.__run_test_on_n_nodes(10)

    def test_lex_dfs_plus_20_nodes(self):
        self.__run_test_on_n_nodes(20)

    def test_lex_dfs_plus_30_nodes(self):
        self.__run_test_on_n_nodes(30)

    def test_lex_dfs_plus_50_nodes(self):
        self.__run_test_on_n_nodes(50)

    def test_lex_dfs_plus_100_nodes(self):
        self.__run_test_on_n_nodes(100)

    def test_lex_dfs_plus_250_nodes(self):
        self.__run_test_on_n_nodes(250)

    def __run_test_on_n_nodes(self, n: int):
        test_dir = os.path.dirname(__file__)
        input_dir = os.path.join(test_dir, '..', 'chordal_graph_inputs')
        input_file_path = os.path.join(input_dir, f'{n}_nodes.txt')
        graph = create_graph_from_file(input_file_path)
        tie_breaking_order = list(range(n))
        for i in range(10):
            shuffle_adj_lists(graph)
            order = lex_dfs_plus_on_chordal(graph, tie_breaking_order)
            correct_order = simple_lex_dfs_plus(graph, tie_breaking_order)
            self.assertEqual(correct_order, order)


if __name__ == '__main__':
    unittest.main()
