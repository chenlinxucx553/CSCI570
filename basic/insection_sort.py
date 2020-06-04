__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/3/2020 11:24 AM'

import random

"""
核心思想： 同时遍历整个数组两次， 外层循环选定一个数，构造有序数组， 内层循环不断向有序数组
中插入内容
优化： 折半插入排序，由于前半部分为已排好序的数列，
这样我们不用按顺序依次寻找插入点，可以采用折半查找的方法来加快寻找插入点的速度
"""


def insection_sort(arr):
    """
    内循环 遍历之前已经排序好的数组，把值插在合适的位置
    :param arr:
    :return:
    """
    count = 0
    switch = 0
    for i in range(len(arr)):
        prev_idx = i - 1
        current = arr[i]
        while prev_idx >= 0 and arr[prev_idx] > current:
            count += 1
            switch += 1
            arr[prev_idx + 1] = arr[prev_idx]
            prev_idx -= 1
        arr[prev_idx + 1] = current
    print("count : ", count)
    print("switch : ", switch)
    return arr


def insection_binary(arr):
    """
    内循环 通过折半查找的方式，插入新的值，不像之前的全遍历一遍
    :param arr:
    :return:
    """
    count = 0
    switch = 0
    for i in range(len(arr)):
        low, high = 0, i - 1
        current = arr[i]

        # 折半查找对应的index
        while low <= high:
            count += 1
            mid = int((low + high) / 2)
            if current < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # 将[low, i] 的值 依次往后移一位
        # 为什么不能正序移位， 因为在不申请多余空间的条件下，
        # 正序移位造成前面的值把后面的值覆盖
        for j in range(i, low, -1):
            switch += 1
            arr[j] = arr[j - 1]
        # 把新加进来的值 放在空出来的位置
        arr[low] = current
    print("count : ", count)
    print("switch : ", switch)
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 100)
    sorted_arr1 = insection_sort(arr.copy())  # count -> 2219 switch -> 2219
    sorted_arr2 = insection_binary(arr.copy())  # count -> 535 switch -> 2219
    print(sorted_arr1)
    print(sorted_arr2)
