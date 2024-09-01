from typing import List
from model.graph import Graph


def find_rightmost_visited_neighbor(neighbors: List[int], positions: List[int]) -> int:
    rightmost_visited_neighbor: int | None = None
    position = -1

    for vertex in neighbors:
        if positions[vertex] > position:
            position = positions[vertex]
            rightmost_visited_neighbor = vertex

    return rightmost_visited_neighbor


def last_in_tree(graph: Graph, order: List[int]) -> Graph:
    tree = Graph(graph.n)
    positions = [-1] * graph.n

    for position, vertex in enumerate(order):
        positions[vertex] = position
        neighbors = graph.adj_list[vertex]
        rightmost_visited_neighbor = find_rightmost_visited_neighbor(neighbors, positions)
        if rightmost_visited_neighbor is not None:
            tree.add_edge(vertex, rightmost_visited_neighbor)

    return tree
