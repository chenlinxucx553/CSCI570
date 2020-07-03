__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/30/2020 10:27 AM'

import itertools

"""
https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
"""


def topological_sort(graph):
    in_degree_dict = dict.fromkeys(graph.keys(), 0)
    flattened_values = list()  # ['B', 'C', 'A', 'C', 'D', 'A'...
    [flattened_values.extend(value) for value in graph.values()]
    for key, group in itertools.groupby(sorted(flattened_values), lambda x: x):
        in_degree_dict[key] = len(list(group))

    result = list()
    if not all(list(map(lambda val: val >= 1, in_degree_dict.values()))):
        # if not all in degree values greater than 1
        # = at least one degree equals to 0, continue or stop
        candidates = [key for key in in_degree_dict if in_degree_dict[key] == 0]
        while len(candidates) > 0:
            candidate = candidates.pop()
            result.append(candidate)
            for node in graph[candidate]:
                in_degree_dict[node] -= 1

            in_degree_dict.pop(candidate)
            candidates.extend([key for key in in_degree_dict if in_degree_dict[key] == 0])
    else:
        print("U need build a graph with one node in-degree equals 0 at least")
    return result


if __name__ == '__main__':
    graph_dict = {
        "A": {"B": 5, "D": 1},
        "B": {"C": 2, "D": 1},
        "C": {"E": 8},
        "D": {"C": 4, "E": 3},
        "E": {}
    }

    for k, v in graph_dict.items():
        graph_dict[k] = list(v.keys())

    # {
    # 'A': ['B', 'C'],
    # 'B': ['A', 'C', 'D'],
    # 'C': ['A', 'B', 'D', 'E'],
    # 'D': ['B', 'C', 'E', 'F'],
    # 'E': ['C', 'D'],
    # 'F': ['D']
    # }

    path = topological_sort(graph_dict)
    print(path)
