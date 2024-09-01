from typing import Dict, List


class Graph:
    """
    Represents an undirected graph with size n and vertices numbered from 0 to n-1.

    Attributes
    ----------
    n: int
        number of vertices in the graph

    adj_list: Dict[int, List[int]]
        a dictionary representing the adjacency list of the graph
    
    Methods
    -------
    add_edge(u: int, v: int)
        Adds an undirected edge between nodes u and v to the graph.

    reorder(order: List[int])
        Reorders the adjacency list of the graph according to the given order.
    """

    def __init__(self, n: int) -> None:
        """Initializes the graph with n vertices and an empty adjacency list."""
        self.n: int = n
        self.adj_list: Dict[int, List[int]] = {v: [] for v in range(n)}

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected edge between nodes u and v to the graph."""
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def reorder(self, order: List[int]) -> None:
        """Reorders the adjacency list of the graph according to the given order."""
        new_adj_list: Dict[int, List[int]] = {v: [] for v in range(self.n)}
        for u in reversed(order):
            neighbors = self.adj_list[u]
            for v in neighbors:
                new_adj_list[v].append(u)

        self.adj_list = new_adj_list

    def __str__(self) -> str:
        return str(self.adj_list)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Graph):
            return NotImplemented

        if self.n != other.n:
            return False

        for u in range(self.n):
            self_neighbors = self.adj_list[u]
            other_neighbors = other.adj_list[u]
            if set(self_neighbors) != set(other_neighbors):
                return False

        return True
