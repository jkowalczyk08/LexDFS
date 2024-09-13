import random

from model.graph import Graph


def shuffle_adj_lists(graph: Graph) -> None:
    for neighbors in graph.adj_list:
        random.shuffle(neighbors)
