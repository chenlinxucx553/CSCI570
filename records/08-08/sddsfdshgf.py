__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/8/2020 5:11 PM'

import itertools


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


class Solution:

    def alienOrder(self, words) -> str:
        # 每个字母代表图的一个顶点
        # 邻接表表示有向图

        graph = {}

        # 构建图顶点
        for word in words:
            for w in word:
                if w not in graph:
                    graph[w] = []

        # 两两单词进行比较，确定图的方向
        for i in range(len(words) - 1):
            j = 0
            while j < len(words[i]) and j < len(words[i + 1]):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].append(words[i + 1][j])
                    break
                j += 1

        # 拓扑排序输出字母顺序
        in_degrees = {}
        topo_result = []
        for k in graph:
            in_degrees[k] = 0  # 初始化顶点入度为0

        for values in graph.values():
            for value in values:
                in_degrees[value] += 1  # 计算每个顶点的入度

        zeros = [k for (k, v) in in_degrees.items() if v == 0]
        dequeues = []  # 出队元素
        while zeros:
            node = zeros.pop()
            dequeues.append(node)
            topo_result.append(node)
            for value in graph[node]:
                in_degrees[value] -= 1  # 删除该入度为0的节点后，该节点指向的节点入度减1
                if in_degrees[value] == 0:
                    zeros.append(value)

        # 判断非法顺序(判断有向图是否有环)
        is_unval = False
        if len(dequeues) != len(graph):  # 出队元素个数不等于图顶点个数，说明有环
            is_unval = True

        # abc 排在 ab前面，也属于非法输入。。。。
        for i in range(len(words) - 1):
            if len(words[i]) > len(words[i + 1]) and words[i][:len(words[i + 1])] == words[i + 1]:
                is_unval = True
                break

        if is_unval:
            return ""
        # 无法判断顺序的返回随机顺序
        if not is_unval and topo_result == []:
            return "".join([k for k in graph])
        return "".join(topo_result)


ss = [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]
print(Solution().alienOrder(ss))
