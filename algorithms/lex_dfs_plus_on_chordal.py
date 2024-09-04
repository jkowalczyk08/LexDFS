from typing import List

from algorithms.last_in_tree import last_in_tree
from algorithms.lex_bfs_plus import lex_bfs_plus
from algorithms.ordering import ordering
from model.graph import Graph


def lex_dfs_plus_on_chordal(graph: Graph, tie_breaking_order: List[int]) -> List[int]:
    """
        Performs the lexDFS+ algorithm on a chordal graph in linear time using:

        - tie_breaking_order order as the tie-breaking rule (rightmost vertex wins)

        - rightmost vertex from tie_breaking_order as the starting vertex

        Returns:
            List[int]: search order of the vertices of the graph
    """
    s = tie_breaking_order[-1]
    lex_bfs_plus_order = lex_bfs_plus(graph, tie_breaking_order)
    tree = last_in_tree(graph, lex_bfs_plus_order)
    lex_dfs_order = ordering(graph, tree, s, tie_breaking_order)

    return lex_dfs_order
