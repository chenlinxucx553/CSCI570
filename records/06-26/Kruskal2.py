__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/26/2020 4:20 PM'

"""
将每个顶点放入其自身的数据集中，然后按照权重的升序来选择边。
当选择每条边时，判断定义边的顶点是否在不同的数据集中。如果是，
将此边插入最小生成树的集合中，将集合中包含每个顶点的联合体取出
"""


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
