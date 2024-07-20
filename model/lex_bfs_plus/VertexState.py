from model.lex_bfs_plus.interval import Interval
from model.lex_bfs_plus.node import Node


class VertexState:
    def __init__(self, interval: Node[Interval[int]], node: Node[int]):
        self.visited: bool = False
        self.interval: Node[Interval[int]] = interval
        self.vertex_node: Node[int] = node

    def __str__(self):
        return f'visited: {str(self.visited)}, interval: {str(self.interval)}, vertex_node: {str(self.vertex_node)}'
