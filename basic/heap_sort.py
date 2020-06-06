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

通常堆是通过一维数组来实现的。在阵列起始位置为0的情况中
(1)父节点i的左子节点在位置(2*i+1);
(2)父节点i的右子节点在位置(2*i+2);
(3)子节点i的父节点在位置floor((i-1)/2);

"""


def heapify(arr, size, root_idx):
    largest_idx = root_idx
    left_node_idx = 2 * root_idx + 1
    right_node_idx = 2 * root_idx + 2

    if left_node_idx < size and arr[largest_idx] < arr[left_node_idx]:
        largest_idx = left_node_idx

    if right_node_idx < size and arr[largest_idx] < arr[right_node_idx]:
        largest_idx = right_node_idx

    if largest_idx != root_idx:
        arr[root_idx], arr[largest_idx] = arr[largest_idx], arr[root_idx]

        heapify(arr, size, largest_idx)


def heap_sort(arr):
    for i in range(len(arr), -1, -1):
        heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        # 将根节点取出与最后一位做对调，
        # 对前面len-1个节点继续进行对调整过程。
        # why switch? see this
        # https://user-images.githubusercontent.com/24391143/83936114-14312a00-a775-11ea-8bb0-5d90ee5d7ff9.jpg
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr2 = heap_sort(arr.copy())  # count -> 503 switch -> 467
    print(sorted_arr2)
