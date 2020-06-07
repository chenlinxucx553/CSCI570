__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/5/2020 9:52 PM'

import random

"""
将输入的数据值转化为键存储在额外开辟的数组空间中

计数排序要求输入的数据必须是有确定范围的整数
"""


def counting_sort(arr):
    max_val = max(arr) + 1
    counter = [0] * max_val  # a large number of 0
    sorted_idx = 0

    for i in range(len(arr)):
        counter[arr[i]] += 1

    for j in range(max_val):
        while counter[j] > 0:
            arr[sorted_idx] = j
            sorted_idx += 1
            counter[j] -= 1
    return arr


def counting_sort2(arr):
    max_val = max(arr) + 1
    counter = [0] * max_val  # a large number of 0
    sorted_idx = 0

    for i in range(len(arr)):
        counter[arr[i]] += 1

    for index, value in enumerate(counter):
        while value != 0:
            arr[sorted_idx] = index
            sorted_idx += 1
            value -= 1
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr2 = counting_sort2(arr.copy())  # count -> 503 switch -> 467
    print(sorted_arr2)
