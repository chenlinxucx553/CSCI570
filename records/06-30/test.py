__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/30/2020 10:34 AM'

"""
https://zhuanlan.zhihu.com/p/69858335
"""

def topoSort(graph):
    in_degrees = dict((u,0) for u in graph)   #初始化所有顶点入度为0
    num = len(in_degrees)
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1    #计算每个顶点的入度
    Q = [u for u in in_degrees if in_degrees[u] == 0]   # 筛选入度为0的顶点
    Seq = []
    while Q:
        u = Q.pop()       #默认从最后一个删除
        Seq.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1    #移除其所有出边
            if in_degrees[v] == 0:
                Q.append(v)          #再次筛选入度为0的顶点
    if len(Seq) == num:       #输出的顶点数是否与图中的顶点数相等
        return Seq
    else:
        return None

G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}
print(topoSort(G))