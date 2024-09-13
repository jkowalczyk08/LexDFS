from typing import List, Tuple
from model.graph import Graph
from model.partition.DoublyLinkedList import DoublyLinkedList
from model.partition.Partition import Partition
from model.partition.node import Node


def prepare_initial_algorithm_state(
        graph: Graph,
        tie_breaking_order: List[int]
) -> Tuple[Partition, List[int], List[bool]]:

    vertices: DoublyLinkedList[int] = DoublyLinkedList()
    graph.reorder(tie_breaking_order)
    for vertex in tie_breaking_order:
        vertices.prepend(Node(vertex))

    partition = Partition(vertices)
    result: List[int] = []
    visited = [False] * graph.n

    return partition, result, visited


def get_unvisited_neighbors(vertex: int, graph: Graph, visited: List[bool]) -> List[int]:
    partition_refinement_pivot: List[int] = []
    for neighbor in graph.adj_list[vertex]:
        if not visited[neighbor]:
            partition_refinement_pivot.append(neighbor)

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
    partition, result, visited = prepare_initial_algorithm_state(
        graph,
        tie_breaking_order)

    while partition.is_not_empty():
        current_vertex = partition.pop_first()

        visited[current_vertex] = True
        result.append(current_vertex)

        pivot = get_unvisited_neighbors(current_vertex, graph, visited)

        partition.refine(pivot)

    return result
