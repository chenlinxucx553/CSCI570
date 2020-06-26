__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/25/2020 12:07 PM'

import heapq


def dijkstra(graph, init_node):
    primary_queue = []
    heapq.heappush(primary_queue, (0, init_node))
    # the reason why i need to use this heap is because
    # i want to take advantage of its automatic sorting

    result = dict.fromkeys(graph.keys(), 123131)
    result[init_node] = 0

    while len(primary_queue) > 0:
        cost, start = heapq.heappop(primary_queue)

        for end in graph[start].keys():
            if result[start] + graph[start][end] < result[end]:
                # dist[j] = min(dist[j], dist[i] +  weight[i][j])
                heapq.heappush(primary_queue, (result[start] + graph[start][end], end))
                result[end] = result[start] + graph[start][end]

    return result


if __name__ == '__main__':
    graph_dict = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6},
    }

    distance = dijkstra(graph_dict, "A")
    print(distance)
