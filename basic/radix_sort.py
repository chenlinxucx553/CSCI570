__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/6/2020 5:58 PM'

import random


def radix_sort(arr):
    digit = 0
    max_digit = 1
    max_value = max(arr)

    while 10 ** max_digit < max_value:  # 找出列表中最大的位数
        max_digit += 1

    while digit < max_digit:
        buckets = [[] for _ in range(10)]
        for i in arr:
            # 求出每一个元素的个、十、百位的值
            num = int((i / 10 ** digit) % 10)
            buckets[num].append(i)

        temp_result = []
        for bucket in buckets:
            temp_result.extend(bucket)

        arr = temp_result
        digit += 1
    return arr


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr2 = radix_sort(arr.copy())  # count -> 503 switch -> 467
    print(sorted_arr2)
