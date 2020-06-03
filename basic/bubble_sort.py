__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/3/2020 11:24 AM'

import random

"""
核心思想： 同时遍历整个数组两次， 外层循环选定一个数， 内层循环进行比较和交换，
目标： 把最大值往后放
"""


def bubble_sort(arr):
    """
    内循环每次找最大的值， 放在后面
    区别： 内循环之间的交换
    :param arr:
    :return:
    """
    count = 0
    switch = 0
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            count += 1
            # print("({}, {}) -> arr : {}".format(i, j, arr))
            if arr[j] >= arr[j + 1]:
                switch += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("count : ", count)
    print("switch : ", switch)
    return arr


def bubble_flag(arr):
    """
    内循环每次找最大的值， 放在后面
    区别： 内循环之间的交换， 当在一次内循环中， 没有发生过交换，就直接退出
    :param arr:
    :return:
    """
    count = 0
    switch = 0
    for i in range(len(arr)):
        flag = 0
        for j in range(0, len(arr) - i - 1):
            count += 1
            # print("({}, {}) -> arr : {}".format(i, j, arr))
            if arr[j] >= arr[j + 1]:
                switch += 1
                flag += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if flag == 0:
            break
    print("count : ", count)
    print("switch : ", switch)
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr2 = bubble_sort(arr.copy())  # count -> 45 switch -> 23
    sorted_arr3 = bubble_flag(arr.copy())  # count -> 39 switch -> 23
    print(sorted_arr2)
    print(sorted_arr3)
