from model.lex_bfs_plus.DoublyLinkedList import DoublyLinkedList
from model.lex_bfs_plus.VertexState import VertexState
from model.lex_bfs_plus.interval import Interval
from model.lex_bfs_plus.node import Node
from typing import List, Dict


class Partition:
    def __init__(self, vertices: DoublyLinkedList[int]):
        self.vertices = vertices

        self.intervals: DoublyLinkedList[Interval[int]] = DoublyLinkedList()
        initial_interval = Node(Interval(vertices.first(), vertices.last()))
        self.intervals.prepend(initial_interval)
        self.vertex_states = {node.data: VertexState(initial_interval, node) for node in vertices}

    def is_not_empty(self) -> bool:
        return self.intervals.is_not_empty()

    def pop_first(self) -> int:
        interval_node = self.intervals.first()
        interval = interval_node.data

        vartex_node = interval.start
        vertex = vartex_node.data

        if interval.is_singleton():
            self.intervals.delete(interval_node)
        else:
            interval.pop_start()

        self.vertices.delete(vartex_node)
        self.vertex_states[vertex].interval = None

        return vertex

    def refine(self, pivot: List[int]):
        new_intervals: Dict[Node[Interval[int]], Node[Interval[int]]] = {}

        for vertex in pivot:
            vertex_interval_node = self.vertex_states[vertex].interval
            vertex_node = self.vertex_states[vertex].vertex_node

            new_interval_node = new_intervals.get(vertex_interval_node, None)

            if vertex_interval_node.data.is_singleton() and new_interval_node is None:
                continue

            self.__pop_from_interval(vertex_interval_node, vertex_node)

            if new_interval_node is None:
                new_interval_node = self.__append_to_new_interval(
                    vertex_node,
                    self.vertex_states[vertex],
                    vertex_interval_node)

                new_intervals[vertex_interval_node] = new_interval_node

            else:
                self.__append_to_existing_interval(
                    vertex_node,
                    self.vertex_states[vertex],
                    new_interval_node)

    def __pop_from_interval(self, interval_node: Node[Interval[int]], vertex_node: Node[int]):
        interval = interval_node.data

        if interval.is_singleton():
            self.intervals.delete(interval_node)
        else:
            interval.pop(vertex_node)

        self.vertices.delete(vertex_node)

    def __append_to_new_interval(
            self,
            vertex_node: Node[int],
            vertex_state: VertexState,
            original_interval_node: Node[Interval[int]]
    ) -> Node[Interval[int]]:

        new_interval_node = Node(Interval(vertex_node, vertex_node))
        self.intervals.insert_before(original_interval_node, new_interval_node)
        self.vertices.insert_before(original_interval_node.data.start, vertex_node)
        vertex_state.interval = new_interval_node

        return new_interval_node

    def __append_to_existing_interval(
            self,
            vertex_node: Node[int],
            vertex_state: VertexState,
            existing_interval_node: Node[Interval[int]]
    ):
        existing_interval = existing_interval_node.data
        existing_interval_end = existing_interval.end
        self.vertices.insert_behind(existing_interval_end, vertex_node)
        existing_interval.end = vertex_node
        vertex_state.interval = existing_interval_node
