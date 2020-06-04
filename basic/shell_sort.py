__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/3/2020 9:34 PM'

import random

"""
核心思想：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序

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


def shell_sort(arr):
    """
    每次对比某一间隔的两个元素，如果前面的元素大了，那就交换， 后面的元素整体往后移，
    为新元素腾出位置
    :param arr:
    :return:
    □                    □
    |____________________|
    |<--------gap------->|
front_idx1        arr[i] = end_val1
        □                    □
        |____________________|
        |<--------gap------->|
    front_idx2        arr[i+1] = end_val2
    """
    count = 0
    switch = 0
    gap = len(arr) // 2
    while gap >= 1:
        for i in range(gap, len(arr)):
            count += 1
            end_val = arr[i]
            front_idx = i - gap
            # similar to direct insertion sort
            while front_idx >= 0 and arr[front_idx] > end_val:
                switch += 1
                arr[front_idx + gap] = arr[front_idx]
                front_idx -= gap
            arr[front_idx + gap] = end_val
        gap //= 2
    print("count : ", count)
    print("switch : ", switch)
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 100)
    sorted_arr1 = shell_sort(arr.copy())  # count -> 503 switch -> 467
    sorted_arr2 = insection_sort(arr.copy())  # count -> 2503 switch -> 2503
    sorted_arr3 = insection_binary(arr.copy())  # count -> 530 switch -> 2503
    print(sorted_arr1)
    print(sorted_arr2)
    print(sorted_arr2)
