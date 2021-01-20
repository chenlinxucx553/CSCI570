__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '1/5/2021 10:45 AM'


class Solution:
    def calcEquation(self, equations, values, queries):
        # 构造图，equations的第一项除以第二项等于value里的对应值，第二项除以第一项等于其倒数
        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        # dfs找寻从s到t的路径并返回结果叠乘后的边权重即结果
        def dfs(start, end) -> int:
            if start not in graph:
                return -1
            if end == start:
                return 1

            for node in graph[start].keys():
                if node == end:
                    return graph[start][node]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, end)
                    if v != -1:
                        return graph[start][node] * v
            return -1

        # 逐个计算query的值
        res = []
        for A, B in queries:
            visited = set()
            res.append(dfs(A, B))
        return res


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

Solution().calcEquation(equations, values, queries)
