__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/3/2020 11:24 AM'

import random

"""
核心思想： 同时遍历整个数组两次， 外层循环选定一个数， 内层循环进行比较和交换，
目标： 把最小值往前放
优化： 通过记录最小值标签，减少交换的次数，比较次数还是一样的
"""


def selection_sort(arr):
    """
    内循环 每次寻找最小的值， 放在前面
    区别： 内外循环之间的交换
    :param arr:
    :return:
    """
    count = 0
    switch = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            count += 1
            # print("({}, {}) -> arr : {}".format(i, j, arr))
            if arr[i] > arr[j]:
                switch += 1
                arr[i], arr[j] = arr[j], arr[i]
    print("count : ", count)
    print("switch : ", switch)
    return arr


def selection_index(arr):
    """
    区别： 内外循环之间的交换， 记录下标，减少交换
    :param arr:
    :return:
    """
    count = 0
    switch = 0
    for i in range(len(arr)):
        min_idx = i  # save the index who point to the min value
        for j in range(i, len(arr)):
            count += 1
            # print("({}, {}) -> arr : {}".format(i, j, arr))
            if arr[min_idx] > arr[j]:
                min_idx = j
        if i != min_idx:
            switch += 1
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print("count : ", count)
    print("switch : ", switch)
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr1 = selection_sort(arr.copy())  # count -> 55 switch -> 30
    sorted_arr2 = selection_index(arr.copy())  # count -> 55 switch -> 6
    print(sorted_arr1)
    print(sorted_arr2)
