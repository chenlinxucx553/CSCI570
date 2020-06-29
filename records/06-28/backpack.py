__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/28/2020 11:50 AM'

"""
https://blog.csdn.net/MrLevo520/article/details/75676160
"""

# 这里使用了图解中的吉他，音箱，电脑，手机做的测试，数据保持一致
weight = [0, 1, 4, 3, 1]  # n个物体的重量(w[0]无用)
value = [0, 1500, 3000, 2000, 2000]  # n个物体的价值(p[0]无用)
info = [(0, 0), (1, 1500), (4, 3000), (3, 2000), (1, 2000)]
threshold = 4  # 背包的载重量


def knapsack_dynamic(weight, price, limit):
    max_value, items = 0, []
    records = [[0 for __ in range(limit + 1)] for _ in range(len(weight))]

    for i in range(1, len(weight)):  # 物品一件件来
        for j in range(1, limit + 1):  # j为子背包的载重量，寻找能够承载物品的子背包
            if j >= weight[i]:  # 当物品的重量小于背包能够承受的载重量的时候，才考虑能不能放进去
                records[i][j] = max(records[i - 1][j],
                                    records[i - 1][j - weight[i]] + price[i])
                # records[i - 1][j]是上一个单元的值， records[i - 1][j - w[i]]为剩余空间的价值
            else:
                records[i][j] = records[i - 1][j]

    # 递推装入背包的物体,寻找跳变的地方，从最后结果开始逆推
    j = limit
    for i in range(len(weight) - 1, 0, -1):
        if records[i][j] > records[i - 1][j]:
            items.append(i)
            j = j - weight[i]

            # 返回最大价值，即表格中最后一行最后一列的值
    max_value = records[len(weight) - 1][limit]
    return max_value, items


amount, items = knapsack_dynamic(weight, value, threshold)
print(amount, items)

# 最大值为：4000
# 物品的索引： [4, 3]
