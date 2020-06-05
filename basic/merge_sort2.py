__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/4/2020 4:26 PM'

import random

"""
核心思想： 分治法， 但跟递归方式的归并排序不同

迭代方式的归并排序， 直接将单个元素组合排列， 最后再将两个有序的结果再排序

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


def merge_iteration(arr):
    step = 1
    while step < len(arr):
        low = 0
        while low < len(arr):
            mid = low + step  # mid前后均为有序
            high = min(low + 2 * step, len(arr))
            if mid < high:
                merge(arr, low, mid, high)
            low += 2 * step
        step *= 2
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr1 = merge_iteration(arr.copy())  # count -> 503 switch -> 467
    print(sorted_arr1)
