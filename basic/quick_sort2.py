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


def quick_sort6(arr, left, right):
    if left < right:
        pivot = arr[right]
        low, high = left, right
        while left < right:

            while left < right and arr[left] < pivot:
                left += 1
            arr[right] = arr[left]
            while left < right and arr[right] > pivot:
                right -= 1
            arr[left] = arr[right]

        arr[left] = pivot
        quick_sort6(arr, low, left - 1)
        quick_sort6(arr, left + 1, high)
    return arr


def quick_sort5(arr, left, right):
    if left < right:
        pivot = arr[left]
        low, high = left, right
        while left < right:

            while left < right and arr[right] > pivot:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] < pivot:
                left += 1
            arr[right] = arr[left]

        arr[right] = pivot
        quick_sort5(arr, low, left - 1)
        quick_sort5(arr, left + 1, high)
    return arr


def quick_sort2(arr, left, right):
    if left >= right:
        return arr
    low = left
    high = right
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] > pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    arr[right] = pivot
    quick_sort2(arr, low, left - 1)
    quick_sort2(arr, left + 1, high)
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)

    quick_sort1 = lambda xs: ((len(xs) <= 1 and [xs]) or [
        quick_sort1([x for x in xs[1:] if x < xs[0]]) + [xs[0]] + quick_sort1([x for x in xs[1:] if x >= xs[0]])])[0]

    print(quick_sort1(arr))

    sorted_arr2 = quick_sort2(arr.copy(), 0, len(arr) - 1)  # count -> 503 switch -> 467
    print(sorted_arr2)

    sorted_arr5 = quick_sort6(arr.copy(), 0, len(arr) - 1)  # count -> 503 switch -> 467
    print(sorted_arr5)
