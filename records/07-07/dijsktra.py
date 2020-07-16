__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/7/2020 9:43 AM'

import heapq
import math

def dijkstra(graph, init_node):
    pqueue = []
    heapq.heappush(pqueue, (0, init_node))  # min heap, sort data item automatically
    visited = set()  # actually you dont have to use this.
    weight = dict.fromkeys(graph.keys(), math.inf)
    weight[init_node] = 0
    connection_dict = {init_node: "Path: Start From -> "}  # save connection records

    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)  # Pop the smallest item off the heap
        cost, start = pair[0], pair[1]
        visited.add(start)
        for end in graph[start].keys():
            if end not in visited and cost + graph[start][end] < weight[end]:
                # dist[j] = min(dist[j], dist[i] +  weight[i][j])
                heapq.heappush(pqueue, (cost + graph[start][end], end))
                connection_dict[end] = start
                weight[end] = cost + graph[start][end]

    return {v: k for k, v in connection_dict.items()}, weight


if __name__ == '__main__':
    graph_dict = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6},
    }

    path, distance = dijkstra(graph_dict, "A")
    print(path) # {'Path: Start From -> ': 'A', 'C': 'B', 'A': 'C', 'B': 'D', 'D': 'F'}
    print(distance) # {'A': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 7, 'F': 10}
