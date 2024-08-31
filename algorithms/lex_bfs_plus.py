from typing import List, Optional, Dict, Tuple

from model.graph import Graph
from model.lex_bfs_plus.DoublyLinkedList import DoublyLinkedList
from model.lex_bfs_plus.VertexState import VertexState
from model.lex_bfs_plus.interval import Interval
from model.lex_bfs_plus.node import Node


def pop_neighbour_from_interval(
        vertices: DoublyLinkedList[int],
        intervals: DoublyLinkedList[Interval[int]],
        interval_node: Node[Interval[int]],
        neighbour_node: Node[int]
):
    interval = interval_node.data

    if interval.is_singleton():
        intervals.delete(interval_node)
    else:
        interval.pop(neighbour_node)

    vertices.delete(neighbour_node)


def push_to_new_interval(
        vertices: DoublyLinkedList[int],
        intervals: DoublyLinkedList[Interval[int]],
        neighbour_interval_node: Node[Interval[int]],
        neighbour_node: Node[int],
        neighbour_state: VertexState
) -> Node[Interval[int]]:

    interval_partition_node = Node(Interval(neighbour_node, neighbour_node))
    intervals.insert_before(neighbour_interval_node, interval_partition_node)
    vertices.insert_before(neighbour_interval_node.data.start, neighbour_node)
    neighbour_state.interval = interval_partition_node

    return interval_partition_node


def push_to_existing_interval(
        vertices: DoublyLinkedList[int],
        interval_partition_node: Node[Interval[int]],
        neighbour_node: Node[int],
        neighbour_state: VertexState
):
    interval_partition = interval_partition_node.data
    interval_partition_end = interval_partition.end
    vertices.insert_behind(interval_partition_end, neighbour_node)
    interval_partition.end = neighbour_node
    neighbour_state.interval = interval_partition_node


def partition_refinement(
        vertices: DoublyLinkedList[int],
        intervals: DoublyLinkedList[Interval[int]],
        vertex_states: Dict[int, VertexState],
        pivot: List[int]
):
    new_intervals: Dict[Node[Interval[int]], Node[Interval[int]]] = {}

    for neighbour in pivot:
        neighbour_interval_node = vertex_states[neighbour].interval
        neighbour_node = vertex_states[neighbour].vertex_node

        interval_partition_node = new_intervals.get(neighbour_interval_node, None)

        if neighbour_interval_node.data.is_singleton() and interval_partition_node is None:
            continue

        pop_neighbour_from_interval(vertices, intervals, neighbour_interval_node, neighbour_node)

        if interval_partition_node is None:
            interval_partition_node = push_to_new_interval(
                vertices,
                intervals,
                neighbour_interval_node,
                neighbour_node,
                vertex_states[neighbour])

            new_intervals[neighbour_interval_node] = interval_partition_node

        else:
            push_to_existing_interval(
                vertices,
                interval_partition_node,
                neighbour_node,
                vertex_states[neighbour])


def prepare_initial_algorithm_state(
        graph: Graph,
        tie_breaking_order: List[int]
) -> Tuple[DoublyLinkedList[int], DoublyLinkedList[Interval[int]], Dict[int, VertexState], List[int], List[bool]]:

    vertices: DoublyLinkedList[int] = DoublyLinkedList()
    intervals: DoublyLinkedList[Interval[int]] = DoublyLinkedList()
    result: List[int] = []
    visited = [False] * graph.n

    graph.reorder(tie_breaking_order)

    for vertex in tie_breaking_order:
        vertices.prepend(Node(vertex))

    initial_interval = Node(Interval(vertices.first(), vertices.last()))
    intervals.prepend(initial_interval)

    vertex_states = {node.data: VertexState(initial_interval, node) for node in vertices}

    return vertices, intervals, vertex_states, result, visited


def pop_first_from_partition(intervals: DoublyLinkedList[Interval[int]], vertices: DoublyLinkedList[int], vertex_states: Dict[int, VertexState]) -> int:
    interval_node = intervals.first()
    interval = interval_node.data

    vartex_node = interval.start
    vertex = vartex_node.data

    if interval.is_singleton():
        intervals.delete(interval_node)
    else:
        interval.pop_start()

    vertices.delete(vartex_node)
    vertex_states[vertex].interval = None

    return vertex


def get_unvisited_neighbours(vertex: int, graph: Graph, visited: List[bool]) -> List[int]:
    partition_refinement_pivot: List[int] = []
    for neighbour in graph.adj_list[vertex]:
        if not visited[neighbour]:
            partition_refinement_pivot.append(neighbour)

    return partition_refinement_pivot


def lex_bfs_plus(graph: Graph, tie_breaking_order: List[int]) -> List[int]:
    """
        Performs the lexBFS+ algorithm on a graph using:

        - tie_breaking_order order as the tie-breaking rule (rightmost vertex wins)

        - rightmost vertex from tie_breaking_order as the starting vertex

        This implementation uses partition refinement, to find the lexBFS+ search order in linear time.

        Returns:
            List[int]: search order of the vertices of the graph
    """
    vertices, intervals, vertex_states, result, visited = prepare_initial_algorithm_state(graph, tie_breaking_order)

    while intervals.is_not_empty():
        current_vertex = pop_first_from_partition(intervals, vertices, vertex_states)

        visited[current_vertex] = True
        result.append(current_vertex)

        pivot = get_unvisited_neighbours(current_vertex, graph, visited)

        partition_refinement(vertices, intervals, vertex_states, pivot)

    return result
