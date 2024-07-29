import random

from model.graph import Graph


def shuffle_adj_lists(graph: Graph) -> None:
    for neighbours in graph.adj_list.values():
        random.shuffle(neighbours)
