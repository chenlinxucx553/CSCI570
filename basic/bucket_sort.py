__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/5/2020 10:08 PM'

import random


def bucket_sort(arr):
    buckets = [0] * ((max(arr) - min(arr)) + 1)
    for i in range(len(arr)):
        buckets[arr[i] - min(arr)] += 1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i + min(arr)] * buckets[i]
    return res


if __name__ == '__main__':
    # random.seed(666)
    arr = random.sample(range(0, 100000), 10)
    sorted_arr2 = bucket_sort(arr.copy())  # count -> 503 switch -> 467
    print(sorted_arr2)
