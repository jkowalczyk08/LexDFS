from typing import List

from model.graph import Graph


def dfs_plus_util(graph: Graph, v: int, visited: List[bool], result: List[int]):
    visited[v] = True
    result.append(v)
    for u in graph.adj_list[v]:
        if not visited[u]:
            dfs_plus_util(graph, u, visited, result)


def dfs_plus(graph: Graph, order: List[int]) -> List[int]:
    graph.reorder(order)
    result: List[int] = []
    visited = [False] * graph.n
    s = order[-1]
    dfs_plus_util(graph, s, visited, result)

    return result
