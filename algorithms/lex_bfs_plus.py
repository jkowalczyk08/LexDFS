from typing import List, Optional, Dict

from model.graph import Graph
from model.lex_bfs_plus.DoublyLinkedList import DoublyLinkedList
from model.lex_bfs_plus.VertexState import VertexState
from model.lex_bfs_plus.interval import Interval
from model.lex_bfs_plus.node import Node


def pop_neighbour_from_interval(
        vertices: DoublyLinkedList[int],
        intervals: DoublyLinkedList[Interval[int]],
        interval_node: Node[Interval[int]],
        neighbour_node: Node[int]):

    interval = interval_node.data

    if interval.is_singleton():
        intervals.delete(interval_node)
    else:
        interval.pop(neighbour_node)

    vertices.delete(neighbour_node)


def push_to_new_interval_partition(
        vertices: DoublyLinkedList[int],
        intervals: DoublyLinkedList[Interval[int]],
        neighbour_interval_node: Node[Interval[int]],
        neighbour_node: Node[int],
        neighbour_state: VertexState) -> Node[Interval[int]]:

    interval_partition_node = Node(Interval(neighbour_node, neighbour_node))
    intervals.insert_before(neighbour_interval_node, interval_partition_node)
    vertices.insert_before(neighbour_interval_node.data.start, neighbour_node)
    neighbour_state.interval = interval_partition_node

    return interval_partition_node


def push_to_existing_interval_partition(
        vertices: DoublyLinkedList[int],
        interval_partition_node: Node[Interval[int]],
        neighbour_node: Node[int],
        neighbour_state: VertexState):

    interval_partition = interval_partition_node.data
    interval_partition_end = interval_partition.end
    vertices.insert_behind(interval_partition_end, neighbour_node)
    interval_partition.end = neighbour_node
    neighbour_state.interval = interval_partition_node


def lex_bfs_plus(graph: Graph, n: int, tie_breaking_order: List[int]) -> List[int]:
    """
        Performs the lexBFS+ algorithm on a graph using:

        - tie_breaking_order order as the tie-breaking rule (rightmost vertex wins)

        - rightmost vertex from tie_breaking_order as the starting vertex

        This implementation uses partition refinement, to find the lexBFS+ search order in linear time.

        Returns:
            List[int]: search order of the vertices of the graph
    """
    vertices: DoublyLinkedList[int] = DoublyLinkedList()
    intervals: DoublyLinkedList[Interval[int]] = DoublyLinkedList()
    result: List[int] = []

    graph.reorder(tie_breaking_order)

    for vertex in tie_breaking_order:
        vertices.prepend(Node(vertex))

    initial_interval = Node(Interval(vertices.safe_first(), vertices.safe_last()))
    intervals.prepend(initial_interval)

    vertex_states = {node.data: VertexState(initial_interval, node) for node in vertices}

    while intervals.is_not_empty():
        interval_node = intervals.safe_first()
        interval = interval_node.data

        pivot_node = interval.start
        pivot = pivot_node.data

        if interval.is_singleton():
            intervals.delete(interval_node)
        else:
            interval.pop_start()

        vertex_states[pivot].visited = True
        vertex_states[pivot].interval = None
        vertices.delete(pivot_node)
        result.append(pivot)

        interval_partitions: Dict[Node[Interval[int]], Node[Interval[int]]] = {}

        for neighbour in graph.adj_list[pivot]:
            if vertex_states[neighbour].visited is True:
                continue

            neighbour_interval_node = vertex_states[neighbour].interval
            neighbour_node = vertex_states[neighbour].vertex_node

            interval_partition_node = interval_partitions.get(neighbour_interval_node, None)

            if neighbour_interval_node.data.is_singleton() and interval_partition_node is None:
                continue

            pop_neighbour_from_interval(
                vertices,
                intervals,
                neighbour_interval_node,
                neighbour_node)

            if interval_partition_node is None:
                interval_partition_node = push_to_new_interval_partition(
                    vertices,
                    intervals,
                    neighbour_interval_node,
                    neighbour_node,
                    vertex_states[neighbour])

                interval_partitions[neighbour_interval_node] = interval_partition_node

            else:
                push_to_existing_interval_partition(
                    vertices,
                    interval_partition_node,
                    neighbour_node,
                    vertex_states[neighbour])

    return result
