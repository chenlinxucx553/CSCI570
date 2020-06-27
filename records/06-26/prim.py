__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/26/2020 11:42 AM'


def cmp(key1, key2):
    return (key1, key2) if key1 < key2 else (key2, key1)


def prim(graph, init_node):
    visited = {init_node}
    candidate = set(graph.keys())
    candidate.remove(init_node)  # add all nodes into candidate set, except the start node
    tree = []

    while len(candidate) > 0:
        edge_dict = dict()
        for node in visited:  # find all visited nodes
            for connected_node, weight in graph[node].items():  # find those were connected
                if connected_node in candidate:
                    edge_dict[cmp(connected_node, node)] = weight
        edge, cost = sorted(edge_dict.items(), key=lambda kv: kv[1])[0]  # find the minimum cost edge
        tree.append(edge)
        visited.add(edge[0])  # cause you dont know which node will be put in the first place
        visited.add(edge[1])
        candidate.discard(edge[0]) # same reason. discard wont raise an exception.
        candidate.discard(edge[1])
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

    path = prim(graph_dict, "D")
    print(path)  # [('A', 'D'), ('D', 'F'), ('A', 'B'), ('B', 'E'), ('C', 'E'), ('E', 'G')]
