__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/30/2020 11:50 AM'


def bfs(graph, init_node):
    visited = [init_node]
    queue = [init_node]

    while len(queue) > 0:
        current = queue.pop(0)
        for connected_node in graph[current]:
            if connected_node not in visited:
                visited.append(connected_node)
                queue.append(connected_node)
    return visited


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

    for k, v in graph_dict.items():
        graph_dict[k] = list(v.keys())

    # {
    # 'A': ['B', 'D'],
    # 'B': ['A', 'C', 'D', 'E'],
    # 'C': ['B', 'E'],
    # 'D': ['A', 'B', 'E', 'F'],
    # 'E': ['B', 'C', 'D', 'F', 'G'],
    # 'F': ['D', 'E', 'G'],
    # 'G': ['E', 'F']
    # }

    path = bfs(graph_dict, "D")
    print(path)  # ['D', 'A', 'B', 'E', 'F', 'C', 'G']
