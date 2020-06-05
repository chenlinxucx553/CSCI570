__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/4/2020 4:26 PM'

import random

"""
核心思想： 分治法， 递归地把当前序列平均分成两半， 分到只剩一个元素的时候， 停止切分
开始进行排序，当解决完N个小问题之后，就可以把结果再拼装起来
"""


def merge1(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    print("a : ", a)
    print("b : ", b)
    res = list()
    a_idx = b_idx = 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            res.append(a[a_idx])
            a_idx += 1
        else:
            res.append(b[b_idx])
            b_idx += 1

    if a_idx == len(a):
        res.extend(b[b_idx:])
    else:
        res.extend(a[a_idx:])

    return res


def merge2(left, right):
    res = []
    while left and right:
        min_val = left.pop(0) if left[0] < right[0] else right.pop(0)
        res.append(min_val)
    res += left if left else right
    return res


def merge_recursive(arr):
    """
    递归地把当前序列平均分成两半, 直到序列的长度为1
    :param arr:
    :return:
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_recursive(arr[:mid])
    right = merge_recursive(arr[mid:])
    return merge2(left, right)


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr1 = merge_recursive(arr.copy())  # count -> 503 switch -> 467
    print(sorted_arr1)
