from typing import List, Dict
from model.graph import Graph


def largest_unnumbered_label(n: int, label: List[str], is_numbered: List[bool], tie_breaking_order_map: Dict[int, int]) -> int:
    max_node = 0
    max_label = ""
    for i in range(n):
        if is_numbered[i]:
            continue

        if label[i] > max_label:
            max_node = i
            max_label = label[i]
        elif label[i] == max_label:
            if tie_breaking_order_map[i] > tie_breaking_order_map[max_node]:
                max_node = i
                max_label = label[i]

    return max_node


def simple_lex_bfs_plus(graph: Graph, n: int, tie_breaking_order: List[int]) -> List[int]:
    """
        Performs the lexBFS+ algorithm on a graph using:

        - tie_breaking_order order of vertices as the tie-breaking rule (rightmost vertex wins)

        - rightmost last vertex from tie_breaking_order as the starting vertex

        This implementation is in no way optimal. It's just used for testing.

        Returns:
            List[int]: search order of the vertices of the graph
    """
    tie_breaking_order_map = {vertex: position for position, vertex in enumerate(tie_breaking_order)}
    label = [""] * n
    order = [-1] * n
    is_numbered = [False] * n
    s: int = largest_unnumbered_label(n, label, is_numbered, tie_breaking_order_map)
    label[s] = str(n)

    for i in range(n):
        v = largest_unnumbered_label(n, label, is_numbered, tie_breaking_order_map)
        order[i] = v
        is_numbered[v] = True
        for w in graph.adj_list[v]:
            if not is_numbered[w]:
                label[w] = label[w] + str(n - i - 1)
    return order
