G = {
    0: {},
    1: {1: 1, 2: 2},
    2: {1: 1, 3: 6, 4: 11},
    3: {1: 2, 2: 6, 4: 9, 5: 13},
    4: {2: 11, 3: 9, 5: 7, 6: 3},
    5: {3: 13, 4: 7, 6: 4},
    6: {4: 3, 5: 4},
}

# G = {
#
#         "A": {"B": 7, "D": 5},
#         "B": {"A": 7, "C": 8, "D": 9, "E": 5},
#         "C": {"B": 8, "E": 5},
#         "D": {"A": 5, "B": 9, "E": 15, "F": 6},
#         "E": {"B": 7, "C": 5, "D": 15, "F": 8, "G": 9},
#         "F": {"D": 6, "E": 8, "G": 11},
#         "G": {"E": 9, "F": 11}
#     }
'''
Kruskal算法
各种变量：
C：形如{u1:v1,u2:v2,....}的字典，主要用来寻找代表节点(祖先节点)。初始化，v1=u1,v2=u2....
如a-b-c-d {a:a,b:a,c:b,d:c}
G：图
E：列表，存放着形如(e,u,v)的字典，e：权值，u：源点，v：目标点
'''


def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]


def naive_union(C, u, v):
    u, v = find(C, u), find(C, v)
    # u的祖先节点指向v的祖先节点
    C[u] = v


def kruskal(G):
    E = [(G[u][v], u, v) for u, _ in enumerate(G) for v in G[u]]
    # [(1, 1, 1), (2, 1, 2), (1, 2, 1), (6, 2, 3), ...
    print(E)
    T = set()
    C = {u: u for u, _ in enumerate(G)}  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):  # 边的源点的祖先不等于边的目的祖先（因为相等的话说明该点已经添加过了，否则为默认值）
            T.add((u, v))  # 添加
            naive_union(C, u, v)  # 合并，使目标节点变成生成树的一部分（修改其祖先）。
    return T


# ------测试结果---------
sum_count = 0
T = kruskal(G)
for k, v in T:
    sum_count += G[k][v]
print(sum_count)
print(sorted([i for i in T], key=lambda x: x[1]))
# 结果为19
# [(1, 2), (1, 3), (3, 4), (5, 6), (4, 6)]
# 以下为完成后的中间变量，便于理解
# C={0: 0, 1: 3, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6}
