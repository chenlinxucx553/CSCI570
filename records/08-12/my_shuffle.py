__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/12/2020 8:36 PM'

import random


def shuffle(l):
    tmp = list()
    for _ in range(0, len(l)):
        r = random.randint(0, len(l) - 1)
        tmp.append(l[r])
        l.remove(l[r])
    return tmp

def shuffle2(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i + 1)

        arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 2, 32, 32]

    print(shuffle2(arr))
