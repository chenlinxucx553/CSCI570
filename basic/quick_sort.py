__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/5/2020 10:56 AM'

"""
快速排序应该算是在冒泡排序基础上的递归分治法

设当前待排序序列为R[low:high]，其中low ≤ high，
如果待排序的序列规模足够小，则直接进行排序，否则分3步处理。
    1. 在R[low:high]中选定一个元素R[pivot]，
    以此为标准将要排序的序列划分为两个序列R[low:pivot-1]与R[pivot+1：high]，
    并使序列R[low:pivot-1]中所有元素的值小于等于R[pivot]，序列R[pivot+1：high]
    所有的值大于R[pivot]，此时基准元素以位于正确位置，它无需参加后续排序。
    
    2. 对于子序列R[low:pivot-1]与R[pivot+1：high]，分别调用快速排序算法来进行排序。
    
    3. 由于对序列R[low:pivot-1]与R[pivot+1：high]的排序是原地进行的，
    所以R[low:pivot-1]与R[pivot+1：high]都已经排好序后，
    不需要进行任何计算，就已经排好序。
"""

import random


def quick_sort3(arr, left, right):
    if left < right:
        pivot_idx = split(arr, left, right)
        quick_sort3(arr, left, pivot_idx - 1)
        quick_sort3(arr, pivot_idx + 1, right)
    return arr


def split(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = pivot, arr[i + 1]
    return i + 1  # the index of pivot


def quick_sort4(arr):
    if arr:
        pivot = arr[0]
        less = [x for x in arr if x < pivot]
        great = [x for x in arr[1:] if x >= pivot]
        return quick_sort4(less) + [pivot] + quick_sort4(great)
    else:
        return []


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr3 = quick_sort3(arr.copy(), 0, len(arr) - 1)  # count -> 503 switch -> 467
    sorted_arr4 = quick_sort4(arr)
    print(sorted_arr3)
    print(sorted_arr4)
