from typing import List, Tuple
from algorithms.bfs import bfs
from algorithms.dfs_plus import dfs_plus
from model.graph import Graph
from model.lex_bfs_plus.DoublyLinkedList import DoublyLinkedList
from model.lex_bfs_plus.Partition import Partition
from model.lex_bfs_plus.node import Node


def reverse(order: List[int]) -> List[int]:
    return order[::-1]


def initialize_partition(n: int, s: int) -> Tuple[Partition, Node[int]]:
    vertices: DoublyLinkedList[int] = DoublyLinkedList()
    s_node: Node[int]

    for i in range(n):
        node = Node(i)
        vertices.append(node)
        if i == s:
            s_node = node

    return Partition(vertices), s_node


def get_positions(order: List[int]) -> List[int]:
    positions = [-1] * len(order)

    for position, vertex in enumerate(order):
        positions[vertex] = position

    return positions


def get_pivot_set(graph: Graph, reversed_bfs_order_positions: List[int], vertex: int) -> List[int]:
    pivot: List[int] = []
    vertex_position = reversed_bfs_order_positions[vertex]

    for neighbor in graph.adj_list[vertex]:
        if reversed_bfs_order_positions[neighbor] < vertex_position:
            pivot.append(neighbor)

    return pivot


def ordering(graph: Graph, last_in_tree: Graph, s: int, order: List[int]) -> List[int]:
    reversed_bfs_order = reverse(bfs(last_in_tree, s))
    reversed_bfs_order_positions = get_positions(reversed_bfs_order)
    partition, s_node = initialize_partition(graph.n, s)

    for vertex in reversed_bfs_order:
        pivot = get_pivot_set(graph, reversed_bfs_order_positions, vertex)
        partition.refine(pivot)

    partition.order_within_intervals(reverse(order))
    partition.move_to_front(s_node)
    reversed_vertices = reverse(partition.get_vertices())

    result = dfs_plus(graph, reversed_vertices)

    return result
