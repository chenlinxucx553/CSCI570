__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/3/2020 9:34 PM'

import random


def shell_sort(arr):
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

        for j in range(i, low, -1):
            switch += 1
            arr[j] = arr[j - 1]
        arr[low] = current
    print("count : ", count)
    print("switch : ", switch)
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 100)
    sorted_arr1 = shell_sort(arr.copy())  # count -> 2219 switch -> 2219
    # sorted_arr2 = insection_binary(arr.copy())  # count -> 535 switch -> 2219
    print(sorted_arr1)
    # print(sorted_arr2)
