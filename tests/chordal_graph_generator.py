import networkx as nx
import os.path


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


subdirectory = 'chordal_graph_inputs'

try:
    os.mkdir(subdirectory)
except Exception:
    pass

for n in [5, 10, 11, 12, 13, 14, 15, 20, 30, 50, 100, 250]:
    graph = __generate_chordal(n)
    string_representation = __get_internal_string_representation(graph)
    filename = f'{n}_nodes.txt'
    with open(os.path.join(subdirectory, filename), 'w') as file:
        file.write(string_representation)
