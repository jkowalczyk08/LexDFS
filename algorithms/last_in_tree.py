from typing import List
from model.graph import Graph


def find_rightmost_visited_neighbour(neighbours: List[int], positions: List[int]) -> int:
    rightmost_visited_neighbour: int | None = None
    position = -1

    for vertex in neighbours:
        if positions[vertex] > position:
            position = positions[vertex]
            rightmost_visited_neighbour = vertex

    return rightmost_visited_neighbour


def last_in_tree(graph: Graph, order: List[int]) -> Graph:
    tree = Graph(graph.n)
    positions = [-1] * graph.n

    for position, vertex in enumerate(order):
        positions[vertex] = position
        neighbours = graph.adj_list[vertex]
        rightmost_visited_neighbour = find_rightmost_visited_neighbour(neighbours, positions)
        if rightmost_visited_neighbour is not None:
            tree.add_edge(vertex, rightmost_visited_neighbour)

    return tree
