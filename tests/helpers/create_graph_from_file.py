from model.graph import Graph


def create_graph_from_file(file_path) -> Graph:
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        n, m = map(int, first_line.split())

        graph = Graph(n)

        for _ in range(m):
            line = file.readline().strip()
            u, v = map(int, line.split())
            graph.add_edge(u, v)

    return graph
