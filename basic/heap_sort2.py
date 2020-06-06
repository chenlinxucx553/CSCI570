__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/5/2020 3:40 PM'

import random

"""
步骤： 1. 创建堆， 调整堆， 堆排序

创建堆，以数组的形式将堆中所有的数据重新排序，使其成为最大堆/最小堆。

调整堆，调整过程需要保证堆序性质：在一个二叉堆中任意父节点大于其子节点。

堆排序，取出位于堆顶的第一个数据（最大堆则为最大数，最小堆则为最小数），
放入输出数组B 中，再将剩下的对作调整堆的迭代/重复运算直至输入数组 A中只剩下最后一个元素。
"""


def OneHeapSort(arr, left, right):
    if right <= left:
        return
    if right - left == 1 and arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    else:
        mid = left + (right - left - 1) // 2
        OneHeapSort(arr, left, mid)
        OneHeapSort(arr, mid + 1, right - 1)
        if arr[mid] > arr[right]:
            arr[mid], arr[right] = arr[right], arr[mid]
        if arr[right - 1] > arr[right]:
            arr[right - 1], arr[right] = arr[right], arr[right - 1]


def heap_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        OneHeapSort(arr, 0, i)
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr2 = heap_sort(arr.copy())  # count -> 503 switch -> 467
    print(sorted_arr2)
