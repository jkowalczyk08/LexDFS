from model.lex_bfs_plus.interval import Interval
from model.lex_bfs_plus.node import Node


class VertexState:
    def __init__(self, interval_node: Node[Interval[int]], vertex_node: Node[int]):
        self.interval_node: Node[Interval[int]] = interval_node
        self.vertex_node: Node[int] = vertex_node

    def __str__(self):
        return f'interval: {str(self.interval_node)}, vertex_node: {str(self.vertex_node)}'
