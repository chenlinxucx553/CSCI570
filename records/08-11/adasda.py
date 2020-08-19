__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/11/2020 6:29 PM'

import sys


def get_num_of_one(num):
    count = 0
    for i in bin(num)[2:]:
        if i == '1':
            count += 1
    return count


def has_same_one(val, size):
    val_size = get_num_of_one(val)
    if val_size >= size:
        return val_size, True
    else:
        return 0, False


def find_same_one(num):
    size = get_num_of_one(num)
    min_val = int('0b1' + ''.join(['0' for _ in range(len(bin(num)[2:]) - 1)]), 2)
    temp = []
    for val in range(min_val, num):
        val_size, flag = has_same_one(val, size)
        if flag:
            temp.append((val_size, val))

    return temp


def format(arr):
    for val in arr:
        print(val)


while True:
    try:
        T = int(sys.stdin.readline().strip())

        res = []
        for _ in range(T):
            # 读取每一行
            num = int(sys.stdin.readline().strip())
            ll = sorted(find_same_one(num), key=lambda item: (item[0], -item[1]))
            res.append(ll[0][1])

        format(res)


    except:
        break
