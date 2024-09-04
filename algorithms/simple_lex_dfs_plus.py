from typing import List, Dict

from algorithms.simple_lex_something_plus import simple_lex_something_plus
from model.graph import Graph


def lex_dfs_update_strategy(label: List[int], n: int, i: int) -> List[int]:
    return [i] + label


def simple_lex_dfs_plus(graph: Graph, tie_breaking_order: List[int]) -> List[int]:
    """
        Performs the lexDFS+ algorithm on a graph using:

        - tie_breaking_order order of vertices as the tie-breaking rule (rightmost vertex wins)

        - rightmost vertex from tie_breaking_order as the starting vertex

        This implementation is in no way optimal. It's just used for testing.

        Returns:
            List[int]: search order of the vertices of the graph
    """
    return simple_lex_something_plus(graph, graph.n, tie_breaking_order, lex_dfs_update_strategy)
