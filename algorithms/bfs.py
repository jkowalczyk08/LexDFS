from collections import deque
from typing import List

from model.graph import Graph


def bfs(graph: Graph, s: int) -> List[int]:
    result: List[int] = []
    queue = deque()
    visited = [False] * graph.n
    visited[s] = True
    queue.append(s)

    while queue:
        v = queue.popleft()
        result.append(v)
        for u in graph.adj_list[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)

    return result
