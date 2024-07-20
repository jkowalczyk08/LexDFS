from enum import Enum
from typing import List

from algorithms.lex_bfs_plus import lex_bfs_plus
from algorithms.simple_lex_bfs_plus import simple_lex_bfs_plus
from model.graph import Graph


class Mode(Enum):
    ALL = 0,
    SIMPLE_LEX_BFS_PLUS = 1,
    LEX_BFS_PLUS = 2


def create_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        n, m = map(int, first_line.split())

        graph = Graph(n)

        for _ in range(m):
            line = file.readline().strip()
            u, v = map(int, line.split())
            graph.add_edge(u, v)

    return graph


mode: Mode = Mode.ALL
graph: Graph = create_graph_from_file('inputs/250_nodes.txt')
n = graph.n
tie_breaking_order: List[int] = [i for i in range(n)]

print(f'graph: {graph}')

if mode == Mode.ALL or mode == Mode.SIMPLE_LEX_BFS_PLUS:
    simple_lex_bfs_plus_order = simple_lex_bfs_plus(graph, n, tie_breaking_order)
    print(f'simple_lex_bfs_plus_order: {simple_lex_bfs_plus_order}')

if mode == Mode.ALL or mode == Mode.LEX_BFS_PLUS:
    lex_bfs_plus_order = lex_bfs_plus(graph, n, tie_breaking_order)
    print(f'lex_bfs_plus_order: {lex_bfs_plus_order}')

if mode == Mode.ALL:
    print(simple_lex_bfs_plus_order == lex_bfs_plus_order)