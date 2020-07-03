__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/30/2020 11:46 AM'

graph = {'A': ['B', 'D'], 'B': ['A', 'C', 'D', 'E'], 'C': ['B', 'E'], 'D': ['A', 'B', 'E', 'F'], 'E': ['B', 'C', 'D', 'F', 'G'], 'F': ['D', 'E', 'G'], 'G': ['E', 'F']}



def bfs(graph, node):
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
bfs(graph, 'D')
