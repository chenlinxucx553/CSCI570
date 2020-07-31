__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/23/2020 11:48 AM'


def cmp(key1, key2):
    return (key1, key2) if key1 < key2 else (key2, key1)


def find_parent(record, node):
    if record[node] != node:
        record[node] = find_parent(record, record[node])
    return record[node]


def naive_union(record, edge):
    u, v = find_parent(record, edge[0]), find_parent(record, edge[1])
    record[u] = v


def kruskal(graph, init_node):
    edge_dict = {}
    for node in graph.keys():
        edge_dict.update({cmp(node, k): v for k, v in graph[node].items()})
    sorted_edge = list(sorted(edge_dict.items(), key=lambda kv: kv[1]))
    tree = []
    connected_records = {key: key for key in graph.keys()}

    for edge_pair, _ in sorted_edge:
        if find_parent(connected_records, edge_pair[0]) != \
                find_parent(connected_records, edge_pair[1]):
            tree.append(edge_pair)
            naive_union(connected_records, edge_pair)
    return tree


if __name__ == '__main__':
    graph_dict = {
        "A": {"B": 7, "D": 5},
        "B": {"A": 7, "C": 8, "D": 9, "E": 5},
        "C": {"B": 8, "E": 5},
        "D": {"A": 5, "B": 9, "E": 15, "F": 6},
        "E": {"B": 7, "C": 5, "D": 15, "F": 8, "G": 9},
        "F": {"D": 6, "E": 8, "G": 11},
        "G": {"E": 9, "F": 11}
    }

    path = kruskal(graph_dict, "D")
    print(path)  # [('A', 'D'), ('D', 'F'), ('A', 'B'), ('B', 'E'), ('C', 'E'), ('E', 'G')]

