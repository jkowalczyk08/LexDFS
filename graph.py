from typing import Dict, List

class Graph:
    """
    Represents an undirected graph with a fixed number of vertices.

    Attributes
    ----------
    n: int
        number of vertices in the graph

    adj_list: Dict[int, List[int]]
        a dictionary representing the adjecency list of the graph

    Methods
    -------
    add_edge(u: int, v: int)
        Adds an undirected edge between nodes u and v to the graph. 
    """

    def __init__(self, n: int) -> None:
        """Initializes the graph with n vertices and an empty adjecency list."""
        self.n: int = n
        self.adj_list: Dict[int, List[int]] = {v : [] for v in range(n)}

    def add_edge(self, u: int, v: int) -> None:
        """Adds an undirected edge between nodes u and v to the graph."""
        self.adj_list.append(v)
        self.adj_list.append(u)

    def __str__(self) -> str:
        return str(self.adj_list)