import networkx as nx
import os.path


class GenerationError(Exception):
    pass


def __get_internal_string_representation(graph: nx.Graph) -> str:
    n = len(graph.nodes)
    m = len(graph.edges)
    lines = [f'{n} {m}']
    for u, v in graph.edges:
        lines.append(f'{u} {v}')

    return "\n".join(lines)


def __generate_chordal(n: int) -> nx.Graph:
    graph = nx.cycle_graph(n)
    chordal_graph, _ = nx.complete_to_chordal_graph(graph)
    return chordal_graph


def __generate_connected(n: int) -> nx.Graph:
    graph = nx.erdos_renyi_graph(n, 0.5, seed=123, directed=False)
    retry_count = 10
    while retry_count > 0 and not nx.is_connected(graph):
        graph = nx.erdos_renyi_graph(n, 0.5, seed=123, directed=False)
        retry_count -= 1

    if retry_count <= 0:
        raise GenerationError("Unable to generate connected graphs. Please retry")

    return graph


chordal_subdirectory = 'chordal_graph_inputs'
connected_subdirectory = 'connected_graph_inputs'

try:
    os.mkdir(chordal_subdirectory)
    os.mkdir(connected_subdirectory)
except Exception as e:
    pass

for n in [5, 10, 20, 30, 50, 100, 250]:
    chordal_graph = __generate_chordal(n)
    connected_graph = __generate_connected(n)
    chordal_string_representation = __get_internal_string_representation(chordal_graph)
    connected_string_representation = __get_internal_string_representation(connected_graph)
    filename = f'{n}_nodes.txt'
    with open(os.path.join(chordal_subdirectory, filename), 'w') as file:
        file.write(chordal_string_representation)

    with open(os.path.join(connected_subdirectory, filename), 'w') as file:
        file.write(chordal_string_representation)
