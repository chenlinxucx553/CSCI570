__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/4/2020 4:26 PM'

import random

"""
核心思想： 分治法， 但跟递归方式的归并排序不同

迭代方式的归并排序， 直接将单个元素组合排列， 最后再将两个有序的结果再排序

迭代方式，从最小问题开始一步一步解决  直到复杂的问题
1. 划分每个子数组 元素的个数
2. 对每个相邻的数组进行排序, 然后对相邻的两个数组进行合并
    相邻两个数组的 通过[low: mid], [mid: high] 进行切分获得 

"""


def merge(arr, low, mid, high):
    left = arr[low: mid]
    right = arr[mid: high]
    k = 0
    j = 0
    result = []
    while k < len(left) and j < len(right):
        if left[k] <= right[j]:
            result.append(left[k])
            k += 1
        else:
            result.append(right[j])
            j += 1
    result += left[k:]
    result += right[j:]
    arr[low: high] = result


def merge2(arr, low, mid, high):
    left = arr[low: mid]
    right = arr[mid: high]
    res = []
    while left and right:
        min_val = left.pop(0) if left[0] < right[0] else right.pop(0)
        res.append(min_val)
    res += left if left else right
    arr[low: high] = res


def merge_iteration(arr):
    sub_length = 1
    while sub_length < len(arr):
        low = 0
        while low < len(arr):
            mid = low + sub_length  # mid前后均为有序
            high = min(low + 2 * sub_length, len(arr))
            if mid < high:
                merge2(arr, low, mid, high)
            low += 2 * sub_length
        sub_length *= 2
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr1 = merge_iteration(arr.copy())  # count -> 503 switch -> 467
    print(sorted_arr1)
